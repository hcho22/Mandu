"""Tests for gr0wth-teardown's scripts: the robots.txt gate, the fetcher, every
parser (on fixtures shaped like the real responses read on 2026-10-30), the
arithmetic, the renderer, and the run check. No test touches the network.

Run from Mandu's root: python3 -m unittest discover -s .claude/skills/gr0wth-teardown/tests
"""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import gt_ads  # noqa: E402
import gt_analyze as ga  # noqa: E402
import gt_appstore  # noqa: E402
import gt_check  # noqa: E402
import gt_common as gc  # noqa: E402
import gt_render  # noqa: E402
import gt_stack  # noqa: E402
import gt_web  # noqa: E402

UTC = dt.timezone.utc


class FakeOpener:
    """Answers requests from a table {url: (status, headers, body)}; records every call."""

    def __init__(self, table, default=(404, {}, b"")):
        self.table = table
        self.default = default
        self.calls = []

    def __call__(self, url, data=None, headers=None, timeout=30):
        self.calls.append(url)
        answer = self.table.get(url, self.default)
        if isinstance(answer, list):  # a sequence of answers for repeated calls
            answer = answer.pop(0) if len(answer) > 1 else answer[0]
        status, hdrs, body = answer
        if isinstance(body, str):
            body = body.encode()
        return status, hdrs, body, url


def make_run(tmp):
    return gc.new_run("RepToday", "Example App", "full", "us", base=Path(tmp) / "teardowns")


# ---------------------------------------------------------------- robots.txt


class RobotsRules(unittest.TestCase):
    APPLE = """User-agent: *
Disallow: /*/rss/*
Disallow: /search*
Disallow: /WebObjects/*
"""

    def verdict(self, text, path, token=gc.TOOL_TOKEN):
        return gc.robots_verdict(gc.parse_robots(text), token, path)[0]

    def test_wildcards_refuse_the_review_feed_and_search(self):
        self.assertFalse(self.verdict(self.APPLE, "/us/rss/customerreviews/page=1/id=1/sortby=mostrecent/json"))
        self.assertFalse(self.verdict(self.APPLE, "/search?term=workout&entity=software"))
        self.assertTrue(self.verdict(self.APPLE, "/lookup?id=1502936453&entity=software"))

    def test_longest_match_wins_and_allow_wins_a_tie(self):
        text = "User-agent: *\nDisallow: /a\nAllow: /a/b\nDisallow: /x\nAllow: /x\n"
        self.assertTrue(self.verdict(text, "/a/b/c"))
        self.assertFalse(self.verdict(text, "/a/c"))
        self.assertTrue(self.verdict(text, "/x"))

    def test_end_anchor(self):
        text = "User-agent: *\nDisallow: /*.json$\n"
        self.assertFalse(self.verdict(text, "/feed.json"))
        self.assertTrue(self.verdict(text, "/feed.json?x=1"))

    def test_the_tool_group_beats_star_and_an_empty_disallow_allows(self):
        text = "User-agent: *\nDisallow: /\n\nUser-agent: Mandu-gr0wth-teardown\nDisallow:\n"
        self.assertTrue(self.verdict(text, "/anything"))
        self.assertFalse(self.verdict(text, "/anything", token="otherbot"))

    def test_groups_with_several_agents_and_crawl_delay(self):
        text = "User-agent: a\nUser-agent: *\nCrawl-delay: 5\nDisallow: /private\n"
        allowed, rule, delay = gc.robots_verdict(gc.parse_robots(text), gc.TOOL_TOKEN, "/private/x")
        self.assertFalse(allowed)
        self.assertEqual(delay, 5.0)
        self.assertEqual(rule, "Disallow: /private")


class RobotsFetch(unittest.TestCase):
    def check(self, answer, url="https://example.com/page"):
        opener = FakeOpener({"https://example.com/robots.txt": answer})
        return gc.Robots(opener=opener).check(url)

    def test_status_handling(self):
        self.assertTrue(self.check((404, {}, ""))[0])
        self.assertTrue(self.check((403, {}, ""))[0])
        self.assertFalse(self.check((503, {}, ""))[0])
        self.assertFalse(self.check((429, {}, ""))[0])

    def test_an_html_page_is_not_a_robots_txt(self):
        self.assertFalse(self.check((200, {"Content-Type": "text/html"}, "<!doctype html><html></html>"))[0])

    def test_a_network_filter_page_refuses(self):
        self.assertFalse(self.check((200, {}, 'var url="https://myhomenetwork.att.com"; networkprotected'))[0])

    def test_redirects_are_followed(self):
        opener = FakeOpener({
            "https://example.com/robots.txt": (308, {"Location": "https://www.example.com/robots.txt"}, ""),
            "https://www.example.com/robots.txt": (200, {}, "User-agent: *\nDisallow: /secret\n"),
        })
        robots = gc.Robots(opener=opener)
        self.assertFalse(robots.check("https://example.com/secret/x")[0])
        self.assertTrue(robots.check("https://example.com/open")[0])

    def test_an_unreachable_robots_txt_is_not_cached(self):
        with tempfile.TemporaryDirectory() as tmp:
            def boom(url, **_kw):
                raise OSError("no network")
            self.assertFalse(gc.Robots(tmp, opener=boom).check("https://example.com/x")[0])
            self.assertEqual(os.listdir(tmp), [])


# ---------------------------------------------------------------- the fetcher


class FetcherTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.run = make_run(self.tmp.name)
        self.sleeps = []

    def tearDown(self):
        self.tmp.cleanup()

    def fetcher(self, table):
        table.setdefault("https://example.com/robots.txt", (200, {}, "User-agent: *\nDisallow: /no\n"))
        table.setdefault("https://www.example.com/robots.txt", (200, {}, "User-agent: *\nDisallow: /blocked\n"))
        self.opener = FakeOpener(table)
        return gc.Fetcher(self.run, opener=self.opener, sleep=self.sleeps.append, clock=lambda: 0.0)

    def sources(self):
        return gc.read_csv(self.run / "sources.csv")

    def test_a_refused_url_is_logged_and_raises(self):
        f = self.fetcher({})
        with self.assertRaises(gc.Blocked):
            f.get("https://example.com/no/thing")
        self.assertEqual(self.sources()[-1]["status"], "robots-denied")
        self.assertNotIn("https://example.com/no/thing", self.opener.calls)

    def test_http_is_upgraded_and_responses_are_cached(self):
        f = self.fetcher({"https://example.com/a": (200, {}, "hello")})
        self.assertEqual(f.get("http://example.com/a").text(), "hello")
        again = f.get("https://example.com/a")
        self.assertTrue(again.from_cache)
        self.assertEqual(self.opener.calls.count("https://example.com/a"), 1)

    def test_each_redirect_hop_is_gated(self):
        f = self.fetcher({"https://example.com/go": (301, {"Location": "https://www.example.com/blocked/x"}, "")})
        with self.assertRaises(gc.Blocked):
            f.get("https://example.com/go")
        f2 = self.fetcher({"https://example.com/ok": (308, {"Location": "https://www.example.com/fine"}, ""),
                           "https://www.example.com/fine": (200, {}, "done")})
        response = f2.get("https://example.com/ok")
        self.assertEqual(response.text(), "done")
        self.assertEqual(response.url, "https://www.example.com/fine")

    def test_throttling_is_retried_and_never_cached(self):
        f = self.fetcher({"https://example.com/slow": [(429, {"Retry-After": "7"}, ""), (200, {}, "ok")]})
        self.assertEqual(f.get("https://example.com/slow").text(), "ok")
        self.assertIn(7.0, self.sleeps)
        f = self.fetcher({"https://example.com/busy": (429, {}, "")})
        self.assertEqual(f.get("https://example.com/busy", retries=1).status, 429)
        self.assertEqual(self.sources()[-1]["note"], "not cached")
        self.assertFalse(f.get("https://example.com/busy", retries=0).from_cache)

    def test_secrets_never_reach_the_log(self):
        f = self.fetcher({"https://example.com/api?key=SECRET123&q=1": (200, {}, "{}")})
        f.get("https://example.com/api?key=SECRET123&q=1", secrets=("SECRET123",))
        text = (self.run / "sources.csv").read_text()
        self.assertNotIn("SECRET123", text)
        self.assertIn("key=REDACTED", text)
        for meta in (self.run / "data" / "raw").rglob("*.json"):
            self.assertNotIn("SECRET123", meta.read_text())

    def test_a_filter_page_is_refused(self):
        f = self.fetcher({"https://example.com/p": (200, {}, "<script>var url='https://myhomenetwork.att.com'</script>")})
        with self.assertRaises(gc.Blocked):
            f.get("https://example.com/p")

    def test_gzip_bodies_are_decompressed(self):
        import gzip
        self.assertEqual(gc._decompress(gzip.compress(b"abc"), ""), b"abc")
        self.assertEqual(gc._decompress(b"plain", ""), b"plain")


# ---------------------------------------------------------------- App Store parsers


SERIALIZED = '<script type="application/json" id="serialized-server-data">%s</script>'


class AppStoreParsers(unittest.TestCase):
    def test_json_ld_ratings(self):
        html = ('<script type="application/ld+json">{"@type":"SoftwareApplication","softwareVersion":"4.9.0",'
                '"aggregateRating":{"@type":"AggregateRating","ratingValue":4.9,"reviewCount":14751},'
                '"offers":{"@type":"Offer","price":0}}</script>')
        parsed = gt_appstore.parse_listing(html)
        self.assertEqual(parsed["ratings"], 14751)
        self.assertTrue(parsed["ratings_exact"])
        self.assertEqual(parsed["rating_value"], 4.9)
        self.assertEqual(parsed["version"], "4.9.0")

    def test_old_page_fallbacks(self):
        html = '<h2 class="product-header__subtitle app-header__subtitle">Fitness, Workouts, Coaching</h2> 14.8K Ratings'
        parsed = gt_appstore.parse_listing(html)
        self.assertEqual(parsed["ratings"], 14800)
        self.assertFalse(parsed["ratings_exact"])
        self.assertEqual(parsed["subtitle"], "Fitness, Workouts, Coaching")

    def test_live_listing(self):
        data = {"data": [{"data": {"shelves": [
            {"items": [{"title": "LADDER Strength Training Plans", "subtitle": "Fitness Workouts at Home & Gym"}]},
            {"items": [{"$kind": "Annotation", "title": "In-App Purchases", "summary": "Yes",
                        "items": [{"leadingText": "PRO", "trailingText": "$29.99"},
                                  {"leadingText": "PRO Annual", "trailingText": "$179.99"}]},
                       {"$kind": "Annotation", "title": "Size", "summary": "253.4 MB", "items": []}]},
            {"page": "versionHistory", "pageData": {"shelves": [{"items": [
                {"$kind": "TitledParagraph", "text": "This version includes the following:\n\n- Faster logging",
                 "primarySubtitle": "4.16.1", "secondarySubtitle": "Fri Oct 30 2026 15:16:56 GMT+0000 (UTC)"}]}]}},
        ]}}]}
        parsed = gt_appstore.parse_live_listing(SERIALIZED % json.dumps(data), "LADDER Strength Training Plans")
        self.assertEqual(parsed["subtitle"], "Fitness Workouts at Home & Gym")
        self.assertEqual([p["price"] for p in parsed["in_app_purchases"]], ["$29.99", "$179.99"])
        self.assertEqual(parsed["facts"]["Size"], "253.4 MB")
        self.assertEqual(parsed["versions"][0], {"version": "4.16.1", "date": "2026-10-30", "notes": "- Faster logging"})

    def test_chart_positions_span_items_and_remaining_ids(self):
        segment = {"$kind": "TopChartSegment", "chart": "top-free",
                   "shelves": [{"items": [{"adamId": "1", "title": "A"}, {"adamId": "2", "title": "B"}]}],
                   "nextPage": {"remainingContent": [{"id": "3"}, {"id": "1502936453"}]}}
        charts = gt_appstore.parse_chart(SERIALIZED % json.dumps({"segments": [segment]}))
        self.assertEqual([e[1] for e in charts["top-free"]], ["1", "2", "3", "1502936453"])
        self.assertEqual(charts["top-free"][3][0], 4)

    def test_listing_urls_cover_both_domains(self):
        urls = gt_appstore.listing_urls({"trackId": 9, "trackViewUrl": "https://apps.apple.com/us/app/x/id9?uo=4"})
        self.assertIn("https://apps.apple.com/us/app/x/id9", urls)
        self.assertIn("https://itunes.apple.com/us/app/x/id9", urls)
        self.assertEqual(len(urls), len(set(urls)))


# ---------------------------------------------------------------- ads and stack


class AdsAndStack(unittest.TestCase):
    def test_google_creatives(self):
        body = json.dumps({"1": [
            {"1": "AR1", "2": "CR1", "3": {"3": {"2": '<img src="https://tpc.googlesyndication.com/archive/simgad/1" height="2">'}},
             "4": 1, "6": {"1": "1764949270"}, "7": {"1": "1793389972"}, "12": "MILTON FINCH, INC.", "13": 144,
             "14": "joinladder.com"},
            {"1": "AR1", "2": "CR2", "3": {"1": {"4": "https://displayads-formats.googleusercontent.com/ads/preview/content.js?x=1"}},
             "4": 3, "6": {"1": "1776804204"}, "7": {"1": "1779136561"}, "12": "MILTON FINCH, INC.", "13": 28,
             "14": "joinladder.com"}], "4": "100", "5": "200"}).encode()
        rows, total = gt_ads.parse_search_creatives(body)
        self.assertEqual(total, "200")
        self.assertEqual(rows[0]["format"], "text")
        self.assertEqual(rows[0]["preview_kind"], "image")
        self.assertEqual(rows[0]["first_shown"], "2025-12-05")
        self.assertTrue(rows[0]["running_60_plus"])
        self.assertEqual(rows[1]["format"], "video")
        self.assertEqual(rows[1]["preview_kind"], "script")
        self.assertFalse(rows[1]["running_60_plus"])
        self.assertTrue(rows[1]["preview_url"].startswith("https://displayads-formats"))

    def test_detects_tools_and_their_ids(self):
        urls = [
            "https://www.googletagmanager.com/gtm.js?id=GTM-NWJCL3B",
            "https://connect.facebook.net/signals/config/120204865154143?v=2.9",
            "https://analytics.tiktok.com/i18n/pixel/events.js?sdkid=C97L7M3C77U37LFVKAFG&lib=ttq",
            "https://cdn.segment.com/analytics.js/v1/9AXppx/analytics.min.js",
            "https://s.axon.ai/pixel.js",
            "https://toolkit.com/kit.js",
            "https://tracker.example/?ref=https://www.facebook.com/tr?id=1",
        ]
        found = {r["name"]: r for r in gt_stack.detect(urls)}
        self.assertEqual(found["Google Tag Manager"]["ids"], "GTM-NWJCL3B")
        self.assertEqual(found["Meta Pixel"]["ids"], "120204865154143")
        self.assertEqual(found["TikTok Pixel"]["ids"], "C97L7M3C77U37LFVKAFG")
        self.assertEqual(found["Segment"]["ids"], "9AXppx")
        self.assertIn("AppLovin Axon", found)
        self.assertNotIn("Kit (ConvertKit)", found)
        self.assertEqual(found["Meta Pixel"]["requests"], 1)

    def test_inline_ids_and_rea_evidence(self):
        html = "<script>fbq('init', '2199559587058620'); gtag('config', 'AW-10851135234');</script>"
        found = {r["name"]: r for r in gt_stack.detect([], html)}
        self.assertEqual(found["Meta Pixel"]["ids"], "2199559587058620")
        self.assertEqual(found["Google Ads"]["ids"], "AW-10851135234")
        evidence = {"normalized_result": {"events": {"items": [
            {"kind": "request", "url": {"url": "https://a.example/x"}}, {"kind": "response", "url": {"url": "https://b"}}]}}}
        self.assertEqual(gt_stack.urls_from_rea(evidence), ["https://a.example/x"])

    def test_unknown_hosts_skip_first_party_and_known_tools(self):
        urls = ["https://www.joinladder.com/a", "https://cdn.joinladder.com/b", "https://cdn.segment.com/x",
                "https://mystery.example/y"]
        self.assertEqual(gt_stack.third_party_hosts(urls, "joinladder.com"), [("mystery.example", 1)])


# ---------------------------------------------------------------- web parsers


class WebParsers(unittest.TestCase):
    def test_handles_from_links_and_json_ld(self):
        html = ('<a href="https://instagram.com/joinladder">IG</a><a href="https://www.facebook.com/sharer/x">share</a>'
                '<script type="application/ld+json">{"sameAs":["https:\\/\\/twitter.com\\/joinladder"]}</script>')

        class F:
            def get(self, url, **_kw):
                return gc.Response(url, 200, html.encode())
        rows = gt_web.handles(F(), "joinladder.com")
        self.assertEqual({(r["network"], r["handle"]) for r in rows}, {("instagram", "joinladder"), ("x", "joinladder")})

    def test_page_text_skips_scripts(self):
        parsed = gt_web.page_text("<title>T</title><script>var x=1</script><p>Hello <b>you</b></p><a href='/p'>p</a>")
        self.assertEqual(parsed["title"], "T")
        self.assertIn("Hello you", parsed["text"])
        self.assertNotIn("var x", parsed["text"])
        self.assertEqual(parsed["links"], ["/p"])

    def test_families(self):
        rows = [{"url": "https://x.com/blog/a", "lastmod": "2026-01-02"}, {"url": "https://x.com/en/blog/b", "lastmod": "2026-03-04"},
                {"url": "https://x.com/quiz", "lastmod": ""}, {"url": "https://x.com/hilary", "lastmod": ""}]
        fams = {g["family"]: g for g in gt_web.families(rows)}
        self.assertEqual(fams["blog"]["count"], 2)
        self.assertEqual(fams["blog"]["last_lastmod"], "2026-03-04")
        self.assertIn("web-funnel", fams)
        self.assertIn("other:hilary", fams)

    def test_tiktok_profile(self):
        data = {"__DEFAULT_SCOPE__": {"webapp.user-detail": {"userInfo": {
            "user": {"uniqueId": "joinladder", "nickname": "Ladder", "signature": "bio", "bioLink": {"link": "linktr.ee/joinladder"}},
            "stats": {"followerCount": 49500, "heartCount": 626900, "videoCount": 345, "followingCount": 77}}}}}
        html = '<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">%s</script>' % json.dumps(data)
        profile = gt_web.parse_tiktok_profile(html)
        self.assertEqual((profile["followers"], profile["likes"], profile["videos"]), (49500, 626900, 345))
        self.assertIsNone(gt_web.parse_tiktok_profile("<html></html>"))

    def test_youtube_tab(self):
        data = {"contents": [{"videoRenderer": {"videoId": "abc", "title": {"runs": [{"text": "I built it"}]},
                                                "viewCountText": {"simpleText": "1.2M views"},
                                                "publishedTimeText": {"simpleText": "3 months ago"},
                                                "lengthText": {"simpleText": "8:01"}}},
                             {"shortsLockupViewModel": {"onTap": {"innertubeCommand": {"reelWatchEndpoint": {"videoId": "s1"}}},
                                                        "overlayMetadata": {"primaryText": {"content": "Short"},
                                                                            "secondaryText": {"content": "45K views"}}}}]}
        html = "<script>var ytInitialData = %s;</script>" % json.dumps(data)
        rows = gt_web.parse_youtube_tab(html, "video")
        self.assertEqual(rows[0]["metric"], 1200000)
        self.assertEqual(rows[1]["kind"], "short")
        self.assertEqual(rows[1]["metric"], 45000)

    def test_counts_and_channels(self):
        self.assertEqual(gt_web.parse_count("1,234 views"), 1234)
        self.assertEqual(gt_web.parse_count("2.5K"), 2500)
        self.assertIsNone(gt_web.parse_count("no views"))
        self.assertEqual(gt_web.channel_of("Lead Creator, Brand Social"), "creator, content, brand")


# ---------------------------------------------------------------- arithmetic


class Arithmetic(unittest.TestCase):
    NOW = dt.datetime(2026, 10, 30, tzinfo=UTC)

    def test_rank_tiers_and_unsettled_posts(self):
        rows = [{"metric": str(v), "date": "2026-09-%02d" % (i + 1)} for i, v in enumerate([10, 80, 30, 50, 70, 20, 60, 40])]
        rows.append({"metric": "999", "date": "2026-10-28"})
        rows.append({"metric": "", "date": "2026-09-01"})
        ranked, summary = ga.rank(rows, self.NOW)
        tiers = {r["metric"]: r["tier"] for r in ranked}
        self.assertEqual(summary["posts"], 8)
        self.assertEqual(summary["top"], 2)
        self.assertEqual(summary["bottom"], 4)
        self.assertEqual([m for m, t in tiers.items() if t == "top"], ["80", "70"])
        self.assertEqual(tiers["999"], "unsettled")
        self.assertEqual(tiers[""], "unranked")
        self.assertFalse(summary["pattern_callable"])
        self.assertEqual(len(ranked), 10)

    def test_relative_dates(self):
        when = ga.relative_date("3 months ago", self.NOW)
        self.assertEqual(when.strftime("%Y-%m"), "2026-07")
        self.assertIsNone(ga.relative_date("Premiered", self.NOW))

    def test_spearman(self):
        self.assertAlmostEqual(ga.spearman([1, 2, 3, 4], [10, 20, 30, 40]), 1.0)
        self.assertAlmostEqual(ga.spearman([1, 2, 3, 4], [4, 3, 2, 1]), -1.0)
        self.assertAlmostEqual(ga.spearman([1, 2, 2, 3], [1, 2, 3, 4]), 0.9486832980505138)
        self.assertIsNone(ga.spearman([1, 1, 1], [1, 2, 3]))

    def test_ratings_series_and_inflection(self):
        history = [{"snapshot": "20240101000000", "ratings": "1000"}, {"snapshot": "20240201000000", "ratings": "1310"},
                   {"snapshot": "20240301000000", "ratings": "1600"}, {"snapshot": "20240401000000", "ratings": "3150"},
                   {"snapshot": "20240501000000", "ratings": "4650"}, {"snapshot": "20240601000000", "ratings": "6200"}]
        series = ga.ratings_series(history)
        self.assertEqual(series[1]["ratings_per_day"], 10.0)
        self.assertEqual(series[1]["rate_month"], "2024-01")  # the January interval, read on Feb 1
        merged = ga.merge_growth(series)
        self.assertEqual(merged[0], {"month": "2024-01", "ratings": 1000, "ratings_per_day": 10.0,
                                     "rate_interval_days": 31})
        point = ga.inflection(merged)
        self.assertEqual(point["month"], "2024-03")
        self.assertGreater(point["after"], point["before"])

    def test_clusters_and_lift(self):
        series = [{"month": "2024-%02d" % m, "ratings_per_day": v} for m, v in [(1, 10), (2, 10), (3, 30), (4, 30), (5, 30)]]
        moves = [{"date": "2024-03-02", "channel": "tiktok", "label": "a"}, {"date": "2024-03-20", "channel": "ads", "label": "b"},
                 {"date": "2024-03-20", "channel": "celebrity", "label": "same day"},
                 {"date": "2024-05-25", "channel": "x", "label": "c"}]
        groups = ga.clusters(moves)
        self.assertEqual([len(g["moves"]) for g in groups], [3, 1])
        lifts = ga.moves_vs_growth(moves, series)
        self.assertEqual(lifts[0]["lift"], 20.0)
        self.assertEqual(lifts[0]["lift_pct"], 200.0)
        self.assertEqual(lifts[0]["channels"], "ads, celebrity, tiktok")

    def test_correlation_needs_enough_months(self):
        series = [{"month": "2024-%02d" % m, "ratings_per_day": m} for m in range(1, 7)]
        rows = ga.channel_correlations([{"date": "2024-02-01", "channel": "x"}], series)
        self.assertIn("too few", rows[0]["note"])

    def test_trends_export(self):
        text = ("Category: All categories\n\nWeek,ladder app: (United States)\n2024-01-07,40\n2024-01-14,60\n"
                "2024-02-04,<1\n")
        trends = ga.parse_trends(text)
        self.assertEqual(trends["ladder app"], {"2024-01": 50.0, "2024-02": 0.5})


# ---------------------------------------------------------------- render and check


PLAYBOOK = """# Ladder growth teardown

SEEN Ladder ranks #6 in Health & Fitness Top Free ([chart](https://apps.apple.com/us/iphone/charts/6013)).
INFERRED the celebrity campaign targets women over 30.

## The path

| Stage | What |
|---|---|
| Get noticed | Ads |

## Plays

### 1. Ready-on-open hook

- **Stage:** pre-launch
- **Evidence:** SEEN in data/pages/hilary.txt
- **Effort:** day
- **First result:** 7 days - saves per post
- **Cost:** $0

```prompt
Draft three hooks <b>now</b>.
```

## Things to skip

- Celebrity deals.

## Timeline

<!-- gt:growth-chart -->

## By channel

<!-- gt:contact-sheet channel=youtube -->

## 14-day plan

1. Day 1: post.
   - nested detail

## Method notes

- All counts dated.
"""


class RenderAndCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.run = make_run(self.tmp.name)
        gc.write_csv(self.run / "sources.csv", [{"url": "https://apps.apple.com/us/iphone/charts/6013", "status": "200"}],
                     gc.SOURCES_FIELDS)
        gc.write_csv(self.run / "data" / "growth.csv",
                     [{"month": "2024-01", "ratings": "100"}, {"month": "2024-06", "ratings": "900"}], ["month", "ratings"])
        gc.write_csv(self.run / "data" / "moves.csv", [{"date": "2024-03-01", "channel": "ads", "label": "Ads <start>"}],
                     ["date", "channel", "label"])
        (self.run / "playbook.md").write_text(PLAYBOOK, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_render(self):
        out = gt_render.render(self.run)
        page = out.read_text(encoding="utf-8")
        self.assertIn('<button class="copy" type="button">Copy the prompt</button>', page)
        self.assertIn("Draft three hooks &lt;b&gt;now&lt;/b&gt;.", page)
        self.assertIn('<span class="tag seen">SEEN</span>', page)
        self.assertIn("<table>", page)
        self.assertIn('<path class="series"', page)
        self.assertIn("Ads &lt;start&gt;", page)
        self.assertIn("No youtube posts were pulled or captured.", page)
        self.assertIn("<ol><li>Day 1: post.<ul><li>nested detail</li></ul></li></ol>", page)
        self.assertIn('prefers-color-scheme:dark', page)
        self.assertNotIn("\u2014", page)

    def test_chart_scale_uses_round_steps(self):
        self.assertEqual(gt_render._nice_scale(202735), (250000, 50000))
        self.assertEqual(gt_render._nice_scale(900), (1000, 200))
        top, step = gt_render._nice_scale(7)
        self.assertTrue(4 <= top / step <= 6 and top >= 7)

    def test_check_passes_a_clean_run_and_names_each_problem(self):
        gt_render.render(self.run)
        self.assertEqual(gt_check.check(self.run), [])
        text = PLAYBOOK.replace("- **Cost:** $0\n", "") + "\nSEEN a claim with no source.\nSee https://example.com/x \u2014 here.\n"
        (self.run / "playbook.md").write_text(text, encoding="utf-8")
        problems = gt_check.check(self.run)
        joined = "\n".join(problems)
        self.assertIn("em dash", joined)
        self.assertIn("did not read: https://example.com/x", joined)
        self.assertIn("no **Cost:** line", joined)
        self.assertIn("marked SEEN but names no source", joined)
        self.assertIn("older than playbook.md", joined)

    def test_wayback_and_data_urls_are_citable(self):
        gc.write_csv(self.run / "sources.csv", [
            {"url": "https://web.archive.org/web/20240101000000id_/https://apps.apple.com/us/app/x/id1", "status": "200"}],
            gc.SOURCES_FIELDS)
        gc.write_csv(self.run / "data" / "ads-google.csv",
                     [{"ad_url": "https://adstransparency.google.com/advertiser/AR1/creative/CR1"}], ["ad_url"])
        allowed = gt_check.citable(self.run)
        self.assertIn(gt_check._norm("https://web.archive.org/web/20240101000000/https://apps.apple.com/us/app/x/id1"), allowed)
        self.assertIn(gt_check._norm("https://adstransparency.google.com/advertiser/AR1/creative/CR1"), allowed)

    def test_run_numbering(self):
        second = gc.new_run("RepToday", "Other", "content", "us", base=self.run.parent)
        self.assertTrue(second.name.startswith("02-other_"))


if __name__ == "__main__":
    unittest.main()
