#!/usr/bin/env python3
"""
Verify CHANGELOG.md's stated entry dates against the actual GitHub commit
dates that introduced each entry.

Run inside a git clone of the repo:
    python datecheck.py

For each commit that touched CHANGELOG.md, finds any "## X.Y — YYYY-MM-DD"
lines added in that commit's diff. Two things are tracked separately per
version: the date of the EARLIEST commit to introduce that version's line
(when it actually shipped) and the stated date from the MOST RECENT commit
to touch that line (what the entry currently says, after any correction).
The two are compared -- not "did the original text match its own commit,"
which would falsely re-flag every entry a later correction commit fixed,
and not "does the latest commit's date match its own text," which would
miss a real drift on any entry a correction commit never touched.

Note: commit date != author date in general, but for commits made via
GitHub's web upload flow (which is this repo's normal workflow), both are
server-stamped at upload time and should agree. Uses committer date
(%cI), since that's what GitHub's UI displays and what actually matters
for "when did this become public."
"""

import re
import subprocess
import sys

ENTRY_RE = re.compile(r"^\+## (\d+\.\d+) — (\d{4}-\d{2}-\d{2})")

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8").stdout

# One log call, full patches, for CHANGELOG.md only, oldest first
log = run([
    "git", "log", "--follow", "--reverse",
    "--date=iso-strict",
    "--pretty=format:@@COMMIT@@%H@@%cI@@%s",
    "-p", "--", "CHANGELOG.md",
])

if not log.strip():
    print("No commits found touching CHANGELOG.md. Wrong directory?")
    sys.exit(1)

commits = log.split("@@COMMIT@@")[1:]  # first split chunk is empty
mismatches = []
checked = 0

ship_commit = {}    # version -> (date, hash) of the EARLIEST commit to
                     # introduce this version's header line -- this is when
                     # the version actually shipped, regardless of any later
                     # edits to the entry's text.
latest_text = {}     # version -> stated_date from the MOST RECENT commit to
                     # touch this header line -- this is what the entry
                     # currently says, after any corrections.

for chunk in commits:
    header, _, body = chunk.partition("\n")
    commit_hash, commit_date_iso, subject = header.split("@@", 2)
    commit_date = commit_date_iso[:10]  # YYYY-MM-DD

    for line in body.splitlines():
        m = ENTRY_RE.match(line)
        if m:
            version, stated_date = m.groups()
            if version not in ship_commit:
                ship_commit[version] = (commit_date, commit_hash[:8])
            latest_text[version] = stated_date

for version in sorted(ship_commit, key=lambda v: [int(p) for p in v.split(".")]):
    ship_date, ship_hash = ship_commit[version]
    stated_date = latest_text[version]
    checked += 1
    status = "OK" if stated_date == ship_date else "MISMATCH"
    marker = "  " if status == "OK" else "!!"
    print(f"{marker} v{version:<8} stated={stated_date}  "
          f"shipped={ship_date}  ({ship_hash})  {status}")
    if status == "MISMATCH":
        mismatches.append((version, stated_date, ship_date, ship_hash))

print(f"\n{checked} changelog entries checked.")
if mismatches:
    print(f"\n{len(mismatches)} MISMATCHES:")
    for version, stated, actual, h in mismatches:
        print(f"  v{version}: changelog says {stated}, GitHub committed it {actual}  ({h})")
    sys.exit(1)
else:
    print("All changelog dates match their commit dates.")
    sys.exit(0)
