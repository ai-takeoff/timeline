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

WORD_CEILING = 7400  # drift guard; raise deliberately, never incidentally
# Raised 7000 -> 7400 at v1.27. Reasoning: the ceiling guards against
# review-driven accretion (more rows, more caveats, more structure). This
# raise accommodates evidence-driven additions instead - external
# corroboration of the retraining-clock claim, a second tripwire anchored
# on coding uplift, and an explicit statement of what the estimates are
# conditional on. Cutting argumentative material to fit new evidence would
# be the wrong trade: the arguments are what make the numbers interpretable.
# Margin is deliberately thin (~125 words) so the guard still binds.

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
    "this document is estimating" if False else "more than this document",
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

doc = DOC.read_text()
log = LOG.read_text()

# ---------------------------------------------------- 1. version match
m = re.search(r"\*\*Version (\d+\.\d+) — (\d{1,2} \w+ \d{4})\*\*", doc)
if not m:
    fail("Document header has no parseable '**Version X.Y — D Month YYYY**' line")
    doc_ver = None
else:
    doc_ver = m.group(1)
    note(f"Document version: {doc_ver} ({m.group(2)})")

log_vers = re.findall(r"^## (\d+\.\d+) — (\d{4}-\d{2}-\d{2})", log, re.M)
if not log_vers:
    fail("CHANGELOG has no parseable '## X.Y — YYYY-MM-DD' entries")
else:
    newest = max(log_vers, key=lambda t: [int(p) for p in t[0].split(".")])
    note(f"Newest changelog entry: {newest[0]} ({newest[1]})")
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
raw_ids = re.findall(r"^\| (\d+[a-z]?) \|", doc, re.M)
if not raw_ids:
    fail("No tripwire rows found")
else:
    def parse(tid):
        m = re.match(r"(\d+)([a-z]?)", tid)
        return int(m.group(1)), m.group(2)

    parsed = [parse(t) for t in raw_ids]
    backbone = [n for n, suf in parsed if not suf]
    suffixed = [(n, suf) for n, suf in parsed if suf]
    note(f"Tripwires: {len(raw_ids)} rows — backbone 1-{max(backbone) if backbone else 0}"
         + (f", sub-rows {', '.join(f'{n}{s}' for n, s in suffixed)}" if suffixed else ""))

    if len(backbone) != len(set(backbone)):
        dupes = sorted({n for n in backbone if backbone.count(n) > 1})
        fail(f"Duplicate tripwire numbers: {dupes}")
    missing = [n for n in range(1, max(backbone) + 1) if n not in backbone] if backbone else []
    if missing:
        fail(f"Gaps in tripwire numbering: {missing}")
    if backbone != sorted(backbone):
        fail(f"Tripwire backbone not in ascending file order: {backbone}")

    # a sub-row (e.g. 2b) must sit immediately after its parent, or after an
    # earlier sub-row of the same parent
    for i, (n, suf) in enumerate(parsed):
        if not suf:
            continue
        if i == 0:
            fail(f"Sub-row {n}{suf} appears before any parent row")
            continue
        pn, psuf = parsed[i - 1]
        if pn != n:
            fail(f"Sub-row {n}{suf} does not immediately follow tripwire {n} "
                 f"(follows {pn}{psuf} instead)")

    uniq = sorted(set(backbone))
    refs = set()
    for chunk in re.findall(r"tripwires? ([\d, and]+)", doc):
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

# ------------------------------- 8. references coverage
# LIMITATION: the source list below is hardcoded, so this catches a source
# being dropped from REFERENCES.md while still named in the document, but
# NOT a newly named source that was never added to either the list or the
# references file. Adding a source means adding it here too.
ref_path = Path("REFERENCES.md")
if ref_path.exists():
    refs_text = ref_path.read_text()
    named = set(re.findall(
        r"\b(METR|Grace et al|Wang et al|Metaculus|Epoch|AI Futures|Dream-RSI|"
        r"SimpleTES|KataGo|Prime Intellect|RentAHuman|TC260|McAfee|Halstead)\b", doc))
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
