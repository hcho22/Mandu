"""Free web sources for a teardown: the target's own site, archived copies of its
pages, Google's autocomplete, Hacker News, Bluesky, public job boards, and the
public profile pages of TikTok and YouTube.

Every read goes through gt_common.Fetcher, so robots.txt decides what is read.
"""

from __future__ import annotations

import html as html_lib
import html.parser
import json
import os
import re
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import gt_common as gc

SOCIAL_HOSTS = {
    "instagram.com": "instagram", "tiktok.com": "tiktok", "youtube.com": "youtube", "youtu.be": "youtube",
    "x.com": "x", "twitter.com": "x", "facebook.com": "facebook", "linkedin.com": "linkedin",
    "threads.net": "threads", "threads.com": "threads", "pinterest.com": "pinterest", "reddit.com": "reddit",
    "bsky.app": "bluesky", "discord.gg": "discord", "discord.com": "discord", "linktr.ee": "linktree",
    "snapchat.com": "snapchat", "twitch.tv": "twitch", "medium.com": "medium", "substack.com": "substack",
}
SHARE_PATHS = ("/sharer", "/share", "/intent/", "/shareArticle", "/pin/create", "/dialog/")

# Path families a growth teardown cares about, by first path segment.
FAMILIES = {
    "blog": "blog", "articles": "blog", "news": "blog", "learn": "blog", "guides": "blog", "resources": "blog",
    "compare": "compare", "vs": "compare", "alternatives": "compare", "alternative": "compare",
    "templates": "templates", "integrations": "integrations", "partners": "partners", "affiliates": "affiliate",
    "affiliate": "affiliate", "referral": "referral", "refer": "referral", "invite": "referral",
    "pricing": "pricing", "plans": "pricing", "help": "help", "help-center": "help", "support": "help",
    "faq": "help", "docs": "docs", "changelog": "changelog", "updates": "changelog", "careers": "careers",
    "jobs": "careers", "press": "press", "about": "about", "team": "about", "coaches": "people",
    "trainers": "people", "creators": "people", "ambassadors": "people", "workouts": "content-library",
    "exercises": "content-library", "programs": "content-library", "plans-library": "content-library",
    "recipes": "content-library", "challenges": "content-library", "u": "public-profiles",
    "user": "public-profiles", "users": "public-profiles", "profile": "public-profiles", "p": "shared-outputs",
    "s": "shared-outputs", "share": "shared-outputs", "gift": "referral", "download": "download",
    "app": "download", "get": "download", "legal": "legal", "privacy": "legal", "terms": "legal",
    "lp": "landing-pages", "landing": "landing-pages", "go": "landing-pages", "start": "landing-pages",
    "quiz": "web-funnel", "onboarding": "web-funnel", "funnel": "web-funnel", "checkout": "web-funnel",
    "join": "web-funnel", "signup": "web-funnel",
}


# ---------------------------------------------------------------- page text and links


class _TextAndLinks(html.parser.HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "template"}
    BLOCK = {"p", "div", "section", "article", "li", "h1", "h2", "h3", "h4", "h5", "h6", "br", "tr",
             "header", "footer", "main", "nav", "button", "a", "td", "th", "figcaption"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.links, self.meta, self.title = [], [], {}, ""
        self._skip, self._in_title = 0, False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in self.SKIP:
            self._skip += 1
        if tag == "title":
            self._in_title = True
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "meta" and attrs.get("content"):
            key = attrs.get("property") or attrs.get("name")
            if key:
                self.meta[key.lower()] = attrs["content"]
        if tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1
        if tag == "title":
            self._in_title = False
        if tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self._skip:
            self.parts.append(data)

    def text(self):
        joined = "".join(self.parts)
        lines = [re.sub(r"[ \t ]+", " ", line).strip() for line in joined.splitlines()]
        out, blank = [], False
        for line in lines:
            if line:
                out.append(line)
                blank = False
            elif not blank and out:
                out.append("")
                blank = True
        return "\n".join(out).strip()


def page_text(html_text: str):
    parser = _TextAndLinks()
    parser.feed(html_text)
    return {"title": parser.title.strip(), "meta": parser.meta, "text": parser.text(), "links": parser.links}


def read(fetcher, url):
    response = fetcher.get(url)
    parsed = page_text(response.text())
    parsed["status"] = response.status
    parsed["url"] = url
    return parsed


def handles(fetcher, domain):
    """Official social accounts linked from the site's home page."""
    home = "https://%s/" % domain
    response = fetcher.get(home)
    parsed = page_text(response.text())
    # Links in <a> tags, and addresses anywhere else in the page, such as JSON-LD `sameAs`.
    raw = re.findall(r"https?://[^\s\"'<>\\]+", response.text().replace("\\/", "/"))
    rows, seen = [], set()
    for href in parsed["links"] + raw:
        url = urllib.parse.urljoin(home, html_lib.unescape(href))
        parts = urllib.parse.urlsplit(url)
        host = parts.netloc.lower()
        host = host[4:] if host.startswith("www.") else host
        network = SOCIAL_HOSTS.get(host) or next(
            (v for k, v in SOCIAL_HOSTS.items() if host.endswith("." + k)), None)
        if not network or any(p in parts.path for p in SHARE_PATHS):
            continue
        segments = [s for s in parts.path.split("/") if s]
        if not segments:
            continue
        handle = segments[0] if network not in ("linkedin", "youtube") or len(segments) == 1 else "/".join(segments[:2])
        key = (network, handle.lower().lstrip("@"))
        if key in seen:
            continue
        seen.add(key)
        rows.append({"network": network, "handle": handle.lstrip("@"), "url": url, "found_on": home})
    return rows


# ---------------------------------------------------------------- sitemap and path families


def _robots_sitemaps(fetcher, domain):
    response = fetcher.get("https://%s/robots.txt" % domain)
    if not response.ok:
        return []
    return [line.split(":", 1)[1].strip() for line in response.text().splitlines()
            if line.lower().startswith("sitemap:")]


def _parse_sitemap(xml_bytes):
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return [], []
    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0] + "}"
    children, urls = [], []
    if root.tag.endswith("sitemapindex"):
        for node in root.findall(ns + "sitemap"):
            loc = node.findtext(ns + "loc")
            if loc:
                children.append(loc.strip())
    else:
        for node in root.findall(ns + "url"):
            loc = node.findtext(ns + "loc")
            if loc:
                urls.append({"url": loc.strip(), "lastmod": (node.findtext(ns + "lastmod") or "").strip()})
    return children, urls


def sitemap(fetcher, domain, max_sitemaps=60, max_urls=50000):
    queue = _robots_sitemaps(fetcher, domain) or ["https://%s/sitemap.xml" % domain]
    seen, urls = set(), []
    while queue and len(seen) < max_sitemaps and len(urls) < max_urls:
        current = queue.pop(0)
        if current in seen:
            continue
        seen.add(current)
        try:
            response = fetcher.get(current)
        except (gc.Blocked, gc.FetchError):
            continue
        if not response.ok:
            continue
        children, found = _parse_sitemap(response.body)
        queue.extend(children)
        urls.extend(found)
    return urls[:max_urls], sorted(seen)


def family_of(url):
    parts = urllib.parse.urlsplit(url)
    segments = [s for s in parts.path.split("/") if s]
    if not segments:
        return "home", ""
    first = segments[0].lower()
    if re.fullmatch(r"[a-z]{2}(-[a-z]{2})?", first) and len(segments) > 1:  # a locale prefix
        first = segments[1].lower()
    return FAMILIES.get(first, "other:" + first), first


def families(url_rows):
    groups = {}
    for row in url_rows:
        family, segment = family_of(row["url"])
        g = groups.setdefault((family, segment), {"family": family, "segment": segment, "count": 0,
                                                   "first_lastmod": "", "last_lastmod": "", "example": row["url"]})
        g["count"] += 1
        lastmod = row.get("lastmod", "")[:10]
        if lastmod:
            if not g["first_lastmod"] or lastmod < g["first_lastmod"]:
                g["first_lastmod"] = lastmod
            if lastmod > g["last_lastmod"]:
                g["last_lastmod"] = lastmod
    return sorted(groups.values(), key=lambda g: -g["count"])


# ---------------------------------------------------------------- universal links (AASA)


def aasa(fetcher, domain):
    """The app paths this domain hands to the iOS app: shared outputs, invites, referrals."""
    for path in ("/.well-known/apple-app-site-association", "/apple-app-site-association"):
        try:
            response = fetcher.get("https://%s%s" % (domain, path))
        except (gc.Blocked, gc.FetchError):
            continue
        if not response.ok:
            continue
        try:
            data = response.json()
        except ValueError:
            continue
        rows = []
        for detail in (data.get("applinks") or {}).get("details", []):
            app_ids = detail.get("appIDs") or ([detail["appID"]] if detail.get("appID") else [])
            for comp in detail.get("components", []):
                rows.append({"app_ids": " ".join(app_ids), "path": comp.get("/", ""),
                             "query": json.dumps(comp.get("?")) if comp.get("?") else "",
                             "exclude": bool(comp.get("exclude")), "comment": comp.get("comment", "")})
            for p in detail.get("paths", []):
                rows.append({"app_ids": " ".join(app_ids), "path": p, "query": "",
                             "exclude": p.startswith("NOT "), "comment": ""})
        return {"url": "https://%s%s" % (domain, path), "paths": rows,
                "webcredentials": (data.get("webcredentials") or {}).get("apps", []),
                "appclips": (data.get("appclips") or {}).get("apps", [])}
    return None


# ---------------------------------------------------------------- page history (Wayback)


_PRICE_RE = re.compile(r"(?:US)?\$\s?([0-9]{1,4}(?:[.,][0-9]{2})?)\s*(?:/|per\s)?\s*(mo|month|yr|year|week|wk)?", re.I)
_TRIAL_RE = re.compile(r"(\d{1,2})[- ]day(?:s)? free trial|free for (\d{1,2}) days|(\d{1,2})[- ]day trial", re.I)


def page_history(fetcher, url, limit_months=36):
    bare = url.split("://", 1)[-1]
    cdx = "https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode({
        "url": bare, "output": "json", "fl": "timestamp,original,statuscode",
        "filter": "statuscode:200", "collapse": "timestamp:6", "limit": "400"})
    response = fetcher.get(cdx, route="wayback")
    if not response.ok or not response.body.strip():
        return []
    rows_in = response.json()[1:]
    rows = []
    for timestamp, original, _status in rows_in[-limit_months:]:
        snap = "https://web.archive.org/web/%sid_/%s" % (timestamp, original)
        try:
            page = fetcher.get(snap, route="wayback", also_gate=[original])
        except (gc.Blocked, gc.FetchError):
            continue
        if not page.ok:
            continue
        parsed = page_text(page.text())
        text = parsed["text"]
        prices = sorted({"$%s%s" % (m.group(1), ("/" + m.group(2).lower()) if m.group(2) else "")
                         for m in _PRICE_RE.finditer(text)})
        trials = sorted({next(g for g in m.groups() if g) + "-day" for m in _TRIAL_RE.finditer(text)})
        h1 = next((line for line in text.splitlines() if line.strip()), "")
        rows.append({"month": "%s-%s" % (timestamp[:4], timestamp[4:6]), "snapshot": timestamp,
                     "title": parsed["title"], "first_line": h1[:160], "prices": " ".join(prices[:12]),
                     "trials": " ".join(trials), "snapshot_url": "https://web.archive.org/web/%s/%s" % (timestamp, original)})
    return rows


# ---------------------------------------------------------------- search demand and mentions


def suggest(fetcher, seed, expand=False, country="us"):
    """Google autocomplete for a seed, and optionally for the seed plus each letter."""
    queries = [seed] + (["%s %s" % (seed, ch) for ch in "abcdefghijklmnopqrstuvwxyz"] if expand else [])
    rows, seen = [], set()
    for query in queries:
        url = "https://suggestqueries.google.com/complete/search?" + urllib.parse.urlencode(
            {"client": "firefox", "hl": "en", "gl": country, "q": query})
        response = fetcher.get(url, route="api")
        if not response.ok:
            continue
        try:
            data = json.loads(response.body.decode("utf-8", "replace"))
        except ValueError:
            data = json.loads(response.body.decode("latin-1"))
        for position, phrase in enumerate(data[1] if len(data) > 1 else [], 1):
            if phrase not in seen:
                seen.add(phrase)
                rows.append({"seed": seed, "query": query, "suggestion": phrase, "position": position})
    return rows


def hn(fetcher, query, pages=2):
    rows = []
    for page in range(pages):
        url = "https://hn.algolia.com/api/v1/search?" + urllib.parse.urlencode(
            {"query": query, "tags": "story", "hitsPerPage": 50, "page": page})
        hits = fetcher.get(url, route="api").json().get("hits", [])
        for hit in hits:
            rows.append({"date": hit.get("created_at", ""), "title": hit.get("title", ""),
                         "url": hit.get("url") or "", "points": hit.get("points") or 0,
                         "comments": hit.get("num_comments") or 0, "author": hit.get("author", ""),
                         "hn_url": "https://news.ycombinator.com/item?id=%s" % hit.get("objectID")})
        if len(hits) < 50:
            break
    return rows


def bluesky(fetcher, handle, limit=100):
    url = "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?" + urllib.parse.urlencode(
        {"actor": handle, "limit": min(limit, 100), "filter": "posts_no_replies"})
    feed = fetcher.get(url, route="api").json().get("feed", [])
    rows = []
    for item in feed:
        post = item.get("post", {})
        if (post.get("author") or {}).get("handle") != handle:
            continue  # a repost
        record = post.get("record", {})
        rkey = post.get("uri", "").rsplit("/", 1)[-1]
        images = [img.get("fullsize") for img in ((post.get("embed") or {}).get("images") or [])]
        rows.append({"channel": "bluesky", "id": rkey, "url": "https://bsky.app/profile/%s/post/%s" % (handle, rkey),
                     "date": record.get("createdAt", ""), "text": record.get("text", ""),
                     "likes": post.get("likeCount", 0), "reposts": post.get("repostCount", 0),
                     "replies": post.get("replyCount", 0),
                     "metric": int(post.get("likeCount", 0)) + int(post.get("repostCount", 0)),
                     "media": "image" if images else "", "image_url": images[0] if images else ""})
    return rows


# ---------------------------------------------------------------- jobs


CHANNEL_WORDS = [
    ("aso", r"\baso\b|app store optim"), ("seo", r"\bseo\b|search engine"), ("paid", r"paid|performance market|user acquisition|\bua\b|media buy|growth market"),
    ("lifecycle", r"lifecycle|crm|retention market|email market"), ("community", r"community"),
    ("creator", r"creator|influencer|ugc|partnerships? market"), ("content", r"content|copywrit|editor|\bsocial\b"),
    ("video", r"video|motion|editor"), ("brand", r"brand"), ("design", r"design"), ("partnerships", r"partnership|business development|\bbd\b"),
    ("data", r"analyst|analytics|data scien"), ("product", r"product manager|\bpm\b"), ("engineering", r"engineer|developer"),
    ("coach", r"coach|trainer"), ("sales", r"sales|account exec"),
]


def channel_of(title):
    lowered = title.lower()
    return ", ".join(name for name, pattern in CHANNEL_WORDS if re.search(pattern, lowered)) or "other"


def jobs(fetcher, slug):
    """Open roles from whichever public job board API knows this company slug."""
    boards = [
        ("greenhouse", "https://boards-api.greenhouse.io/v1/boards/%s/jobs" % slug),
        ("lever", "https://api.lever.co/v0/postings/%s?mode=json" % slug),
        ("ashby", "https://api.ashbyhq.com/posting-api/job-board/%s" % slug),
    ]
    for board, url in boards:
        try:
            response = fetcher.get(url, route="api")
        except (gc.Blocked, gc.FetchError):
            continue
        if not response.ok:
            continue
        try:
            data = response.json()
        except ValueError:
            continue
        rows = []
        if board == "greenhouse":
            for job in data.get("jobs", []):
                rows.append({"board": board, "title": job.get("title", ""), "team": "",
                             "location": (job.get("location") or {}).get("name", ""),
                             "updated": job.get("updated_at", ""), "url": job.get("absolute_url", "")})
        elif board == "lever":
            for job in data if isinstance(data, list) else []:
                cats = job.get("categories") or {}
                created = job.get("createdAt")
                rows.append({"board": board, "title": job.get("text", ""), "team": cats.get("team", ""),
                             "location": cats.get("location", ""),
                             "updated": gc.iso_z(gc.from_epoch(created / 1000)) if created else "",
                             "url": job.get("hostedUrl", "")})
        else:
            for job in data.get("jobs", []):
                rows.append({"board": board, "title": job.get("title", ""), "team": job.get("department", ""),
                             "location": job.get("location", ""), "updated": job.get("publishedAt", ""),
                             "url": job.get("jobUrl", "")})
        for row in rows:
            row["channel"] = channel_of(row["title"] + " " + row["team"])
        if rows or board != "ashby":
            return board, rows
    return None, []


# ---------------------------------------------------------------- TikTok and YouTube public pages


def _script_json(html_text, element_id):
    m = re.search(r'<script[^>]*id="%s"[^>]*>(.*?)</script>' % re.escape(element_id), html_text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def parse_tiktok_profile(html_text):
    data = _script_json(html_text, "__UNIVERSAL_DATA_FOR_REHYDRATION__")
    if not data:
        return None
    info = ((data.get("__DEFAULT_SCOPE__") or {}).get("webapp.user-detail") or {}).get("userInfo") or {}
    user, stats = info.get("user") or {}, info.get("stats") or {}
    if not user:
        return None
    return {"handle": user.get("uniqueId"), "name": user.get("nickname"), "bio": user.get("signature"),
            "bio_link": (user.get("bioLink") or {}).get("link", ""), "verified": user.get("verified"),
            "followers": stats.get("followerCount"), "likes": stats.get("heartCount") or stats.get("heart"),
            "videos": stats.get("videoCount"), "following": stats.get("followingCount")}


def tiktok_profile(fetcher, handle):
    url = "https://www.tiktok.com/@%s" % handle.lstrip("@")
    profile = parse_tiktok_profile(fetcher.get(url).text())
    if profile:
        profile["url"] = url
    return profile


_COUNT_WORDS = {"K": 1e3, "M": 1e6, "B": 1e9}


def parse_count(text):
    """'1.2M views' -> 1200000; '1,234 views' -> 1234; None when there is no number."""
    if not text:
        return None
    m = re.search(r"([0-9][0-9.,]*)\s*([KMB])?", text.replace(" ", " "))
    if not m:
        return None
    number = float(m.group(1).replace(",", ""))
    return int(round(number * _COUNT_WORDS.get(m.group(2) or "", 1)))


def _walk(node, key):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == key:
                yield v
            for found in _walk(v, key):
                yield found
    elif isinstance(node, list):
        for item in node:
            for found in _walk(item, key):
                yield found


def _yt_initial_data(html_text):
    m = re.search(r"var ytInitialData\s*=\s*(\{.*?\});\s*</script>", html_text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def _text(node):
    if not node:
        return ""
    if isinstance(node, str):
        return node
    if "simpleText" in node:
        return node["simpleText"]
    return "".join(run.get("text", "") for run in node.get("runs", []))


def parse_youtube_tab(html_text, kind):
    """Videos or Shorts listed on a channel tab page, with the page's rounded counts."""
    data = _yt_initial_data(html_text)
    if not data:
        return []
    rows = []
    for renderer in _walk(data, "videoRenderer"):
        vid = renderer.get("videoId")
        if not vid:
            continue
        rows.append({"channel": "youtube", "kind": kind, "id": vid, "url": "https://www.youtube.com/watch?v=" + vid,
                     "title": _text(renderer.get("title")), "views_text": _text(renderer.get("viewCountText")),
                     "metric": parse_count(_text(renderer.get("viewCountText"))),
                     "published_text": _text(renderer.get("publishedTimeText")),
                     "length": _text(renderer.get("lengthText")),
                     "image_url": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % vid, "approx": True})
    for lockup in _walk(data, "shortsLockupViewModel"):
        vid = (((lockup.get("onTap") or {}).get("innertubeCommand") or {}).get("reelWatchEndpoint") or {}).get("videoId")
        if not vid:
            continue
        overlay = lockup.get("overlayMetadata") or {}
        views = ((overlay.get("secondaryText") or {}).get("content")) or ""
        rows.append({"channel": "youtube", "kind": "short", "id": vid, "url": "https://www.youtube.com/shorts/" + vid,
                     "title": ((overlay.get("primaryText") or {}).get("content")) or "", "views_text": views,
                     "metric": parse_count(views), "published_text": "", "length": "",
                     "image_url": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % vid, "approx": True})
    return rows


def youtube(fetcher, handle, api_key=None):
    """A channel's recent uploads: exact numbers through the Data API when a key is
    set, otherwise the rounded numbers the channel's public tab pages show."""
    handle = handle.lstrip("@")
    api_key = api_key or os.environ.get("YOUTUBE_API_KEY")
    if api_key:
        return _youtube_api(fetcher, handle, api_key), "data-api"
    rows = []
    for tab, kind in (("videos", "video"), ("shorts", "short")):
        try:
            page = fetcher.get("https://www.youtube.com/@%s/%s" % (handle, tab))
        except (gc.Blocked, gc.FetchError):
            continue
        if page.ok:
            rows.extend(parse_youtube_tab(page.text(), kind))
    return rows, "channel-page"


def _youtube_api(fetcher, handle, key):
    base = "https://www.googleapis.com/youtube/v3/"

    # The key travels in the query string; the fetcher redacts it from the log and cache records.
    def call(path, params):
        query = urllib.parse.urlencode(dict(params, key=key))
        return fetcher.get(base + path + "?" + query, route="api", secrets=(key,)).json()
    channel = call("channels", {"part": "contentDetails,statistics,snippet", "forHandle": "@" + handle})
    items = channel.get("items") or []
    if not items:
        return []
    uploads = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, token = [], None
    for _ in range(2):
        params = {"part": "contentDetails", "playlistId": uploads, "maxResults": 50}
        if token:
            params["pageToken"] = token
        page = call("playlistItems", params)
        ids += [i["contentDetails"]["videoId"] for i in page.get("items", [])]
        token = page.get("nextPageToken")
        if not token:
            break
    rows = []
    for start in range(0, len(ids), 50):
        videos = call("videos", {"part": "snippet,statistics,contentDetails", "id": ",".join(ids[start:start + 50])})
        for v in videos.get("items", []):
            stats, snippet = v.get("statistics", {}), v.get("snippet", {})
            duration = v.get("contentDetails", {}).get("duration", "")
            rows.append({"channel": "youtube", "kind": "short" if _seconds(duration) <= 180 else "video",
                         "id": v["id"], "url": "https://www.youtube.com/watch?v=" + v["id"],
                         "title": snippet.get("title", ""), "views_text": stats.get("viewCount", ""),
                         "metric": int(stats.get("viewCount", 0) or 0), "date": snippet.get("publishedAt", ""),
                         "published_text": "", "length": duration, "likes": stats.get("likeCount", ""),
                         "comments": stats.get("commentCount", ""),
                         "image_url": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % v["id"], "approx": False})
    return rows


def _seconds(iso_duration):
    m = re.fullmatch(r"P(?:\d+D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso_duration or "")
    if not m:
        return 0
    h, mnt, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mnt * 60 + s


def save_images(fetcher, rows, out_dir, key="image_url", limit=None):
    """Download each row's image into out_dir as <id>.jpg and record it in row['image']."""
    out_dir = Path(out_dir)
    for index, row in enumerate(rows[:limit] if limit else rows, 1):
        url = row.get(key)
        if not url:
            continue
        dest = out_dir / ("%s.jpg" % gc.slugify(str(row.get("id") or "%03d" % index)))
        try:
            fetcher.save(url, dest)
            row["image"] = str(dest)
        except (gc.Blocked, gc.FetchError) as exc:
            row["image"] = ""
            row["image_note"] = str(exc)[:200]
    return rows
