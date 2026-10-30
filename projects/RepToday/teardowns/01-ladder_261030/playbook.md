# Ladder growth teardown for Rep Today

Target: LADDER Strength Training Plans (App Store id 1502936453, joinladder.com), read on 2026-10-30.
Product: Rep Today, pre-launch, inside gr0wthlab's posting window 1 until 2026-11-08.
Every count below is dated in the run's data files.
A finding is labeled seen when a file or page this run read shows it, and inferred when it is reasoned from what was seen.

## The short version

- SEEN Ladder's App Store ratings went from 14,751 (2023-10) to 202,735 (2026-10), and it sits #6 in Health & Fitness Top Free on 2026-10-30 (data/appstore-history.csv, data/appstore-chart.json).
- SEEN Ratings per day stepped from about 175 (February to April 2026) to 412-537 (May to September 2026), the month after its Hilary Duff campaign launched on 2026-04-21 (data/growth.csv, [press release](https://www.joinladder.com/hilary/press-release)).
- SEEN The campaign's own words sell Rep Today's wedge: "I open the app, my workout is right there, I press play, and go." ([joinladder.com/hilary](https://www.joinladder.com/hilary)).
- SEEN Its longest-running Google search ads (321-340 days) repeat two lines, "Classes start Monday" and no credit card to start (img/ads-google/CR17193012179062751233.jpg, data/ads-google.csv).
- INFERRED Ladder grows on paid acquisition financed for it: a $90M go-to-market investment from General Catalyst's Customer Value strategy ([Orrick](https://www.orrick.com/en/News/2024/11/Strength-Training-App-Ladder-Raises-100-Million)), ad pixels for Meta, TikTok, Google, and AppLovin on every page (data/stack.csv), and about 200 Google creatives (data/ads-google-summary.json).
- First play this week: play 2, the App Store screenshot storyboard, because the on-device screenshots are already a submission blocker and cost nothing but time.

## When it grew

<!-- gt:growth-chart -->

- SEEN The ratings total grew slowly through 2021 (523 in 2021-01, 772 in 2021-05) and was 8,246 by 2023-05 (data/appstore-history.csv).
- SEEN The largest sustained step is May 2026: ratings per day averaged 174.64 over February to April 2026 and 461.58 over May to July 2026, 2.64 times as many (data/growth-summary.json).
- SEEN January 2026 is a one-month spike: 305.1 ratings per day against 111.12 in December 2025 and 178.61 in February 2026 (data/growth.csv).
- INFERRED The January spike is New Year demand plus a Google ad push (14 of the 40 creatives read were first shown 2026-01-24 to 2026-01-26, data/ads-google.csv); the data cannot separate the two.
- INFERRED Ratings are a proxy for installs, and Ladder asks for ratings in 16 of its last 25 release notes (data/appstore-versions.csv), so part of any jump can be the asking rather than new users.

## The path

| Stage | What Ladder does | Evidence |
|---|---|---|
| Get noticed | Google search ads on brand and category lines, a celebrity campaign, out-of-home and stunt media, a TikTok account of 49,500 followers | SEEN data/ads-google.csv, [press release](https://www.joinladder.com/hilary/press-release), [Marketing Brew](https://www.marketingbrew.com/stories/hilary-duff-cash-cab-and-branded-newspapers-how-ladder-is-communicating-stronger-not-smaller-to-women), data/tiktok-profile.json |
| Install | Listing promises "GET STRONGER, WITH A PLAN." over awards laurels; subtitle "Fitness Workouts at Home & Gym" | SEEN img/appstore/01.png, data/appstore-listing.json |
| Sign up | Every web button says "Find your plan" and leads to a team quiz at /quiz; the quiz page loads no ad pixel before an answer | SEEN [home](https://www.joinladder.com/), data/stack-pages.csv |
| First run | A coach-written plan for the week, "Know exactly what WORKOUT to do, eVERY day"; the weekly plan drops Sunday 9 AM local | SEEN data/pages/home.txt, data/appstore-versions.csv (4.13.1) |
| Pay | 7-day free trial, "No payment info collected until AFTER your trial ends", then $29.99 a month or $179.99 a year; the App Store lists nine purchase options up to $479.99 a year | SEEN [pricing](https://www.joinladder.com/pricing), data/appstore-listing.json |
| Share | Team chat, Ladder for Groups, a merch shop, and universal links on every web path except /stripe/* and a shop claim page | SEEN data/site-urls.csv, data/aasa.json |

## Plays

### 1. Make the ready-on-open moment the hook

- **Stage:** next posting window (after 2026-11-08), as a proposal through gr0wthlab's Review Queue
- **Evidence:** SEEN Ladder's biggest campaign leads with the exact moment Rep Today is built on: open the app, the workout is there, press play ([joinladder.com/hilary](https://www.joinladder.com/hilary)); SEEN the cluster around its launch (2026-04-11 to 2026-05-15) carries the largest lift in ratings per day, 162.2 or 91.7% (data/moves-vs-growth.csv). INFERRED the promise of no decision at workout time is what the market pays to hear, and Rep Today can show it literally in a screen recording.
- **Effort:** day
- **First result:** 14 days - saves per post against the window-1 average, from gr0wthlab's Weekly Read
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md and the current Angles and Hooks in projects/RepToday/gtm/.
Draft five Hook proposals for the next posting window, each built on one moment: the app opens and a full session is already on screen with one Start button.
Each Hook is a text-only line for a screen recording of opening Rep Today, under 9 words, identity-framed, no streaks, no health claims, no competitor or celebrity named.
Write them to projects/RepToday/teardowns/01-ladder_261030/plays/01-ready-on-open/hooks.md with one sentence each on why it fits the brief.
Do not change the package, post anything, or touch gr0wthlab; hcho raises the proposal himself.
```

### 2. Storyboard the ten App Store screenshots

- **Stage:** pre-submission (on-device screenshots are an open submission item)
- **Evidence:** SEEN Ladder's ten screenshots use one system: the first two form one panorama carrying the whole promise and two awards; each other screenshot has a 3-4 word capitalized headline over real app UI ("A PLAN FOR EVERY WORKOUT", "GET COACHED THROUGH IT ALL") on white, with a dark #0e0e0e UI and one neon accent, #e6ff01 (img/appstore/01.png to img/appstore/10.png, colors read by code). SEEN the line "Get Coached Through It All" also heads a Google ad that ran 175 days (data/ads-google.csv). INFERRED one message carried from search ad to screenshot to app.
- **Effort:** week
- **First result:** 14 days after the listing goes live - App Store product page conversion rate in App Store Connect
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md and projects/RepToday/gtm/02-brand/brand-guidelines.md.
Storyboard ten App Store screenshots for Rep Today: screenshots 1 and 2 carry the whole promise (opens to a ready workout, free, no account) as one continuous panel; screenshots 3 to 10 each pair one 3-4 word headline with one real screen (the ready session, the duration chip, a mid-session swap, the Consistency Score, a Return after a gap, mobility, offline, Apple Health).
For each, give the headline, the exact screen and state to capture on device, and the brand color for the panel; no awards, ratings, or user counts, since Rep Today has none.
Write it to projects/RepToday/teardowns/01-ladder_261030/plays/02-screenshots/storyboard.md.
Do not submit or change anything in App Store Connect.
```

### 3. Choose the subtitle from search language and date every change

- **Stage:** pre-submission, then every release
- **Evidence:** SEEN Ladder's subtitle changed three times: "A new digital fitness movement" (2020-07 to 2021-05), "Future of personal training" (2023-05), "Fitness, Workouts, Coaching" (2023-10 to 2026-10-01), and "Fitness Workouts at Home & Gym" on 2026-10-30 (data/appstore-history.csv, data/appstore-listing.json). INFERRED it moved from a slogan to search words, and the newest adds where people train.
- **Effort:** day
- **First result:** 14 days after launch - rank for five chosen terms, checked by hand on an iPhone (capture/appstore-terms.md)
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md, projects/RepToday/gtm/01-research/aso-landscape.md, and projects/RepToday/teardowns/01-ladder_261030/data/suggest.csv.
Propose three subtitle options (30 characters or fewer) and one 100-character keyword field for Rep Today, each keeping "opens to a ready workout" true and using words people type (home workout, no equipment, quick, short).
Explain each choice in one line and name the five terms to check by hand 14 days after launch.
Write to projects/RepToday/teardowns/01-ladder_261030/plays/03-subtitle/options.md; the listing name and subtitle stay hcho's decision.
```

### 4. Say "free, no account" where Ladder says "no credit card"

- **Stage:** landing page and waitlist now; App Store copy at submission
- **Evidence:** SEEN "No Credit Card To Start" on Ladder's home page and "No payment info collected until AFTER your trial ends" on its pricing page ([home](https://www.joinladder.com/), [pricing](https://www.joinladder.com/pricing)); SEEN 3 of its 10 longest-running Google ads say no card or risk-free, and none of the 5 newest do (img/ads-google/CR17193012179062751233.jpg, img/ads-google/CR09944342710498361345.jpg, img/ads-google/CR01635720367488106497.jpg). INFERRED removing the payment fear is the line that kept earning its ad spend.
- **Effort:** day
- **First result:** 14 days - waitlist sign-up rate on reptoday.app
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md.
Rep Today's strongest friction remover is stronger than "no card": unlimited workouts are free forever and the app works without an account.
Draft three versions of a one-line reassurance for the landing page hero and the waitlist button, each literally true to the brief, no exclamation marks, no em dashes.
Write to projects/RepToday/teardowns/01-ladder_261030/plays/04-free-no-account/lines.md, and list which current page lines each would replace.
Do not publish or deploy the site.
```

### 5. Ask for ratings after a finished session, and in every release note

- **Stage:** launch build and every release
- **Evidence:** SEEN 16 of Ladder's last 25 release notes end with a request to rate and review, and it shipped 25 releases in 213 days, 3.5 every 30 days (data/appstore-versions.csv). SEEN its ratings reached 214,770 at 4.95 stars (data/appstore.json). INFERRED steady asking, at a steady release pace, compounds into the ratings count that ranks and sells the listing.
- **Effort:** week
- **First result:** 30 days after launch - ratings per 100 installs in App Store Connect
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md.
Write a one-page proposal for asking for an App Store rating: the trigger (the system review prompt after a completed session, at most as often as Apple allows, never after a hard or abandoned session, never in the first session), and a two-line closing sentence for release notes in Rep Today's voice.
Write it to projects/RepToday/teardowns/01-ladder_261030/plays/05-ratings/proposal.md, as a product change for hcho to give firstmate; do not edit the app.
```

### 6. A weekly "this week" rhythm without streak pressure

- **Stage:** social now (as a proposal), product later
- **Evidence:** SEEN "Classes start Monday" or "Starts Monday" appears in 5 of Ladder's 10 longest-running Google ads and in none of its 5 newest (img/ads-google/CR15057180055782293505.jpg, data/ads-google.csv); SEEN its weekly plan drops Sunday 9 AM local (data/appstore-versions.csv, 4.13.1). INFERRED a fresh-start date gives a reason to begin now. Ad age is a confound: the newest ads have had 17-47 days.
- **Effort:** day
- **First result:** 14 days - saves on Sunday and Monday posts against other days
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md, especially the Consistency Score and Return rules.
Draft four post ideas for a Sunday-evening or Monday-morning slot that frame the week as a fresh start without streaks, loss, or shame: showing up for 5 minutes counts, a Return is celebrated.
Write to projects/RepToday/teardowns/01-ladder_261030/plays/06-weekly-rhythm/ideas.md as a proposal for the next window.
Do not post or change the package.
```

### 7. Publish a free sample session on the web

- **Stage:** after launch
- **Evidence:** SEEN Ladder's site links "Free Workout Of The Day" from every page and lists /app/workout/today in its sitemap (data/pages/home.txt, data/site-urls.csv). INFERRED a free daily page gives search and shares a reason to land before the install.
- **Effort:** week
- **First result:** 14 days - visits to the page and taps through to the App Store
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md and the site source in projects/RepToday/gtm/03-site/.
Spec a static "today's 10-minute session" page for reptoday.app: one bodyweight session from the movement library, shown as the app would show it, with the honest note that the app builds a new one on your phone every day, offline.
Write the spec and the page copy to projects/RepToday/teardowns/01-ladder_261030/plays/07-sample-session/spec.md; do not deploy.
```

### 8. Put the app one tap away on every web page

- **Stage:** at launch
- **Evidence:** SEEN Ladder's apple-app-site-association file hands every web path to the app ("/*"), excludes only checkout, sign-in, and a shop claim page, and turns off the Smart App Banner only on support pages (data/aasa.json). INFERRED any web visit becomes an app open or an App Store visit.
- **Effort:** day
- **First result:** 14 days - App Store page views from web referrers in App Store Connect
- **Cost:** $0

```prompt
In Mandu, for RepToday: read the site source in projects/RepToday/gtm/03-site/.
Write the exact changes for launch day: the Smart App Banner meta tag with Rep Today's App Store id, and an apple-app-site-association file for reptoday.app that opens the app for every path except the privacy policy.
Write them to projects/RepToday/teardowns/01-ladder_261030/plays/08-app-banner/changes.md; do not deploy before the app is live.
```

### 9. Speak to the tired parent in their own search words

- **Stage:** next posting window and the landing page
- **Evidence:** SEEN Ladder's campaign frames its buyer as a busy parent with no mental space to plan a workout ([joinladder.com/hilary](https://www.joinladder.com/hilary)); SEEN Google autocomplete for "strength training app" returns "for women over 40", "for women over 50", "for beginners", and "free" (data/suggest.csv). INFERRED the audience Rep Today's brief already names (a tired parent at 9pm) is the one Ladder pays the most to reach.
- **Effort:** day
- **First result:** 14 days - saves and profile visits on parent-framed posts against the rest
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md and projects/RepToday/teardowns/01-ladder_261030/data/suggest.csv.
Draft six short lines for a busy parent at 9pm, built from the search phrases (beginners, free, short, at home), each true to the brief: 5 minutes counts, no equipment, nothing to decide.
Write to projects/RepToday/teardowns/01-ladder_261030/plays/09-tired-parent/lines.md as a proposal for the next window; no ages, bodies, or weight promises.
```

### 10. Nominate the app for featuring and the best-of lists

- **Stage:** at submission and launch
- **Evidence:** SEEN Ladder's first screenshot spends half its space on two 2024 awards, Women's Health "Best Strength Training Program" and CNET "Best Strength Training App" (img/appstore/01.png); SEEN its search ads cite being an Apple App of the Year finalist (img/ads-google/CR09944342710498361345.jpg). INFERRED third-party praise does the persuading a new app cannot do for itself.
- **Effort:** day
- **First result:** 30 days - any feature or list inclusion
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md.
Draft the text for Apple's featuring nomination in App Store Connect (what is new, who it is for, why now) and a short pitch for editors of "best workout apps" lists, both strictly factual: pre-launch, free core, offline, no account.
Write to projects/RepToday/teardowns/01-ladder_261030/plays/10-featuring/drafts.md; hcho submits them himself.
```

## Paid plays (not at $0)

### 11. Google search ads on category lines

- **Stage:** after launch, only if the organic numbers justify spend
- **Evidence:** SEEN 31 of the 40 Google creatives read ran 60 days or more, the oldest since 2025-11-25 (data/ads-google.csv); SEEN the cluster around its first long-running ads shows a lift of 42.73 ratings per day, 31.5% (data/moves-vs-growth.csv), INFERRED partly January demand.
- **Effort:** week
- **First result:** 14 days - cost per install
- **Cost:** paid per click; not estimated here

```prompt
In Mandu, for RepToday: draft a search ad test plan with three ad groups (quick workout, home workout, no equipment), two headlines each built on "opens to a ready workout" and "free, no account", and a daily cap hcho sets.
Write to projects/RepToday/teardowns/01-ladder_261030/plays/11-search-ads/plan.md; do not create an ads account or spend.
```

## Things to skip

- Coach-led teams, team chat, and named programs: Rep Today is not coaching and has no social features (product-facts brief), so the format does not transfer.
- Badges and streaks: Ladder said in 2023 that it uses "gamification elements like badges and streaks" ([pulse2](https://pulse2.com/ladder-12-million-funding/)); Rep Today forbids both.
- A celebrity partnership and stunt media: SEEN they line up with Ladder's largest lift ([press release](https://www.joinladder.com/hilary/press-release), data/moves-vs-growth.csv), but they cost money, and the lift cluster also holds new Google ads and a product release, so the celebrity's share is not separable.
- The nine-option price ladder: Ladder's in-app purchases run from $29.99 a month to $479.99 a year (data/appstore-listing.json); Rep Today's price is hcho's decision and its free core is the point.

## Timeline

| Date | Channel | Move | Lift in ratings per day (2 months before against the month of and 2 after) |
|---|---|---|---|
| 2020-06-23 | product | App Store release (data/appstore.json) | not enough data |
| 2023-05-10 | aso | Subtitle "Future of personal training" first seen (data/appstore-history.csv) | not enough data |
| 2023-10-10 | aso | Subtitle "Fitness, Workouts, Coaching" first seen (data/appstore-history.csv) | not enough data |
| 2023-12-19 | funding | $12M Series A reported, over 50,000 paying members ([pulse2](https://pulse2.com/ladder-12-million-funding/)) | not enough data |
| 2024-11-22 | funding | $15M Series B and $90M go-to-market investment ([Orrick](https://www.orrick.com/en/News/2024/11/Strength-Training-App-Ladder-Raises-100-Million)) | +25.67 (25.5%) |
| 2025-11-25 | ads | Google search ads that ran 321-340 days first shown (data/ads-google.csv) | +42.73 (31.5%) |
| 2026-01-24 | ads | 14 Google creatives first shown in three days (data/ads-google.csv) | +104.93 (91.5%) |
| 2026-04-11 to 2026-05-15 | ads, celebrity, offline, product | Widgets release, Hilary Duff launch and its Google ads, Miami Swim Week out-of-home (data/moves.csv) | +162.2 (91.7%) |
| 2026-08-05 to 2026-08-29 | hiring, product | Two Brand Social roles posted, flexible weekly plan released (data/jobs.csv) | +1.99 (0.4%) |
| 2026-10-30 | aso | Subtitle "Fitness Workouts at Home & Gym" seen (data/appstore-listing.json) | too recent |

Lifts are SEEN as numbers from data/moves-vs-growth.csv; that a move caused its lift is INFERRED, because the data is monthly, moves overlap, and January is New Year season.
No channel has enough dated moves for a correlation (data/moves-correlation.csv).

## By channel

### App Store listing

<!-- gt:gallery dir=img/appstore limit=10 -->

- SEEN #6 in Health & Fitness Top Free on 2026-10-30, between Yuka and Cal AI (data/appstore-chart.csv).
- SEEN House style: heavy capitalized headlines of 3-4 words, white panels, a dark #0e0e0e UI, and one neon accent, #e6ff01, read by code from img/appstore/01.png and img/appstore/03.png.
- SEEN Formula: "[VERB] [WHAT] [FOR WHOM OR HOW]", such as "GET COACHED THROUGH IT ALL" and "FIND THE PERFECT PLAN FOR YOU" (img/appstore/04.png, img/appstore/05.png).
- SEEN Version cadence of 3.5 releases every 30 days, 16 of 25 notes ending with a rating request (data/appstore-versions.csv).

### Google search ads

<!-- gt:contact-sheet channel=ads source=ads-google metric=days_shown -->

- SEEN About 200 creatives shown for joinladder.com in the US, 40 read: 39 text ads and 1 video, all under the advertiser name "MILTON FINCH, INC." (data/ads-google-summary.json, data/ads-google.csv).
- SEEN Pattern, 10 longest-running against the 5 newest: "Monday" in 5 against 0, "Hilary Duff" in 5 against 0, no card or risk-free in 3 against 0 (images in img/ads-google/, tiered by days shown).
- SEEN Formula: "[Join or Start] Ladder - [Daily Workout Plans or Find Your Perfect Plan] - [Classes Start Monday or Start Your Trial]" (img/ads-google/CR15057180055782293505.jpg).
- INFERRED The newest ads are generic ("Ladder Workout App"), which reads as new tests; their short run is age, not proof they lost.

### Site, funnel, and growth stack

- SEEN Every call to action is "Find your plan", leading to a quiz page that loads only Ladder's own files and Sentry before an answer (data/pages/home.txt, data/stack-pages.csv).
- SEEN Tools on the home and pricing pages: Google Tag Manager GTM-NWJCL3B, Google Analytics 4, Segment, Sentry, and ad pixels for Meta (2 ids), TikTok, Google Ads (AW-10851135234), Floodlight, Google remarketing, and AppLovin Axon (data/stack.csv).
- INFERRED The AppLovin Axon pixel means Ladder measures web visits for AppLovin's ad network, a channel most fitness apps do not run.
- Not read: what the quiz asks and where it ends, because that needs answering a form.

### TikTok

- SEEN @joinladder has 49,500 followers, 626,900 likes, and 345 videos, with a Linktree in its bio (data/tiktok-profile.json).
- Not captured: per-video plays and covers; TikTok served its video list only to a full browser (capture/CHECKLIST.md, step 1).

### Instagram, X, LinkedIn, Facebook, Reddit, and the other ad libraries

- SEEN Ladder links Instagram, X, LinkedIn, and Facebook from its home page (data/handles.csv).
- Not captured: their posts, Meta's, TikTok's, and LinkedIn's ad libraries, Apple's Ad Repository, Reddit, Google Trends, and App Store search ranks, which all refuse automated readers; capture/CHECKLIST.md lists each step.

### PR, celebrity, and offline

- SEEN 2026-04-21: "Hilary Duff Trains on Ladder", Ladder's first celebrity partnership; Ladder reported 400,000 members, 80% women ([press release](https://www.joinladder.com/hilary/press-release)).
- SEEN May 2026: out-of-home ads and branded zines at Miami Swim Week, and a "Ladder Quiz Cab" with the host of Cash Cab, as reported by [Marketing Brew](https://www.marketingbrew.com/stories/hilary-duff-cash-cab-and-branded-newspapers-how-ladder-is-communicating-stronger-not-smaller-to-women) on 2026-07-21.

### Hiring

- SEEN Both open roles are in brand social, "Senior Manager, Brand Social" and "Lead Creator, Brand Social", posted 2026-08-05 (data/jobs.csv).
- INFERRED Ladder is moving organic social content in-house next, the channel Rep Today's test already uses.

## 14-day plan

Days 1-14 run 2026-11-09 to 2026-11-22, after window 1 ends, so nothing changes during a posting window.

1. Days 1-2, App Store: run play 2's storyboard and capture the ten screens on device.
   Number on day 14: all ten screenshots exist at the required sizes.
2. Days 3-4, App Store: pick the subtitle and keyword field (play 3).
   Number on day 14: one subtitle chosen, with five terms to check after launch.
3. Days 5-6, web: ship the "free, no account" line on reptoday.app (play 4) after hcho approves it.
   Number on day 14: waitlist sign-up rate against the 2026-10-26 baseline of 0 sign-ups.
4. Days 7-8, social: hcho raises plays 1, 6, and 9 as proposals through gr0wthlab's Review Queue for window 2.
   Number on day 14: the proposals decided on the sitting page.
5. Days 9-14, product: hand plays 5 and 8 to firstmate as launch-build changes if hcho approves them.
   Number on day 14: both in the build's task list.

## Method notes

- Reads: 116 logged in sources.csv on 2026-10-30 (106 answered 200; 4 were 308 redirects followed hop by hop; 2 were BusinessWire pages that answered 403 and were replaced by other reports of the same news; 3 were 404s; 1 Wayback 429 was retried later from a fresh request).
- robots.txt refused, so not read: Apple's review feed and App Store search, Instagram, X, LinkedIn, Reddit, Facebook's Ad Library, TikTok's Ad Library, Apple's Ad Repository, and Google Trends' explore page (references/free-sources.md in the skill).
- Captures not taken: every step in capture/CHECKLIST.md; the channels they cover are marked not captured above.
- Images read: the 10 App Store screenshots and 15 of the 39 Google ad previews (the 10 longest-running and the 5 newest); colors were read by code, not by eye.
- Counts are as of 2026-10-30 except the archived App Store pages, each dated in data/appstore-history.csv.
- Every "reported" number (members, women, growth) is Ladder's own claim in a press release or interview.
- The INFERRED lines above are interpretations, not findings.
- $0 spent: no paid tool, account, sign-up, or form.
- No affiliation with Ladder Technologies, Inc.
