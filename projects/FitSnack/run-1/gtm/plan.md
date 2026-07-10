# Nonzero: Go-To-Market Plan (run-1)

Written 2026-07-09. Inputs: `positioning.md` (tournament winner), `../research/pricing.md` (locked pricing), `../research/discovery-demand.md` (channel evidence), `../research/market-channels.md` (case studies), `../naming/decision.md` (name).
Every market number cites a fetched source in `../research/`; strategy choices are labeled as the calls they are.

## The one-paragraph plan

Nonzero launches as a build-in-public solo-founder iOS app riding a verified content wave it does not depend on.
Positioning leads with the Ready Screen ("Open the app. Your workout is already there."), beat two is the Consistency Score ("A score that dents. Never zeroes.").
Primary acquisition is short-form video (TikTok/Reels/Shorts) where the exercise-snacking trend's 122M+ views actually live, amplified by build-in-public on X - the only channel pair with verified indie case studies (Habit Pixel $0->$1K MRR; HabitKit $15K/mo).
ASO is a deliberate secondary: own "exercise snacks" in the subtitle as a cheap call option on the trend converting to search, target "micro workout" / "desk workout" in the keyword field, and do not fight Seven for "7 minute workout."
Monetization is freemium with the core loop free forever: $9.99/mo, $59.99/yr, 14-day trial, paywall on adaptivity depth + variety + analytics.
Apple featuring is the aspirational channel the product is deliberately shaped for (native SwiftUI, HealthKit, a distinctive philosophy - the exact profile of Gentler Streak's featuring run).

## 1. The wedge, restated as a GTM asset

The product IS the ad. The entire positioning is verifiable in a single screenshot or a 3-second screen recording: app opens -> a complete session is there -> one tap -> moving.
That collapses creative production cost to near zero and makes every surface (App Store screenshot #1, TikTok hook, X demo clip, landing hero) the same asset.
No competitor can run this creative honestly: Seven opens on a questionnaire, Wakeout on a vibe-picker, Fitbod on equipment config (verified in `../research/competitors-micro.md`).

## 2. Channels, ranked by evidence

### Primary: short-form video (TikTok, Reels, Shorts)

- The demand is verified there: 122M+ views of snack-workout content, avg ~2.6M views/video (Virlo.ai via Forbes, Apr 2026 - MEDIUM confidence, phrase as cross-platform views).
- The discovery research shows this attention does NOT yet flow into App Store search - so the channel must carry the install directly (link-in-bio, App Store card), not just awareness.
- Creative system (three repeatable formats, all derived from the wedge):
  1. **The Open** - screen recording: open Nonzero, session is there, start moving. Text overlay: "No quiz. No browsing. Start." 5-15s.
  2. **The Dent** - the Consistency Score simulator: "I missed Tuesday. Here's what happened to my score vs my old streak." Emotional core for the streak-burned.
  3. **Build-in-public** - the founder shows the engine, the no-streak decision, the "things I refuse to add" list. Feeds X and TikTok simultaneously.
- Cadence (solo-founder realistic, per the prior social plan): 1 video/day produced once, repurposed thrice (TikTok -> Reel -> Short).

### Primary (paired): build-in-public on X + the waitlist

- The only channel with two verified indie case studies with numbers (`../research/market-channels.md`): Habit Pixel (launch day did little; sustained build-in-public compounded to $1K+ MRR in 8 months), HabitKit/Sebastian Rohl ($15K/mo; X was "my main channel").
- hcho already runs this motion for Agentic RAG; the marginal cost is a second content lane, not a new skill.
- Every post drives to one mechanic: the early-access waitlist (one-field page, per-platform tagged links `?src=x|tt|ig`). Success metric pre-launch: signups, not views.

### Secondary: ASO as a call option

- Verified keyword reality (`../research/discovery-demand.md`): "7 minute workout" and "home workout" are locked by incumbents with 117k-530k ratings; "exercise snacks" has near-zero typed volume but a beatable results page (current #1 has 6 ratings).
- Listing strategy: **Name:** "Nonzero: Micro Workouts". **Subtitle:** "Exercise snacks, no streaks" (owns the trend term + the differentiator). **Keyword field:** micro workout, desk workout, 5 minute workout, quick workout, no equipment.
- Expectation set honestly: ASO is not the growth engine at launch; it is cheap insurance that pays off only if the trend converts to search. Re-evaluate quarterly.

### Ignition: Reddit + the communities that already speak the language

- r/NonZeroDay is the name's native habitat; also r/getdisciplined, r/bodyweightfitness, r/AppleWatch streak-grief threads (the win-back copy targets these: "You did not lose the habit. The counter did.").
- Reddit worked as the ignition step in the Habit Pixel case study. Rules: participate, don't blast; share the build story, not the pitch. (This run publishes nothing; this is the plan for launch.)

### Aspirational: Apple featuring

- The Gentler Streak precedent is exact (`../research/market-channels.md`): 8-person indie, native SwiftUI + HealthKit + distinctive philosophy -> Apple Watch App of the Year, Apple Design Award, Behind the Design editorial.
- Nonzero is deliberately the same shape: Apple-native stack, offline deterministic engine, accessibility-first, a philosophy Apple's editorial team can write about ("the app that refuses to guilt you").
- Action: submit to App Store editorial (featuring nomination form) at launch and at each marquee release; design award submission once the design system matures.

### Deprioritized: Product Hunt

- Verified weak for consumer apps in 2025-26 (founder reports of 100-200 hours for near-zero durable return; the audience is founders, not fitness consumers). A launch-day post is fine as a backlink; zero hours beyond that.

## 3. Launch sequence (from today's state: Epics A-I built, UI shell J-N remaining)

| Stage | Gate | GTM motion |
|---|---|---|
| Now -> TestFlight | Epics J-M built (Ready Screen through Progress) | Stand up the waitlist page + link-in-bio; begin build-in-public lane 2 (the "no streaks" manifesto content); collect streak-grief receipts for launch creative |
| TestFlight beta | Epic N (Apple integrations) + StoreKit sandbox verified | Invite the waitlist in waves; instrument the trial window (day-5/7 value moment); recruit 10-20 vocal beta users from r/NonZeroDay + waitlist replies |
| App Store launch | Beta D7 retention signal >= category strong quartile (15-22%) | The Open + The Dent creative blitz; Reddit build-story posts; Apple featuring nomination; PH backlink post |
| Post-launch | 4 weeks of cohort data | Double down on whichever creative format drove installs; begin win-back track; quarterly ASO review |

The gate discipline matters: the category's measured kill zone is minute one through week one (activation 26% D1 -> 10% D28), so launch creative pushes people into a first session that must already be excellent.

## 4. Pricing (locked; full reconciliation in `../research/pricing.md`)

- **Free forever**: complete core loop - 5-60 min deterministic sessions, Consistency Score, basic history. NTC-proofing: a crippled free tier loses to a free default.
- **Premium $9.99/mo** (raised from planned $7.99: category median is $9.99; every verified competitor monthly is $8.99-12.99; $7.99 reads discount, not depth).
- **Annual $59.99/yr** (kept: mid-pack of the verified set $39.99-$79.99; the $9.99 monthly anchors it as "6 months free").
- **Trial 14 days** (kept: 10-16 day trials convert ~35.4%, on par with the category norm, and a consistency product needs two weeks to demonstrate value) with a day-5/7 milestone moment and a pre-renewal save flow (35% of annual cancellations land in Month 1; only ~5% of cancelled annual subscribers ever return).
- **Paywall**: AI Programmer adaptivity depth, variety/catalog, analytics depth - the exact set Seven and Gentler Streak successfully charge for. Never the core loop.
- **Planning basis**: 25-33% of annual payers renew into Year 2; ~57% monthly first renewal; H&F median trial-to-paid 37.7%; D35 download-to-paid 2.9% median / 6.2% top quartile.

## 5. Funnel math (planning ranges, all benchmark-anchored)

Assumptions: RevenueCat H&F medians (MEDIAN case) and top-quartile (STRONG case); blended $50 average annual revenue per payer given 68% annual mix at $59.99 and monthly churn at $9.99.

| Installs/mo | Payers by D35 (2.9% / 6.2%) | Monthly revenue run-rate added (~$50/payer-yr) |
|---|---|---|
| 1,000 | 29 / 62 | ~$1.5k / ~$3.1k annualized |
| 5,000 | 145 / 310 | ~$7.3k / ~$15.5k annualized |
| 10,000 | 290 / 620 | ~$14.5k / ~$31k annualized |

INFERENCE: these are benchmark multiplications, not forecasts. The honest read: at median execution Nonzero needs roughly 5-10k installs/month to matter as an income bet, which is why the channel plan leans on the one verified high-reach channel (short-form) rather than ASO.

## 6. What we are NOT doing, and why

- **Not leading with AI.** Commoditized ("AI coach" everywhere) and actively risky with this audience (Wakeout's users punished AI content). The Programmer stays invisible plumbing.
- **Not claiming longevity.** The science researcher's verdict: mortality evidence is vigorous-only; "longevity-first" over-claims. Format-level language only ("short, frequent movement counts - WHO dropped the 10-minute rule in 2020").
- **Not attacking streak lovers.** Streaks demonstrably retain while intact (Duolingo 3.6x). The anti-streak message is relief for the burned, run as a win-back/retargeting track, not the lead.
- **Not fighting Seven for "7 minute workout."** 136k ratings vs zero; the keyword is lost. Win the open ground ("exercise snacks", "no streak") and the feed.
- **Not Product Hunt as a strategy.** Evidence says it's a founder-audience channel now.

## 7. Risks this plan carries on purpose (red-team fodder)

1. Short-form reach is verified for the CONTENT trend, not for app-install conversion - no verified indie fitness app case study converts TikTok views to installs at known rates. The channel bet is evidence-informed, not evidence-proven.
2. The build-in-public case studies are habit apps (n=2, self-reported); the one fitness app in those stories (Liftbear) failed.
3. Solo-founder content cadence competes with hcho's Agentic RAG flagship for the same weekly hours; the plan assumes ~1 produced video/day is sustainable, which the prior social plan flags as the ceiling.
4. The wedge window: Freeletics, Google's Gemini coach, and Muscle Booster are each one product decision from the compound (`../research/competitor-holes.md`). Speed matters more than polish everywhere except the first session.

## 8. Red-team adjustments (2026-07-09, dispositions in `../redteam/objections.md`)

The plan above stands as written, and this section supersedes it where they conflict.

### 8.1 Corrected funnel math (R16, R27)

The section 5 table used $50/payer-yr; the package's own RevenueCat citation says H&F Year-1 realized LTV is **$35.64 median per payer**, and no commission line was included. Corrected, at the 15% App Store Small Business rate:

| Installs/mo | Payers by D35 (2.9% / 6.2%) | Year-1 revenue per cohort, net of 15% (~$30.29/payer) |
|---|---|---|
| 1,000 | 29 / 62 | ~$880 / ~$1.9k |
| 5,000 | 145 / 310 | ~$4.4k / ~$9.4k |
| 10,000 | 290 / 620 | ~$8.8k / ~$18.8k |

Cohorts are not recurring: 25-33% of annual payers renew into Year 2, so run-rate decays ~70% per cohort per year without new installs.
The honest restatement: **income-relevance needs roughly 10-20k installs/month sustained**, which exceeds every named entrant in the niche except the declining category leader.
Until the channel test (8.2) proves otherwise, Nonzero is a portfolio asset with revenue upside, not a second income pillar; that label change is surfaced to hcho for the priorities call.
A free-tier caveat applies on top: the 2.9% median comes from apps that convert by withholding; Nonzero's complete free tier should be planned below median until measured.

### 8.2 Top-of-funnel model and kill thresholds (R2, R18, R26)

Section 5 started at "installs/mo" with no mechanism. The channel hypothesis, stated falsifiably:

- Hypothesis: short-form demo content (the Ready Screen as the first frame) converts views to installs at a rate that makes 5k+ installs/month reachable within 6 months of launch.
- 30 days post-first-post: 20+ videos published, any video over 10k views, or restrategize the hook.
- 60 days: profile-to-store CTR measurable and above 1%; if unmeasurable or below, move spend of effort to the fallback.
- 90 days: 1,000+ cumulative installs attributable to short-form, or short-form is demoted to secondary.
- Fallback channel (pre-named): build-in-public X + ASO demand-term iteration + waitlist/win-back email. The install table becomes aspirational, and the bet is relabeled per 8.1.

### 8.3 Cadence and hours (R28)

Sustainable floor is **2-3 videos/week**, not 1/day; the daily blitz is reserved for launch week only, and the whole lane is sequenced behind the Agentic RAG validation milestone (first buyer interviews booked). Weekly budget: ~6 hours content, ~2 hours community. If FitSnack content hours collide with flagship validation hours in any week, the flagship wins by standing rule.

### 8.4 Mechanic validation gates (R1, R11, R12, R13)

- V1 (open-friction pain): instrument first-session drop-off from day one. If open-friction churn does not appear in our own funnel, the anti-streak win-back angle is pre-committed to take the lead.
- V2 (category demand): the 8.2 thresholds double as the demand test; "exercise snacks" is framing, not a channel.
- V3 (dent-score retention): instrument D7/D30 by mechanic exposure. If D7 underperforms category benchmarks, test a streak-with-repair variant instead of defending the pure no-streak line. The Score's data model must support that A/B without a rebuild.
- Mechanic-copy contract (R13): the shipping Score follows the prototype's per-day credit model (every miss dents), not a raw weekly bucket; US-H01 amendment recommended (per-day granularity, windowed floor). "Miss a day, your score dents" is only honest under that model.

### 8.5 Wedge falsification triggers (R6, R7, R8, R9)

Any of the following forces a positioning decision (not a quiet re-narrowing): Seven or another scaled incumbent ships a default ready-on-open session; Gentler Streak ships guided micro sessions; Google's coach adds a session player on its adaptive targets; a comprehension or demand test shows the compound wedge does not register with the lapsed-non-exerciser segment. Assume dent-parity from at least one scaled incumbent within 12 months. Gentler Streak sits on the live-threat watchlist with the counter-position: session-first for lapsed non-exercisers vs tracker-first for the already-active.

### 8.6 Smaller corrections

- Reddit is demoted from "ignition" to community listening and win-back copy research, behind a genuine participation runway and mod outreach (R29).
- Apple-featuring pitch angle is decision-removal (the Ready Screen), not "refuses to guilt you", which is Gentler Streak's already-written Apple story (R31).
- Launch pricing tactic: intro annual $44.99-49.99 until the Strength-Phase catalog ships, then step to the $59.99 list (R19). List price and the free/paid boundary spec are unchanged.
- First-50-reviews plan: beta wave asked at the moment of a completed week-two session via SKStoreReviewController; no review gating (R30).
- The pre-renewal save flow gets written under the voice contract (forgiveness with a spine), as a named copy deliverable (R20).
