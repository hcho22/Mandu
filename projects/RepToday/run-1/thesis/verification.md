# Adversarial Claim Verification (run-1)

Run 2026-07-09. Twelve independent skeptic agents, each assigned one load-bearing thesis claim with a single job: refute it.
Each skeptic re-fetched the cited primary source and hunted for counter-evidence.
Scoreboard: **9 CONFIRMED, 2 WEAKENED (corrections applied), 1 REFUTED (thesis reshaped)**.
All corrections below are already folded into `thesis.md`; this file preserves the audit trail.

| Claim | Verdict | What the skeptic found |
|---|---|---|
| H&F apps: 3% D30 retention; activation 26% D1 -> 10% D28 (Business of Apps) | **CONFIRMED** | Fetched via curl (WebFetch 403); both figures verbatim on the public page. Cross-checked AppsFlyer (~2.78% D30 - consistent). Context noted: 3% is the broad-category floor; dedicated fitness apps retain better (8-12%). |
| Median 70% abandon health apps within 100 days (Kidman, JMIR 2024) | **CONFIRMED** | Verbatim in the PMC abstract, incl. the 54-75% physical-activity range. |
| BJSM 2025: CRF g=1.37; adherence 82.8%/compliance 91.1%; null on strength/body-comp/BP/lipids | **CONFIRMED** | Skeptic downloaded the actual PDF and matched every figure verbatim; corroborated by the BMJ Group press release. No retraction found. |
| VILPA mortality HR ~0.61-0.73 at 3-4 min/day, vigorous-only | **WEAKENED - corrected** | The vigorous-only core holds (VILPA def: >=64% VO2max / >=77% HRmax / RPE >=15). But the HR range conflated metrics: 3-4 min/day (duration) = **HR ~0.70-0.78**; HR ~0.61 belongs to the frequency measure (3 bouts/day) or CVD-specific mortality. Thesis §5 corrected. |
| Lally 2010: one missed opportunity doesn't impair habit formation; 66-day average | **CONFIRMED** | Both statements verbatim on the UCL page (Lally's own Q&A answer). |
| Duolingo: 3.6x completion at 7-day streak; freezes +0.38% DAU; Streak Wager +14% D7; Amulet +4% | **CONFIRMED** | All five statistics verbatim across the two cited Duolingo posts, none misattributed. |
| **No app combines ready-on-open + no-streak forgiving + adaptive** | **REFUTED - thesis reshaped** | Skeptic found two live counterexamples in US top results: **Dr. Muscle** (4.5, 376 ratings: day's workout with weights/reps pre-chosen on open, no streak mechanic, auto-lightens after a 10+ day break, updates after every set) and **BodBot** (4.76, 2,870 ratings: today's workout on open, no streaks, "completely adaptive" to missed sessions). Both require onboarding quizzes, lack any designed consistency metric, and are strength-optimization tools for people who already train. See the reshaped wedge in `thesis.md` §3. |
| FIT SNACK live (87315837, IC 035); FITSNACK dead; no live NONZERO in 009/041/042/044 | **CONFIRMED** | Skeptic fetched TSDR records directly (not mirrors): FIT SNACK Reg. 5398277 live/active, Section 8 accepted 2024, owner Agora Ventures LLC; FITSNACK dead; NONZERO live-pending only in IC 033 (gin). |
| RevenueCat H&F medians ($9.99/mo, $39.94/yr, 37.7% trial-to-paid, 68% annual, 25% annual renewal) | **CONFIRMED** | All verbatim on the fetched RevenueCat pages (the 25% renewal on the renewal-rates-by-category post). |
| Gentler Streak is a tracker that does not generate/serve workouts; recent reviews ask for guided workouts | **WEAKENED - corrected** | It does not serve guided sessions, but its "Go Gentler" feature DOES generate daily activity suggestions (type + HR zone + duration), so "generates nothing" overstates. And the strongest "guide me" review quotes date to 2024, not 2026 (skeptic scanned all 494 US RSS reviews). Thesis wording corrected to "serves no guided session and prescribes no exercises." |
| Seven is mature/declining (~30k downloads/$90k June 2026 vs ~40k/$100k Oct 2025) | **CONFIRMED** | Sensor Tower live page ("30k downloads and $90k revenue") vs Wayback 2025-11 snapshot ("40k/$100k") - both fetched verbatim. Third-party estimates; direction robust. |
| Exercise snacking is a named 2026 wellness trend; 122M+ views (Virlo via Forbes) | **CONFIRMED (with sourcing grade)** | Who What Wear dated 2026-01-17, expert-predicted framing verified; Forbes contributor post carries the Virlo number. Skeptic's grade matches ours: usable as MEDIUM with attribution, never as a bare fact. |

## What changed as a result

1. **The wedge claim was reshaped** (the single most important output of this pass). Old: "no app combines the three." New, honest form - see `thesis.md` §3: adaptive no-streak trainers exist for committed lifters (Dr. Muscle, BodBot); what remains unclaimed is that intersection **for the lapsed, desk-bound non-exerciser**: micro-first (5-60 min, zero-equipment), zero-question daily open, and a *designed* forgiving consistency mechanic (a score that dents, never zeroes) rather than the mere absence of streaks. Dr. Muscle and BodBot are optimization products for people who already train; Nonzero is a discipline product for people whose problem is showing up at all.
2. **VILPA numbers corrected** in `thesis.md` §5 (HR 0.70-0.78 for the 3-4 min/day duration measure).
3. **Gentler Streak gap language tightened** in `thesis.md` §3 (it generates suggestions, not sessions; the "guide me" quotes are from 2024).
