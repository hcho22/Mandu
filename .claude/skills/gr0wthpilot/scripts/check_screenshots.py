#!/usr/bin/env python3
"""Screenshot and image gates for a Candidate Package.

site PACKAGE
  Phase 2's gate. Every landing page variant `03-site/index*.html` has two
  screenshots, `03-site/screenshots/<page>-390x844.png` and
  `<page>-1440x900.png` (at 1x, 2x, or 3x), each a real render (not blank),
  a width measurement `03-site/screenshots/<page>-<width>.json` from
  `gp-chrome measure` at that viewport showing no horizontal overflow, and an
  inspection note in `03-site/screenshot-gate.md`: a line naming the file
  followed by what the inspecting agent saw, after it viewed the image. Each
  screenshot and measurement is newer than its page and every local file the
  page loads, so a re-gate never passes on evidence of an older page.

launch-set PACKAGE
  Phase 3's Launch Set gate. `10-launch-set/manifest.json` lists every asset
  with its platform, kind, path, and expected size; every asset that is not
  text (`first-week-posts` or `bio`) is a PNG, JPEG, or WebP image at exactly
  that size and not blank; each `size_source` is the http(s) URL of the
  platform page that gives the size; each of Instagram, X, and TikTok has a
  profile image and first-week posts.

image FILE --size WIDTHxHEIGHT
  One image at one size.

Usage: check_screenshots.py site|launch-set PACKAGE [--json]
       check_screenshots.py image FILE --size WxH
"""

from __future__ import annotations

import argparse
import json
import re
import struct
import subprocess
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402

SITE_SIZES = ((390, 844), (1440, 900))
LAUNCH_PLATFORMS = ("instagram", "x", "tiktok")
TEXT_KINDS = {"first-week-posts", "bio"}
RASTER_SUFFIXES = (".png", ".jpg", ".jpeg", ".webp")
# The tags whose attribute a browser loads with the page (an <a> is followed, not loaded).
LOADED_TAGS = {"link", "script", "img", "source", "video", "audio", "iframe", "embed", "object", "track"}
CSS_URL_RE = re.compile(r"""url\(\s*(?:"([^"]*)"|'([^']*)'|([^)\s]*))\s*\)|@import\s+(?:"([^"]*)"|'([^']*)')""",
                        re.I)
NOTE_MIN_CHARS = 40


def png_size(path):
    with open(str(path), "rb") as handle:
        head = handle.read(33)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        raise ValueError("%s is not a PNG" % path)
    return struct.unpack(">II", head[16:24])


def image_size(path):
    if path.suffix.lower() == ".png":
        return png_size(path)
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height", "-of", "json", str(path)],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    streams = json.loads(out.stdout or "{}").get("streams") or []
    if not streams:
        raise ValueError("%s is not an image ffprobe can read" % path)
    return streams[0]["width"], streams[0]["height"]


def is_blank(path):
    """Decode a 32x32 thumbnail with ffmpeg; blank when it holds almost one color."""
    proc = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-vf", "scale=32:32", "-f", "rawvideo",
                           "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data = proc.stdout
    if proc.returncode != 0 or len(data) < 32 * 32 * 3:
        return True
    pixels = [data[i:i + 3] for i in range(0, len(data), 3)]
    colors = {tuple(c // 16 for c in p) for p in pixels}
    luma = [0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2] for p in pixels]
    mean = sum(luma) / len(luma)
    variance = sum((v - mean) ** 2 for v in luma) / len(luma)
    return len(colors) < 3 or variance < 4.0


def check_image(path, width, height, problems, scales=(1, 2, 3)):
    if not path.is_file():
        problems.append("%s is missing" % path)
        return
    try:
        w, h = image_size(path)
    except ValueError as exc:
        problems.append(str(exc))
        return
    if not any((w, h) == (width * s, height * s) for s in scales):
        problems.append("%s is %dx%d, not %dx%d%s" % (path.name, w, h, width, height,
                                                      " (or 2x/3x)" if len(scales) > 1 else ""))
    if is_blank(path):
        problems.append("%s looks blank (almost one color); re-render it" % path.name)


def inspection_notes(text):
    notes = {}
    for line in text.splitlines():
        m = re.match(r"^\s*[-*]\s+`?([\w./-]+\.png)`?\s*[:-]\s*(.+)$", line)
        if m:
            notes[Path(m.group(1)).name] = m.group(2).strip()
    return notes


def css_urls(css):
    """Each url(...) and @import target in a piece of CSS."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return [next(g for g in m.groups() if g is not None) for m in CSS_URL_RE.finditer(css)]


def local_file(base, value):
    """The local file a URL written in `base` names, if it is one."""
    parsed = urllib.parse.urlsplit(value.strip())
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    target = (base.parent / urllib.parse.unquote(parsed.path)).resolve()
    return target if target.is_file() else None


def page_inputs(page):
    """The page and every local file it loads: by its own tags (every srcset
    candidate too), by url(...) and @import in its style elements and style
    attributes, and by url(...) and @import in each local stylesheet it loads,
    resolved from that stylesheet."""
    text = page.read_text(encoding="utf-8", errors="replace")
    _, links, _ = gc.parse_html(text)
    wanted = [local_file(page, value) for tag, _, value in links if tag in LOADED_TAGS]
    wanted += [local_file(page, value) for css in gc.html_styles(text) for value in css_urls(css)]
    found = [page]
    while wanted:
        target = wanted.pop(0)
        if target is None or target in found:
            continue
        found.append(target)
        if target.suffix.lower() == ".css":
            css = target.read_text(encoding="utf-8", errors="replace")
            wanted += [local_file(target, value) for value in css_urls(css)]
    return found


def stale_evidence(evidence, inputs):
    """A problem for each evidence file older than the newest of its inputs."""
    newest = max(inputs, key=lambda p: p.stat().st_mtime)
    return ["%s is older than %s; make it again from what ships now" % (e.name, newest.name)
            for e in evidence if e.is_file() and e.stat().st_mtime < newest.stat().st_mtime]


def check_site(pkg):
    pkg = Path(pkg)
    problems = []
    site = pkg / "03-site"
    pages = sorted(p for p in site.glob("index*.html")) if site.is_dir() else []
    if len(pages) < 2:
        problems.append("03-site/ needs two hero variants (index.html and index-b.html); found %d" % len(pages))
    gate = site / "screenshot-gate.md"
    notes = inspection_notes(gate.read_text(encoding="utf-8")) if gate.is_file() else {}
    if not gate.is_file():
        problems.append("03-site/screenshot-gate.md is missing")
    shots = 0
    for page in pages:
        inputs = page_inputs(page)
        for width, height in SITE_SIZES:
            shot = site / "screenshots" / ("%s-%dx%d.png" % (page.stem, width, height))
            shots += 1
            check_image(shot, width, height, problems)
            note = notes.get(shot.name, "")
            if len(note) < NOTE_MIN_CHARS:
                problems.append("03-site/screenshot-gate.md has no inspection note for %s (view the image, "
                                "then say what is on it and whether the layout holds)" % shot.name)
            measure = site / "screenshots" / ("%s-%d.json" % (page.stem, width))
            problems += stale_evidence([shot, measure], inputs)
            try:
                data = gc.read_json(measure)
            except (OSError, ValueError):
                problems.append("%s is missing: run gp-chrome measure %s %dx%d and save its output"
                                % (gc.rel(pkg, measure), gc.rel(pkg, page), width, height))
                continue
            data = data if isinstance(data, dict) else {}
            scroll, inner = data.get("scrollWidth"), data.get("innerWidth")
            if data.get("viewport") != "%dx%d" % (width, height) \
                    or not all(isinstance(v, int) and not isinstance(v, bool) for v in (scroll, inner)):
                problems.append("%s is not gp-chrome measure's output for %s at %dx%d (viewport, scrollWidth, "
                                "innerWidth); measure it again" % (gc.rel(pkg, measure), page.name, width, height))
            elif data.get("overflows") or scroll > inner:
                problems.append("%s overflows horizontally at %dpx (scroll width %s)" % (page.name, width, scroll))
    return {"pages": len(pages), "screenshots": shots, "problems": problems}


def parse_size(text):
    m = re.fullmatch(r"(\d+)x(\d+)", text or "")
    if not m:
        raise ValueError("size %r is not WIDTHxHEIGHT" % text)
    return int(m.group(1)), int(m.group(2))


def check_launch_set(pkg):
    pkg = Path(pkg)
    problems = []
    manifest_path = pkg / "10-launch-set" / "manifest.json"
    try:
        manifest = gc.read_json(manifest_path)
    except (OSError, ValueError) as exc:
        return {"assets": 0, "problems": ["10-launch-set/manifest.json is missing or invalid: %s" % exc]}
    assets = manifest.get("assets") or []
    kinds = {p: set() for p in LAUNCH_PLATFORMS}
    for asset in assets:
        platform = str(asset.get("platform", "")).lower()
        kind = str(asset.get("kind", ""))
        path = pkg / "10-launch-set" / str(asset.get("path", ""))
        if platform not in kinds:
            problems.append("manifest: %s has platform %r (want instagram, x, or tiktok)" % (asset.get("path"), platform))
            continue
        kinds[platform].add(kind)
        if kind not in TEXT_KINDS:
            if path.suffix.lower() not in RASTER_SUFFIXES:
                problems.append("manifest: %s is a %s, which must be a PNG, JPEG, or WebP image rendered at its "
                                "size" % (asset.get("path"), kind))
            else:
                try:
                    width, height = parse_size(asset.get("size"))
                    check_image(path, width, height, problems, scales=(1,))
                except ValueError as exc:
                    problems.append("manifest: %s: %s" % (asset.get("path"), exc))
        elif not path.is_file():
            problems.append("%s is missing" % gc.rel(pkg, path))
        if not re.match(r"https?://\S+$", str(asset.get("size_source") or "")):
            problems.append("manifest: %s needs size_source, the http(s) URL of the platform page fetched in this "
                            "run that gives its size" % asset.get("path"))
    for platform, found in kinds.items():
        for needed in ("profile-image", "first-week-posts"):
            if needed not in found:
                problems.append("Launch Set for %s has no %s" % (platform, needed))
    return {"assets": len(assets), "problems": problems}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Screenshot and image gates")
    parser.add_argument("mode", choices=("site", "launch-set", "image"))
    parser.add_argument("target")
    parser.add_argument("--size")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.mode == "image":
        problems = []
        width, height = parse_size(args.size)
        check_image(Path(args.target), width, height, problems, scales=(1,))
        result = {"problems": problems}
    elif args.mode == "site":
        result = check_site(args.target)
    else:
        result = check_launch_set(args.target)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for problem in result["problems"]:
            print("FAIL " + problem)
        print("%s: %s gate, %d problem(s)" % ("PASS" if not result["problems"] else "FAIL", args.mode,
                                             len(result["problems"])))
    return 0 if not result["problems"] else 1


if __name__ == "__main__":
    sys.exit(main())
