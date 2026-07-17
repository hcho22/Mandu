# Naming Decision: the app is named **Nonzero**

Locked 2026-07-09.
Process: availability sweep on the three names on the table (FitSnack, Cairn, Stack) -> two blocked on availability alone -> tournament with 3 independent namer agents (21 fresh candidates), a factual availability screen (DNS/RDAP + iTunes Search API on every candidate), and a 3-judge panel (brand strategist, target user, trademark/ASO risk) scoring the survivors against the FitSnack incumbent.
Raw data: `availability-raw.md`, `screen-results.md`, and the tournament journal.
Guardrail honored: availability checked everywhere; nothing purchased, registered, or filed.

## The decision

**Nonzero.** Suggested store listing: "Nonzero: Micro Workouts" (final ASO keyword pending `../research/discovery-demand.md`). Suggested domains: **nonzero.io** and **getnonzero.com** (both unregistered as of 2026-07-09, RDAP 404). Suggested bundle ID: `io.nonzero.app`.

## Why Nonzero won

1. **It IS the mechanic.** The product's sharpest differentiator is a Consistency Score that dents but never zeroes, and a 5-minute session that counts as a full show-up. "Nonzero" states that in one word. The name and App Store screenshot #2 ("A score that dents. Never zeroes.") reinforce each other without explanation.
2. **The audience already speaks it.** "No more zero days" / r/NonZeroDay is an existing self-improvement ethos with years of organic usage by exactly the streak-burned, restart-cycle audience in `../research/pain-voices.md`. The name borrows a belief the target user already holds. (INFERENCE on marketing value; the community's existence is common knowledge and checkable.)
3. **Identity framing is native.** "A nonzero day." "You're someone whose days are nonzero." It extends into the brand's copy system without strain, which the judges' winning positioning ("It's Already Ready") needs for its retention and premium layers.
4. **Calm, durable, trend-free.** No "fit," no "snack," no 2026 trend word to date it. It passes the say-it-to-a-coworker test.
5. **Cleanest availability picture of all 22 candidates screened:**
   - App Store: no Health & Fitness collision; only a 0-rating Productivity app named "NonZero" (iTunes Search API, 2026-07-09). "non zero day" search also shows no meaningful collision.
   - USPTO (tmsearch.uspto.gov, queried 2026-07-09): 3 results for "nonzero" - NONZERO (LIVE/PENDING, serial 98660279) is **IC 033 gin/spirits** (Nonzero Corporation, Taiwan; unrelated goods); NONZERO GRAVITY twice, both DEAD (compression garments). **No live mark in IC 009/041/042/044.**
   - Domains: nonzero.io RDAP 404 (unregistered), getnonzero.com RDAP 404 (unregistered). nonzero.app is registered/parked (dan.com), acceptable loss with .io + getnonzero.com free.

## Judge scores (Nonzero vs FitSnack incumbent)

| Judge | Nonzero | FitSnack |
|---|---|---|
| Target user | 9 | 4 |
| Brand strategist | 8.5 | 3.5 |
| Trademark/ASO risk | 8.5 | 3.5 |

User judge, verbatim: "Nonzero is the product's anti-streak-guilt philosophy stated in one word... FitSnack sounds like a diet-food subscription wearing workout clothes."

## Why the other names on the table lost

- **FitSnack (incumbent):** "FIT SNACK" is a **LIVE USPTO registration** (serial 87315837, Agora Ventures LLC, IC 035, healthy-snack subscription boxes) and fitsnack.com is an active snack-food storefront - an identical mark in the adjacent wellness space, with permanent brand confusion ("snack" reads food-first) and a lost .com. Descriptive trend language ("snacking") with weak defensibility. Kept as the internal project codename only.
- **Cairn:** BLOCKED. Live bare CAIRN registration (serial 79380586, The Game Bakers, France) covering **IC 009 downloadable software**; cairn.app registered since 2018; "Cairn - Hiking Safety Tracker" already ships in Health & Fitness (4.7, 533 ratings).
- **Stack:** BLOCKED on distinctiveness. Generic category language in fitness ("stacking" workouts/habits), every natural domain taken, "Stacked - Workout Tracker" ships (4.6, 1.7k ratings). Near-zero trademark defensibility.

## Why the other 20 fresh candidates lost (screen results, `screen-results.md`)

Every other candidate failed the availability screen: same-name Health & Fitness collisions (Kept -> "The Kept App with Chris Powell"; Steady -> "Steady: Fear of Flying"; Sturdy -> two same-name H&F apps; Mettle -> "Mettle: Mental Fitness for Men"; Bout -> two boxing apps; Still, Breather -> multiple), famous-brand adjacency (Ember mug, Reed.co.uk, Tend Dental), or all-domains-taken with no clean fallback (Anyway, Keel, Ajar, Sliver, Threshold, Kata, Leeway).

## Known risks, stated plainly

1. **Robert Wright's "Nonzero"** (nonzero.org): a book (2000), an active newsletter/podcast brand in media/commentary. Different category (media vs. fitness software), no USPTO mark found in our classes, but it is the largest existing user of the word as a brand. Coexistence risk assessed LOW-MODERATE; a fitness app and a geopolitics newsletter are unlikely to confuse, but worth counsel review before filing.
2. **LIVE/PENDING NONZERO in IC 033 (gin).** Unrelated goods; monitor only.
3. **Suggestive, not fanciful.** "Nonzero" is a real word doing real semantic work, so the mark is suggestive-strength, weaker than a coined name like "Peloton" but far stronger than descriptive "FitSnack."
4. **Math/engineering connotation.** To some ears "nonzero" is jargon. The target persona (desk professional, often tech-adjacent) is the cohort MOST likely to know and like the term; the r/NonZeroDay usage shows it carries in self-improvement contexts. INFERENCE.
5. This is availability evidence, not legal clearance. A real filing needs a professional search (common-law marks, state registrations, international classes).

## What carries over

- The engine, PRD, and codebase are unaffected (internal identifiers can stay; bundle ID changes at App Store setup).
- The one-liner becomes: "Nonzero - the micro-workout app where your workout is already there when you open it, and missing a day dents your score but never zeroes it."

## Post-red-team rider (2026-07-09, see ../redteam/objections.md R21-R25)

The lock is **provisional**, with three pre-conditions before public launch spend:

1. **Counsel review** of the Robert Wright "Nonzero" coexistence call (this run's no-spend guardrail made that impossible here; the LOW-MODERATE assessment above is a lay read of USPTO evidence, not clearance).
2. **Search-shadow check**: "nonzero" organic results are owned by Wright's media brand and we hold neither .com, .org, nor .app; verify "nonzero app" and App Store bare-name ranking against the incumbent "NonZero" productivity app before committing ad spend to the bare name.
3. **5-second comprehension test**: name plus icon, no copy, shown to non-Reddit desk workers. The "audience already speaks it" rationale is inference from r/NonZeroDay; if cold comprehension is near zero, the subtitle must carry the entire meaning and should be chosen for that job.

Fallback if any pre-condition fails: rerun the screen on the next tier of tournament candidates (all documented in `screen-results.md`) rather than reverting to the trademark-blocked FitSnack.
