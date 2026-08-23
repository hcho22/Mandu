# Rep Today - Social Media Execution Checklist

**Created:** 2026-08-17
**Scope:** the operational runbook for actually posting to social - the shoot list, the 14-day calendar, and the reading discipline.
**Source of truth:** the GTM social kit at `/Users/hcho/firstmate/projects/RepToday/gtm/05-social-pmf/` (angles, cadence, platform assignment, A/B pairs, read-the-results), plus `06-channels/channel-plan.md` and the `08-redteam/pre-publication-checklist.md`.
**Parent:** `02-marketing-launch-checklist_260807.md` owns the broad Gate 0 / Track A vs B picture. This file is the drill-down into Track A's social execution. Where the two overlap (Gate 0, benchmark), the parent is authoritative; check items in both.

_Status: not started. Blocked only partially - see Gate 0 below. Most angles can run without the device benchmark. Platform set (updated 2026-08-18): TikTok + YouTube Shorts adjudicate the experiment; Instagram Reels + X added as non-adjudicating distribution mirrors._

---

## Read this first - what this actually is

This is not "make content and see what sticks."
The team already built a **pre-registered PMF experiment**: 16 angles (P01-P16), each a falsifiable hypothesis with a frozen hook and a pre-registered kill criterion, plus 6 A/B hook pairs.
The hooks are frozen in `angles.md` and `ab-pairs.md` **before any results exist**.
Executing means running the frozen kit exactly.
Rewriting a hook mid-window destroys the experiment's validity.

**Platforms, in two tiers (the distinction is load-bearing - do not blur it).**
**Adjudicating (the experiment):** TikTok (primary - its metrics adjudicate the signal) and YouTube Shorts (secondary - a free second sample, read but never adjudicating). These two, and ONLY these two, decide whether an angle lives, dies, or doubles down.
**Distribution mirrors (reach + brand presence, added 2026-08-18 at hcho's request):** Instagram Reels and X. The same asset also posts here the same day, but their metrics are informational only and NEVER adjudicate an angle. This is deliberate, not an oversight: Instagram Reels ranks partly on follower count and X has thin 30-49 reach, so at zero followers their weak numbers are ambiguous (weak content vs no audience) and cannot be trusted as signal. They cost almost nothing to cross-post, they start building the presence and follower base you will want later, and Reels discovery reach is real once a following exists - so they earn their place as mirrors, just not as judges.
Identical creative posts to all four the same day (the caption wrapper adapts per platform format, below); the frozen hook never changes per platform.

**The one expectation to internalize:** at zero followers with no App Store listing, this run cannot measure downloads or conversions.
TikTok gates clickable bio links behind account requirements a brand-new account may not meet, and there is nothing to download yet.
This run answers exactly one question: which message makes the ICP stop scrolling.
Winning angles become the App Store creative and the launch-day hooks.
Treat social now as message discovery, not customer acquisition.

---

## Gate 0 - must be TRUE before any asset posts

- [x] Naming cleared + reserved; `@reptoday` handles secured; `reptoday.app` live. (Done - see parent `02-`.)
- [x] Privacy policy hosted + wired at `reptoday.app/privacy`. (Done - see parent `02-`.)
- [ ] **USPTO trademark clearance for "Rep Today"** finalized. (Blocks everything public. Tracked in parent `02-`.)
- [ ] **Device p95 for the "under 100ms" claim** on iPhone XS / iOS 17. Blocks **only P06 and P16** (the two speed-claim angles); every other angle can proceed without it. If the slowest device misses 100ms, change the number in those two hooks before posting them.
- [ ] **Confirm the @reptoday handle is actually free** on TikTok, YouTube, Instagram, and X (the research check was blocked by login walls; parent `02-` lists all four handles as secured defensively, so this is a re-verify at account-creation time).

---

## Phase 1 - Set up the rails (one-time)

- [x] Create the **TikTok** account and **YouTube** channel; confirm @reptoday on both.
- [ ] Create / confirm the **Instagram** and **X** accounts as @reptoday (distribution mirrors). Same bio, avatar, and waitlist link across all four. Note the link rules: X allows a clickable link in the post body and bio; Instagram allows a link in bio only (no clickable caption link), so point the bio at the waitlist.
- [x] Pick **one consistent local-evening posting slot** and lock it for the whole 14-day window. Time-of-day must be held constant or the day-N / day-N+7 A/B legs are not comparable.
- [x] Join the three **Reddit listening** subs read-only: r/fitness30plus, r/bodyweightfitness, r/getdisciplined. Zero links, zero product mentions, ever - they permanently ban self-promo. **Manually read each sub's self-promotion rules first.**
- [x] Confirm the **Kit waitlist** capture form is live on the landing page so a bio link has a destination once TikTok unlocks clickable bio links. (Parent `02-` tracks standing up the waitlist as the last Gate 0 item.)
- [ ] Name the **non-founder K8 coder** before the first TestFlight cohort. The K8 rubric itself is already pre-registered (dev-repo #93); only the coder slot is open. Not a blocker for social, but it must be filled before the TestFlight cohort that social feeds into.

## Phase 2 - Produce the footage (record once, reuse all window)

The kit is built so most days re-cut the same source footage with a different hook. Record a small source set:

- [ ] **Core cold-open demo** - real device, real time, no cuts, home screen to ready session. Powers P01 on days 1 and 8. Single most-reused asset; this is Day 1.
  Step 2 - Prep the phone so the recording is clean

A distraction in the frame ruins the take:
- Turn on Do Not Disturb / a Focus mode so no notification banners pop in mid-record.
- Charge above ~30% so the battery icon looks healthy (it's visible in the status bar).
- Put the Rep Today icon somewhere easy to tap in the first second (e.g. the dock or top-left).
- Optional polish: clear other clutter off that home screen page so the icon is the obvious subject.

Step 3 - Force a true "cold open"

This is the detail most people miss. "Cold open" means the app starts fresh, not resumes from memory:
1. Open the app switcher (swipe up from the bottom and hold, or double-click Home on older phones).
2. Swipe the Rep Today card up to fully close it.
3. Go back to the home screen.

Now the next launch is a genuine cold start, which is exactly what proves the session is generated at open, not left over from before.

Step 4 - Record with the iPhone's built-in screen recorder

1. Add the screen-record button if you haven't: Settings → Control Center → add Screen Recording.
2. Swipe into Control Center and long-press the screen-record button. Make sure the microphone is OFF (P01 has no voiceover). Tap Start; it gives you a 3-second countdown.
3. Wait for the countdown to finish, pause ~1 second on the home screen, then tap the Rep Today icon and let it open to the ready session. Hold on the ready screen for ~2 seconds.
4. Stop the recording (tap the red clock/pill at the top, or back in Control Center).

- [ ] **Founder first-person batch** - format changed to **voice-over + faceless** (hcho's own recorded voice over screen recordings / b-roll, no face on camera; decided 2026-08-17, logged in `decisions/log.md`). Real recorded voice only, never TTS/AI voice. Scripts ready in `posts/02-founder-voiceover-scripts_260817.md`. Record the voice-overs in one sitting:
  - [ ] Comeback story (P02, day 4)
  - [ ] Reading a real paywall review aloud (P07, days 2 and 9)
  - [ ] No-streaks contrarian (P09, days 6 and 13)
  - [ ] Discipline inversion (P10, day 12 - the ONE sanctioned test)
  - Read caveat: face-to-camera often out-earns faceless for trust/story angles (P02, P09), so do not kill an angle on a weak result alone - it may be the format, not the message.
- [ ] **Silent mechanic screen-records** (real device, real time):
  - [ ] Missed-day Consistency Score dip, never resets (P03, days 3 and 10)
  - [ ] 5-minute session timelapse, phone timer visible (P04, day 7)
  - [ ] Airplane-mode-on, session still builds (P11, day 5)
  - [ ] Mobility-blocks-as-co-equal session scroll (P08, day 11)
- [ ] All screen recordings are **real device, real time, cuts only where the shot list declares** - faked or over-edited demos read as AI-slop in-feed.
- [ ] **Do NOT reuse the 48s launch video's macOS `say` voiceover.** Any video with narration needs a human voice re-record first (parent `02-` Gate 1).

**Recording dependency:** these record the running app. The app is build-complete; confirm you can build to your own device to capture footage now rather than waiting on TestFlight provisioning.

## Phase 3 - Run the 14-day calendar (window 1)

Execute `05-social-pmf/cadence-14-day.md` exactly. One asset/day, same locked slot. The listed platform is the primary that adjudicates; the same asset also mirrors to YouTube Shorts and now to Instagram Reels and X the same day. The calendar rows below are unchanged - only the distribution surface widened.

**Every day's asset posts to all four surfaces the same day:**
- **TikTok** (primary, adjudicates) and **YouTube Shorts** (secondary, second sample) - unchanged.
- **Instagram Reels** - drop the identical 9:16 vertical video; metrics informational only.
- **X** - attach the same clip, but the caption/hook text carries more weight here (text-forward platform); metrics informational only. Salvaged X-native text variants live in `05-social-pmf/week-1-drafts.md`.
- Post all four inside the same evening slot; do not stagger them to different days, or the day-N / day-N+7 A/B comparability on the adjudicating platforms breaks.

**Week 1**
- [ ] Day 1 - P01 cold-open demo, hook A (AB-1 leg A) - TikTok
- [ ] Day 2 - P07 founder reads paywall review, pain-first (AB-3 leg A) - TikTok
- [ ] Day 3 - P03 missed-day score record (AB-2 leg A) - YouTube Shorts
- [ ] Day 4 - P02 founder comeback story - TikTok
- [ ] Day 5 - P11 airplane-mode demo - YouTube Shorts
- [ ] Day 6 - P09 no-streaks contrarian, declaration-led (AB-6 leg A) - TikTok
- [ ] Day 7 - P04 5-minute timelapse - TikTok. **Evening: run the Day-7 midpoint review.**

**Week 2**
- [ ] Day 8 - P01 cold-open demo, hook B (AB-1 leg B, same footage as day 1) - TikTok
- [ ] Day 9 - P07 paywall review, promise-first cut (AB-3 leg B, same footage as day 2) - TikTok
- [ ] Day 10 - P03 missed-day, negation hook (AB-2 leg B, same footage as day 3) - YouTube Shorts
- [ ] Day 11 - P08 mobility-as-relief session scroll - YouTube Shorts
- [ ] Day 12 - P10 discipline inversion - TikTok (the one sanctioned test)
- [ ] Day 13 - P09 no-streaks contrarian, curiosity-led (AB-6 leg B, same footage as day 6) - TikTok
- [ ] Day 14 - Flex slot: double-down re-cut of the day-7 review's top angle, or P14 (no-signup demo) if nothing qualifies - TikTok

**Per-post pre-publication check (every asset, every day - from `cadence-14-day.md`):**
- [ ] Status lines true on the day of posting (pre-launch, no listing, no invented numbers; captions may say "iOS, not released yet" and nothing more optimistic).
- [ ] "Rep Today" in prose; no trademark/registration claim or implication.
- [ ] Any post that says "AI" carries the disclosure in the same post or its pinned first comment: at launch the policy tuner is deterministic on-device logic, and the only AI-generated text is one optional line with an offline fallback.
- [ ] No em dash characters, no health claims, no competitor-motive claims, no engagement-machinery language.
- [ ] Founder on camera for every first-person line; screen recordings are real device, real time, cuts only where declared.
- [ ] **Per-platform format:** TikTok / Reels / Shorts take the identical 9:16 vertical video; X takes the same clip with a text-forward caption within X's length limit, hook line first. Same creative and same frozen hook on every platform - only the caption wrapper adapts to length/format, never the hook itself.
- [ ] **Instagram:** no clickable link in the caption (bio link only); do not promise a tappable in-caption link. Keep hashtags modest and honest.
- [ ] **Reply to every substantive comment within 24h** - comment handling is part of the experiment, and comment language is logged as hook-mining input for the next window. Reply on all four platforms, but only TikTok + Shorts comment language feeds the adjudicated mining.

## Phase 4 - Read results with discipline

Follow `read-the-results.md`. Do not eyeball raw view counts.

- [ ] **Only TikTok (primary) and YouTube Shorts (secondary) adjudicate.** Instagram Reels and X numbers are read for interest and follower growth only - never use them to kill, promote, or rank an angle. At zero followers their follower-weighted, low-reach signal is not trustworthy, which is the entire reason they are mirrors and not test platforms. A strong Reels/X number is a nice-to-have, not evidence; a weak one is not a kill signal.
- [ ] A post counts only at **>=200 impressions** on its primary (adjudicating) platform; below that it is UNREAD and triggers no decision. IG/X impressions never count toward this floor.
- [ ] Signal is **relative rank within the angle bank** once >=10 posts have shipped, never absolute numbers.
- [ ] **Day-7 midpoint review** (days 1-5 only; days 6-7 too fresh): rank readable posts on their own pre-registered signal; the top angle earns the day-14 double-down IF it also cleared its threshold, not merely ranked first among weak posts. **Nothing can be killed at day 7** - kills require two consecutive weekly reads above the impression floor. Day 7 may only flag "at risk".
- [ ] If all of days 1-5 are unread: that is a distribution problem, not a message problem. Continue the calendar unchanged; check only mechanical causes (slot consistency, caption length, hashtag hygiene, video resolution). Do not rewrite any hook mid-window.
- [ ] **P10 special rule:** any drill-sergeant misreading in the comments retires the discipline-inversion angle permanently to the essay layer, whatever the numbers. No window-2 rerun.
- [ ] A/B pair resolves only if both legs are readable and the rank gap is large; otherwise the pair reposts in window 2 before any hook is declared the winner.
- [ ] Log every read into `creative-log.json` with dates and status (at-risk / killed / double-down).

---

## What NOT to do

- No treating Instagram Reels or X as the **test vehicle** - they are distribution mirrors only. Never let their follower-weighted, low-reach numbers kill or promote an angle; only TikTok + Shorts adjudicate.
- No follower or engagement buys - it poisons the honest-signal property that made TikTok and Shorts the pick.
- No streak / countdown / challenge / "day N of posting" framing in captions - the product refuses those mechanics.
- No overlay numbers the screen does not visibly justify.
- No paid install spend pre-launch (structurally unavailable with no listing; buys noise at small budgets).
- No product links or DMs in the three listening subreddits, ever.

---

## Reddit and creator on-ramps (parallel, low-volume)

- [ ] **Weekly Reddit listening pass:** mine verbatim pain language (starting friction, streak grief, paywall anger, time windows) with permalinks and fetch dates; feed it to the angle bank. Genuine non-promotional participation builds the account age + karma r/getdisciplined gates on. r/SideProject is the one sanctioned posting venue, and only after TestFlight exists.
- [ ] **Three honest creator DMs** (GMB Fitness, Hybrid Calisthenics, The Bioneer): ask-free (early access, a founder conversation, story material), never sponsorship; one follow-up each, then take the answer. Do not broaden into cold-DM spam.
