"""Ads a target runs, from free public ad libraries.

Google's Ads Transparency Center allows automated readers in its robots.txt but
is a JavaScript application, so REA loads it in a browser and this module reads
the creatives from the page's own SearchCreatives responses. The field meanings
below were read off a real response on 2026-10-30 (Ladder, joinladder.com):
format 1 creatives were search text ads (headline, display URL, sitelinks)
delivered as a rendered <img> preview, format 3 was a video delivered as a preview
script, and field 13 was smaller than the first-to-last span, so it counts days
shown. Format 2 (image) is inferred from the Transparency Center's three formats.

Meta's Ad Library, TikTok's Ad Library, LinkedIn's Ad Library, and Apple's Ad
Repository refuse automated readers in robots.txt; `manual_urls` gives hcho the
pre-filled search pages to open himself (see references/capture-guide.md).
"""

from __future__ import annotations

import json
import re
import urllib.parse

import gt_common as gc
import gt_rea

FORMATS = {1: "text", 2: "image", 3: "video"}
GOOGLE_FIELDS = ["creative_id", "advertiser_id", "advertiser", "domain", "format", "first_shown",
                 "last_shown", "days_shown", "span_days", "running_60_plus", "preview_kind", "preview_url",
                 "image", "ad_url"]


def _epoch(node):
    if isinstance(node, dict) and node.get("1"):
        return gc.from_epoch(node["1"])
    return None


def parse_search_creatives(raw: bytes):
    """(rows, shown_total) from one SearchCreatives response body."""
    data = json.loads(raw.decode("utf-8", "replace"))
    rows = []
    for creative in data.get("1") or []:
        content = creative.get("3") or {}
        preview, kind = "", ""
        img = re.search(r'src="([^"]+)"', ((content.get("3") or {}).get("2")) or "")
        if img:
            preview, kind = img.group(1), "image"
        elif (content.get("1") or {}).get("4"):
            preview, kind = content["1"]["4"], "script"
        first, last = _epoch(creative.get("6")), _epoch(creative.get("7"))
        span = (last - first).days + 1 if first and last else None
        advertiser, cid = creative.get("1", ""), creative.get("2", "")
        rows.append({
            "creative_id": cid, "advertiser_id": advertiser, "advertiser": creative.get("12", ""),
            "domain": creative.get("14", ""), "format": FORMATS.get(creative.get("4"), "code %s" % creative.get("4")),
            "first_shown": first.strftime("%Y-%m-%d") if first else "",
            "last_shown": last.strftime("%Y-%m-%d") if last else "",
            "days_shown": creative.get("13", ""), "span_days": span or "",
            "running_60_plus": bool(span and span >= 60),
            "preview_kind": kind, "preview_url": preview, "image": "",
            "ad_url": "https://adstransparency.google.com/advertiser/%s/creative/%s" % (advertiser, cid),
        })
    return rows, data.get("5") or data.get("4") or ""


def google(fetcher, domain, region="US"):
    """Creatives Google shows for a domain in a region (the first page, up to 40)."""
    path = gt_rea.capture(fetcher, "ads-google", "https://adstransparency.google.com/",
                          query=[("region", region), ("domain", domain)], wait_ms=9000, bodies=True,
                          at_end=("url", "accessibility"))
    evidence = gt_rea.load(path)
    rows, total = [], ""
    seen = set()
    for _url, _method, raw in gt_rea.bodies(evidence, r"SearchService/SearchCreatives"):
        try:
            page_rows, page_total = parse_search_creatives(raw)
        except ValueError:
            continue
        total = total or page_total
        for row in page_rows:
            if row["creative_id"] not in seen:
                seen.add(row["creative_id"])
                rows.append(row)
    return rows, {"domain": domain, "region": region, "shown_total": total, "creatives_read": len(rows),
                  "page": "https://adstransparency.google.com/?region=%s&domain=%s" % (region, domain),
                  "evidence": str(path.relative_to(fetcher.run))}


def manual_urls(name, domain, country="US"):
    """Ad library searches hcho opens in his own browser and captures by hand."""
    q = urllib.parse.quote(name)
    return [
        ("meta", "Meta Ad Library (Facebook, Instagram, Messenger, Audience Network)",
         "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=%s&q=%s"
         "&search_type=keyword_unordered&media_type=all" % (country, q)),
        ("tiktok-ads", "TikTok Ad Library (ads shown in the EU and UK)",
         "https://library.tiktok.com/ads?region=all&adv_name=%s&sort_type=last_shown_date,desc" % q),
        ("linkedin-ads", "LinkedIn Ad Library", "https://www.linkedin.com/ad-library/search?accountOwner=%s" % q),
        ("apple-ads", "Apple Ad Repository (App Store ads shown in the EU; search the developer name)",
         "https://adrepository.apple.com/"),
        ("google-ads", "Google Ads Transparency Center (read automatically; open it to see the creatives)",
         "https://adstransparency.google.com/?region=%s&domain=%s" % (country, domain)),
    ]
