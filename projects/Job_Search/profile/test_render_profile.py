"""Tests for render_profile.py. Run: python3 -m unittest test_render_profile (from this folder)."""

import copy
import datetime as dt
import unittest

import render_profile as rp


def base_profile():
    return {
        "schema_version": 1,
        "as_of": dt.date(2026, 10, 8),
        "person": {"name": "Test Person"},
        "lanes": {"quality": "Quality", "ai-product": "AI product"},
        "skills": ["C#", "Python"],
        "periods": [
            {"id": "acme", "kind": "employment", "title": "Engineer", "org": "Acme", "start": 2008, "end": 2018},
            {"id": "solo", "kind": "independent", "title": "Independent", "start": "2025-06", "end": "present"},
            {"id": "club", "kind": "volunteer", "title": "Volunteer", "start": "2023-04", "end": "2025-06"},
        ],
        "claims": [
            {
                "id": "acme-tooling",
                "period": "acme",
                "text": "Built C# tooling.",
                "dates": {"start": 2008, "end": 2018},
                "scale": "employer",
                "evidence": {"kind": "attested"},
                "skills": ["C#"],
                "lanes": ["quality"],
            },
            {
                "id": "solo-app",
                "period": "solo",
                "text": "Built a Python app.",
                "dates": {"start": "2025-06", "end": "present"},
                "scale": "project",
                "evidence": {"kind": "linked", "refs": ["https://example.com/repo"]},
                "numbers": [{"value": "10", "what": "tests", "as_of": dt.date(2026, 9, 1), "source": "pytest count"}],
                "skills": ["Python"],
                "lanes": ["ai-product"],
            },
        ],
    }


def problems_for(profile):
    try:
        rp.validate(profile)
    except rp.ProfileError as exc:
        return exc.problems
    return []


class ValidationTests(unittest.TestCase):
    def test_base_profile_is_valid(self):
        self.assertEqual(problems_for(base_profile()), [])

    def test_recent_work_needs_linked_evidence(self):
        profile = base_profile()
        profile["claims"][1]["evidence"] = {"kind": "attested"}
        self.assertTrue(any("needs linked evidence" in p for p in problems_for(profile)))

    def test_linked_evidence_needs_a_ref(self):
        profile = base_profile()
        profile["claims"][1]["evidence"] = {"kind": "linked", "refs": []}
        self.assertTrue(any("at least one ref" in p for p in problems_for(profile)))

    def test_volunteer_work_cannot_be_employer_scale(self):
        profile = base_profile()
        claim = copy.deepcopy(profile["claims"][0])
        claim.update(id="club-model", period="club", dates={"start": "2023-04", "end": "2025-06"})
        profile["claims"].append(claim)
        self.assertTrue(any("not allowed in a volunteer period" in p for p in problems_for(profile)))

    def test_unknown_skill_is_rejected(self):
        profile = base_profile()
        profile["claims"][0]["skills"] = ["COBOL"]
        self.assertTrue(any("not in the vocabulary" in p for p in problems_for(profile)))

    def test_unused_vocabulary_skill_is_rejected(self):
        profile = base_profile()
        profile["skills"].append("Rust")
        self.assertTrue(any("'Rust'" in p and "no claim uses it" in p for p in problems_for(profile)))

    def test_number_needs_as_of_and_source(self):
        profile = base_profile()
        profile["claims"][1]["numbers"] = [{"value": "10", "what": "tests"}]
        problems = problems_for(profile)
        self.assertTrue(any("missing as_of" in p for p in problems))
        self.assertTrue(any("missing source" in p for p in problems))

    def test_linked_claims_may_not_leave_dates_pending(self):
        profile = base_profile()
        profile["claims"][1]["dates"] = {"pending": True}
        profile["claims"][1]["open_question"] = "When?"
        self.assertTrue(any("only attested claims" in p for p in problems_for(profile)))

    def test_attested_claims_may_leave_dates_pending_with_a_question(self):
        profile = base_profile()
        profile["claims"][0]["dates"] = {"pending": True}
        self.assertTrue(any("need an open_question" in p for p in problems_for(profile)))
        profile["claims"][0]["open_question"] = "Which months?"
        self.assertEqual(problems_for(profile), [])

    def test_independent_work_needs_linked_evidence_even_without_dates(self):
        profile = base_profile()
        profile["claims"][1]["evidence"] = {"kind": "attested"}
        profile["claims"][1]["dates"] = {"pending": True}
        profile["claims"][1]["open_question"] = "When?"
        self.assertTrue(any("needs linked evidence" in p for p in problems_for(profile)))

    def test_pending_dates_add_no_time(self):
        profile = base_profile()
        profile["claims"][0]["dates"] = {"pending": True}
        profile["claims"][0]["open_question"] = "Which months?"
        rows = {r["skill"]: r for r in rp.skill_rows(profile)}
        self.assertEqual(rows["C#"]["employer"], "yes, dates pending")

    def test_unknown_project_is_rejected(self):
        profile = base_profile()
        profile["claims"][1]["project"] = "ghost"
        self.assertTrue(any("unknown project" in p for p in problems_for(profile)))

    def test_resume_location_must_be_plain_city_and_state(self):
        profile = base_profile()
        profile["person"]["resume_location"] = "Los Angeles, CA"
        self.assertEqual(problems_for(profile), [])
        for bad in ("Burbank, CA (greater Los Angeles)", "Burbank, CA; open to US-remote", "Los Angeles", "Remote"):
            profile["person"]["resume_location"] = bad
            self.assertTrue(any("resume_location" in p for p in problems_for(profile)), bad)

    def test_private_project_is_flagged_in_the_rendered_profile(self):
        profile = base_profile()
        profile["projects"] = {"app": {"name": "App", "repo": "https://example.com/app", "access": "private"}}
        profile["claims"][1]["project"] = "app"
        self.assertEqual(problems_for(profile), [])
        self.assertIn("private repository, links open only for hcho", rp.render_profile(profile))

    def test_interview_ready_accepts_only_yes_or_study(self):
        profile = base_profile()
        profile["claims"][1]["interview_ready"] = "maybe"
        self.assertTrue(any("interview_ready" in p for p in problems_for(profile)))
        profile["claims"][1]["interview_ready"] = "study"
        self.assertEqual(problems_for(profile), [])
        self.assertIn("Study this before any draft uses it", rp.render_profile(profile))

    def test_end_before_start_is_rejected(self):
        profile = base_profile()
        profile["claims"][0]["dates"] = {"start": "2018-05", "end": "2018-01"}
        self.assertTrue(any("end before they start" in p for p in problems_for(profile)))


class SkillIndexTests(unittest.TestCase):
    def test_year_only_dates_are_approximate_ten_years(self):
        rows = {r["skill"]: r for r in rp.skill_rows(base_profile())}
        self.assertEqual(rows["C#"]["employer"], "~10.0 yrs (2008 to 2018)")
        self.assertEqual(rows["C#"]["project"], "none")

    def test_month_dates_count_inclusively_to_present(self):
        rows = {r["skill"]: r for r in rp.skill_rows(base_profile())}
        # 2025-06 through 2026-10 inclusive is 17 months.
        self.assertEqual(rows["Python"]["project"], "1.4 yrs (2025-06 to present)")
        self.assertEqual(rows["Python"]["employer"], "none")

    def test_overlapping_claims_count_once(self):
        self.assertEqual(rp.merged_months([(0, 12), (6, 18), (30, 36)]), 24)

    def test_project_time_never_appears_as_employer_time(self):
        profile = base_profile()
        profile["claims"][1]["skills"] = ["Python", "C#"]
        rows = {r["skill"]: r for r in rp.skill_rows(profile)}
        self.assertEqual(rows["C#"]["employer"], "~10.0 yrs (2008 to 2018)")
        self.assertEqual(rows["C#"]["project"], "1.4 yrs (2025-06 to present)")


class StalenessTests(unittest.TestCase):
    def test_numbers_older_than_threshold_are_listed(self):
        found = rp.stale_numbers(base_profile(), dt.date(2026, 10, 8))
        self.assertEqual([(cid, age) for cid, _, age in found], [("solo-app", 37)])

    def test_attested_numbers_are_never_listed(self):
        profile = base_profile()
        profile["claims"][0]["numbers"] = [
            {"value": "30%", "what": "faster cycles", "as_of": dt.date(2026, 1, 1), "source": "hcho"}
        ]
        found = rp.stale_numbers(profile, dt.date(2026, 10, 8))
        self.assertEqual([cid for cid, _, _ in found], ["solo-app"])

    def test_fresh_numbers_are_not_listed(self):
        self.assertEqual(rp.stale_numbers(base_profile(), dt.date(2026, 9, 10)), [])


class RealProfileTests(unittest.TestCase):
    def test_master_profile_is_valid(self):
        rp.validate(rp.load())

    def test_rendering_is_deterministic(self):
        profile = rp.load()
        self.assertEqual(rp.render_profile(profile), rp.render_profile(profile))
        self.assertEqual(rp.render_skill_index(profile), rp.render_skill_index(profile))


if __name__ == "__main__":
    unittest.main()
