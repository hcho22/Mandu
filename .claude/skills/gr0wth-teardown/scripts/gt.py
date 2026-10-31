#!/usr/bin/env python3
"""gr0wth-teardown's command line: every free data pull, the analysis, the render,
and the check, each writing into one run folder.

    python3 .claude/skills/gr0wth-teardown/scripts/gt.py <command> ...

Run `gt.py -h` or `gt.py <command> -h` for the arguments. Commands print a short
summary and the files they wrote; the data itself is in the run's data/ folder.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import gt_ads  # noqa: E402
import gt_analyze  # noqa: E402
import gt_appstore  # noqa: E402
import gt_capture  # noqa: E402
import gt_check  # noqa: E402
import gt_common as gc  # noqa: E402
import gt_rea  # noqa: E402
import gt_render  # noqa: E402
import gt_stack  # noqa: E402
import gt_web  # noqa: E402

POST_FIELDS = ["channel", "kind", "id", "url", "date", "published_text", "title", "text", "metric", "views_text",
               "likes", "comments", "reposts", "replies", "length", "media", "image_url", "image", "approx", "source",
               "tier", "metric_value", "age_days", "spread_per_day", "fast_spreader"]


def say(*lines):
    for line in lines:
        print(line)


def run_dir(value) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    gc.load_run(path)
    return path


def domain_of(run: Path, given=None) -> str:
    if given:
        return given.lower().replace("https://", "").replace("http://", "").strip("/")
    meta = gc.load_run(run)
    if not meta.get("domain"):
        raise SystemExit("No domain for this run yet; pass --domain or run `appstore lookup` first.")
    return meta["domain"]


def rel(run, path) -> str:
    return str(Path(path).relative_to(run))


# ---------------------------------------------------------------- commands


def cmd_init(a):
    run = gc.new_run(a.product, a.target, a.mode, a.country)
    fields = {}
    if a.domain:
        fields["domain"] = domain_of(run, a.domain)
    if a.app_id:
        fields["app_id"] = str(a.app_id)
    if fields:
        gc.update_run(run, **fields)
    say(str(run))


def cmd_robots(a):
    allowed, detail, delay = gc.Robots().check(a.url)
    say("%s  %s  (%s%s)" % ("ALLOW" if allowed else "DENY", a.url, detail,
                            ", crawl-delay %ss" % delay if delay else ""))
    return 0 if allowed else 3


def cmd_read(a):
    run = run_dir(a.run)
    f = gc.Fetcher(run, refresh=a.refresh)
    page = gt_web.read(f, a.url)
    name = a.save or gc.slugify(urllib.parse.urlsplit(a.url).path or "home")[:60] or "home"
    out = run / "data" / "pages" / ("%s.txt" % name)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("URL: %s\nStatus: %s\nTitle: %s\nDescription: %s\n\n%s\n" % (
        a.url, page["status"], page["title"], page["meta"].get("description", page["meta"].get("og:description", "")),
        page["text"]), encoding="utf-8")
    say("status %s, %d characters of text -> %s" % (page["status"], len(page["text"]), rel(run, out)))
    if a.print:
        say("", page["text"][:a.max_chars])


def cmd_appstore(a):
    run = run_dir(a.run)
    meta = gc.load_run(run)
    country = a.country or meta.get("country", "us")
    f = gc.Fetcher(run, refresh=a.refresh)
    app_id = a.id or meta.get("app_id")
    if a.action != "lookup" and not (run / "data" / "appstore.json").exists():
        raise SystemExit("Run `appstore lookup` first.")
    if a.action == "lookup":
        if not app_id:
            raise SystemExit("Pass --id: the digits after 'id' in the app's App Store address "
                             "(apps.apple.com/.../id<digits>). Apple's robots.txt refuses search by name.")
        app = gt_appstore.lookup(f, app_id, country=country)
        summary = gt_appstore.summarize(app)
        gc.write_json(run / "data" / "appstore.json", app)
        others = gt_appstore.developer_apps(f, app["artistId"], country) if app.get("artistId") else []
        gc.write_csv(run / "data" / "appstore-developer-apps.csv", [gt_appstore.summarize(o) for o in others],
                     gt_appstore.LOOKUP_FIELDS)
        fields = {"app_id": str(app["trackId"]), "app_name": app.get("trackName")}
        seller = app.get("sellerUrl")
        if seller and not meta.get("domain"):
            host = urllib.parse.urlsplit(seller).netloc.lower()
            fields["domain"] = host[4:] if host.startswith("www.") else host
        gc.update_run(run, **fields)
        say("%s (id %s) by %s" % (summary["trackName"], summary["trackId"], summary["artistName"]),
            "released %s; version %s of %s" % (summary["releaseDate"], summary["version"], summary["currentVersionReleaseDate"]),
            "rating %s from %s ratings; price %s; genre %s" % (summary["averageUserRating"], summary["userRatingCount"],
                                                             summary["formattedPrice"], summary["primaryGenreName"]),
            "seller site: %s; developer has %d apps" % (seller, len(others)),
            "-> data/appstore.json, data/appstore-developer-apps.csv")
    elif a.action == "listing":
        app = gc.read_json(run / "data" / "appstore.json")
        found = gt_appstore.listing(f, app)
        gc.write_json(run / "data" / "appstore-listing.json", found)
        gc.write_csv(run / "data" / "appstore-versions.csv", found["versions"], gt_appstore.VERSION_FIELDS)
        say("subtitle: %s" % (found["subtitle"] or "not seen"),
            "in-app purchases: %s" % ("; ".join("%s %s" % (p["name"], p["price"]) for p in found["in_app_purchases"])
                                      or "none listed"),
            "versions listed: %d, newest %s" % (len(found["versions"]), (found["versions"] or [{}])[0].get("date", "-")),
            "-> data/appstore-listing.json, data/appstore-versions.csv")
    elif a.action == "chart":
        app = gc.read_json(run / "data" / "appstore.json")
        rows, summary = gt_appstore.chart(f, app, country)
        gc.write_csv(run / "data" / "appstore-chart.csv", rows, gt_appstore.CHART_FIELDS)
        gc.write_json(run / "data" / "appstore-chart.json", summary)
        say("%s charts (%s): %s" % (summary["genre"], ", ".join("%s %d" % kv for kv in summary["chart_lengths"].items()),
                                    ", ".join("#%d in %s" % (p, c) for c, p in summary["positions"].items())
                                    or "not in the top 200 of either chart"),
            "-> data/appstore-chart.csv, data/appstore-chart.json")
    elif a.action == "history":
        app = gc.read_json(run / "data" / "appstore.json")
        rows = gt_appstore.history(f, app, country)
        gc.write_csv(run / "data" / "appstore-history.csv", rows, gt_appstore.HISTORY_FIELDS)
        if rows:
            say("%d monthly snapshots, %s (%s ratings) to %s (%s ratings) -> data/appstore-history.csv" % (
                len(rows), rows[0]["month"], rows[0]["ratings"], rows[-1]["month"], rows[-1]["ratings"]))
        else:
            say("No archived App Store page with a ratings count was found.")
    elif a.action == "screenshots":
        app = gc.read_json(run / "data" / "appstore.json")
        saved = gt_appstore.screenshots(f, app, run / "img" / "appstore")
        rows = [{"channel": "appstore", "kind": "screenshot", "id": "%02d" % s["index"], "url": s["url"],
                 "image": rel(run, s["file"]) if s["file"] else "", "title": "App Store screenshot %d" % s["index"]}
                for s in saved]
        gc.write_csv(run / "data" / "appstore-screenshots.csv", rows, POST_FIELDS)
        say("%d of %d screenshots saved -> img/appstore/, data/appstore-screenshots.csv" % (
            sum(1 for s in saved if s["file"]), len(saved)))


def cmd_site(a):
    run = run_dir(a.run)
    f = gc.Fetcher(run, refresh=a.refresh)
    domain = domain_of(run, a.domain)
    if a.action == "handles":
        rows = gt_web.handles(f, domain)
        gc.write_csv(run / "data" / "handles.csv", rows, ["network", "handle", "url", "found_on"])
        for r in rows:
            say("  %-10s %s" % (r["network"], r["url"]))
        say("%d accounts linked from the home page -> data/handles.csv" % len(rows))
    elif a.action == "map":
        urls, maps = gt_web.sitemap(f, domain)
        gc.write_csv(run / "data" / "site-urls.csv", urls, ["url", "lastmod"])
        fams = gt_web.families(urls)
        gc.write_csv(run / "data" / "site-families.csv", fams,
                     ["family", "segment", "count", "first_lastmod", "last_lastmod", "example"])
        say("%d URLs from %d sitemaps; top families:" % (len(urls), len(maps)))
        for g in fams[:15]:
            say("  %-22s /%-24s %5d  %s..%s" % (g["family"], g["segment"], g["count"], g["first_lastmod"], g["last_lastmod"]))
        say("-> data/site-urls.csv, data/site-families.csv")
    elif a.action == "aasa":
        found = gt_web.aasa(f, domain)
        if not found:
            say("No apple-app-site-association file on %s." % domain)
            return
        gc.write_json(run / "data" / "aasa.json", found)
        for p in found["paths"]:
            say("  %s%s %s" % ("NOT " if p["exclude"] else "", p["path"], p["comment"]))
        say("%d universal-link rules -> data/aasa.json" % len(found["paths"]))
    elif a.action == "history":
        if not a.url:
            raise SystemExit("site history needs --url")
        rows = gt_web.page_history(f, a.url)
        name = a.name or gc.slugify(urllib.parse.urlsplit(a.url).path or "home")
        out = run / "data" / ("history-%s.csv" % name)
        gc.write_csv(out, rows, ["month", "snapshot", "title", "first_line", "prices", "trials", "snapshot_url"])
        for r in rows:
            say("  %s  %-40s %s %s" % (r["month"], r["first_line"][:40], r["prices"][:50], r["trials"]))
        say("%d monthly snapshots -> %s" % (len(rows), rel(run, out)))


def cmd_rea(a):
    run = run_dir(a.run)
    f = gc.Fetcher(run)
    try:
        path = gt_rea.capture(f, a.name, a.url, wait_ms=a.wait, bodies=a.bodies)
    except gt_rea.ReaUnavailable as exc:
        raise SystemExit("REA capture failed: %s\nFall back to `gt.py stack --html %s` (static tags only)." % (exc, a.url))
    urls = gt_stack.urls_from_rea(gt_rea.load(path))
    say("%d requests captured -> %s" % (len(urls), rel(run, path)))


def cmd_stack(a):
    run = run_dir(a.run)
    rows = []
    domain = gc.load_run(run).get("domain", "")
    unknown = {}
    pages = []
    for name in a.rea or []:
        path = Path(name) if name.endswith(".json") else run / "data" / "rea" / ("%s.json" % name)
        urls = gt_stack.load_capture(path)
        found = gt_stack.detect(urls, page=name, source="rea")
        rows += found
        hosts = {}
        for url in urls:
            host = urllib.parse.urlsplit(url).netloc or "(inline)"
            hosts[host] = hosts.get(host, 0) + 1
        pages.append({"page": name, "requests": len(urls), "tools": "; ".join(r["name"] for r in found),
                      "hosts": "; ".join("%s %d" % kv for kv in sorted(hosts.items(), key=lambda kv: -kv[1]))})
        for host, count in gt_stack.third_party_hosts(urls, domain):
            unknown[host] = unknown.get(host, 0) + count
    if pages:
        gc.write_csv(run / "data" / "stack-pages.csv", pages, ["page", "requests", "tools", "hosts"])
    for url in a.html or []:
        f = gc.Fetcher(run)
        page = f.get(url)
        urls = gt_stack.urls_from_html(page.text(), url)
        rows += gt_stack.detect(urls, page.text(), page=url, source="static html")
    merged = {}
    for r in rows:
        m = merged.setdefault(r["name"], dict(r, pages=set(), sources=set(), ids=set()))
        m["pages"].add(r["page"])
        m["sources"].add(r["source"])
        m["ids"].update(i for i in r["ids"].split() if i)
        m["requests"] = max(m["requests"], r["requests"])
    out_rows = [dict(m, pages=" ".join(sorted(m["pages"])), sources=" ".join(sorted(m["sources"])),
                     ids=" ".join(sorted(m["ids"]))) for m in merged.values()]
    order = [s[1] for s in gt_stack.SIGNATURES]
    out_rows.sort(key=lambda r: (order.index(r["category"]), r["name"]))
    gc.write_csv(run / "data" / "stack.csv", out_rows, ["category", "name", "ids", "requests", "pages", "sources", "example"])
    gc.write_csv(run / "data" / "stack-unknown-hosts.csv",
                 [{"host": h, "requests": c} for h, c in sorted(unknown.items(), key=lambda kv: -kv[1])], ["host", "requests"])
    for r in out_rows:
        say("  %-26s %-28s %s" % (r["category"], r["name"], r["ids"]))
    say("%d tools -> data/stack.csv; %d unnamed third-party hosts -> data/stack-unknown-hosts.csv" % (
        len(out_rows), len(unknown)))


def cmd_ads(a):
    run = run_dir(a.run)
    f = gc.Fetcher(run)
    domain = domain_of(run, a.domain)
    try:
        rows, summary = gt_ads.google(f, domain, a.region)
    except gt_rea.ReaUnavailable as exc:
        raise SystemExit("REA capture failed: %s\nCapture the Transparency Center by hand instead (capture kit)." % exc)
    if a.images:
        for row in rows:
            if row["preview_kind"] == "image" and row["preview_url"]:
                try:
                    dest = run / "img" / "ads-google" / ("%s.jpg" % row["creative_id"])
                    f.save(row["preview_url"], dest)
                    row["image"] = rel(run, dest)
                except (gc.Blocked, gc.FetchError):
                    continue
    gc.write_csv(run / "data" / "ads-google.csv", rows, gt_ads.GOOGLE_FIELDS)
    gc.write_json(run / "data" / "ads-google-summary.json", summary)
    formats = {}
    for r in rows:
        formats[r["format"]] = formats.get(r["format"], 0) + 1
    long_runners = [r for r in rows if r["running_60_plus"]]
    advertisers = sorted({r["advertiser"] for r in rows})
    say("page shows about %s creatives for %s in %s; read %d: %s" % (
        summary["shown_total"] or "?", domain, a.region, len(rows), ", ".join("%s %d" % kv for kv in sorted(formats.items()))),
        "advertiser name(s): %s" % ", ".join(advertisers),
        "%d of the creatives read ran 60+ days (first to last shown)" % len(long_runners),
        "-> data/ads-google.csv, data/ads-google-summary.json")


def cmd_social(a):
    run = run_dir(a.run)
    f = gc.Fetcher(run, refresh=a.refresh)
    if a.network == "tiktok":
        profile = gt_web.tiktok_profile(f, a.handle)
        if not profile:
            say("The TikTok profile page held no profile data; capture it by hand (capture kit).")
            return
        gc.write_json(run / "data" / "tiktok-profile.json", profile)
        say("@%s: %s followers, %s likes, %s videos; bio link %s -> data/tiktok-profile.json" % (
            profile["handle"], profile["followers"], profile["likes"], profile["videos"], profile["bio_link"]),
            "Per-video plays come from the capture kit (TikTok serves its video list only to a full browser).")
    elif a.network == "youtube":
        rows, route = gt_web.youtube(f, a.handle)
        for row in rows:
            row["source"] = route
        if a.images:
            gt_web.save_images(f, rows, run / "img" / "youtube")
            for row in rows:
                if row.get("image"):
                    row["image"] = rel(run, row["image"])
        gc.write_csv(run / "data" / "youtube-posts.csv", rows, POST_FIELDS)
        say("%d YouTube uploads via %s%s -> data/youtube-posts.csv" % (
            len(rows), route, " (rounded counts, relative dates)" if route == "channel-page" else ""))
    elif a.network == "bluesky":
        rows = gt_web.bluesky(f, a.handle)
        if a.images:
            gt_web.save_images(f, rows, run / "img" / "bluesky")
            for row in rows:
                if row.get("image"):
                    row["image"] = rel(run, row["image"])
        gc.write_csv(run / "data" / "bluesky-posts.csv", rows, POST_FIELDS)
        say("%d Bluesky posts -> data/bluesky-posts.csv" % len(rows))


def cmd_mentions(a):
    run = run_dir(a.run)
    f = gc.Fetcher(run, refresh=a.refresh)
    rows = gt_web.hn(f, a.query)
    gc.write_csv(run / "data" / "mentions-hn.csv", rows, ["date", "title", "url", "points", "comments", "author", "hn_url"])
    top = sorted(rows, key=lambda r: -int(r["points"] or 0))[:5]
    for r in top:
        say("  %s  %4s pts  %s" % (r["date"][:10], r["points"], r["title"][:80]))
    say("%d Hacker News stories -> data/mentions-hn.csv" % len(rows))


def cmd_suggest(a):
    run = run_dir(a.run)
    f = gc.Fetcher(run, refresh=a.refresh)
    rows = []
    for seed in a.seeds:
        rows += gt_web.suggest(f, seed, expand=a.expand, country=gc.load_run(run).get("country", "us"))
    out = run / "data" / "suggest.csv"
    previous = [r for r in gc.read_csv(out) if r["seed"] not in set(a.seeds)]
    gc.write_csv(out, previous + rows, ["seed", "query", "suggestion", "position"])
    say("%d autocomplete phrases -> data/suggest.csv" % len(rows))
    for r in rows[:20]:
        say("  " + r["suggestion"])


def cmd_jobs(a):
    run = run_dir(a.run)
    f = gc.Fetcher(run, refresh=a.refresh)
    board, rows = gt_web.jobs(f, a.slug)
    gc.write_csv(run / "data" / "jobs.csv", rows, ["board", "title", "team", "location", "updated", "channel", "url"])
    if not board:
        say("No public Greenhouse, Lever, or Ashby board for '%s'; read the careers page with `gt.py read`." % a.slug)
        return
    for r in rows:
        say("  %-44s %-20s %s" % (r["title"][:44], r["channel"][:20], r["updated"][:10]))
    say("%d open roles on %s -> data/jobs.csv" % (len(rows), board))


def cmd_capture_kit(a):
    run = run_dir(a.run)
    out, steps = gt_capture.checklist(run)
    say("%d capture steps -> %s; record each screenshot in %s" % (steps, rel(run, out), gc.CAPTURES_NAME))


def cmd_analyze(a):
    run = run_dir(a.run)
    now = gc.utc_now()
    if a.what == "rank":
        path = run / "data" / ("%s-posts.csv" % a.channel)
        rows = gc.read_csv(path)
        if not rows:
            raise SystemExit("No rows in %s." % rel(run, path))
        ranked, summary = gt_analyze.rank(rows, now)
        fields = list(dict.fromkeys(list(rows[0].keys()) + ["tier", "metric_value", "age_days", "spread_per_day",
                                                            "fast_spreader"]))
        gc.write_csv(path, ranked, fields)
        summary.update({"channel": a.channel, "ranked_at": gc.iso_z(now)})
        gc.write_json(run / "data" / ("%s-rank.json" % a.channel), summary)
        say(json.dumps(summary, indent=2))
    elif a.what == "growth":
        ratings = gt_analyze.ratings_series(gc.read_csv(run / "data" / "appstore-history.csv"))
        trends = {}
        for path in sorted((run / "capture" / "trends").glob("*.csv")) if (run / "capture" / "trends").exists() else []:
            trends.update(gt_analyze.parse_trends(path.read_text(encoding="utf-8")))
        series = gt_analyze.merge_growth(ratings, trends)
        fields = list(dict.fromkeys(["month", "ratings", "ratings_per_day"] + [k for r in series for k in r.keys()]))
        gc.write_csv(run / "data" / "growth.csv", series, fields)
        point = gt_analyze.inflection(series)
        result = {"months": len(series), "ratings_points": len(ratings), "trends_terms": sorted(trends),
                  "inflection": point, "computed_at": gc.iso_z(now)}
        gc.write_json(run / "data" / "growth-summary.json", result)
        say(json.dumps(result, indent=2))
    elif a.what == "moves":
        moves = gc.read_csv(run / "data" / "moves.csv")
        series = gc.read_csv(run / "data" / "growth.csv")
        if not moves or not series:
            raise SystemExit("Needs data/moves.csv (date, channel, kind, label, url, reach) and data/growth.csv.")
        lifts = gt_analyze.moves_vs_growth(moves, series, a.key)
        gc.write_csv(run / "data" / "moves-vs-growth.csv", lifts, list(lifts[0].keys()) if lifts else ["cluster_start"])
        corr = gt_analyze.channel_correlations(moves, series, a.key)
        gc.write_csv(run / "data" / "moves-correlation.csv", corr,
                     ["channel", "lag_months", "months", "moves", "rho", "note"])
        for r in sorted(lifts, key=lambda r: -(r["lift"] if isinstance(r["lift"], (int, float)) else -1e18))[:5]:
            say("  %s..%s  %-28s lift %s (%s%%) %s" % (r["cluster_start"], r["cluster_end"], r["channels"][:28],
                                                        r["lift"], r["lift_pct"], r["note"]))
        say("-> data/moves-vs-growth.csv, data/moves-correlation.csv")


def cmd_render(a):
    run = run_dir(a.run)
    out = gt_render.render(run, link_images=a.link_images)
    say("-> %s (%d KB)" % (rel(run, out), out.stat().st_size // 1024))


def cmd_check(a):
    run = run_dir(a.run)
    problems = gt_check.check(run)
    if problems:
        say("%d problem(s):" % len(problems), *("  - " + p for p in problems))
        return 1
    say("OK: every cited URL was read or captured, plays are complete, and the HTML is current.")
    return 0


def cmd_status(a):
    run = run_dir(a.run)
    meta = gc.load_run(run)
    say("%s: %s for %s (%s mode, %s)" % (run.name, meta.get("target"), meta.get("product"), meta.get("mode"),
                                         meta.get("country")))
    sources = gc.read_csv(run / "sources.csv")
    statuses = {}
    for r in sources:
        statuses[r["status"]] = statuses.get(r["status"], 0) + 1
    say("reads logged: %d (%s)" % (len(sources), ", ".join("%s %d" % kv for kv in sorted(statuses.items()))))
    for path in sorted((run / "data").glob("*.csv")):
        say("  %-36s %5d rows" % (rel(run, path), len(gc.read_csv(path))))
    captures = gc.read_csv(run / gc.CAPTURES_NAME)
    say("captures recorded: %d" % len(captures))


def build_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command")
    sub.required = True

    s = sub.add_parser("init", help="start a run folder")
    s.add_argument("product", help="the Mandu Product folder, e.g. RepToday")
    s.add_argument("target", help="the company or app to tear down, e.g. Ladder")
    s.add_argument("--mode", choices=["full", "content"], default="full")
    s.add_argument("--country", default="us")
    s.add_argument("--domain")
    s.add_argument("--app-id")
    s.set_defaults(func=cmd_init)

    s = sub.add_parser("robots", help="ask whether robots.txt allows a URL")
    s.add_argument("url")
    s.set_defaults(func=cmd_robots)

    def with_run(name, func, help_text):
        sp = sub.add_parser(name, help=help_text)
        sp.add_argument("run", help="the run folder")
        sp.add_argument("--refresh", action="store_true", help="refetch instead of reading the cache")
        sp.set_defaults(func=func)
        return sp

    s = with_run("read", cmd_read, "read one page's visible text into data/pages/")
    s.add_argument("url")
    s.add_argument("--save", help="file name under data/pages/")
    s.add_argument("--print", action="store_true", help="also print the text")
    s.add_argument("--max-chars", type=int, default=6000)

    s = with_run("appstore", cmd_appstore, "App Store lookup, live listing, category chart, ratings history, screenshots")
    s.add_argument("action", choices=["lookup", "listing", "chart", "history", "screenshots"])
    s.add_argument("--id", help="for lookup: the App Store id (digits after 'id' in its address)")
    s.add_argument("--country")

    s = with_run("site", cmd_site, "the target's site: handles, sitemap families, universal links, page history")
    s.add_argument("action", choices=["handles", "map", "aasa", "history"])
    s.add_argument("--domain")
    s.add_argument("--url", help="for history: the page to trace")
    s.add_argument("--name", help="for history: a short name for the output file")

    s = with_run("rea", cmd_rea, "capture one page with REA's browser")
    s.add_argument("name", help="a short name, e.g. home or pricing")
    s.add_argument("url")
    s.add_argument("--wait", type=int, default=6000, help="milliseconds to let the page settle")
    s.add_argument("--bodies", action="store_true", help="keep response bodies")

    s = with_run("stack", cmd_stack, "name the growth tools from REA captures and static HTML")
    s.add_argument("--rea", action="append", help="a capture name in data/rea/, or a HAR or REA JSON path")
    s.add_argument("--html", action="append", help="a page URL to read static tags from")

    s = with_run("ads", cmd_ads, "ads from Google's Ads Transparency Center (through REA)")
    s.add_argument("network", choices=["google"])
    s.add_argument("--domain")
    s.add_argument("--region", default="US")
    s.add_argument("--images", action="store_true", help="download image creatives into img/ads-google/")

    s = with_run("social", cmd_social, "public profile data: TikTok stats, YouTube uploads, Bluesky posts")
    s.add_argument("network", choices=["tiktok", "youtube", "bluesky"])
    s.add_argument("handle")
    s.add_argument("--images", action="store_true", help="download thumbnails")

    s = with_run("mentions", cmd_mentions, "Hacker News stories that name the target")
    s.add_argument("source", choices=["hn"])
    s.add_argument("query")

    s = with_run("suggest", cmd_suggest, "Google autocomplete phrases for seeds")
    s.add_argument("seeds", nargs="+")
    s.add_argument("--expand", action="store_true", help="also seed + each letter a-z")

    s = with_run("jobs", cmd_jobs, "open roles from Greenhouse, Lever, or Ashby")
    s.add_argument("slug", help="the company's job-board slug, e.g. ladder")

    s = with_run("capture-kit", cmd_capture_kit, "write capture/CHECKLIST.md for hcho's by-hand captures")

    s = with_run("analyze", cmd_analyze, "rank a channel, build the growth series, or line moves up with growth")
    s.add_argument("what", choices=["rank", "growth", "moves"])
    s.add_argument("channel", nargs="?", help="for rank: the <channel> in data/<channel>-posts.csv")
    s.add_argument("--key", default="ratings_per_day", help="for moves: the growth column to read")

    s = with_run("render", cmd_render, "render playbook.md or content.md to one HTML file")
    s.add_argument("--link-images", action="store_true", help="link images instead of embedding them")

    with_run("check", cmd_check, "check the finished run")
    with_run("status", cmd_status, "what the run holds so far")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        code = args.func(args)
    except gc.Blocked as exc:
        print("BLOCKED: %s" % exc, file=sys.stderr)
        return 3
    except gc.FetchError as exc:
        print("FAILED: %s" % exc, file=sys.stderr)
        return 4
    return code or 0


if __name__ == "__main__":
    sys.exit(main())
