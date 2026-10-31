"""The arithmetic of a teardown. Every number a playbook states comes out of here
or out of a data file, never out of the agent's head.

- rank: per channel, settled posts only, top quarter vs bottom half, spread speed
- growth: a monthly series from App Store ratings history and a Google Trends
  export, with the inflection (the largest sustained step up)
- moves: dated moves, clustered when under 30 days apart, each cluster's lift in
  growth (the two months before vs the month of and the two after), and per
  channel a Spearman correlation between monthly moves and later growth
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import math
import re

import gt_common as gc

SETTLE_DAYS = 7
MIN_PATTERN_POSTS = 20
CLUSTER_GAP_DAYS = 30
MIN_CORR_MONTHS = 12
MIN_CORR_MOVES = 5


# ---------------------------------------------------------------- small statistics


def mean(values):
    values = [v for v in values if v is not None]
    return sum(values) / len(values) if values else None


def ranks_of(values):
    """Average ranks (1-based), ties sharing the mean of their positions."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        for k in range(i, j + 1):
            ranks[order[k]] = (i + j) / 2.0 + 1
        i = j + 1
    return ranks


def pearson(x, y):
    n = len(x)
    if n < 2:
        return None
    mx, my = sum(x) / n, sum(y) / n
    sx = math.sqrt(sum((a - mx) ** 2 for a in x))
    sy = math.sqrt(sum((b - my) ** 2 for b in y))
    if sx == 0 or sy == 0:
        return None
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)


def spearman(x, y):
    return pearson(ranks_of(x), ranks_of(y))


def to_number(value):
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace(",", "")
    m = re.fullmatch(r"([0-9]*\.?[0-9]+)\s*([KMB]?)", text, re.I)
    if not m:
        return None
    return float(m.group(1)) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2).upper()]


_REL = re.compile(r"(\d+)\s+(second|minute|hour|day|week|month|year)s?\s+ago", re.I)
_DAYS = {"second": 1 / 86400, "minute": 1 / 1440, "hour": 1 / 24, "day": 1, "week": 7, "month": 30.44, "year": 365.25}


def relative_date(text, now):
    """'3 months ago' -> an approximate date; None when the text is not relative."""
    m = _REL.search(text or "")
    if not m:
        return None
    return now - dt.timedelta(days=int(m.group(1)) * _DAYS[m.group(2).lower()])


# ---------------------------------------------------------------- ranking posts


def rank(rows, now, metric_key="metric", date_key="date", settle_days=SETTLE_DAYS):
    """Mark each settled post top, middle, or bottom within its channel, and add its age
    and spread speed (metric per day since posting). Returns (rows, summary)."""
    usable, unsettled, undated = [], 0, 0
    for row in rows:
        value = to_number(row.get(metric_key))
        if value is None:
            row["tier"] = "unranked"
            continue
        when = gc.parse_date(row.get(date_key, "")) or relative_date(row.get("published_text", ""), now)
        age = (now - when).total_seconds() / 86400 if when else None
        if age is not None and age < settle_days:
            unsettled += 1
            row["tier"] = "unsettled"
            continue
        if age is None:
            undated += 1
        row["metric_value"] = value
        row["age_days"] = round(age, 1) if age is not None else ""
        row["spread_per_day"] = round(value / max(age, 1.0), 2) if age is not None else ""
        usable.append(row)
    ordered = sorted(usable, key=lambda r: -r["metric_value"])
    n = len(ordered)
    top_n = int(math.ceil(n / 4.0)) if n else 0
    bottom_n = n // 2
    for index, row in enumerate(ordered):
        row["tier"] = "top" if index < top_n else ("bottom" if index >= n - bottom_n else "middle")
    spreads = [r for r in ordered if r["spread_per_day"] != ""]
    spreads.sort(key=lambda r: -r["spread_per_day"])
    fast_n = int(math.ceil(len(spreads) / 4.0)) if spreads else 0
    for index, row in enumerate(spreads):
        row["fast_spreader"] = index < fast_n
    summary = {
        "posts": n, "unsettled_dropped": unsettled, "undated": undated, "top": top_n, "bottom": bottom_n,
        "top_cut": ordered[top_n - 1]["metric_value"] if top_n else None,
        "bottom_cut": ordered[n - bottom_n]["metric_value"] if bottom_n else None,
        "median": ordered[n // 2]["metric_value"] if n else None,
        "pattern_callable": n >= MIN_PATTERN_POSTS,
        "note": "" if n >= MIN_PATTERN_POSTS else "too few posts to call a pattern (%d settled, %d needed)" % (n, MIN_PATTERN_POSTS),
    }
    return ordered + [r for r in rows if r.get("tier") in ("unsettled", "unranked")], summary


# ---------------------------------------------------------------- growth


def ratings_series(history_rows):
    """Ratings total per snapshot month, and ratings gained per day since the previous snapshot.
    A rate covers the interval before its snapshot, so it is filed under the month of that
    interval's midpoint (`rate_month`), not the snapshot's month."""
    points = []
    for row in history_rows:
        ratings = to_number(row.get("ratings"))
        when = dt.datetime.strptime(row["snapshot"][:8], "%Y%m%d").replace(tzinfo=dt.timezone.utc)
        if ratings is not None:
            points.append((when, ratings, row))
    points.sort(key=lambda p: p[0])
    out = []
    for i, (when, ratings, row) in enumerate(points):
        per_day, rate_month, days = None, "", ""
        if i:
            prev_when, prev_ratings, _ = points[i - 1]
            days = (when - prev_when).days
            if days > 0 and ratings >= prev_ratings:
                per_day = (ratings - prev_ratings) / days
                rate_month = gc.month_of(prev_when + (when - prev_when) / 2)
        out.append({"month": gc.month_of(when), "date": when.strftime("%Y-%m-%d"), "ratings": int(ratings),
                    "ratings_per_day": round(per_day, 2) if per_day is not None else "",
                    "rate_month": rate_month, "interval_days": days,
                    "exact": row.get("ratings_exact", ""), "source": row.get("snapshot_url", "")})
    return out


def parse_trends(text):
    """A Google Trends 'multiTimeline.csv' export -> {term: {month: mean index}}."""
    lines = text.lstrip("﻿").splitlines()
    start = next((i for i, line in enumerate(lines) if re.match(r"^(Week|Month|Day|Time)\b", line)), None)
    if start is None:
        return {}
    reader = csv.reader(io.StringIO("\n".join(lines[start:])))
    header = next(reader)
    terms = [re.sub(r":\s*\(.*\)$", "", h).strip() for h in header[1:]]
    sums = {t: {} for t in terms}
    for record in reader:
        if not record or not record[0].strip():
            continue
        month = record[0].strip()[:7]
        for term, raw in zip(terms, record[1:]):
            value = 0.5 if raw.strip() == "<1" else to_number(raw)
            if value is None:
                continue
            total, count = sums[term].get(month, (0.0, 0))
            sums[term][month] = (total + value, count + 1)
    return {t: {m: round(s / c, 2) for m, (s, c) in months.items()} for t, months in sums.items()}


def merge_growth(ratings=(), trends=None):
    rows = {}
    for r in ratings:
        rows.setdefault(r["month"], {"month": r["month"]})["ratings"] = r["ratings"]
        if r.get("rate_month") and r["ratings_per_day"] != "":
            rows.setdefault(r["rate_month"], {"month": r["rate_month"]}).update(
                {"ratings_per_day": r["ratings_per_day"], "rate_interval_days": r["interval_days"]})
    for term, months in (trends or {}).items():
        for month, value in months.items():
            rows.setdefault(month, {"month": month})["trends:" + term] = value
    return [rows[m] for m in sorted(rows)]


def inflection(series, key="ratings_per_day", window=3, min_points=2):
    """The month where the mean of `key` over the next `window` observed points most
    exceeds the mean over the previous `window`; None without enough points."""
    points = [(r["month"], to_number(r.get(key))) for r in series]
    points = [(m, v) for m, v in points if v is not None]
    best = None
    for i in range(min_points, len(points) - min_points + 1):
        before = [v for _m, v in points[max(0, i - window):i]]
        after = [v for _m, v in points[i:i + window]]
        if len(before) < min_points or len(after) < min_points:
            continue
        b, a = mean(before), mean(after)
        step = a - b
        if best is None or step > best["step"]:
            best = {"month": points[i][0], "before": round(b, 2), "after": round(a, 2), "step": round(step, 2),
                    "ratio": round(a / b, 2) if b else None, "key": key,
                    "before_months": [m for m, _v in points[max(0, i - window):i]],
                    "after_months": [m for m, _v in points[i:i + window]]}
    return best


# ---------------------------------------------------------------- moves vs growth


def _month_index(month):
    year, mon = int(month[:4]), int(month[5:7])
    return year * 12 + mon - 1


def _month_name(index):
    return "%04d-%02d" % (index // 12, index % 12 + 1)


def clusters(moves, gap_days=CLUSTER_GAP_DAYS):
    """Group dated moves: a move under `gap_days` after the previous one joins its cluster."""
    dated = sorted(((gc.parse_date(m["date"]), m) for m in moves if gc.parse_date(m.get("date", ""))),
                   key=lambda pair: pair[0])
    groups = []
    for when, move in dated:
        if groups and (when - groups[-1]["last"]).days < gap_days:
            groups[-1]["moves"].append(move)
            groups[-1]["last"] = when
        else:
            groups.append({"start": when, "last": when, "moves": [move]})
    return groups


def lift(series, month, key="ratings_per_day"):
    """Mean of `key` in the month of and the two after, minus the two months before."""
    values = {r["month"]: to_number(r.get(key)) for r in series}
    m = _month_index(month)
    before = [values.get(_month_name(m - k)) for k in (2, 1)]
    after = [values.get(_month_name(m + k)) for k in (0, 1, 2)]
    b, a = mean(before), mean(after)
    if b is None or a is None:
        return {"before": b, "after": a, "lift": None, "lift_pct": None,
                "note": "not enough growth data around %s" % month}
    return {"before": round(b, 2), "after": round(a, 2), "lift": round(a - b, 2),
            "lift_pct": round(100.0 * (a - b) / b, 1) if b else None, "note": ""}


def moves_vs_growth(moves, series, key="ratings_per_day"):
    rows = []
    for group in clusters(moves):
        month = gc.month_of(group["start"])
        result = lift(series, month, key)
        rows.append({
            "cluster_start": group["start"].strftime("%Y-%m-%d"), "cluster_end": group["last"].strftime("%Y-%m-%d"),
            "moves": len(group["moves"]), "channels": ", ".join(sorted({m.get("channel", "") for m in group["moves"]})),
            "labels": " | ".join(m.get("label", "") for m in group["moves"])[:500],
            "urls": " ".join(m.get("url", "") for m in group["moves"] if m.get("url")),
            "key": key, "before": result["before"], "after": result["after"], "lift": result["lift"],
            "lift_pct": result["lift_pct"], "note": result["note"]})
    return rows


def channel_correlations(moves, series, key="ratings_per_day", lags=(0, 1, 2)):
    values = {r["month"]: to_number(r.get(key)) for r in series}
    observed = sorted(m for m, v in values.items() if v is not None)
    out = []
    by_channel = {}
    for move in moves:
        when = gc.parse_date(move.get("date", ""))
        if when:
            by_channel.setdefault(move.get("channel", ""), []).append(gc.month_of(when))
    for channel, months in sorted(by_channel.items()):
        counts = {}
        for month in months:
            counts[month] = counts.get(month, 0) + 1
        for lag in lags:
            pairs = []
            for month in observed:
                source = _month_name(_month_index(month) - lag)
                pairs.append((counts.get(source, 0), values[month]))
            row = {"channel": channel, "lag_months": lag, "months": len(pairs), "moves": len(months), "rho": "",
                   "note": ""}
            if len(pairs) < MIN_CORR_MONTHS or len(months) < MIN_CORR_MOVES:
                row["note"] = "too few months or moves to call a correlation"
            else:
                rho = spearman([p[0] for p in pairs], [p[1] for p in pairs])
                row["rho"] = round(rho, 3) if rho is not None else ""
                row["note"] = "" if rho is not None else "no variation"
            out.append(row)
    return out
