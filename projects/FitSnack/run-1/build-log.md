# FitSnack run-1 Build Log

Run started 2026-07-08.
This log records every decision made autonomously, every question I would have asked hcho, the answer I chose, and why.
Append-only, chronological.

---

## Phase 0: Setup and recon

### Environment facts established

- Substrate read: `prd-fitsnack-mvp-v6_0702.md` (968 lines, full v6 PRD), `README.md`, `posts/01-social-1week-launch_260701.md`, daily logs through 2026-07-08.
- Build state: Epics A-I done in the dev repo (engine, AI Programmer option C, cold start, Variety Language, Consistency Score, PhaseEvaluator, onboarding). UI shell (J-N) unbuilt. No shippable app yet.
- No `.env` file exists anywhere in the Mandu repo or home directory, so no API keys are fair game. All media production will use free local tooling: ffmpeg 7.1.1, node v20.19.5, macOS `say`, headless Chrome (chrome-devtools-axi), npm packages (free).
- The prior market-scan raw file referenced by the social plan (`~/Documents/Last30Days/exercise-snacking-and-micro-workout-habit-apps-raw-v3.md`) does not exist on disk. All of its claims (80% quit in 30 days, 122M+ TikTok views, "lost motivation = 38% of churn") are treated as UNVERIFIED hypotheses until re-grounded with live URLs.

### Q1: What are "my voice rules" for the founder video script? (~/VOICE.md is referenced by global CLAUDE.md but does not exist)

**Answer:** Derive the voice contract from the two sources that do exist:
1. `.claude/rules/communication-style.md` external tone: professional, confident, concrete and metrics-driven, no buzzword soup; pet peeves: no emojis, no em dashes, no marketing fluff, concise, no "As an AI" hedging.
2. The FitSnack brand voice line already written by hcho in `posts/01-social-1week-launch_260701.md`: "confident, concrete, no fluff, no emojis, no em dashes; calm, forgiving, identity-framed, anti-hype."

**Why:** These are the only voice specifications hcho has actually written down, and they agree with each other. The founder script will be graded against this combined contract, and the red team will check it.

### Q2: Where do run artifacts live given the master prompt says `projects/fitsnack/run-1/`?

**Answer:** `/Users/hcho/Mandu/projects/FitSnack/run-1/` - macOS is case-insensitive, so this is the same directory. Structure: `research/`, `thesis/`, `naming/`, `gtm/`, `brand/`, `site/`, `videos/`, `redteam/`, `extras/`, plus `build-log.md` and `recap.html` at the root.

### Q3: Does the naming decision also go to the Mandu `decisions/log.md`?

**Answer:** No. The guardrail says all artifacts go in run-1, and this is a self-contained test run. The naming decision lives in `naming/decision.md`. If hcho adopts it after reviewing the run, he can log it in `decisions/log.md` himself.

### Plan of record (phases)

1. Research fan-out (multi-agent): pain evidence, competitor landscape, market and channels, science of exercise snacking. Every claim needs a live URL.
2. Naming: availability sweep (domains via DNS/whois, App Store via iTunes Search API, USPTO trademark search) for FitSnack / Cairn / Stack + alternates, then a name tournament with judge panel.
3. Thesis: synthesize a validated (or reshaped) pain-and-market thesis; adversarial verification of every load-bearing claim.
4. Positioning tournament + go-to-market + pricing.
5. Brand guidelines.
6. Marketing site + interactive Ready Screen prototype, screenshot-verified mobile and desktop.
7. Launch video + founder video (rendered locally, actually watched).
8. Red team the whole package.
9. Extras (App Store listing, screenshot mockups, + at least one unexpected deliverable).
10. recap.html + self-grade against the definition of done.

---
## Phase 1/2 interim findings (2026-07-08)

### Naming availability (inline sweep, see naming/availability-raw.md)

- FitSnack: App Store clear, fitsnack.app/.io unregistered, bundle com.fitsnack.app unclaimed. BUT "FIT SNACK" is a LIVE USPTO registration (87315837, IC 035 snack subscription boxes) and fitsnack.com is an active snack storefront. Moderate risk, food-first connotation.
- Cairn: BLOCKED (live bare CAIRN mark incl. IC 009 software, by The Game Bakers; cairn.app taken 2018; "Cairn - Hiking Safety Tracker" ships in Health & Fitness).
- Stack: BLOCKED (generic in fitness; all natural domains taken; "Stacked" workout tracker ships).
- Q4: Should the tournament include fresh names beyond the three on the table? Answer: yes - two of the three are dead on availability alone, so a fair tournament needs live alternates. FitSnack stays in as incumbent finalist.

### Research fan-out: the thesis survives only in a sharper form

- Pain (a) GROUNDED: streak anxiety, ring guilt, analysis paralysis, desk exhaustion all have recent first-person quotes with URLs; WHO 31% inactivity; D30 install retention ~3-5%; JMIR 2024 median 70% abandonment in 100 days.
- Both inherited headline stats FALSIFIED as sourced: "80% quit in 30 days" is folklore (real data is worse: ~3% D30 retention); "38% motivation churn" is an editorial estimate (real anchor: Krebs & Duncan JMIR 2015 - 40.5% loss of interest, 44.5% data-entry burden).
- Differentiation (b) PARTIALLY FALSIFIED as originally phrased: "forgiving fitness" is already owned (Gentler Streak, Apple Design Award; Apple rest days/pause rings; Bare Minimum copies the message; Keizoku is a habit tracker, not a workout app). "No guesswork" is table stakes in strength apps (Fitbod, Ladder, SHRED, Alpha Progression). "AI adjusts your plan" is fully commoditized (Peloton IQ, Fitbit Gemini, Zing, Freeletics).
- What remains EMPIRICALLY OPEN (verified across ~20 app profiles): the compound wedge - (a) complete session ready on open with zero questions + (b) forgiving no-streak consistency + (c) adaptive programming, zero-equipment, micro-first. No shipping app combines all three.
- Counter-evidence kept visible: streaks work for a large cohort; NTC is free and loved WITH browsing; boredom and "free alternatives" are churn drivers forgiveness does not fix; every "exercise snacks" pure-play has near-zero traction (label may not pull downloads); annual payers retain ~33-50% (the pain is an installer/free-user phenomenon).

## 2026-07-09: positioning and name locked

### Q5: Which positioning wins?

**Answer: "It's Already Ready" - the Ready Screen is the product.** Unanimous 3-judge verdict (9 / 9 / 8.5) over anti-streak relief, identity lead, and time-scarcity lead. Reasons: zero promise-to-proof gap (the headline IS the first screenshot IS the first second of use); attacks the measured activation cliff (26% D1 -> 10% D28, 3% D30); defended by competitors' own economics (their questionnaires and browsing ARE their funnels). Message architecture absorbs the losers: "A score that dents. Never zeroes." is beat 2 everywhere; anti-streak is the win-back track; identity is the retention/premium layer. See gtm/positioning.md.

### Q6: What is the app named?

**Answer: Nonzero.** The tournament generated 21 fresh candidates; the availability screen (DNS/RDAP + iTunes on all 21) killed everything except Nonzero; judges scored Nonzero 8.5-9 vs FitSnack 3.5-4. USPTO clean in IC 009/041/042/044 (only live NONZERO is Taiwanese gin, IC 033); nonzero.io and getnonzero.com unregistered; no App Store collision. FitSnack incumbent rejected: LIVE identical "FIT SNACK" mark in IC 035 + snack storefront owns the .com + food-first reading. Known risk logged: Robert Wright's Nonzero media brand (different category, LOW-MODERATE). See naming/decision.md.

### Engineering notes

- Ready Screen prototype mini-engine built and tested on the real 42-movement library (site/prototype/engine.js): deterministic, correct shape boundaries at 10/20/40 min, timing fit within +/-1 min at 5-60, dedicated primal block at 41+, First-Week Contrast enforced, deterministic swap with honest "no alternative" state.
- Consistency Score simulator logic built per US-H01 (extras/simulator/score.js): "one missed day" scenario yields score 95 vs streak 0 - the demo contrast works. TODO: reframe scenarios around a daily-habit user so the streak comparison is fair (daily streaks trivially zero for 3x/week users, which overstates our case).
