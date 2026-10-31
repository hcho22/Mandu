# Free sources: how each paid call upstream is replaced

Upstream `rea-growth` buys its data through treg's catalog, with a default cap of $3 a run.
This table maps each of its paid calls to the route gr0wth-teardown uses at no cost.
The robots.txt verdicts were read with `gt robots` on 2026-10-30, for this tool's product token and for `*`; re-check any that a run depends on, since sites change them.

| Upstream step and paid call | Free route here | robots.txt (2026-10-30) |
|---|---|---|
| 1. `treg.web.map`, `treg.web.extract` (site map and page reads) | `gt site map` (the sitemaps robots.txt lists), `gt read` | each target's own; Ladder allowed |
| 1. Handles from the site | `gt site handles` (links and JSON-LD `sameAs` on the home page) | the target's own |
| 2. `predictleads technology_detections` (pixels, analytics, A/B, referral) | `gt rea` (REA's headless Chrome records every request) and `gt stack` (a signature table of about 120 tools) | the start page's own |
| 2. `predictleads connections`, `news_events`, `financing_events` | WebSearch to find, then `gt read` each page cited; `gt mentions hn` (Hacker News Algolia API) | hn.algolia.com allows all (404) |
| 3. `dataforseo historical_rank_overview` (monthly traffic) | `gt appstore history`: monthly App Store ratings counts from Wayback Machine snapshots (JSON-LD `aggregateRating`) | web.archive.org allows all (404); apps.apple.com and itunes.apple.com `/us/app/` allowed |
| 3. `akta website-traffic` (traffic by channel) | Not available free; a Google Trends export hcho downloads by hand stands in for demand | trends.google.com `Disallow: /trends/explore?` |
| 4. `dataforseo ranked_keywords` (Google rankings) | `gt suggest` (Google autocomplete), the sitemap's families, WebSearch presence for buyer questions | suggestqueries.google.com allows all (404) |
| 4. App Store keyword ranks (not upstream; the channel that matters for an app) | The capture kit: hcho searches each term on his iPhone | itunes.apple.com `Disallow: /search*`; apps.apple.com `Disallow: */search?*` |
| 4. App Store chart position, subtitle, in-app purchases, versions (not upstream) | `gt appstore chart` and `gt appstore listing` (the live pages' server data); `gt appstore lookup` (iTunes lookup API) | apps.apple.com charts and app pages allowed; itunes.apple.com `/lookup` allowed |
| 4. `cloro chatgpt.scrape` (AI answers) | Optional: hcho pastes ChatGPT or Perplexity answers into `capture/ai-answers.md` | not read automatically |
| 5. `serpapi google.ads.transparency` | `gt ads google`: REA loads the Transparency Center and the creatives are read from its own SearchCreatives responses | adstransparency.google.com allows all (404) |
| 5. `scrapecreators facebook-adlibrary` | The capture kit opens Meta's Ad Library search | facebook.com `Disallow: /` |
| 5. `adyntel linkedin ads`, `anyapi tiktok ad_library_search` | The capture kit opens LinkedIn's and TikTok's ad libraries | linkedin.com `Disallow: /`; library.tiktok.com `Disallow: /ads` |
| 5. Apple Search Ads (not upstream) | The capture kit opens Apple's Ad Repository (EU ads) | adrepository.apple.com `Disallow: /` |
| 6. `anyapi x.search.posts`, `scrapecreators reddit.search` | The capture kit's X and Reddit searches | x.com and reddit.com `Disallow: /` |
| 6. `anyapi youtube.search` | WebSearch, then `gt read` | as each page allows |
| 7. YouTube channel videos | `gt social youtube`: the YouTube Data API when `YOUTUBE_API_KEY` is set (free quota), else the channel's public Videos and Shorts tabs (rounded counts) | youtube.com `/@handle/videos` allowed; `/feeds/` and `/youtubei/` refused, so neither is read |
| 7. `crawl4ai tiktok.user.videos` | `gt social tiktok` reads the profile's totals; per-video plays come from the capture kit, because TikTok serves its video list only to a full browser session and returned an empty body to REA's headless one | tiktok.com profile pages allowed |
| 7. `scrapecreators instagram.user.posts` | The capture kit (the Reels tab shows play counts) | instagram.com answers its robots.txt with an HTML page, which the gate treats as a refusal |
| 7. `anyapi x.user.posts.timeline`, `harvestapi linkedin.company.posts` | The capture kit | refused (above) |
| 7. Bluesky (not upstream) | `gt social bluesky` (the public AppView API) | public.api.bsky.app `Allow: /` |
| 7. Image reads | Free: the agent opens the downloaded thumbnails, covers, and screenshots | i.ytimg.com allowed; is1-ssl.mzstatic.com allows all (403); tpc.googlesyndication.com allows all (404) |
| 8. `dataforseo backlinks.summary`, `anchors.list` (product loops) | Universal-link paths (`gt site aasa`), the sitemap's public-profile families, the stack's referral tools, and WebSearch for loop phrases, then `gt read` | the target's own |
| 9. `predictleads job_openings` | `gt jobs` (Greenhouse, Lever, and Ashby public board APIs), or `gt read` the careers page | boards-api.greenhouse.io allowed; api.lever.co `Allow: /`; api.ashbyhq.com allows all (401) |
| 10-13. Python analysis and the report | `gt analyze`, `gt render`, `gt check` | no reads |

## What the free routes cannot see

- Traffic by channel, Google keyword volumes, and backlink counts have no free source; the playbook says "not available at $0" instead of estimating them.
- Apple's review feed is refused (`Disallow: /*/rss/*`), so review counts by month are not used; the ratings total from archived listing pages is.
- The Wayback Machine has gaps: a month without a snapshot is missing, not zero, and the growth math only uses months it has.
- Upstream's `amp-api.apps.apple.com` style routes (an undocumented API whose robots.txt answers 404, used with a token taken from Apple's web page) are a way around Apple's refusal of search on its own hosts, so they are not used.
