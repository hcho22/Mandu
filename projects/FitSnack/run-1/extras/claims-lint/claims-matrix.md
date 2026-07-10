# Claims traceability matrix

2026-07-09.
Every factual claim that appears in a user-facing Nonzero asset, traced to the evidence it rests on.
The companion linter (`lint.js`) enforces the negative space (banned phrases); this matrix covers the positive claims.
Full quotes, fetch dates, and confidence grades live in the cited research files; URLs here are the primary sources those files actually fetched.

| # | Claim (as used in copy) | Where it appears | Evidence | Primary source | Status |
|---|---|---|---|---|---|
| 1 | "Short sessions, done consistently, measurably improve cardiorespiratory fitness" | site science strip, App Store description | BJSM Oct 2025 meta-analysis, 11 RCTs, n=414: CRF g=1.37 (95% CI 0.58-2.17); holds at g=1.02 after sensitivity analysis | http://press.psprings.co.uk/bjsm/october/bjsm110027.pdf (see `../../research/science.md` finding 1) | APPROVED |
| 2 | "Every move counts" (WHO) | site science strip, App Store description | WHO 2020 Guidelines on Physical Activity: 10-minute-bout rule removed | https://www.who.int/news/item/25-11-2020-every-move-counts-towards-better-health-says-who (finding 4) | APPROVED (format support, never a longevity promise) |
| 3 | "One missed day does not break a habit" | site science strip + FAQ, App Store description, launch/founder video mechanic | Lally et al. 2010, European Journal of Social Psychology: missing one opportunity did not materially impair habit formation | https://pmc.ncbi.nlm.nih.gov/articles/PMC4704953/ (finding 3, verified verbatim) | APPROVED |
| 4 | "About 3% of the people who install a fitness app are still using it thirty days later" | founder video (VO + on-screen stat card) | Business of Apps health-and-fitness benchmarks: 3% D30 install retention (2023 data); corroborated by UXCam benchmark compilation (~3-5%) | https://www.businessofapps.com/data/health-fitness-app-benchmarks/ (see `../../research/pain-stats.md`) | APPROVED (say "about"; it is 2023-cohort data) |
| 5 | "Assembled on your phone in under a tenth of a second, offline" | site hero subhead, prototype badge | Measured in the run-1 prototype: the deterministic engine generates a session in <1 ms on the real 42-movement library; the iOS engine is the same deterministic design (PRD v6, Epic C) | `../../site/prototype/engine.js` + build-log engineering notes | APPROVED for prototype-backed marketing ("in under a tenth of a second" is a >100x safety margin), re-verify on device before App Store submission |
| 6 | "Miss a day and your score dents; it never zeroes" (floor 25) | everywhere (beat 2) | Product mechanic, PRD v6 US-H01, demonstrated in the simulator: one missed day reads score 95 vs streak 0 | `../simulator/score.js` | APPROVED **with a mechanic contract** (red-team R13): the claim is only true under the prototype's per-day credit model; a raw weekly bucket makes over-goal misses costless. The shipping Score must implement per-day dents or the copy must change. |
| 7 | "Five minutes counts as a full show-up" | everywhere (beat 3) | Product mechanic: weekly adherence credits any completed session | `../simulator/score.js`, PRD v6 | APPROVED |
| 8 | "$9.99 a month or $59.99 a year, 14-day trial; core loop free forever" | site pricing, App Store listing | Pricing decision, gtm/plan.md, grounded in RevenueCat State of Subscription Apps benchmarks | https://www.revenuecat.com/state-of-subscription-apps/ (see `../../research/pricing.md`) | APPROVED (decision, benchmark-informed) |
| 9 | "It quietly retunes to you between sessions" | site, App Store caption 4 | Product mechanic: deterministic on-device policy re-weighting (PRD v6 option C AI Programmer); deliberately not marketed as AI | PRD v6 (dev repo) | APPROVED with the quiet-intelligence rule (lint enforces the ban on "AI-powered") |

## Claims we deliberately do NOT make (and the linter enforces)

| Banned claim | Why | Evidence |
|---|---|---|
| Builds strength / visible muscle | BJSM 2025 meta-analysis: no significant effect from snack-length dosing | `../../research/science.md` finding 2 |
| Burns fat / weight loss | Same meta-analysis: null on body composition | finding 2 |
| Lowers blood pressure | Same meta-analysis: null | finding 2 |
| Adds years to your life / longevity | VILPA mortality evidence is vigorous-only (HR ~0.70-0.78 range per verification pass); gentle mobility snacks do not qualify | finding 3 in `../../thesis/verification.md` |
| "The only app that..." | Broad-triple uniqueness was refuted (Dr. Muscle, BodBot) | `../../thesis/verification.md` |
| "AI-powered" / "AI coach" | Brand rule: the app is quiet about its intelligence; "AI adjusts your plan" is commoditized copy | `../../research/competitors-incumbents.md` |

## How to run the gate

    node lint.js

Exit 0 means every user-facing asset is clean.
Add new user-facing files to `TARGETS` in `lint.js` as they are created; add a scoped waiver to `ALLOW` only for honest-negation lines that name a banned claim in order to refuse it.
