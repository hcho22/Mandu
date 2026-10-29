#!/usr/bin/env python3
"""The run journal: which gates a Gr0wthPilot run has passed, so a run cut off
by a session limit resumes from its last passed gate instead of restarting.

The journal is `run-journal.json` in the Candidate Package. The launcher
creates it; this script is the only thing that records a gate, and it records
one only after that gate's mechanical checks pass and every earlier gate has
passed. A phase's critic gate also needs the critic's report to end with
`Verdict: PASS` and to be newer than the latest pass of each of the phase's
work gates, its first pass or a later re-pass, so a fix re-gated after the
critic ran sends the critic round again. The `package` gate re-checks every
earlier phase's critic that way, and `complete` re-checks all five.

A later phase that sends a gate back reopens it: the gate keeps its record but
counts as not passed, so the run passes it again, in order, before any later
gate. Reopening a work gate reopens its phase's critic too, and every reopen is
noted in the journal as a send-back.

A name-only rerun (the launcher's `--rename`) reopens the tournament and every
gate after it, and the journal refuses every gate after the tournament until
the Founder hands over the name App Store Connect accepted (`--accept-name`);
the rerun ends at the shortlist `journal.py shortlist` records. The hand-over
swaps the name through the package and reopens each gate whose files changed.

Usage:
  journal.py status [PACKAGE]
  journal.py pass GATE [PACKAGE]     (a gate passed earlier is checked again, not recorded again)
  journal.py reopen GATE [GATE ...] --reason TEXT [--package PACKAGE]
  journal.py shortlist [PACKAGE]     (a name-only rerun's ranked shortlist, checked and recorded)
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
import rename  # noqa: E402

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
    problems += stale_critics(pkg, [ph for ph in PHASES if ph != "5"])
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


WORK_GATES = {}
for _gid, _phase, _ in GATES:
    if not _gid.startswith("critic-"):
        WORK_GATES.setdefault(_phase, []).append(_gid)
PHASES = [gid.split("-", 1)[1] for gid in GATE_IDS if gid.startswith("critic-")]


def last_passed(entry):
    """When a recorded gate last passed: its first pass, or its latest re-pass."""
    return gc.parse_iso_z(entry.get("repassed_at") or entry["passed_at"])


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
        work_gates = [g for g in journal.get("gates", []) if g["id"] in WORK_GATES.get(phase, [])]
        if work_gates:
            latest = max(work_gates, key=last_passed)
            if report.stat().st_mtime < last_passed(latest).timestamp():
                problems.append("the phase %s critic report is older than the last pass of gate %s; run the critic "
                                "again" % (phase, latest["id"]))
        return problems
    return gate


def stale_critics(pkg, phases):
    """Problems of each recorded critic gate of these phases, checked again."""
    passed = set(passed_ids(gc.load_journal(pkg) or {}))
    problems = []
    for phase in phases:
        if "critic-" + phase in passed:
            problems += ["critic-%s: %s" % (phase, p) for p in critic(phase)(pkg, {})]
    return problems


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


def recorded(journal):
    """Each recorded gate's entry, by id."""
    return {g["id"]: g for g in journal.get("gates", [])}


def passed_ids(journal):
    """Recorded gates that are not reopened, in the order they were recorded."""
    return [g["id"] for g in journal.get("gates", []) if not g.get("reopened_at")]


def reopened_ids(journal):
    return [gid for gid in GATE_IDS if recorded(journal).get(gid, {}).get("reopened_at")]


def next_gate(journal):
    passed = set(passed_ids(journal))
    for gid, phase, meaning in GATES:
        if gid not in passed:
            return gid, phase, meaning
    return None


def phase_of(gid):
    return next(ph for g, ph, _ in GATES if g == gid)


def add_note(journal, text, now):
    journal.setdefault("notes", []).append({"at": now, "text": text})


def reopen(journal, gate_ids, reason, now):
    """Reopen these recorded gates, and the critic of each work gate's phase,
    so each must pass again, in order. Returns the gates newly reopened; a gate
    never passed, or already reopened, is left as it is. Notes the send-back."""
    wanted = set(gate_ids)
    wanted |= {"critic-" + phase_of(g) for g in gate_ids if not g.startswith("critic-")}
    entries, out = recorded(journal), []
    for gid in GATE_IDS:
        entry = entries.get(gid)
        if gid in wanted and entry and not entry.get("reopened_at"):
            entry["reopened_at"] = now
            entry["reopen_reason"] = reason
            out.append(gid)
    if out:
        add_note(journal, "Send-back: %s Reopened: %s." % (reason, ", ".join(out)), now)
    return out


def waiting_for_name(journal, gate):
    """Why a name-only rerun refuses this gate, or None: every gate after the
    tournament waits until the Founder hands over an accepted name."""
    stage = (journal.get("rename") or {}).get("stage")
    if stage == "shortlist" and GATE_IDS.index(gate) > GATE_IDS.index("tournament"):
        return ("gate %s waits for the name App Store Connect accepts: this name-only rerun ends at its shortlist "
                "(journal.py shortlist), and the Founder hands the accepted name over with `bin/gr0wthpilot %s "
                "--accept-name \"<name>\"`" % (gate, journal.get("product")))
    return None


# The package files each gate's checks read, by path prefix; "*" is every file.
# A swap reopens each passed gate whose files it changed.
GATE_FILES = {
    "product-facts": ["01-research/product-facts-brief.md", "decisions-log.md", "sources.md"],
    "research": ["01-research/", "sources.md"],
    "tournament": [rename.TOURNAMENT + "/"],
    "brand": ["02-brand/", "06-channels/channel-plan.md", "07-thesis/"],
    "claims-1": "*",
    "site": ["03-site/", "06-channels/event-metric-schema.md"],
    "test-kit": ["05-social-pmf/", "09-extras/marketing-agent/", "launch-checklist.md",
                 "08-redteam/pre-publication-checklist.md"],
    "launch-set": ["10-launch-set/", "05-social-pmf/", "09-extras/marketing-agent/"],
    "video": ["04-video/"],
    "red-team": ["08-redteam/"],
    "package": "*",
}


def gates_touching(changed):
    """Work gates whose checks read any of these package paths."""
    out = []
    for gid, prefixes in GATE_FILES.items():
        if changed and (prefixes == "*" or any(rel.startswith(p) for rel in changed for p in prefixes)):
            out.append(gid)
    return out


def rerun_refusal(journal, old):
    """Why this run cannot start a name-only rerun from `old`, or None."""
    current = journal.get("rename") or {}
    if "tournament" not in recorded(journal):
        return ("the run has not passed its tournament yet, so there is no name to rerun; resume it with "
                "`bin/gr0wthpilot %s`" % journal.get("product"))
    if current.get("stage") == "shortlist" and rename.slug(current.get("old_name")) != rename.slug(old):
        return ("a name-only rerun from %s is already waiting for its accepted name; hand one over with "
                "--accept-name, or rerun from %s" % (current["old_name"], current["old_name"]))
    return None


def accept_refusal(journal, new):
    """Why `new` cannot be handed over now, or None."""
    current = journal.get("rename") or {}
    product = journal.get("product")
    if current.get("stage") != "shortlist":
        return ("no name-only rerun is waiting for an accepted name; start one with `bin/gr0wthpilot %s --rename "
                "<the name App Store Connect refused>`" % product)
    if not current.get("shortlist"):
        return ("the name-only rerun has not recorded its shortlist yet; resume it with `bin/gr0wthpilot %s`"
                % product)
    return rename.valid_name(new) or rename.ruled_out(new, current["rule_out"], current["rule_out_roots"])


def begin_rerun(pkg, journal, old, names, roots, backup_dir, now):
    """Start a name-only rerun from `old`, the name App Store Connect refused.

    Sets the earlier tournament aside in the package, reopens the tournament
    and every later recorded gate, and records the rerun in the journal's
    `rename` block with the ruled-out names, which always include `old`. A
    second rerun from the same name while the first waits for its accepted
    name adds its ruled-out names to the first's. Raises ValueError when the
    run cannot rerun its name."""
    why = rerun_refusal(journal, old)
    if why:
        raise ValueError(why)
    current = journal.get("rename") or {}
    if current.get("stage") == "shortlist":
        names = current.get("rule_out", []) + list(names)
        roots = current.get("rule_out_roots", []) + list(roots)
    elif current:
        journal.setdefault("renames", []).append(current)
        current = {}
    names = unique([old] + list(names))
    roots = unique(roots)
    moved = rename.set_aside_tournament(pkg, old)
    later = GATE_IDS[GATE_IDS.index("tournament"):]
    reason = ("name-only rerun from %s, which App Store Connect refused; the Founder started it with the launcher's "
              "--rename. Ruled out: %s%s. The positioning, hero message, and look stay as they are." % (
                  old, ", ".join(names), ", and every name holding the root " + " or ".join(roots) if roots else ""))
    reopen(journal, later, reason, now)
    add_note(journal, "Name-only rerun from %s: the package as it was before the rerun is kept in %s; the earlier "
             "tournament is %s." % (old, backup_dir, moved or "absent"), now)
    journal["rename"] = {
        "stage": "shortlist", "old_name": old, "rule_out": names, "rule_out_roots": roots,
        "started_at": now, "earlier_tournament": moved,
        "backups": current.get("backups", []) + [{"at": now, "before": "rerun", "path": str(backup_dir)}],
        "shortlist": None, "shortlist_names": [], "accepted_name": None,
    }
    return journal["rename"]


def accept_name(pkg, journal, new, work, backup_dir, now):
    """Swap `new`, the name App Store Connect accepted, through the package
    in place of the rerun's earlier name, write the review sheet into the
    cache folder, and reopen each recorded gate whose files the swap changed,
    with the brand gate always (its naming decision is rewritten for the new
    name). Raises ValueError when no rerun waits for a name, or the name is
    ruled out."""
    why = accept_refusal(journal, new)
    if why:
        raise ValueError(why)
    current = journal["rename"]
    product = journal.get("product")
    old = current["old_name"]
    report = rename.swap(pkg, old, new)
    review = rename.write_review(Path(work) / "rename" / ("%s-%s-review.md" % (now.replace(":", ""), rename.slug(new))),
                                 old, new, report, backup_dir, product)
    reason = ("the Founder handed over %s, which App Store Connect accepted, with the launcher's --accept-name; the "
              "launcher swapped it through the package in place of %s (%d lines in %d files); the review sheet is %s."
              % (new, old, sum(report["files"].values()), len(report["files"]), review))
    reopen(journal, ["brand"] + gates_touching(list(report["files"])), reason, now)
    add_note(journal, "Name swap to %s: the package as it was before the swap is kept in %s." % (new, backup_dir), now)
    current.update({
        "stage": "swapped", "accepted_name": new, "accepted_at": now,
        "on_shortlist": rename.slug(new) in {rename.slug(n) for n in current.get("shortlist_names", [])},
        "backups": current.get("backups", []) + [{"at": now, "before": "swap", "path": str(backup_dir)}],
        "swap": {"review": str(review), "files": len(report["files"]), "lines": sum(report["files"].values()),
                 "left": sum(len(v) for v in report["left"].values()), "svgs": report["svgs"],
                 "media": len(report["media"])},
    })
    return current


def record_shortlist(pkg, journal, now):
    """(problems, names): check a rerun's shortlist and, when it passes,
    record it, which ends the rerun until the Founder hands a name over."""
    current = journal.get("rename") or {}
    if current.get("stage") != "shortlist":
        return ["no name-only rerun is open; the shortlist belongs to one (the launcher's --rename)"], []
    if "tournament" not in passed_ids(journal):
        return ["pass the rerun's tournament first (journal.py pass tournament)"], []
    problems, names = rename.check_shortlist(pkg / rename.SHORTLIST, journal.get("product"),
                                             current["rule_out"], current["rule_out_roots"])
    problems += ["sources: " + p for p in check_sources.check(pkg)["problems"]]
    if not problems:
        current.update(shortlist=rename.SHORTLIST, shortlist_at=now, shortlist_names=names)
        add_note(journal, "Name-only rerun from %s ended at its shortlist (%s): %s. The Founder tries them in App Store "
                 "Connect in that order." % (current["old_name"], rename.SHORTLIST, ", ".join(names)), now)
    return problems, names


def unique(items):
    out = []
    for item in items:
        if item and rename.slug(item) not in {rename.slug(i) for i in out}:
            out.append(item)
    return out


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
    r = sub.add_parser("reopen")
    r.add_argument("gates", nargs="+", choices=GATE_IDS, metavar="GATE")
    r.add_argument("--reason", required=True)
    r.add_argument("--package")
    sl = sub.add_parser("shortlist")
    sl.add_argument("package", nargs="?")
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
            "passed": passed_ids(journal), "reopened": reopened_ids(journal),
            "next_gate": {"id": nxt[0], "phase": nxt[1], "means": nxt[2]} if nxt else None,
            "waiting_for_name": bool(nxt and waiting_for_name(journal, nxt[0])),
            "rename": journal.get("rename"),
            "workflows": len(journal.get("workflows", [])), "sessions": len(journal.get("sessions", [])),
        }, indent=2))
        return 0
    if journal.get("status") == "complete":
        print("this run is complete; nothing more is recorded")
        return 1
    if args.cmd == "pass":
        nxt = next_gate(journal)
        passed = passed_ids(journal)
        waiting = waiting_for_name(journal, args.gate)
        if waiting:
            print("FAIL " + waiting)
            return 1
        if args.gate in passed:
            problems = CHECKS[args.gate](pkg, cfg)
            for problem in problems:
                print("FAIL " + problem)
            if problems:
                print("FAIL: gate %s passed earlier, but its checks fail now (%d problem(s)); fix them"
                      % (args.gate, len(problems)))
                return 1
            phase = phase_of(args.gate)
            if args.gate in WORK_GATES.get(phase, []):
                entry = recorded(journal)[args.gate]
                entry["repassed_at"] = now
                save(pkg, journal)
                if "critic-" + phase in passed:
                    print("NOTE: the phase %s critic passed before this re-pass; run it again, then pass critic-%s"
                          % (phase, phase))
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
        entry = recorded(journal).get(args.gate)
        if entry:
            entry.setdefault("reopens", []).append({"reopened_at": entry.pop("reopened_at"),
                                                    "reason": entry.pop("reopen_reason", None), "repassed_at": now})
            entry["repassed_at"] = now
            verb = "passed again after its send-back"
        else:
            journal.setdefault("gates", []).append({"id": args.gate, "passed_at": now})
            verb = "recorded"
        save(pkg, journal)
        nxt = next_gate(journal)
        print("PASS: gate %s %s; next: %s" % (args.gate, verb, nxt[0] if nxt else "journal.py complete"))
        if nxt and waiting_for_name(journal, nxt[0]):
            print("NOTE: the next gate waits for the Founder's accepted name; write the shortlist and record it with "
                  "journal.py shortlist")
        return 0
    if args.cmd == "reopen":
        unknown = [g for g in args.gates if g not in recorded(journal)]
        if unknown:
            print("FAIL gate(s) never passed, so there is nothing to send back: %s" % ", ".join(unknown))
            return 1
        reopened = reopen(journal, args.gates, args.reason, now)
        save(pkg, journal)
        print("reopened: %s; next: %s" % (", ".join(reopened) or "nothing new", next_gate(journal)[0]))
        return 0
    if args.cmd == "shortlist":
        problems, names = record_shortlist(pkg, journal, now)
        if problems:
            for problem in problems:
                print("FAIL " + problem)
            print("FAIL: shortlist not recorded (%d problem(s))" % len(problems))
            return 1
        save(pkg, journal)
        print("PASS: shortlist recorded: %s. The rerun ends here: tell the Founder to try them in App Store Connect "
              "in that order and to run `bin/gr0wthpilot %s --accept-name \"<name>\"` with the first one it "
              "accepts." % (", ".join(names), journal.get("product")))
        return 0
    if args.cmd == "workflow":
        journal.setdefault("workflows", []).append({"phase": args.phase, "name": args.name, "run_id": args.run_id,
                                                    "agents": args.agents, "at": now})
        save(pkg, journal)
        print("recorded workflow %s" % args.name)
        return 0
    if args.cmd == "note":
        add_note(journal, args.text, now)
        save(pkg, journal)
        print("noted")
        return 0
    if args.cmd == "complete":
        nxt = next_gate(journal)
        if nxt:
            print("FAIL the run is not done; the next gate is %s" % nxt[0])
            return 1
        problems = stale_critics(pkg, PHASES)
        if problems:
            for problem in problems:
                print("FAIL " + problem)
            print("FAIL: a critic must run again before the run is complete")
            return 1
        journal["status"] = "complete"
        journal["completed_at"] = now
        save(pkg, journal)
        print("complete")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
