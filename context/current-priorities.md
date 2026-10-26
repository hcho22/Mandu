# Current Priorities

**2026-10-26 (hcho's call): Purvia is a portfolio piece, not an income bet.**
Its paid starter kit and the 10 buyer interviews are off the board; it keeps its #3 place in the order and its standing obligation to keep the eval receipts alive.
Older sections of this file that call Purvia a "live income bet" or "second income bet" predate this call.

**2026-09-29 ranking update (hcho's call): Immerse is ranked #2, immediately after Rep Today.**
Order is now Rep Today, Immerse, Purvia, then the job search as the parallel hedge.
Immerse (`projects/Immerse/`, repo `hcho22/Immerse`) was a planning baseline when ranked; full native v1 implementation started on 2026-10-02 (PR #7).
Purvia is now #3 but keeps its standing obligation: keep the eval schedules live and fix the E7 gate and RAGAS run.
Older sections of this file and other docs that call Purvia "#2" predate this change.
Local checkout: `/Users/hcho/Developer/fm_private/firstmate-private/projects/Immerse`.

**2026-10-26 verified review (order unchanged; later that day hcho made gr0wthlab and Mandu private and called Purvia a portfolio piece):**

- **Repo visibility:** at the morning review all five repos were public. `hcho22/gr0wthlab` had been private on the morning of 10-23 and was public again, changed by an action no record names, and `hcho22/Mandu` had been public since its creation on 2026-06-01, so everything committed here was publicly readable until then. **hcho made both private at about 10:40 PT on 10-26** (GitHub API: Mandu 17:40 UTC, gr0wthlab 17:41 UTC). RepToday, Immerse, and Purvia stay public. Copies cloned while gr0wthlab was public cannot be recalled.
- **Rep Today:** **Nothing has moved since 10-22.** GitHub is still at PR #214 (`f274ad0`, green, no CI run since), firstmate finished no Rep Today task, and hcho has said nothing about it in any session since 10-23. So the only TestFlight build is still 1.0.0 (4) for internal testers, the live Coach is still Worker `ecc259b4`, and the device checklist has no row newer than 10-13: PLAY-7 has no result, TELE-2 is unconfirmed, and COACH-5 still shows the old fail, all waiting on a build 5 that carries the trial-line (#202) and Today-spinner (#205) fixes. **Window 1 starts today with the old footer live:** both landing pages still say the name was never trademark-searched, and no task tracks the fix. The Waitlist job ran 70 times since 10-23, with 0 sign-ups at 10-26 09:30 PT. **New, and waiting on hcho only in chat:** P08's YouTube Shorts stop rule is judged on saves, which gr0wthlab never asks for, so its day-11 post (11-05) cannot be judged at the day-14 read (11-08); firstmate asks for "RepToday saves - look into it". The two CI flakes from 10-23 are still untracked. Remaining submission work is unchanged: on-device screenshots, nutrition labels, legal review of the privacy policy. See `projects/RepToday/log/2026-10-26.md`.
- **Immerse:** No repo change since 10-21 (`main` at `8eb6f50`, no PR, no CI run). **Gr0wthPilot's first real run wrote an untracked Candidate Package to `projects/Immerse/gtm/` on 10-25** (run `immerse-20261025-043407`, 471 files): it proposes the name Rewound (clearance UNVERIFIED), $4.99 a month or $29.99 a year, kill criteria K1-K8 with a hard park at Day 90, and a 14-day Test Kit plus Beta Cohort, none adopted, and expects no Immerse income in 2026. Gates are recorded only through `critic-1`: the site gate stalled because the run called `gp-chrome` by absolute path, which the sandbox does not exempt (Chrome itself works), and `launch-set` waits on hcho reading the Instagram and X profile-photo sizes. Its first ask is whether Immerse runs now or stays listening-only. **The formal phone pass has still not run** (candidate `8a104e1`, 42 scenarios), and the package now makes it the gate before any public page. Tracker unchanged (10 of 253). See `projects/Immerse/log/2026-10-26.md`.
- **Purvia:** **Nothing changed on GitHub or at firstmate since 10-16** (`main` still `9f57976`, no run since 10-16 14:29 UTC, 0 open issues, Supabase `agentic_rag` still `INACTIVE` by hcho's "leave it paused"). The four PRs hcho merged on 10-15 PT (#182 RAGAS pins and stem-prefix tier, #184 E7 offline judge, #186 live answer gate on gpt-4o-mini, #185 monthly cadence) are still unproven on `main`, which shows the 10-11 E7 breach and the 10-04 RAGAS failure until **the first scheduled run on the fixes, 2026-11-01 (Saturday 10-31, 19:00-23:00 PDT); its crons, secrets, and ruleset are verified in place**. **All 18 Purvia Master profile Claims need a re-read from those snapshots by 11-03**: 19 numbers from 10-08 are already stale and the 13 numbers from 10-20 go stale on 11-04. **hcho's call on 10-26: "purvia: portfolio piece"**, so the paid kit and the 10 buyer interviews (0 done) are off the board. See `projects/Purvia/log/2026-10-26.md`.
- **Job search:** **Still six applications, and nothing new recorded since 10-23**: three on 10-14 (OpenRouter Fit 5, Arbiter AI Fit 4, Disney SE II GenAI Fit 4) and three on 10-20 (MiniMed Senior SDET Fit 4, Syllo Fit 4, AssemblyAI Fit 4), all six postings still listed. The week of 10-19 closed at 3 of 5, the second week in a row at 3, and the week of 10-26 is at 0. Lane mix is 1 software quality, 2 AI quality, 3 AI product, against a 40/35/25 target. No responses recorded (email not searched); the 10-14 batch reaches two weeks on 10-28. 15 open, unapplied Fit 4 roles remain now that PwC's AI Senior Associate is off its board; MiniMed's Senior Software Quality Engineer, the only software quality role, closes 10-30. **None of the 61 stale Master profile numbers has been re-read (now 18 days old), so `build_packet.py` still refuses any packet that cites them; the weekly scan due 10-26 has not run.** See `projects/Job_Search/log/2026-10-26.md`.
- **gr0wthlab (tracked, not ranked):** **The first scheduled run did not happen.** The LaunchAgent fired at 16:00 on 10-25, but the run refused to start because `hcho22/gr0wthlab` is **public again**. GitHub traffic shows outside clones (15 by 8 on 10-23, 10 by 10 on 10-24) of a history that holds his 10-16 and 10-19 records (15 decisions with reasons, the sitting, Drafts, run reports); a key and token scan found none. A refused start earns no retry and writes no run report, so the week's run waits for him: make the repo private, start a run on demand, then sit. No sitting happened and no post item was ever queued, so nothing was ready for day 1 at 10:00 today, and a run from today prepares days 2-14 only; keeping window 1's dates or moving `first_sitting` is his call. The production clone is still at `df34b86`, 4 commits behind `main` (`6776dd0`). The queue is unchanged since 10-19 (5 open), nothing approved is waiting for Mandu, and there is still no footage. One PR merged (#34, Mac-installed skills kept out of sessions), CI green, 73 of 99 PRD boxes, contract still version 8. A run costs about $0.05 to $0.12 at API prices, but Codex runs on hcho's ChatGPT sign-in, so nothing is billed per run. **hcho made the repo private at 10:41 PT on 10-26**; a refused start gets no retry, so the week's run still waits for him to start it on demand (`~/gr0wthlab/src/bin/gr0wthlab run`), then sit. See `projects/gr0wthlab/log/2026-10-26.md`.

_Last verified: 2026-10-26. Update priority order only when hcho's focus shifts._

**ACTIVE CHECKOUTS (verified 2026-10-26): `/Users/hcho/Developer/FM_Private/firstmate-private/projects/{RepToday,Immerse,Purvia,gr0wthlab}`.**
firstmate runs from `firstmate-private`; all four checkouts there are clean and in sync with GitHub: RepToday at `f274ad0`, Immerse at `8eb6f50`, Purvia at `9f57976`, and gr0wthlab at `6776dd0`.
Immerse's local worktrees (`~/.treehouse/Immerse-3833fe/`) hold nothing unmerged.
gr0wthlab's production clone is `~/gr0wthlab` (since 2026-10-16); Mandu only reads it. It is at `df34b86` (10-19), 4 commits behind `main`, because the 10-25 run that would have fast-forwarded it refused to start.
**hcho's own Rep Today checkout `/Users/hcho/Developer/RepToday` is in use, not retired**, and is at `fff7314` (PR #200), 14 PRs behind `main`, with his local Release scheme change and two stashes; it looks like the checkout he builds to his phone from.
The 2026-08-05 home `/Users/hcho/firstmate` stopped on 2026-09-24 and is superseded: its RepToday checkout is still frozen at PR #168 with seven modified files and two stashes, and its Purvia checkout has two untracked items; preserve or discard those before deleting it.
The full GTM package lives in Mandu at `projects/RepToday/gtm/` (Mandu is private since 2026-10-26 and was public before that); the development repo retains `gtm/03-site/` as the canonical deployable public-site source.

**🗓️ 2026-09-14 UPDATE (RepToday synced through PR #155).**
- **Production telemetry is live-wired (#154).** Release targets Convex production deployment
  `sensible-spider-810`; the private token stays in the captain-owned macOS Keychain and is injected
  only by `tools/archive-release.sh`. Production and optimized Release validation proved opted-in
  rows persist and opt-out creates zero requests. Remaining measurement work is the TestFlight
  US-T13 reconciliation; known undercounts remain for in-flight events lost on suspension and later
  trial-to-paid conversions.
- **The premium Coach moved to OpenAI `gpt-5.6-luna` (#153).** The stateless, bounded boundary is
  unchanged in spirit: the deterministic engine owns every workout; Coach content and a separate
  rotating safety pseudonym go through Rep Today's proxy; `store: false` and standard retention are
  disclosed. The production Coach endpoint is still empty, so the feature remains unavailable in
  shipping builds until deployed.
- **Earned Strength Phase now persists (#155).** Completion writes a newly earned phase, app-open
  reconciliation repairs pre-existing qualified histories before phase-dependent tabs load, and the
  shared user persistence boundary prevents `.strength` from being downgraded by stale aggregate
  saves. Earning criteria are unchanged.
- **Active focus:** submission and PMF execution, not another product wave - publish the reviewed
  privacy source, finish legal/App Store fields, capture real-device screenshots and the iPhone XS
  latency result, decide whether to deploy the optional Coach, then run TestFlight + US-T13/K8.

**🗓️ 2026-08-21 UPDATE (Purvia repo pulled + status re-synced).**
Firstmate checkout of Purvia pulled to `origin/main` HEAD `14de073` (PR #120). Two things
since 08-11, and one corrects the optimism below:
- **New Luna model-migration workstream (US-120-124, PRs #115-120):** the retrieval eval
  **answerer moved to `gpt-5.6-luna`** (#115) with **judges + aux-helpers deliberately unchanged**
  (ADR-0012), a boot-time warning when an unpinned helper would inherit the temperature-refusing
  answerer (#116), a model-neutral answerer/helper role-split doc (#118), and a new
  **`JUDGE_REASONING_EFFORT` knob** on both runtime deflection gates (ADR-0013, #120). Eval-infra
  work, not launch prep.
- **⚠️ Precondition 1 regressed - correct the "effectively resolved" line below.** The auto-merge
  publish (#109) **silently broke from 08-12** (`EVAL_PUBLISH_TOKEN` empty), stranding 17 nights of
  receipts on branches with `main` frozen a week - kill-criterion-4 again. #111 backfilled them
  byte-for-byte; #112 added a named-cause preflight + auto-filed alarm issue. **But it is stranded
  again as of 08-21:** 08-20/08-21 nightlies sit on `eval-publish/*` branches, newest receipt on
  `main` is 08-19, token still unfixed. The evals run **green** (08-21 permissions-scale = 1.000
  across all cells on its stranded branch); only publishing-to-`main` fails. This time the alarm
  **worked** - open issues **#113/#114** flag it. **Owner action:** set a valid fine-grained
  `EVAL_PUBLISH_TOKEN` (Contents + PRs read/write), re-run, land the stranded snapshots, then
  delete the branches. Preconditions 3 and 6 stay green; precondition 1 is **not** green until the
  series publishes cleanly for several consecutive nights.

**🗓️ 2026-08-11 UPDATE (both projects advanced the same day).**
- **Rep Today** (firstmate `main`): **#93** pre-registered the **K8 wedge-comprehension coding
  rubric** in `gtm/` before the first cohort - this closes the marketing-checklist Track A "K8
  rubric" item and one half of the thesis's standing open owner slot (naming the non-founder
  *coder* who applies it is still open). **#94** prescribes **one set per Movement Practice
  stretch** (engine correction). Both land on top of #88-#92 (privacy policy hosted + wired,
  nutrition-label spec, latency-benchmark harness) already recorded below. Provisioning + assets
  remain the active focus; no code build is gating.
- **Purvia is NOT idle - it moved today, and its launch preconditions are clearing.** Four items
  landed: **#107** `SECURITY.md` + private vulnerability reporting → **precondition 6 GREEN**;
  **#108** security gates report on every PR (dropped the path filter) → **precondition 3 step 1**;
  **#109** nightly evals publish via **auto-merge PR** (needed once branch protection blocks direct
  push); and a **branch-protection ruleset on `main`** requiring the E6/E7 + AU4 checks with no
  bypass (repo setting) → **precondition 3 (branch protection) COMPLETE / GREEN**. Verified
  independently: the **nightly series is publishing again** (08-05/09/10/11) and the
  **permissions-scale nightly for 2026-08-11 is GREEN (1.000 across all cells)**, not the 0.000
  the text below still describes - so **precondition 1 is effectively resolved too**. Net:
  **8 RED → ~4-5 RED** (1, 3, 6 cleared; 2 likely). The "receipts rotting / kill criterion 4
  half-true / idle since 07-16" framing throughout this file is now stale. Still open: USPTO
  clearance (4), founder-bio verification (5), repo hygiene (7), pre-launch career read (8), and
  confirming the README all-1.000 table is dated (2).

**⭐ PRIORITY CHANGE (2026-08-02, hcho's call): Rep Today is now #1, Purvia #2.**
The reasoning, in hcho's words: Purvia is the stronger portfolio piece and may well be what
lands an AI role, but **Rep Today is the more likely source of near-term income**. The move
is a bet on speed-to-market - Rep Today is a finished app that can be in front of real users
in weeks, while Purvia's revenue path has been stalled on an unreachable buyer for six weeks
(0 of 10 interviews). The goal for this cycle is explicit: **launch Rep Today and find out
whether there is PMF**, judged against the thesis's pre-registered kill criteria rather than
by feel. Purvia stays a live income bet, not portfolio-only - it is ranked second, not
shelved, so it is still standing if Rep Today's kill criteria fire. Full sequencing, the
two mandatory builds, and the K1-K8 gates are in item 1 below. Logged in `decisions/log.md`.

**✅ FUNNEL INSTRUMENTATION CODE-COMPLETE (US-T01-T13, all on `main` 2026-08-10; PRs #69-#83).**
Gate one of the two-build pre-launch gate is done. All 13 pre-registered events now emit:
app-entry (US-T07, #76), onboarding (US-T08, #77), `ready_screen_shown`+`generation_ms`
(US-T09, #78), session lifecycle (US-T10, #79), `week_active` (US-T11, #80), monetization
(US-T12, #81), plus the US-T13 reconciliation harness (#82) and a shared-secret + rate-limit
abuse guard on `POST /logEvent` (#83). PRD synced: **96/103 boxes checked.** The pipeline that
was "built but emits nothing" through US-T06 now genuinely collects.
**The 7 open boxes are all US-T13's cohort-dependent reconciliation** - comparing the pipeline's
records against a non-founder coder's observations of the moderated TestFlight cohort. That is a
launch-time verification activity, not a build; it cannot run until the TestFlight cohort exists,
so "all US-Txx *implementations* done" is exactly the honest state.

**✅ BOTH MANDATORY BUILDS DONE - the app is now build-complete for submission.** Account
deletion (US-AD01-AD06) shipped as dev-repo **#86** (2026-08-10): `AccountDeletionService` +
view model, a Delete Account flow added to the US-T06 `SettingsView`, the bulk delete methods,
and **US-AD05 as Option (a)** (`getCredentialState` + on-device Apple-ID guidance, no revoke
proxy), with service/view-model/UI tests. That was the last App Store 5.1.1(v) blocker, and with
instrumentation (US-T01-T13) already done, **no mandatory code build remains.**

**⭐ ACTIVE FOCUS is now SUBMISSION + ASSETS, not building.** The path to actually submitting
and running the PMF test:
- ⬜ **Capture the iPhone XS / iOS 17 real-hardware p95** to substantiate "under 100ms" (or change
  the number everywhere). #92 landed the harness + a strong Simulator-proxy signal, but that is
  explicitly not device evidence; it blocks every asset carrying the claim, incl. the App Store
  listing.
- ✅ **Production Convex deployment + private Release token are provisioned and validated** (#154).
- ⬜ **App Store submission mechanics:** real on-device screenshots (Guideline 2.3.3), confirm
  pricing, enter the authored nutrition labels into App Store Connect (record + name already
  reserved).
- ⬜ **Stand up the waitlist** (the last Gate 0 marketing item; name/handles/domain all done).
- Then **TestFlight** → at which point US-T13's reconciliation and the K8 wedge cohort can finally
  run.

**The three armed pre-publication items, updated 2026-08-11** (dev-repo #88-#92; see the marketing
checklist and the GTM `08-redteam/pre-publication-checklist.md`):
(1) ✅ **Privacy policy authored + hosted** - live at `reptoday.app/privacy` (Cloudflare Worker),
the in-app `LegalLinks.privacyPolicy` rewired from the `example.com` placeholder to the real URL
(onboarding, Settings, paywall), contact email set (#89), FAQ linked (#90), and the App Store
**nutrition-label spec authored** (#91) - to be entered into App Store Connect at submission. This
also means **`reptoday.app` is now registered and live**, closing the Gate 0 domain item.
(2) 🔄 **Site FAQ + event schema + nutrition label reconciled to one story** - largely done: FAQ
now links the hosted policy (#90), label spec authored (#91); remaining is confirming the FAQ names
the opt-out on the final emitting build and entering the labels at submission.
(3) ✅ **Production Convex deployment + private Release token provisioned and validated** (#154,
2026-09-01). The source keeps the Release token empty; `tools/archive-release.sh` injects it from
the captain-owned Keychain without committing or printing it.
**Also (Gate 1, still open):** the "under 100ms" benchmark got a re-runnable harness + a strong
Simulator-proxy signal (p95 ~2.7ms, ≈36x margin) in #92, but the record is explicit the proxy is
"not evidence for a device latency claim" - the **iPhone XS / iOS 17 real-hardware p95 is still the
outstanding blocker** and the claim must not be published until it passes.

**Transport correction (2026-08-05):** the US-T01 spike returned a **no-go on `convex-swift`**
(it ships an arm64-only xcframework, so it cannot build for the Intel host's Simulator). Adopted
transport is a **Convex HTTP action (`POST /logEvent`) reached by a plain `URLSession` POST -
zero new Swift Package dependencies** (Lottie stays the only third-party package). This corrects
both the "self-built Convex ingest-only pipeline" bullet just below and the 2026-08-04 decision
log, which named `convex-swift` as the new dependency; the pipeline is still Convex-backed and
ingest-only, just reached over plain HTTPS rather than via an SDK.

Two decisions in that PRD supersede what this file said on 2026-08-02, both reconciled below
(item 1(a)):
- **Approach: a self-built Convex ingest-only pipeline, not on-device aggregation.** Events
  do leave the device, but only anonymous per-install usage counts (random UUID, no identity,
  no IDFA, no ATT). The privacy story holds because no shipped copy ever promised "nothing
  leaves the device" - that phrase lived only in internal notes; the shipped claims
  (generated on-device, no account, history on your device) stay literally true.
- **Consent: opt-out, not opt-in.** On by default, disclosed in onboarding + the privacy
  policy, one Settings toggle, zero emission when off. Rationale is sample size: at ~90
  installs/week and ~30% opt-in acceptance, a single cohort would need 7+ weeks to reach the
  thesis's 200-user floor, leaving the week-8/12 checkpoints reading a tiny self-selected
  sample. This **reverses the "explicit opt-in" line I wrote on 2026-08-02.**

Account deletion (US-AD01-AD06) remains a mandatory gate, just sequenced second now.

---

**Now (2026-08-02, from a dev-repo sync of both projects).** Two corrections to what this file said:

⛔ **Rep Today has one mandatory build left, and it is a hard App Store rejection blocker.**
An audit on 2026-07-31 found the app ships Sign in with Apple with **zero account-deletion path**
(no Delete Account, no Delete my data, no reachable sign-out; the Profile tab is still a
placeholder), which violates **App Store Guideline 5.1.1(v)**. Optional sign-in does not exempt
it - Apple treats *supporting account creation* as triggering the requirement. The teardown
capability exists only as unreachable dead code, and the Keychain identifier survives reinstall,
so a partial implementation resurrects deleted identities. PRD is implementation-ready
(`projects/RepToday/01-prd-account-deletion_260731.md`, US-AD01-AD06), **not started**. This
directly overturns the "next step is not more build" line below, and it gates every other
pre-submission item (privacy policy, App Store Connect record, trademark clearance, on-device
screenshots). **This is the single highest-leverage unblocked task on the board.**

✅ **Rep Today Epic O complete (US-O01-O04, 2026-07-19 → 2026-07-31)** plus TestFlight
submission prep. Post-v6 refinements added and finished after the MVP closed: Lottie demo seam
(#62), fitness-level Start Seed with the library grown 42 → 57 movements, a per-side work model
and a set-aware swap (`a048b86`), the session timer redesign - clock hidden, per-exercise Hold
Timer (#66), imperial onboarding units plus a new out-of-process `RepTodayUITests` scheme (#67),
and Progress-tab repairs (#68). **Signing is done:** `DEVELOPMENT_TEAM`, app icon, and
distribution entitlements landed 2026-07-30 (#64/#65), so entitlement-gated paths build for
device. ~829 unit tests plus the new XCUITest bundle.

✅ **Purvia go-to-market launch package DONE (2026-07-16, `.claude/launch/`, gitignored).** A
sourced, red-teamed launch build: a falsifiable `THESIS.md`, a 385-line red-team dossier, a
per-claim evidence ledger, brand guidelines + marks + tokens, an unpublished landing site, a
datasheet, profile assets, and a content calendar hard-gated on **eight RED launch
preconditions**. Three things in it change the plan: (1) **the buyer moved** - from
"agency/freelance devs" to "a production-minded engineer or 2-5 person team adding RAG to a
real multi-user product," with agencies *explicitly excluded*, which contradicts the framing in
item 1 below and needs an hcho call; (2) **pricing came off every surface** after the red team
called a priced-but-empty tier "a price tag on an empty box" - and the deeper constraint is that
everything in the repo is MIT and irrevocably granted, so a paid tier can only ever gate work
that does not exist yet; (3) **the pitch is no longer "adopt my kit"** but "you'll build the
retrieval loop yourself anyway - what you won't cheaply build is the proof."

⚠️ **[SUPERSEDED 2026-08-11 - see the top update block: the nightly is publishing again
(08-05/09/10/11) and the permissions-scale benchmark is GREEN at 1.000, so this "idle / receipts
rotting" read no longer holds; preconditions 1/3/6 cleared 2026-08-11.]** ~~Purvia has been idle
since 2026-07-16, and its own kill criterion 4 is half-true.~~ The
nightly eval series stopped publishing on 07-16, and the permissions-scale benchmark has been red
(0.000 in every cell) since 2026-06-19. The thesis names exactly this as a kill signal; it does
not fire only because nobody is reading the artifacts yet. That is the same "publication is not
detection" failure the launch package sells its centerpiece lesson from, now on its third run.
Restarting the nightly and dating the README's stale all-1.000 table are preconditions 1 and 2
and the cheapest credibility items on the list. **Buyer validation is unchanged at 0 of 10
interviews** - the constraint was never the marketing asset.

---

**Previously (by 2026-07-18), per hcho 2026-07-12:** finish both in-flight PRDs. ✅ **BOTH DONE.**
✅ **Agentic RAG retrieval-quality pass DONE** (2026-07-13, two days early - all six
stories US-113-118 merged, manual QA passed).
✅ **FitSnack v6 MVP DONE** (2026-07-14, four days early - final 8 stories US-L02, M01-M02,
N01-N05 merged; all epics A-N shipped). Immediately followed by the **FitSnack → Rep Today
rebrand** (US-001-009, PRs #52-#60, complete 2026-07-14; 667/667 tests green). Both build
tracks for the week are closed. ✅ **Rep Today GO-TO-MARKET PACKAGE DONE (2026-07-16,
dev-repo PR #61):** a full sourced, red-teamed, Rep Today-branded GTM package
(`/Users/hcho/firstmate/projects/RepToday/gtm/`, front door `gtm/recap.html`) - research (139 cited
URLs), naming tournament + brand guidelines, landing site, 48s launch video, investment
thesis with kill criteria, an ASO-led channel plan, a 55-objection red-team dossier, App
Store assets + social launch kit; self-graded 2026-07-15, honesty guardrails held (pre-launch,
zero users/downloads/revenue, nothing published). It supersedes the run-1 GTM plan. ~~Rep Today's
next step is not more build or planning~~ **- overturned 2026-07-31 by the account-deletion
audit; see the block at the top.** Signing/`DEVELOPMENT_TEAM` cleared 2026-07-30; App Store
Connect record, privacy-policy URL, and trademark + App Store name clearance remain open behind
the deletion build, then the channel test against the thesis kill criteria. With both passes closed, Agentic RAG returns to purely validation
(the standing #1). ✅ **Purvia rebrand DONE (2026-07-17):** the product's
first real brand shipped - a tight display-only rename (vendor-facing "Agentic RAG"
strings → "Purvia") plus naming ADR-0011 and the GitHub repo rename to Purvia;
US-001-007 merged (dev-repo PRs #88-92), zero behavior/RLS/contract change, technical
namespace untouched. Source PRD `projects/Agentic_RAG/raw/prd-rebrand-purvia-2026-07-14.md`.
With that closed there is now zero in-flight build; Agentic RAG is purely validation.

1. **Rep Today as the primary short-term income bet - ship it and test PMF (top focus,
   set 2026-08-02):** discipline-first micro-workout iOS app, freemium (free unlimited core
   loop, premium "depth" paywall via StoreKit 2). Promoted from #2 on hcho's call: Purvia is
   the stronger portfolio piece and the better job-search asset, but **Rep Today is the
   faster path to actual dollars** - it is a finished app that can be in front of real users
   in weeks, against a B2B kit whose buyer has not been reachable in six weeks of trying.
   The goal for this cycle is not more product: **get it launched and find out whether there
   is PMF**, against pre-registered kill criteria rather than vibes.

   **The path to the PMF test, in dependency order. Nothing below can be skipped or
   reordered.**

   **(a) Two builds, both mandatory before anyone can use the app. ✅ BOTH DONE (2026-08-10):
   instrumentation (US-T01-T13) and account deletion (US-AD01-AD06). No mandatory code build
   remains; what gates submission now is provisioning + assets (top block).**
   - **✅ Funnel instrumentation (US-T01-T13) - CODE-COMPLETE on `main` 2026-08-10** (PRs
     #69-#83, 96/103 PRD boxes checked). A **Convex-backed, ingest-only** pipeline for the **13
     pre-registered events** (from `gtm/06-channels/event-metric-schema.md`), strictly
     fire-and-forget so the offline core loop is never touched, keyed by an anonymous per-install
     UUID in `UserDefaults` (never Keychain), **opt-out** consent with a real `SettingsView` +
     onboarding disclosure, **zero new Swift Package dependencies** (Convex HTTP action reached by
     `URLSession`; `convex-swift` no-go'd on the Intel Simulator), and a shared-secret +
     rate-limit abuse guard on `POST /logEvent` (#83). All 13 events now emit: app-entry (T07),
     onboarding (T08), `ready_screen_shown`+`generation_ms` (T09), session lifecycle (T10),
     `week_active` (T11), monetization (T12). **The 7 open boxes are all US-T13's
     cohort-dependent reconciliation** - line-by-line comparison of the pipeline's records against
     a non-founder coder's observations of the moderated TestFlight cohort. That is a launch-time
     verification, not a build, and cannot run until the cohort exists; the *harness* for it
     shipped (#82). **Bonus delivered:** `ready_screen_shown.generation_ms` (US-T09) is the
     on-device benchmark that substantiates the "under 100ms" marketing claim - though the claim
     still needs a real-hardware p95 recorded (pre-pub gate). **Emission being live now arms the
     three pre-publication items in the top block** (privacy policy hosted; site/schema/label
     reconciled before any emitting build ships; production Convex deployment + shared secret
     provisioned).
   - **✅ Account deletion (US-AD01-AD06) - DONE** (dev-repo **#86**, 2026-08-10), the last App
     Store 5.1.1(v) blocker. Shipped in one flow: `AccountDeletionService` + `AccountDeletionViewModel`,
     a Delete Account row that **extends the US-T06 `SettingsView`** (not a second surface), the
     bulk delete methods (`deleteAllLogs()`, SessionPolicy/ActiveSession deletes), and **US-AD05 as
     Option (a)** - `getCredentialState` + on-device Apple-ID guidance, no revoke proxy, no backend.
     Backed by `AccountDeletionServiceTests` (276 lines), a view-model test, and a UI test. PRD at
     `projects/RepToday/01-prd-account-deletion_260731.md`. **With this, both mandatory builds are
     done and no mandatory code build remains** - see the top block for the provisioning/assets
     path to submission.

   **(b) Clear the name and the legal surface.** USPTO trademark search for "Rep Today" plus
   the App Store Connect record and name reservation for "Rep Today, Rest Tomorrow" - both
   still UNVERIFIED, and both block *everything public*. Author and host the privacy policy.
   Do **not** buy reptoday.com ($3,895, investor-held); reptoday.app is available.

   **(c) Run the moderated TestFlight cohort - this is the actual PMF test, and it is
   cheapest first.** The thesis puts this ahead of any public launch for a reason: 20-50
   testers, K8 coding rubric frozen *before* the first session, moderated first-run
   recordings coded by someone who is not hcho. If observed first runs do not show
   comprehension of "it's already ready when you open it," nothing downstream matters and the
   fix costs a design iteration instead of a burned launch. Also capture real on-device
   screenshots here (Guideline 2.3.3 - the marketing comps are not submission assets).

   **(d) Then launch, ASO-led, and read the kill criteria on fixed dates.** The channel plan
   ranks App Store search #1 because "micro workout" is near-empty whitespace and it is the
   only channel that works without founder attention. Reviews at week 8 and week 12.

   **The pre-registered PMF gates (from the thesis; no rate judged on fewer than 200 users):**

   | # | Metric | Expected | Kill line |
   |---|---|---|---|
   | K1 | Onboarding → first session | 45-60% | Below 35% after two fix iterations |
   | K2 | D7 return | 12-20% | At or below 10% |
   | K3 | D30 return | 6-12% | At or below 5% |
   | K4 | Week-4 weekly active exercisers / installs | 15-35% | Below 10% at week 8 |
   | K5 | Organic installs/week | ~90/week steady state | 4-week average below 90 |
   | K6 | Trial starts / installs | 3-7% | Below 1.5% |
   | K7 | Free-to-paid (day-35) | 1.5-3% | Below 1% at month 3 |
   | K8 | Wedge is perceived unprompted | - | >50% hunt for a workout list, or <30% mention ready-on-open |

   Any one firing is stop-and-diagnose. Two at once, or K1/K8 at all, is walk away - that is
   the premise failing, not the execution. **Retention landing at category median counts as
   failure, not survival**; the bet requires beating the medians materially. Two owner slots
   are still unfilled and should be filled before launch: the non-founder K8 coder, and the
   outside person who holds the walk-away call.

   **Honest framing, unchanged:** the corrected funnel math needs 10-20k installs/month
   sustained for this to be income-relevant. Until the gates clear, the truthful label is
   "portfolio asset with revenue upside." Promoting it to #1 is a bet on speed-to-market and
   on getting a real answer, not a claim that the income is likely.

   **Background:** MVP build complete 2026-07-14 (all epics A-N against the v6 PRD,
   Apple-native so near-zero hosting cost); rebranded FitSnack → Rep Today 2026-07-14 with
   `com.reptoday.app` baked in pre-public; Epic O post-v6 refinements complete 2026-07-31;
   signing/`DEVELOPMENT_TEAM` done 2026-07-30; GTM package complete 2026-07-16 (dev-repo
   PR #61, 139 cited URLs, naming tournament, brand guidelines, landing site, 48s launch
   video, investment thesis with kill criteria, ASO-led channel plan, 55-objection red-team
   dossier, App Store assets, social launch kit; nothing published or purchased, zero
   fabricated stats). Still feeds the build: PRD US-H01 amendment recommended (per-day score
   credit, so "miss a day, your score dents" stays literally true). Two GTM-package assets
   need work before they ship: the 48s launch video's voiceover is macOS `say` TTS and must
   be re-recorded with a human voice, and the landing page is currently a deliberate dead end
   with no action on it.

2. **Purvia (Agentic RAG) Phase 2 as the flagship portfolio piece and the second income bet:**
   Model A, sell the starter kit, built in public. **Demoted from #1 on 2026-08-02, and the
   reason matters: it stays a live income bet, not portfolio-only** - the paid kit and the 10
   buyer interviews remain on the board, just behind Rep Today's launch. What changed is the
   honest read on *which* value is nearer: Purvia is the strongest evidence hcho can show an
   AI hiring manager, and that job-search leverage is now its most reliable payoff, while its
   revenue path has been blocked on an unreachable buyer for six weeks. If Rep Today's kill
   criteria fire, Purvia is still standing as a revenue path rather than something to restart.
   **⚠️ Buyer definition is contested as of
   2026-07-16:** this line says "agency/freelance AI devs," but the launch package's thesis
   narrows it to "a production-minded engineer or 2-5 person team adding RAG to a real
   multi-user product" and *explicitly excludes agencies*. Needs an hcho call, because it
   changes where the 10 interviews get sourced. **The full Phase 2
   implementation PRD is now complete (A-F, US-001-112, done 2026-07-07)**, so there is no
   core build left to compete for attention - focus is now *purely* validation, then gated
   productization. Done: post #1 published on X, waitlist live (Tally), 5-day campaign running
   (Days 1-2 out). Remaining validation = **book the 10 buyer interviews** (still 0; the
   constraint is no warm network, so route through communities hcho belongs to - FourthBrain,
   Omdena, r/RAG - plus campaign engagers and a free "permission-RAG teardown" on-ramp, not
   warm intros) and drive waitlist signups. Only after findings: P-series productization
   (template-ization, license/delivery, open-core split, landing page, threat-model) - the
   sole remaining build track, and it stays gated. **The 2026-07-16 launch package
   pre-answered three of those on paper:** the landing page exists unpublished, the
   positioning rewrite is done, and open-core got a hard constraint - everything in the repo
   is MIT and irrevocably granted, so a paid tier can only gate work that does not exist yet.
   Template-ization and the threat model are untouched. Observability O-series and F2/F3 are a
   later follow-up PRD. ~~**Maintenance debt now competes for this slot:** the nightly evals
   stopped 2026-07-16 and the permissions-scale benchmark has been red since 2026-06-19, which
   is the thesis's own kill criterion 4 in slow motion.~~ **[RESOLVED 2026-08-11: the nightly is
   publishing daily again (08-05/09/10/11) and the permissions-scale benchmark is back to 1.000;
   preconditions 3 (branch protection) and 6 (SECURITY.md) also cleared today via #107/#108/#109 +
   the ruleset. The cheapest-credibility maintenance debt is largely paid down.]** Restarting and
   annotating them was launch preconditions 1 and 2.
3. **Job search as the parallel income hedge:** sustained applications at 5/week against
   the verified target list, plus interview prep. Non-negotiable minimum given the 6-12 month runway.
   Three-lane targeting: software quality/systems validation; AI quality/evaluation; and
   AI product/integration/technical delivery. Start with an approximate 40/35/25 mix without
   padding weak matches; preserve qualified AI-builder roles and pitch the validation-to-software bridge honestly.
4. **Evals as the edge, not a study track:** express it through Purvia's eval harness
   (leak suite, escalation golden set, CI gate), not a standalone 20-hour study plan.
   Note the harness is currently unattended - see the maintenance-debt note in item 1. An
   eval story told from a series that stopped publishing is the weaker version of it.
5. **Second brain / AI OS:** lowest; an enabler, maintained not pushed.

## Demoted / paused

- **CreativeBridge:** portfolio-only; finish TestFlight opportunistically, not a focus.
- **CompeteIntel:** backlog/paused while Purvia and Rep Today are the product bets.

## Recently completed

- **F2F** and **HabitLoop** (unchanged; see archives/).

## Active deadlines

- Income by end of 2026 (app revenue or a full-time role).
- Purvia: ~~open-core public + waitlist (Q3 2026)~~ retired 2026-10-26, when hcho called Purvia a portfolio piece; the precondition history below is kept for the record. Public launch is hard-gated on the eight
  launch preconditions (nightly fixed, README dated, branch protection, USPTO clearance,
  bio verified, SECURITY.md, repo hygiene, career read). **As of 2026-08-11 three-to-four are
  green** - branch protection (#108 + ruleset), SECURITY.md/private vuln reporting (#107), and
  the nightly-fixed benchmark (permissions-scale back to 1.000, publishing daily); README-dated
  likely too. Remaining RED: USPTO clearance, bio verified, repo hygiene, career read. See the
  2026-08-11 update block at the top.
- Rep Today: App Store submission (date TBD). No code build is blocking as of 2026-10-26; TestFlight build 4
  exists and the Coach fixes are live. It waits on a build 5 from `main`, PLAY-7, TELE-2, COACH-5 and COACH-11
  on that build, and the submission assets (on-device screenshots, nutrition labels, privacy-policy legal review).
- Rep Today social PMF test: window 1 was due to start Monday 2026-10-26 at 10:00 (text-only screen recordings),
  but gr0wthlab's 10-25 scheduled run refused to start (repo public), so day 1 had nothing prepared. A run started
  on 10-26 prepares days 2-14 (10-27 to 11-08); a run on 10-27 starts at day 3.
- Rep Today P08: decide the YouTube Shorts saves gap before the day-11 post on 2026-11-05 (day-14 read 11-08).
- Job search: MiniMed Senior Software Quality Engineer closes Friday 2026-10-30; the 10-14 applications reach two
  weeks on 2026-10-28.
- Purvia: first monthly eval run on the 10-15 fixes is 2026-11-01 (fires Saturday 10-31, 19:00-23:00 PDT); refresh
  all 18 Purvia Master profile Claims from those snapshots by 2026-11-03.
