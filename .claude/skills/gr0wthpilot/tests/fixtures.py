"""Build a small Candidate Package that passes every Gr0wthPilot check.

Each test copies it, breaks one thing, and expects the check that guards that
thing to fail. Images and video are made with ffmpeg, which every check that
reads media needs anyway.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
BIN = Path(__file__).resolve().parent.parent / "bin"
sys.path.insert(0, str(SCRIPTS))

PRODUCT = "Testprod"
FETCHED = "2026-10-24T10:00:00Z"
URLS = {
    "pain": ["https://forum.example.org/t/%d" % i for i in range(1, 16)],
    "comp_a": "https://apps.apple.com/us/app/alpha-camera/id1111111111",
    "comp_b": "https://apps.apple.com/us/app/beta-camera/id2222222222",
    "comp_c": "https://apps.apple.com/us/app/gamma-camera/id3333333333",
    "stat": "https://research.example.org/report",
    "size_ig": "https://help.example.org/instagram-sizes",
    "size_x": "https://help.example.org/x-sizes",
    "size_tt": "https://help.example.org/tiktok-sizes",
}


def all_urls():
    out = list(URLS["pain"])
    out += [v for k, v in URLS.items() if k != "pain"]
    return out


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + list(args), check=True)


def png(path, size, blank=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    source = "color=c=white:s=%s" % size if blank else "testsrc2=s=%s" % size
    ffmpeg("-f", "lavfi", "-i", source, "-frames:v", "1", str(path))


def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


ANGLE_HEADER = ("| ID | Angle | Sourced pain | Hook | Format | Platform | Pre-registered success signal | "
                "Kill criterion |\n|---|---|---|---|---|---|---|---|\n")


def angles_md():
    rows = []
    for i in range(1, 16):
        platform = "TikTok" if i % 2 else "YouTube Shorts"
        rows.append('| P%02d | Angle %d | Waiting for film to develop is the point, per %s | "Hook number %d '
                    'for the camera" | 20s screen record of the app | %s | watched-full rank in the top half | '
                    'retire if bottom third after two reads |' % (i, i, URLS["pain"][i - 1], i, platform))
    return "# Angle bank\n\n" + ANGLE_HEADER + "\n".join(rows) + "\n"


def pairs_md():
    return ("# A/B pairs\n\n"
            "## AB-1: first pair (angle P01, TikTok, same screen record)\n\n"
            '- Leg A hook: "Hook number 1 for the camera"\n'
            '- Leg B hook: "Shoot now, see it later"\n\n'
            "## AB-2: second pair (angle P02, YouTube Shorts, same screen record)\n\n"
            '- Leg A hook: "Hook number 2 for the camera"\n'
            '- Leg B hook: "A roll of film on your phone"\n')


def cadence_md():
    rows = []
    plan = {1: "P01 / AB-1 leg A", 2: "P02 / AB-2 leg A", 8: "P01 / AB-1 leg B", 9: "P02 / AB-2 leg B"}
    for day in range(1, 15):
        if day == 14:
            angle = "Flex: double down on the leader, else P05"
        else:
            angle = plan.get(day, "P%02d" % (day if day < 13 else 3))
        platform = "TikTok" if day % 2 else "YouTube Shorts"
        if day in (1, 8):
            platform = "TikTok"
        if day in (2, 9):
            platform = "YouTube Shorts"
        rows.append("| %d | Asset %d | %s | %s | note |" % (day, day, angle, platform))
    return ("# 14-day cadence\n\n| Day | Asset | Angle / pair leg | Primary platform | Notes |\n"
            "|---|---|---|---|---|\n" + "\n".join(rows) + "\n\n## Asset checklist\n\n"
            "- Every screen recording is made on a real device, in real time, with cuts only where marked.\n"
            "- A killed Angle is marked in creative-log.json with status killed.\n")


def creative_log():
    records = []
    for i in range(1, 16):
        records.append({"angle_id": "P%02d-angle" % i, "hook": "Hook number %d for the camera" % i,
                        "platform": "tiktok" if i % 2 else "youtube_shorts", "pain_source_url": URLS["pain"][i - 1],
                        "status": "draft", "results": None})
    return json.dumps({"comment": "one record per Angle", "angles": records}, indent=2) + "\n"


BRAND_RULES = {
    "comment": "test rules",
    "hook_max_words": 12,
    "hook_must_not_be_question": True,
    "banned_words_in_hook": ["revolutionary", "vintage filter"],
    "banned_social_proof_in_hook": ["stars", "reviews"],
    "banned_characters_anywhere": ["\u2014"],
    "no_emoji_in_hook": True,
    "no_all_caps_words_in_hook": True,
    "all_caps_allowlist": ["ISO"],
    "pain_source_url_must_start_with": "https://",
    "stock_phrases": ["say goodbye to", "game-changer"],
    "invented_proof_terms": ["users", "reviews", "photographers"],
    "invented_proof_quantities": ["thousands of"],
    "fake_scarcity": ["only today", "last chance"],
    "loss_framing": ["don't miss"],
    "frozen_hooks_exempt_from": ["hook_max_words", "banned_words_in_hook"],
    "caption_call_to_action": {"line": "Join the waitlist: {link}",
                               "links": {"TikTok": "testprod.example/tiktok", "YouTube Shorts": "testprod.example/youtube"}},
}


def recap_html():
    return """<!doctype html><html><head><meta charset="utf-8"><title>Testprod Candidate Package</title></head><body>
<section id="naming"><h2>Name</h2><p>Testprod is confirmed. Trademark and App Store name clearance are UNVERIFIED and are the Founder's next action.</p></section>
<section id="thesis"><h2>Thesis</h2><p>See <a href="07-thesis/investment-thesis.md">the thesis</a>.</p></section>
<section id="objection"><h2>Strongest surviving objection</h2><p>See <a href="08-redteam/dossier.md#surviving">the dossier</a>.</p></section>
<section id="deliverables"><h2>Deliverables</h2><ul>
<li><a href="01-research/">Research</a></li><li><a href="02-brand/brand-guidelines.md">Brand</a></li>
<li><a href="03-site/index.html">Site A</a> <a href="03-site/index-b.html">Site B</a></li>
<li><a href="04-video/walkthrough.mp4">Walkthrough</a></li><li><a href="05-social-pmf/angles.md">Test Kit</a></li>
<li><a href="06-channels/channel-plan.md">Channels</a></li><li><a href="07-thesis/investment-thesis.md">Thesis</a></li>
<li><a href="08-redteam/dossier.md">Red team</a></li><li><a href="09-extras/marketing-agent/">Marketing agent</a></li>
<li><a href="09-extras/darkroom-letter.md">Invented deliverable</a></li><li><a href="10-launch-set/manifest.json">Launch Set</a></li>
<li><a href="README.md">README</a></li><li><a href="decisions-log.md">Decisions</a></li><li><a href="sources.md">Sources</a></li>
<li><a href="self-grade.md">Self-grade</a></li><li><a href="launch-checklist.md">Launch checklist</a></li>
<li><a href="run-audit.md">Run audit</a></li><li><a href="handoff/registry-entry.json">Registry entry</a></li>
<li><a href="run-journal.json">Run journal</a></li>
</ul></section>
<section id="handoff"><h2>Handoff</h2><p>When you approve it, say: <code>Testprod - hand to gr0wthlab</code></p></section>
</body></html>
"""


def site_html(variant):
    return """<!doctype html><html><head><meta charset="utf-8"><title>Testprod</title>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Testprod"}</script>
</head><body><header><h1>Shoot a roll. See it tomorrow. (%s)</h1></header>
<p>A camera app that develops your photos overnight, like film did.</p>
<p>Most people never print a photo again, per <a href="%s">this report</a>.</p>
<form><label>Email <input type="email"></label><button type="button">Join the waitlist</button></form>
</body></html>
""" % (variant, URLS["stat"])


def build(root=None, video=True):
    root = Path(root) if root else Path(tempfile.mkdtemp(prefix="gp-pkg-")) / "gtm"
    write(root, "run-journal.json", json.dumps({
        "gr0wthpilot_journal": 1, "product": PRODUCT, "run_id": "testprod-1", "status": "in-progress",
        "package": "projects/Testprod/gtm", "kind": "first-package", "repo": None, "started_at": FETCHED,
        "sessions": [], "gates": [], "phase_skills_read": [], "workflows": [], "decisions": 0, "notes": []}))
    write(root, "sources.md", "# Sources\n\n## research\n\n" + "".join(
        "- %s - fetched %s - supports a claim\n" % (u, FETCHED) for u in all_urls()))
    evidence = root / "run-evidence"
    evidence.mkdir(parents=True, exist_ok=True)
    (evidence / "fetch-log.jsonl").write_text("".join(
        json.dumps({"at": FETCHED, "url": u, "code": 200, "bytes": 100}) + "\n" for u in all_urls()))
    write(root, "decisions-log.md", "# Decisions log\n\n- D-001 [DECIDED BY AGENT]: price at $4.99 [PROPOSAL], "
                                    "rejected $9.99 because the category anchors lower.\n")
    write(root, "01-research/product-facts-brief.md", "# Product facts\n\n" + "".join(
        "- Fact %d (repo: App/Source%d.swift)\n" % (i, i) for i in range(1, 7)))
    write(root, "01-research/pain-points.md", "# Pain points\n\n" + "".join(
        "> Waiting is the point of film (%s)\n\n" % u for u in URLS["pain"]))
    for slug, name, key in (("alpha", "Alpha Camera", "comp_a"), ("beta", "Beta Camera", "comp_b"),
                            ("gamma", "Gamma Camera", "comp_c")):
        write(root, "01-research/competitor-%s.md" % slug,
              "# Competitor Teardown: %s\n\nListing: %s\n\nIt charges $2.99 a month (%s).\n" % (name, URLS[key], URLS[key]))
    t = "02-brand/tournament/"
    for i in range(1, 5):
        write(root, t + "pitch-%d.md" % i, "# Pitch %d\n\nA positioning.\n" % i)
    for j in ("differentiation", "conversion", "defensibility"):
        write(root, t + "rubric-%s.md" % j, "# Rubric\n\n| Criterion | Weight |\n|---|---|\n| Fit | 50%% |\n")
        write(root, t + "judge-%s.md" % j, "# Judge %s\n\nScores below.\n" % j)
    write(root, t + "scorecard.md", "# Scorecard\n\n| Pitch | Score |\n|---|---|\n| 1 | 8.1 |\n| 2 | 7.4 |\n\n"
                                    "Winning margin: 0.7.\n")
    write(root, "02-brand/positioning.md", "# Positioning\n\nFor people who miss film.\n")
    write(root, "02-brand/naming-decision.md", "# Naming\n\nTestprod. Clearance UNVERIFIED: the Founder's next action.\n")
    write(root, "02-brand/brand-guidelines.md", "# Brand guidelines\n\nPalette #111111.\n")
    write(root, "02-brand/gate-test-report.md", "# Brand gate\n\nRound 1.\n\nVerdict: PASS\n")
    write(root, "02-brand/gate-test-asset.html", "<!doctype html><p>asset</p>\n")
    write(root, "06-channels/channel-plan.md", "# Channel plan\n\nApp Store search first.\n")
    write(root, "06-channels/event-metric-schema.md", "# Events\n\ninstall, first photo.\n")
    write(root, "07-thesis/investment-thesis.md", "# Thesis\n\nKill if the first session takes over 5 minutes [TARGET].\n")
    write(root, "08-redteam/claims-ledger.md",
          "# Claims ledger\n\n| ID | Claim | Source | Skeptic verdict | Shipped as |\n|---|---|---|---|---|\n"
          "| C1 | Most people never print a photo again | %s | WEAKENED | softened on the site |\n"
          "| C2 | Every competitor charges over ten dollars a month for film looks | %s | REFUTED | cut |\n"
          % (URLS["stat"], URLS["comp_a"]))
    write(root, "03-site/index.html", site_html("A"))
    write(root, "03-site/index-b.html", site_html("B"))
    notes = []
    for stem in ("index", "index-b"):
        for w, h in ((390, 844), (1440, 900)):
            name = "%s-%dx%d.png" % (stem, w, h)
            png(root / "03-site" / "screenshots" / name, "%dx%d" % (w, h))
            write(root, "03-site/screenshots/%s-%d.json" % (stem, w),
                  json.dumps({"scrollWidth": w, "innerWidth": w, "innerHeight": h, "overflows": False,
                              "viewport": "%dx%d" % (w, h)}))
            notes.append("- %s: hero, waitlist card, and footer all visible; no clipped text or overflow at this width." % name)
    write(root, "03-site/screenshot-gate.md", "# Screenshot gate\n\n" + "\n".join(notes) + "\n")
    kit = "05-social-pmf/"
    write(root, kit + "angles.md", angles_md())
    write(root, kit + "ab-pairs.md", pairs_md())
    write(root, kit + "cadence-14-day.md", cadence_md())
    write(root, kit + "platform-assignment.md", "# Platforms\n\n## The two test platforms\n\n### 1. TikTok (primary)\n\n"
                                                "Fastest signal.\n\n### 2. YouTube Shorts (secondary)\n\nMirror.\n")
    write(root, kit + "read-the-results.md", "# Reading results\n\n- Any post under 200 impressions is unread, not "
                                             "failed; the floor counts each platform's views [ASSUMPTION: a floor "
                                             "below which a read is noise].\n")
    write(root, kit + "creative-log.json", creative_log())
    write(root, kit + "week-1-drafts.md", "# Week 1\n\n## Day 1\n\n**Caption:** Shoot now. See it tomorrow.\n\n"
                                          "**Alt text:** A phone screen showing a film counter.\n")
    write(root, "09-extras/marketing-agent/brand-rules.json", json.dumps(BRAND_RULES, indent=2) + "\n")
    write(root, "09-extras/marketing-agent/BUILD-SPEC.md", "# Build spec\n\nHow drafts are made.\n")
    write(root, "09-extras/darkroom-letter.md", "# A letter from the darkroom\n\nShoot now. See it tomorrow.\n")
    write(root, "08-redteam/pre-publication-checklist.md", "# Pre-publication checklist\n\n"
                                                           "- [ ] **Trademark search for Testprod** (blocking: naming)\n")
    for persona in ("investor", "competitor", "user", "lawyer"):
        write(root, "08-redteam/redteam-%s.md" % persona, "# %s\n\nFindings.\n" % persona)
    write(root, "08-redteam/dossier.md", "# Dossier\n\n## Material changes\n\n- Site hero: before 'the only film "
                                         "app', after 'a camera that waits'.\n\n## Surviving objections\n\n"
                                         "<a id=\"surviving\"></a>- Copyable.\n")
    for phase in "12345":
        write(root, "08-redteam/critic-phase-%s.md" % phase, "# Critic phase %s\n\nRound 1.\n\nVerdict: PASS\n" % phase)
    assets = []
    for platform, size, src in (("instagram", "320x320", "size_ig"), ("x", "400x400", "size_x"),
                                ("tiktok", "200x200", "size_tt")):
        png(root / "10-launch-set" / platform / "profile.png", size)
        write(root, "10-launch-set/%s/week-1.md" % platform, "# %s week 1\n\n**Caption:** Shoot now. See it tomorrow.\n"
              % platform)
        assets += [{"platform": platform, "kind": "profile-image", "path": "%s/profile.png" % platform, "size": size,
                    "size_source": URLS[src]},
                   {"platform": platform, "kind": "first-week-posts", "path": "%s/week-1.md" % platform,
                    "size_source": URLS[src]}]
    write(root, "10-launch-set/manifest.json", json.dumps({"assets": assets}, indent=2))
    if video:
        vdir = root / "04-video"
        vdir.mkdir(parents=True, exist_ok=True)
        ffmpeg("-f", "lavfi", "-i", "testsrc2=s=270x480:d=4", "-f", "lavfi", "-i", "sine=frequency=440:duration=4",
               "-shortest", "-pix_fmt", "yuv420p", str(vdir / "walkthrough.mp4"))
        write(root, "04-video/script.md", "# Script\n\nBeat 1.\n")
        write(root, "04-video/gate.json", json.dumps({"video": "walkthrough.mp4", "size": "270x480",
                                                      "min_seconds": 2, "max_seconds": 10}))
        import contextlib
        import io
        import check_video
        with contextlib.redirect_stdout(io.StringIO()):
            check_video.prepare(vdir / "walkthrough.mp4")
        frames = "\n".join("- frame-%03d.png: the test pattern with its moving gradient, matching beat %d of the "
                           "script." % (p, i + 1) for i, p in enumerate((0, 25, 50, 75, 100)))
        write(root, "04-video/gate-report.md", "# Video gate\n\nAudio: a 440 Hz test tone.\n\n" + frames + "\n")
    write(root, "README.md", "# Testprod package\n\n```\npython3 -m http.server 8080\n```\n")
    write(root, "self-grade.md", "# Self-grade\n\nAll gates passed.\n")
    write(root, "launch-checklist.md", "# Launch checklist\n\n- [ ] **Waitlist live**\n")
    write(root, "handoff/README.md", "# Handoff\n\nSay `Testprod - hand to gr0wthlab`.\n")
    write(root, "run-audit.md", "# Run audit\n")
    write(root, "recap.html", recap_html())
    import check_layout
    registry = SCRIPTS.parent / "references" / "registry-template.json"
    result = check_layout.check(root, PRODUCT, registry=str(registry), write_entry=True)
    assert not result["problems"], result["problems"]
    return root


_CACHE = {}


def package(folder="gtm", kind=None):
    """A fresh copy of the passing package (built once per test run), in a
    package folder of that name, its run journal marked with that kind."""
    if "base" not in _CACHE:
        _CACHE["base"] = build()
    dest = Path(tempfile.mkdtemp(prefix="gp-case-")) / folder
    shutil.copytree(str(_CACHE["base"]), str(dest))
    if kind:
        journal = json.loads((dest / "run-journal.json").read_text(encoding="utf-8"))
        journal["kind"] = kind
        (dest / "run-journal.json").write_text(json.dumps(journal), encoding="utf-8")
    return dest
