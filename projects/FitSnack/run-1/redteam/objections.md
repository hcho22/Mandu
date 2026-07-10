# Red team: objections and dispositions

2026-07-09.
Process: six adversarial skeptics attacked the package in parallel (pain/demand, moat, retention mechanic, pricing, name/brand, GTM realism), each instructed to attack the strongest form of every claim and to rest every objection on package files or the package's own cited market facts.
A seventh completeness critic swept the deliverables against `../master_prompt.md`.
Full unabridged attacks: `objections-raw.json` (38 objections).
Dispositions: **ACCEPT** (the objection stands; plan changed or consequence recorded), **MITIGATE** (partially stands; guardrail added), **REBUT** (does not survive contact with the evidence).

The one-paragraph honest summary: the red team did not kill the product, but it killed two comforts.
First, the income-bet framing: on the package's own benchmarks, achievable install volumes make Nonzero portfolio-plus-modest-revenue in 2026, not a second income pillar, unless the unproven short-form channel dramatically outperforms.
Second, any notion that the wedge is self-validating: the Ready Screen pain, the dent-score's retention power, and the category's demand are all explicit hypotheses now, each with an instrumentation plan and a kill criterion in `../gtm/plan.md` (Red-team adjustments section).

---

## Pain and demand

| # | Sev | Objection (compressed) | Disposition |
|---|---|---|---|
| R1 | HIGH | The winning positioning sits on the weakest pain leg: open-friction churn is one HN onboarding quote plus inference, while streak anxiety has five quotes, an experiment, and Duolingo's numbers. | **MITIGATE.** The Ready Screen stays the door because it is the only claim a stranger can verify in one screenshot, not because the pain evidence is strongest; positioning.md already flags the inference. Consequence added: validation gate V1 (instrument first-session drop-off from day one; if open-friction churn does not appear in our own funnel, the anti-streak angle is pre-committed to take the lead). |
| R2 | HIGH | "Exercise snacks" has no typed demand: autocomplete is supply keywords, every trend-named app is under 5k installs/month, Glimpse's top-20 excludes the format; the 122M-views stat is duration-keyword content, not category demand. | **ACCEPT.** The category label is a framing device, not a demand channel. Consequence: validation gate V2 (named top-of-funnel hypothesis with view/install kill thresholds), and the listing keeps "exercise snacks" only as the subtitle option with a demand-term fallback recorded. |
| R3 | MED | The thesis one-liner overclaims: measured churn reasons are interest-loss, free alternatives, and boredom, which Nonzero mostly does not fix; "two most-cited mechanisms" means most-cited in our curated quotes. | **ACCEPT.** thesis.md reworded to "two design-choice mechanisms with the strongest qualitative evidence"; boredom/variety noted as carried by the engine, unproven. |
| R4 | MED | Segment trajectory points down: Seven declined ~25% in downloads over eight months inside a growing market; the $3.4B tailwind is not this segment's. | **ACCEPT.** Added to the thesis counter-evidence ledger with the honest sizing anchor: Seven's ~$1M/yr US run rate is the realistic ceiling anchor, not the market size. |
| R5 | LOW | The single organic "I want an app for this" post in all of Reddit asked for reminders plus streaks, both things Nonzero rejects or omits. | **ACCEPT** as a targeting note: category-name seekers are not the audience; the streak-burned win-back track is. The comeback push notification (brand guidelines section 9) is the reminder-shaped answer, quiet by design. |

## Moat

| # | Sev | Objection | Disposition |
|---|---|---|---|
| R6 | HIGH | positioning.md's "five-year defensibility" contradicts thesis.md's "window, not a moat", and the cannibalization argument only covers gym-strength apps, not Seven, Google, or Gentler Streak. | **ACCEPT.** Correction #6 appended to positioning.md scoping the defensibility claim to questionnaire-funnel strength apps and adopting the window framing; the plan assumes Seven-class copying within quarters. |
| R7 | HIGH | The dent-score is a UI-layer metric; Duolingo proves forgiveness is routinely retrofitted onto streaks; nothing makes it hard to copy. | **ACCEPT.** The mechanic is uncopied, not uncopyable. The plan leans on speed, craft, and the compound (ready + forgiving + adaptive in one default posture); roadmap assumption recorded: dent-parity from at least one scaled incumbent within 12 months. |
| R8 | HIGH | The wedge already narrowed once under adversarial search (Dr. Muscle/BodBot); narrowing-on-contact is the signature of a thin wedge being managed. | **MITIGATE.** True as pattern; the reshaped wedge names a different person, not a capability. Consequence: falsification triggers written into gtm/plan.md (which competitor moves kill the wedge and force the pivot decision). |
| R9 | MED | "Credibility of holding the no-streak line" is owned by Gentler Streak (ADA 2024), not available to a zero-brand entrant. | **MITIGATE.** Dropped as a launch-day advantage; kept as a 24-month posture. Counter-position recorded: Nonzero is session-first for lapsed non-exercisers vs GS's tracker-first for the already-active. |
| R10 | MED | Empty ground may mean weak demand: every forgiving/snack pure-play has near-zero traction while punitive Seven holds 4.77 stars at scale. | **MITIGATE.** Partially rebutted (Dr. Muscle/BodBot longevity shows the mechanics retain users who arrive) but the demand half stands; covered by gate V2's early install-signal test. |

## Retention mechanic

| # | Sev | Objection | Disposition |
|---|---|---|---|
| R11 | HIGH | Nonzero forfeits proven early-window loss-aversion (streaks lift D7 for brand-new users) to protect the 3% who survive to day 30; the cushion protects the wrong cohort. | **MITIGATE.** Sharpest objection in the set. Partial rebut: the target user is defined as already streak-burned, and the opt-in longest-chain is retained as pride. Standing consequence: week-one salience is now a named design problem (the dent must be felt in days 1-7, not only after a miss in week 4), and gate V3 instruments D7 by mechanic exposure. |
| R12 | HIGH | Zero direct evidence the dent-score retains anyone; every measured forgiveness win is a bolt-on to an intact streak; the package admits the synthesis is INFERENCE. | **ACCEPT.** The dent-score is the product hypothesis, stated as such. Gate V3 pre-commits: if D7 underperforms category benchmarks, a streak-with-repair variant gets tested rather than defended against. |
| R13 | HIGH | As coded, the dent often does not exist: weekly `min(1, done/goal)` makes misses costless for over-goal users, and the unconditional floor 25 makes long lapses costless, contradicting "Miss a day. Your score dents." | **ACCEPT - real defect, reproduced** (5x/week user, goal 3, misses a day: 100 before, 100 after). The shipping mechanic must follow the prototype's per-day credit model (`../site/prototype/index.html` line 211: a miss earns 0.55 credit, so every miss dents), not a raw weekly bucket; recommended PRD amendment to US-H01: per-day granularity plus a windowed (not permanent) floor. The simulator's scenarios all run goal 7, where the weekly model dents on any miss, so the demo remains honest; caveat added to the claims matrix and to score.js. |
| R14 | MED | The dominant design per our own evidence is streak-plus-repair (Duolingo), which captures both sides of the trade. | **MITIGATE.** The win-back audience is specifically chain-averse (pain-voices), which is the rebuttal for the wedge persona; hedge recorded: the Score's data model must support an A/B chain-with-repair skin without a rebuild. |
| R15 | MED | The one forgiving-fitness operator with real cohort data (Gentler Streak) moved TOWARD a workout streak. | **ACCEPT** as adverse evidence; added to the thesis counter-evidence ledger, and "why did GS add a streak" is now a required buyer-interview question. |

## Pricing and business

| # | Sev | Objection | Disposition |
|---|---|---|---|
| R16 | HIGH | Funnel math overstates revenue ~2x: $50/payer vs the cited $35.64 Year-1 LTV, no Apple commission line, cohorts treated as recurring despite 25-33% renewal. | **ACCEPT.** Corrected funnel table written into gtm/plan.md (Red-team adjustments): $35.64 median LTV, 15% commission line, renewal decay noted; honest install threshold restated at roughly 10-20k/month for income-relevance. |
| R17 | HIGH | The paywall sells what the copy already gives away: listing said "full movement library" free while pricing.md gates catalog variety; "longer programming" free-tier contradiction. | **ACCEPT - inconsistency was real.** Free/paid boundary spec written once and the listing corrected to quote it: free = complete core loop (5-60 min ready sessions, core movement library, the Score); paid = Strength-Phase catalog, deeper variety and adaptivity depth, richer progress and history. |
| R18 | HIGH | Every verified channel case study runs an order of magnitude below the required install volume; the channels with evidence can't supply the volume, the channel with volume has no evidence. | **ACCEPT.** Reframed in the plan: explicit install kill/continue threshold and date; the income-bet label is downgraded to "portfolio asset with revenue upside" unless the channel test clears the bar. Surfaced to hcho for the priorities call (this file, summary paragraph). |
| R19 | MED | $59.99 fails the package's own defensibility test at MVP: apps priced above earn it with catalogs Nonzero ships only in Phase 2. | **MITIGATE.** List price stays $59.99; launch tactic recorded: intro annual $44.99-49.99 until the Strength-Phase catalog ships, then step to list. |
| R20 | LOW | The save-flow/interception playbook the pricing depends on conflicts with the no-guilt brand. | **MITIGATE.** "On-brand save flow" recorded as a copy deliverable (the voice contract's forgiveness-with-a-spine pattern fits it naturally). |

## Name and brand

| # | Sev | Objection | Disposition |
|---|---|---|---|
| R21 | HIGH | The name was locked past the package's own "worth counsel review" flag, against the largest existing user of the word (Robert Wright's Nonzero), whose newsletter audience overlaps the target persona; we own neither .com, .org, nor .app. | **MITIGATE.** Lock re-stated as provisional in naming/decision.md: counsel review plus a search-shadow check are pre-conditions to public launch (the no-spend guardrail made counsel impossible in this run). Fallback path recorded. |
| R22 | HIGH | Nonzero won by elimination (sole availability survivor); judges only beat it against a dead incumbent; both audience-resonance rationales are self-flagged inferences. | **MITIGATE.** True description of the process; the elimination was on evidence, which is the point of screening. Consequence: a 5-second comprehension test (name + icon, no copy, non-Reddit desk workers) is a pre-condition to brand spend; until then the App Store subtitle must carry the entire meaning. |
| R23 | MED | The brand surface is stacked negation ("non-", "no streaks", "never zeroes", "Zero is the only way to lose"). | **MITIGATE.** Copy rule added to brand guidelines: affirmative beat 1 leads every surface; at most one negation construction per surface; "Zero is the only way to lose" is reserved for closers, never headlines. |
| R24 | MED | A slashed ring is the universal prohibition glyph; the rising-slash defense dies at 16px. | **MITIGATE.** Guidelines amended: below 24px use the single-color ring-only or thicken/exaggerate the slash overshoot; small-size confusion test added to the pre-launch checklist. The full-size mark keeps the slash: at display sizes the rise reads, and the prohibition echo ("no to zero days") is partly the joke. |
| R25 | MED | Spelling fragments three ways ("nonzero", "non zero", "non-zero") and an exact-name "NonZero" app squats the bare name; the keyword field ignores it. | **ACCEPT.** Keyword field updated with the spaced variant; bare-name ranking check vs the incumbent recorded as a launch-week task. |

## GTM realism

| # | Sev | Objection | Disposition |
|---|---|---|---|
| R26 | HIGH | The funnel math starts at "installs/mo" with no top-of-funnel model at all: no views/video, CTR, or store-conversion assumptions for a zero-follower account; the plan promoted short-form to primary against its own research ranking. | **ACCEPT.** Top-of-funnel model with 30/60/90-day view, CTR, and install thresholds plus the named fallback (build-in-public X + ASO + waitlist) written into gtm/plan.md. |
| R27 | HIGH | On cited numbers the income bet does not close: ~$5.2k Year-1 revenue per 5k-install cohort, and 5k/mo sustained exceeds every named entrant except the declining category leader. | **ACCEPT.** Same consequence as R16/R18: corrected math, honest labels. This is the red team's core finding and it is surfaced, not buried. |
| R28 | HIGH | The hours don't exist: daily short-form cadence is flagged as the ceiling in the same doc that calls it "not a new skill", while the flagship's buyer interviews sit at zero. | **ACCEPT.** Cadence floor set at 2-3 videos/week, weekly hour budget stated, and the daily blitz sequenced behind an Agentic RAG validation milestone in the plan. |
| R29 | MED | "Reddit worked as ignition" overreads a case study where launch day produced $28 MRR; mod tolerance is assumed against our own PullPush data. | **MITIGATE.** Reddit demoted to community listening plus win-back copy research; participation runway (genuine contribution weeks before any app mention) added. |
| R30 | MED | The two highest-weight ASO fields spend on zero-demand supply terms, and the social-to-store funnel has a zero-social-proof hole at launch. | **MITIGATE.** Demand-term title/subtitle alternative recorded in the listing; first-50-reviews plan (beta wave + SKStoreReviewController timing) added to the plan. |
| R31 | LOW | The Apple-featuring pitch ("refuses to guilt you") walks into Gentler Streak's already-written Behind the Design story. | **ACCEPT.** Featuring angle rewritten around decision-removal (the Ready Screen), per our own research's "unclaimed ground" finding. |

## Completeness critic

| # | Sev | Finding | Disposition |
|---|---|---|---|
| R32 | HIGH | recap.html missing. | **ACCEPT** - Phase 10, in flight when the critic ran. |
| R33 | HIGH | redteam/ empty, thesis links to a nonexistent objections.md. | **ACCEPT** - this file is the fix; the link now resolves. |
| R34 | HIGH | Founder video not rendered (350/1224 frames at sweep time). | **ACCEPT** - render was in progress; muxed and watched before close (see build log). |
| R35 | MED | Simulator's streak comparison self-admittedly unfair (3x/week user vs daily streak). | **ACCEPT - already fixed** before the sweep landed: scenarios reframed to a daily-habit user (goal 7), where both mechanics watch the same behavior. |
| R36 | MED | Prototype verified with only one screenshot. | **ACCEPT** - mobile and desktop prototype captures added to site/screenshots/. |
| R37 | LOW | Screenshot mockups promised, not delivered. | **ACCEPT** - built at extras/screenshot-mockups/ with rendered PNG. |
| R38 | LOW | "FitSnack" appears in site/README.md. | **ACCEPT** - reworded; the codename now lives only in internal research/build docs. |
