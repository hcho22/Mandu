"""Name the growth tools a page loads, from the URLs it requested.

The input is the request list of an REA browser capture (the best source: it
sees tags a tag manager adds after load), a HAR file, or a page's static HTML
(which sees only tags written into the page). A tool seen this way is SEEN;
what the team runs on it is INFERRED.
"""

from __future__ import annotations

import json
import re
import urllib.parse

# (name, category, host or URL regex, optional regex whose group 1 is the account or pixel id)
SIGNATURES = [
    # Tag managers and site analytics
    ("Google Tag Manager", "tag manager", r"googletagmanager\.com/gtm\.js", r"[?&]id=(GTM-[A-Z0-9]+)"),
    ("Google tag (gtag.js)", "tag manager", r"googletagmanager\.com/gtag/js", r"[?&]id=([A-Z]{1,3}-[A-Z0-9]+)"),
    ("Google Analytics 4", "analytics", r"google-analytics\.com/g/collect|analytics\.google\.com/g/collect|google-analytics\.com/analytics\.js", r"[?&]tid=(G-[A-Z0-9]+)"),
    ("Segment", "customer data", r"cdn\.segment\.com|api\.segment\.io", r"analytics\.js/v1/([A-Za-z0-9]+)/"),
    ("RudderStack", "customer data", r"rudderlabs\.com|rudderstack\.com", None),
    ("mParticle", "customer data", r"mparticle\.com", None),
    ("Amplitude", "product analytics", r"amplitude\.com", None),
    ("Mixpanel", "product analytics", r"mxpnl\.com|mixpanel\.com", None),
    ("PostHog", "product analytics", r"posthog\.com", None),
    ("Heap", "product analytics", r"heapanalytics\.com", None),
    ("Hotjar", "session replay", r"hotjar\.com", r"hjid[=:](\d+)"),
    ("Microsoft Clarity", "session replay", r"clarity\.ms", r"clarity\.ms/tag/([a-z0-9]+)"),
    ("FullStory", "session replay", r"fullstory\.com", None),
    ("LogRocket", "session replay", r"logrocket\.(com|io)|lr-ingest", None),
    ("Sentry", "error monitoring", r"sentry\.io|sentry-cdn\.com", r"\bo(\d+)\.ingest"),
    ("Datadog RUM", "error monitoring", r"datadoghq\.com|browser-intake-datadoghq", None),
    ("Cloudflare Web Analytics", "analytics", r"cloudflareinsights\.com", None),
    ("Vercel Analytics", "analytics", r"/_vercel/insights|vitals\.vercel-insights\.com", None),
    ("Plausible", "analytics", r"plausible\.io", None),
    # Ad pixels: a pixel on the site means the team can measure that network's ads
    ("Meta Pixel", "ad pixel", r"connect\.facebook\.net/.+/fbevents\.js|connect\.facebook\.net/signals/|facebook\.com/tr\b", r"facebook\.com/tr/?\?id=(\d+)|signals/config/(\d+)"),
    ("TikTok Pixel", "ad pixel", r"analytics\.tiktok\.com|analytics-ipv6\.tiktokw\.us", r"sdkid=([A-Z0-9]+)"),
    ("Google Ads", "ad pixel", r"googleads\.g\.doubleclick\.net|googleadservices\.com|google\.com/pagead|google\.com/ccm/collect", r"pagead/(?:viewthrough)?conversion/(\d+)"),
    ("Google Campaign Manager / Floodlight", "ad pixel", r"ad\.doubleclick\.net|fls\.doubleclick\.net|\.fls\.doubleclick", None),
    ("Google remarketing audiences", "ad pixel", r"stats\.g\.doubleclick\.net|cm\.g\.doubleclick\.net|google\.com/ads/ga-audiences|google\.com/pagead/1p-user-list", None),
    ("Snap Pixel", "ad pixel", r"sc-static\.net/scevent|tr\.snapchat\.com", None),
    ("Pinterest Tag", "ad pixel", r"s\.pinimg\.com/ct/|ct\.pinterest\.com", None),
    ("Reddit Pixel", "ad pixel", r"redditstatic\.com/ads/pixel|alb\.reddit\.com|pixel-config\.reddit\.com", None),
    ("X (Twitter) Pixel", "ad pixel", r"static\.ads-twitter\.com|analytics\.twitter\.com|t\.co/1/i/adsct|t\.co/i/adsct", None),
    ("LinkedIn Insight Tag", "ad pixel", r"snap\.licdn\.com|px\.ads\.linkedin\.com", None),
    ("Microsoft Ads (UET)", "ad pixel", r"bat\.bing\.com", None),
    ("AppLovin Axon", "ad pixel", r"axon\.ai|applovin\.com", None),
    ("Quora Pixel", "ad pixel", r"quora\.com/qevents|q\.quora\.com", None),
    ("Taboola", "ad pixel", r"taboola\.com", None),
    ("Outbrain", "ad pixel", r"outbrain\.com", None),
    ("The Trade Desk", "ad pixel", r"adsrvr\.org", None),
    ("Podscribe (podcast ads)", "ad pixel", r"podscribe\.com", None),
    ("Spotify Ad Analytics", "ad pixel", r"pixel\.byspotify\.com|spotifyadanalytics", None),
    ("StackAdapt", "ad pixel", r"srv\.stackadapt\.com", None),
    # Attribution and deep links: how a web visit is tied to an app install
    ("AppsFlyer", "attribution / deep link", r"appsflyer\.com|onelink\.me", None),
    ("Branch", "attribution / deep link", r"branch\.io|app\.link\b|bnc\.lt", None),
    ("Adjust", "attribution / deep link", r"adjust\.com|adj\.st", None),
    ("Singular", "attribution / deep link", r"singular\.net|sng\.link", None),
    ("Kochava", "attribution / deep link", r"kochava\.com", None),
    ("Firebase Dynamic Links", "attribution / deep link", r"\.page\.link", None),
    # Affiliate and referral programs
    ("Impact", "affiliate / referral", r"impact\.com|impactradius|ojrq\.net|sjv\.io|pxf\.io", None),
    ("PartnerStack", "affiliate / referral", r"partnerstack\.com|partnerlinks\.io", None),
    ("Rewardful", "affiliate / referral", r"rewardful\.com|r\.wdfl\.co", None),
    ("FirstPromoter", "affiliate / referral", r"firstpromoter\.com", None),
    ("Tolt", "affiliate / referral", r"tolt\.io", None),
    ("CJ Affiliate", "affiliate / referral", r"emjcd\.com|cj\.com", None),
    ("Awin", "affiliate / referral", r"dwin1\.com|awin1\.com", None),
    ("ShareASale", "affiliate / referral", r"shareasale\.com", None),
    ("Refersion", "affiliate / referral", r"refersion\.com", None),
    ("ReferralCandy", "affiliate / referral", r"referralcandy\.com", None),
    ("Friendbuy", "affiliate / referral", r"friendbuy\.(com|io)", None),
    ("Viral Loops", "affiliate / referral", r"viral-loops\.com", None),
    ("ReferralHero", "affiliate / referral", r"referralhero\.com", None),
    # Experiments and personalization
    ("Optimizely", "A/B testing", r"optimizely\.com", None),
    ("VWO", "A/B testing", r"visualwebsiteoptimizer\.com|vwo\.com", None),
    ("GrowthBook", "A/B testing", r"growthbook\.io", None),
    ("Statsig", "A/B testing", r"statsig\.com|featuregates\.org|statsigapi\.net", None),
    ("LaunchDarkly", "A/B testing", r"launchdarkly\.com", None),
    ("Mutiny", "A/B testing", r"mutinycdn\.com|mutinyhq\.com", None),
    ("Intellimize", "A/B testing", r"intellimize\.co", None),
    ("Eppo", "A/B testing", r"geteppo\.com", None),
    # Lifecycle messaging, chat, and email capture
    ("Klaviyo", "lifecycle messaging", r"klaviyo\.com", None),
    ("Braze", "lifecycle messaging", r"braze\.com|appboycdn\.com|braze\.eu", None),
    ("Customer.io", "lifecycle messaging", r"customer\.io", None),
    ("Iterable", "lifecycle messaging", r"iterable\.com", None),
    ("OneSignal", "lifecycle messaging", r"onesignal\.com", None),
    ("HubSpot", "lifecycle messaging", r"hs-scripts\.com|hubspot\.com|hsforms\.(com|net)|hs-analytics\.net", None),
    ("Mailchimp", "lifecycle messaging", r"chimpstatic\.com|list-manage\.com", None),
    ("Kit (ConvertKit)", "lifecycle messaging", r"convertkit\.com|ck\.page|kit\.com", None),
    ("beehiiv", "lifecycle messaging", r"beehiiv\.com", None),
    ("Attentive", "lifecycle messaging", r"attn\.tv|attentivemobile\.com", None),
    ("Postscript", "lifecycle messaging", r"postscript\.io", None),
    ("Intercom", "support chat", r"intercom\.io|intercomcdn\.com", None),
    ("Zendesk", "support chat", r"zdassets\.com|zendesk\.com", None),
    ("Crisp", "support chat", r"crisp\.chat", None),
    ("Drift", "support chat", r"drift\.com|driftt\.com", None),
    ("Gorgias", "support chat", r"gorgias\.(chat|io)", None),
    # Payments, paywalls, and web-to-app funnels
    ("Stripe", "web checkout", r"js\.stripe\.com|checkout\.stripe\.com|m\.stripe\.network", None),
    ("Paddle", "web checkout", r"paddle\.com", None),
    ("RevenueCat", "subscriptions / paywall", r"revenuecat\.com|rev\.cat", None),
    ("Superwall", "subscriptions / paywall", r"superwall\.(com|me)", None),
    ("Adapty", "subscriptions / paywall", r"adapty\.io", None),
    ("Qonversion", "subscriptions / paywall", r"qonversion\.io", None),
    ("FunnelFox", "web-to-app funnel", r"funnelfox\.(com|io)|fnlfx\.com", None),
    ("Chargebee", "web checkout", r"chargebee\.com", None),
    ("Recurly", "web checkout", r"recurly\.com", None),
    ("Shopify", "web checkout", r"cdn\.shopify\.com|myshopify\.com", None),
    ("Typeform", "forms / quiz", r"typeform\.com", None),
    ("Tally", "forms / quiz", r"tally\.so", None),
    ("Heyflow", "forms / quiz", r"heyflow\.(app|co)", None),
    ("Involve.me", "forms / quiz", r"involve\.me", None),
    # Consent, site builders, and media
    ("OneTrust", "consent", r"cookielaw\.org|onetrust\.com", None),
    ("Cookiebot", "consent", r"cookiebot\.com", None),
    ("Osano", "consent", r"osano\.com", None),
    ("Usercentrics", "consent", r"usercentrics\.eu", None),
    ("Termly", "consent", r"termly\.io", None),
    ("Webflow", "site builder", r"website-files\.com|webflow\.(com|io)", None),
    ("Framer", "site builder", r"framerusercontent\.com|framer\.(com|website)", None),
    ("Wix", "site builder", r"wixstatic\.com|parastorage\.com", None),
    ("Squarespace", "site builder", r"squarespace(-cdn)?\.com", None),
    ("WordPress", "site builder", r"/wp-content/|/wp-includes/", None),
    ("Next.js", "site builder", r"/_next/static/", None),
    ("Contentful", "content platform", r"ctfassets\.net|contentful\.com", None),
    ("Sanity", "content platform", r"sanity\.io", None),
    ("imgix", "media", r"imgix\.net", None),
    ("Cloudinary", "media", r"cloudinary\.com", None),
    ("Mux", "media", r"mux\.com", None),
    ("Vimeo", "media", r"vimeo\.com|vimeocdn\.com", None),
    ("Wistia", "media", r"wistia\.(com|net)", None),
    ("YouTube embed", "media", r"youtube\.com/embed|youtube-nocookie\.com|ytimg\.com", None),
    ("Lottie", "media", r"lottiefiles\.com|/lottie[.-][a-z0-9.]*\.js|\.lottie$", None),
    ("Trustpilot", "reviews widget", r"trustpilot\.com", None),
    ("Linktree", "link in bio", r"linktr\.ee", None),
]

def _bounded(pattern: str) -> str:
    """Anchor a domain pattern at a host boundary, so `kit.com` never matches `toolkit.com`."""
    if pattern.startswith(("/", "\\.")):
        return pattern
    return r"(?<![a-z0-9-])(?:%s)" % pattern


# Patterns match the request's host and path only (a query string can name any site);
# id patterns read the whole URL.
_COMPILED = [(name, cat, re.compile(_bounded(host), re.I), re.compile(idre) if idre else None)
             for name, cat, host, idre in SIGNATURES]


def _host_path(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    return (parts.netloc + parts.path).lower()

# Inline-script snippets that name an id even when the request list does not.
INLINE_IDS = [
    ("Meta Pixel", r"fbq\(\s*['\"]init['\"]\s*,\s*['\"](\d{8,20})['\"]"),
    ("TikTok Pixel", r"ttq\.load\(\s*['\"]([A-Z0-9]{10,})['\"]"),
    ("Google Tag Manager", r"(GTM-[A-Z0-9]{4,})"),
    ("Google Analytics 4", r"['\"](G-[A-Z0-9]{6,})['\"]"),
    ("Google Ads", r"['\"](AW-\d{6,})['\"]"),
    ("Microsoft Clarity", r"clarity['\"]\s*,\s*['\"]script['\"]\s*,\s*['\"]([a-z0-9]{8,})['\"]"),
]


def urls_from_rea(evidence: dict):
    """Request URLs from an REA capture_browser_scenario result (CLI or MCP)."""
    result = evidence.get("normalized_result", evidence)
    items = ((result.get("events") or {}).get("items")) or []
    return [it["url"]["url"] for it in items
            if it.get("kind") == "request" and isinstance(it.get("url"), dict) and it["url"].get("url")]


def urls_from_har(har: dict):
    return [entry["request"]["url"] for entry in (har.get("log") or {}).get("entries", [])]


_SRC_RE = re.compile(r"""(?:src|href|data-src)\s*=\s*["']([^"']+)["']""", re.I)


def urls_from_html(html_text: str, base_url: str):
    return [urllib.parse.urljoin(base_url, m.group(1)) for m in _SRC_RE.finditer(html_text)]


def detect(urls, html_text: str = "", page: str = "", source: str = ""):
    """One row per tool found: name, category, ids, an example URL, and how many requests matched."""
    found = {}
    for url in urls:
        target = _host_path(url)
        for name, cat, host_re, id_re in _COMPILED:
            if host_re.search(target):
                row = found.setdefault(name, {"name": name, "category": cat, "ids": set(), "requests": 0,
                                              "example": url.split("?")[0][:300], "page": page, "source": source})
                row["requests"] += 1
                if id_re:
                    m = id_re.search(url)
                    if m:
                        row["ids"].add(next(g for g in m.groups() if g))
    for name, pattern in INLINE_IDS:
        for m in re.finditer(pattern, html_text or ""):
            cat = next(c for n, c, _h, _i in SIGNATURES if n == name)
            row = found.setdefault(name, {"name": name, "category": cat, "ids": set(), "requests": 0,
                                          "example": "inline script", "page": page, "source": source})
            row["ids"].add(m.group(1))
    rows = []
    for row in found.values():
        row["ids"] = " ".join(sorted(row["ids"]))
        rows.append(row)
    order = [s[1] for s in SIGNATURES]
    return sorted(rows, key=lambda r: (order.index(r["category"]), r["name"]))


def third_party_hosts(urls, first_party: str):
    """Hosts the page contacted that no signature names, for the agent to look up by hand."""
    first = first_party.lower().lstrip(".")
    first = first[4:] if first.startswith("www.") else first
    counts = {}
    for url in urls:
        host = urllib.parse.urlsplit(url).netloc.lower()
        target = _host_path(url)
        if not host or host == first or host.endswith("." + first) or any(
                host_re.search(target) for _n, _c, host_re, _i in _COMPILED):
            continue
        counts[host] = counts.get(host, 0) + 1
    return sorted(counts.items(), key=lambda kv: -kv[1])


def load_capture(path):
    with open(str(path), encoding="utf-8") as handle:
        data = json.load(handle)
    if "log" in data:
        return urls_from_har(data)
    return urls_from_rea(data)
