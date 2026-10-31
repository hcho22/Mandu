"""The capture kit: what hcho opens in his own browser and saves into the run,
for the sources whose robots.txt refuses automated readers or that show their
numbers only to a signed-in visitor. Reading a page as a person and saving a
screenshot of it is how this skill reaches those sources at no cost.
"""

from __future__ import annotations

import urllib.parse
from pathlib import Path

import gt_ads
import gt_common as gc

CAPTURE_HELP = {
    "tiktok": ("Open the profile, wait for the grid, and screenshot it so every cover's play count shows; "
               "scroll and screenshot again until about 60 videos or 6 months are covered. "
               "Then open the 'Popular' tab and take one more screenshot."),
    "instagram": ("Open the Reels tab (it shows play counts) and screenshot until about 60 reels are covered; "
                  "then screenshot the main grid once for the house style. For a carousel that looks like a "
                  "winner, open it and screenshot the first and last slide."),
    "x": ("Open the profile and screenshot posts top to bottom so each one's text, views, and date show; "
          "about 60 posts or 6 months. Do the same for each founder account listed."),
    "linkedin": ("Open the company page's Posts tab and screenshot about 20 posts with their reactions; "
                 "note any post that says 'Promoted'."),
    "youtube": ("Only if the run could not read the channel: open the Videos tab, sort by Popular, and "
                "screenshot; then the Latest order."),
    "reddit": ("Open the search (it is sorted by top posts of the past year) and screenshot the first two "
               "screens; open the top 3 threads and save each one's address in captures.csv."),
}


def checklist(run: Path):
    meta = gc.load_run(run)
    name = meta.get("target", "")
    domain = meta.get("domain", "")
    handles = gc.read_csv(run / "data" / "handles.csv")
    have = {c: len(gc.read_csv(run / "data" / ("%s-posts.csv" % c))) for c in
            ("tiktok", "instagram", "x", "linkedin", "youtube", "reddit", "bluesky")}
    lines = ["# Capture checklist: %s" % name, "",
             "These sources refuse automated readers or show numbers only in a browser.",
             "Open each address in your own browser, take the screenshots described, and save them under",
             "`capture/<channel>/` as `01.png`, `02.png`, and so on.",
             "Add one row per screenshot to `capture/captures.csv` (file, channel, url, captured_at, notes).",
             "Skip anything you do not want to do; the report then says that channel was not captured.",
             "Nothing here needs an account, a purchase, or a message to anyone.", ""]
    step = 1
    by_network = {}
    for row in handles:
        by_network.setdefault(row["network"], []).append(row)
    for channel in ("tiktok", "instagram", "x", "linkedin", "youtube"):
        accounts = by_network.get(channel, [])
        if not accounts or (channel == "youtube" and have["youtube"]):
            continue
        for account in accounts:
            url = account["url"]
            if channel == "instagram":
                url = "https://www.instagram.com/%s/reels/" % account["handle"].strip("/")
            if channel == "linkedin":
                url = account["url"].rstrip("/") + "/posts/"
            lines += ["## %d. %s: %s" % (step, channel.title() if channel != "x" else "X", account["handle"]), "",
                      "- Open: %s" % url, "- Capture: %s" % CAPTURE_HELP[channel],
                      "- Save to: `capture/%s/`" % channel, ""]
            step += 1
    terms_file = run / "capture" / "appstore-terms.md"
    terms = [t.strip("-* ").strip() for t in terms_file.read_text(encoding="utf-8").splitlines()
             if t.strip("-* ").strip() and not t.startswith("#")] if terms_file.exists() else []
    lines += ["## %d. App Store search ranks" % step, "",
              "- Open: the App Store app on your iPhone (Apple refuses automated App Store search).",
              "- Capture: search each term below and screenshot the first screen of results.",
              "- Terms: %s" % ("; ".join(terms) if terms else "none listed yet in `capture/appstore-terms.md`"),
              "- Save to: `capture/appstore-search/`", ""]
    step += 1
    reddit = "https://www.reddit.com/search/?" + urllib.parse.urlencode({"q": name, "sort": "top", "t": "year"})
    lines += ["## %d. Reddit: posts that name %s" % (step, name), "", "- Open: %s" % reddit,
              "- Capture: %s" % CAPTURE_HELP["reddit"], "- Save to: `capture/reddit/`", ""]
    step += 1
    for key, label, url in gt_ads.manual_urls(name, domain):
        if key == "google-ads":
            continue
        lines += ["## %d. %s" % (step, label), "", "- Open: %s" % url,
                  "- Capture: the result count, then screenshot the ads in view (each shows its start date);"
                  " for Meta, sort or scan for the oldest ads still active, which are the long-running winners.",
                  "- Save to: `capture/%s/`" % key, ""]
        step += 1
    trends = "https://trends.google.com/trends/explore?" + urllib.parse.urlencode(
        {"date": "today 5-y", "geo": meta.get("country", "us").upper(), "q": name})
    lines += ["## %d. Google Trends: search interest in %s" % (step, name), "", "- Open: %s" % trends,
              "- Capture: click the download arrow on 'Interest over time' and save `multiTimeline.csv` into "
              "`capture/trends/`. It is the free stand-in for paid traffic history.",
              "- Save to: `capture/trends/multiTimeline.csv`", ""]
    step += 1
    lines += ["## %d. Optional: AI answers" % step, "",
              "- Ask ChatGPT or Perplexity the three buyer questions in `capture/ai-questions.md` and paste each "
              "answer, with the date, into `capture/ai-answers.md`.", ""]
    out = run / "capture" / "CHECKLIST.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    captures = run / gc.CAPTURES_NAME
    if not captures.exists():
        gc.write_csv(captures, [], gc.CAPTURES_FIELDS)
    return out, step
