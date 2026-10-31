"""App Store data from Apple's free public endpoints and the Wayback Machine.

- lookup and search: https://itunes.apple.com/lookup and /search (iTunes Search API)
- keyword ranks: the order the Search API returns apps for a term; a proxy for App
  Store search position, not the same thing
- ratings history: monthly Wayback Machine snapshots of the app's App Store page,
  read from the page's JSON-LD aggregateRating

Apple's customer-review feed (/<cc>/rss/customerreviews/...) is not read: its
robots.txt has `Disallow: /*/rss/*`. Review text reaches a teardown only as quotes
hcho copied by hand, through the customer-research skill.
"""

from __future__ import annotations

import html as html_lib
import json
import re
import urllib.parse
from pathlib import Path

import gt_common as gc

LOOKUP_FIELDS = ["trackId", "trackName", "artistName", "artistId", "sellerUrl", "trackViewUrl",
                 "releaseDate", "currentVersionReleaseDate", "version", "averageUserRating",
                 "userRatingCount", "formattedPrice", "primaryGenreName", "genres",
                 "contentAdvisoryRating", "minimumOsVersion", "languageCodesISO2A"]
RANK_FIELDS = ["term", "country", "rank", "results", "top1", "top2", "top3", "checked_at"]
HISTORY_FIELDS = ["month", "snapshot", "ratings", "ratings_exact", "rating_value", "version",
                  "price", "subtitle", "snapshot_url"]
VERSION_FIELDS = ["version", "date", "notes"]
CHART_FIELDS = ["chart", "position", "app_id", "title", "subtitle", "ratings", "is_target"]


def _api(country, path, params):
    return "https://itunes.apple.com/%s?%s" % (path, urllib.parse.urlencode(dict(params, country=country)))


def lookup(fetcher, app_id, country="us"):
    """One app's public record by its App Store id (the digits after `id` in its App
    Store address). Apple's robots.txt refuses /search, so there is no lookup by name."""
    url = _api(country, "lookup", {"id": app_id, "entity": "software"})
    results = fetcher.get(url, route="api").json().get("results", [])
    apps = [r for r in results if r.get("wrapperType") == "software" or r.get("kind") == "software"]
    if not apps:
        raise SystemExit("The iTunes Search API returned no app for id %s." % app_id)
    return apps[0]


def developer_apps(fetcher, artist_id, country="us"):
    url = _api(country, "lookup", {"id": artist_id, "entity": "software", "limit": 200})
    results = fetcher.get(url, route="api").json().get("results", [])
    return [r for r in results if r.get("wrapperType") == "software"]


def summarize(app: dict) -> dict:
    out = {k: app.get(k) for k in LOOKUP_FIELDS}
    out["genres"] = ", ".join(app.get("genres") or [])
    out["languageCodesISO2A"] = ", ".join(app.get("languageCodesISO2A") or [])
    out["description_first_lines"] = "\n".join((app.get("description") or "").splitlines()[:6])
    out["releaseNotes"] = app.get("releaseNotes")
    out["screenshotUrls"] = app.get("screenshotUrls") or []
    return out


# ---------------------------------------------------------------- the live listing and the charts


def _serialized(html_text):
    m = re.search(r'<script[^>]*id="serialized-server-data"[^>]*>(.*?)</script>', html_text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def _nodes(node):
    stack = [node]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            yield current
            stack.extend(reversed(list(current.values())))
        elif isinstance(current, list):
            stack.extend(reversed(current))


def _version_date(text):
    """'Fri Oct 30 2026 15:16:56 GMT+0000 (...)' -> '2026-10-30'."""
    m = re.match(r"\w{3} (\w{3}) (\d{1,2}) (\d{4})", text or "")
    if not m:
        return ""
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    if m.group(1) not in months:
        return ""
    return "%s-%02d-%02d" % (m.group(3), months.index(m.group(1)) + 1, int(m.group(2)))


def parse_live_listing(html_text, track_name):
    """Subtitle, in-app purchases, facts, and version history from the live App Store page."""
    data = _serialized(html_text)
    out = {"subtitle": "", "in_app_purchases": [], "facts": {}, "versions": []}
    if not data:
        return out
    for node in _nodes(data):
        if not out["subtitle"] and node.get("title") == track_name and isinstance(node.get("subtitle"), str):
            out["subtitle"] = node["subtitle"]
        if node.get("$kind") == "Annotation" and node.get("title"):
            if node["title"] == "In-App Purchases":
                out["in_app_purchases"] = [{"name": i.get("leadingText"), "price": i.get("trailingText")}
                                           for i in node.get("items", []) if i.get("leadingText")]
            elif node.get("summary"):
                out["facts"][node["title"]] = node["summary"]
        if node.get("page") == "versionHistory" and node.get("pageData") and not out["versions"]:
            for shelf in node["pageData"].get("shelves", []):
                for item in shelf.get("items", []):
                    if item.get("primarySubtitle"):
                        notes = (item.get("text") or "").replace("This version includes the following:", "").strip()
                        out["versions"].append({"version": item["primarySubtitle"],
                                                "date": _version_date(item.get("secondarySubtitle")),
                                                "notes": re.sub(r"\s+", " ", notes)[:400]})
    return out


def listing(fetcher, app):
    url = (app.get("trackViewUrl") or "").split("?")[0]
    response = fetcher.get(url)
    parsed = parse_live_listing(response.text(), app.get("trackName", ""))
    parsed["url"] = url
    return parsed


def parse_chart(html_text):
    """{chart: [(position, adamId, title, subtitle, ratingCount)]} for Top Free and Top Paid."""
    data = _serialized(html_text)
    charts = {}
    if not data:
        return charts
    for node in _nodes(data):
        if node.get("$kind") != "TopChartSegment":
            continue
        entries = []
        for shelf in node.get("shelves", []):
            for item in shelf.get("items", []):
                entries.append((str(item.get("adamId", "")), item.get("title", ""), item.get("subtitle", ""),
                                item.get("ratingCount", "")))
        for rest in (node.get("nextPage") or {}).get("remainingContent", []):
            entries.append((str(rest.get("id", "")), "", "", ""))
        charts[node.get("chart", node.get("shortName", ""))] = [
            (position,) + entry for position, entry in enumerate(entries, 1)]
    return charts


def chart(fetcher, app, country="us"):
    """The app's position in its category's Top Free and Top Paid charts (top 200)."""
    genre = app.get("primaryGenreId")
    url = "https://apps.apple.com/%s/iphone/charts/%s" % (country, genre)
    charts = parse_chart(fetcher.get(url).text())
    rows, positions = [], {}
    for name, entries in charts.items():
        for position, adam_id, title, subtitle, ratings in entries:
            rows.append({"chart": name, "position": position, "app_id": adam_id, "title": title,
                         "subtitle": subtitle, "ratings": ratings, "is_target": adam_id == str(app["trackId"])})
            if adam_id == str(app["trackId"]):
                positions[name] = position
    return rows, {"url": url, "genre": app.get("primaryGenreName"), "positions": positions,
                  "chart_lengths": {k: len(v) for k, v in charts.items()}, "read_at": gc.iso_z(gc.utc_now())}


# ---------------------------------------------------------------- ratings history


_COUNT_RE = re.compile(r"([0-9][0-9.,]*)\s?([KM]?)\s+Ratings")
_OLD_SUBTITLE = re.compile(r'product-header__subtitle[^>]*>\s*([^<]+?)\s*<', re.S)


def parse_listing(html: str, track_name: str = "") -> dict:
    """Ratings count, average, version, price, and subtitle from one App Store page (any era)."""
    out = {"ratings": None, "ratings_exact": False, "rating_value": None, "version": None, "price": None,
           "subtitle": None}
    old = _OLD_SUBTITLE.search(html)
    if old:
        out["subtitle"] = html_lib.unescape(re.sub(r"\s+", " ", old.group(1)).strip())
    elif track_name:
        out["subtitle"] = parse_live_listing(html, track_name)["subtitle"] or None
    agg = re.search(r'"aggregateRating"\s*:\s*\{(.*?)\}', html, re.S)
    if agg:
        count = re.search(r'"(?:reviewCount|ratingCount)"\s*:\s*"?([0-9]+)', agg.group(1))
        value = re.search(r'"ratingValue"\s*:\s*"?([0-9.]+)', agg.group(1))
        if count:
            out["ratings"], out["ratings_exact"] = int(count.group(1)), True
        if value:
            out["rating_value"] = float(value.group(1))
    if out["ratings"] is None:
        m = _COUNT_RE.search(html)
        if m:
            number = float(m.group(1).replace(",", ""))
            out["ratings"] = int(number * {"K": 1000, "M": 1000000}.get(m.group(2), 1))
    version = re.search(r'"softwareVersion"\s*:\s*"([^"]+)"', html) or re.search(
        r'>\s*Version\s+([0-9][0-9.]*)\s*<', html)
    if version:
        out["version"] = version.group(1)
    offers = re.search(r'"offers"\s*:\s*\{[^}]*?"price"\s*:\s*"?([0-9.]+)', html, re.S)
    if offers:
        out["price"] = offers.group(1)
    return out


def listing_urls(app: dict, country="us"):
    """The App Store page addresses the Wayback Machine may hold for this app."""
    app_id = app["trackId"]
    canonical = (app.get("trackViewUrl") or "").split("?")[0]
    urls = [canonical] if canonical else []
    urls += ["https://apps.apple.com/%s/app/id%s" % (country, app_id),
             "https://itunes.apple.com/%s/app/id%s" % (country, app_id)]
    if canonical:
        urls.append(canonical.replace("https://apps.apple.com/", "https://itunes.apple.com/"))
    seen, out = set(), []
    for url in urls:
        if url and url not in seen:
            seen.add(url)
            out.append(url)
    return out


def snapshots(fetcher, page_url):
    """One 200 snapshot per month: [(timestamp, original)]."""
    bare = page_url.split("://", 1)[-1]
    cdx = "https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode({
        "url": bare, "output": "json", "fl": "timestamp,original,statuscode",
        "filter": "statuscode:200", "collapse": "timestamp:6", "limit": "400"})
    response = fetcher.get(cdx, route="wayback")
    if not response.ok or not response.body.strip():
        return []
    rows = response.json()
    return [(r[0], r[1]) for r in rows[1:]] if rows else []


def history(fetcher, app, country="us"):
    """Monthly ratings history from archived App Store pages."""
    by_month = {}
    for page_url in listing_urls(app, country):
        for timestamp, original in snapshots(fetcher, page_url):
            by_month.setdefault(timestamp[:6], (timestamp, original))
    rows = []
    for month in sorted(by_month):
        timestamp, original = by_month[month]
        snap = "https://web.archive.org/web/%sid_/%s" % (timestamp, original)
        try:
            response = fetcher.get(snap, route="wayback", also_gate=[original])
        except (gc.Blocked, gc.FetchError):
            continue
        if not response.ok:
            continue
        parsed = parse_listing(response.text(), app.get("trackName", ""))
        if parsed["ratings"] is None:
            continue
        rows.append({"month": "%s-%s" % (month[:4], month[4:]), "snapshot": timestamp,
                     "ratings": parsed["ratings"], "ratings_exact": parsed["ratings_exact"],
                     "rating_value": parsed["rating_value"], "version": parsed["version"],
                     "price": parsed["price"], "subtitle": parsed["subtitle"],
                     "snapshot_url": "https://web.archive.org/web/%s/%s" % (timestamp, original)})
    return rows


def screenshots(fetcher, app, out_dir: Path, limit=10):
    saved = []
    for index, url in enumerate((app.get("screenshotUrls") or [])[:limit], 1):
        suffix = Path(urllib.parse.urlsplit(url).path).suffix or ".jpg"
        dest = Path(out_dir) / ("%02d%s" % (index, suffix))
        try:
            fetcher.save(url, dest, route="api")
        except (gc.Blocked, gc.FetchError) as exc:
            saved.append({"index": index, "url": url, "file": "", "note": str(exc)})
            continue
        saved.append({"index": index, "url": url, "file": str(dest), "note": ""})
    return saved


