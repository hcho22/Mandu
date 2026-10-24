#!/usr/bin/env python3
"""Layout check: does a Candidate Package hold what gr0wthlab reads, in a form
gr0wthlab can parse?

gr0wthlab (the Marketing Engineer) reads a Product's package through its
registry, config/products.json. This check takes RepToday's entry there as the
template (the live registry when one is readable, else the snapshot in
references/registry-template.json), points it at the package's own folder
(`projects/<Product>/gtm/` or a dated `gtm-candidate-<date>/`), maps every
path it names into the package, and verifies:

1. every file and folder the entry names exists (a folder holds at least one
   visible file; a `files_starting_with` source has at least one match);
2. each file gr0wthlab parses with code follows the rules its parser enforces
   (src/gr0wthlab/kit.py, results.py, weekly_changes.py, lint.py at the
   template's commit), and the Test Kit meets the run's own floor: at least
   15 distinct Angles, hook-only A/B pairs, a 14-day calendar, and the two
   platforms gr0wthlab runs, TikTok and YouTube Shorts;
3. with --write-entry, writes `handoff/registry-entry.json`: RepToday's entry
   with the Product's name and the package's folder, ready for the reviewed
   gr0wthlab change at Handoff.

Usage: check_layout.py PACKAGE --product NAME [--registry products.json] [--write-entry] [--json]
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

TEMPLATE = gc.REFERENCES / "registry-template.json"
PLATFORMS = ("TikTok", "YouTube Shorts")
PRIMARY_CELLS = {"tiktok", "youtube shorts", "youtube"}
MIN_ANGLES = 15
CALENDAR_DAYS = 14
FLOOR_RE = re.compile(r"Any post under (\d[\d,]*) impressions is unread")
PAIR_HEAD_RE = re.compile(r"^## (AB-\d+)\b.*$")
LEG_RE = re.compile(r"^- Leg ([AB]) hook: (.*)$")
QUOTED_RE = re.compile(r"\"([^\"]+)\"")
PAIR_LEG_RE = re.compile(r"\b(AB-\d+) leg ([AB])\b")
# The recording types gr0wthlab's filming plan reads from a Format (shots.py CAPTURES).
FORMAT_KINDS = re.compile(r"\bfounder[- ]on[- ]camera\b|\bscreen[- ]record(?:ing)?s?\b|\btime-?lapse\b|"
                          r"\bslow[- ]motion\b|\bhigh-frame-rate\b|\bdemo\b|\bpan\b|\bvideo\b", re.I)
CHECK_ITEM_RE = re.compile(r"^- \[([ xX])\] (.*)$")
CREATIVE_KEYS = {"angle_id", "hook", "platform", "hypothesis", "format", "preregistered_success_signal",
                 "kill_criterion", "pain_rank", "pain_state", "verbatim_quote", "pain_source_url",
                 "ab_pair", "results", "status"}


def default_registries():
    paths = []
    env = os.environ.get("GR0WTHLAB_DIR")
    if env:
        paths.append(Path(env) / "config" / "products.json")
    paths.append(Path.home() / "gr0wthlab" / "config" / "products.json")
    paths.append(Path.home() / "Developer" / "FM_Private" / "firstmate-private" / "projects" /
                 "gr0wthlab" / "config" / "products.json")
    return paths


def load_template(registry=None):
    """Return (entry with {product} placeholders, where it came from)."""
    for path in ([Path(registry)] if registry else default_registries()):
        try:
            data = gc.read_json(path)
        except (OSError, ValueError):
            continue
        for product in data.get("products", []):
            if product.get("name") == "RepToday" and product.get("go_to_market_package"):
                entry = product["go_to_market_package"]
                text = json.dumps(entry)
                text = re.sub(r"projects/RepToday/(?!gtm/)[^\"]*launch-checklist[^\"]*\.md",
                              "projects/{product}/gtm/launch-checklist.md", text)
                text = text.replace("projects/RepToday/", "projects/{product}/")
                return json.loads(text), str(path)
    return gc.read_json(TEMPLATE)["go_to_market_package"], str(TEMPLATE)


def package_prefix(pkg, product):
    """The registry path of the package: `projects/<Product>/<its folder>/`."""
    return "projects/%s/%s/" % (product, Path(pkg).resolve().name)


def fill(entry, product, prefix):
    text = json.dumps(entry).replace("projects/{product}/gtm/", prefix)
    return json.loads(text.replace("{product}", product))


def to_package(pkg, prefix, path):
    if not path.startswith(prefix):
        return None
    return pkg / path[len(prefix):]


def check_paths(pkg, prefix, entry, problems):
    needed = []
    for source in entry.get("sources", []):
        needed.append((source["path"], source.get("files_starting_with")))
    needed.append((entry.get("launch_checklist"), None))
    for block in ("post_drafts", "weekly_read", "listening", "outreach"):
        for key, value in (entry.get(block) or {}).items():
            if key != "note" and isinstance(value, str) and value.startswith("projects/"):
                needed.append((value, None))
    seen = set()
    for path, starts in needed:
        if not path or (path, starts) in seen:
            continue
        seen.add((path, starts))
        target = to_package(pkg, prefix, path)
        if target is None:
            problems.append("registry path %s lies outside %s" % (path, prefix))
            continue
        relative = gc.rel(pkg, target)
        if path.endswith("/"):
            files = [p for p in target.iterdir() if p.is_file() and not p.name.startswith(".")] \
                if target.is_dir() else []
            if starts:
                files = [p for p in files if p.name.startswith(starts)]
            if not files:
                problems.append("%s/ holds no %sfiles gr0wthlab can read" % (
                    relative, "'%s*' " % starts if starts else ""))
        elif not target.is_file():
            problems.append("%s is missing (gr0wthlab reads it)" % relative)
    return len(seen)


def read(pkg, relative):
    path = pkg / relative
    return path.read_text(encoding="utf-8") if path.is_file() else None


def check_calendar(text, problems):
    table = gc.find_table(text, ("Day", "Asset", "Angle", "platform"))
    if not table:
        problems.append("cadence-14-day.md: no table with columns Day, Asset, Angle, platform")
        return {}
    header, rows, idx = table
    days, flex = {}, []
    for row in rows:
        if len(row) != len(header):
            problems.append("cadence-14-day.md: a row has %d cells, the header %d" % (len(row), len(header)))
            continue
        day = row[idx["Day"]]
        if not re.fullmatch(r"[0-9]+", day):
            problems.append("cadence-14-day.md: Day %r is not a number" % day)
            continue
        if day in days:
            problems.append("cadence-14-day.md: day %s repeats" % day)
        angle_cell = row[idx["Angle"]]
        platform = " ".join(row[idx["platform"]].lower().split())
        if platform not in PRIMARY_CELLS:
            problems.append("cadence-14-day.md: day %s primary platform %r is not TikTok or YouTube Shorts"
                            % (day, row[idx["platform"]]))
        m = re.match(r"(P\d+)\b", angle_cell)
        leg = PAIR_LEG_RE.search(angle_cell)
        if not m:
            flex.append(day)
            named = re.findall(r"\bP\d+\b", angle_cell)
            if len(named) != 1:
                problems.append("cadence-14-day.md: flex day %s must name exactly one fallback Angle (P..)" % day)
        days[day] = {"angle": m.group(1) if m else None, "leg": leg.groups() if leg else None}
    for d in range(1, CALENDAR_DAYS):
        if str(d) not in days:
            problems.append("cadence-14-day.md: day %d is missing (days 1-13 must exist)" % d)
    if len(flex) > 1:
        problems.append("cadence-14-day.md: %d flex days (%s); exactly one row may lack a fixed Angle"
                        % (len(flex), ", ".join(flex)))
    return days


def check_angles(text, rules, problems, warnings):
    columns = ("ID", "Angle", "pain", "Hook", "Format", "Platform", "signal", "Kill")
    table = gc.find_table(text, columns)
    if not table:
        problems.append("angles.md: no table with columns %s" % ", ".join(columns))
        return {}
    header, rows, idx = table
    if len(set(idx.values())) != len(idx):
        problems.append("angles.md: two wanted columns match the same header; make headers unambiguous")
    prefix = (rules or {}).get("pain_source_url_must_start_with") or "https://"
    angles = {}
    for row in rows:
        aid = row[0] if row else ""
        if len(row) != len(header):
            if row and re.fullmatch(r"P\d+", row[idx["ID"]] if len(row) > idx["ID"] else ""):
                problems.append("angles.md: %s has %d cells, the header %d" % (row[idx["ID"]], len(row), len(header)))
            continue
        aid = row[idx["ID"]]
        if not re.fullmatch(r"P\d+", aid):
            continue
        if aid in angles:
            problems.append("angles.md: %s repeats" % aid)
        hook = row[idx["Hook"]].strip()
        if not re.fullmatch(r"\"([^\"]+)\"", hook):
            problems.append("angles.md: %s Hook must be one straight-quoted string, got %r" % (aid, hook[:60]))
        urls = re.findall(r"https?://[^\s)\]]+", row[idx["pain"]])
        if not any(u.startswith(prefix) for u in urls):
            problems.append("angles.md: %s pain cell has no source URL starting %s" % (aid, prefix))
        platform = row[idx["Platform"]].strip()
        if platform not in ("TikTok", "YouTube Shorts", "YouTube"):
            problems.append("angles.md: %s Platform %r is not TikTok or YouTube Shorts" % (aid, platform))
        if not FORMAT_KINDS.search(row[idx["Format"]]):
            warnings.append("angles.md: %s Format names no recording type gr0wthlab's filming plan knows "
                            "(founder on camera, screen record, time-lapse, slow motion, demo, pan, video); "
                            "its days stay unplanned" % aid)
        for column in ("signal", "Kill"):
            if len(row[idx[column]].strip()) < 8:
                problems.append("angles.md: %s %s cell is empty" % (aid, column))
        angles[aid] = {"hook": hook.strip('"'), "platform": platform}
    if not angles:
        problems.append("angles.md: no Angle rows (IDs like P01)")
    elif len(angles) < MIN_ANGLES:
        problems.append("angles.md: %d Angles; a Test Kit needs at least %d distinct Angles" % (len(angles), MIN_ANGLES))
    return angles


def check_pairs(text, angles, problems):
    pairs, current = {}, None
    for line in text.splitlines():
        head = PAIR_HEAD_RE.match(line)
        if head:
            pid = head.group(1)
            m_angle = re.search(r"\bangle (P\d+)", line)
            m_paren = re.search(r"\(([^)]*)\)\s*$", line)
            parts = [p.strip() for p in m_paren.group(1).split(",")] if m_paren else []
            if not m_angle or len(parts) < 2:
                problems.append("ab-pairs.md: heading %r must name 'angle P..' and end with "
                                "'(angle P.., Platform, ...)'" % line.strip())
            elif parts[1] not in PLATFORMS:
                problems.append("ab-pairs.md: %s platform %r is not TikTok or YouTube Shorts" % (pid, parts[1]))
            current = pairs.setdefault(pid, {"angle": m_angle.group(1) if m_angle else None, "legs": {}})
            continue
        if line.startswith("## "):
            current = None
            continue
        leg = LEG_RE.match(line)
        if leg and current is not None:
            q = QUOTED_RE.search(leg.group(2))
            if not q:
                problems.append("ab-pairs.md: leg %s has no quoted Hook" % leg.group(1))
            current["legs"][leg.group(1)] = q.group(1) if q else None
    if not pairs:
        problems.append("ab-pairs.md: no pair sections (## AB-1: ... (angle P.., TikTok, ...))")
    for pid, pair in pairs.items():
        if set(pair["legs"]) != {"A", "B"}:
            problems.append("ab-pairs.md: %s needs both '- Leg A hook:' and '- Leg B hook:' lines" % pid)
        if pair["angle"] and angles and pair["angle"] not in angles:
            problems.append("ab-pairs.md: %s names %s, which angles.md does not hold" % (pid, pair["angle"]))
        if pair["legs"].get("A") and pair["legs"].get("A") == pair["legs"].get("B"):
            problems.append("ab-pairs.md: %s legs have the same Hook; only the Hook may differ, and it must" % pid)
    return pairs


def check_calendar_links(days, angles, pairs, problems):
    for day, info in days.items():
        if info["angle"] and angles and info["angle"] not in angles:
            problems.append("cadence-14-day.md: day %s names %s, which angles.md does not hold" % (day, info["angle"]))
        if info["leg"]:
            pid, _ = info["leg"]
            pair = pairs.get(pid)
            if not pair:
                problems.append("cadence-14-day.md: day %s names %s, which ab-pairs.md does not hold" % (day, pid))
            elif info["angle"] and pair["angle"] != info["angle"]:
                problems.append("cadence-14-day.md: day %s runs %s on %s, but the pair is for %s"
                                % (day, pid, info["angle"], pair["angle"]))


def check_platforms(text, problems):
    found, inside = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = "test platforms" in line.lower()
            continue
        if inside:
            m = re.match(r"### \d+\. (.+?)(?: \([^)]*\))?\s*$", line)
            if m:
                found.append(m.group(1))
    if not found:
        problems.append("platform-assignment.md: no '## ... test platforms' section with '### 1. TikTok (primary)' items")
    for name in found:
        if name not in PLATFORMS:
            problems.append("platform-assignment.md: %r is not a platform gr0wthlab runs (%s)" % (name, ", ".join(PLATFORMS)))
    return found


def check_checklist(text, problems, warnings):
    items = []
    for line in text.splitlines():
        m = CHECK_ITEM_RE.match(line)
        if m:
            items.append((m.group(1) != " ", m.group(2)))
    if not items:
        problems.append("pre-publication-checklist.md: no '- [ ] **Title** ...' items")
    for done, body in items:
        if not re.search(r"\*\*[^*]+\*\*", body):
            warnings.append("pre-publication-checklist.md: item without a **bold title** (gr0wthlab titles "
                            "an item by it): %s" % body[:60])
        scope = re.findall(r"\(blocking: ([^)]*)\)", body)
        if not done and scope:
            tokens = [t.strip().lower() for t in re.split(r"[,;]", scope[-1])]
            if any(t.startswith(("everything public", "social")) for t in tokens) and \
                    not re.search(r"the \"[^\"]+\" claim", body):
                warnings.append("pre-publication-checklist.md: open item blocks every gr0wthlab post Draft "
                                "until the Founder closes it: %s" % body[:80])
    return items


def check_competitors(pkg, problems):
    names = []
    folder = pkg / "01-research"
    for path in sorted(folder.glob("competitor*")) if folder.is_dir() else []:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        for i, line in enumerate(lines):
            m = re.match(r"# Competitor Teardown: (.+)$", line)
            if m:
                names.append(m.group(1))
            m = re.match(r"## \d+\. (.+)$", line)
            if m:
                nxt = next((rest for rest in lines[i + 1:] if rest.strip()), "")
                if nxt.startswith("Source:"):
                    names.append(m.group(1))
            if line.startswith("Scope:"):
                m = re.findall(r"\(([^)]*)\)", line)
                if m:
                    names.extend(p.strip() for p in m[-1].split(","))
    names = [re.split(r" \(|: | - | \| |! ", n)[0].strip() for n in names]
    names = [n for n in names if len(n) >= 3]
    if not names:
        problems.append("01-research/competitor*: no competitor names gr0wthlab can read "
                        "('# Competitor Teardown: <name>')")
    return names


def check_read_results(text, problems):
    m = FLOOR_RE.search(text or "")
    if not m:
        problems.append("read-the-results.md: no line 'Any post under N impressions is unread' (gr0wthlab's floor)")
    elif "views" not in text[m.start(): m.start() + 300]:
        problems.append("read-the-results.md: the floor line must say it counts each platform's views")


def check_creative_log(text, angles, problems):
    try:
        data = json.loads(text)
    except ValueError as exc:
        problems.append("creative-log.json is not valid JSON: %s" % exc)
        return
    records = data if isinstance(data, list) else data.get("angles") if isinstance(data, dict) else None
    if not isinstance(records, list):
        problems.append("creative-log.json must be a list or an object with an 'angles' list")
        return
    seen = {}
    platform_names = {}
    lines = text.splitlines()
    for record in records:
        if not isinstance(record, dict) or "angle_id" not in record:
            problems.append("creative-log.json: every record needs an angle_id")
            continue
        angle_id = record["angle_id"]
        extra = set(record) - CREATIVE_KEYS
        if extra:
            problems.append("creative-log.json: %s has keys gr0wthlab does not accept: %s"
                            % (angle_id, ", ".join(sorted(extra))))
        if not isinstance(angle_id, str) or not re.fullmatch(r"P\d+(?:-.*)?", angle_id):
            problems.append("creative-log.json: angle_id %r must be its Angle's ID, alone or followed by a hyphen "
                            "(P01 or P01-waiting), as gr0wthlab finds a record to kill" % (angle_id,))
            continue
        number = angle_id.split("-", 1)[0]
        seen[number] = seen.get(number, 0) + 1
        if number in angles:
            platform_names.setdefault(angles[number]["platform"], set()).add(record.get("platform"))
        if record.get("status") != "draft" or "results" not in record or record["results"] is not None:
            problems.append("creative-log.json: %s must start with status \"draft\" and results null" % angle_id)
        if not own_status_line(lines, angle_id):
            problems.append("creative-log.json: %s needs its angle_id on a line of its own, followed in the same "
                            "record by its status line, which gr0wthlab's kill edits" % angle_id)
    for aid in angles:
        if seen.get(aid, 0) != 1:
            problems.append("creative-log.json: %s needs exactly one record, has %d" % (aid, seen.get(aid, 0)))
    for platform, names in platform_names.items():
        if len(names) > 1:
            problems.append("creative-log.json: Angles on %s use different platform strings: %s"
                            % (platform, ", ".join(sorted(str(n) for n in names))))
    lines = text.rstrip().splitlines()
    if len(lines) < 2 or lines[-1].strip() != "}" or lines[-2].strip() not in ("]", "],"):
        problems.append("creative-log.json must be pretty-printed and end with a ']' line then a '}' line")


def own_status_line(lines, angle_id):
    """Whether a record's angle_id sits on exactly one line of its own and the
    next status line after it comes before any other record's angle_id line,
    as gr0wthlab's kill edit (weekly_changes.py id_lines, compose_kill) needs."""
    named = re.compile(r'\s*"angle_id"\s*:\s*' + re.escape(json.dumps(angle_id)) + r"\s*,?\s*")
    starts = [i for i, line in enumerate(lines) if named.fullmatch(line)]
    if len(starts) != 1:
        return False
    for line in lines[starts[0] + 1:]:
        if re.fullmatch(r'\s*"status"\s*:\s*"[^"\\]*",?\s*', line):
            return True
        if re.match(r'\s*"angle_id"\s*:', line):
            return False
    return False


def check(pkg, product, registry=None, write_entry=False):
    pkg = Path(pkg)
    problems, warnings = [], []
    template, origin = load_template(registry)
    prefix = package_prefix(pkg, product)
    entry = fill(template, product, prefix)
    count = check_paths(pkg, prefix, entry, problems)
    rules = None
    rules_text = read(pkg, brand_lint.RULES_PATH)
    if rules_text is not None:
        try:
            rules = json.loads(rules_text)
            problems += ["brand-rules.json: %s" % p for p in brand_lint.validate_rules(rules)]
        except ValueError as exc:
            problems.append("brand-rules.json is not valid JSON: %s" % exc)
    kit = "05-social-pmf/"
    days = check_calendar(read(pkg, kit + "cadence-14-day.md") or "", problems) \
        if read(pkg, kit + "cadence-14-day.md") is not None else {}
    angles = check_angles(read(pkg, kit + "angles.md") or "", rules, problems, warnings) \
        if read(pkg, kit + "angles.md") is not None else {}
    pairs = check_pairs(read(pkg, kit + "ab-pairs.md") or "", angles, problems) \
        if read(pkg, kit + "ab-pairs.md") is not None else {}
    check_calendar_links(days, angles, pairs, problems)
    if read(pkg, kit + "platform-assignment.md") is not None:
        found = check_platforms(read(pkg, kit + "platform-assignment.md"), problems)
        if rules and isinstance(rules.get("caption_call_to_action"), dict):
            links = rules["caption_call_to_action"].get("links") or {}
            if set(links) != set(found):
                problems.append("brand-rules caption_call_to_action.links keys %s differ from the test platforms %s"
                                % (sorted(links), found))
    if read(pkg, kit + "read-the-results.md") is not None:
        check_read_results(read(pkg, kit + "read-the-results.md"), problems)
    if read(pkg, kit + "creative-log.json") is not None:
        check_creative_log(read(pkg, kit + "creative-log.json"), angles, problems)
    else:
        problems.append("05-social-pmf/creative-log.json is missing (gr0wthlab writes kills into it)")
    checklist = read(pkg, "08-redteam/pre-publication-checklist.md")
    if checklist is not None:
        check_checklist(checklist, problems, warnings)
    competitors = check_competitors(pkg, problems)
    result = {"template": origin, "paths": count, "angles": len(angles), "pairs": len(pairs),
              "days": len(days), "competitors": competitors, "problems": problems, "warnings": warnings}
    if write_entry and not problems:
        out = pkg / "handoff" / "registry-entry.json"
        gc.write_json(out, {
            "comment": "The go_to_market_package entry for %s in gr0wthlab's config/products.json, ready "
                       "for the reviewed gr0wthlab change firstmate makes at Handoff. It is RepToday's entry "
                       "with the name changed and every path pointing into %s; only launch_checklist differs, "
                       "pointing inside the package. "
                       "The rest of the Product's registry entry (repository, filming, waitlist, "
                       "beta_recruiting) is product-specific and is set by that change; see handoff/README.md."
                       % (product, prefix),
            "template": origin,
            "go_to_market_package": entry,
        })
        result["entry"] = str(out)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Layout check against gr0wthlab's needed files")
    parser.add_argument("package")
    parser.add_argument("--product", required=True)
    parser.add_argument("--registry")
    parser.add_argument("--write-entry", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = check(args.package, args.product, args.registry, args.write_entry)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for problem in result["problems"]:
            print("FAIL " + problem)
        for warning in result["warnings"]:
            print("WARN " + warning)
        print("%s: %d registry paths, %d Angles, %d pairs, %d calendar days, %d competitors (template %s)" % (
            "PASS" if not result["problems"] else "FAIL", result["paths"], result["angles"],
            result["pairs"], result["days"], len(result["competitors"]), result["template"]))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
