# Rep Today - Marketing Launch Checklist

**Created:** 2026-08-07
**Source of truth:** the GTM package at `/Users/hcho/firstmate/projects/RepToday/gtm/` (v2, self-graded 2026-08-02). Nothing there is published, deployed, or purchased.
**Purpose:** turn the finished GTM package into an execution to-do. Check items off as they land; update the status line below when the picture shifts.

_Status: in progress. Gate 0 nearly clear (as of 2026-08-11): ✅ name cleared + reserved, ✅ handles secured, ✅ `reptoday.app` registered and live (serving the hosted privacy policy). **Remaining Gate 0: stand up the waitlist.** Privacy policy is hosted + wired (dev-repo #88-#91), so the biggest Track B pre-pub item is largely cleared too. Benchmark (Gate 1) has a harness + a strong Simulator-proxy signal but the real-device p95 is still outstanding._

---

## The two tracks (read this first)

The package splits marketing into two tracks with different gates:

- **Track A - organic content + waitlist** can start **now**, in parallel with finishing the build. The channel plan's doctrine is "continuous cadence, not a launch week" (`06-channels/channel-plan.md` §1c), and its #1 channel is organic short-form that needs no App Store listing. This is where "start marketing" actually begins.
- **Track B - launch-day channels** (ASO, TestFlight, Apple Ads, Show HN / Product Hunt) are **blocked** on the app being live - still behind two builds (instrumentation emissions US-T07-T13 and account deletion US-AD01-AD06) and the submission checklist.

**Recommended first move:** clear Gate 0, fix the two asset gates as needed, record the demo asset, then start the 14-day cadence. Do not let Track B compete for attention until the build is submittable.

---

## Gate 0 - clear before ANY public asset (small, founder-owned, days not weeks)

- [x] **USPTO trademark search for "Rep Today"** (ideally with counsel) + **App Store Connect name reservation**. **DONE 2026-08-07** - name cleared and reserved (the App ID `com.reptoday.app` was registered in the Developer portal as part of this, so the ASC app record could be created). This was the self-grade's stated "founder's next action" and it unblocks *everything public*. The "clearance UNVERIFIED" caveat that still appears throughout the GTM package (naming decision, recap banner, README, site footers, teaser, brand guidelines, screenshots README) can now be updated to reflect this.
- [x] **Secure the handles** - `@reptoday` on TikTok and YouTube (primary), plus Instagram / X defensively. **DONE 2026-08-07** - all four claimed (`@reptoday`). The TikTok + YouTube pair is what the PMF cadence actually posts to; IG/X held defensively against impersonation.
- [x] **Commit to `reptoday.app`** as the domain. **DONE (2026-08-11)** - registered and live; DNS resolves and it already serves the hosted privacy policy at `reptoday.app/privacy` (Cloudflare Worker, dev-repo #88). `reptoday.com` correctly **not** bought.
- [ ] **Stand up the waitlist.** It is the measurement spine of the whole plan ("pre-publication action #1") and does not exist yet. The landing page is built (`gtm/03-site/index.html`) but is a deliberate dead end - it needs exactly **one** low-pressure CTA (email capture) wired and hosted. First-party, web-side capture is the one funnel no iOS attribution constraint can degrade.

## Gate 1 - two asset fixes the self-grade flags (do when the asset ships)

- [ ] **Re-record the launch video voiceover** with a human voice (the founder's own is fine). Current VO is macOS `say` (Samantha) and reads as AI-slop in-feed. Reproducible: swap the `say` lines in `gtm/04-video/build/build.sh` for recorded aiff and re-run. *Blocks video publication only.*
- [ ] **Benchmark the "under 100ms" claim** on real hardware including the slowest supported device (iPhone XS / iOS 17). **In progress, NOT cleared (dev-repo #92):** the re-runnable XCTest harness landed (`SessionGenerationBenchmarkTests.swift`) and a **Simulator-proxy** run shows p95 ~2.7ms (≈36x margin) - encouraging, but the substantiation record itself says a Simulator time reflects the Mac's desktop CPU and is **"not evidence for a device latency claim."** The gating requirement - **iPhone XS / iOS 17 real-hardware p95** - is still outstanding, and the record is explicit: do not publish the "under 100ms" number until that row is filled. So this stays open, now with the method + harness + a strong proxy signal behind it. *Blocks any asset that uses the claim.*

---

## Track A - start the organic engine (the actual "start marketing")

Runs for a quarter, not a week. TikTok primary, YouTube Shorts secondary, identical content posted to both the same day.

- [~] **Pre-register the K8 wedge-comprehension rubric** (written coding criteria, 25+ observed first runs) and **name a non-founder coder** - before the first cohort. Standing open slot in the thesis. **Rubric DONE 2026-08-11 (dev-repo #93):** the written coding criteria are pre-registered in `gtm/` before any cohort. **Still open:** naming the non-founder coder who applies it.
- [ ] **Record the core cold-open demo asset** (real device, real time, cuts only where the shot list allows). It is reused across the whole kit and is Day 1 of the cadence.
- [x] **Post at one consistent 10:00 local slot** (the founder's decision of 2026-10-21) and never vary it during the window (holds time-of-day constant).
- [ ] **Run the 14-day cadence, window 1.** Fully specced day-by-day in `gtm/05-social-pmf/cadence-14-day.md` (16 angles, 6 A/B hook pairs, per-post pre-registered signals). Includes a **Day-7 midpoint gate** and a **Day-14 rebuild**.
- [ ] **Reddit listening protocol** - weekly read of r/fitness30plus, r/bodyweightfitness, r/getdisciplined (zero links, ever); mine verbatim pain language for hooks; build the account age + karma r/getdisciplined gates on. **Manually read each sub's self-promotion rules first.** r/SideProject is the one sanctioned posting venue, and only *after* TestFlight exists.
- [ ] **Personal-network waitlist asks** - identity-framed ("movement that fits the life you already have"), never loss-framed; tag the source per signup.
- [ ] **Three honest creator DMs** - GMB Fitness, Hybrid Calisthenics, The Bioneer. Ask-free (early access, a founder conversation, story material), never sponsorship. One follow-up each, then take the answer. Do not broaden into cold-DM spam - the list is three names because only three fit.

### Track A measurement discipline (so the test stays readable)

- [ ] **Honor the pre-registered K0 escalation ladder** - day-14 / week-8 / week-16. Already stated identically across the thesis, channel plan, and results guide; the job is to follow it, not re-derive it.
- [ ] At review time, **read K5 installs off App Store Connect units, not the telemetry `app_install` count.** US-T06 made collection opt-out, so an opted-out install is invisible to telemetry, and K5 is judged against an absolute floor (~90/week) - opt-outs deflate it one-for-one and it could fire with nothing wrong.
- [ ] **Check the opt-out revisit trigger** at each review: it becomes due the first time App Store Connect units and the telemetry install count both exist for the same period (the gap between them *is* the opt-out rate). Note the 200-user minimum-cohort floor now means 200 *consenting* users.

---

## Track B - launch-day (do NOT start yet; line up behind the build)

Blocked on the app being submittable. Sequenced:

1. [ ] **Finish the two mandatory builds** - instrumentation emissions US-T07-T13 (the funnel *must* be instrumented before TestFlight) and account deletion US-AD01-AD06 (App Store 5.1.1(v)). Tracked in `prd-funnel-instrumentation_260803.md` and `01-prd-account-deletion_260731.md`.
2. [x] **Author + host the privacy policy.** **DONE (dev-repo #88-#91, 2026-08-10):** hosted live at `reptoday.app/privacy` (Cloudflare Worker, source `gtm/03-site/privacy.html`), `LegalLinks.privacyPolicy` rewired from the `example.com` placeholder to the real URL (used by onboarding, Settings, and the paywall), contact email set to `reptoday.app@gmail.com` (#89), and the **App Store privacy nutrition-label spec authored** (#91, `gtm/08-redteam/app-store-privacy-labels.md`) aligned to the on-device / optional-iCloud / HealthKit-opt-in story plus the disclosed anonymous Usage Data (funnel PRD FR-12: not linked to identity, not used for tracking, no ATT, no IDFA). The label spec still has to be *entered* into App Store Connect at submission.
3. [~] **Reconcile the site FAQ + event schema + nutrition label to one story** - **largely done:** the FAQ's "Is my data sold?" answer now links the hosted policy (#90) and the nutrition-label spec is authored (#91). Remaining: confirm the FAQ copy names the opt-out once the final emitting build ships, and enter the labels in App Store Connect at submission. Still: **do not "helpfully" fix the live A/B site copy mid-test** if it would break comparability.
4. [ ] **App Store assets** - capture real on-device submission screenshots (Guideline 2.3.3; the comps in `gtm` are design references, not submission assets); confirm final pricing then regenerate screenshot 05 and the site pricing section. Listing title ("Rep Today"), subtitle ("Opens to a ready workout"), and the 99-char keyword field are already decided (`gtm/06-channels/channel-plan.md` A2). Consider adding the return-after-a-gap screen (strongest emotional differentiator).
5. [ ] **Verify every behavioral claim** in the site / video / screenshots against the actual approved binary before launch day.
6. [ ] **Then the launch beats:** TestFlight beta cohort (also the K8 moderated-cohort source) → r/SideProject feedback post → Show HN / Product Hunt one-shot → Apple Ads (cost-per-tap, no minimum, $100 starter credit; hold ~$350-400/mo until the listing is live). Paid stays a post-launch price-discovery tool, not a pre-launch signal source.

---

## What NOT to do (from the package)

- **No paid install spend pre-launch** - install ads are structurally unavailable with no listing, and at small budgets they buy noise, not signal (SKAN/AAK aggregation + learning-phase economics).
- **No follower/engagement buys** - poisons the honest-signal property that made TikTok and Shorts the pick.
- **No `reptoday.com` purchase**, no ASO tools (Apple's free keyword popularity data suffices at this scale).
- **No Instagram Reels or X as the PMF test vehicle** - Reels ranks on follower count (bad for a zero-follower account); X has the lowest 30-49 reach. Revisit Reels once a follower base exists.
- **No streak/countdown/challenge/"day N of posting" framing** in captions - the product refuses those mechanics; the marketing must too.
- **No health claims, no bro-fitness register, no "AI"-led messaging** (the policy tuner is deterministic on-device logic; only one optional line is LLM-generated, with an offline fallback - disclose it when a post says "AI").

---

## Open decision for hcho

The build still needs US-T07-T13 + account deletion before submission, and your time budget is ~25 hrs/week. **Do you start Track A now (organic + waitlist, in parallel with the build), or hold all marketing until the app is submittable?** The package's own doctrine says start the continuous cadence now and treat launch as one beat in it - but it is a real call given solo-founder attention. Everything in Track B is genuinely blocked regardless.
