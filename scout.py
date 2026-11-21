#!/usr/bin/env python3
"""
scout.py (v3.1): weekly source scout for the ai-takeoff/timeline forecast.

It gathers candidate evidence; it decides nothing. Claude reads the digest and
checks primary sources before anything enters the document, and the maintainer
approves every change. The source list and keywords below are the scout's scope,
and so also its blind spots: proposals for sources and keywords are welcome.

Plain Python 3.9+, no AI involved. Standard library only, with one optional extra:
    pip install youtube-transcript-api     (needed for the video part; skipped if missing)

What it does:
  1. Reads lab and research feeds, Google News searches, arXiv searches, a few
     web pages without feeds, chosen YouTube channels, and YouTube searches.
  2. Keeps items in the time window that it has not reported on an earlier run.
  3. News and papers: scores by keywords, drops clear noise, groups duplicate stories.
  4. Videos: fetches transcripts locally and scores the *content*, not the title;
     keeps the best few, with the passages that matched and their timestamps.
  5. Watches a few pages for changes (e.g. the Vals RSI Index) and reports diffs.
  6. Writes digest.md, saves texts, and packs everything into one zip.

Usage:
    python scout.py                       # last 8 days
    python scout.py --days 14             # look further back
    python scout.py --since 2026-07-20    # one-time backfill from a date
    python scout.py --all                 # ignore memory of earlier runs
    python scout.py --quiet               # less progress output
    python scout.py --no-video            # skip YouTube entirely

Changes in v3.1: fewer transcript requests, spaced further apart, stopping early if
YouTube blocks them; reads feeds with a byte-order mark or compression; retries a
failed YouTube search once; reads YouTube's short dates ("3d ago").

Changes from v2: YouTube search; transcripts scored on content (with matched
passages); video descriptions read from channel feeds; duplicate stories grouped
by content as well as title; incident-disclosure news queries; page watches.
"""

import argparse, base64, datetime as dt, difflib, email.utils, html, json, re, sys, time, zipfile
import urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

VERSION = "v3.1"

# ----------------------------------------------------------------------------
# SOURCES: edit freely. A source that fails is reported in the digest; the run continues.
# ----------------------------------------------------------------------------
FEEDS = {
    "OpenAI news":            "https://openai.com/news/rss.xml",
    "Google DeepMind blog":   "https://deepmind.google/blog/rss.xml",
    "AI Futures Project":     "https://blog.ai-futures.org/feed",
    "Import AI (Jack Clark)": "https://importai.substack.com/feed",
    "Epoch AI":               "https://epoch.ai/atom.xml",
    "METR":                   "https://metr.org/feed.xml",
    "AI Alignment Forum":     "https://www.alignmentforum.org/feed.xml",
}

# Pages without a usable feed: collect links on the page whose path matches the pattern.
PAGES = {
    "Anthropic news":      ("https://www.anthropic.com/news",       r"^/news/[\w-]+$"),
    "Anthropic research":  ("https://www.anthropic.com/research",   r"^/research/[\w-]+$"),
    "METR research":       ("https://metr.org/research",            r"^/(blog|research|notes)/[\w/-]+$"),
    "METR home":           ("https://metr.org/",                    r"^/(blog|notes)/[\w/-]+$"),
    "OpenAI system cards": ("https://deploymentsafety.openai.com/", r"^/[a-z0-9][\w-]+$"),
    "UK AISI blog":        ("https://www.aisi.gov.uk/blog",         r"^/blog/[\w-]+$"),
}

# Pages watched for changes: the digest reports what changed since the last run.
WATCH = {
    "Vals RSI Index":          "https://www.vals.ai/benchmarks/rsi_index",
    "METR time horizons page": "https://metr.org/time-horizons/",
}

# Google News searches (free, no key).
NEWS_QUERIES = [
    '"AI research" automation lab',
    '"recursive self-improvement" AI',
    'METR "time horizon"',
    'AI agent owner "locked out" OR "no human owner" OR "keeps running"',
    'AI agent company OR LLC OR ruling "no human"',
    'frontier AI "safety framework" OR "scaling policy" threshold',
    'AI lab "system card"',
    'AI "security institute" evaluation incident',
    'AI model sabotage OR scheming OR exfiltration lab report',
    # v3: incident disclosures, which v2 missed
    'AI lab "misalignment" report OR disclosure',
    'AI agents "unexpected ways" OR unsanctioned OR unauthorized websites',
    'AI model "internet access" incident evaluation OR training',
]

# arXiv searches (Atom API).
ARXIV_QUERIES = [
    'abs:"automated AI research" OR abs:"AI R&D automation"',
    'abs:"time horizon" AND abs:agents',
]

# YouTube channels by handle (latest uploads, with descriptions).
YOUTUBE_HANDLES = [
    "@aiexplained-official",
    "@DwarkeshPatel",
    "@eightythousandhours",
    "@AI_In_Context",
    "@MachineLearningStreetTalk",
    "@aiDotEngineer",
]
# YouTube searches (recent uploads). These catch interviews on channels nobody listed.
YOUTUBE_SEARCHES = [
    "recursive self-improvement AI",
    "AI R&D automation",
    "METR time horizon",
    "AI lab safety incident",
    "superintelligence timeline interview",
    "Vals RSI index",
    "AI alignment research interview",
]
MAX_VIDEO_CANDIDATES = 25       # transcripts fetched and scored locally (costs nothing to read)
TRANSCRIPT_PAUSE = 6            # seconds between transcript requests; YouTube blocks bursts
MAX_BLOCKED_IN_ROW = 3          # stop asking for transcripts after this many blocks in a row
MAX_TRANSCRIPTS = 3             # best-scoring transcripts kept for review
MAX_TRANSCRIPT_WORDS = 15000    # longer ones keep matched passages only, not the full text
VIDEO_MIN_CORE = 3              # distinct core keywords a transcript needs to be kept
VIDEO_MIN_SCORE = 8

# Keywords. Weight 3 = core to the forecast's tripwires; 1 = broadly relevant.
KEYWORDS = {
    3: ["self-improv", "automated ai research", "ai research automation", "ai r&d",
        "research automation", "no human in the loop", "fully autonomous", "time horizon",
        "metr", "locked out", "no human owner", "controller-less", "keeps running",
        "takeoff", "superintelligen", "disempower", "extinction",
        "misalign", "scheming", "sabotage", "exfiltrat", "self-replicat", "rogue",
        "safety framework", "scaling policy", "preparedness framework", "frontier safety",
        "system card", "critical capability", "security institute", "aisi",
        "loss of control", "alignment", "unsanctioned", "unauthoriz", "sandbox",
        "rsi index"],
    1: ["agi", "agent", "agentic", "autonomous", "frontier model", "benchmark",
        "evaluation", "compute", "regulat", "export control", "executive order",
        "anthropic", "openai", "deepmind", "xai", "deepseek", "ai act", "incident"],
}
NOISE = ["raises $", "funding round", "series a", "series b", "series c", "valuation",
         "stock", "shares", "earnings", "price target", "investors", "ipo date",
         "launches", "partnership", "partners with", "customer", "enterprise",
         "smartphone", "deal", "acquire", "hiring", "webinar", "conference schedule"]
ORGS = ["anthropic", "openai", "deepmind", "google", "meta", "xai", "deepseek", "metr",
        "aisi", "security institute", "epoch", "microsoft", "nvidia", "vals"]
STOP = set("about after again against also among another because been before being between "
           "both could does doing during each from further have having here into itself just "
           "more most only other over same says said should since some such than that their "
           "them then there these they this those through under until very were what when "
           "where which while will with would your report reports new news".split())
MIN_SCORE = 4
MIN_SCORE_PRIMARY = 3        # lab feeds and lab pages: one core keyword is enough
NEWS_MIN_CORE = 1
MAX_FULLTEXT = 40
MAX_LOW_LIST = 120

UA = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")

# ----------------------------------------------------------------------------
# Slots for a local model (planned for v4, shadow mode first). Both do nothing now.
# ----------------------------------------------------------------------------
def local_triage(items):
    """Return (kept, dropped). Must only drop clearly off-topic items. Pass-through in v3."""
    return items, []

def local_label(item, text):
    """Return a short label such as 'new fact: ...' / 'opinion' / 'off-topic', or None."""
    return None

# ----------------------------------------------------------------------------
QUIET = False
T0 = time.time()
def log(msg, always=False):
    if always or not QUIET:
        print(f"[{time.time()-T0:6.1f}s] {msg}", flush=True)

MAX_BYTES = 5_000_000

def fetch(url, timeout=15, data=None, headers=None):
    log(f"  GET {url[:110]}" if data is None else f"  POST {url[:110]}")
    t = time.time()
    h = {"User-Agent": UA, "Accept-Language": "en"}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(MAX_BYTES)
            cs = r.headers.get_content_charset() or "utf-8"
            if body[:2] == b"\x1f\x8b" or r.headers.get("Content-Encoding", "") == "gzip":
                import gzip
                body = gzip.decompress(body)
    except Exception as e:
        log(f"    failed after {time.time()-t:.1f}s: {type(e).__name__}: {str(e)[:80]}")
        raise
    log(f"    ok {len(body)//1024} KB in {time.time()-t:.1f}s")
    return body.decode(cs, errors="replace").lstrip("\ufeff \r\n\t")

def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d

def parse_ago(s, now):
    """'3 days ago' / 'Streamed 2 weeks ago' -> approximate datetime, or None."""
    m = re.search(r"(\d+)\s*(seconds?|secs?|s|minutes?|mins?|m|hours?|hrs?|h|days?|d|"
                  r"weeks?|wks?|w|months?|mos?|years?|yrs?|y)\s+ago", (s or "").lower())
    if not m:
        return None
    n, u = int(m.group(1)), m.group(2)
    unit = ("month" if u.startswith("mo") else "minute" if u.startswith("mi") or u == "m"
            else {"s": "second", "h": "hour", "d": "day", "w": "week", "y": "year"}[u[0]])
    days = {"second": 1/86400, "minute": 1/1440, "hour": 1/24, "day": 1, "week": 7,
            "month": 30, "year": 365}[unit] * n
    return now - dt.timedelta(days=days)

def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s or "")).strip()

def local(tag):
    return tag.rsplit("}", 1)[-1]

def yt_url(video_id):
    return f"https://www.youtube.com/watch?v={video_id}"

def parse_feed(xml_text, source):
    root = ET.fromstring(xml_text)
    out = []
    for el in root.iter():
        if local(el.tag) not in ("item", "entry"):
            continue
        f = {local(c.tag): c for c in el}
        title = strip_tags(f["title"].text) if "title" in f and f["title"].text else ""
        link = ""
        if "link" in f:
            link = f["link"].get("href") or (f["link"].text or "")
        for c in el:
            if local(c.tag) == "link" and c.get("rel", "alternate") == "alternate" and c.get("href"):
                link = c.get("href")
        date = None
        for k in ("pubDate", "published", "updated", "date"):
            if k in f and f[k].text:
                date = parse_date(f[k].text); break
        summ = ""
        for k in ("description", "summary", "content"):
            if k in f and (f[k].text or "").strip():
                summ = strip_tags(f[k].text); break
        if not summ:                                    # YouTube: media:group/media:description
            for d in el.iter():
                if local(d.tag) == "description" and (d.text or "").strip():
                    summ = strip_tags(d.text); break
        pub = strip_tags(f["source"].text) if "source" in f and f["source"].text else ""
        vid = f["videoId"].text if "videoId" in f else None
        if vid:
            link = yt_url(vid)
        out.append(dict(source=source, title=title, link=link.strip(), date=date, publisher=pub,
                        summary=re.sub(r"\s+", " ", summ)[:600], video_id=vid))
    return out

class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self._a = None; self._txt = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._a = dict(attrs).get("href"); self._txt = []
    def handle_data(self, d):
        if self._a is not None: self._txt.append(d)
    def handle_endtag(self, tag):
        if tag == "a" and self._a:
            self.links.append((self._a, re.sub(r"\s+", " ", "".join(self._txt)).strip()))
            self._a = None

class TextExtractor(HTMLParser):
    SKIP = {"script", "style", "nav", "footer", "header", "noscript", "svg", "form", "aside"}
    KEEP = {"p", "h1", "h2", "h3", "h4", "li", "td", "th", "blockquote", "pre", "figcaption"}
    def __init__(self):
        super().__init__(); self.skip = 0; self.cur = None; self.buf = []; self.out = []
    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP: self.skip += 1
        elif tag in self.KEEP and not self.skip: self.cur = tag; self.buf = []
    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip: self.skip -= 1
        elif tag == self.cur:
            t = re.sub(r"\s+", " ", "".join(self.buf)).strip()
            if len(t) > 1:
                self.out.append(("#" * int(tag[1]) + " " + t) if tag in ("h1", "h2", "h3", "h4") else t)
            self.cur = None
    def handle_data(self, d):
        if self.cur and not self.skip: self.buf.append(d)

def html_text(raw):
    p = TextExtractor(); p.feed(raw)
    return "\n\n".join(p.out)

def page_text(url):
    text = html_text(fetch(url))
    return text if len(text) > 500 else ""

# --- Google News links -> publisher URL -------------------------------------
def gnews_resolve(link):
    """Best effort. Returns the publisher URL, or None if it cannot be resolved."""
    m = re.search(r"/(?:rss/)?articles/([^?/]+)", link)
    if not m:
        return None
    gid = m.group(1)
    try:
        raw = base64.urlsafe_b64decode(gid + "=" * (-len(gid) % 4))
        u = re.search(rb"https?://[\x21-\x7e]+", raw)
        if u and b"news.google" not in u.group(0):
            return u.group(0).decode("ascii", "ignore")
    except Exception:
        pass
    try:
        page = fetch(f"https://news.google.com/rss/articles/{gid}")
        sg = re.search(r'data-n-a-sg="([^"]+)"', page)
        tsm = re.search(r'data-n-a-ts="([^"]+)"', page)
        if not (sg and tsm):
            return None
        inner = ('["garturlreq",[["X","X",["X","X"],null,null,1,1,"US:en",null,1,null,null,null,'
                 'null,null,0,1],"X","X",1,[1,1,1],1,1,null,0,0,null,0],'
                 f'"{gid}",{tsm.group(1)},"{sg.group(1)}"]')
        body = "f.req=" + urllib.parse.quote(json.dumps([[["Fbv4je", inner, None, "generic"]]]))
        resp = fetch("https://news.google.com/_/DotsSplashUi/data/batchexecute",
                     data=body.encode(),
                     headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"})
        part = json.loads(resp.split("\n\n", 1)[1])
        url = json.loads(part[0][2])[1]
        return url if url.startswith("http") else None
    except Exception as e:
        log(f"    could not resolve Google News link ({type(e).__name__})")
        return None

# --- scoring -----------------------------------------------------------------
def score(item):
    hay = (item["title"] + " " + item.get("summary", "")).lower()
    s, hits, core = 0, [], 0
    for w, words in KEYWORDS.items():
        for k in words:
            if k in hay:
                s += w; hits.append(k)
                if w == 3: core += 1
    noise = [n for n in NOISE if n in hay]
    s -= 3 * len(noise)
    return s, hits, core, noise

def title_tokens(title):
    t = re.sub(r"\s+[-–|]\s+[^-–|]{2,40}$", "", title.lower())     # drop " - Publisher"
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return {w for w in t.split() if len(w) > 3 and w not in STOP}

def same_story(a, b):
    """Title overlap, or the same organisations + a shared core keyword within three days.
    Grouped items stay listed under their lead, so over-grouping hides nothing."""
    ta, tb = a["_tok"], b["_tok"]
    if ta and tb and len(ta & tb) / len(ta | tb) >= 0.4:
        return True
    if a["kind"] != "news" or b["kind"] != "news":
        return False
    if a["date"] and b["date"] and abs((a["date"] - b["date"]).days) > 3:
        return False
    oa = {o for o in ORGS if o in a["title"].lower()}
    ob = {o for o in ORGS if o in b["title"].lower()}
    ca = {h for h in a["hits"] if h in KEYWORDS[3]}
    cb = {h for h in b["hits"] if h in KEYWORDS[3]}
    return bool(oa) and oa == ob and len(ca & cb) >= 1

# --- YouTube -----------------------------------------------------------------
def youtube_channel_feed(handle):
    page = fetch(f"https://www.youtube.com/{handle}")
    m = re.search(r'"(?:channelId|externalId)":"(UC[\w-]{22})"', page)
    if not m:
        raise ValueError("channel id not found on page")
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={m.group(1)}"

def _runs(x):
    if not isinstance(x, dict): return ""
    if "simpleText" in x: return x["simpleText"]
    return "".join(r.get("text", "") for r in x.get("runs", []))

def youtube_search(query, days, now):
    """Parse YouTube's normal search page. Returns video items (no API key needed)."""
    sp = "EgIIAw%3D%3D" if days <= 7 else ("EgIIBA%3D%3D" if days <= 31 else "CAI%3D")
    page = fetch(f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}&sp={sp}")
    m = re.search(r"var ytInitialData\s*=\s*(\{.*?\});\s*</script>", page, re.S)
    if not m:
        raise ValueError("search data not found on page")
    data = json.loads(m.group(1))
    out, stack = [], [data]
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            vr = x.get("videoRenderer")
            if isinstance(vr, dict) and vr.get("videoId"):
                desc = " ".join(_runs(s.get("snippetText", {})) for s in vr.get("detailedMetadataSnippets", []))
                desc = desc or _runs(vr.get("descriptionSnippet", {}))
                out.append(dict(source=f"YouTube search: {query}", title=_runs(vr.get("title", {})),
                                link=yt_url(vr["videoId"]), video_id=vr["videoId"],
                                date=parse_ago(_runs(vr.get("publishedTimeText", {})), now),
                                publisher=_runs(vr.get("ownerText", {})), summary=desc[:600],
                                length=_runs(vr.get("lengthText", {}))))
            stack.extend(x.values())
        elif isinstance(x, list):
            stack.extend(x)
    return out

def transcript(video_id):
    """Returns ([(start_seconds, text), ...], None) or (None, reason)."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return None, "youtube-transcript-api not installed"
    try:
        api = YouTubeTranscriptApi()
        if hasattr(api, "fetch"):
            segs = [(s.start, s.text) for s in api.fetch(video_id, languages=["en", "en-US", "en-GB"])]
        else:
            segs = [(s["start"], s["text"]) for s in
                    YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])]
        return [(t, re.sub(r"\s+", " ", x).strip()) for t, x in segs if x.strip()], None
    except Exception as e:
        return None, f"{type(e).__name__}"

def score_transcript(segs):
    """Keyword density over the whole transcript, plus matched passages with timestamps."""
    text = " ".join(x for _, x in segs).lower()
    words = max(1, len(text.split()))
    counts, core = {}, set()
    for w, kws in KEYWORDS.items():
        for k in kws:
            n = text.count(k)
            if n:
                counts[k] = n
                if w == 3: core.add(k)
    weighted = sum(n * (3 if k in KEYWORDS[3] else 1) for k, n in counts.items())
    density = weighted * 1000 / words
    tscore = round(2 * len(core) + min(10, density), 1)
    windows = {}                                        # 60-second windows with most core hits
    for t, x in segs:
        windows.setdefault(int(t // 60), []).append(x)
    ranked = []
    for b, xs in windows.items():
        chunk = " ".join(xs)
        hits = sum(chunk.lower().count(k) for k in core)
        if hits:
            ranked.append((hits, b, chunk))
    ranked.sort(reverse=True)
    passages = [(b * 60, chunk[:450]) for _, b, chunk in sorted(ranked[:4], key=lambda r: r[1])]
    return tscore, sorted(core), words, passages

def ts(sec):
    sec = int(sec)
    return f"{sec//3600}:{sec%3600//60:02d}:{sec%60:02d}" if sec >= 3600 else f"{sec//60}:{sec%60:02d}"

def slug(s, n=60):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n] or "item"

# --- page watch ----------------------------------------------------------------
def watch_page(name, url, base):
    d = base / "watch"; d.mkdir(exist_ok=True)
    f = d / (slug(name) + ".txt")
    text = re.sub(r"\n{3,}", "\n\n", html_text(fetch(url))).strip()
    if len(text) < 200:
        return "page has little readable text (probably built by script); not compared", None
    if not f.exists():
        f.write_text(text)
        return f"first snapshot saved ({len(text.split())} words); changes reported from next run", None
    old = f.read_text()
    if old == text:
        return "unchanged", None
    diff = list(difflib.unified_diff(old.splitlines(), text.splitlines(), lineterm="", n=0))
    diff = [l for l in diff if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    f.write_text(text)
    return f"CHANGED ({len(diff)} lines differ)", diff[:40]

# ----------------------------------------------------------------------------
def main():
    global QUIET
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=8)
    ap.add_argument("--since", help="backfill from this date, YYYY-MM-DD (overrides --days)")
    ap.add_argument("--all", action="store_true", help="ignore memory of earlier runs")
    ap.add_argument("--out", default="scout-out")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--no-video", action="store_true")
    a = ap.parse_args()
    QUIET = a.quiet

    now = dt.datetime.now(dt.timezone.utc)
    cutoff = (dt.datetime.fromisoformat(a.since).replace(tzinfo=dt.timezone.utc)
              if a.since else now - dt.timedelta(days=a.days))
    window_days = max(1, (now - cutoff).days)
    backfill = bool(a.since)

    base = Path(a.out); base.mkdir(exist_ok=True)
    today = dt.date.today().isoformat()
    tag = today + ("-backfill" if backfill else "")
    run, n = base / tag, 1
    while (run / "digest.md").exists():
        n += 1; run = base / f"{tag}-{n}"
    (run / "texts").mkdir(parents=True, exist_ok=True)
    seen_file = base / "seen.json"
    seen = set() if a.all or not seen_file.exists() else set(json.loads(seen_file.read_text()))

    log(f"scout {VERSION}. Window: {cutoff.date()} to {now.date()}. Output: {run}", always=True)
    log(f"Remembered from earlier runs: {len(seen)} items")

    items, videos, status = [], [], []

    def take(name, url, kind, into=None):
        try:
            got = parse_feed(fetch(url), name)
            for g in got: g["kind"] = kind
            (into if into is not None else items).extend(got)
            status.append((name, True, f"{len(got)} items")); log(f"  {name}: {len(got)} items")
        except Exception as e:
            status.append((name, False, f"{type(e).__name__}: {str(e)[:80]}"))
        time.sleep(1)

    log("== Feeds ==", always=True)
    for name, url in FEEDS.items():
        take(name, url, "feed")

    log("== Google News searches ==", always=True)
    windows = []
    if backfill:
        start = cutoff.date()
        while start < now.date():
            end = min(start + dt.timedelta(days=30), now.date() + dt.timedelta(days=1))
            windows.append(f"after:{start.isoformat()} before:{end.isoformat()}")
            start = end
    else:
        windows = [f"when:{window_days}d"]
    for q in NEWS_QUERIES:
        for w in windows:
            url = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
                {"q": f"{q} {w}", "hl": "en-US", "gl": "US", "ceid": "US:en"})
            take(f"News: {q}" + (f" [{w}]" if backfill else ""), url, "news")

    log("== arXiv searches ==", always=True)
    for q in ARXIV_QUERIES:
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending",
             "max_results": 100 if backfill else 25})
        take(f"arXiv: {q}", url, "arxiv")
        time.sleep(3)

    log("== Pages without feeds ==", always=True)
    for name, (url, pat) in PAGES.items():
        try:
            lc = LinkCollector(); lc.feed(fetch(url))
            found = {}
            for href, txt in lc.links:
                path = urllib.parse.urlparse(href).path if href.startswith("http") else href
                if re.match(pat, path or "") and len(txt) > 8:
                    found.setdefault(urllib.parse.urljoin(url, path), txt)
            for link, txt in found.items():
                items.append(dict(source=name, title=txt[:200], link=link, date=None, publisher="",
                                  summary="", video_id=None, kind="page"))
            status.append((name, True, f"{len(found)} links")); log(f"  {name}: {len(found)} links")
        except Exception as e:
            status.append((name, False, f"{type(e).__name__}: {str(e)[:80]}"))

    log("== Watched pages ==", always=True)
    watched = []
    for name, url in WATCH.items():
        try:
            msg, diff = watch_page(name, url, base)
            watched.append((name, url, msg, diff)); status.append((f"Watch: {name}", True, msg))
        except Exception as e:
            status.append((f"Watch: {name}", False, f"{type(e).__name__}: {str(e)[:80]}"))

    if not a.no_video:
        log("== YouTube channels ==", always=True)
        for h in YOUTUBE_HANDLES:
            try:
                take(f"YouTube {h}", youtube_channel_feed(h), "video", into=videos)
            except Exception as e:
                status.append((f"YouTube {h}", False, f"{type(e).__name__}: {str(e)[:80]}"))
        log("== YouTube searches ==", always=True)
        for q in YOUTUBE_SEARCHES:
            try:
                try:
                    got = youtube_search(q, window_days, now)
                except ValueError:
                    time.sleep(5); got = youtube_search(q, window_days, now)     # one retry
                for g in got: g["kind"] = "video"
                videos.extend(got); status.append((f"YouTube search: {q}", True, f"{len(got)} videos"))
                log(f"  {q}: {len(got)} videos")
            except Exception as e:
                status.append((f"YouTube search: {q}", False, f"{type(e).__name__}: {str(e)[:80]}"))
            time.sleep(2)

    # --- news, papers, pages: new, in window, scored, stories grouped
    fresh, keys = [], set()
    for it in items:
        key = it["link"] or it["title"]
        if not key or key in keys: continue
        keys.add(key)
        if key in seen: continue
        if it["date"] and it["date"] < cutoff: continue
        it["score"], it["hits"], core, it["noise"] = score(it)
        if it["kind"] == "news" and core < NEWS_MIN_CORE:
            it["score"] = min(it["score"], MIN_SCORE - 1)
        it["_tok"] = title_tokens(it["title"])
        it["also"] = []
        fresh.append(it)
    fresh.sort(key=lambda i: -i["score"])               # the strongest version leads its group
    stories = []
    for it in fresh:
        for lead in stories:
            if same_story(lead, it):
                lead["also"].append(it); break
        else:
            stories.append(it)

    def keep(i):
        return i["score"] >= (MIN_SCORE_PRIMARY if i["kind"] in ("feed", "page") else MIN_SCORE)
    relevant = [i for i in stories if keep(i)]
    low = [i for i in stories if not keep(i)]
    relevant, dropped = local_triage(relevant)
    log(f"== Filtering: {len(items)} found, {len(fresh)} new, {len(stories)} stories, "
        f"{len(relevant)} relevant ==", always=True)

    # --- full texts
    log("== Fetching full texts ==", always=True)
    n_txt = 0
    for i, it in enumerate(relevant, 1):
        it["file"] = None
        if n_txt >= MAX_FULLTEXT or it["kind"] == "arxiv":
            continue
        try:
            url = it["link"]
            if it["kind"] == "news" and "news.google." in url:
                real = gnews_resolve(url)
                if not real:
                    it["note"] = "publisher link not resolved"; continue
                it["link"] = url = real
                time.sleep(1)
            t = page_text(url)
            if t:
                n_txt += 1
                fn = f"texts/{i:03d}-{slug(it['title'])}.txt"
                (run / fn).write_text(f"{it['title']}\n{url}\n\n{t}\n")
                it["file"] = fn; it["words"] = len(t.split())
                lab = local_label(it, t)
                if lab: it["label"] = lab
            else:
                it["note"] = "page had no readable text (paywall or script-only)"
            time.sleep(1)
        except Exception as e:
            it["note"] = f"text not fetched ({type(e).__name__})"

    # --- videos: transcripts scored on content
    vfresh, vkeys = [], set()
    for v in videos:
        if v["link"] in vkeys: continue
        vkeys.add(v["link"])
        if v["link"] in seen: continue
        if v["date"] and v["date"] < cutoff: continue
        v["pre"] = score(v)[0]
        vfresh.append(v)
    vfresh.sort(key=lambda v: (-v["pre"], -(v["date"] or cutoff).timestamp()))
    vcand = vfresh[:MAX_VIDEO_CANDIDATES]
    log(f"== Videos: {len(videos)} found, {len(vfresh)} new, scoring {len(vcand)} transcripts ==", always=True)
    blocked_row, stopped = 0, False
    for v in vcand:
        if stopped:
            v["tscore"], v["note"] = -1, "not tried (YouTube was blocking transcript requests)"
            continue
        segs, err = transcript(v["video_id"])
        if segs:
            blocked_row = 0
            v["tscore"], v["core"], v["words"], v["passages"] = score_transcript(segs)
            v["_segs"] = segs
            log(f"  {v['tscore']:5.1f}  {v['title'][:70]}")
        else:
            v["tscore"], v["note"] = -1, f"no transcript ({err})"
            blocked_row = blocked_row + 1 if err and "Block" in err else 0
            if blocked_row >= MAX_BLOCKED_IN_ROW:
                stopped = True
                log("  YouTube is blocking transcript requests; stopping for this run", always=True)
        time.sleep(TRANSCRIPT_PAUSE)
    ranked = sorted([v for v in vcand if v["tscore"] >= VIDEO_MIN_SCORE
                     and len(v.get("core", [])) >= VIDEO_MIN_CORE], key=lambda v: -v["tscore"])
    vkept = ranked[:MAX_TRANSCRIPTS]
    vrest = [v for v in vcand if v not in vkept]
    for k, v in enumerate(vkept, 1):
        full = " ".join(x for _, x in v["_segs"])
        fn = f"texts/video-{k}-{slug(v['title'])}.txt"
        if v["words"] <= MAX_TRANSCRIPT_WORDS:
            body = "\n".join(f"[{ts(t)}] {x}" for t, x in v["_segs"])
            v["saved_note"] = f"full transcript, {v['words']} words"
        else:
            body = "\n\n".join(f"[{ts(t)}] {p}" for t, p in v["passages"])
            v["saved_note"] = f"matched passages only; transcript is {v['words']} words"
        (run / fn).write_text(f"{v['title']}\n{v['link']}\n{v.get('publisher','')}\n\n{body}\n")
        v["file"] = fn
        lab = local_label(v, full)
        if lab: v["label"] = lab

    # --- digest
    win = f"{cutoff.date()} to {now.date()}" + (" (backfill)" if backfill else "")
    L = [f"# Scout digest {today} ({VERSION})", "",
         f"Window: {win}. New stories: {len(stories)} (from {len(fresh)} items). "
         f"Relevant: {len(relevant)}. Full texts: {n_txt}. "
         f"Videos: {len(vfresh)} new, {len(vcand)} transcripts scored, {len(vkept)} kept.", ""]
    changed = [w for w in watched if w[3]]
    if changed:
        L += ["## Watched pages that changed", ""]
        for name, url, msg, diff in changed:
            L += [f"**{name}** — {msg}  ", url, "", "```"] + [l[:200] for l in diff] + ["```", ""]
    L += ["## Relevant items (highest keyword score first)", ""]
    for i, it in enumerate(relevant, 1):
        d = it["date"].date().isoformat() if it["date"] else "undated"
        src = it["source"] + (f" ({it['publisher']})" if it.get("publisher") else "")
        L.append(f"{i}. **{it['title']}**  ")
        L.append(f"   {src} · {d} · score {it['score']}"
                 + (f" · {', '.join(sorted(set(it['hits'])))}" if it.get("hits") else "") + "  ")
        if it["also"]:
            L.append(f"   Same story, {len(it['also'])} more: "
                     + "; ".join(f"{x['title'][:70]} ({x.get('publisher') or x['source']})" for x in it["also"][:3])
                     + (" …" if len(it["also"]) > 3 else "") + "  ")
        L.append(f"   {it['link']}  ")
        if it.get("summary") and it["kind"] != "news":
            L.append(f"   > {it['summary'][:300]}  ")
        if it.get("file"): L.append(f"   Saved: `{it['file']}` ({it['words']} words)  ")
        if it.get("label"): L.append(f"   Local model: {it['label']}  ")
        if it.get("note"): L.append(f"   Note: {it['note']}  ")
        L.append("")
    if not a.no_video:
        L += ["## Videos kept (scored on transcript content)", ""]
        if not vkept:
            L += ["None reached the threshold this run.", ""]
        for k, v in enumerate(vkept, 1):
            d = v["date"].date().isoformat() if v["date"] else "undated"
            L.append(f"{k}. **{v['title']}**  ")
            L.append(f"   {v.get('publisher') or v['source']} · {d}"
                     + (f" · {v['length']}" if v.get("length") else "")
                     + f" · transcript score {v['tscore']} · {', '.join(v['core'])}  ")
            L.append(f"   {v['link']}  ")
            L.append(f"   Saved: `{v['file']}` ({v['saved_note']})  ")
            if v.get("label"): L.append(f"   Local model: {v['label']}  ")
            for t, p in v["passages"][:3]:
                L.append(f"   > [{ts(t)}] {p[:300]}  ")
            L.append("")
        L += ["## Other videos scored (headlines only)", ""]
        for v in sorted(vrest, key=lambda v: -v["tscore"])[:40]:
            sc = f"{v['tscore']}" if v["tscore"] >= 0 else "n/a"
            L.append(f"- [{sc}] {v['title'][:100]} ({v.get('publisher') or v['source']})"
                     + (f" · {v['note']}" if v.get("note") else ""))
        L.append("")
    if dropped:
        L += ["## Dropped by local model (headlines only)", ""]
        L += [f"- {it['title']} ({it['source']}) {it['link']}" for it in dropped] + [""]
    L += [f"## Low-score items (headlines only, top {MAX_LOW_LIST})", ""]
    L += [f"- [{it['score']}] {it['title']} ({it.get('publisher') or it['source']})"
          + (f" · noise: {', '.join(it['noise'])}" if it.get("noise") else "")
          for it in low[:MAX_LOW_LIST]]
    if len(low) > MAX_LOW_LIST:
        L.append(f"- … and {len(low) - MAX_LOW_LIST} more")
    unchanged = [w for w in watched if not w[3]]
    if unchanged:
        L += ["", "## Watched pages (no change to report)", ""]
        L += [f"- {name}: {msg}" for name, url, msg, diff in unchanged]
    L += ["", "## Sources", "", "| Source | Status |", "|---|---|"]
    L += [f"| {s} | {'ok' if ok else 'FAILED'}: {note} |" for s, ok, note in status]
    (run / "digest.md").write_text("\n".join(L) + "\n")

    # remember news/pages seen, and videos whose transcripts were scored
    seen.update(keys)
    seen.update(v["link"] for v in vcand if "not tried" not in v.get("note", "") and "Block" not in v.get("note", ""))
    seen_file.write_text(json.dumps(sorted(seen)))

    zpath = base / f"{run.name}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(run.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(base))
    ok = sum(1 for s in status if s[1])
    log(f"Done: {run/'digest.md'} ({len(relevant)} relevant, {len(vkept)} videos, "
        f"{ok}/{len(status)} sources ok)", always=True)
    log(f"Attach this file: {zpath.resolve()} ({zpath.stat().st_size//1024} KB)", always=True)

if __name__ == "__main__":
    main()
