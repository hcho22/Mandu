#!/usr/bin/env python3
"""Video gate for a Candidate Package's walkthrough video (phase 3).

"You watched it" is not a gate. This is:

prepare VIDEO
  Runs ffprobe and writes `ffprobe-report.txt` and `ffprobe.json` beside the
  video, extracts one frame at 0, 25, 50, 75, and 100% of its length into
  `frames/frame-000.png` .. `frame-100.png`, and builds `frame-strip.png`.

verify VIDEO --size WxH --min-seconds N --max-seconds N
  Passes only when ffprobe shows the expected resolution, a duration inside
  the range, and an audio stream; the five frames and the strip exist and are
  not blank; `gate-report.md` beside the video holds a viewing note for each
  frame (a line naming the frame file, then what the agent saw after viewing
  it) and states what the audio is; and `script.md` exists.

Usage: check_video.py prepare VIDEO
       check_video.py verify VIDEO --size 1080x1920 --min-seconds 20 --max-seconds 90 [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_screenshots as cs  # noqa: E402

POINTS = (0, 25, 50, 75, 100)
NOTE_MIN_CHARS = 40


def probe(video):
    proc = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format",
                           "-show_streams", str(video)], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          universal_newlines=True)
    if proc.returncode != 0:
        raise ValueError("ffprobe could not read %s: %s" % (video, proc.stderr.strip()[-300:]))
    return json.loads(proc.stdout)


def facts(data):
    video = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), None)
    audio = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), None)
    duration = float(data.get("format", {}).get("duration") or (video or {}).get("duration") or 0)
    return {
        "duration": round(duration, 3),
        "width": (video or {}).get("width"),
        "height": (video or {}).get("height"),
        "video_codec": (video or {}).get("codec_name"),
        "audio_codec": (audio or {}).get("codec_name"),
        "audio_channels": (audio or {}).get("channels"),
        "has_audio": audio is not None,
    }


def frame_name(point):
    return "frame-%03d.png" % point


def prepare(video):
    video = Path(video)
    data = probe(video)
    info = facts(data)
    folder = video.parent
    (folder / "ffprobe.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    lines = ["ffprobe report for %s" % video.name, ""] + ["%s: %s" % (k, v) for k, v in info.items()]
    (folder / "ffprobe-report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    frames = folder / "frames"
    frames.mkdir(exist_ok=True)
    outputs = []
    for point in POINTS:
        at = max(0.0, min(info["duration"] * point / 100.0, info["duration"] - 0.1))
        out = frames / frame_name(point)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "%.3f" % at, "-i", str(video), "-frames:v", "1",
                        str(out)], check=True)
        outputs.append(out)
    inputs = []
    for out in outputs:
        inputs += ["-i", str(out)]
    graph = "".join("[%d:v]scale=-2:360[f%d];" % (i, i) for i in range(len(outputs)))
    graph += "".join("[f%d]" % i for i in range(len(outputs))) + "hstack=inputs=%d" % len(outputs)
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", graph,
                                                               str(folder / "frame-strip.png")], check=True)
    print(json.dumps(dict(info, frames=[str(o) for o in outputs], strip=str(folder / "frame-strip.png"))))


def verify(video, size, min_seconds, max_seconds):
    video = Path(video)
    problems = []
    if not video.is_file():
        return {"problems": ["%s is missing" % video]}
    try:
        info = facts(probe(video))
    except ValueError as exc:
        return {"problems": [str(exc)]}
    width, height = cs.parse_size(size)
    if (info["width"], info["height"]) != (width, height):
        problems.append("%s is %sx%s, not %dx%d" % (video.name, info["width"], info["height"], width, height))
    if not (min_seconds <= info["duration"] <= max_seconds):
        problems.append("%s runs %.1fs, outside %d-%ds" % (video.name, info["duration"], min_seconds, max_seconds))
    if not info["has_audio"]:
        problems.append("%s has no audio stream" % video.name)
    folder = video.parent
    for name in ("ffprobe-report.txt", "script.md"):
        if not (folder / name).is_file():
            problems.append("%s is missing beside the video" % name)
    gate = folder / "gate-report.md"
    text = gate.read_text(encoding="utf-8") if gate.is_file() else ""
    if not text:
        problems.append("gate-report.md is missing beside the video")
    notes = {}
    for line in text.splitlines():
        m = re.match(r"^\s*[-*]\s+`?(?:frames/)?(frame-\d{3}\.png)`?\s*[:-]\s*(.+)$", line)
        if m:
            notes[m.group(1)] = m.group(2).strip()
    for point in POINTS:
        frame = folder / "frames" / frame_name(point)
        if not frame.is_file():
            problems.append("frames/%s is missing; run check_video.py prepare" % frame.name)
            continue
        if cs.is_blank(frame):
            problems.append("frames/%s is blank" % frame.name)
        if len(notes.get(frame.name, "")) < NOTE_MIN_CHARS:
            problems.append("gate-report.md has no viewing note for %s (view the frame, then say what is on it "
                            "and whether it matches the script)" % frame.name)
    strip = folder / "frame-strip.png"
    if not strip.is_file():
        problems.append("frame-strip.png is missing")
    elif cs.is_blank(strip):
        problems.append("frame-strip.png is blank")
    if text and not re.search(r"^\s*(?:[-*]\s+)?\**audio\**\s*:", text, re.I | re.M):
        problems.append("gate-report.md must say what the audio is ('Audio: ...')")
    return dict(info, problems=problems)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Video gate")
    parser.add_argument("mode", choices=("prepare", "verify"))
    parser.add_argument("video")
    parser.add_argument("--size", default="1080x1920")
    parser.add_argument("--min-seconds", type=int, default=15)
    parser.add_argument("--max-seconds", type=int, default=120)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.mode == "prepare":
        try:
            prepare(args.video)
        except (ValueError, subprocess.CalledProcessError) as exc:
            print("FAIL %s" % exc)
            return 1
        return 0
    result = verify(args.video, args.size, args.min_seconds, args.max_seconds)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for problem in result["problems"]:
            print("FAIL " + problem)
        print("%s: video gate, %d problem(s)" % ("PASS" if not result["problems"] else "FAIL",
                                                len(result["problems"])))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
