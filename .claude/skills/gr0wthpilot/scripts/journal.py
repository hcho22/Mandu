#!/usr/bin/env python3
"""The run journal: which gates a Gr0wthPilot run has passed, so a run cut off
by a session limit resumes from its last passed gate instead of restarting.

The journal is `run-journal.json` in the Candidate Package. The launcher
creates it; this script is the only thing that records a gate, and it records
one only after that gate's mechanical checks pass and every earlier gate has
passed. A phase's critic gate also needs the critic's report, written after
each of the phase's work gates was first recorded, to end with `Verdict: PASS`.

Usage:
  journal.py status [PACKAGE]
  journal.py pass GATE [PACKAGE]     (a gate passed earlier is checked again, not recorded again)
  journal.py workflow --phase PHASE --name NAME [--run-id ID] [--agents N] [PACKAGE]
  journal.py note TEXT [PACKAGE]
  journal.py complete [PACKAGE]
PACKAGE defaults to the run's Candidate Package (from GR0WTHPILOT_CONFIG).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402
import brand_lint  # noqa: E402
import check_layout  # noqa: E402
import check_recap  # noqa: E402
import check_screenshots  # noqa: E402
import check_sources  # noqa: E402
import check_video  # noqa: E402
import claim_audit  # noqa: E402

# (gate id, phase, what passing it means). The checks are in CHECKS below; the
# full exit criteria each critic applies are in references/phase-gates.md.
GATES = [
    ("product-facts", "read", "The product-facts brief exists and cites the Product's repository"),
    ("research", "1", "Research files, competitor teardowns, and the pain corpus exist; every source was fetched"),
    ("tournament", "1", "At least 4 blind pitches, 3 judge reports, 3 published rubrics, and a scorecard with margins"),
    ("brand", "1", "Positioning, naming verdict, brand guidelines (fresh-agent gate passed), channel plan, thesis"),
    ("claims-1", "1", "Every load-bearing claim is in the ledger with a skeptic verdict; the claim audit passes"),
    ("critic-1", "1", "The completeness critic passed phase 1"),
    ("site", "2", "Two hero variants, screenshots at 390x844 and 1440x900 inspected, no overflow, event list"),
    ("critic-2", "2", "The completeness critic passed phase 2"),
    ("test-kit", "3", "The Test Kit parses as gr0wthlab reads it: 15+ Angles, hook-only pairs, 14-day calendar"),
    ("launch-set", "3", "Instagram, X, and TikTok profile assets and first-week posts; brand lint passes"),
    ("video", "3", "The walkthrough video passed ffprobe, its five frames were viewed, and its strip exists"),
    ("critic-3", "3", "The completeness critic passed phase 3"),
    ("red-team", "4", "Four persona reports, a dossier with a material change and surviving objections, the checklist"),
    ("critic-4", "4", "The completeness critic passed phase 4"),
    ("package", "5", "Every check passes, the recap links everything, the Handoff entry is written, no simulator is left"),
    ("critic-5", "5", "The completeness critic passed phase 5"),
]
GATE_IDS = [g[0] for g in GATES]


def need_files(pkg, names):
    return ["%s is missing" % n for n in names if not (pkg / n).exists()]


def count_glob(pkg, pattern):
    return len([p for p in pkg.glob(pattern) if p.is_file()])


def g_product_facts(pkg, cfg):
    problems = need_files(pkg, ["01-research/product-facts-brief.md", "decisions-log.md", "sources.md"])
    brief = pkg / "01-research/product-facts-brief.md"
    if brief.is_file() and len(re.findall(r"\brepo:\s?[\w./-]+", brief.read_text(encoding="utf-8"))) < 5:
        problems.append("the product-facts brief cites fewer than 5 repo: paths; every product fact cites where "
                        "in the Product's repository it was read")
    return problems


def g_research(pkg, cfg):
    problems = need_files(pkg, ["01-research/pain-points.md"])
    if count_glob(pkg, "01-research/competitor-*.md") < 3:
        problems.append("fewer than 3 competitor teardowns (01-research/competitor-<slug>.md)")
    problems += check_sources.check(pkg)["problems"]
    return problems


def g_tournament(pkg, cfg):
    problems = need_files(pkg, ["02-brand/tournament/scorecard.md"])
    if count_glob(pkg, "02-brand/tournament/pitch-*.md") < 4:
        problems.append("fewer than 4 pitches in 02-brand/tournament/")
    if count_glob(pkg, "02-brand/tournament/judge-*.md") < 3:
        problems.append("fewer than 3 judge reports in 02-brand/tournament/")
    if count_glob(pkg, "02-brand/tournament/rubric-*.md") < 3:
        problems.append("fewer than 3 published rubrics in 02-brand/tournament/")
    card = pkg / "02-brand/tournament/scorecard.md"
    if card.is_file() and not re.search(r"\bmargin", card.read_text(encoding="utf-8"), re.I):
        problems.append("the scorecard shows no margins")
    return problems


def g_brand(pkg, cfg):
    problems = need_files(pkg, ["02-brand/positioning.md", "02-brand/naming-decision.md",
                                "02-brand/brand-guidelines.md", "02-brand/gate-test-report.md",
                                "06-channels/channel-plan.md", "07-thesis/investment-thesis.md"])
    naming = pkg / "02-brand/naming-decision.md"
    if naming.is_file() and "UNVERIFIED" not in naming.read_text(encoding="utf-8"):
        problems.append("the naming decision must say trademark and store-name clearance are UNVERIFIED")
    report = pkg / "02-brand/gate-test-report.md"
    if report.is_file() and last_verdict(report) != "PASS":
        problems.append("the fresh-agent brand gate has not passed (gate-test-report.md must end Verdict: PASS)")
    if not list(pkg.glob("02-brand/gate-test-asset*")):
        problems.append("the fresh agent's test asset is not in 02-brand/")
    return problems


def g_claims(pkg, cfg):
    return claim_audit.check(pkg)["problems"]


def g_site(pkg, cfg):
    return check_screenshots.check_site(pkg)["problems"] + need_files(pkg, ["06-channels/event-metric-schema.md"])


def g_test_kit(pkg, cfg):
    result = check_layout.check(pkg, cfg["product"])
    kit = [p for p in result["problems"] if not p.startswith(("launch-checklist.md", "pre-publication-checklist",
                                                              "08-redteam/", "09-extras/marketing-agent/BUILD-SPEC"))]
    return kit


def g_launch_set(pkg, cfg):
    return check_screenshots.check_launch_set(pkg)["problems"] + brand_lint.check(pkg)["problems"]


def g_video(pkg, cfg):
    try:
        spec = gc.read_json(pkg / "04-video" / "gate.json")
    except (OSError, ValueError):
        return ["04-video/gate.json is missing: {\"video\": \"walkthrough.mp4\", \"size\": \"1080x1920\", "
                "\"min_seconds\": 15, \"max_seconds\": 120}"]
    return check_video.verify(pkg / "04-video" / spec.get("video", "walkthrough.mp4"), spec.get("size", "1080x1920"),
                              int(spec.get("min_seconds", 15)), int(spec.get("max_seconds", 120)))["problems"]


def g_red_team(pkg, cfg):
    problems = need_files(pkg, ["08-redteam/dossier.md", "08-redteam/pre-publication-checklist.md"])
    if count_glob(pkg, "08-redteam/redteam-*.md") < 4:
        problems.append("fewer than 4 red-team persona reports (08-redteam/redteam-<persona>.md)")
    dossier = pkg / "08-redteam/dossier.md"
    if dossier.is_file():
        text = dossier.read_text(encoding="utf-8")
        m = re.search(r"^## Material changes\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        if not m or not re.search(r"^\s*[-*]\s+.*\bbefore\b.*\bafter\b", m.group(1), re.M | re.I):
            problems.append("dossier.md needs a '## Material changes' section with at least one bullet saying "
                            "what changed, before and after; a red team that changed nothing performed, not ran")
        if not re.search(r"^## Surviving objections", text, re.M):
            problems.append("dossier.md needs a '## Surviving objections' section")
    return problems


def all_checks(pkg, cfg):
    problems = []
    problems += ["sources: " + p for p in check_sources.check(pkg)["problems"]]
    problems += ["claims: " + p for p in claim_audit.check(pkg)["problems"]]
    layout = check_layout.check(pkg, cfg["product"], write_entry=True)
    problems += ["layout: " + p for p in layout["problems"]]
    problems += ["brand: " + p for p in brand_lint.check(pkg)["problems"]]
    problems += ["site: " + p for p in check_screenshots.check_site(pkg)["problems"]]
    problems += ["launch-set: " + p for p in check_screenshots.check_launch_set(pkg)["problems"]]
    problems += ["video: " + p for p in g_video(pkg, cfg)]
    problems += ["recap: " + p for p in check_recap.check(pkg, cfg["product"])["problems"]]
    return problems


def g_package(pkg, cfg):
    problems = need_files(pkg, ["README.md", "self-grade.md", "launch-checklist.md", "handoff/README.md",
                                "recap.html", "decisions-log.md", "sources.md"])
    problems += all_checks(pkg, cfg)
    try:
        ledger = gc.read_json(Path(cfg["simulators"]))
        left = [d["name"] for d in ledger.get("devices", []) if not d.get("deleted_at")]
        if left:
            problems.append("simulators still present: %s (run gp-sim cleanup)" % ", ".join(left))
    except (OSError, ValueError, KeyError):
        pass
    return problems


def last_verdict(path):
    verdicts = re.findall(r"^\s*\**Verdict:?\**:?\s*\**\s*(PASS|SEND BACK|FAIL)\b", path.read_text(encoding="utf-8"),
                          re.M | re.I)
    return verdicts[-1].upper() if verdicts else None


def critic(phase):
    def gate(pkg, cfg):
        report = pkg / "08-redteam" / ("critic-phase-%s.md" % phase)
        if not report.is_file():
            return ["08-redteam/%s is missing; run the completeness critic for phase %s" % (report.name, phase)]
        problems = []
        if last_verdict(report) != "PASS":
            problems.append("the phase %s critic's last verdict is not PASS; do what it sent back, then run it again"
                            % phase)
        journal = gc.load_journal(pkg) or {}
        work_gates = [g for g in journal.get("gates", []) if g["id"] in
                      [gid for gid, ph, _ in GATES if ph == phase and not gid.startswith("critic")]]
        if work_gates:
            last = max(gc.parse_iso_z(g["passed_at"]) for g in work_gates)
            if report.stat().st_mtime < last.timestamp():
                problems.append("the critic report is older than the phase's last work gate; run the critic again")
        return problems
    return gate


CHECKS = {
    "product-facts": g_product_facts, "research": g_research, "tournament": g_tournament, "brand": g_brand,
    "claims-1": g_claims, "critic-1": critic("1"), "site": g_site, "critic-2": critic("2"),
    "test-kit": g_test_kit, "launch-set": g_launch_set, "video": g_video, "critic-3": critic("3"),
    "red-team": g_red_team, "critic-4": critic("4"), "package": g_package, "critic-5": critic("5"),
}


def resolve(args_pkg):
    config = os.environ.get("GR0WTHPILOT_CONFIG")
    cfg = gc.read_json(Path(config)) if config and Path(config).is_file() else {}
    pkg = Path(args_pkg).resolve() if args_pkg else Path(cfg.get("package", "."))
    journal = gc.load_journal(pkg)
    if journal is None:
        raise SystemExit("no %s in %s" % (gc.JOURNAL_NAME, pkg))
    cfg.setdefault("product", journal.get("product"))
    cfg.setdefault("simulators", str(Path(cfg.get("work", pkg)) / "simulators.json"))
    return pkg, journal, cfg


def next_gate(journal):
    passed = {g["id"] for g in journal.get("gates", [])}
    for gid, phase, meaning in GATES:
        if gid not in passed:
            return gid, phase, meaning
    return None


def save(pkg, journal):
    gc.write_json(pkg / gc.JOURNAL_NAME, journal)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd")
    s = sub.add_parser("status")
    s.add_argument("package", nargs="?")
    p = sub.add_parser("pass")
    p.add_argument("gate", choices=GATE_IDS)
    p.add_argument("package", nargs="?")
    w = sub.add_parser("workflow")
    w.add_argument("--phase", required=True)
    w.add_argument("--name", required=True)
    w.add_argument("--run-id")
    w.add_argument("--agents", type=int)
    w.add_argument("package", nargs="?")
    n = sub.add_parser("note")
    n.add_argument("text")
    n.add_argument("package", nargs="?")
    c = sub.add_parser("complete")
    c.add_argument("package", nargs="?")
    args = parser.parse_args(argv)
    if not args.cmd:
        parser.print_help()
        return 2
    pkg, journal, cfg = resolve(getattr(args, "package", None))
    now = gc.iso_z(gc.utc_now())
    if args.cmd == "status":
        nxt = next_gate(journal)
        print(json.dumps({
            "run_id": journal.get("run_id"), "status": journal.get("status"), "package": str(pkg),
            "passed": [g["id"] for g in journal.get("gates", [])],
            "next_gate": {"id": nxt[0], "phase": nxt[1], "means": nxt[2]} if nxt else None,
            "workflows": len(journal.get("workflows", [])), "sessions": len(journal.get("sessions", [])),
        }, indent=2))
        return 0
    if journal.get("status") == "complete":
        print("this run is complete; nothing more is recorded")
        return 1
    if args.cmd == "pass":
        nxt = next_gate(journal)
        passed = [g["id"] for g in journal.get("gates", [])]
        if args.gate in passed:
            problems = CHECKS[args.gate](pkg, cfg)
            for problem in problems:
                print("FAIL " + problem)
            if problems:
                print("FAIL: gate %s passed earlier, but its checks fail now (%d problem(s)); fix them"
                      % (args.gate, len(problems)))
                return 1
            print("PASS: gate %s passed earlier and its checks still pass" % args.gate)
            return 0
        if not nxt or nxt[0] != args.gate:
            print("FAIL gates pass in order; the next gate is %s" % (nxt[0] if nxt else "none"))
            return 1
        problems = CHECKS[args.gate](pkg, cfg)
        if problems:
            for problem in problems:
                print("FAIL " + problem)
            print("FAIL: gate %s not passed (%d problem(s))" % (args.gate, len(problems)))
            return 1
        journal.setdefault("gates", []).append({"id": args.gate, "passed_at": now})
        save(pkg, journal)
        nxt = next_gate(journal)
        print("PASS: gate %s recorded; next: %s" % (args.gate, nxt[0] if nxt else "journal.py complete"))
        return 0
    if args.cmd == "workflow":
        journal.setdefault("workflows", []).append({"phase": args.phase, "name": args.name, "run_id": args.run_id,
                                                    "agents": args.agents, "at": now})
        save(pkg, journal)
        print("recorded workflow %s" % args.name)
        return 0
    if args.cmd == "note":
        journal.setdefault("notes", []).append({"at": now, "text": args.text})
        save(pkg, journal)
        print("noted")
        return 0
    if args.cmd == "complete":
        nxt = next_gate(journal)
        if nxt:
            print("FAIL the run is not done; the next gate is %s" % nxt[0])
            return 1
        journal["status"] = "complete"
        journal["completed_at"] = now
        save(pkg, journal)
        print("complete")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
