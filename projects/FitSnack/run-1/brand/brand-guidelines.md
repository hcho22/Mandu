# Nonzero Brand Guidelines

v1.0, 2026-07-09. The complete brand system.
Written so that a stranger with no other context can produce a new on-brand asset from this document alone.
Sources of truth: positioning in `../gtm/positioning.md`, naming rationale in `../naming/decision.md`.

---

## 1. The brand in one paragraph

Nonzero is a micro-workout iOS app for desk-bound adults who are done being guilted by fitness products.
Open it and a complete 5-60 minute zero-equipment workout is already there - no questions, one tap.
Miss a day and your Consistency Score takes a dent; it never zeroes.
The brand's job is to feel like the opposite of every fitness app the user has quit: calm where they shout, concrete where they hype, forgiving where they punish.
The name states the promise: your days don't go to zero here.

## 2. Name

- The product name is **Nonzero**. Capitalized as a proper noun in prose ("Nonzero"), all-lowercase in the wordmark ("nonzero").
- Never "NonZero", "Non-Zero", "NONZERO" (except legal filings where required).
- App Store listing name: "Nonzero: Micro Workouts". Subtitle: "Exercise snacks, no streaks".
- The article rule: "Nonzero", never "the Nonzero app" on first reference; "the app" thereafter is fine.
- Vocabulary the name unlocks (use sparingly, never all at once): "a nonzero day", "keep your days nonzero", "zero is the only way to lose".
- Internal/engineering codename "FitSnack" never appears in anything user-facing.

## 3. Logo

Files: `logo.svg` (logomark + wordmark lockup), `appicon.svg` (app icon).

- **The logomark is the slashed zero**: a ring (the day) crossed by a rising slash (the refusal). The slash rises left-to-right - it must never descend.
- Construction: ring stroke and slash stroke are equal weight (14 units at 160-unit height; scale proportionally). The slash overshoots the ring slightly on both ends, capped round.
- **Colors**: ring in Ink on light backgrounds, Bone on dark; the slash is always Ember. Single-color versions (all-Ink or all-Bone) are permitted where one ink is required (engraving, favicons); never recolor the slash to any other hue.
- **Wordmark**: "nonzero" lowercase, bold, tight tracking (-1), system sans (SF Pro on Apple platforms; -apple-system/Helvetica Neue stack elsewhere).
- Clear space: one ring-radius on all sides. Minimum size: logomark 16px, lockup 120px wide.
- Don't: rotate, outline, gradient, shadow, animate the slash separately (exception: the launch video may draw the slash once, as a single deliberate stroke).
- The app icon is the logomark on an Ink field with Bone ring and Ember slash. No other icon backgrounds.

## 4. Color

The palette is "quiet depth": a dark forest ink, a warm paper, one ember accent. It deliberately refuses fitness-category neon.

| Token | Hex | Role |
|---|---|---|
| **Ink** | `#12261F` | Primary dark: text on light, dark surfaces, the ring |
| **Bone** | `#F4F1EA` | Primary light: backgrounds, text on dark |
| **Ember** | `#C97B2D` | The one accent: the slash, primary CTAs, the Score dent highlight, Start actions |
| **Moss** | `#7FA48E` | Secondary: success states, completed sessions, calm charts |
| **Pine** | `#1E4D3B` | Mid-dark: secondary surfaces on Ink, hover states, pillar tags |
| **Clay** | `#B9B2A4` | Muted: secondary text on light, dividers, disabled |

Rules:
- Ink on Bone is the default reading pair (contrast 13.9:1). Bone on Ink for dark surfaces.
- Ember is scarce by design: one Ember element per screen (the thing you should touch). Ember on Ink passes contrast for large text/UI (4.6:1); do not set body text in Ember on Bone (3.1:1 - large text only).
- Moss is never a CTA. Clay is never body text.
- No pure white (#FFF) or pure black (#000) anywhere. No gradients in UI; flat color only.

## 5. Typography

- **Apple platforms (product)**: SF Pro via system. Display: SF Pro Display Bold, tight tracking. Text: SF Pro Text Regular/Medium.
- **Web/marketing**: the system stack `-apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Arial, sans-serif` - self-hosted-font-free on purpose (fast, native-feeling, matches the product).
- Scale (marketing): hero 56-72px/1.05 bold; section head 32-40px/1.15 bold; body 17-19px/1.55 regular; caption 14px/1.4.
- Numbers are content at Nonzero (scores, minutes): set key numbers in bold, same family, often Ember or Moss. Use `font-variant-numeric: tabular-nums` for anything that counts.
- Never: italics for emphasis (use bold sparingly), ALL CAPS except tiny labels (12-13px, +0.08em tracking), more than two weights per surface.

## 6. Voice

The voice contract (inherited from hcho's rules + the brand): **calm, confident, concrete, forgiving, identity-framed, anti-hype. No emojis. No em dashes. No exclamation marks. No marketing fluff.**

Principles with patterns:

1. **Say the mechanic, not the vibe.** The brand's claims are checkable product facts.
   - Yes: "A score that dents. Never zeroes."
   - No: "Fitness that finally understands you."
2. **Short declaratives. Full stops do the emphasis.**
   - Yes: "Open the app. Your workout is already there."
   - No: "Imagine opening an app and BOOM - your workout is ready!!"
3. **Identity, never body-shame; effort, never aesthetics.**
   - Yes: "You're someone who moves."
   - No: "Get shredded", "summer body", any before/after framing.
4. **Forgiveness with a spine.** A miss costs something visible and small; the copy never pretends misses don't matter, and never scolds.
   - Yes: "Tuesday cost you two points. It's Wednesday."
   - No: "Don't worry, it's fine!" (toothless) / "You broke your commitment." (scold)
5. **Respect the streak-lovers.** Anti-streak copy is relief, not superiority.
   - Yes: "Keep your chain if you love it. It just can't hurt you here."
   - No: "Streaks are toxic."
6. **Claims stay inside the evidence.** Approved science lines (see `../thesis/thesis.md` §5): cardio fitness from short sessions, "every move counts" (WHO), "one missed day doesn't break a habit" (Lally 2010), sit less move more. Banned claims: builds strength (micro-format), burns fat, lowers blood pressure, adds years to your life, anything "AI-powered" in user-facing copy.
7. **The app is quiet about its intelligence.** The AI Programmer is never marketed as AI. Approved: "It quietly retunes to you between sessions." Banned: "AI coach", "powered by machine learning", model names.

### Message architecture (fixed order)

1. **Beat 1 - the door**: "Open the app. Your workout is already there." (the Ready Screen)
2. **Beat 2 - the net**: "Miss a day. Your score dents. It never zeroes."
3. **Beat 3 - the floor**: "Five minutes counts as a full show-up."
4. **Beat 4 - the destination**: "You're becoming someone who moves." (retention/premium surfaces only)

Win-back track (streak-burned audiences only): "You did not lose the habit. The counter did."

### Copy blocks (canonical, reuse verbatim)

- One-liner: "Nonzero is the micro-workout app where your workout is already there when you open it, and missing a day dents your score but never zeroes it."
- Subhead: "A complete zero-equipment session, 5 to 60 minutes, assembled before you arrive. No questions. One tap. Five minutes counts."
- Pricing line: "The core loop is free forever. Depth is $9.99 a month or $59.99 a year, with a 14-day trial."

## 7. The dent (graphic motif)

The product's signature visual is the **Score ring with a dent**: a circular progress ring in Moss/Bone whose past misses appear as small notches - visibly there, visibly small, never a gap that empties the ring.
Usage: product Score displays, the launch video, the simulator, marketing charts of "dents vs zeroes."
Rules: a dent is at most 8% of the circumference; dents fade (opacity steps down) as they age; the ring never renders below 25% full for any user with any history - the visual floor mirrors the mechanic's floor.
The logomark's slash is NOT the dent; do not combine slash and dent in one glyph.

## 8. Imagery and interface principles

- **Show the product, not stock athletes.** The hero image is always the Ready Screen itself. No stock photography of gyms, abs, or sunrise runners. If humans appear: ordinary clothes, ordinary rooms, mid-movement, never posed.
- **The Ready Screen rule (from the PRD, verbatim design contract):** it reads "Today: N min - Start", never "How long do you have today?" with Start gated. One visually dominant Start (Ember). Duration is a chip row (5/10/15/20/30/45/60), never a picker that blocks.
- No XP, levels, badges, confetti, flames, or trophy iconography anywhere - including marketing.
- Motion: calm and brief (200-300ms ease-out); one purposeful animation per screen; honors Reduce Motion with static fallbacks.
- Screenshots and mockups use an iPhone frame, Ink or Bone background, one caption line per screenshot in the message-architecture order.

## 9. Applications (how the pieces assemble)

- **App Store screenshot captions, in order:** 1) "Your workout is already there." 2) "A score that dents. Never zeroes." 3) "Five minutes counts." 4) "It quietly retunes to you." 5) "Free forever. Depth if you want it."
- **Social avatar**: app icon. **Banner**: Ink field, lockup left, "Open the app. Your workout is already there." right.
- **Email/push tone**: one sentence, concrete, no urgency theater. Push example (comeback): "Your next session is ready. 10 minutes, mobility. It's been ready all week."
- **Landing page structure**: hero (beat 1 + live prototype), the net (beat 2 + simulator), the floor (beat 3 + science strip with citations), how it works (engine, quiet retuning), honest pricing, no-nonsense FAQ including "Why no streaks?" answered with the Duolingo/Lally evidence.

## 10. Do / Don't (quick reference)

| Do | Don't |
|---|---|
| "Open the app. Your workout is already there." | "Revolutionary AI fitness companion" |
| Ember on exactly one element per screen | Neon gradients, glassmorphism, dark-mode neon green |
| "Five minutes counts as a full show-up." | "Crush your goals in just 5 minutes!" |
| Cite the mechanic ("dents, never zeroes") | Promise outcomes the science bans (fat loss, strength from 5-min snacks, longevity) |
| lowercase "nonzero" wordmark, rising slash | Descending slash, recolored slash, "NonZero" |
| Respect streaks as opt-in pride (longest chain) | Mock streak users |
| System fonts, flat color, full stops | Custom display fonts, italics, exclamation marks, emojis, em dashes |
