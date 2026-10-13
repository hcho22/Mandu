#!/usr/bin/env python3
"""Check and build one Application packet from hcho's Master profile.

An Application packet lives in its own folder under applications/ and is driven
by packet.yaml: the role, a one-page resume made only of Master profile Claims,
answers for the application form's text fields, and a note on gaps to own.

Every resume line and answer must cite Claims. Before anything is written, the
packet is refused if it:
  - cites a Claim that does not exist, is marked `interview_ready: study`, or
    (for experience bullets) belongs to a different period;
  - contains a number that none of its cited Claims contains;
  - cites a Linked Claim whose numbers are more than 14 days old;
  - contains a retired phrase, an em dash, or a link to a private repository;
  - lists a skill outside the profile's vocabulary;
  - exceeds an answer's word limit, or renders to more than one page.

Usage:
  python3 build_packet.py <packet-folder>            check, then write the resume
                                                     (.pdf, .docx) and packet.md
  python3 build_packet.py <packet-folder> --check    check only
  python3 build_packet.py <packet-folder> --today YYYY-MM-DD
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Optional

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "profile"))
import render_profile as rp  # noqa: E402

STATUSES = ("draft", "approved", "submitted", "withdrawn")
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
RESUME_BASENAME = "Hyung_Cho_Resume"
NUMBER_RE = re.compile(r"\d[\d,]*(?:\.\d+)?")
URL_RE = re.compile(r"https?://\S+")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


class PacketError(Exception):
    def __init__(self, problems: List[str]):
        super().__init__("\n".join(problems))
        self.problems = problems


# ---------------------------------------------------------------- helpers


def number_tokens(text: str) -> set:
    """Numbers in a string, normalized: '1,687' -> '1687'; trailing dots dropped."""
    return {m.group(0).replace(",", "").rstrip(".") for m in NUMBER_RE.finditer(str(text))}


def claim_number_tokens(claim: dict) -> set:
    """Numbers a line citing this Claim may use: from its text, its numbers, and its date years."""
    tokens = number_tokens(claim["text"])
    for number in claim.get("numbers") or []:
        tokens |= number_tokens(number["value"]) | number_tokens(number["what"])
    dates = claim.get("dates") or {}
    for key in ("start", "end"):
        match = re.match(r"^(\d{4})", str(dates.get(key, "")))
        if match:
            tokens.add(match.group(1))
    return tokens


def period_dates(period: dict) -> str:
    def fmt(value) -> str:
        text = str(value)
        if text == "present":
            return "Present"
        m = re.match(r"^(\d{4})-(\d{2})$", text)
        return "%s %s" % (MONTHS[int(m.group(2)) - 1], m.group(1)) if m else text

    return "%s - %s" % (fmt(period["start"]), fmt(period["end"]))


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def cited_items(packet: dict):
    """Yield (where, item, required_period) for every Claim-citing item in the packet."""
    for i, item in enumerate(packet.get("summary") or []):
        yield "summary[%d]" % i, item, None
    for entry in packet.get("experience") or []:
        for i, item in enumerate(entry.get("bullets") or []):
            yield "experience %s[%d]" % (entry.get("period"), i), item, entry.get("period")
    for i, item in enumerate(packet.get("education") or []):
        yield "education[%d]" % i, item, None
    for i, item in enumerate(packet.get("answers") or []):
        yield "answer %r" % item.get("field", i), item, None


def item_text(item: dict) -> str:
    return " ".join(str(item.get(k, "")) for k in ("label", "text"))


def all_text(packet: dict) -> List[str]:
    texts = [str(packet.get("headline", ""))]
    texts += [item_text(item) for _, item, _ in cited_items(packet)]
    for gap in packet.get("gaps") or []:
        texts += [str(gap.get("gap", "")), str(gap.get("how_to_own_it", ""))]
    return texts


# ---------------------------------------------------------------- validation


def load_packet(folder: Path) -> dict:
    with (folder / "packet.yaml").open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate(packet: dict, profile: dict, today: dt.date) -> None:
    problems: List[str] = []
    claims = {c["id"]: c for c in profile["claims"]}
    periods = {p["id"]: p for p in profile["periods"]}
    vocabulary = set(profile["skills"])
    private_repos = [p["repo"] for p in (profile.get("projects") or {}).values() if p["access"] == "private"]

    role = packet.get("role") or {}
    for key in ("company", "title", "url"):
        if not role.get(key):
            problems.append("role is missing %s" % key)
    if packet.get("status") not in STATUSES:
        problems.append("status must be one of %s" % ", ".join(STATUSES))
    if packet.get("status") == "submitted" and not packet.get("submitted_on"):
        problems.append("a submitted packet needs submitted_on")
    if not packet.get("headline"):
        problems.append("missing headline")
    else:
        cited_anywhere = {cid for _, item, _ in cited_items(packet) for cid in item.get("claims") or []}
        allowed_anywhere = set()
        for cid in cited_anywhere & set(claims):
            allowed_anywhere |= claim_number_tokens(claims[cid])
        loose = sorted(number_tokens(packet["headline"]) - allowed_anywhere)
        if loose:
            problems.append("headline has numbers no cited Claim contains: %s" % ", ".join(loose))

    for entry in packet.get("experience") or []:
        if entry.get("period") not in periods:
            problems.append("experience: unknown period %r" % entry.get("period"))

    stale_ids = {cid for cid, _, _ in rp.stale_numbers(profile, today)}
    for where, item, required_period in cited_items(packet):
        cited = item.get("claims") or []
        if not cited:
            problems.append("%s cites no Claims" % where)
            continue
        allowed = set()
        for cid in cited:
            claim = claims.get(cid)
            if claim is None:
                problems.append("%s cites unknown Claim %r" % (where, cid))
                continue
            if claim.get("interview_ready") == "study":
                problems.append("%s cites %s, which is marked interview_ready: study" % (where, cid))
            if required_period and claim["period"] != required_period:
                problems.append("%s cites %s from period %s" % (where, cid, claim["period"]))
            if cid in stale_ids:
                problems.append("%s cites %s, whose numbers are over 14 days old; re-read the source first" % (where, cid))
            allowed |= claim_number_tokens(claim)
        unsupported = sorted(number_tokens(item_text(item)) - allowed)
        if unsupported:
            problems.append("%s has numbers its Claims do not contain: %s" % (where, ", ".join(unsupported)))

    for answer in packet.get("answers") or []:
        limit = answer.get("limit_words")
        if limit and word_count(answer.get("text", "")) > limit:
            problems.append("answer %r is %d words, over its %d-word limit"
                            % (answer.get("field"), word_count(answer["text"]), limit))

    for group in packet.get("skills") or []:
        for skill in group.get("items") or []:
            if skill not in vocabulary:
                problems.append("skills: %r is not in the profile vocabulary" % skill)

    texts = all_text(packet)
    for text in texts:
        if "—" in text:
            problems.append("em dash found in: %s" % text[:60])
        for url in URL_RE.findall(text):
            if any(url.startswith(repo) for repo in private_repos):
                problems.append("link to a private repository: %s" % url)
    joined = "\n".join(texts).lower()
    for retired in profile.get("retired_phrases") or []:
        if retired["phrase"].lower() in joined:
            problems.append("retired phrase %r (%s)" % (retired["phrase"], retired["reason"]))

    if problems:
        raise PacketError(problems)


# ---------------------------------------------------------------- resume model


def resume_sections(packet: dict, profile: dict) -> dict:
    """The resume as plain data, shared by the HTML, DOCX, and review renderers."""
    person = profile["person"]
    periods = {p["id"]: p for p in profile["periods"]}
    taglines = {p["name"]: p.get("tagline", "") for p in (profile.get("projects") or {}).values()}
    contact = [person.get("location", "").split(";")[0], person.get("email"), person.get("phone"),
               person.get("linkedin"), person.get("github")]
    experience = []
    for entry in packet.get("experience") or []:
        period = periods[entry["period"]]
        # Consecutive bullets with the same label share one project heading.
        groups: List[dict] = []
        for bullet in entry.get("bullets") or []:
            label = bullet.get("label")
            if not groups or groups[-1]["label"] != label:
                groups.append({"label": label, "tagline": taglines.get(label, "") if label else "", "bullets": []})
            groups[-1]["bullets"].append(bullet)
        experience.append({
            "title": period["title"],
            "org": period.get("org", ""),
            "location": period.get("location", ""),
            "dates": period_dates(period),
            "subline": period.get("resume_subline", ""),
            "groups": groups,
        })
    return {
        "name": person["name"],
        "headline": packet["headline"],
        "contact": [c for c in contact if c],
        "summary": " ".join(item["text"].strip() for item in packet.get("summary") or []),
        "experience": experience,
        "skills": packet.get("skills") or [],
        "education": packet.get("education") or [],
    }


# ---------------------------------------------------------------- renderers

CSS = """
@page { size: Letter; margin: 0.45in 0.55in; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 9.5pt; line-height: 1.3; color: #111; margin: 0; }
h1 { font-size: 17pt; margin: 0; letter-spacing: 0.3px; }
.headline { font-size: 10.5pt; font-weight: bold; margin: 2px 0 1px; }
.contact { font-size: 9pt; color: #333; }
h2 { font-size: 9.5pt; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid #555;
     margin: 9px 0 4px; padding-bottom: 1px; }
p { margin: 0; }
.row { display: flex; justify-content: space-between; gap: 12px; }
.role { font-weight: bold; margin-top: 6px; }
.sub { font-style: italic; color: #333; }
.proj { margin-top: 3px; }
ul { margin: 2px 0 0; padding-left: 15px; }
li { margin: 1.5px 0; }
.skills p { margin: 1.5px 0; }
"""


def render_html(model: dict) -> str:
    e = html.escape
    out = ["<!doctype html><html><head><meta charset=\"utf-8\"><title>%s - Resume</title><style>%s</style></head><body>"
           % (e(model["name"]), CSS)]
    out.append("<h1>%s</h1><p class=\"headline\">%s</p><p class=\"contact\">%s</p>"
               % (e(model["name"]), e(model["headline"]), " | ".join(e(c) for c in model["contact"])))
    if model["summary"]:
        out.append("<h2>Summary</h2><p>%s</p>" % e(model["summary"]))
    out.append("<h2>Experience</h2>")
    for job in model["experience"]:
        org = ", ".join(x for x in (job["org"], job["location"]) if x)
        out.append("<div class=\"row role\"><span>%s%s</span><span>%s</span></div>"
                   % (e(job["title"]), (" | " + e(org)) if org else "", e(job["dates"])))
        if job["subline"]:
            out.append("<p class=\"sub\">%s</p>" % e(job["subline"]))
        for group in job["groups"]:
            if group["label"]:
                tagline = (", " + e(group["tagline"])) if group["tagline"] else ""
                out.append("<p class=\"proj\"><b>%s</b>%s</p>" % (e(group["label"]), tagline))
            out.append("<ul>")
            for bullet in group["bullets"]:
                out.append("<li>%s</li>" % e(bullet["text"].strip()))
            out.append("</ul>")
    if model["skills"]:
        out.append("<h2>Skills</h2><div class=\"skills\">")
        for group in model["skills"]:
            out.append("<p><b>%s:</b> %s</p>" % (e(group["label"]), e(", ".join(group["items"]))))
        out.append("</div>")
    if model["education"]:
        out.append("<h2>Education and Training</h2>")
        for item in model["education"]:
            out.append("<p>%s</p>" % e(item["text"].strip()))
    out.append("</body></html>")
    return "".join(out)


def render_pdf(html_text: str, pdf_path: Path) -> int:
    """Print the HTML with headless Chrome and return the page count."""
    if not Path(CHROME).exists():
        raise PacketError(["Chrome not found at %s; set CHROME to its path" % CHROME])
    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "resume.html"
        source.write_text(html_text, encoding="utf-8")
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             "--print-to-pdf=%s" % pdf_path, source.as_uri()],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120,
        )
    pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf_path.read_bytes()))
    if pages == 0:
        raise PacketError(["could not count pages in %s" % pdf_path.name])
    return pages


def render_docx(model: dict, docx_path: Path) -> None:
    from docx import Document
    from docx.enum.text import WD_TAB_ALIGNMENT
    from docx.shared import Inches, Pt

    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Inches(8.5), Inches(11)
    section.left_margin = section.right_margin = Inches(0.55)
    section.top_margin = section.bottom_margin = Inches(0.45)
    right_edge = section.page_width - section.left_margin - section.right_margin
    normal = doc.styles["Normal"]
    normal.font.name, normal.font.size = "Arial", Pt(9.5)
    normal.paragraph_format.space_after = Pt(0)

    def para(text="", bold=False, italic=False, size=None, space_before=0):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(space_before)
        if text:
            run = p.add_run(text)
            run.bold, run.italic = bold, italic
            if size:
                run.font.size = Pt(size)
        return p

    def heading(text):
        p = para(text.upper(), bold=True, space_before=8)
        p.paragraph_format.space_after = Pt(2)

    para(model["name"], bold=True, size=17)
    para(model["headline"], bold=True, size=10.5)
    para(" | ".join(model["contact"]), size=9)
    if model["summary"]:
        heading("Summary")
        para(model["summary"])
    heading("Experience")
    for job in model["experience"]:
        org = ", ".join(x for x in (job["org"], job["location"]) if x)
        p = para(space_before=5)
        p.paragraph_format.tab_stops.add_tab_stop(right_edge, WD_TAB_ALIGNMENT.RIGHT)
        p.add_run(job["title"] + ((" | " + org) if org else "")).bold = True
        p.add_run("\t" + job["dates"]).bold = True
        if job["subline"]:
            para(job["subline"], italic=True)
        for group in job["groups"]:
            if group["label"]:
                p = para(space_before=2)
                p.add_run(group["label"]).bold = True
                if group["tagline"]:
                    p.add_run(", " + group["tagline"])
            for bullet in group["bullets"]:
                doc.add_paragraph(bullet["text"].strip(), style="List Bullet")
    if model["skills"]:
        heading("Skills")
        for group in model["skills"]:
            p = para()
            p.add_run(group["label"] + ": ").bold = True
            p.add_run(", ".join(group["items"]))
    if model["education"]:
        heading("Education and Training")
        for item in model["education"]:
            para(item["text"].strip())
    doc.save(str(docx_path))


def render_review(packet: dict, model: dict, pages: Optional[int], today: dt.date) -> str:
    role = packet["role"]
    lines = [
        "# Application packet: %s, %s" % (role["company"], role["title"]),
        "",
        "_Generated by `build_packet.py` from `packet.yaml` on %s. Do not edit by hand._" % today.isoformat(),
        "",
        "- **Status:** %s%s" % (packet["status"], (" on %s" % packet["submitted_on"]) if packet.get("submitted_on") else ""),
        "- **Posting:** %s" % role["url"],
    ]
    for key, label in (("location", "Location"), ("compensation", "Compensation"), ("fit", "Fit"), ("closes", "Closes")):
        if role.get(key):
            lines.append("- **%s:** %s" % (label, role[key]))
    lines += [
        "- **Checks:** passed (Claims exist and are interview-ready, numbers match their Claims, no stale numbers, "
        "no retired phrases, no em dashes, skills in vocabulary, answers within limits)%s"
        % ("; resume is %d page%s" % (pages, "" if pages == 1 else "s") if pages else ""),
        "- **Files:** `%s.pdf` and `%s.docx`" % (RESUME_BASENAME, RESUME_BASENAME),
        "",
        "## How to submit",
        "",
        "1. Read the resume PDF and the answers below; ask Mandu for any changes.",
        "2. Open the posting, upload `%s.pdf` (or the .docx if the form asks for Word)." % RESUME_BASENAME,
        "3. Paste each answer into its field. Answer the legal questions (work authorization, sponsorship) yourself.",
        "4. After submitting, tell Mandu \"submitted %s\" so the packet is marked submitted with today's date." % role["company"],
        "",
        "## Resume",
        "",
        "**%s**" % model["headline"],
        "",
    ]
    if model["summary"]:
        lines += ["**Summary.** %s" % model["summary"], ""]
        lines.append("_Claims: %s_" % ", ".join(c for item in packet.get("summary") or [] for c in item["claims"]))
        lines.append("")
    for job in model["experience"]:
        lines.append("**%s** | %s | %s" % (job["title"], job["org"] or job["location"], job["dates"]))
        if job["subline"]:
            lines.append("_%s_" % job["subline"])
        lines.append("")
        for group in job["groups"]:
            if group["label"]:
                lines += ["**%s**%s" % (group["label"], (", " + group["tagline"]) if group["tagline"] else ""), ""]
            for bullet in group["bullets"]:
                lines.append("- %s _(%s)_" % (bullet["text"].strip(), ", ".join(bullet["claims"])))
            lines.append("")
    for group in model["skills"]:
        lines.append("- **%s:** %s" % (group["label"], ", ".join(group["items"])))
    if model["skills"]:
        lines.append("")
    for item in model["education"]:
        lines.append("- %s _(%s)_" % (item["text"].strip(), ", ".join(item["claims"])))
    if packet.get("answers"):
        lines += ["", "## Form answers", ""]
        for answer in packet["answers"]:
            limit = (" of %d allowed" % answer["limit_words"]) if answer.get("limit_words") else ""
            lines += ["### %s" % answer["field"], "",
                      answer["text"].strip(), "",
                      "_%d words%s. Claims: %s_" % (word_count(answer["text"]), limit, ", ".join(answer["claims"])), ""]
    if packet.get("gaps"):
        lines += ["## Gaps to own", ""]
        for gap in packet["gaps"]:
            lines += ["- **%s** %s" % (gap["gap"].strip(), gap["how_to_own_it"].strip())]
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------- main


def build(folder: Path, today: dt.date, check_only: bool = False) -> str:
    profile = rp.load()
    rp.validate(profile)
    packet = load_packet(folder)
    validate(packet, profile, today)
    if check_only:
        return "Packet checks passed."
    model = resume_sections(packet, profile)
    html_text = render_html(model)
    pdf_path = folder / ("%s.pdf" % RESUME_BASENAME)
    pages = render_pdf(html_text, pdf_path)
    if pages != 1:
        raise PacketError(["resume renders to %d pages; trim it to one" % pages])
    render_docx(model, folder / ("%s.docx" % RESUME_BASENAME))
    (folder / "packet.md").write_text(render_review(packet, model, pages, today), encoding="utf-8")
    return "Built %s: one-page resume (.pdf, .docx) and packet.md." % folder.name


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder", help="the packet folder containing packet.yaml")
    parser.add_argument("--check", action="store_true", help="run the checks without writing files")
    parser.add_argument("--today", help="override today's date (YYYY-MM-DD) for the staleness check")
    args = parser.parse_args(argv)
    today = rp.parse_date(args.today) if args.today else dt.date.today()
    folder = Path(args.folder).resolve()
    try:
        print(build(folder, today, check_only=args.check))
    except (PacketError, rp.ProfileError) as exc:
        print("Packet %s was not built:" % folder.name, file=sys.stderr)
        for problem in exc.problems:
            print("  - " + problem, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
