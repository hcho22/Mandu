# The capture kit

Some sources refuse automated readers in robots.txt (Instagram, X, LinkedIn, Reddit, Meta's, TikTok's, and LinkedIn's ad libraries, Apple's Ad Repository, Google Trends, and App Store search), and TikTok shows per-video plays only to a full browser.
hcho reads those as a person, in his own browser or on his phone, and saves screenshots into the run.
That costs nothing and needs no account beyond what he already uses.
Every capture is optional; the report says "not captured" for any he skips.

## For hcho

1. Open `<run>/capture/CHECKLIST.md`; each step has the address to open and what to screenshot.
2. Save screenshots as `capture/<channel>/01.png`, `02.png`, and so on, with the counts and dates visible.
3. Add one row per screenshot to `capture/captures.csv`: `file, channel, url, captured_at, notes`.
   `url` is the page the screenshot shows, `captured_at` is the date (`2026-10-30`), and `notes` is anything not on screen, such as "Popular tab".
4. For Google Trends, save the exported `multiTimeline.csv` into `capture/trends/` as it downloads.
5. For App Store keyword ranks, search each term in `capture/appstore-terms.md` (the agent writes it) on an iPhone, screenshot the first screen of results, and save it under `capture/appstore-search/`.
6. Tell the session the captures are in.

## For the agent: transcribing captures

- Open each screenshot and write one row per visible post to `data/<channel>-posts.csv`, with the columns `gt` uses: `channel, kind, id, url, date, title, text, metric, image, source`.
- `metric` is the channel's engagement number: plays on TikTok and Instagram Reels, views on X and YouTube, likes plus comments on Instagram posts, reactions on LinkedIn, score on Reddit.
- `image` is the screenshot's path (`capture/tiktok/01.png`); `source` is `capture:<file>`.
- `id` is the post's address or, when the screenshot shows none, `<file>#<position>` (`capture/tiktok/01.png#3` for the third cover).
- `date` is the post's date when the screenshot shows it; a grid with no dates gets the dates of its first and last post from `notes`, and the rows between them are left blank rather than guessed.
- A number you cannot read is left blank, and the row still counts toward what was captured.
- App Store search screenshots go to `data/appstore-search.csv`: `term, position, app, is_target, captured_at, file`.
- Then run `gt analyze <run> rank <channel>`.

Captured numbers are SEEN, cited to their capture file.
