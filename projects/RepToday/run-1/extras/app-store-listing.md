# App Store listing (Nonzero)

Drafted 2026-07-09 against `../brand/brand-guidelines.md` (voice contract, section 6; caption order, section 9) and the approved-claims list in `../thesis/thesis.md` section 5.
Character limits are Apple's current listing limits; every field below is inside its limit.

## Name (30 chars max)

**Nonzero: Micro Workouts** (24)

## Subtitle (30 chars max)

**Exercise snacks, no streaks** (27)

Rationale: "exercise snacks" is the rising search phrase the discovery research flagged (`../research/discovery-demand.md`); "no streaks" is beat 2 compressed to two words.
Post-red-team caveat (objections R2/R30): the same research classifies "exercise snacks" and "micro workout" as supply keywords with near-zero typed demand, so treat this subtitle as the launch option, and validate against a demand-term alternative such as "5 minute home workouts" (22 chars) or "Quick workouts, no streaks" (26 chars) once keyword tooling is available.
Fallback if ASO testing shows "exercise snacks" is too niche: "Your workout is already there" is 29 characters and restates beat 1.

## Promotional text (170 chars max, editable without review)

Open the app. Your workout is already there. A complete 5 to 60 minute session, no equipment, no questions. Miss a day and your score dents. It never zeroes. (157)

## Description (4000 chars max)

Open the app. Your workout is already there.

A complete session, five to sixty minutes, assembled on your phone before you arrive. No questionnaire. No plan to configure. No browsing. The first screen is the workout, and the biggest button on it is Start.

WHY THE FIRST SCREEN MATTERS
Most fitness apps open with questions at the exact moment you have no decisions left in you. Nonzero moves every decision to the other side of one tap. Pick a different duration with one chip if you want. Swap any exercise for a same-muscle alternative with one tap. Or just press Start.

A SCORE THAT DENTS. NEVER ZEROES.
Nonzero has no streaks to lose. Your Consistency Score is a rolling picture of how you actually show up. Miss a day and it dents, visibly and a little. It never resets to zero, because one missed Tuesday is not nothing, and it is not everything either. If you love chains, your longest one is tracked quietly as opt-in pride. It just can't hurt you here.

FIVE MINUTES COUNTS
Five minutes counts as a full show-up. The point is the identity, not the burn: you are becoming someone who moves. Sessions run from five minutes to a full hour, all zero-equipment, built from strength, mobility, and primal movement patterns.

IT QUIETLY RETUNES
Between sessions, Nonzero adjusts what it serves you based on how you are actually doing. No forms, no check-ins. It notices, and tomorrow's session is tuned. The engine is deterministic and runs on your phone: fast, offline, private.

WHAT THE SCIENCE SUPPORTS
Short sessions, done consistently, measurably improve cardiorespiratory fitness. The World Health Organization's guidance is that every move counts. And the habit research says one missed day does not break a habit. That is the whole design.

We will not promise fat loss, a six-pack, or extra years of life from five-minute sessions. We promise a workout that is already there, and a score that survives your worst week.

FREE FOREVER, DEPTH IF YOU WANT IT
The core loop is free forever: the daily ready session at any length from five to sixty minutes, the Consistency Score, and the core movement library. Depth is the paid tier: the Strength Phase catalog, deeper session variety and adaptivity, richer progress views, and history tools. $9.99 a month or $59.99 a year, with a 14-day free trial.

Nonzero. Zero is the only way to lose.

(~2,150 chars, within limit)

## Keywords (100 chars max, comma-separated, no spaces)

exercise snacks,micro workout,no streak,habit,quick,home,bodyweight,short,desk,non zero (88)

Notes: "workout" and "fitness" are covered by the name and subtitle fields, which index too; do not waste keyword characters on them.
"non zero" covers the spaced spelling fragment (word-of-mouth arrives as "nonzero", "non zero", and "non-zero"; Apple does not reliably match spacing variants of the name field, and an unrelated "NonZero" productivity app holds the bare name).

## Screenshot captions (in the fixed message-architecture order, brand guidelines section 9)

1. "Your workout is already there."
2. "A score that dents. Never zeroes."
3. "Five minutes counts."
4. "It quietly retunes to you."
5. "Free forever. Depth if you want it."

Mockups: `screenshot-mockups/` (iPhone frame, Ink or Bone background, one caption line each).

## What's-new template (first release)

Nonzero 1.0. Open the app. Your workout is already there. Five to sixty minutes, zero equipment, and a Consistency Score that dents but never zeroes.

## Age rating and category

- Primary category: Health & Fitness. Secondary: Lifestyle.
- Age rating: 4+.

## Review notes (App Review)

- No account required for the core loop; Sign in with Apple only gates sync.
- The session engine is deterministic and on-device; no workout content is fetched at runtime.
- Subscription: auto-renewing, StoreKit 2, 14-day free trial, priced $9.99/month or $59.99/year.

## Compliance checklist (against the voice contract and approved claims)

- No exclamation marks, emojis, or em dashes anywhere above.
- No banned claims: no fat loss, no strength promises from micro sessions, no blood pressure, no longevity, no "AI-powered."
- Science lines stay inside the approved set: CRF from short sessions, WHO every-move-counts, Lally one-miss. Sources in `../research/science.md`.
- "Exercise snacks" appears in subtitle and keywords only as a category term, not a trademark claim.
