# Launch video storyboard (run-1)

Written 2026-07-09.
Format: 1280x720, 12 fps, ~40 seconds.
Render pipeline: deterministic HTML timeline (`launch/frame.html`, `window.seek(ms)`) -> per-frame headless-Chrome screenshots -> ffmpeg (libx264, yuv420p).
Audio: macOS `say` voiceover (voice: Samantha) plus a soft ffmpeg-generated ambient pad.
Final scene timings are locked to the measured durations of the rendered VO segments; the times below are the design targets.

## The argument in four beats (message architecture, brand guidelines section 6)

1. The door: every fitness app opens with questions; Nonzero opens with the workout.
2. The net: miss a day, the score dents, it never zeroes.
3. The floor: five minutes counts as a full show-up.
4. End card: the slashed zero draws once; name and promise.

## Scenes

| # | Time (target) | Visual | VO (Samantha) |
|---|---|---|---|
| 1 | 0.0-9.0s | Ink background. Fake onboarding gauntlet: question chips appear one by one ("What are your goals?", "What equipment do you have?", "Pick your level.", "Build your plan.") then dim to Clay as a stack. | "Every fitness app opens the same way. Questions. Goals. Equipment. A plan to configure before you're allowed to move." |
| 2 | 9.0-13.0s | Hard cut to Bone. Headline "Nonzero opens with the workout." Phone frame slides up carrying the real Ready Screen (screenshot of the live prototype). | "Nonzero opens with the workout." |
| 3 | 13.0-21.0s | Phone holds. Captions cycle beside it: "Assembled before you arrive." / "5 to 60 minutes. Zero equipment." / "One tap. You're moving." | "A complete session, five to sixty minutes, assembled before you arrive. No questions. One tap. You're moving." |
| 4 | 21.0-27.0s | Cut to Ink. The Score ring (Moss on Ink) with score number; an Ember dent notch appears with a small downtick (96 to 94); ring visibly stays full. Text: "Miss a day. Your score dents." then "It never zeroes." | "Miss a day. Your score dents. It never zeroes." |
| 5 | 27.0-31.0s | Ink. Single line, centered: "Five minutes counts as a full show-up." | "Five minutes counts as a full show-up." |
| 6 | 31.0-40.0s | End card: the ring fades in, the Ember slash draws once left-to-right (the one permitted slash animation, brand guidelines section 3), wordmark "nonzero", tagline "Your workout is already there.", small line "Free on iOS. Depth if you want it." | "Nonzero. Your workout is already there." |

## Rules honored

- No exclamation marks, no emojis, no em dashes in any on-screen text or VO.
- One Ember element per screen (chip highlight, Start button in the screenshot, dent, slash).
- No stock athletes; the hero image is the product (the real prototype screenshot).
- No banned claims (strength, fat loss, longevity, "AI-powered").
- The slash rises left-to-right and draws exactly once.
