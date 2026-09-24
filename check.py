#!/usr/bin/env python3
"""
Integrity checks for the timeline document.

Enforces the invariants that have historically broken under manual review:
version drift, table arithmetic, tripwire numbering and cross-references,
process commentary in the body, and document growth.

Run: python3 check.py
Exit 0 = all pass. Exit 1 = at least one failure.
"""

import re
import sys
from pathlib import Path

DOC = Path("ai-timelines-and-outcomes.md")
LOG = Path("CHANGELOG.md")
README = Path("README.md")

WORD_CEILING = 7800  # drift guard; raise deliberately, never incidentally
# Raised 7000 -> 7400 at v1.27 (see prior comment below).
# Raised 7400 -> 7800 at v1.53. Reasoning: an external review (Opus 5.5)
# identified that repeated compression of the same passages (thermodynamics,
# Halstead, Soares, survivorship) had degraded them to the point of being
# unparseable by a new reader ("gross complements" unexplained, a one-line
# Soares paragraph, "The objection is survivorship" as a bare heading). The
# same review also required three substantive additions to fix real errors:
# a mathematical mistake in tripwire 3's bias-cancellation argument, a
# tripwire-stacking/monotonicity rule that didn't exist, and an
# acknowledgment that the outcome table's row sums contradict its own
# exhaustiveness disclaimer. Six further compression passes on already-tight
# prose yielded steeply diminishing savings before this raise, confirming
# the diagnosis rather than refuting it: the ceiling was no longer trading
# length for clarity, it was trading correctness and clarity for length.
# Margin is again left deliberately thin so the guard keeps binding.

# Phrases that indicate process commentary rather than current view.
# The maintenance rule itself names these, so that line is exempt.
BANNED = [
    "next revisit",
    "earlier version",
    "previous version",
    "this document should",
    "elsewhere in this document",
    "was missing until now",
    "corrected in v",
    "an earlier threshold",
    "false dichotomy",
    "second time this table",
    "recurring failure",
    "than this document does",
    "more than this document",
    "the +5 implied",
    "the +2 implied",
    "Reduced to +",
    "previous draft",
]
BANNED_EXEMPT = "No process commentary in the body"

failures = []
notes = []


def fail(msg):
    failures.append(msg)


def note(msg):
    notes.append(msg)


# ---------------------------------------------------------------- load
if not DOC.exists():
    print(f"FATAL: {DOC} not found")
    sys.exit(1)
if not LOG.exists():
    print(f"FATAL: {LOG} not found")
    sys.exit(1)

doc = DOC.read_text(encoding="utf-8")
log = LOG.read_text(encoding="utf-8")
readme = README.read_text(encoding="utf-8") if README.exists() else ""

# ---------------------------------------------------- 1. version match
m = re.search(r"\*\*Version (\d+\.\d+) — (\d{1,2} \w+ \d{4})\*\*", doc)
if not m:
    fail("Document header has no parseable '**Version X.Y — D Month YYYY**' line")
    doc_ver = None
else:
    doc_ver = m.group(1)
    note(f"Document version: {doc_ver} ({m.group(2)})")

# ------------------------------------- 1b. estimates-last-changed marker
em = re.search(r"Estimates last changed: v(\d+\.\d+)", doc)
if not em:
    fail("No 'Estimates last changed: vX.Y' marker in the header — the "
         "document version alone conflates content changes with numeric "
         "changes, which is exactly the ambiguity this marker exists to "
         "remove for anyone citing a figure.")
elif doc_ver:
    est_ver = em.group(1)
    est_tuple = [int(p) for p in est_ver.split(".")]
    doc_tuple = [int(p) for p in doc_ver.split(".")]
    if est_tuple > doc_tuple:
        fail(f"Estimates-last-changed marker (v{est_ver}) is newer than the "
             f"document's own version (v{doc_ver}) — that can't be right.")
    else:
        note(f"Estimates last changed: v{est_ver}"
             + (" (this version)" if est_ver == doc_ver else ""))

    # The marker now carries a date too ("v1.21 (17 September 2026)") --
    # cross-check it against that version's own changelog entry, so a
    # future edit can't update the version number without also updating
    # the date, or vice versa.
    dm = re.search(rf"Estimates last changed: v{re.escape(est_ver)} \((\d{{1,2}} \w+ \d{{4}})\)", doc)
    log_entry_date = re.search(rf"^## {re.escape(est_ver)} — (\d{{4}}-\d{{2}}-\d{{2}})", log, re.M)
    if dm and log_entry_date:
        # convert "17 September 2026" and "2026-09-17" to the same form for comparison
        import datetime
        marker_date = datetime.datetime.strptime(dm.group(1), "%d %B %Y").date()
        log_date = datetime.date.fromisoformat(log_entry_date.group(1))
        if marker_date != log_date:
            fail(f"Estimates marker shows v{est_ver} dated {dm.group(1)}, but "
                 f"the changelog dates v{est_ver} as {log_entry_date.group(1)} "
                 f"— one of these is stale.")
    elif not dm:
        fail(f"Estimates marker (v{est_ver}) has no readable "
             f"'(D Month YYYY)' date alongside the version number.")

    # README.md carries a copy of this same marker for visitors who never
    # open the full document -- the two must say the same thing, or the
    # README becomes exactly the kind of unsynced duplicate this whole
    # marker exists to prevent.
    if readme:
        rm = re.search(r"Estimates last changed: v[\d.]+ \([^)]+\)", readme)
        dm_full = re.search(r"Estimates last changed: v[\d.]+ \([^)]+\)", doc)
        if not rm:
            fail("README.md has no 'Estimates last changed' marker -- either "
                 "add one (kept in sync with the document's) or remove this "
                 "check if the README is no longer meant to carry it.")
        elif dm_full and rm.group(0) != dm_full.group(0):
            fail(f"README.md's estimates marker ({rm.group(0)!r}) does not "
                 f"match the document's ({dm_full.group(0)!r}).")
else:
    est_tuple = None

log_vers = re.findall(r"^## (\d+\.\d+) — (\d{4}-\d{2}-\d{2})", log, re.M)
if not log_vers:
    fail("CHANGELOG has no parseable '## X.Y — YYYY-MM-DD' entries")
else:
    newest = max(log_vers, key=lambda t: [int(p) for p in t[0].split(".")])
    note(f"Newest changelog entry: {newest[0]} ({newest[1]})")
    if est_tuple:
        since = sum(1 for v, _ in log_vers
                    if [int(p) for p in v.split(".")] > est_tuple)
        note(f"Versions published since the estimates marker: {since}")
    if doc_ver and doc_ver != newest[0]:
        fail(f"Version mismatch: document says {doc_ver}, newest changelog entry is {newest[0]}")

# --------------------------------------------- 2. outcome table midpoints
def midpoint(cell):
    nums = re.findall(r"(\d+(?:\.\d+)?)", cell.replace("–", "-"))
    if not nums:
        return None
    vals = [float(n) for n in nums]
    return sum(vals) / len(vals)


PCT = r"\s*\**\d+(?:\.\d+)?\s*[–-]\s*\d+(?:\.\d+)?%\**\s*"
rows = re.findall(
    rf"^\| ((?:Human-less RSI|Cognitive RSI|No closed-loop RSI)[^|]*?)\|({PCT})\|({PCT})\|({PCT})\|",
    doc, re.M)
if not rows:
    fail("Could not locate the outcome table rows")
else:
    note(f"Outcome table rows found: {len(rows)}")
    for label, a, b, c in rows:
        mids = [midpoint(x) for x in (a, b, c)]
        if any(x is None for x in mids):
            fail(f"Outcome row has an unparseable cell: {label.strip()}")
            continue
        total = sum(mids)
        short = label.strip()[:52]
        if not (95 <= total <= 105):
            fail(f"Row midpoints sum to {total:.1f}, outside 95-105: {short}")
        else:
            note(f"  {total:5.1f}  {short}")

# ------------------------------------------------ 3. tripwire numbering
tw = [int(n) for n in re.findall(r"^\| (\d+) \|", doc, re.M)]
if not tw:
    fail("No tripwire rows found")
else:
    uniq = sorted(set(tw))
    note(f"Tripwires: {len(uniq)} rows, 1-{max(uniq)}")
    if len(tw) != len(uniq):
        dupes = sorted({n for n in tw if tw.count(n) > 1})
        fail(f"Duplicate tripwire numbers: {dupes}")
    missing = [n for n in range(1, max(uniq) + 1) if n not in uniq]
    if missing:
        fail(f"Gaps in tripwire numbering: {missing}")
    if tw != sorted(tw):
        fail(f"Tripwires not in ascending file order: {tw}")

    refs = set()
    for chunk in re.findall(r"tripwires? ([\d, and]+)", doc, re.I):
        refs.update(int(x) for x in re.findall(r"\d+", chunk))
    unresolved = sorted(r for r in refs if r not in uniq)
    if unresolved:
        fail(f"Cross-reference to nonexistent tripwire(s): {unresolved}")
    elif refs:
        note(f"Cross-references resolve: {sorted(refs)}")

# --------------------------------------------- 4. no empty table cells
cog_rows = re.findall(r"^\| ([A-Z][^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|$",
                       doc.split("### Cognitive")[1].split("###")[0] if "### Cognitive" in doc else "",
                       re.M)
for label, c28, c30, c35 in cog_rows:
    for colname, cell in (("2028", c28), ("2030", c30), ("2035", c35)):
        if cell.strip() in ("—", "-", ""):
            fail(f'Empty cell ({colname}) in cognitive table row: {label.strip()[:50]} '
                 f'— use a value or an explicit "n/a", not a bare dash')
    m28, m30, m35 = midpoint(c28), midpoint(c30), midpoint(c35)
    if None not in (m28, m30, m35) and not (m28 <= m30 <= m35):
        fail(f"Non-monotonic 2028/2030/2035 midpoints in cognitive table row "
             f"'{label.strip()[:50]}': {m28:.1f} / {m30:.1f} / {m35:.1f} — "
             f"a later column reads lower than an earlier one")

# --------------------------------------------- 5. process commentary
body = doc.split("## Revision history")[0]
for phrase in BANNED:
    for line in body.splitlines():
        if phrase.lower() in line.lower() and BANNED_EXEMPT not in line:
            fail(f'Process commentary in body — "{phrase}": {line.strip()[:80]}...')
            break

# ------------------------------------------------------ 6. drift guard
words = len(doc.split())
note(f"Word count: {words} (ceiling {WORD_CEILING})")
if words > WORD_CEILING:
    fail(f"Document is {words} words, over the {WORD_CEILING} ceiling — cut, or raise the ceiling deliberately")

# ------------------------------------------- 7. required structure
for heading in ["## What this is", "## Definitions", "## Timeline estimates",
                "## Three pathways to loss of control", "## Governance",
                "## Tripwires", "## Maintenance"]:
    if heading.split(" ", 1)[1].lower() not in doc.lower():
        fail(f"Missing required section: {heading}")

if "CHANGELOG.md" not in doc:
    fail("Document does not point to CHANGELOG.md")

# ------------ newest changelog entry has a Files-changed list
if log_vers:
    newest_num = max(log_vers, key=lambda t: [int(p) for p in t[0].split(".")])[0]
    m = re.search(rf"^## {re.escape(newest_num)} — \d{{4}}-\d{{2}}-\d{{2}}\n(.*?)(?=\n## |\Z)", log, re.S | re.M)
    if m:
        entry_body = m.group(1)
        if "Files changed:" not in entry_body:
            fail(f"Newest changelog entry (v{newest_num}) has no Files changed: list.")
        if re.search(r"added?\s+(a\s+)?changelog entry\s+(for|to record)\s+this", entry_body, re.I):
            fail(f"Newest changelog entry (v{newest_num}) cites itself as its own reason.")

# ------------------------------- 8. references coverage
# LIMITATION: the source list below is hardcoded, so this catches a source
# being dropped from REFERENCES.md while still named in the document, but
# NOT a newly named source that was never added to either the list or the
# references file. Adding a source means adding it here too.
ref_path = Path("REFERENCES.md")
if ref_path.exists():
    refs_text = ref_path.read_text(encoding="utf-8")
    named = set(re.findall(
        r"\b(METR|Grace et al|Wang et al|Metaculus|Epoch|AI Futures|Dream-RSI|"
        r"SimpleTES|KataGo|Prime Intellect|RentAHuman|TC260|McAfee|Halstead|Kokotajlo)\b", doc))
    uncited = sorted(n for n in named if n not in refs_text)
    if uncited:
        fail(f"Source(s) named in the document but absent from REFERENCES.md: {uncited}")
    else:
        note(f"REFERENCES.md covers all {len(named)} named sources in the document")
else:
    fail("REFERENCES.md not found — externally checkable claims have no citation map")

# ------------------------------------------------------------ report
print("=" * 62)
for n in notes:
    print(f"  {n}")
print("=" * 62)
if failures:
    print(f"\nFAILED ({len(failures)}):\n")
    for f in failures:
        print(f"  ✗ {f}")
    print()
    sys.exit(1)
print("\nAll checks passed.\n")
sys.exit(0)
