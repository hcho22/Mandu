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
