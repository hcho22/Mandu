"""Tests for build_packet.py. Run: python3 -m unittest test_build_packet (from this folder)."""

import copy
import datetime as dt
import tempfile
import unittest
from pathlib import Path

import build_packet as bp

TODAY = dt.date(2026, 10, 8)


def profile():
    return {
        "as_of": dt.date(2026, 10, 8),
        "person": {"name": "Test Person", "location": "Burbank, CA (greater Los Angeles); open to remote",
                   "resume_location": "Los Angeles, CA", "email": "t@example.com"},
        "lanes": {"quality": "Quality"},
        "skills": ["C#", "Python"],
        "retired_phrases": [{"phrase": "108 services", "reason": "dead code"}],
        "projects": {
            "pub": {"name": "Pub", "tagline": "a test app", "repo": "https://github.com/x/pub", "access": "public"},
            "priv": {"name": "Priv", "repo": "https://github.com/x/priv", "access": "private"},
        },
        "periods": [
            {"id": "acme", "kind": "employment", "title": "Engineer", "org": "Acme", "start": "2008-02", "end": "2018-07"},
            {"id": "solo", "kind": "independent", "title": "Independent", "start": "2025-06", "end": "present",
             "resume_subline": "Solo work."},
        ],
        "claims": [
            {"id": "acme-tooling", "period": "acme", "text": "Built C# tooling that cut cycles by about 30%.",
             "scale": "employer", "evidence": {"kind": "attested"}, "skills": ["C#"], "lanes": ["quality"],
             "numbers": [{"value": "about 30%", "what": "shorter cycles", "as_of": dt.date(2026, 1, 1), "source": "hcho"}]},
            {"id": "solo-app", "period": "solo", "project": "pub", "text": "Built an app with 1,687 tests.",
             "scale": "project", "evidence": {"kind": "linked", "refs": ["https://github.com/x/pub"]},
             "skills": ["Python"], "lanes": ["quality"],
             "numbers": [{"value": "1,687", "what": "tests", "as_of": dt.date(2026, 10, 1), "source": "count"}]},
            {"id": "solo-shaky", "period": "solo", "project": "pub", "text": "Built a thing.", "scale": "project",
             "evidence": {"kind": "linked", "refs": ["https://github.com/x/pub"]}, "skills": ["Python"],
             "lanes": ["quality"], "interview_ready": "study"},
        ],
    }


def packet():
    return {
        "role": {"company": "Co", "title": "Engineer", "url": "https://example.com/job"},
        "status": "draft",
        "headline": "Engineer | Quality",
        "summary": [{"text": "Ten years of validation.", "claims": ["acme-tooling"]}],
        "experience": [
            {"period": "solo", "bullets": [{"label": "Pub", "text": "Grew the suite to 1,687 tests.", "claims": ["solo-app"]},
                                          {"label": "Pub", "text": "Built an app.", "claims": ["solo-app"]}]},
            {"period": "acme", "bullets": [{"text": "Cut regression cycles by about 30% with C# tooling.", "claims": ["acme-tooling"]}]},
        ],
        "skills": [{"label": "Languages", "items": ["Python", "C#"]}],
        "education": [],
        "answers": [{"field": "Why us?", "limit_words": 20, "text": "Because I test things.", "claims": ["acme-tooling"]}],
        "gaps": [{"gap": "Two paid years.", "how_to_own_it": "Say it plainly."}],
    }


def with_letter(pk=None):
    pk = pk or packet()
    pk["cover_letter"] = {
        "limit_words": 30,
        "greeting": "Dear Hiring Team,",
        "paragraphs": [{"text": "I cut regression cycles by about 30% with C# tooling.", "claims": ["acme-tooling"]},
                       {"text": "I grew a suite to 1,687 tests.", "claims": ["solo-app"]}],
        "closing": "Sincerely,",
    }
    return pk


def problems_for(pk, prof=None, today=TODAY):
    try:
        bp.validate(pk, prof or profile(), today)
    except bp.PacketError as exc:
        return exc.problems
    return []


class ValidationTests(unittest.TestCase):
    def test_base_packet_is_valid(self):
        self.assertEqual(problems_for(packet()), [])

    def test_unknown_claim_is_rejected(self):
        pk = packet()
        pk["summary"][0]["claims"] = ["ghost"]
        self.assertTrue(any("unknown Claim" in p for p in problems_for(pk)))

    def test_uncited_line_is_rejected(self):
        pk = packet()
        pk["summary"][0]["claims"] = []
        self.assertTrue(any("cites no Claims" in p for p in problems_for(pk)))

    def test_number_not_in_claims_is_rejected(self):
        pk = packet()
        pk["experience"][0]["bullets"][0]["text"] = "Grew the suite to 2,000 tests."
        self.assertTrue(any("2000" in p for p in problems_for(pk)))

    def test_number_formatting_is_normalized(self):
        pk = packet()
        pk["experience"][0]["bullets"][0]["text"] = "Grew the suite to 1687 tests."
        self.assertEqual(problems_for(pk), [])

    def test_years_from_claim_dates_are_allowed(self):
        prof = profile()
        prof["claims"][1]["dates"] = {"start": "2025-06", "end": "present"}
        pk = packet()
        pk["experience"][0]["bullets"][0]["text"] = "Since 2025, grew the suite to 1,687 tests."
        self.assertEqual(problems_for(pk, prof), [])
        pk["experience"][0]["bullets"][0]["text"] = "Since 2024, grew the suite to 1,687 tests."
        self.assertTrue(any("2024" in p for p in problems_for(pk, prof)))

    def test_study_claim_is_rejected(self):
        pk = packet()
        pk["experience"][0]["bullets"][0]["claims"] = ["solo-shaky"]
        pk["experience"][0]["bullets"][0]["text"] = "Built a thing."
        self.assertTrue(any("interview_ready: study" in p for p in problems_for(pk)))

    def test_bullet_must_cite_its_own_period(self):
        pk = packet()
        pk["experience"][1]["bullets"][0]["claims"] = ["solo-app"]
        pk["experience"][1]["bullets"][0]["text"] = "Built an app."
        self.assertTrue(any("from period solo" in p for p in problems_for(pk)))

    def test_stale_linked_numbers_are_rejected_but_attested_are_not(self):
        problems = problems_for(packet(), today=dt.date(2026, 10, 30))
        self.assertTrue(any("solo-app" in p and "14 days" in p for p in problems))
        self.assertFalse(any("acme-tooling" in p and "14 days" in p for p in problems))

    def test_retired_phrase_is_rejected(self):
        pk = packet()
        pk["summary"][0]["text"] = "Monitored 108 Services."
        self.assertTrue(any("retired phrase" in p for p in problems_for(pk)))

    def test_headline_numbers_must_come_from_cited_claims(self):
        pk = packet()
        pk["headline"] = "Engineer | 1,687 tests"
        self.assertEqual(problems_for(pk), [])
        pk["headline"] = "Engineer | 12 years of automation"
        self.assertTrue(any("headline" in p and "12" in p for p in problems_for(pk)))

    def test_em_dash_is_rejected(self):
        pk = packet()
        pk["headline"] = "Engineer — Quality"
        self.assertTrue(any("em dash" in p for p in problems_for(pk)))

    def test_private_repo_link_is_rejected(self):
        pk = packet()
        pk["answers"][0]["text"] = "See https://github.com/x/priv/pull/1 for it."
        self.assertTrue(any("private repository" in p for p in problems_for(pk)))

    def test_skill_outside_vocabulary_is_rejected(self):
        pk = packet()
        pk["skills"][0]["items"].append("COBOL")
        self.assertTrue(any("COBOL" in p for p in problems_for(pk)))

    def test_answer_over_word_limit_is_rejected(self):
        pk = packet()
        pk["answers"][0]["text"] = "word " * 25
        self.assertTrue(any("over its 20-word limit" in p for p in problems_for(pk)))

    def test_resume_location_is_required_and_plain(self):
        prof = profile()
        del prof["person"]["resume_location"]
        self.assertTrue(any("resume_location" in p for p in problems_for(packet(), prof)))
        prof["person"]["resume_location"] = "Burbank, CA (greater Los Angeles)"
        self.assertTrue(any("resume_location" in p for p in problems_for(packet(), prof)))

    def test_submitted_needs_a_date(self):
        pk = packet()
        pk["status"] = "submitted"
        self.assertTrue(any("submitted_on" in p for p in problems_for(pk)))

    def test_cover_letter_is_valid(self):
        self.assertEqual(problems_for(with_letter()), [])

    def test_cover_letter_paragraph_must_cite_and_match_numbers(self):
        pk = with_letter()
        pk["cover_letter"]["paragraphs"][1]["text"] = "I grew a suite to 2,000 tests."
        self.assertTrue(any("cover letter paragraph 2" in p and "2000" in p for p in problems_for(pk)))
        pk["cover_letter"]["paragraphs"][1]["claims"] = []
        self.assertTrue(any("cover letter paragraph 2 cites no Claims" in p for p in problems_for(pk)))

    def test_cover_letter_over_word_limit_is_rejected(self):
        pk = with_letter()
        pk["cover_letter"]["limit_words"] = 10
        self.assertTrue(any("cover letter is 17 words, over its 10-word limit" in p for p in problems_for(pk)))

    def test_cover_letter_greeting_may_not_carry_facts_or_em_dashes(self):
        pk = with_letter()
        pk["cover_letter"]["greeting"] = "Dear team of 12,"
        self.assertTrue(any("greeting has numbers" in p for p in problems_for(pk)))
        pk = with_letter()
        pk["cover_letter"]["closing"] = "Thanks — Test"
        self.assertTrue(any("em dash" in p for p in problems_for(pk)))

    def test_empty_cover_letter_is_rejected(self):
        pk = with_letter()
        pk["cover_letter"]["paragraphs"] = []
        self.assertTrue(any("no paragraphs" in p for p in problems_for(pk)))


class RenderTests(unittest.TestCase):
    def test_titles_and_dates_come_from_the_profile(self):
        model = bp.resume_sections(packet(), profile())
        self.assertEqual(model["experience"][1]["dates"], "Feb 2008 - Jul 2018")
        self.assertEqual(model["experience"][0]["dates"], "Jun 2025 - Present")
        self.assertEqual(model["experience"][0]["subline"], "Solo work.")

    def test_contact_line_uses_resume_location_not_search_location(self):
        pk = with_letter()
        for contact in (bp.resume_sections(pk, profile())["contact"], bp.letter_model(pk, profile())["contact"]):
            self.assertEqual(contact[0], "Los Angeles, CA")
            self.assertFalse(any("Burbank" in c or "greater" in c for c in contact))

    def test_consecutive_labels_share_one_project_heading(self):
        model = bp.resume_sections(packet(), profile())
        groups = model["experience"][0]["groups"]
        self.assertEqual([(g["label"], g["tagline"], len(g["bullets"])) for g in groups], [("Pub", "a test app", 2)])
        self.assertEqual([g["label"] for g in model["experience"][1]["groups"]], [None])

    def test_html_escapes_and_shows_project_heading_once(self):
        pk = packet()
        pk["experience"][0]["bullets"][0]["text"] = "Grew the suite to 1,687 tests <fast>."
        html_text = bp.render_html(bp.resume_sections(pk, profile()))
        self.assertEqual(html_text.count("<b>Pub</b>, a test app"), 1)
        self.assertIn("&lt;fast&gt;", html_text)

    def test_docx_renders(self):
        try:
            import docx  # noqa: F401
        except ImportError:
            self.skipTest("python-docx not installed")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "r.docx"
            bp.render_docx(bp.resume_sections(packet(), profile()), path)
            self.assertGreater(path.stat().st_size, 1000)

    def test_review_lists_claims_and_word_counts(self):
        pk = packet()
        review = bp.render_review(pk, bp.resume_sections(pk, profile()), 1, TODAY)
        self.assertIn("_(solo-app)_", review)
        self.assertIn("4 words of 20 allowed", review)
        self.assertIn("resume is 1 page", review)

    @unittest.skipUnless(Path(bp.CHROME).exists(), "Chrome not installed")
    def test_pdf_page_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            pages = bp.render_pdf(bp.render_html(bp.resume_sections(packet(), profile())), Path(tmp) / "r.pdf")
        self.assertEqual(pages, 1)

    def test_letter_html_escapes_and_signs_with_the_profile_name(self):
        pk = with_letter()
        pk["cover_letter"]["paragraphs"][0]["text"] = "I test <things>."
        letter = bp.letter_model(pk, profile())
        self.assertEqual(letter["regarding"], "Re: Engineer, Co")
        html_text = bp.render_letter_html(letter)
        self.assertIn("&lt;things&gt;", html_text)
        self.assertIn("Sincerely,<br>Test Person", html_text)

    def test_review_shows_cover_letter_with_claims_and_word_count(self):
        pk = with_letter()
        review = bp.render_review(pk, bp.resume_sections(pk, profile()), 1, TODAY,
                                  letter=bp.letter_model(pk, profile()), letter_pages=1)
        self.assertIn("## Cover letter", review)
        self.assertIn("_Claims: solo-app_", review)
        self.assertIn("17 words of 30 allowed", review)
        self.assertIn("cover letter is 1 page", review)
        self.assertIn("Hyung_Cho_Cover_Letter.pdf", review)

    def test_submit_steps_name_only_what_the_packet_has(self):
        pk = with_letter()
        pk["answers"] = []
        review = bp.render_review(pk, bp.resume_sections(pk, profile()), 1, TODAY,
                                  letter=bp.letter_model(pk, profile()), letter_pages=1)
        self.assertIn("1. Read the resume PDF and the cover letter; ask Mandu", review)
        self.assertNotIn("Paste each answer", review)
        pk = with_letter()
        review = bp.render_review(pk, bp.resume_sections(pk, profile()), 1, TODAY,
                                  letter=bp.letter_model(pk, profile()), letter_pages=1)
        self.assertIn("1. Read the resume PDF, the cover letter, and the form answers below;", review)
        self.assertIn("3. Paste each answer into its field.", review)

    def test_review_without_letter_has_no_letter_section(self):
        pk = packet()
        review = bp.render_review(pk, bp.resume_sections(pk, profile()), 1, TODAY)
        self.assertNotIn("Cover letter", review)
        self.assertNotIn("cover letter", review)

    def test_letter_docx_renders(self):
        try:
            import docx  # noqa: F401
        except ImportError:
            self.skipTest("python-docx not installed")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "l.docx"
            bp.render_letter_docx(bp.letter_model(with_letter(), profile()), path)
            self.assertGreater(path.stat().st_size, 1000)

    @unittest.skipUnless(Path(bp.CHROME).exists(), "Chrome not installed")
    def test_letter_pdf_page_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            pages = bp.render_pdf(bp.render_letter_html(bp.letter_model(with_letter(), profile())), Path(tmp) / "l.pdf")
        self.assertEqual(pages, 1)


if __name__ == "__main__":
    unittest.main()
