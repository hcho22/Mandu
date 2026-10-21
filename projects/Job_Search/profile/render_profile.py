#!/usr/bin/env python3
"""Validate hcho's Master profile and render its readable views.

The Master profile (master-profile.yaml) is the single source of truth for job
applications: a ledger of Claims, each backed by Linked or Attested evidence.
This script enforces the ledger's rules and generates two pages that must never
be edited by hand:

  master-profile.md  every Claim, grouped by period
  skill-index.md     per skill: employer, project, and coursework time, and lanes

Usage:
  python3 render_profile.py            validate and write both pages
  python3 render_profile.py --check    validate and fail if either page is stale
  python3 render_profile.py --stale    list numbers due for a re-check (default 14 days)
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "master-profile.yaml"
PROFILE_MD = HERE / "master-profile.md"
SKILL_INDEX_MD = HERE / "skill-index.md"

SCALES = ("employer", "project", "coursework")
EVIDENCE_KINDS = ("linked", "attested")
REPO_ACCESS = ("public", "private")
# Can hcho explain the work, how and why, without notes in an interview?
# "study" Claims are not used in tailored drafts until hcho marks them "yes".
INTERVIEW_READY = ("yes", "study")
# Which Evidence scales a Claim may carry, by the kind of period it belongs to.
ALLOWED_SCALES = {
    "employment": {"employer"},
    "volunteer": {"project"},
    "independent": {"project"},
    "career-break": {"project", "coursework"},
    "education": {"coursework"},
}
# Work from this month onward must carry Linked evidence (coursework excepted).
LINKED_REQUIRED_FROM = (2025, 6)
STALE_AFTER_DAYS = 14
GENERATED_NOTE = (
    "_Generated from `master-profile.yaml` by `render_profile.py`. "
    "Do not edit by hand; change the YAML and re-run the script._"
)

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# The location printed on resumes and cover letters: a plain "City, ST", nothing else.
CITY_STATE_RE = re.compile(r"^[A-Z][A-Za-z.' -]*[A-Za-z.], [A-Z]{2}$")
MONTH_RE = re.compile(r"^(\d{4})-(\d{2})$")
YEAR_RE = re.compile(r"^(\d{4})$")


class ProfileError(Exception):
    """The profile breaks one or more ledger rules."""

    def __init__(self, problems: List[str]):
        super().__init__("\n".join(problems))
        self.problems = problems


# ---------------------------------------------------------------- dates


class Month:
    """A start or end date at month or year precision."""

    def __init__(self, year: int, month: Optional[int], present: bool = False):
        self.year = year
        self.month = month
        self.present = present

    @property
    def approximate(self) -> bool:
        return self.month is None

    def label(self) -> str:
        if self.present:
            return "present"
        return str(self.year) if self.month is None else "%04d-%02d" % (self.year, self.month)

    def start_index(self) -> int:
        return self.year * 12 + ((self.month or 1) - 1)

    def end_index(self) -> int:
        """Exclusive end. A year-only end counts up to January of that year."""
        if self.month is None:
            return self.year * 12
        return self.year * 12 + self.month


def parse_month(value, as_of: dt.date) -> Month:
    text = str(value).strip()
    if text == "present":
        return Month(as_of.year, as_of.month, present=True)
    m = MONTH_RE.match(text)
    if m and 1 <= int(m.group(2)) <= 12:
        return Month(int(m.group(1)), int(m.group(2)))
    m = YEAR_RE.match(text)
    if m:
        return Month(int(m.group(1)), None)
    raise ValueError("expected YYYY, YYYY-MM, or 'present', got %r" % (value,))


def parse_date(value) -> dt.date:
    if isinstance(value, dt.date):
        return value
    return dt.datetime.strptime(str(value), "%Y-%m-%d").date()


def merged_months(intervals: List[Tuple[int, int]]) -> int:
    """Total months covered by possibly overlapping [start, end) intervals."""
    total = 0
    current_start, current_end = None, None
    for start, end in sorted(intervals):
        if current_end is None or start > current_end:
            if current_end is not None:
                total += current_end - current_start
            current_start, current_end = start, end
        else:
            current_end = max(current_end, end)
    if current_end is not None:
        total += current_end - current_start
    return total


# ---------------------------------------------------------------- validation


def load(path: Path = SOURCE) -> dict:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate(profile: dict) -> None:
    problems: List[str] = []

    def need(cond: bool, message: str) -> bool:
        if not cond:
            problems.append(message)
        return cond

    for key in ("schema_version", "as_of", "person", "lanes", "skills", "periods", "claims"):
        need(key in profile, "missing top-level key: %s" % key)
    if problems:
        raise ProfileError(problems)

    try:
        as_of = parse_date(profile["as_of"])
    except ValueError:
        raise ProfileError(["as_of must be YYYY-MM-DD"])

    resume_location = (profile["person"] or {}).get("resume_location")
    if resume_location is not None:
        need(bool(CITY_STATE_RE.match(str(resume_location))),
             "person.resume_location must be a plain 'City, ST' such as 'Los Angeles, CA', not %r" % resume_location)

    lanes = set(profile["lanes"] or {})
    skills = profile["skills"] or []
    need(len(skills) == len(set(skills)), "skills vocabulary has duplicates")
    vocabulary = set(skills)

    projects = profile.get("projects") or {}
    for key, project in projects.items():
        need(bool(ID_RE.match(str(key))), "project id %r is not kebab-case" % key)
        need(bool((project or {}).get("name")), "project %s: missing name" % key)
        need((project or {}).get("access") in REPO_ACCESS, "project %s: access must be public or private" % key)

    periods: Dict[str, dict] = {}
    for period in profile["periods"]:
        pid = period.get("id", "?")
        need(bool(ID_RE.match(str(pid))), "period id %r is not kebab-case" % pid)
        need(pid not in periods, "duplicate period id: %s" % pid)
        need(period.get("kind") in ALLOWED_SCALES, "period %s: unknown kind %r" % (pid, period.get("kind")))
        need(bool(period.get("title")), "period %s: missing title" % pid)
        periods[pid] = period

    seen_ids = set()
    used_skills = set()
    for claim in profile["claims"]:
        cid = claim.get("id", "?")
        where = "claim %s" % cid
        need(bool(ID_RE.match(str(cid))), "%s: id is not kebab-case" % where)
        need(cid not in seen_ids, "%s: duplicate id" % where)
        seen_ids.add(cid)
        need(bool(str(claim.get("text", "")).strip()), "%s: missing text" % where)
        if claim.get("project") is not None:
            need(claim["project"] in projects, "%s: unknown project %r" % (where, claim["project"]))
        if "interview_ready" in claim:
            need(claim["interview_ready"] in INTERVIEW_READY, "%s: interview_ready must be yes or study" % where)

        period = periods.get(claim.get("period"))
        if not need(period is not None, "%s: unknown period %r" % (where, claim.get("period"))):
            continue
        scale = claim.get("scale")
        need(scale in SCALES, "%s: scale must be one of %s" % (where, ", ".join(SCALES)))
        need(
            scale in ALLOWED_SCALES.get(period.get("kind"), set()),
            "%s: scale %r is not allowed in a %s period" % (where, scale, period.get("kind")),
        )

        start = end = None
        dates = claim.get("dates") or {}
        kind = (claim.get("evidence") or {}).get("kind")
        if dates.get("pending"):
            # Pending dates add no time to the Skill index, so only Attested
            # Claims (whose dates rest on hcho's word) may use them.
            need(kind == "attested", "%s: only attested claims may leave their dates pending" % where)
            need(bool(claim.get("open_question")), "%s: pending dates need an open_question" % where)
        else:
            try:
                start = parse_month(dates.get("start"), as_of)
                end = parse_month(dates.get("end"), as_of)
                need(end.end_index() > start.start_index(), "%s: dates end before they start" % where)
            except ValueError as exc:
                problems.append("%s: %s" % (where, exc))

        evidence = claim.get("evidence") or {}
        need(kind in EVIDENCE_KINDS, "%s: evidence kind must be linked or attested" % where)
        if kind == "linked":
            refs = evidence.get("refs") or []
            need(bool(refs), "%s: linked evidence needs at least one ref" % where)
        recent = start is not None and (start.year, start.month or 1) >= LINKED_REQUIRED_FROM
        if scale != "coursework" and (recent or period.get("kind") == "independent"):
            need(kind == "linked", "%s: work from June 2025 onward needs linked evidence" % where)

        claim_skills = claim.get("skills") or []
        need(bool(claim_skills), "%s: needs at least one skill" % where)
        for skill in claim_skills:
            need(skill in vocabulary, "%s: skill %r is not in the vocabulary" % (where, skill))
            used_skills.add(skill)
        claim_lanes = claim.get("lanes") or []
        need(bool(claim_lanes), "%s: needs at least one lane" % where)
        for lane in claim_lanes:
            need(lane in lanes, "%s: unknown lane %r" % (where, lane))

        for number in claim.get("numbers") or []:
            for field in ("value", "what", "as_of", "source"):
                need(number.get(field) not in (None, ""), "%s: a number is missing %s" % (where, field))
            if number.get("as_of"):
                try:
                    parse_date(number["as_of"])
                except ValueError:
                    problems.append("%s: number as_of must be YYYY-MM-DD" % where)

    for skill in sorted(vocabulary - used_skills):
        problems.append("skill %r is in the vocabulary but no claim uses it" % skill)

    if problems:
        raise ProfileError(problems)


# ---------------------------------------------------------------- skill index


def skill_rows(profile: dict) -> List[dict]:
    as_of = parse_date(profile["as_of"])
    lane_order = list(profile["lanes"])
    rows = []
    for skill in sorted(profile["skills"], key=str.lower):
        claims = [c for c in profile["claims"] if skill in c["skills"]]
        row = {"skill": skill, "claims": [c["id"] for c in claims]}
        for scale in SCALES:
            scoped = [c for c in claims if c["scale"] == scale]
            dated = [c for c in scoped if not (c.get("dates") or {}).get("pending")]
            if not scoped:
                row[scale] = "none"
                continue
            if not dated:
                row[scale] = "yes, dates pending"
                continue
            starts = [parse_month(c["dates"]["start"], as_of) for c in dated]
            ends = [parse_month(c["dates"]["end"], as_of) for c in dated]
            months = merged_months([(s.start_index(), e.end_index()) for s, e in zip(starts, ends)])
            approx = any(m.approximate for m in starts + ends)
            first = min(starts, key=lambda m: m.start_index())
            last = max(ends, key=lambda m: m.end_index())
            cell = "%s%.1f yrs (%s to %s)" % ("~" if approx else "", months / 12.0, first.label(), last.label())
            if len(dated) < len(scoped):
                cell += ", plus claims with dates pending"
            row[scale] = cell
        lanes = {lane for c in claims for lane in c["lanes"]}
        row["lanes"] = [lane for lane in lane_order if lane in lanes]
        rows.append(row)
    return rows


# ---------------------------------------------------------------- rendering


def _cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def render_skill_index(profile: dict) -> str:
    lanes = profile["lanes"]
    lines = [
        "# Skill index",
        "",
        GENERATED_NOTE,
        "",
        "**Profile as of:** %s" % parse_date(profile["as_of"]).isoformat(),
        "",
        "Each cell is the total time covered by Claims at that Evidence scale, with overlaps counted once.",
        "Project-scale time never counts as employer tenure.",
        "A `~` means at least one contributing date is year-only, so the figure is approximate.",
        "",
        "Lanes: " + "; ".join("`%s` = %s" % (key, name) for key, name in lanes.items()) + ".",
        "",
        "| Skill | Employer | Project | Coursework | Lanes | Claims |",
        "|---|---|---|---|---|---|",
    ]
    for row in skill_rows(profile):
        lines.append(
            "| %s | %s | %s | %s | %s | %s |"
            % (
                _cell(row["skill"]),
                _cell(row["employer"]),
                _cell(row["project"]),
                _cell(row["coursework"]),
                ", ".join(row["lanes"]),
                ", ".join("`%s`" % cid for cid in row["claims"]),
            )
        )
    return "\n".join(lines) + "\n"


def _period_dates(period: dict) -> str:
    start, end = period.get("start"), period.get("end")
    if start is None and end is None:
        return "dates not shown"
    return "%s to %s" % (start, end)


def render_profile(profile: dict) -> str:
    person = profile["person"]
    lines = [
        "# Master profile: %s" % person["name"],
        "",
        GENERATED_NOTE,
        "",
        "**Profile as of:** %s" % parse_date(profile["as_of"]).isoformat(),
        "",
    ]
    labels = (("location", "Location"), ("resume_location", "Location on resumes and cover letters"),
              ("email", "Email"), ("phone", "Phone"), ("linkedin", "LinkedIn"), ("github", "GitHub"))
    for key, label in labels:
        if person.get(key):
            lines.append("- **%s:** %s" % (label, person[key]))
    lines += [
        "",
        "## Timeline",
        "",
        "| Period | Kind | Organization | Dates | Evidence scale |",
        "|---|---|---|---|---|",
    ]
    for period in profile["periods"]:
        scales = sorted(ALLOWED_SCALES[period["kind"]])
        lines.append(
            "| %s | %s | %s | %s | %s |"
            % (
                _cell(period["title"]),
                period["kind"],
                _cell(period.get("org", "-")),
                _period_dates(period),
                ", ".join(scales),
            )
        )

    projects = profile.get("projects") or {}
    for period in profile["periods"]:
        claims = [c for c in profile["claims"] if c["period"] == period["id"]]
        lines += ["", "## %s" % period["title"], ""]
        if period.get("org"):
            lines.append("**%s**, %s, %s." % (period["org"], period.get("location", "Remote"), _period_dates(period)))
        if period.get("resume_subline"):
            lines.append("Resume subline: %s" % period["resume_subline"])
        if period.get("note"):
            lines.append(period["note"])
        current_project = None
        for claim in claims:
            project_id = claim.get("project")
            heading = "###"
            if project_id is not None:
                heading = "####"
                if project_id != current_project:
                    project = projects[project_id]
                    lines += ["", "### %s" % project["name"], ""]
                    lines.append("Repository: %s (%s)." % (project.get("repo", "none"), project["access"]))
                    current_project = project_id
            lines += ["", "%s `%s`" % (heading, claim["id"]), "", claim["text"].strip(), ""]
            dates = claim.get("dates") or {}
            when = "pending" if dates.get("pending") else "%s to %s" % (dates["start"], dates["end"])
            evidence = claim["evidence"]
            access = projects[project_id]["access"] if project_id is not None else "public"
            private_note = "; private repository, links open only for hcho" if access == "private" else ""
            lines.append("- **Dates:** %s" % when)
            lines.append("- **Evidence:** %s, %s scale%s" % (evidence["kind"], claim["scale"], private_note))
            for ref in evidence.get("refs") or []:
                lines.append("  - %s" % ref)
            if evidence.get("note"):
                lines.append("  - %s" % evidence["note"])
            for number in claim.get("numbers") or []:
                lines.append(
                    "- **Number:** %s %s. _As of %s; source: %s._"
                    % (number["value"], number["what"], parse_date(number["as_of"]).isoformat(), number["source"])
                )
            lines.append("- **Skills:** %s" % ", ".join(claim["skills"]))
            lines.append("- **Lanes:** %s" % ", ".join(claim["lanes"]))
            if claim.get("caveats"):
                lines.append("- **Caveats:** %s" % claim["caveats"].strip())
            if claim.get("interview_ready") == "study":
                lines.append("- **Interview-ready:** no. Study this before any draft uses it.")
            if claim.get("open_question"):
                lines.append("- **Open question for hcho:** %s" % claim["open_question"].strip())
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- staleness


def stale_numbers(profile: dict, today: dt.date, days: int = STALE_AFTER_DAYS) -> List[Tuple[str, dict, int]]:
    """Numbers whose as-of date is more than `days` old: re-read their source before use.

    Attested numbers are skipped: they describe finished work and their only
    source is hcho, so there is nothing to re-read.
    """
    found = []
    for claim in profile["claims"]:
        if claim["evidence"]["kind"] == "attested":
            continue
        for number in claim.get("numbers") or []:
            age = (today - parse_date(number["as_of"])).days
            if age > days:
                found.append((claim["id"], number, age))
    return found


# ---------------------------------------------------------------- main


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="fail if the generated pages are stale")
    parser.add_argument("--stale", action="store_true", help="list numbers due for a re-check")
    parser.add_argument("--days", type=int, default=STALE_AFTER_DAYS, help="staleness threshold in days")
    parser.add_argument("--today", help="override today's date (YYYY-MM-DD) for --stale")
    args = parser.parse_args(argv)

    profile = load()
    try:
        validate(profile)
    except ProfileError as exc:
        print("Master profile breaks %d rule(s):" % len(exc.problems), file=sys.stderr)
        for problem in exc.problems:
            print("  - " + problem, file=sys.stderr)
        return 2

    if args.stale:
        today = parse_date(args.today) if args.today else dt.date.today()
        found = stale_numbers(profile, today, args.days)
        if not found:
            print("No numbers older than %d days." % args.days)
        for cid, number, age in found:
            print("%s: %s %s (%d days old; re-read: %s)" % (cid, number["value"], number["what"], age, number["source"]))
        return 0

    outputs = {PROFILE_MD: render_profile(profile), SKILL_INDEX_MD: render_skill_index(profile)}
    if args.check:
        stale = [p.name for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale:
            print("Generated pages are out of date: %s. Run render_profile.py." % ", ".join(stale), file=sys.stderr)
            return 1
        print("Master profile is valid and its pages are current.")
        return 0

    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8")
    print("Wrote %s and %s (%d claims, %d skills)." % (
        PROFILE_MD.name, SKILL_INDEX_MD.name, len(profile["claims"]), len(profile["skills"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
