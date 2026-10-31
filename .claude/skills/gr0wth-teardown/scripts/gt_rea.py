"""Run REA's browser capture for a teardown, and read what it captured.

REA (`rea-agents` on npm) drives a headless Chrome on a throwaway profile, loads
one public page the way a visitor's browser would, and returns every request
the page made, with response bodies when asked. A teardown uses it for two jobs
a plain fetch cannot do:
  - the growth stack: tags that a tag manager adds after the page loads;
  - pages that are JavaScript applications, such as Google's Ads Transparency
    Center, whose data arrives in the page's own API responses.

robots.txt must allow the start URL; the page's own subresources load as they
would for any visitor. The capture runs through REA's CLI, so it works whether or
not REA's MCP server is connected in this session.
"""

from __future__ import annotations

import base64
import glob
import json
import os
import re
import subprocess
import urllib.parse
from pathlib import Path

import gt_common as gc

REA_PACKAGE = "rea-agents@6.8.0"
# rea-agents 6.8.0 imports zlib.zstdDecompress, which Node added in 22.15 and 23.8.
NODE_MINIMUMS = ((22, 15), (23, 8))
CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]
LIMITS = {
    "max_events": 20000,
    "max_event_allocation_bytes": 33554432,
    "max_total_event_allocation_bytes": 536870912,
    "max_network_body_bytes": 8000000,
    "max_network_body_allocation_bytes": 268435456,
    "max_network_header_allocation_bytes": 16777216,
    "max_network_metadata_allocation_bytes": 16777216,
}


class ReaUnavailable(Exception):
    pass


def _version(node: str):
    try:
        out = subprocess.run([node, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             timeout=20, check=False).stdout.decode().strip()
    except (OSError, subprocess.SubprocessError):
        return None
    m = re.match(r"v(\d+)\.(\d+)\.(\d+)", out)
    return tuple(int(x) for x in m.groups()) if m else None


def supports_rea(version) -> bool:
    if not version:
        return False
    major, minor = version[0], version[1]
    if major >= 24:
        return True
    return any(major == want_major and minor >= want_minor for want_major, want_minor in NODE_MINIMUMS)


def find_node():
    """The newest Node on this Mac that REA can run on, or None."""
    candidates = []
    if os.environ.get("GT_NODE"):
        candidates.append(os.environ["GT_NODE"])
    for folder in os.environ.get("PATH", "").split(os.pathsep):
        candidates.append(os.path.join(folder, "node"))
    candidates += sorted(glob.glob(os.path.expanduser("~/.nvm/versions/node/*/bin/node")))
    candidates += ["/opt/homebrew/bin/node", "/usr/local/bin/node"]
    best = None
    seen = set()
    for path in candidates:
        real = os.path.realpath(path)
        if real in seen or not os.path.exists(real):
            continue
        seen.add(real)
        version = _version(real)
        if supports_rea(version) and (best is None or version > best[1]):
            best = (real, version)
    return best


def find_chrome():
    for path in ([os.environ["GT_CHROME"]] if os.environ.get("GT_CHROME") else []) + CHROME_PATHS:
        if os.path.exists(path):
            return path
    return None


def scenario(url, query=(), wait_ms=6000, bodies=False, request_bodies=False, chrome=None, at_end=("url",)):
    return {
        "browser": {"mode": "launch", "executable_path": chrome or find_chrome(), "headless": True},
        "start_url": {"url": url, "query": [{"name": k, "value": {"source": "literal", "value": v}} for k, v in query]},
        "actions": [{"action": "wait_for_timeout", "step_id": "settle", "duration_ms": int(wait_ms)}],
        "capture": {"events": ["network"], "at_end": list(at_end),
                    "network": {"response_body": bool(bodies), "request_body": bool(request_bodies),
                                "header_values": False},
                    "limits": LIMITS},
    }


def capture(fetcher, name, url, query=(), wait_ms=6000, bodies=False, request_bodies=False, at_end=("url",)):
    """Run one capture and save it as data/rea/<name>.json; return that path."""
    run = fetcher.run
    full_url = url + (("&" if "?" in url else "?") + urllib.parse.urlencode(list(query)) if query else "")
    detail, _delay = fetcher.gate(full_url, route="rea")
    node = find_node()
    if not node:
        raise ReaUnavailable("REA needs Node 22.15+ (or 23.8+, 24+); none was found. Install one with nvm, "
                             "or set GT_NODE to its path.")
    chrome = find_chrome()
    if not chrome:
        raise ReaUnavailable("No Chrome or Chromium found; set GT_CHROME to its executable.")
    out_dir = run / "data" / "rea"
    out_dir.mkdir(parents=True, exist_ok=True)
    spec = out_dir / ("%s.scenario.json" % name)
    gc.write_json(spec, scenario(url, query, wait_ms, bodies, request_bodies, chrome, at_end))
    out = out_dir / ("%s.json" % name)
    node_bin = os.path.dirname(node[0])
    npx = os.path.join(node_bin, "npx")
    env = dict(os.environ, PATH=node_bin + os.pathsep + os.environ.get("PATH", ""))
    with open(str(out), "wb") as handle:
        proc = subprocess.run([npx, "-y", REA_PACKAGE, "capture-browser-scenario", str(spec), "--format", "json"],
                              stdout=handle, stderr=subprocess.PIPE, env=env, timeout=600, check=False)
    try:
        evidence = gc.read_json(out)
    except ValueError:
        tail = proc.stderr.decode("utf-8", "replace")[-800:]
        fetcher.log(full_url, "error", route="rea", robots=detail, note="REA output was not JSON")
        raise ReaUnavailable("REA did not return JSON (exit %s): %s" % (proc.returncode, tail))
    if "error" in evidence:
        fetcher.log(full_url, "error", route="rea", robots=detail, note=evidence.get("code", "rea error"))
        raise ReaUnavailable("REA refused the capture: %s" % json.dumps(evidence)[:800])
    status = document_status(evidence, url)
    fetcher.log(full_url, status if status is not None else "captured", route="rea", robots=detail,
                cache=str(out.relative_to(run)), note="evidence %s" % evidence.get("evidence_id", ""))
    return out


def _items(evidence):
    result = evidence.get("normalized_result", evidence)
    return ((result.get("events") or {}).get("items")) or []


def document_status(evidence, url):
    """The HTTP status of the start page's document response, when the capture holds it."""
    target = gc.normalize_url(url)
    for item in _items(evidence):
        if item.get("kind") == "response" and item.get("resource_type") == "document":
            if gc.normalize_url(item["url"]["url"].split("?")[0]) == target.split("?")[0]:
                return item.get("status")
    return None


def bodies(evidence, url_pattern, phase="response"):
    """[(url, method, bytes)] for captured bodies whose request URL matches a regex."""
    pattern = re.compile(url_pattern)
    requests = {}
    for item in _items(evidence):
        if item.get("kind") == "request":
            requests[item["transaction_id"]] = (item["url"]["url"], item.get("method", "GET"))
    out, seen = [], set()
    for item in _items(evidence):
        if item.get("kind") != "network-content" or item.get("phase") != phase:
            continue
        body = item.get("body") or {}
        if body.get("state") != "captured" or not body.get("content"):
            continue
        url, method = requests.get(item["transaction_id"], ("", ""))
        if not pattern.search(url):
            continue
        raw = base64.b64decode(body["content"]) if body.get("encoding") == "base64" else body["content"].encode()
        if raw in seen:
            continue
        seen.add(raw)
        out.append((url, method, raw))
    return out


def load(path):
    return gc.read_json(Path(path))
