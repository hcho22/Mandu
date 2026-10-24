"""Tests for the Candidate Package checks: each passes on the fixture package
and fails when the one thing it guards is broken.

Run from Mandu's root: python3 -m unittest discover -s .claude/skills/gr0wthpilot/tests
"""

from __future__ import annotations

import contextlib
import io
import json
import re
import unittest
from pathlib import Path

import fixtures

import brand_lint
import check_layout
import check_recap
import check_screenshots
import check_sources
import check_video
import claim_audit
import journal

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
        lines = [l for l in log.read_text().splitlines() if fixtures.URLS["stat"] not in l]
        log.write_text("\n".join(lines) + "\n")
        self.assertTrue(has(check_sources.check(pkg)["problems"], r"research.example.org/report was not fetched"))

    def test_dead_link_fails(self):
        pkg = fixtures.package()
        log = pkg / "run-evidence" / "fetch-log.jsonl"
        edit(log, '"url": "%s", "code": 200' % fixtures.URLS["stat"], '"url": "%s", "code": 404' % fixtures.URLS["stat"])
        self.assertTrue(has(check_sources.check(pkg)["problems"], r"dead or refused link \(HTTP 404\)"))

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

    def test_html_stat_needs_citation(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/teaser.html", "<p>The market grew 30% last year.</p>")
        self.assertTrue(has(claim_audit.check(pkg)["problems"], r"teaser.html: percentage"))

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

    def test_notes_outside_copy_fields_are_not_linted(self):
        pkg = fixtures.package()
        with open(str(pkg / "05-social-pmf/week-1-drafts.md"), "a") as handle:
            handle.write("\nFilming note: never say revolutionary, 10k users, or use \u2014 dashes.\n")
        self.assertEqual(brand_lint.check(pkg)["problems"], [])


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
        lines = [l for l in path.read_text().splitlines() if not re.match(r"\| P1[0-5] ", l)]
        path.write_text("\n".join(lines) + "\n")
        edit(path, '"Hook number 3 for the camera"', "Hook number 3 for the camera")
        problems = self.check(pkg)["problems"]
        self.assertTrue(has(problems, r"9 Angles; a Test Kit needs at least 15"))
        self.assertTrue(has(problems, r"P03 Hook must be one straight-quoted string"))

    def test_pain_needs_url_and_platform_must_be_supported(self):
        pkg = fixtures.package()
        path = pkg / "05-social-pmf/angles.md"
        edit(path, "per %s |" % fixtures.URLS["pain"][0], "per a forum |")
        edit(path, "| YouTube Shorts | watched", "| Instagram | watched")
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
        fixtures.write(pkg, "03-site/screenshots/index-390.json", json.dumps({"scrollWidth": 470, "innerWidth": 390, "overflows": True}))
        self.assertTrue(has(check_screenshots.check_site(pkg)["problems"], r"index.html overflows horizontally at 390px"))

    def test_one_variant_fails(self):
        pkg = fixtures.package()
        (pkg / "03-site/index-b.html").unlink()
        self.assertTrue(has(check_screenshots.check_site(pkg)["problems"], r"needs two hero variants"))

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

    def test_prepare_writes_frames_strip_and_report(self):
        pkg = fixtures.package()
        for p in (pkg / "04-video" / "frames").glob("*.png"):
            p.unlink()
        (pkg / "04-video" / "frame-strip.png").unlink()
        quiet(check_video.prepare, self.video(pkg))
        self.assertEqual(len(list((pkg / "04-video" / "frames").glob("frame-*.png"))), 5)
        self.assertTrue((pkg / "04-video" / "frame-strip.png").is_file())
        self.assertIn("has_audio: True", (pkg / "04-video" / "ffprobe-report.txt").read_text())


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

    def test_handoff_line_and_clearance(self):
        pkg = fixtures.package()
        edit(pkg / "recap.html", "Testprod - hand to gr0wthlab", "hand it over")
        edit(pkg / "recap.html", "UNVERIFIED", "pending")
        problems = check_recap.check(pkg, fixtures.PRODUCT)["problems"]
        self.assertTrue(has(problems, r"'Testprod - hand to gr0wthlab' word for word"))
        self.assertTrue(has(problems, r"UNVERIFIED"))

    def test_every_extra_must_be_mapped(self):
        pkg = fixtures.package()
        fixtures.write(pkg, "09-extras/pitch-deck.html", "<p>deck</p>")
        self.assertTrue(has(check_recap.check(pkg, fixtures.PRODUCT)["problems"], r"does not link the extra 09-extras/pitch-deck.html"))

    def test_missing_section(self):
        pkg = fixtures.package()
        edit(pkg / "recap.html", 'id="objection"', 'id="other"')
        self.assertTrue(has(check_recap.check(pkg, fixtures.PRODUCT)["problems"], r'id="objection"'))


def quiet(func, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return func(*args)


class JournalTest(unittest.TestCase):
    def run_gate(self, pkg, gate):
        return quiet(journal.main, ["pass", gate, str(pkg)])

    def test_gates_pass_in_order_on_the_fixture(self):
        pkg = fixtures.package()
        self.assertEqual(self.run_gate(pkg, "research"), 1)
        import os
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
        import os
        report.write_text("Round 1\n\nVerdict: PASS\n\nRound 2\n\nVerdict: SEND BACK\n")
        self.assertEqual(self.run_gate(pkg, "critic-1"), 1)
        report.write_text("Round 3\n\nVerdict: PASS\n")
        os.utime(str(report), (1, 1))
        self.assertEqual(self.run_gate(pkg, "critic-1"), 1)
        os.utime(str(report), None)
        self.assertEqual(self.run_gate(pkg, "critic-1"), 0)

    def test_red_team_must_change_something(self):
        pkg = fixtures.package()
        (pkg / "08-redteam/dossier.md").write_text("# Dossier\n\n## Material changes\n\nNone.\n\n## Surviving objections\n\n- x\n")
        self.assertTrue(has(journal.g_red_team(pkg, {}), r"performed, not ran"))

    def test_complete_refuses_before_the_last_gate(self):
        pkg = fixtures.package()
        self.assertEqual(quiet(journal.main, ["complete", str(pkg)]), 1)


if __name__ == "__main__":
    unittest.main()
