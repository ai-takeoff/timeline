#!/usr/bin/env python3
"""
Check the external links in REFERENCES.md.

Run manually, or monthly via .github/workflows/linkcheck.yml.
Deliberately NOT part of check.py: link health is a different failure mode
from structural integrity, and a dead external link should not block a
commit that fixes a typo.

arXiv and DOI identifiers are treated as permanent and reported separately
rather than fetched — they are versioned and never rewritten in place.

Exit 0 = all reachable. Exit 1 = at least one failure.
"""

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REFS = Path("REFERENCES.md")
TIMEOUT = 20
UA = "Mozilla/5.0 (compatible; timeline-linkcheck/1.0)"

PERMANENT = ("arxiv.org/abs/", "doi.org/", "dx.doi.org/")

if not REFS.exists():
    print("FATAL: REFERENCES.md not found")
    sys.exit(1)

text = REFS.read_text(encoding="utf-8")
full_urls = re.findall(r"https?://[^\s)\]|>]+", text)
# Bare domain references ("aifuturesmodel.com,", "alignment.anthropic.com/2026/...")
# are legitimate citations the http(s):// pattern above misses entirely.
# Must handle subdomains (alignment.anthropic.com is two label segments plus
# the TLD, not one).
bare = re.findall(
    r"(?<![\w/.])(?:[a-z0-9][a-z0-9-]*\.)+(?:com|org|net|io)(?:/[^\s,;)\]|>\"']*)?",
    text)
urls = sorted(set(full_urls) | {"https://" + b for b in bare})
urls = [u.rstrip(".,;") for u in urls]

permanent = [u for u in urls if any(p in u for p in PERMANENT)]
checkable = [u for u in urls if u not in permanent]
archived = [u for u in urls if "web.archive.org" in u]

print(f"{len(urls)} URLs in REFERENCES.md")
print(f"  {len(permanent)} permanent identifiers (arXiv/DOI) — not fetched")
print(f"  {len(archived)} archive snapshots")
print(f"  {len(checkable)} live URLs to check\n")

# Only 404/410 mean the resource is gone. 403 and 429 are overwhelmingly
# anti-bot responses (Cloudflare and similar reject HEAD from unfamiliar
# user agents), and a network proxy will 403 everything indiscriminately.
# Reporting those as failures produces a monthly issue full of false
# alarms, which is how a maintenance job gets ignored.
DEAD = (404, 410)

failures, inconclusive = [], []


def fetch(url, method):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method=method)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.status


for url in checkable:
    code = None
    try:
        code = fetch(url, "HEAD")
    except urllib.error.HTTPError as e:
        code = e.code
        if code not in DEAD:
            try:  # some hosts reject HEAD but serve GET
                code = fetch(url, "GET")
            except urllib.error.HTTPError as e2:
                code = e2.code
            except Exception:
                pass
    except Exception as e:
        inconclusive.append((url, type(e).__name__))
        print(f"  ??   {type(e).__name__}  {url}")
        continue

    if code in DEAD:
        failures.append((url, f"HTTP {code}"))
        print(f"  DEAD {code}  {url}")
    elif code and code >= 400:
        inconclusive.append((url, f"HTTP {code}"))
        print(f"  ??   {code}  {url}  (likely anti-bot, not dead)")
    else:
        print(f"  ok   {code}  {url}")

# unstable sources should carry an archive snapshot
UNSTABLE_HINTS = ("substack.com", "blog.aifutures.org",  # Substack-hosted
                  # under a custom domain -- doesn't match "substack.com" as
                  # a substring, so it silently escaped the archive rule
                  # until listed explicitly
                  "truthsocial.com", "twitter.com", "x.com",
                  "rentahuman.ai", "medium.com")
unarchived = [u for u in checkable
              if any(h in u for h in UNSTABLE_HINTS)
              and f"web.archive.org" not in text.split(u)[1][:400]]
if unarchived:
    print("\nUnstable sources without an adjacent archive snapshot:")
    for u in unarchived:
        print(f"  {u}")

print()
if inconclusive:
    print(f"{len(inconclusive)} inconclusive (403/429/network) — verify by hand "
          f"before assuming anything is wrong:")
    for u, why in inconclusive:
        print(f"  {why}  {u}")
    print()

if failures:
    print(f"FAILED: {len(failures)} confirmed dead (404/410)")
    for u, why in failures:
        print(f"  {why}  {u}")
    sys.exit(1)

print("No confirmed dead links.")
sys.exit(0)
