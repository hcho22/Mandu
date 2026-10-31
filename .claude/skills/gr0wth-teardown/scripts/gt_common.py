"""Shared helpers for gr0wth-teardown: the run folder, the robots.txt gate, the
logged and cached fetcher, and small CSV and date helpers.

Standard library only, and Python 3.7 compatible, because the Mac's default
`python3` can be 3.7.9.

Every network read in a run goes through `Fetcher.get`, which:
  - refuses any URL whose host's robots.txt disallows it for this tool's
    product token or for `*` (RFC 9309 matching, wildcards included);
  - uses HTTPS only, and refuses a response a network filter substituted;
  - waits between requests to the same host (at least one second, longer when
    robots.txt asks or the host is known to rate-limit);
  - caches every body under the run's `data/raw/`, so a rerun reads the cache;
  - logs every fetch, refusal, and failure in the run's `sources.csv`.
"""

from __future__ import annotations

import csv
import datetime as dt
import gzip
import hashlib
import json
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
MANDU = SKILL_DIR.parents[2]

TOOL_TOKEN = "Mandu-gr0wth-teardown"
TOOL_VERSION = "1.0"
# A browser-like string so sites serve their normal public page, with this
# tool's product token appended so a site owner can see who read it.
USER_AGENT = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/130.0 Safari/537.36 %s/%s" % (TOOL_TOKEN, TOOL_VERSION))

SOURCES_NAME = "sources.csv"
SOURCES_FIELDS = ["url", "fetched_at", "status", "bytes", "sha256", "route", "robots", "cache", "note"]
CAPTURES_NAME = "capture/captures.csv"
CAPTURES_FIELDS = ["file", "channel", "url", "captured_at", "notes"]

# Seconds between two requests to one host, when robots.txt asks for nothing longer.
DEFAULT_INTERVAL = 1.0
HOST_INTERVALS = {
    "itunes.apple.com": 3.1,  # Apple's public APIs allow about 20 calls a minute.
    "web.archive.org": 4.0,  # it answers 429 to a faster pace
    "suggestqueries.google.com": 1.5,
}
MAX_CRAWL_DELAY = 10.0

# Text a network filter puts in place of the page that was asked for.
INTERCEPT_MARKERS = (b"networkprotected", b"myhomenetwork.att.com")

REDIRECTS = (301, 302, 303, 307, 308)
MAX_REDIRECTS = 5
RETRY_STATUSES = (429, 500, 502, 503, 504)
MAX_RETRY_WAIT = 60.0


class Blocked(Exception):
    """A URL this run must not read: robots.txt refuses it, or a filter intercepted it."""


class FetchError(Exception):
    """A URL that could not be read after retries."""


# ---------------------------------------------------------------- dates and files


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def iso_z(moment: dt.datetime) -> str:
    return moment.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def from_epoch(seconds) -> dt.datetime:
    return dt.datetime.fromtimestamp(int(seconds), dt.timezone.utc)


def parse_date(text: str):
    """Parse an ISO date or date-time (with Z, an offset, or none); None when it is not one."""
    if not text:
        return None
    # Fractions longer than microseconds do not parse; keep six digits.
    text = re.sub(r"(\.\d{6})\d+", r"\1", text.strip())
    # %z takes "Z" and "+00:00" from Python 3.7 on.
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S",
                "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            value = dt.datetime.strptime(text, fmt)
        except ValueError:
            continue
        if value.tzinfo is None:
            value = value.replace(tzinfo=dt.timezone.utc)
        return value.astimezone(dt.timezone.utc)
    return None


def month_of(moment: dt.datetime) -> str:
    return moment.strftime("%Y-%m")


def read_json(path):
    with open(str(path), encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path, data) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def read_csv(path):
    path = Path(path)
    if not path.exists():
        return []
    with open(str(path), encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows, fields) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: ("" if row.get(k) is None else row.get(k)) for k in fields})


def append_csv(path, row, fields) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    with open(str(path), "a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        if new:
            writer.writeheader()
        writer.writerow({k: ("" if row.get(k) is None else row.get(k)) for k in fields})


def redact(text: str, secrets=()) -> str:
    for secret in secrets:
        if secret:
            text = text.replace(secret, "REDACTED").replace(urllib.parse.quote(secret, safe=""), "REDACTED")
    return text


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "target"


def normalize_url(url: str) -> str:
    """The form two URLs are compared in: no fragment, no trailing slash, lower-case host."""
    parts = urllib.parse.urlsplit(url.strip())
    path = parts.path.rstrip("/") or ""
    return urllib.parse.urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))


# ---------------------------------------------------------------- the run folder


def product_dir(product: str) -> Path:
    path = MANDU / "projects" / product
    if not path.is_dir():
        raise SystemExit("No Product folder at %s; name one of: %s" % (
            path, ", ".join(sorted(p.name for p in (MANDU / "projects").iterdir() if p.is_dir()))))
    return path


def new_run(product: str, target: str, mode: str, country: str, today=None, base=None) -> Path:
    """Create projects/<Product>/teardowns/NN-<target>_YYMMDD/ and its run.json."""
    base = Path(base) if base else product_dir(product) / "teardowns"
    base.mkdir(parents=True, exist_ok=True)
    numbers = [int(m.group(1)) for m in (re.match(r"^(\d{2})-", p.name) for p in base.iterdir()) if m]
    number = (max(numbers) + 1) if numbers else 1
    today = today or utc_now()
    run = base / ("%02d-%s_%s" % (number, slugify(target), today.strftime("%y%m%d")))
    for sub in ("data/raw", "img", "capture"):
        (run / sub).mkdir(parents=True, exist_ok=True)
    write_json(run / "run.json", {
        "product": product, "target": target, "slug": slugify(target), "mode": mode,
        "country": country.lower(), "created_at": iso_z(today), "tool": "%s/%s" % (TOOL_TOKEN, TOOL_VERSION),
    })
    return run


def load_run(run) -> dict:
    run = Path(run)
    meta = run / "run.json"
    if not meta.exists():
        raise SystemExit("%s is not a gr0wth-teardown run folder (no run.json); start one with `gt.py init`." % run)
    data = read_json(meta)
    data["dir"] = run
    return data


def update_run(run, **fields) -> dict:
    run = Path(run)
    data = read_json(run / "run.json")
    data.update(fields)
    write_json(run / "run.json", data)
    return data


# ---------------------------------------------------------------- robots.txt (RFC 9309)


def parse_robots(text: str):
    """Return a list of groups: {"agents": [...], "rules": [(allow, pattern)], "delay": float|None}."""
    groups = []
    agents, rules, delay = [], [], None
    in_agents = False
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip().lower(), value.strip()
        if key in ("user-agent", "useragent"):
            if not in_agents and (agents or rules):
                groups.append({"agents": agents, "rules": rules, "delay": delay})
                agents, rules, delay = [], [], None
            agents.append(value.lower())
            in_agents = True
        elif key in ("allow", "disallow"):
            in_agents = False
            if agents and value:
                rules.append((key == "allow", value))
        elif key == "crawl-delay":
            in_agents = False
            try:
                delay = float(value)
            except ValueError:
                pass
    if agents or rules:
        groups.append({"agents": agents, "rules": rules, "delay": delay})
    return groups


def _pattern_regex(pattern: str):
    anchored = pattern.endswith("$")
    body = pattern[:-1] if anchored else pattern
    regex = "".join(".*" if ch == "*" else re.escape(ch) for ch in body)
    return re.compile(regex + ("$" if anchored else ""))


def _normalize_path(path: str) -> str:
    # Compare in one percent-encoding: decode what is safe, re-encode the rest.
    return urllib.parse.quote(urllib.parse.unquote(path), safe="/?=&*$:@!,;+%-._~")


def robots_verdict(groups, token: str, path: str):
    """(allowed, matched_rule, delay) for a path, per RFC 9309: the most specific
    agent's groups merged, then the longest matching rule, with allow winning a tie."""
    token = token.lower()
    chosen = [g for g in groups if token in g["agents"]]
    if not chosen:
        chosen = [g for g in groups if "*" in g["agents"]]
    rules = [r for g in chosen for r in g["rules"]]
    delay = max([g["delay"] for g in chosen if g["delay"] is not None] or [0.0])
    if path == "/robots.txt":
        return True, None, delay
    target = _normalize_path(path)
    best = None
    for allow, pattern in rules:
        if _pattern_regex(_normalize_path(pattern)).match(target):
            length = len(pattern)
            if best is None or length > best[0] or (length == best[0] and allow and not best[1]):
                best = (length, allow, pattern)
    if best is None:
        return True, None, delay
    return best[1], ("Allow: " if best[1] else "Disallow: ") + best[2], delay


class Robots:
    """robots.txt for each origin, fetched once per run and kept in `data/robots/`."""

    def __init__(self, cache_dir=None, opener=None):
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.opener = opener or _open
        self._origins = {}

    def _load(self, origin: str):
        if origin in self._origins:
            return self._origins[origin]
        cached = None
        if self.cache_dir:
            cached = self.cache_dir / (slugify(origin) + ".json")
            if cached.exists():
                state = read_json(cached)
                self._origins[origin] = state
                return state
        try:
            # RFC 9309: follow at least five redirects for robots.txt itself.
            url, hops = origin + "/robots.txt", 0
            while True:
                status, headers, body, _final = self.opener(url)
                location = headers.get("Location") if headers else None
                if status in REDIRECTS and location and hops < MAX_REDIRECTS:
                    url, hops = urllib.parse.urljoin(url, location), hops + 1
                    continue
                break
        except Exception as exc:  # network failure: RFC 9309 says assume complete disallow
            state = {"mode": "deny-all", "why": "robots.txt unreachable (%s)" % type(exc).__name__, "text": ""}
        else:
            looks_html = body.lstrip()[:200].lower().startswith((b"<!doctype", b"<html"))
            via = " via %s" % url if hops else ""
            if any(marker in body for marker in INTERCEPT_MARKERS):
                state = {"mode": "deny-all", "why": "robots.txt intercepted by a network filter", "text": ""}
            elif 200 <= status < 300 and looks_html:
                # A soft 404 or a filter page: not a robots.txt, and not proof of permission.
                state = {"mode": "deny-all", "why": "robots.txt answered with an HTML page%s" % via, "text": ""}
            elif 200 <= status < 300:
                state = {"mode": "rules", "why": "robots.txt %d%s" % (status, via), "text": body.decode("utf-8", "replace")}
            elif status in REDIRECTS or status == 429 or status >= 500:
                state = {"mode": "deny-all", "why": "robots.txt status %d%s" % (status, via), "text": ""}
            else:  # other 4xx: RFC 9309 treats the file as absent, so everything is allowed
                state = {"mode": "allow-all", "why": "robots.txt status %d%s" % (status, via), "text": ""}
        self._origins[origin] = state
        # A refusal from an unreachable or failing robots.txt may be temporary: keep it
        # for this process only, so the next command asks again.
        if cached and state["mode"] != "deny-all":
            write_json(cached, state)
        return state

    def check(self, url: str):
        """(allowed, detail, crawl_delay) for one URL."""
        parts = urllib.parse.urlsplit(url)
        origin = "%s://%s" % (parts.scheme, parts.netloc)
        state = self._load(origin)
        if state["mode"] == "deny-all":
            return False, state["why"], 0.0
        if state["mode"] == "allow-all":
            return True, state["why"], 0.0
        path = parts.path or "/"
        if parts.query:
            path += "?" + parts.query
        allowed, rule, delay = robots_verdict(parse_robots(state["text"]), TOOL_TOKEN, path)
        return allowed, (rule or "no matching rule"), delay


# ---------------------------------------------------------------- the fetcher


def _ssl_context():
    """A verifying TLS context. A python.org build that never ran its 'Install
    Certificates' step has no CA certificates; use the system bundle (or certifi)."""
    context = ssl.create_default_context()
    if context.cert_store_stats().get("x509_ca", 0):
        return context
    for bundle in ("/etc/ssl/cert.pem", "/usr/local/etc/openssl/cert.pem", "/opt/homebrew/etc/openssl@3/cert.pem"):
        if Path(bundle).exists():
            context.load_verify_locations(cafile=bundle)
            return context
    try:
        import certifi  # noqa: WPS433 (optional)
        context.load_verify_locations(cafile=certifi.where())
    except ImportError:
        pass
    return context


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Return every redirect to the caller, which checks robots.txt for each hop."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_OPENER = None


def _open(url, data=None, headers=None, timeout=30):
    """One request, no redirects followed: (status, headers, body, url)."""
    global _OPENER
    if _OPENER is None:
        _OPENER = urllib.request.build_opener(_NoRedirect, urllib.request.HTTPSHandler(context=_ssl_context()))
    request = urllib.request.Request(url, data=data, headers=dict({
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    }, **(headers or {})))
    try:
        response = _OPENER.open(request, timeout=timeout)
        status = response.status
    except urllib.error.HTTPError as exc:
        response = exc
        status = exc.code
    body = response.read()
    encoding = (response.headers.get("Content-Encoding") or "").lower()
    body = _decompress(body, encoding)
    return status, response.headers, body, response.geturl()


def _decompress(body: bytes, encoding: str) -> bytes:
    if encoding == "gzip" or body[:2] == b"\x1f\x8b":
        try:
            return gzip.decompress(body)
        except OSError:
            return body
    if encoding == "deflate":
        try:
            return zlib.decompress(body)
        except zlib.error:
            return zlib.decompress(body, -zlib.MAX_WBITS)
    return body


def _retry_after(headers, default):
    value = headers.get("Retry-After") if headers else None
    try:
        return min(max(float(value), 1.0), MAX_RETRY_WAIT)
    except (TypeError, ValueError):
        return default


class Response:
    def __init__(self, url, status, body, headers=None, from_cache=False, cache=None):
        self.url = url
        self.status = status
        self.body = body
        self.headers = headers or {}
        self.from_cache = from_cache
        self.cache = cache

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 300

    def text(self) -> str:
        return self.body.decode("utf-8", "replace")

    def json(self):
        return json.loads(self.text())


class Fetcher:
    """Reads public URLs for one run: robots-gated, HTTPS only, polite, cached, and logged."""

    def __init__(self, run, refresh=False, opener=None, sleep=time.sleep, clock=time.monotonic):
        self.run = Path(run)
        self.refresh = refresh
        self.opener = opener or _open
        self.sleep = sleep
        self.clock = clock
        self.robots = Robots(self.run / "data" / "robots", opener=self.opener)
        self._last = {}

    # The log ------------------------------------------------------------
    def log(self, url, status, body=b"", route="direct", robots="", cache="", note="", secrets=()):
        url = redact(url, secrets)
        append_csv(self.run / SOURCES_NAME, {
            "url": url, "fetched_at": iso_z(utc_now()), "status": status, "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest() if body else "", "route": route,
            "robots": robots, "cache": cache, "note": note,
        }, SOURCES_FIELDS)

    def gate(self, url: str, route: str = "direct", secrets=()):
        """Raise Blocked when robots.txt refuses the URL; return (detail, delay) otherwise."""
        allowed, detail, delay = self.robots.check(url)
        if not allowed:
            self.log(url, "robots-denied", route=route, robots=detail, secrets=secrets)
            raise Blocked("%s: robots.txt refuses it (%s)" % (redact(url, secrets), detail))
        return detail, delay

    def _cache_path(self, url: str, data=None) -> Path:
        key = hashlib.sha1((url + "\n" + (data.decode("utf-8", "replace") if data else "")).encode()).hexdigest()[:20]
        host = urllib.parse.urlsplit(url).netloc or "local"
        return self.run / "data" / "raw" / slugify(host) / key

    def _wait(self, host: str, delay: float):
        interval = max(DEFAULT_INTERVAL, HOST_INTERVALS.get(host, 0.0), min(delay or 0.0, MAX_CRAWL_DELAY))
        last = self._last.get(host)
        if last is not None:
            remaining = interval - (self.clock() - last)
            if remaining > 0:
                self.sleep(remaining)
        self._last[host] = self.clock()

    def get(self, url, route="direct", also_gate=(), data=None, headers=None, retries=4, secrets=()) -> Response:
        """Fetch a URL. `also_gate` lists further URLs whose robots.txt must allow the read,
        such as the original page behind a Wayback Machine snapshot. Redirects are
        followed here, hop by hop, so robots.txt is asked about every address read.
        `secrets` are values (an API key) that never reach the log, the cache records,
        or an error message."""
        if url.startswith("http://"):
            url = "https://" + url[len("http://"):]
        if not url.startswith("https://"):
            raise Blocked("%s: only https:// URLs are read" % redact(url, secrets))
        for other in also_gate:
            self.gate(other, route=route)
        shown = redact(url, secrets)
        cache = self._cache_path(shown, data)
        meta = cache.with_suffix(".json")
        if cache.exists() and meta.exists() and not self.refresh:
            self.gate(url, route=route, secrets=secrets)
            info = read_json(meta)
            return Response(info.get("final_url") or url, info["status"], cache.read_bytes(),
                            info.get("headers", {}), True, cache)
        current, hops = url, 0
        while True:
            status, resp_headers, body, detail = self._fetch_one(current, route, data, headers, retries, secrets)
            location = resp_headers.get("Location") if resp_headers else None
            if status in REDIRECTS and location and hops < MAX_REDIRECTS:
                nxt = urllib.parse.urljoin(current, location)
                if nxt.startswith("http://"):
                    nxt = "https://" + nxt[len("http://"):]
                self.log(current, status, route=route, robots=detail, note="redirect to " + redact(nxt, secrets),
                         secrets=secrets)
                current, hops = nxt, hops + 1
                data = None if status == 303 else data
                continue
            break
        final_shown = redact(current, secrets)
        if any(marker in body[:4000] for marker in INTERCEPT_MARKERS) or urllib.parse.urlsplit(current).netloc.endswith("att.com"):
            self.log(current, "intercepted", body, route=route, robots=detail, note="network filter page", secrets=secrets)
            raise Blocked("%s: a network filter replaced the response (read it from another network or by hand)" % shown)
        kept = {k: resp_headers.get(k) for k in ("Content-Type", "Last-Modified", "Date") if resp_headers and resp_headers.get(k)}
        cache_note = ""
        if status in RETRY_STATUSES:  # throttled or failing: never cached, so the next run asks again
            cache_note = "not cached"
        else:
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_bytes(body)
            write_json(meta, {"url": shown, "status": status, "headers": kept, "final_url": final_shown})
        self.log(current, status, body, route=route, robots=detail, secrets=secrets,
                 cache="" if cache_note else str(cache.relative_to(self.run)),
                 note=cache_note or ("" if final_shown == shown else "reached from " + shown))
        return Response(current, status, body, kept, False, cache)

    def _fetch_one(self, url, route, data, headers, retries, secrets):
        """One address, gated and paced, retried when throttled: (status, headers, body, robots detail)."""
        detail, delay = self.gate(url, route=route, secrets=secrets)
        host = urllib.parse.urlsplit(url).netloc
        attempt = 0
        while True:
            self._wait(host, delay)
            try:
                status, resp_headers, body, _final = self.opener(url, data=data, headers=headers)
            except Exception as exc:
                if attempt < retries:
                    attempt += 1
                    self.sleep(min(2.0 ** attempt, MAX_RETRY_WAIT))
                    continue
                self.log(url, "error", route=route, robots=detail, note=type(exc).__name__, secrets=secrets)
                raise FetchError("%s: %s" % (redact(url, secrets), redact(str(exc), secrets)))
            if status in RETRY_STATUSES and attempt < retries:
                attempt += 1
                self.sleep(_retry_after(resp_headers, default=min(4.0 * 2 ** (attempt - 1), MAX_RETRY_WAIT)))
                continue
            return status, resp_headers, body, detail

    def save(self, url, dest, route="direct") -> Path:
        """Fetch a URL into a file (an image, usually) and return the file's path."""
        response = self.get(url, route=route)
        if not response.ok:
            raise FetchError("%s: status %s" % (url, response.status))
        dest = Path(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(response.body)
        return dest


def logged_urls(run) -> set:
    """Every URL this run read (sources.csv, fetched rows only) or hcho captured by hand."""
    run = Path(run)
    urls = set()
    for row in read_csv(run / SOURCES_NAME):
        status = row.get("status", "")
        if status.isdigit() and 200 <= int(status) < 400:
            urls.add(normalize_url(row["url"]))
    for row in read_csv(run / CAPTURES_NAME):
        if row.get("url"):
            urls.add(normalize_url(row["url"]))
    return urls
