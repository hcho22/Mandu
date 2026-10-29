"""Tests for the Candidate Package checks: each passes on the fixture package
and fails when the one thing it guards is broken.

Run from Mandu's root: python3 -m unittest discover -s .claude/skills/gr0wthpilot/tests
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import re
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

import fixtures

import audit_run
import brand_lint
import check_layout
import check_recap
import check_screenshots
import check_sources
import check_video
import claim_audit
import gp_common as gc
import journal
import rename

FETCHED = fixtures.FETCHED
REGISTRY = str(fixtures.SCRIPTS.parent / "references" / "registry-template.json")


def edit(path, old, new, count=1):
    text = path.read_text(encoding="utf-8")
    assert old in text, "fixture text not found: %r" % old
    path.write_text(text.replace(old, new, count), encoding="utf-8")


def has(problems, pattern):
    return any(re.search(pattern, p) for p in problems)


class SourcesTest(unittest.TestCase):
    def test_fixture_passes(self):
        pkg = fixtures.package()
        self.assertEqual(check_sources.check(pkg)["problems"], [])

    def test_unfetched_source_fails(self):
        pkg = fixtures.package()
        log = pkg / "run-evidence" / "fetch-log.jsonl"
        lines = [line for line in log.read_text().splitlines() if fixtures.URLS["stat"] not in line]
        log.write_text("\n".join(lines) + "\n")
        self.assertTrue(has(check_sources.check(pkg)["problems"], r"research.example.org/report was not fetched"))

    def test_dead_link_fails(self):
        pkg = fixtures.package()
        log = pkg / "run-evidence" / "fetch-log.jsonl"
        edit(log, '"url": "%s", "code": 200' % fixtures.URLS["stat"], '"url": "%s", "code": 404' % fixtures.URLS["stat"])
        self.assertTrue(has(check_sources.check(pkg)["problems"], r"dead or refused link \(HTTP 404\)"))

    def test_an_exempt_prefix_ends_at_a_path_boundary(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "sources-exempt.md", "- https://www.reddit.com/r/testprod/ - the Product's own planned "
                                                 "subreddit, not a claim\n")
        fixtures.write(pkg, "06-channels/extra.md", "Ours: https://www.reddit.com/r/testprod/comments/a1\n\n"
                                                    "Theirs: https://www.reddit.com/r/testprodfans/comments/b2\n")
        problems = check_sources.check(pkg)["problems"]
        self.assertTrue(has(problems, r"r/testprodfans/comments/b2 is cited but not listed"))
        self.assertFalse(has(problems, r"r/testprod/comments/a1"))

    def test_cited_url_missing_from_sources_fails(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "06-channels/extra.md", "See https://unlisted.example.net/page for this.\n")
        self.assertTrue(has(check_sources.check(pkg)["problems"], r"unlisted.example.net/page is cited but not listed"))

    def test_malformed_entry_and_bad_time_fail(self):
        pkg = fixtures.package()
        with open(str(pkg / "sources.md"), "a") as handle:
            handle.write("- https://x.example.org/a fetched yesterday\n")
            handle.write("- https://x.example.org/b - fetched 2026-10-24 - no time\n")
        problems = check_sources.check(pkg)["problems"]
        self.assertTrue(has(problems, r"malformed entry"))
        self.assertTrue(has(problems, r"is not YYYY-MM-DDTHH:MMZ"))

    def test_exempt_prefix_needs_reason(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "06-channels/extra.md", "Waitlist at https://testprod.example/tiktok\n")
        fixtures.write(pkg, "sources-exempt.md", "- https://testprod.example/ - short\n")
        problems = check_sources.check(pkg)["problems"]
        self.assertTrue(has(problems, r"needs a reason"))
        fixtures.write(pkg, "sources-exempt.md", "- https://testprod.example/ - the Product's own planned site, not a claim\n")
        self.assertEqual(check_sources.check(pkg)["problems"], [])

    def test_fragments_must_be_merged(self):
        import merge_sources
        pkg = fixtures.package()
        fixtures.write(pkg, "sources.d/lane.md", "- %s - fetched 2026-10-24T10:00Z - a report\n" % fixtures.URLS["stat"])
        fixtures.write(pkg, "sources.d/zeta.md", "- https://new.example.org/x - fetched 2026-10-24T10:00Z - new\n")
        self.assertTrue(has(check_sources.check(pkg)["problems"], r"zeta.md:1: https://new.example.org/x is not in sources.md"))
        # Merging rebuilds sources.md from the fragments alone.
        for url in fixtures.all_urls():
            with open(str(pkg / "sources.d" / "lane.md"), "a") as handle:
                handle.write("- %s - fetched 2026-10-24T10:00Z - research\n" % url)
        merge_sources.merge(pkg)
        problems = check_sources.check(pkg)["problems"]
        self.assertTrue(has(problems, r"new.example.org/x was not fetched"))
        self.assertFalse(has(problems, r"is not in sources.md"))
        self.assertIn("## lane", (pkg / "sources.md").read_text())

    def test_urls_with_parentheses_match_their_sources_entry(self):
        pkg = fixtures.package()
        url = "https://en.wikipedia.org/wiki/Polaroid_(brand)"
        with open(str(pkg / "sources.md"), "a") as handle:
            handle.write("- %s - fetched 2026-10-24T10:00Z - the brand's history\n" % url)
        with open(str(pkg / "run-evidence" / "fetch-log.jsonl"), "a") as handle:
            handle.write(json.dumps({"url": url, "code": 200}) + "\n")
        fixtures.write(pkg, "06-channels/history.md", "See [Polaroid](%s).\n\nThe brand (%s) made instant film.\n"
                       % (url, url))
        self.assertEqual(check_sources.check(pkg)["problems"], [])
        self.assertEqual(gc.find_urls("(see https://x.example/a), then https://y.example/b_(c)."),
                         ["https://x.example/a", "https://y.example/b_(c)"])

    def test_adjacent_markdown_links_are_separate_urls(self):
        self.assertEqual(gc.find_urls("[1](https://a.example/x)[2](https://b.example/y) and "
                                      "(https://c.example/z),[4](https://d.example/w)"),
                         ["https://a.example/x", "https://b.example/y", "https://c.example/z", "https://d.example/w"])
        pkg = fixtures.package()
        fixtures.write(pkg, "06-channels/cites.md", "Sources: [1](%s)[2](%s),[3](%s)\n"
                       % (fixtures.URLS["stat"], fixtures.URLS["comp_a"], fixtures.URLS["comp_b"]))
        self.assertEqual(check_sources.check(pkg)["problems"], [])

    def test_the_live_fetch_log_is_the_only_record_during_a_run(self):
        pkg = fixtures.package()
        state = Path(tempfile.mkdtemp(prefix="gp-state-"))
        live = state / "fetch-log.jsonl"
        lines = (pkg / "run-evidence" / "fetch-log.jsonl").read_text().splitlines()
        live.write_text("\n".join(line for line in lines if fixtures.URLS["stat"] not in line) + "\n")
        config = state / "guard-config.json"
        gc.write_json(config, {"fetch_log": str(live), "last30days_log": str(state / "last30days-log.jsonl")})
        with mock.patch.dict(os.environ, {"GR0WTHPILOT_CONFIG": str(config)}):
            self.assertTrue(has(check_sources.check(pkg)["problems"], r"research.example.org/report was not fetched"))
        with mock.patch.dict(os.environ):
            os.environ.pop("GR0WTHPILOT_CONFIG", None)
            self.assertEqual(check_sources.check(pkg)["problems"], [])

    def test_a_rerun_counts_only_its_own_fetches(self):
        import hashlib
        pkg = fixtures.package()
        state = Path(tempfile.mkdtemp(prefix="gp-state-"))
        records = [dict(json.loads(line), run_id="run-1" if fixtures.URLS["stat"] in line else "run-2")
                   for line in (pkg / "run-evidence" / "fetch-log.jsonl").read_text().splitlines()]
        (state / "fetch-log.jsonl").write_text("".join(json.dumps(r) + "\n" for r in records))
        reddit = "https://www.reddit.com/r/film/comments/abc/"
        raw = fixtures.write(pkg, "01-research/last30days/raw.md", "Thread: %s\n" % reddit)
        with open(str(pkg / "sources.md"), "a") as handle:
            handle.write("- %s - fetched 2026-10-24T11:00Z - a Reddit pain\n" % reddit)
        (state / "last30days-log.jsonl").write_text(json.dumps({"run_id": "run-1", "files": [
            {"path": str(raw), "sha256": hashlib.sha256(raw.read_bytes()).hexdigest()}]}) + "\n")
        config = state / "guard-config.json"
        gc.write_json(config, {"run_id": "run-2", "fetch_log": str(state / "fetch-log.jsonl"),
                               "last30days_log": str(state / "last30days-log.jsonl")})
        with mock.patch.dict(os.environ, {"GR0WTHPILOT_CONFIG": str(config)}):
            problems = check_sources.check(pkg)["problems"]
            self.assertTrue(has(problems, r"research.example.org/report was not fetched"))
            self.assertTrue(has(problems, r"reddit.com/r/film/comments/abc/? was not fetched"))
            gc.write_json(config, {"run_id": "run-1", "fetch_log": str(state / "fetch-log.jsonl"),
                                   "last30days_log": str(state / "last30days-log.jsonl")})
            self.assertFalse(has(check_sources.check(pkg)["problems"], r"reddit.com/r/film/comments/abc/? was not"))

    def test_last30days_output_counts_only_when_its_hash_matches(self):
        import hashlib
        pkg = fixtures.package()
        raw = fixtures.write(pkg, "01-research/last30days/raw.md", "Thread: https://www.reddit.com/r/film/comments/abc/\n")
        url = "https://www.reddit.com/r/film/comments/abc/"
        with open(str(pkg / "sources.md"), "a") as handle:
            handle.write("- %s - fetched 2026-10-24T11:00Z - a Reddit pain\n" % url)
        log = pkg / "run-evidence" / "last30days-log.jsonl"
        log.write_text(json.dumps({"files": [{"path": str(raw), "sha256": hashlib.sha256(raw.read_bytes()).hexdigest()}]}) + "\n")
        self.assertEqual(check_sources.check(pkg)["problems"], [])
        raw.write_text("Thread: %s\nedited by hand\n" % url)
        self.assertTrue(has(check_sources.check(pkg)["problems"], r"reddit.com/r/film/comments/abc/? was not fetched"))


class ClaimAuditTest(unittest.TestCase):
    def test_fixture_passes(self):
        self.assertEqual(claim_audit.check(fixtures.package())["problems"], [])

    def test_unsourced_stat_fails_and_label_fixes_it(self):
        pkg = fixtures.package()
        path = fixtures.write(pkg, "06-channels/notes.md", "About 40% of buyers churn in a month.\n")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"notes.md:1: percentage"))
        path.write_text("About 40% of buyers churn in a month [ASSUMPTION: category norm, unsourced].\n")
        self.assertEqual(claim_audit.check(pkg)["problems"], [])

    def test_counts_ratings_rankings_superlatives(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "06-channels/notes.md", "It has 12,000 users.\n\nRated 4.8 stars.\n\n"
                                                    "Ranked #3 in Photo.\n\nThe only app that does this.\n")
        found = claim_audit.check(pkg)["problems"]
        for kind in ("count", "rating", "ranking", "superlative"):
            self.assertTrue(has(found, kind), kind)

    def test_link_to_research_file_counts_as_citation(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "06-channels/notes.md", "Competitors charge $2.99 ([teardown](../01-research/competitor-alpha.md)).\n")
        self.assertEqual(claim_audit.check(pkg)["problems"], [])

    def test_source_keys_defined_in_the_file_count_as_citations(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "01-research/notes.md", "[L]: %s\n\n| Field | Observed | Source |\n|---|---|---|\n"
                                                    "| Rating | 4.6 out of 5, 2.8K ratings | L |\n\n"
                                                    "It costs $2.99 a month [L].\n" % fixtures.URLS["comp_a"])
        self.assertEqual(claim_audit.check(pkg)["problems"], [])
        fixtures.write(pkg, "01-research/notes.md", "| Field | Observed | Source |\n|---|---|---|\n"
                                                    "| Rating | 4.6 out of 5, 2.8K ratings | L |\n\nIt costs $2.99 a month [L].\n")
        problems = claim_audit.check(pkg)["problems"]
        self.assertTrue(has(problems, r"notes.md:3: count"))
        self.assertTrue(has(problems, r"notes.md:5: price"))

    def test_own_number_columns_are_skipped(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "06-channels/rank.md", "| Channel | Kill criterion |\n|---|---|\n| Search | under 5% conversion |\n")
        self.assertEqual(claim_audit.check(pkg)["problems"], [])
        fixtures.write(pkg, "06-channels/rank.md", "| Channel | Evidence |\n|---|---|\n| Search | 5% convert |\n")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"rank.md:3: percentage"))

    def test_unsourced_quote_fails(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "06-channels/q.md", "> I would pay for this in a heartbeat\n")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"q.md:1: quote"))

    def test_an_html_stat_is_cited_only_by_its_own_links(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "03-site/index.html",
                       '<!doctype html><html><head><link href="https://fonts.googleapis.com/css2?family=Inter" '
                       'rel="stylesheet"><script type="application/ld+json">{"@context": "https://schema.org"}'
                       '</script></head><body><h1>Loved by 10,000 photographers. 87%% of users print more.</h1>'
                       '<ul><li><a href="%s">Alpha Camera</a> charges $2.99 a month.</li></ul></body></html>'
                       % fixtures.URLS["comp_a"])
        problems = claim_audit.check(pkg)["problems"]
        self.assertTrue(has(problems, r"index.html: .*Loved by 10,000 photographers"))
        self.assertFalse(has(problems, r"Alpha Camera charges"))

    def test_red_team_records_are_not_scanned_for_stats(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "08-redteam/dossier.md", "# Dossier\n\n## Material changes\n\n- Site hero: before "
                                                     "'loved by 10,000 photographers', after 'a camera that waits'.\n\n"
                                                     "## Surviving objections\n\n- Copyable.\n")
        fixtures.write(pkg, "08-redteam/redteam-user.md", "# User\n\n- user-1: '87% of users print more' is unsourced.\n")
        self.assertEqual(claim_audit.check(pkg)["problems"], [])

    def test_html_stat_needs_citation(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/teaser.html", "<p>The market grew 30% last year.</p>")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"teaser.html: percentage"))

    def test_only_the_runs_own_number_columns_are_skipped(self):
        pkg = fixtures.package()
        for header, cell in (("Pain points", "40% of film shooters cannot afford development"),
                             ("Total ratings", "12,400 ratings"), ("Market size", "$2.1B a year"),
                             ("Today", "9% churn")):
            fixtures.write(pkg, "06-channels/table.md", "| Item | %s |\n|---|---|\n| A | %s |\n" % (header, cell))
            self.assertTrue(has(claim_audit.check(pkg)["problems"], r"table.md:3"), header)
        fixtures.write(pkg, "06-channels/table.md", "| Channel | Kill criteria |\n|---|---|\n| Search | under 5% |\n")
        self.assertEqual(claim_audit.check(pkg)["problems"], [])

    def test_a_refuted_claim_is_found_through_markup(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/teaser.html",
                       "<p><strong>Every competitor</strong> charges over ten dollars a month for film looks.</p>")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"REFUTED claim C2 still appears in 09-extras/teaser.html"))
        pkg = fixtures.package()
        fixtures.write(pkg, "06-channels/notes.md", "**Every competitor** charges over ten dollars a month for "
                                                    "[film looks](https://x.example/a).\n")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"REFUTED claim C2 still appears in 06-channels/notes.md"))

    def test_a_refuted_claim_is_found_in_attributes_and_json_ld(self):
        claim = "Every competitor charges over ten dollars a month for film looks"
        for head, body in (('<meta name="description" content="%s.">' % claim, ""),
                           ('<meta property="og:description" content="%s.">' % claim, ""),
                           ('<meta name="twitter:description" content="%s.">' % claim, ""),
                           ("", '<img src="a.png" alt="%s.">' % claim),
                           ("", '<abbr title="%s.">Why switch</abbr>' % claim),
                           ('<script type="application/ld+json">{"@type": "SoftwareApplication", '
                            '"description": "%s."}</script>' % claim, "")):
            pkg = fixtures.package()
            fixtures.write(pkg, "09-extras/teaser.html",
                           "<!doctype html><html><head>%s</head><body><p>A camera.</p>%s</body></html>" % (head, body))
            self.assertTrue(has(claim_audit.check(pkg)["problems"],
                                r"REFUTED claim C2 still appears in 09-extras/teaser.html"), head + body)

    def test_html_attribute_and_json_ld_stats_need_citations(self):
        cases = (('<meta name="description" content="Loved by 10,000 photographers.">', "", "count"),
                 ('<meta property="og:title" content="Rated 4.9 stars">', "", "rating"),
                 ('<meta name="twitter:description" content="87% of users print more.">', "", "percentage"),
                 ("", '<img src="a.png" alt="The only app that develops overnight">', "superlative"),
                 ("", '<abbr title="Studies show film makes you happier">Why film</abbr>', "research"),
                 ('<script type="application/ld+json">{"@type": "SoftwareApplication", '
                  '"description": "Join 50,000 users."}</script>', "", "count"))
        for head, body, trigger in cases:
            pkg = fixtures.package()
            fixtures.write(pkg, "09-extras/teaser.html",
                           "<!doctype html><html><head>%s</head><body><p>A camera.</p>%s</body></html>" % (head, body))
            self.assertTrue(has(claim_audit.check(pkg)["problems"], r"teaser.html: %s with no citation" % trigger),
                            head + body)
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/teaser.html",
                       '<!doctype html><html><head><meta name="description" content="Loved by 10,000 photographers '
                       '[TARGET for year one]."></head><body><p>A camera.</p></body></html>')
        self.assertEqual(claim_audit.check(pkg)["problems"], [])

    def test_form_copy_stats_need_citations(self):
        for field, trigger in (('<input type="email" placeholder="Join 10,000 photographers">', "count"),
                               ('<textarea placeholder="Rated 4.9 stars by film fans"></textarea>', "rating"),
                               ('<input type="submit" value="Last chance: 40% off">', "percentage"),
                               ('<input type="button" value="Save $5 today">', "price")):
            pkg = fixtures.package()
            fixtures.write(pkg, "09-extras/teaser.html", "<form>%s</form>" % field)
            self.assertTrue(has(claim_audit.check(pkg)["problems"], r"teaser.html: %s with no citation" % trigger), field)
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/teaser.html", '<form><input type="hidden" name="ref" value="40% campaign">'
                                                     '<input type="checkbox" value="10,000 users"></form>')
        self.assertEqual(claim_audit.check(pkg)["problems"], [])

    def test_an_html_blockquote_needs_a_citation_inside_it(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/teaser.html", "<blockquote><p>Best film app I have used.</p>"
                                                     "<footer>A photographer</footer></blockquote>")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"teaser.html: quote with no citation or label: Best film"))
        fixtures.write(pkg, "09-extras/teaser.html", "<blockquote><p>Best film app I have used.</p></blockquote>"
                                                     '<p><a href="%s">source</a></p>' % fixtures.URLS["stat"])
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"teaser.html: quote with no citation"))
        for quote in ('<blockquote cite="%s"><p>Best film app I have used.</p></blockquote>' % fixtures.URLS["stat"],
                      '<blockquote><p>Best film app I have used.</p><footer><a href="%s">A photographer</a></footer>'
                      '</blockquote>' % fixtures.URLS["stat"],
                      '<blockquote><p>Best film app I have used.</p><footer><a href="../sources.md">sources</a>'
                      '</footer></blockquote>'):
            fixtures.write(pkg, "09-extras/teaser.html", quote)
            self.assertEqual(claim_audit.check(pkg)["problems"], [], quote)

    def test_a_blockquote_is_cited_by_the_caption_of_its_figure(self):
        pkg = fixtures.package()
        quote = "<blockquote><p>I would pay for real film delay.</p></blockquote>"
        link = '<a href="%s">r/analog</a>' % fixtures.URLS["stat"]
        for page in ("<figure>%s<figcaption>A Reddit user, %s</figcaption></figure>" % (quote, link),
                     "<figure><figcaption>%s</figcaption><div>%s</div></figure>" % (link, quote),
                     "<figure>%s<figcaption>A Reddit user, %s</figcaption></figure>" % (quote, fixtures.URLS["stat"])):
            fixtures.write(pkg, "09-extras/teaser.html", page)
            self.assertEqual(claim_audit.check(pkg)["problems"], [], page)
        for page in ("<figure>%s<figcaption>A Reddit user</figcaption></figure>" % quote,
                     '<figure>%s</figure><figure><img src="a.png" alt="A frame"><figcaption>%s</figcaption></figure>'
                     % (quote, link)):
            fixtures.write(pkg, "09-extras/teaser.html", page)
            self.assertTrue(has(claim_audit.check(pkg)["problems"],
                                r"teaser.html: quote with no citation or label: I would pay"), page)

    def test_a_stat_inside_a_cited_quote_is_cited_by_the_quote(self):
        pkg = fixtures.package()
        url = fixtures.URLS["stat"]
        for page in ('<figure><blockquote><p>I would pay $3 for real film delay.</p></blockquote>'
                     '<figcaption>A Reddit user, <a href="%s">r/analog</a></figcaption></figure>' % url,
                     '<blockquote cite="%s"><p>I would pay $3 for real film delay.</p></blockquote>' % url,
                     '<blockquote><p>I tried 5 apps before this.</p><footer><a href="%s">src</a></footer></blockquote>'
                     % url):
            fixtures.write(pkg, "09-extras/teaser.html", page)
            self.assertEqual(claim_audit.check(pkg)["problems"], [], page)
        for page, trigger in (('<blockquote><p>I would pay $3 for real film delay.</p><footer>A Reddit user</footer>'
                               '</blockquote>', "price"),
                              ('<blockquote><p>I tried 5 apps before this.</p></blockquote><p>Most people never print '
                               'a photo again, per <a href="%s">this report</a>.</p>' % url, "count")):
            fixtures.write(pkg, "09-extras/teaser.html", page)
            problems = claim_audit.check(pkg)["problems"]
            self.assertTrue(has(problems, r"teaser.html: %s with no citation or label: I " % trigger), page)
            self.assertTrue(has(problems, r"teaser.html: quote with no citation or label: I "), page)
        fixtures.write(pkg, "09-extras/teaser.html", '<blockquote cite="%s"><p>Worth it.</p></blockquote>'
                                                     '<p>Join 50,000 users.</p>' % url)
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"teaser.html: count with no citation or label: Join"))

    def test_structured_data_carries_no_ratings_or_reviews(self):
        cases = (
            '<script type="application/ld+json">{"@type": "SoftwareApplication", "name": "Testprod", "aggregateRating": '
            '{"@type": "AggregateRating", "ratingValue": "4.8", "ratingCount": "1250"}}</script>',
            '<script type="application/ld+json">{"@type": "Product", "name": "Testprod", "review": [{"@type": "Review", '
            '"reviewBody": "Best film app I have used.", "url": "%s"}]}</script>' % fixtures.URLS["stat"],
            '<script type="application/ld+json">{"@graph": [{"@type": ["CreativeWork", "schema:UserReview"]}]}</script>',
            '<script type="application/ld+json">{"@type": "Recommendation", "itemReviewed": "Testprod"}</script>',
            '<script type="application/ld+json">{"@type": "Product", "https://schema.org/reviewCount": 3}</script>',
            '<div itemscope itemtype="https://schema.org/Product"><span itemprop="aggregateRating">4.8</span></div>',
            '<div vocab="https://schema.org/" typeof="Review"><span property="reviewBody">Great</span></div>')
        for case in cases:
            pkg = fixtures.package()
            fixtures.write(pkg, "09-extras/teaser.html", "<html><head>%s</head><body><p>A camera.</p></body></html>" % case)
            self.assertTrue(has(claim_audit.check(pkg)["problems"],
                                r"teaser.html: structured data carries ratings or reviews"), case)
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/teaser.html",
                       '<html><head><script type="application/ld+json">{"@type": "SoftwareApplication", "name": "Testprod", '
                       '"contentRating": "4+", "applicationCategory": "PhotographyApplication"}</script></head>'
                       '<body><div itemscope itemtype="https://schema.org/Product"><span itemprop="name">Testprod</span>'
                       '</div></body></html>')
        self.assertEqual(claim_audit.check(pkg)["problems"], [])

    def test_refuted_claim_must_not_ship(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "03-site/extra.md", "Every competitor charges over ten dollars a month for film looks.\n")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"REFUTED claim C2 still appears in 03-site/extra.md"))

    def test_ledger_rows_need_source_and_verdict(self):
        pkg = fixtures.package()
        edit(pkg / "08-redteam/claims-ledger.md", "| %s | WEAKENED |" % fixtures.URLS["stat"], "| a guess | MAYBE |")
        problems = claim_audit.check(pkg)["problems"]
        self.assertTrue(has(problems, r"C1 has no source"))
        self.assertTrue(has(problems, r"C1 verdict 'MAYBE'"))


class BrandLintTest(unittest.TestCase):
    def test_fixture_passes(self):
        self.assertEqual(brand_lint.check(fixtures.package())["problems"], [])

    def test_unknown_key_blocks(self):
        pkg = fixtures.package()
        path = pkg / brand_lint.RULES_PATH
        data = json.loads(path.read_text())
        data["vibes"] = ["calm"]
        path.write_text(json.dumps(data))
        self.assertTrue(has(brand_lint.check(pkg)["problems"], r"unknown key 'vibes'"))

    def test_cta_links_must_match_test_platforms(self):
        rules = dict(fixtures.BRAND_RULES)
        rules["caption_call_to_action"] = {"line": "Join: {link}", "links": {"TikTok": "a.example/t", "Instagram": "a.example/i"}}
        self.assertTrue(has(brand_lint.validate_rules(rules), r"keys must be exactly TikTok, YouTube Shorts"))
        rules["caption_call_to_action"] = {"line": "Join", "links": {"TikTok": "https://a.example/t", "YouTube Shorts": "a.example/t"}}
        problems = brand_lint.validate_rules(rules)
        self.assertTrue(has(problems, r"\{link\} once"))
        self.assertTrue(has(problems, r"bare address"))

    def test_hook_rules(self):
        rules = fixtures.BRAND_RULES
        self.assertTrue(brand_lint.lint_copy("Is this the camera you want?", rules, hook=True))
        self.assertTrue(brand_lint.lint_copy("one two three four five six seven eight nine ten eleven twelve thirteen", rules, hook=True))
        self.assertTrue(brand_lint.lint_copy("A revolutionary camera", rules, hook=True))
        self.assertTrue(brand_lint.lint_copy("SHOOT film now", rules, hook=True))
        self.assertFalse(brand_lint.lint_copy("Set ISO and shoot", rules, hook=True))
        self.assertTrue(brand_lint.lint_copy("Shoot now \U0001F4F8", rules, hook=True))

    def test_invented_proof_matches_gr0wthlab(self):
        rules = fixtures.BRAND_RULES
        self.assertTrue(brand_lint.lint_copy("Loved by 10k photographers", rules))
        self.assertTrue(brand_lint.lint_copy("Join thousands of happy users", rules))
        self.assertTrue(brand_lint.lint_copy("3x faster developing", rules))
        self.assertFalse(brand_lint.lint_copy("Shoot a roll of 24 photos", rules))

    def test_social_copy_and_page_copy(self):
        pkg = fixtures.package()
        edit(pkg / "10-launch-set/x/week-1.md", "Shoot now. See it tomorrow.", "Loved by 10k photographers. Don't miss it.")
        problems = brand_lint.check(pkg)["problems"]
        self.assertTrue(has(problems, r"x/week-1.md:3: unsourced proof"))
        self.assertTrue(has(problems, r"loss-framed phrase"))
        pkg = fixtures.package()
        edit(pkg / "03-site/index.html", "like film did.", "like film did \u2014 say goodbye to waiting.")
        problems = brand_lint.check(pkg)["problems"]
        self.assertTrue(has(problems, r"index.html: banned character"))
        self.assertTrue(has(problems, r"stock phrase 'say goodbye to'"))

    def test_page_copy_includes_attributes_and_json_ld(self):
        for old, new, finding in (
                ("<title>Testprod</title>", '<title>Testprod</title><meta name="description" content="Last chance '
                                            'to shoot film.">', r"index.html: scarcity or urgency 'last chance'"),
                ("<title>Testprod</title>", '<title>Testprod</title><meta property="og:title" content="Testprod '
                                            '\u2014 film, overnight">', r"index.html: banned character"),
                ("like film did.", 'like film did.<img src="a.png" alt="Say goodbye to waiting">',
                 r"index.html: stock phrase 'say goodbye to'"),
                ('"name": "Testprod"}', '"name": "Testprod", "description": "Only today: shoot film."}',
                 r"index.html: scarcity or urgency 'only today'"),
                ('<input type="email">', '<input type="email" placeholder="Last chance to join">',
                 r"index.html: scarcity or urgency 'last chance'"),
                ('<button type="button">Join the waitlist</button>', '<input type="submit" value="Only today: join">',
                 r"index.html: scarcity or urgency 'only today'")):
            pkg = fixtures.package()
            edit(pkg / "03-site/index.html", old, new)
            self.assertTrue(has(brand_lint.check(pkg)["problems"], finding), new)

    def test_post_copy_questions_and_cta_links_follow_gr0wthlab(self):
        rules = fixtures.BRAND_RULES
        self.assertTrue(has(brand_lint.lint_copy("Remember waiting for prints?", rules), r"asks a question"))
        self.assertFalse(brand_lint.lint_copy("Remember waiting for prints?", rules, full=False))
        pkg = fixtures.package()
        edit(pkg / "10-launch-set/x/week-1.md", "Shoot now. See it tomorrow.", "Remember waiting for prints?")
        self.assertTrue(has(brand_lint.check(pkg)["problems"], r"x/week-1.md:3: asks a question"))
        bad = dict(rules, caption_call_to_action={"line": "Join: {link}", "links": {
            "TikTok": "immerse/tiktok", "YouTube Shorts": "immerse/youtube"}})
        self.assertTrue(has(brand_lint.validate_rules(bad), r"bare address with a domain"))
        good = dict(rules, caption_call_to_action={"line": "Join: {link}", "links": {
            "TikTok": "immerse.app/tiktok", "YouTube Shorts": "immerse.app/youtube"}})
        self.assertEqual(brand_lint.validate_rules(good), [])

    def test_frozen_hooks_are_exempt_as_gr0wthlab_exempts_them(self):
        long_hook = "Hook number 1 for the camera that waits a whole night to show the revolutionary roll"
        for name, old, where in (("angles.md", '"Hook number 1 for the camera"', "angles.md P01: "),
                                 ("ab-pairs.md", '"Shoot now, see it later"', "ab-pairs.md:6: ")):
            pkg = fixtures.package()
            edit(pkg / "05-social-pmf" / name, old, '"%s"' % long_hook)
            problems = brand_lint.check(pkg)["problems"]
            self.assertEqual(sorted(p.split(": ")[1] for p in problems),
                             ["banned word 'revolutionary'", "the Hook has 16 words; at most 12"], name)
            self.assertTrue(all(p.startswith(where) for p in problems), problems)

    def test_a_draft_field_repeating_a_frozen_hook_is_exempt(self):
        long_hook = "Hook number 1 for the camera that waits a whole night to show the revolutionary roll"
        pkg = fixtures.package()
        edit(pkg / "05-social-pmf/angles.md", '"Hook number 1 for the camera"', '"%s"' % long_hook)
        edit(pkg / "05-social-pmf/week-1-drafts.md", "**Caption:** Shoot now. See it tomorrow.",
             "**Hook:** %s\n\n**Caption:** %s\nShoot it now." % (long_hook, long_hook))
        problems = brand_lint.check(pkg)["problems"]
        self.assertEqual(len(problems), 2)
        self.assertTrue(all(p.startswith("angles.md P01: ") for p in problems), problems)
        edit(pkg / "05-social-pmf/week-1-drafts.md", "Shoot it now.", "A revolutionary roll.")
        drafts = [p for p in brand_lint.check(pkg)["problems"] if not p.startswith("angles.md P01: ")]
        self.assertEqual(len(drafts), 1)
        self.assertTrue(drafts[0].startswith("05-social-pmf/week-1-drafts.md:7: banned word 'revolutionary': "))
        rules = dict(fixtures.BRAND_RULES, frozen_hooks_exempt_from=["hook_max_words"])
        found = brand_lint.lint_copy(long_hook, rules, hook=True, frozen=(long_hook,))
        self.assertEqual(found, ["banned word 'revolutionary'"])
        rules = dict(fixtures.BRAND_RULES)
        del rules["frozen_hooks_exempt_from"]
        self.assertEqual(len(brand_lint.lint_copy(long_hook, rules, hook=True, frozen=(long_hook,))), 2)
        self.assertTrue(has(brand_lint.lint_copy(long_hook + " now", fixtures.BRAND_RULES, hook=True,
                                                 frozen=(long_hook,)), r"the Hook has 17 words"))
        self.assertEqual(brand_lint.lint_copy("Shoot now?", fixtures.BRAND_RULES, frozen=("Shoot now?",)),
                         ["asks a question"])

    def test_a_creator_message_gets_no_frozen_hook_exemption(self):
        hook = "Hook number 1 for the revolutionary camera"
        pkg = fixtures.package()
        edit(pkg / "05-social-pmf/angles.md", '"Hook number 1 for the camera"', '"%s"' % hook)
        edit(pkg / "05-social-pmf/week-1-drafts.md", "**Caption:** Shoot now. See it tomorrow.",
             "**Caption:** %s\n\n**Message:** Our first post opens on %s" % (hook, hook))
        with open(str(pkg / "06-channels/creator-shortlist.md"), "a") as handle:
            handle.write("# Creators\n\n**Subject:** %s\n\n**Message:** Our first post opens on %s\n" % (hook, hook))
        problems = [p for p in brand_lint.check(pkg)["problems"] if not p.startswith("angles.md P01: ")]
        self.assertEqual(sorted(p.split(": ")[0] for p in problems),
                         ["05-social-pmf/week-1-drafts.md:7", "06-channels/creator-shortlist.md:5"])
        self.assertTrue(all(p.split(": ")[1] == "banned word 'revolutionary'" for p in problems), problems)

    def test_long_sentences_warn_and_skip_alt_text(self):
        rules = dict(fixtures.BRAND_RULES, long_sentence_words=6, long_sentence_commas=1)
        pkg = fixtures.package()
        (pkg / brand_lint.RULES_PATH).write_text(json.dumps(rules))
        edit(pkg / "05-social-pmf/week-1-drafts.md", "**Caption:** Shoot now. See it tomorrow.",
             "**Caption:** Shoot a roll, wait a night, and see every frame tomorrow.")
        edit(pkg / "05-social-pmf/week-1-drafts.md", "**Alt text:** A phone screen showing a film counter.",
             "**Alt text:** A phone screen showing a film counter, a roll, and a clock.")
        result = brand_lint.check(pkg)
        self.assertEqual(result["problems"], [])
        drafts = [w for w in result["warnings"] if w.startswith("05-social-pmf/week-1-drafts.md")]
        self.assertEqual([w.split(": ", 1)[1].rsplit(": ", 1)[0] for w in drafts],
                         ["long_sentence_words: 11 words, over 6", "long_sentence_commas: 2 commas, over 1"])
        self.assertTrue(all(w.startswith("05-social-pmf/week-1-drafts.md:5:") for w in drafts))
        self.assertIn("ab-pairs.md:11: long_sentence_words: 7 words, over 6: A roll of film on your phone",
                      result["warnings"])

    def test_sponsorship_asks_are_read_in_creator_messages_only(self):
        rules = dict(fixtures.BRAND_RULES, sponsorship_asks=["rate card", "sponsored post"])
        pkg = fixtures.package()
        (pkg / brand_lint.RULES_PATH).write_text(json.dumps(rules))
        with open(str(pkg / "06-channels/creator-shortlist.md"), "a") as handle:
            handle.write("# Creators\n\nVetted: one film blog.\n\n**Subject:** Early access to Testprod, no "
                         "sponsored post\n\n"
                         "**Message:** Early access is yours. Send your rate card for a sponsored post.\n")
        edit(pkg / "05-social-pmf/week-1-drafts.md", "**Caption:** Shoot now. See it tomorrow.",
             "**Caption:** Not a sponsored post. Shoot now.")
        problems = brand_lint.check(pkg)["problems"]
        self.assertEqual(sorted(p.split(": ")[1] for p in problems),
                         ["sponsorship ask 'rate card'", "sponsorship ask 'sponsored post'"])
        self.assertTrue(all(p.startswith("06-channels/creator-shortlist.md:7:") for p in problems))

    def test_rules_gr0wthlab_applies_and_does_not(self):
        rules = dict(fixtures.BRAND_RULES, required_sections=["Hook"], required_disclosure="Screens are real.",
                     sponsorship_asks=["rate card"])
        rows = {rule: status for rule, status, _ in brand_lint.statuses(rules)}
        self.assertEqual(rows["required_sections"], "not applicable")
        self.assertEqual(rows["required_disclosure"], "not applicable")
        self.assertEqual(rows["sponsorship_asks"], "not applicable")
        self.assertNotIn("sponsorship asks", rows)
        self.assertEqual(rows["long sentences (warning)"], "pending")
        rows = {rule: status for rule, status, _ in brand_lint.statuses(fixtures.BRAND_RULES)}
        self.assertEqual(rows["sponsorship asks"], "pending")
        self.assertNotIn("sponsorship_asks", rows)
        self.assertEqual(brand_lint.validate_rules(rules), [])
        no_proof = dict(fixtures.BRAND_RULES)
        del no_proof["invented_proof_terms"]
        self.assertEqual(brand_lint.lint_copy("Develops 3x faster, 50% of rolls", no_proof), [])
        self.assertEqual(len(brand_lint.lint_copy("Develops 3x faster, 50% of rolls", fixtures.BRAND_RULES)), 2)

    def test_notes_outside_copy_fields_are_not_linted(self):
        pkg = fixtures.package()
        with open(str(pkg / "05-social-pmf/week-1-drafts.md"), "a") as handle:
            handle.write("\nFilming note: never say revolutionary, 10k users, or use \u2014 dashes.\n")
        self.assertEqual(brand_lint.check(pkg)["problems"], [])

    def test_every_post_field_is_read_as_gr0wthlab_reads_it(self):
        pkg = fixtures.package()
        (pkg / "05-social-pmf/week-1-drafts.md").write_text(
            "# Week 1\n\n## Day 2 - P02 / AB-2 leg A\n\n"
            "**Hook (0.0-3s, on screen):**\n\n> Rated 4.9 stars by film lovers.\n\n"
            "**Hook / Shorts title:** A revolutionary roll\n\n"
            "**On-screen text sequence:** Shoot now, then say goodbye to waiting.\n\n"
            "**Spoken line:** Loved by 10k photographers.\n\n"
            "**Visual action:** The App Store page shows 4.9 stars and 10k reviews.\n\n"
            "**Caption:**\n\n> Shoot now.\n> Only today: a roll.\n\n"
            "**Spoken line:** none\n\n"
            "**Alt text:**\n\n"
            "**Caption:** Shoot now. See it tomorrow.\n")
        problems = brand_lint.check(pkg)["problems"]
        empty = [p for p in problems if "holds no copy" in p]
        self.assertEqual(len(empty), 1)
        self.assertTrue(empty[0].startswith("05-social-pmf/week-1-drafts.md:24: the alt text field holds no copy"))
        found = sorted((int(p.split(": ")[0].rsplit(":", 1)[1]), p.split(": ")[1]) for p in problems
                       if p not in empty)
        self.assertEqual(found, [(5, "social proof 'stars'"), (9, "banned word 'revolutionary'"),
                                 (11, "stock phrase 'say goodbye to'"), (13, "unsourced proof '10k photographers'"),
                                 (15, "social proof 'reviews'"), (15, "social proof 'stars'"),
                                 (17, "scarcity or urgency 'only today'")])
        self.assertTrue(all(p.startswith("05-social-pmf/week-1-drafts.md:") for p in problems))

    def test_a_line_of_hashtags_is_copy_not_a_heading(self):
        pkg = fixtures.package()
        (pkg / "05-social-pmf/week-1-drafts.md").write_text(
            "# Week 1\n\n## Day 1\n\n"
            "**Hashtags:**\n#filmcamera #revolutionary\n\n"
            "**Caption:** Shoot now. See it tomorrow.\n#streak #revolutionaryroll\n"
            "## Day 2 revolutionary\n\n"
            "**Caption:** Shoot now.\n")
        self.assertEqual(sorted(p.split(": ")[:2] for p in brand_lint.check(pkg)["problems"]),
                         [["05-social-pmf/week-1-drafts.md:5", "banned word 'revolutionary'"],
                          ["05-social-pmf/week-1-drafts.md:8", "banned word 'revolutionary'"]])


class LayoutTest(unittest.TestCase):
    def check(self, pkg):
        return check_layout.check(pkg, fixtures.PRODUCT, registry=REGISTRY)

    def test_fixture_passes_and_writes_entry(self):
        pkg = fixtures.package()
        result = check_layout.check(pkg, fixtures.PRODUCT, registry=REGISTRY, write_entry=True)
        self.assertEqual(result["problems"], [])
        entry = json.loads((pkg / "handoff" / "registry-entry.json").read_text())
        paths = [s["path"] for s in entry["go_to_market_package"]["sources"]]
        self.assertIn("projects/Testprod/gtm/05-social-pmf/angles.md", paths)
        self.assertNotIn("RepToday", json.dumps(entry["go_to_market_package"]))
        self.assertEqual(entry["go_to_market_package"]["launch_checklist"], "projects/Testprod/gtm/launch-checklist.md")

    def test_entry_points_at_the_package_folder(self):
        for kind, folder in (("first-package", "gtm"), ("candidate", "gtm-candidate-2026-10-24"),
                             ("beside-live", "gtm-candidate-2026-10-24")):
            pkg = fixtures.package(folder, kind)
            result = check_layout.check(pkg, fixtures.PRODUCT, registry=REGISTRY, write_entry=True)
            self.assertEqual(result["problems"], [], kind)
            entry = json.loads((pkg / "handoff" / "registry-entry.json").read_text())["go_to_market_package"]
            prefix = "projects/Testprod/%s/" % folder
            self.assertEqual(entry["path"], prefix, kind)
            self.assertEqual(entry["launch_checklist"], prefix + "launch-checklist.md", kind)
            self.assertTrue(all(s["path"].startswith(prefix) for s in entry["sources"]), kind)

    def test_template_matches_rep_today_entry(self):
        template = json.loads(Path(REGISTRY).read_text())["go_to_market_package"]
        self.assertEqual(len(template["sources"]), 14)
        self.assertEqual(template["post_drafts"]["angles"], "projects/{product}/gtm/05-social-pmf/angles.md")

    def test_missing_needed_file_fails(self):
        pkg = fixtures.package()
        (pkg / "05-social-pmf/read-the-results.md").unlink()
        self.assertTrue(has(self.check(pkg)["problems"], r"read-the-results.md is missing"))

    def test_empty_research_prefix_fails(self):
        pkg = fixtures.package()
        for p in (pkg / "01-research").glob("competitor-*"):
            p.unlink()
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"no competitor names"))

    def test_too_few_angles_and_unquoted_hook(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        lines = [line for line in path.read_text().splitlines() if not re.match(r"\| P1[0-5] ", line)]
        path.write_text("\n".join(lines) + "\n")
        edit(path, '"Hook number 3 for the camera"', "Hook number 3 for the camera")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"9 Angles; a Test Kit needs at least 15"))
        self.assertTrue(has(problems, r"P03 Hook must be one straight-quoted string"))

    def test_pain_needs_url_and_platform_must_be_supported(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        edit(path, "per %s |" % fixtures.URLS["pain"][0], "per a forum |")
        edit(path, "| YouTube Shorts | viewed", "| Instagram | viewed")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"P01 pain cell has no source URL"))
        self.assertTrue(has(problems, r"Platform 'Instagram'"))

    def test_pairs_need_both_legs_and_matching_calendar(self):
        pkg = fixtures.package()
        edit(pkg / "05-social-pmf/ab-pairs.md", '- Leg B hook: "Shoot now, see it later"\n', "")
        edit(pkg / "05-social-pmf/cadence-14-day.md", "| 2 | Asset 2 | P02 / AB-2 leg A |", "| 2 | Asset 2 | P04 / AB-2 leg A |")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"AB-1 needs both"))
        self.assertTrue(has(problems, r"day 2 runs AB-2 on P04, but the pair is for P02"))

    def test_calendar_days_platform_and_flex(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/cadence-14-day.md"
        edit(path, "| 5 | Asset 5 | P05 | TikTok | note |\n", "")
        edit(path, "| 6 | Asset 6 | P06 | YouTube Shorts |", "| 6 | Asset 6 | P06 | Instagram |")
        edit(path, "| 7 | Asset 7 | P07 |", "| 7 | Asset 7 | Flex |")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"day 5 is missing"))
        self.assertTrue(has(problems, r"day 6 primary platform 'Instagram'"))
        self.assertTrue(has(problems, r"flex day 7 must name exactly one fallback"))
        self.assertTrue(has(problems, r"2 flex days"))

    def test_creative_log_records_are_what_gr0wthlabs_kill_edits(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/creative-log.json"
        data = json.loads(path.read_text())
        data["angles"][0]["angle_id"] = "P01_angle"
        data["angles"][1]["status"] = "live"
        data["angles"][2]["results"] = {"views": 10}
        del data["angles"][3]["status"]
        path.write_text(json.dumps(data, indent=2) + "\n")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"angle_id 'P01_angle' must be its Angle's ID"))
        self.assertTrue(has(problems, r'P02-angle must start with status "draft" and results null'))
        self.assertTrue(has(problems, r"P03-angle must start with status"))
        self.assertTrue(has(problems, r"P04-angle needs its angle_id on a line of its own"))

    def test_platform_assignment_and_floor_and_creative_log(self):
        pkg = fixtures.package()
        edit(pkg / "05-social-pmf/platform-assignment.md", "### 2. YouTube Shorts (secondary)", "### 2. Instagram Reels (secondary)")
        edit(pkg / "05-social-pmf/read-the-results.md", "Any post under 200 impressions is unread", "Posts under 200 are unread")
        path = pkg / "05-social-pmf/creative-log.json"
        data = json.loads(path.read_text())
        data["angles"] = data["angles"][1:]
        data["angles"][0]["mood"] = "x"
        path.write_text(json.dumps(data))
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"'Instagram Reels' is not a platform gr0wthlab runs"))
        self.assertTrue(has(problems, r"no line 'Any post under N impressions is unread'"))
        self.assertTrue(has(problems, r"P01 needs exactly one record, has 0"))
        self.assertTrue(has(problems, r"keys gr0wthlab does not accept: mood"))
        self.assertTrue(has(problems, r"pretty-printed"))


class GrowthlabLayoutTest(unittest.TestCase):
    """The layout rules gr0wthlab's own reader depends on (kit.py, results.py,
    shots.py, weekly_changes.py, drafts.py, posts.py)."""

    def check(self, pkg):
        return check_layout.check(pkg, fixtures.PRODUCT, registry=REGISTRY)

    def test_angle_ids_are_zero_padded_to_one_width(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        edit(path, "| P07 |", "| P7 |")
        edit(path, "| P15 |", "| P1a |")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"zero-padded .*: P7$"))
        self.assertTrue(has(problems, r"ID 'P1a' is not P and digits, so gr0wthlab skips its row"))
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        text = re.sub(r"\| P(\d\d) \|", r"| P0\1 |", path.read_text())
        path.write_text(text)
        for name in ("ab-pairs.md", "cadence-14-day.md", "creative-log.json"):
            target = pkg / "05-social-pmf" / name
            target.write_text(re.sub(r"\bP(\d\d)\b", r"P0\1", target.read_text()))
        self.assertFalse(has(self.check(pkg)["problems"], r"zero-padded"))

    def test_platform_names_are_exact(self):
        pkg = fixtures.package()
        edit(pkg / "05-social-pmf/angles.md", "| YouTube Shorts | viewed", "| YouTube | viewed")
        edit(pkg / "05-social-pmf/cadence-14-day.md", "| 3 | Asset 3 | P03 | TikTok |", "| 3 | Asset 3 | P03 | tiktok |")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"P02 Platform 'YouTube' is not exactly TikTok or YouTube Shorts"))
        self.assertTrue(has(problems, r"day 3 primary platform 'tiktok' is not exactly"))

    def test_format_must_name_a_recording_gr0wthlab_plans(self):
        pkg = fixtures.package()
        edit(pkg / "05-social-pmf/angles.md", "20s screen record of the app", "20s clip of the app")
        result = self.check(pkg)
        self.assertTrue(has(result["problems"], r"P01 Format names no recording type"))
        self.assertFalse(has(result["warnings"], r"Format"))

    def test_signal_and_kill_name_numbers_the_platform_gives(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        edit(path, "viewed-vs-swiped rank in the top half", "saves rank in the top half")
        edit(path, "retire if bottom third watched-full after two reads", "retire if views stay low")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"P02 signal names no number gr0wthlab asks YouTube Shorts for .*only saves"))
        self.assertTrue(has(problems, r"P01 kill criterion names no number gr0wthlab asks TikTok for"))
        pkg = fixtures.package()
        edit(pkg / "05-social-pmf/angles.md", "viewed-vs-swiped rank in the top half",
             "viewed-vs-swiped rank and saves in the top half")
        self.assertTrue(has(self.check(pkg)["problems"], r"P02 signal names saves, which gr0wthlab does not ask "
                                                          r"YouTube Shorts for"))
        pkg = fixtures.package()
        edit(pkg / "05-social-pmf/angles.md", "watched-full rank in the top half",
             "average watch time and profile visits in the top half")
        self.assertEqual(self.check(pkg)["problems"], [])

    def test_signal_and_kill_are_read_on_the_calendar_days_platform(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        text = re.sub(r"(\| P05 \|.*)watched-full rank in the top half \| retire if bottom third watched-full",
                      r"\1saves and shares rank in the top half | retire if bottom third on shares", path.read_text())
        text = re.sub(r"(\| P04 \|.*)viewed-vs-swiped rank in the top half \| retire if bottom third viewed-vs-swiped",
                      r"\1saves rank in the top half | retire if bottom third on shares", text)
        path.write_text(text)
        cadence = pkg / "05-social-pmf/cadence-14-day.md"
        edit(cadence, "| 4 | Asset 4 | P04 | YouTube Shorts |", "| 4 | Asset 4 | P05 | YouTube Shorts |")
        p05 = ("angles.md: P05 signal names saves, which gr0wthlab does not ask YouTube Shorts for "
               "(cadence-14-day.md day 4)")
        self.assertEqual(self.check(pkg)["problems"], [p05])
        edit(cadence, "| 14 | Asset 14 | Flex: double down on the leader, else P05 | YouTube Shorts |",
             "| 14 | Asset 14 | P04 | YouTube Shorts |")
        self.assertEqual(self.check(pkg)["problems"], [p05])
        edit(cadence, "| 13 | Asset 13 | P03 | TikTok |", "| 13 | Asset 13 | P04 | YouTube Shorts |")
        self.assertEqual(self.check(pkg)["problems"], [
            "angles.md: P04 signal names no number gr0wthlab asks YouTube Shorts for (viewed-vs-swiped, % viewed, "
            "shares, likes, comment); it names only saves (cadence-14-day.md day 13)", p05])

    def test_signal_and_kill_are_read_where_the_flex_slot_puts_an_angle(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        text = path.read_text()
        for aid in ("P03", "P05", "P07"):
            text = re.sub(r"(\| %s \|.*)\| TikTok \|" % aid, r"\1| YouTube Shorts |", text)
        path.write_text(text)

        def flagged():
            found = [p for p in self.check(pkg)["problems"] if p.startswith("angles.md")]
            self.assertTrue(all(" asks YouTube Shorts for " in p and p.endswith("only watched-full") for p in found),
                            found)
            return sorted(tuple(p.split(" ")[1:3]) for p in found)

        self.assertEqual(flagged(), [])
        cadence = pkg / "05-social-pmf/cadence-14-day.md"
        edit(cadence, "| 13 | Asset 13 | P03 | TikTok | note |",
             "| 13 | Asset 13 | Flex: double down on the leader, else P05 | YouTube Shorts | note |")
        edit(cadence, "| 14 | Asset 14 | Flex: double down on the leader, else P05 | YouTube Shorts | note |\n", "")
        self.assertEqual(flagged(), [("P03", "kill"), ("P03", "signal"), ("P05", "kill"), ("P05", "signal")])

    def test_the_documented_angle_row_passes(self):
        doc = (fixtures.SCRIPTS.parent / "references" / "package-layout.md").read_text()
        example = next(block for block in doc.split("```") if "| ID | Angle |" in block)
        problems = []
        angles = check_layout.check_angles(example, fixtures.BRAND_RULES, problems, [])
        days = check_layout.check_calendar("| Day | Asset | Angle | Primary platform |\n|---|---|---|---|\n"
                                           "| 1 | Asset 1 | P01 | TikTok |\n", [])
        check_layout.check_metrics(days, angles, problems)
        self.assertEqual(list(angles), ["P01"])
        self.assertEqual(problems, ["angles.md: 1 Angles; a Test Kit needs at least 15 distinct Angles"])

    def test_checklist_titles_and_scopes_as_gr0wthlab_reads_them(self):
        pkg = fixtures.package()
        path = pkg / "08-redteam/pre-publication-checklist.md"
        path.write_text("# Pre-publication checklist\n\nItems marked (blocking: X) block only that asset.\n\n"
                        "- [ ] Measure latency on the oldest phone. It backs the claim. (blocking: site)\n"
                        "- [ ] **Benchmark record** for the \"under 100 milliseconds\" claim (blocking: social)\n"
                        "- [ ] **Waitlist live** (Blocking: social)\n"
                        "- [ ] **Two scopes** (blocking: site) and (blocking: social)\n"
                        "- [ ] **Trademark search**\n"
                        "(blocking: naming)\n"
                        "  - [ ] **Nested** item (blocking: social)\n"
                        "* [ ] **Starred** item\n"
                        "- [ ] **Empty scope** (blocking: )\n")
        result = self.check(pkg)
        problems = [p for p in result["problems"] if p.startswith("pre-publication")]
        self.assertTrue(has(problems, r":6: the item names its claim outside its title"))
        self.assertTrue(has(problems, r":7: a blocking scope gr0wthlab cannot read"))
        self.assertTrue(has(problems, r":8: more than one blocking scope"))
        self.assertTrue(has(problems, r":10: this line is not part of the item above it"))
        self.assertTrue(has(problems, r":12: a checkbox gr0wthlab does not read as an item"))
        self.assertTrue(has(problems, r":13: '\(blocking: \)' names no scope"))
        self.assertFalse(has(problems, r":[35]:"))
        self.assertFalse(has(result["warnings"], r"bold title"))
        path.write_text("# Checklist\n\n- [ ] **Waitlist live** before any post\n  (blocking: everything public)\n"
                        "- [ ] **Benchmark record for the \"under 100 milliseconds\" claim** (blocking: social)\n"
                        "- [ ] Measure latency first. Then decide.\n")
        result = self.check(pkg)
        self.assertFalse(has(result["problems"], r"^pre-publication"))
        self.assertEqual(len([w for w in result["warnings"] if ":3: open item blocks every" in w]), 1)
        self.assertFalse(has(result["warnings"], r":5:"))

    def test_checklist_lines_gr0wthlab_merges_or_drops_are_caught(self):
        pkg = fixtures.package()
        path = pkg / "08-redteam/pre-publication-checklist.md"
        path.write_text("# Checklist\n\n- [x] **Site live** done\n  - [ ] **Verify waitlist** (blocking: social)\n"
                        "- [ ] **Waitlist copy** reviewed\nnot indented, so the item ended\n  (blocking: social)\n"
                        "- [ ] **Trademark search**\n\n  (blocking: naming)\n\n"
                        "- [ ] **Benchmark record** on two phones\n  measured in real time\n"
                        "  - [ ] **Nested deeper** (blocking: social)\n\n## Notes\n\n"
                        "Lines marked (blocking: social) block posts.\n")
        problems = [p for p in self.check(pkg)["problems"] if p.startswith("pre-publication")]
        self.assertEqual(len(problems), 4, problems)
        self.assertTrue(has(problems, r":4: a checkbox gr0wthlab does not read as an item \(an indented one is "
                                      r"read as part of the item above, its blocking scope included\)"))
        self.assertTrue(has(problems, r":7: this line is not part of the item above it"))
        self.assertTrue(has(problems, r":10: this line is not part of the item above it"))
        self.assertTrue(has(problems, r":14: a checkbox gr0wthlab does not read as an item"))

    def test_the_angle_bank_is_the_table_with_its_eight_columns(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        path.write_text(path.read_text().replace(
            "# Angle bank\n\n", "# Angle bank\n\n| ID | Hook | Hypothesis |\n|---|---|---|\n"
                                "| P01 | \"Hook number 1 for the camera\" | waiting sells |\n\n", 1))
        log = pkg / "05-social-pmf/creative-log.json"
        data = json.loads(log.read_text())
        data["angles"][0]["hypothesis"] = "waiting sells"
        log.write_text(json.dumps(data, indent=2) + "\n")
        self.assertTrue(has(self.check(pkg)["problems"], r"P01-angle holds hypothesis, but angles.md has no "
                                                         r"Hypothesis column"))
        path.write_text(re.sub(r'(\| P01 \| Angle 1 \|.*)"Hook number 1 for the camera"',
                               r'\1"Hook number 1 for the revolutionary camera"', path.read_text()))
        self.assertEqual([p.split(": ")[:2] for p in brand_lint.check(pkg)["problems"]],
                         [["angles.md P01", "banned word 'revolutionary'"]])

    def test_creative_log_shape_is_one_gr0wthlab_edits(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/creative-log.json"
        records = json.loads(path.read_text())["angles"]
        path.write_text(json.dumps(records, indent=2) + "\n")
        self.assertEqual(self.check(pkg)["problems"], [])
        path.write_text(json.dumps({"angles": records}, indent=4) + "\n")
        self.assertEqual(self.check(pkg)["problems"], [])
        text = json.dumps({"angles": records}, indent=2).replace('"results": null\n    }\n  ]', '"results": null}\n  ]')
        path.write_text(text + "\n")
        self.assertTrue(has(self.check(pkg)["problems"], r"last record's '}' line followed by the list's ']' line"))
        records[0]["hypothesis"] = "waiting sells"
        records[1]["platform"] = None
        path.write_text(json.dumps({"angles": records}, indent=2) + "\n")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"P01-angle holds hypothesis, but angles.md has no Hypothesis column"))
        self.assertTrue(has(problems, r"Angles on YouTube Shorts must all use one platform string"))
        records[1]["platform"] = "youtube_shorts"
        del records[0]["hypothesis"]
        path.write_text(json.dumps({"angles": records}, indent=2) + "\n")
        self.assertEqual(self.check(pkg)["problems"], [])


class ScreenshotTest(unittest.TestCase):
    def test_fixture_passes(self):
        pkg = fixtures.package()
        self.assertEqual(check_screenshots.check_site(pkg)["problems"], [])
        self.assertEqual(check_screenshots.check_launch_set(pkg)["problems"], [])

    def test_wrong_size_blank_and_missing_note(self):
        pkg = fixtures.package()
        shots = pkg / "03-site" / "screenshots"
        fixtures.png(shots / "index-390x844.png", "500x844")
        fixtures.png(shots / "index-b-1440x900.png", "1440x900", blank=True)
        edit(pkg / "03-site/screenshot-gate.md", "- index-390x844.png: hero", "- index-390x844.png: ok\n- x: hero")
        problems = check_screenshots.check_site(pkg)["problems"]
        self.assertTrue(has(problems, r"index-390x844.png is 500x844, not 390x844"))
        self.assertTrue(has(problems, r"index-b-1440x900.png looks blank"))
        self.assertTrue(has(problems, r"no inspection note for index-390x844.png"))

    def test_retina_size_accepted_and_overflow_fails(self):
        pkg = fixtures.package()
        fixtures.png(pkg / "03-site/screenshots/index-390x844.png", "780x1688")
        self.assertEqual(check_screenshots.check_site(pkg)["problems"], [])
        fixtures.write(pkg, "03-site/screenshots/index-390.json", json.dumps({"scrollWidth": 470, "innerWidth": 390, "overflows": True,
                                                                               "viewport": "390x844"}))
        self.assertTrue(has(check_screenshots.check_site(pkg)["problems"], r"index.html overflows horizontally at 390px"))

    def test_one_variant_fails(self):
        pkg = fixtures.package()
        (pkg / "03-site/index-b.html").unlink()
        self.assertTrue(has(check_screenshots.check_site(pkg)["problems"], r"needs two hero variants"))

    def test_a_measurement_must_be_for_its_own_viewport(self):
        pkg = fixtures.package()
        shots = pkg / "03-site" / "screenshots"
        (shots / "index-390.json").write_text((shots / "index-1440.json").read_text())
        (shots / "index-b-390.json").write_text("{}")
        problems = check_screenshots.check_site(pkg)["problems"]
        self.assertTrue(has(problems, r"index-390.json is not gp-chrome measure's output for index.html at 390x844"))
        self.assertTrue(has(problems, r"index-b-390.json is not gp-chrome measure's output"))

    def test_site_evidence_older_than_its_page_or_its_files_fails(self):
        pkg = fixtures.package()
        page = pkg / "03-site" / "index.html"
        edit(page, "<title>Testprod</title>", '<title>Testprod</title><link rel="stylesheet" href="style.css">')
        css = fixtures.write(pkg, "03-site/style.css", "body { margin: 0 }")
        now = time.time()
        evidence = [p for p in (pkg / "03-site" / "screenshots").glob("index-*") if not p.name.startswith("index-b")]

        def stamp(paths, when):
            for path in paths:
                os.utime(str(path), (when, when))

        stamp([page, css], now - 100)
        stamp(evidence, now - 50)
        self.assertEqual(check_screenshots.check_site(pkg)["problems"], [])
        stamp([css], now - 10)
        self.assertTrue(has(check_screenshots.check_site(pkg)["problems"], r"index-390x844.png is older than style.css"))
        stamp([page], now)
        self.assertTrue(has(check_screenshots.check_site(pkg)["problems"], r"index-390.json is older than index.html"))
        stamp(evidence, now + 10)
        self.assertEqual(check_screenshots.check_site(pkg)["problems"], [])

    def test_site_evidence_older_than_files_its_css_or_srcset_loads_fails(self):
        pkg = fixtures.package()
        site = pkg / "03-site"
        edit(site / "index.html", "<title>Testprod</title>",
             '<title>Testprod</title><link rel="stylesheet" href="css/style.css">'
             "<style>.a { background: url('img/inline.png') }</style>")
        edit(site / "index.html", "like film did.",
             'like film did.<span style="background-image: url(img/attr.png)"></span>'
             '<img src="img/a.png" srcset="img/a.png 1x, img/a@2x.png 2x" alt="A frame">'
             '<picture><source srcset="img/b.webp 1x, img/b@2x.webp 2x"></picture>')
        fixtures.write(pkg, "03-site/css/style.css",
                       '@import "parts/type.css";\n/* .old { background: url(../img/old.png) } */\n'
                       '.hero { background: url("../img/hero.png") }\n')
        fixtures.write(pkg, "03-site/css/parts/type.css",
                       '@font-face { font-family: Film; src: url(../../fonts/film.woff2) format("woff2") }\n')
        loaded = ["img/inline.png", "img/attr.png", "img/a.png", "img/a@2x.png", "img/b.webp", "img/b@2x.webp",
                  "img/hero.png", "fonts/film.woff2"]
        for rel in loaded + ["img/old.png"]:
            fixtures.write(pkg, "03-site/" + rel, "x")
        inputs = [site / rel for rel in loaded + ["index.html", "css/style.css", "css/parts/type.css"]]
        evidence = [p for p in (site / "screenshots").glob("index-*") if not p.name.startswith("index-b")]
        now = time.time()

        def stamp(paths, when):
            for path in paths:
                os.utime(str(path), (when, when))

        stamp(inputs + [site / "img/old.png"], now - 100)
        stamp(evidence, now - 50)
        self.assertEqual(check_screenshots.check_site(pkg)["problems"], [])
        for path in inputs:
            stamp([path], now - 10)
            self.assertTrue(has(check_screenshots.check_site(pkg)["problems"],
                                r"index-390x844.png is older than %s" % re.escape(path.name)), path.name)
            stamp([path], now - 100)
        stamp([site / "img/old.png"], now - 10)
        self.assertEqual(check_screenshots.check_site(pkg)["problems"], [])

    def test_launch_set_images_are_sized_rasters_with_fetched_sources(self):
        pkg = fixtures.package()
        path = pkg / "10-launch-set/manifest.json"
        data = json.loads(path.read_text())
        (pkg / "10-launch-set/instagram/profile.svg").write_text("<svg/>")
        data["assets"][0]["path"] = "instagram/profile.svg"
        data["assets"][2]["size_source"] = "X help center"
        path.write_text(json.dumps(data))
        problems = check_screenshots.check_launch_set(pkg)["problems"]
        self.assertTrue(has(problems, r"instagram/profile.svg is a profile-image, which must be a PNG"))
        self.assertTrue(has(problems, r"x/profile.png needs size_source, the http\(s\) URL"))

    def test_launch_set_needs_each_platform_and_sizes(self):
        pkg = fixtures.package()
        path = pkg / "10-launch-set/manifest.json"
        data = json.loads(path.read_text())
        data["assets"] = [a for a in data["assets"] if not (a["platform"] == "tiktok" and a["kind"] == "profile-image")]
        data["assets"][0]["size"] = "999x999"
        del data["assets"][1]["size_source"]
        path.write_text(json.dumps(data))
        problems = check_screenshots.check_launch_set(pkg)["problems"]
        self.assertTrue(has(problems, r"tiktok has no profile-image"))
        self.assertTrue(has(problems, r"profile.png is 320x320, not 999x999"))
        self.assertTrue(has(problems, r"needs size_source"))


class VideoTest(unittest.TestCase):
    def video(self, pkg):
        return pkg / "04-video" / "walkthrough.mp4"

    def test_fixture_passes(self):
        pkg = fixtures.package()
        self.assertEqual(check_video.verify(self.video(pkg), "270x480", 2, 10)["problems"], [])

    def test_wrong_size_duration_and_no_audio(self):
        pkg = fixtures.package()
        fixtures.ffmpeg("-f", "lavfi", "-i", "testsrc2=s=320x240:d=1", "-pix_fmt", "yuv420p", str(self.video(pkg)))
        problems = check_video.verify(self.video(pkg), "270x480", 2, 10)["problems"]
        self.assertTrue(has(problems, r"is 320x240, not 270x480"))
        self.assertTrue(has(problems, r"outside 2-10s"))
        self.assertTrue(has(problems, r"no audio stream"))

    def test_frames_must_be_viewed_and_audio_stated(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "04-video/gate-report.md", "# Video gate\n\n- frame-000.png: looked fine\n")
        problems = check_video.verify(self.video(pkg), "270x480", 2, 10)["problems"]
        self.assertTrue(has(problems, r"no viewing note for frame-000.png"))
        self.assertTrue(has(problems, r"no viewing note for frame-100.png"))
        self.assertTrue(has(problems, r"must say what the audio is"))

    def test_video_evidence_older_than_the_video_fails(self):
        pkg = fixtures.package()
        video = self.video(pkg)
        folder = video.parent
        past = video.stat().st_mtime - 60
        for path in list((folder / "frames").glob("frame-*.png")) + [folder / "frame-strip.png",
                                                                    folder / "ffprobe-report.txt"]:
            os.utime(str(path), (past, past))
        problems = check_video.verify(video, "270x480", 2, 10)["problems"]
        self.assertTrue(has(problems, r"frames/frame-000.png is older than walkthrough.mp4"))
        self.assertTrue(has(problems, r"frame-strip.png is older than walkthrough.mp4"))
        self.assertTrue(has(problems, r"ffprobe-report.txt is older than walkthrough.mp4"))
        quiet(check_video.prepare, video)
        self.assertEqual(check_video.verify(video, "270x480", 2, 10)["problems"], [])

    def test_prepare_writes_frames_strip_and_report(self):
        pkg = fixtures.package()
        for p in (pkg / "04-video" / "frames").glob("*.png"):
            p.unlink()
        (pkg / "04-video" / "frame-strip.png").unlink()
        quiet(check_video.prepare, self.video(pkg))
        self.assertEqual(len(list((pkg / "04-video" / "frames").glob("frame-*.png"))), 5)
        self.assertTrue((pkg / "04-video" / "frame-strip.png").is_file())
        self.assertIn("has_audio: True", (pkg / "04-video" / "ffprobe-report.txt").read_text())

    def test_prepare_times_frames_by_the_video_frames_not_the_file_length(self):
        # Like a simulator recording, whose last frame comes seconds before the file ends.
        pkg = fixtures.package()
        fixtures.ffmpeg("-f", "lavfi", "-i", "testsrc2=s=270x480:r=1:d=4", "-f", "lavfi", "-i",
                        "sine=frequency=440:duration=4", "-shortest", "-pix_fmt", "yuv420p", str(self.video(pkg)))
        self.assertEqual(quiet(check_video.main, ["prepare", str(self.video(pkg))]), 0)
        frames = pkg / "04-video" / "frames"
        self.assertTrue(all((frames / check_video.frame_name(p)).is_file() for p in check_video.POINTS))
        self.assertEqual(check_video.verify(self.video(pkg), "270x480", 2, 10)["problems"], [])

    def test_prepare_names_a_video_with_no_frames(self):
        pkg = fixtures.package()
        audio = pkg / "04-video" / "tone.m4a"
        fixtures.ffmpeg("-f", "lavfi", "-i", "sine=frequency=440:duration=2", str(audio))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(check_video.main(["prepare", str(audio)]), 1)
        self.assertIn("FAIL ffprobe found no video frames in", out.getvalue())


class RecapTest(unittest.TestCase):
    def test_fixture_passes(self):
        self.assertEqual(check_recap.check(fixtures.package(), fixtures.PRODUCT)["problems"], [])

    def test_broken_link_and_anchor(self):
        pkg = fixtures.package()
        edit(pkg / "recap.html", "08-redteam/dossier.md#surviving", "08-redteam/dossier.md#nowhere")
        edit(pkg / "recap.html", "06-channels/channel-plan.md", "06-channels/missing.md")
        problems = check_recap.check(pkg, fixtures.PRODUCT)["problems"]
        self.assertTrue(has(problems, r"06-channels/missing.md does not resolve"))
        self.assertTrue(has(problems, r"the deliverables map does not link 06-channels/"))

    def test_every_srcset_candidate_must_resolve(self):
        pkg = fixtures.package()
        edit(pkg / "recap.html", "<h2>Deliverables</h2>",
             '<h2>Deliverables</h2><img src="03-site/screenshots/index-390x844.png" alt="Site" '
             'srcset="03-site/screenshots/index-390x844.png 1x, 03-site/screenshots/index@2x.png 2x">')
        self.assertTrue(has(check_recap.check(pkg, fixtures.PRODUCT)["problems"],
                            r"srcset 03-site/screenshots/index@2x.png does not resolve"))
        self.assertEqual(gc.srcset_urls("a.png?x=1,2 1x, b.png 2x,c.png 100w (x, y), d.png,"),
                         ["a.png?x=1,2", "b.png", "c.png", "d.png"])

    def test_handoff_line_and_clearance(self):
        pkg = fixtures.package()
        edit(pkg / "recap.html", "Testprod - hand to gr0wthlab", "hand it over")
        edit(pkg / "recap.html", "UNVERIFIED", "pending")
        problems = check_recap.check(pkg, fixtures.PRODUCT)["problems"]
        self.assertTrue(has(problems, r"'Testprod - hand to gr0wthlab' word for word"))
        self.assertTrue(has(problems, r"UNVERIFIED"))

    def test_candidate_folder_needs_its_own_handoff_line(self):
        pkg = fixtures.package("gtm-candidate-2026-10-24", "candidate")
        problems = check_recap.check(pkg, fixtures.PRODUCT)["problems"]
        self.assertTrue(has(problems, r"'Testprod - hand to gr0wthlab \(gtm-candidate-2026-10-24\)' word for word"))
        edit(pkg / "recap.html", "Testprod - hand to gr0wthlab", "Testprod - hand to gr0wthlab (gtm-candidate-2026-10-24)")
        self.assertEqual(check_recap.check(pkg, fixtures.PRODUCT)["problems"], [])

    def test_beside_live_package_needs_no_handoff_line(self):
        pkg = fixtures.package("gtm-candidate-2026-10-24", "beside-live")
        edit(pkg / "recap.html", "When you approve it, say: <code>Testprod - hand to gr0wthlab</code>",
             "Testprod's live package stays in place until gr0wthlab can take a replacement package.")
        self.assertEqual(check_recap.check(pkg, fixtures.PRODUCT)["problems"], [])

    def test_every_extra_must_be_mapped(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/pitch-deck.html", "<p>deck</p>")
        self.assertTrue(has(check_recap.check(pkg, fixtures.PRODUCT)["problems"], r"does not link the extra 09-extras/pitch-deck.html"))

    def test_handoff_line_is_exact_and_absent_beside_live(self):
        pkg = fixtures.package()
        edit(pkg / "recap.html", "<code>Testprod - hand to gr0wthlab</code>",
             "<code>Testprod - hand to gr0wthlab (gtm-candidate-2026-10-01)</code>")
        self.assertTrue(has(check_recap.check(pkg, fixtures.PRODUCT)["problems"],
                            r"'Testprod - hand to gr0wthlab' word for word"))
        pkg = fixtures.package("gtm-candidate-2026-10-24", "beside-live")
        self.assertTrue(has(check_recap.check(pkg, fixtures.PRODUCT)["problems"],
                            r"a package beside a live one has no ready Handoff line"))

    def test_missing_section(self):
        pkg = fixtures.package()
        edit(pkg / "recap.html", 'id="objection"', 'id="other"')
        self.assertTrue(has(check_recap.check(pkg, fixtures.PRODUCT)["problems"], r'id="objection"'))


def quiet(func, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return func(*args)


class AuditTest(unittest.TestCase):
    def test_refused_calls_in_the_audit_are_not_claims(self):
        pkg = fixtures.package()
        state = Path(tempfile.mkdtemp(prefix="gp-state-"))
        refused = [
            {"run_id": "testprod-1", "event": "pre", "tool": "WebFetch", "input": "https://blocked.example.net/pricing",
             "decision": "deny",
             "reason": "https://blocked.example.net/robots.txt disallows https://blocked.example.net/pricing"},
            {"run_id": "testprod-1", "event": "pre", "tool": "Bash", "input": "awk -F= '{print $1}' /repo/.env",
             "decision": "deny", "reason": "reading a .env file can print secret values"},
            {"run_id": "testprod-0", "event": "pre", "tool": "Bash", "input": "gh pr create", "decision": "deny",
             "reason": "an earlier run's refusal"},
        ]
        (state / "tool-log.jsonl").write_text("".join(json.dumps(r) + "\n" for r in refused))
        fetches = [dict(json.loads(line), run_id="testprod-1")
                   for line in (pkg / "run-evidence" / "fetch-log.jsonl").read_text().splitlines()]
        (state / "fetch-log.jsonl").write_text("".join(json.dumps(r) + "\n" for r in fetches))
        gc.write_json(state / "simulators.json", {"devices": [
            {"udid": "OLD", "name": "Gr0wthPilot-Testprod-1", "run_id": "testprod-0", "deleted_at": FETCHED},
            {"udid": "NEW", "name": "Gr0wthPilot-Testprod-2", "run_id": "testprod-1", "deleted_at": FETCHED}]})
        cfg = {"package": str(pkg), "product": fixtures.PRODUCT, "package_rel": "projects/Testprod/gtm",
               "run_id": "testprod-1", "tool_log": str(state / "tool-log.jsonl"),
               "fetch_log": str(state / "fetch-log.jsonl"), "last30days_log": str(state / "last30days-log.jsonl"),
               "simulators": str(state / "simulators.json")}
        with mock.patch.dict(os.environ):
            os.environ.pop("GR0WTHPILOT_CONFIG", None)
            self.assertEqual(audit_run.summarize(cfg)["denied"], 2)
            self.assertIn("blocked.example.net/pricing", (pkg / gc.AUDIT_NAME).read_text())
            copied = [json.loads(line) for line in (pkg / "run-evidence" / "tool-log.jsonl").read_text().splitlines()]
            self.assertEqual({r["run_id"] for r in copied}, {"testprod-1"})
            devices = json.loads((pkg / "run-evidence" / "simulators.json").read_text())["devices"]
            self.assertEqual([d["udid"] for d in devices], ["NEW"])
            self.assertEqual(check_sources.check(pkg)["problems"], [])
            self.assertEqual(claim_audit.check(pkg)["problems"], [])


class JournalTest(unittest.TestCase):
    def setUp(self):
        for patcher in (mock.patch.object(check_layout, "default_registries", lambda: [Path(REGISTRY)]),
                        mock.patch.dict(os.environ)):
            patcher.start()
            self.addCleanup(patcher.stop)
        os.environ.pop("GR0WTHPILOT_CONFIG", None)

    def run_gate(self, pkg, gate):
        return quiet(journal.main, ["pass", gate, str(pkg)])

    def test_gates_pass_in_order_on_the_fixture(self):
        pkg = fixtures.package()
        self.assertEqual(self.run_gate(pkg, "research"), 1)
        for gate in journal.GATE_IDS:
            if gate.startswith("critic-"):
                os.utime(str(pkg / "08-redteam" / ("critic-phase-%s.md" % gate[-1])), None)
            self.assertEqual(self.run_gate(pkg, gate), 0, gate)
        self.assertEqual(quiet(journal.main, ["complete", str(pkg)]), 0)
        data = json.loads((pkg / "run-journal.json").read_text())
        self.assertEqual(data["status"], "complete")
        self.assertEqual([g["id"] for g in data["gates"]], journal.GATE_IDS)

    def test_gate_refuses_when_its_check_fails(self):
        pkg = fixtures.package()
        (pkg / "01-research/product-facts-brief.md").write_text("# Product facts\n\nNo citations.\n")
        self.assertEqual(self.run_gate(pkg, "product-facts"), 1)
        self.assertEqual(json.loads((pkg / "run-journal.json").read_text())["gates"], [])

    def test_critic_must_say_pass_and_be_fresh(self):
        pkg = fixtures.package()
        for gate in journal.GATE_IDS[:5]:
            self.assertEqual(self.run_gate(pkg, gate), 0, gate)
        report = pkg / "08-redteam/critic-phase-1.md"
        report.write_text("Round 1\n\nVerdict: PASS\n\nRound 2\n\nVerdict: SEND BACK\n")
        self.assertEqual(self.run_gate(pkg, "critic-1"), 1)
        report.write_text("Round 3\n\nVerdict: PASS\n")
        os.utime(str(report), (1, 1))
        self.assertEqual(self.run_gate(pkg, "critic-1"), 1)
        os.utime(str(report), None)
        self.assertEqual(self.run_gate(pkg, "critic-1"), 0)

    def test_a_fix_re_gated_after_the_critic_sends_the_critic_again(self):
        pkg = fixtures.package()
        for gate in journal.GATE_IDS[:journal.GATE_IDS.index("critic-1") + 1]:
            if gate.startswith("critic-"):
                os.utime(str(pkg / "08-redteam" / ("critic-phase-%s.md" % gate[-1])), None)
            self.assertEqual(self.run_gate(pkg, gate), 0, gate)
        path = pkg / "run-journal.json"
        data = json.loads(path.read_text())
        for entry in data["gates"]:
            entry["passed_at"] = "2026-01-01T00:00:00Z"
        path.write_text(json.dumps(data))
        report = pkg / "08-redteam/critic-phase-1.md"
        os.utime(str(report), (time.time() - 600,) * 2)
        self.assertEqual(self.run_gate(pkg, "critic-1"), 0)
        self.assertEqual(journal.stale_critics(pkg, ["1"]), [])
        self.assertEqual(self.run_gate(pkg, "claims-1"), 0)
        self.assertTrue([g for g in json.loads(path.read_text())["gates"] if g["id"] == "claims-1"][0]["repassed_at"])
        self.assertEqual(self.run_gate(pkg, "critic-1"), 1)
        self.assertTrue(has(journal.stale_critics(pkg, ["1"]), r"critic-1: .*last pass of gate claims-1"))
        os.utime(str(report), None)
        self.assertEqual(self.run_gate(pkg, "critic-1"), 0)
        self.assertEqual(journal.stale_critics(pkg, ["1"]), [])

    def test_package_and_complete_recheck_every_critic(self):
        pkg = fixtures.package()
        for gate in journal.GATE_IDS:
            if gate.startswith("critic-"):
                os.utime(str(pkg / "08-redteam" / ("critic-phase-%s.md" % gate[-1])), None)
            self.assertEqual(self.run_gate(pkg, gate), 0, gate)
        report = pkg / "08-redteam/critic-phase-2.md"
        os.utime(str(report), (1, 1))
        self.assertTrue(has(journal.g_package(pkg, {"product": fixtures.PRODUCT, "simulators": "/nonexistent"}),
                            r"critic-2: "))
        self.assertEqual(quiet(journal.main, ["complete", str(pkg)]), 1)
        os.utime(str(report), None)
        self.assertEqual(quiet(journal.main, ["complete", str(pkg)]), 0)

    def test_red_team_must_change_something(self):
        pkg = fixtures.package()
        (pkg / "08-redteam/dossier.md").write_text("# Dossier\n\n## Material changes\n\nNone.\n\n## Surviving objections\n\n- x\n")
        self.assertTrue(has(journal.g_red_team(pkg, {}), r"performed, not ran"))

    def test_a_passed_gate_is_checked_again(self):
        pkg = fixtures.package()
        for gate in journal.GATE_IDS[:journal.GATE_IDS.index("site") + 1]:
            if gate.startswith("critic-"):
                os.utime(str(pkg / "08-redteam" / ("critic-phase-%s.md" % gate[-1])), None)
            self.assertEqual(self.run_gate(pkg, gate), 0, gate)
        self.assertEqual(self.run_gate(pkg, "site"), 0)
        (pkg / "03-site" / "screenshots" / "index-390x844.png").unlink()
        self.assertEqual(self.run_gate(pkg, "site"), 1)
        gates = [g["id"] for g in json.loads((pkg / "run-journal.json").read_text())["gates"]]
        self.assertEqual(gates.count("site"), 1)

    def test_complete_refuses_before_the_last_gate(self):
        pkg = fixtures.package()
        self.assertEqual(quiet(journal.main, ["complete", str(pkg)]), 1)


def pass_through(case, pkg, last):
    """Pass every gate up to and including `last`, freshening each critic's report."""
    for gate in journal.GATE_IDS[:journal.GATE_IDS.index(last) + 1]:
        if gate.startswith("critic-"):
            os.utime(str(pkg / "08-redteam" / ("critic-phase-%s.md" % gate[-1])), None)
        case.assertEqual(quiet(journal.main, ["pass", gate, str(pkg)]), 0, gate)


def load(pkg):
    return json.loads((pkg / "run-journal.json").read_text())


def save(pkg, data):
    (pkg / "run-journal.json").write_text(json.dumps(data))


def shortlist_md(names, product=fixtures.PRODUCT, next_step=True):
    url = fixtures.URLS["comp_a"]
    out = ["# Name shortlist: %s" % product, ""]
    for rank, name in enumerate(names, 1):
        out += ["## %d. %s `[PROPOSAL]`" % (rank, name), "",
                "- App Store: none seen in a search; nearest listing %s" % url,
                "- Web: none seen.",
                "- Domains: registry lookup %s" % url,
                "- Clearance: trademark and App Store name clearance are UNVERIFIED.", ""]
    if next_step:
        out += ["## Next step", "",
                "Try the names in App Store Connect in this order, then run "
                "`bin/gr0wthpilot %s --accept-name \"<name>\"` with the first one it accepts." % product, ""]
    return "\n".join(out)


class RenameTest(unittest.TestCase):
    def test_ruled_out_names_and_roots_match_in_any_case_or_spacing(self):
        self.assertIn("ruled out", rename.ruled_out("REWOUND", ["Rewound"], []))
        self.assertIn("ruled out", rename.ruled_out("Re-wound", ["Rewound"], []))
        self.assertIn("root Rewind", rename.ruled_out("Rewindpix", [], ["Rewind"]))
        self.assertIn("root Rewind", rename.ruled_out("Un Re Wind", [], ["Rewind"]))
        self.assertIsNone(rename.ruled_out("Cineroll", ["Rewound"], ["Rewind"]))
        self.assertIsNone(rename.valid_name("Whole Roll"))
        self.assertIsNotNone(rename.valid_name("--"))
        self.assertIsNotNone(rename.valid_name("a/b"))

    def test_the_swap_changes_the_brand_never_a_url_a_word_or_a_bare_domain(self):
        text = "\n".join([
            "Rewound is a camera app; REWOUND in caps; Rewound's roll.",
            "Join at getrewound.app/tiktok or @rewound, second choice rewoundcamera.app.",
            "The film is rewound before the camera is opened.",
            "rewound.app is held by someone else (https://pubapi.registry.google/rdap/domain/rewound.app).",
            "[IM]: https://imore.com/rewound-app-pulled",
            "Rewoundish and preRewound stay.",
        ])
        after, changed, left = rename.swap_text(text, "Rewound", "Whole Roll")
        lines = after.split("\n")
        self.assertEqual(lines[0], "Whole Roll is a camera app; WHOLE ROLL in caps; Whole Roll's roll.")
        self.assertEqual(lines[1], "Join at getwholeroll.app/tiktok or @wholeroll, second choice wholerollcamera.app.")
        self.assertEqual(lines[2:5], text.split("\n")[2:5])
        self.assertEqual([n for n, _ in changed], [1, 2])
        self.assertEqual([(n, in_url) for n, _, in_url in left], [(3, False), (4, True), (5, True), (6, False)])

    def test_the_swap_never_swaps_the_name_it_just_put_in(self):
        after, changed, left = rename.swap_text("Roll is here. ROLL. @roll getroll.app", "Roll", "Cineroll")
        self.assertEqual(after, "Cineroll is here. CINEROLL. @cineroll getcineroll.app")
        self.assertEqual((len(changed), left), (1, []))
        after, _, left = rename.swap_text("Wound app; WOUND; getwound.app\nThe film is wound.", "Wound", "Rewound")
        self.assertEqual(after, "Rewound app; REWOUND; getrewound.app\nThe film is wound.")
        self.assertEqual([n for n, _, _ in left], [2])

    def test_a_url_naming_the_earlier_name_is_kept_and_listed(self):
        line = '<meta property="og:url" content="https://getrewound.app/">'
        after, changed, left = rename.swap_text(line, "Rewound", "Cinewell")
        self.assertEqual((after, changed, left), (line, [], [(1, line, True)]))
        pkg = fixtures.package()
        fixtures.write(pkg, "03-site/meta.html", line + "\n")
        report = rename.swap(pkg, "Rewound", "Cinewell")
        self.assertEqual((pkg / "03-site/meta.html").read_text(), line + "\n")
        work = Path(tempfile.mkdtemp(prefix="gp-work-"))
        sheet = rename.write_review(work / "review.md", "Rewound", "Cinewell", report, work / "b", "Testprod").read_text()
        self.assertIn("### 03-site/meta.html\n\n- URL L1: %s" % line, sheet)

    def test_the_swap_keeps_last30days_output_and_its_fetched_urls(self):
        import hashlib
        pkg = fixtures.package()
        url = "https://www.reddit.com/r/film/comments/abc/"
        raw = fixtures.write(pkg, "01-research/last30days/raw.md", "Filmora the roll first, says %s\n" % url)
        fixtures.write(pkg, "01-research/pain-points-extra.md", "Filmora answers %s\n" % url)
        with open(str(pkg / "sources.md"), "a") as handle:
            handle.write("- %s - fetched 2026-10-24T11:00Z - a Reddit pain\n" % url)
        log = pkg / "run-evidence" / "last30days-log.jsonl"
        log.write_text(json.dumps({"files": [{"path": str(raw), "sha256": hashlib.sha256(raw.read_bytes()).hexdigest()}]}) + "\n")
        self.assertEqual(check_sources.check(pkg)["problems"], [])
        report = rename.swap(pkg, "Filmora", "Cinewell")
        self.assertNotIn("01-research/last30days/raw.md", report["files"])
        self.assertIn("01-research/pain-points-extra.md", report["files"])
        self.assertEqual(raw.read_text(), "Filmora the roll first, says %s\n" % url)
        self.assertEqual(check_sources.check(pkg)["problems"], [])

    def test_the_swap_skips_records_and_lists_what_to_review(self):
        pkg = fixtures.package()
        work = Path(tempfile.mkdtemp(prefix="gp-work-"))
        for rel in ("03-site/index.html", "02-brand/tournament/judge-conversion.md", "decisions-log.md",
                    "08-redteam/dossier.md", "08-redteam/pre-publication-checklist.md", "04-video/build/build.py",
                    "02-brand/logo-wordmark.svg"):
            path = pkg / rel
            prefix = path.read_text(encoding="utf-8") if path.is_file() else ""
            fixtures.write(pkg, rel, prefix + "\nFilmora collided with an app named Filmora.\n")
        fixtures.png(pkg / "10-launch-set/x/post-1.png", "64x64")
        before = {rel: (pkg / rel).read_text() for rel in ("02-brand/tournament/judge-conversion.md",
                                                            "decisions-log.md", "08-redteam/dossier.md")}
        report = rename.swap(pkg, "Filmora", "Cinewell")
        self.assertEqual(sorted(report["files"]), ["02-brand/logo-wordmark.svg", "03-site/index.html",
                                                   "04-video/build/build.py",
                                                   "08-redteam/pre-publication-checklist.md"])
        for rel, text in before.items():
            self.assertEqual((pkg / rel).read_text(), text, rel)
        self.assertIn("Cinewell collided with an app named Cinewell.", (pkg / "04-video/build/build.py").read_text())
        self.assertEqual(report["svgs"], ["02-brand/logo-wordmark.svg"])
        self.assertIn("10-launch-set/x/post-1.png", report["media"])
        sheet = rename.write_review(work / "review.md", "Filmora", "Cinewell", report, work / "backups/x", "Testprod")
        text = sheet.read_text()
        self.assertIn("## Swapped lines (4 in 4 files)", text)
        self.assertIn("- CHECK L", text)
        self.assertIn("- 10-launch-set/x/post-1.png", text)

    def test_the_backup_copies_the_whole_package(self):
        pkg = fixtures.package()
        work = Path(tempfile.mkdtemp(prefix="gp-work-"))
        now = gc.utc_now()
        first = rename.backup(pkg, work, "before-rerun-from-x", now)
        second = rename.backup(pkg, work, "before-rerun-from-x", now)
        self.assertNotEqual(first, second)
        self.assertEqual(first.parent, work / "backups")
        originals = sorted(gc.rel(pkg, f) for f in pkg.rglob("*") if f.is_file())
        self.assertEqual(sorted(gc.rel(first, f) for f in first.rglob("*") if f.is_file()), originals)
        self.assertEqual((first / "run-journal.json").read_bytes(), (pkg / "run-journal.json").read_bytes())


class JournalReopenTest(unittest.TestCase):
    def setUp(self):
        for patcher in (mock.patch.object(check_layout, "default_registries", lambda: [Path(REGISTRY)]),
                        mock.patch.dict(os.environ)):
            patcher.start()
            self.addCleanup(patcher.stop)
        os.environ.pop("GR0WTHPILOT_CONFIG", None)

    def test_a_reopened_gate_passes_again_in_order_with_its_critic(self):
        pkg = fixtures.package()
        pass_through(self, pkg, "critic-1")
        self.assertEqual(quiet(journal.main, ["reopen", "claims-1", "--reason", "the lawyer found a claim.",
                                              "--package", str(pkg)]), 0)
        data = load(pkg)
        self.assertEqual(journal.reopened_ids(data), ["claims-1", "critic-1"])
        self.assertEqual(journal.next_gate(data)[0], "claims-1")
        self.assertIn("Send-back: the lawyer found a claim. Reopened: claims-1, critic-1.", data["notes"][-1]["text"])
        self.assertEqual(quiet(journal.main, ["pass", "critic-1", str(pkg)]), 1)
        self.assertEqual(quiet(journal.main, ["complete", str(pkg)]), 1)
        self.assertEqual(quiet(journal.main, ["pass", "claims-1", str(pkg)]), 0)
        entry = journal.recorded(load(pkg))["claims-1"]
        self.assertNotIn("reopened_at", entry)
        self.assertEqual(entry["reopens"][0]["reason"], "the lawyer found a claim.")
        self.assertEqual(entry["repassed_at"], entry["reopens"][0]["repassed_at"])
        report = pkg / "08-redteam/critic-phase-1.md"
        os.utime(str(report), (time.time() - 600,) * 2)
        self.assertEqual(quiet(journal.main, ["pass", "critic-1", str(pkg)]), 1)
        os.utime(str(report), None)
        self.assertEqual(quiet(journal.main, ["pass", "critic-1", str(pkg)]), 0)
        self.assertEqual(journal.reopened_ids(load(pkg)), [])
        self.assertEqual([g["id"] for g in load(pkg)["gates"]], journal.GATE_IDS[:6])

    def test_reopen_refuses_a_gate_never_passed(self):
        pkg = fixtures.package()
        pass_through(self, pkg, "research")
        self.assertEqual(quiet(journal.main, ["reopen", "brand", "--reason", "x", "--package", str(pkg)]), 1)
        self.assertEqual(journal.reopened_ids(load(pkg)), [])
        self.assertEqual(load(pkg)["notes"], [])


class NameRerunTest(unittest.TestCase):
    def setUp(self):
        for patcher in (mock.patch.object(check_layout, "default_registries", lambda: [Path(REGISTRY)]),
                        mock.patch.dict(os.environ)):
            patcher.start()
            self.addCleanup(patcher.stop)
        os.environ.pop("GR0WTHPILOT_CONFIG", None)
        self.pkg = fixtures.package()
        pass_through(self, self.pkg, "critic-1")
        edit(self.pkg / "02-brand/naming-decision.md", "Testprod.", "Propose Filmora.")
        edit(self.pkg / "02-brand/positioning.md", "For people", "Filmora is for people")
        self.now = "2026-10-28T12:00:00Z"

    def begin(self, names=(), roots=("Film",)):
        data = load(self.pkg)
        info = journal.begin_rerun(self.pkg, data, "Filmora", list(names), list(roots), "/cache/backups/one", self.now)
        save(self.pkg, data)
        return info

    def new_tournament(self):
        t = self.pkg / "02-brand/tournament"
        for i in range(1, 5):
            fixtures.write(t, "pitch-%d.md" % i, "# Pitch %d\n\nNames.\n" % i)
        for j in ("differentiation", "conversion", "defensibility"):
            fixtures.write(t, "rubric-%s.md" % j, "# Rubric\n\nA ruled-out name scores zero.\n")
            fixtures.write(t, "judge-%s.md" % j, "# Judge\n")
        fixtures.write(t, "scorecard.md", "# Scorecard\n\nMargin: 0.4.\n")

    def test_a_rerun_reopens_the_tournament_and_every_later_gate(self):
        info = self.begin(names=["Shutterly"])
        data = load(self.pkg)
        self.assertEqual(journal.reopened_ids(data), ["tournament", "brand", "claims-1", "critic-1"])
        self.assertEqual(journal.passed_ids(data), ["product-facts", "research"])
        self.assertEqual((info["stage"], info["rule_out"], info["rule_out_roots"]),
                         ("shortlist", ["Filmora", "Shutterly"], ["Film"]))
        self.assertEqual(info["earlier_tournament"], "02-brand/tournament-filmora")
        self.assertTrue((self.pkg / "02-brand/tournament-filmora/scorecard.md").is_file())
        self.assertFalse((self.pkg / "02-brand/tournament").exists())
        self.assertIn("Send-back: name-only rerun from Filmora", data["notes"][-2]["text"])
        self.assertIn("/cache/backups/one", data["notes"][-1]["text"])
        self.assertEqual(quiet(journal.main, ["pass", "tournament", str(self.pkg)]), 1)
        self.new_tournament()
        self.assertEqual(quiet(journal.main, ["pass", "tournament", str(self.pkg)]), 0)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(journal.main(["pass", "brand", str(self.pkg)]), 1)
        self.assertIn("waits for the name App Store Connect accepts", out.getvalue())
        with contextlib.redirect_stdout(out):
            journal.main(["status", str(self.pkg)])
        self.assertTrue(json.loads(out.getvalue()[out.getvalue().index("{"):])["waiting_for_name"])

    def test_a_second_rerun_adds_its_names_and_keeps_both_tournaments(self):
        self.begin(names=["Shutterly"])
        self.new_tournament()
        info = self.begin(names=["Grainly"], roots=["Grain"])
        self.assertEqual(info["rule_out"], ["Filmora", "Shutterly", "Grainly"])
        self.assertEqual(info["rule_out_roots"], ["Film", "Grain"])
        self.assertEqual(len(info["backups"]), 2)
        self.assertTrue((self.pkg / "02-brand/tournament-filmora-2/scorecard.md").is_file())
        with self.assertRaises(ValueError):
            journal.begin_rerun(self.pkg, load(self.pkg), "Other", [], [], "/b", self.now)

    def test_the_shortlist_is_checked_then_recorded(self):
        self.begin(names=["Shutterly"])
        path = self.pkg / rename.SHORTLIST
        path.write_text(shortlist_md(["Cinewell", "Rollbook", "Halide Days"]))
        problems, _ = journal.record_shortlist(self.pkg, load(self.pkg), self.now)
        self.assertTrue(has(problems, r"pass the rerun's tournament first"))
        self.new_tournament()
        self.assertEqual(quiet(journal.main, ["pass", "tournament", str(self.pkg)]), 0)
        path.write_text(shortlist_md(["Cinewell", "Filmwise", "shutterly"]))
        problems, _ = journal.record_shortlist(self.pkg, load(self.pkg), self.now)
        self.assertTrue(has(problems, r"Filmwise shares the ruled-out root Film"))
        self.assertTrue(has(problems, r"shutterly is ruled out"))
        path.write_text(shortlist_md(["Cinewell", "Rollbook"], next_step=False))
        problems, _ = journal.record_shortlist(self.pkg, load(self.pkg), self.now)
        self.assertTrue(has(problems, r"ranks 2 names"))
        self.assertTrue(has(problems, r"no '## Next step' section"))
        path.write_text(shortlist_md(["Cinewell", "Rollbook", "Halide Days"]).replace("- Web: none seen.\n", "", 1))
        problems, _ = journal.record_shortlist(self.pkg, load(self.pkg), self.now)
        self.assertEqual(problems, ["Cinewell has no '- Web:' line with its evidence"])
        path.write_text(shortlist_md(["Cinewell", "Rollbook", "Halide Days"]).replace(
            "registry lookup %s" % fixtures.URLS["comp_a"], "not looked up", 1))
        problems, _ = journal.record_shortlist(self.pkg, load(self.pkg), self.now)
        self.assertEqual(len(problems), 1)
        self.assertTrue(has(problems, r"Cinewell's Domains entry 'not looked up' cites no URL"))
        path.write_text(shortlist_md(["Cinewell", "Rollbook", "Halide Days"]))
        self.assertEqual(quiet(journal.main, ["shortlist", str(self.pkg)]), 0)
        info = load(self.pkg)["rename"]
        self.assertEqual((info["shortlist"], info["shortlist_names"]),
                         (rename.SHORTLIST, ["Cinewell", "Rollbook", "Halide Days"]))
        self.assertEqual(quiet(journal.main, ["pass", "brand", str(self.pkg)]), 1)

    def test_a_domain_lookup_that_found_no_registration_is_recorded_unverified(self):
        self.begin()
        self.new_tournament()
        self.assertEqual(quiet(journal.main, ["pass", "tournament", str(self.pkg)]), 0)
        path = self.pkg / rename.SHORTLIST
        registered = "registry lookup %s" % fixtures.URLS["comp_a"]

        def domains(line):
            path.write_text(shortlist_md(["Cinewell", "Rollbook", "Halide Days"]).replace(registered, line, 1))
            return journal.record_shortlist(self.pkg, load(self.pkg), self.now)[0]

        self.assertEqual(domains("cinewell.app: no registration found, UNVERIFIED; cinewell.com registered, lookup %s"
                                 % fixtures.URLS["comp_a"]), [])
        for line, entry in (("cinewell.app: registered to someone else, UNVERIFIED", "cinewell.app: registered"),
                            ("cinewell.app: no registration found", "cinewell.app: no registration found'"),
                            ("no registration found, UNVERIFIED", "no registration found, UNVERIFIED'"),
                            ("cinewell.app and cinewell.com: no registration found, UNVERIFIED", "cinewell.app and")):
            problems = domains(line)
            self.assertEqual(len(problems), 1, line)
            self.assertTrue(has(problems, r"Cinewell's Domains entry '%s" % re.escape(entry)), problems)
        self.assertEqual(domains(""), ["Cinewell's Domains line names no domain"])
        self.assertEqual(domains("cinewell.app: no registration found, UNVERIFIED"), [])
        self.assertEqual(quiet(journal.main, ["shortlist", str(self.pkg)]), 0)

    def test_an_accepted_name_is_swapped_and_its_gates_reopened(self):
        self.begin(names=["Shutterly"])
        self.new_tournament()
        quiet(journal.main, ["pass", "tournament", str(self.pkg)])
        data = load(self.pkg)
        with self.assertRaises(ValueError):
            journal.accept_name(self.pkg, data, "Cinewell", self.pkg.parent / "work", "/b2", self.now)
        (self.pkg / rename.SHORTLIST).write_text(shortlist_md(["Cinewell", "Rollbook", "Halide Days"]))
        self.assertEqual(quiet(journal.main, ["shortlist", str(self.pkg)]), 0)
        data = load(self.pkg)
        with self.assertRaises(ValueError):
            journal.accept_name(self.pkg, data, "Filmwise", self.pkg.parent / "work", "/b2", self.now)
        with self.assertRaises(ValueError) as raised:
            journal.accept_name(self.pkg, data, "Shutterbox", self.pkg.parent / "work", "/b2", self.now)
        self.assertIn("Shutterbox is not on the rerun's shortlist (Cinewell, Rollbook, Halide Days)",
                      str(raised.exception))
        self.assertIn('bin/gr0wthpilot Testprod --rename "Filmora"', str(raised.exception))
        self.assertIn('--rule-out "<name>"', str(raised.exception))
        self.assertEqual(data["rename"]["stage"], "shortlist")
        fixtures.write(self.pkg, "05-social-pmf/notes.md", "Filmora on TikTok, @filmora, getfilmora.app/tiktok.\n")
        edit(self.pkg / "01-research/pain-points.md", "# Pain points", "# Pain points Filmora answers")
        info = journal.accept_name(self.pkg, data, "Cinewell", self.pkg.parent / "work", "/b2", self.now)
        save(self.pkg, data)
        self.assertEqual(data["rename"]["backups"][-1], {"at": self.now, "before": "swap", "path": "/b2"})
        self.assertEqual((info["stage"], info["accepted_name"]), ("swapped", "Cinewell"))
        self.assertEqual((self.pkg / "02-brand/positioning.md").read_text(), "# Positioning\n\nCinewell is for people who miss film.\n")
        self.assertEqual((self.pkg / "05-social-pmf/notes.md").read_text(),
                         "Cinewell on TikTok, @cinewell, getcinewell.app/tiktok.\n")
        self.assertIn("Propose Filmora.", (self.pkg / "02-brand/naming-decision.md").read_text())
        self.assertTrue(Path(info["swap"]["review"]).is_file())
        self.assertEqual(journal.reopened_ids(data), ["brand", "claims-1", "critic-1"])
        self.assertEqual(journal.next_gate(data)[0], "brand")
        self.assertIn("# Pain points Cinewell answers", (self.pkg / "01-research/pain-points.md").read_text())
        self.assertIsNone(journal.waiting_for_name(data, "brand"))
        note = data["notes"][-1]["text"]
        self.assertIn("Name swap to Cinewell: the Founder handed over Cinewell", note)
        self.assertIn(info["swap"]["review"], note)
        self.assertIn("/b2", note)
        with self.assertRaises(ValueError):
            journal.accept_name(self.pkg, data, "Rollbook", self.pkg.parent / "work", "/b3", self.now)


if __name__ == "__main__":
    unittest.main()
