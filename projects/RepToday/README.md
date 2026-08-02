# Rep Today

**One-liner:** A discipline-first micro-workout iOS app. Open it and a complete zero-equipment session (5-60 min) is already waiting - a deterministic on-device engine blends strength, mobility, and primal movement to land within ±1 min of your Default Duration. No browsing, no choosing, no thinking. Between sessions a daily-adaptive AI Programmer quietly rewrites each user's Session Policy (progression, pillar weighting, variety); it shapes the program, never the workout, and is never on the path to pressing start.

**Name:** Rebranded **FitSnack → Rep Today** on 2026-07-14, pre-public (FitSnack was trademark-blocked; "Nonzero" was an interim run-1 placeholder, now retired). App Store listing name: "Rep Today, Rest Tomorrow". The Mandu tracker folder was renamed `FitSnack → RepToday` on 2026-07-16 to match; the shipped app, module, identifiers (`com.reptoday.app`), and GitHub repo are all "Rep Today". See `prd-rebrand-fitsnack-to-rep-today_071426.md`. Trademark and App Store name clearance for "Rep Today" remain UNVERIFIED (the founder's next action, per the GTM package self-grade).

**Repo:** https://github.com/hcho22/reptoday (private; formerly `hcho22/FitSnack`, auto-redirects)

**Strategic role:** **Second income bet** alongside the Purvia (Agentic RAG) flagship, and an **AI-builder portfolio asset** for the job search. Where Purvia is the B2B starter kit sold to agency/freelance devs, Rep Today is the B2C consumer freemium play (see Monetization). The two run as parallel revenue paths under the same income-by-end-of-2026 north star; Purvia remains the primary flagship.

---

## Status

_Update this line as the project moves. Last reviewed: 2026-08-02._

- **⛔ NEW HARD SUBMISSION BLOCKER (opened 2026-07-31): account deletion is missing.** A build audit against **App Store Guideline 5.1.1(v)** found the app ships Sign in with Apple with **zero deletion path** - no "Delete Account", no "Delete my data", no reachable sign-out anywhere in the UI, and the Profile tab is still a `PlaceholderTabView`. Apple treats *supporting account creation* as triggering 5.1.1(v) regardless of whether sign-in is optional (it is - the app falls back to a local UUID). The teardown capability half-exists as unreachable dead code (`AppleAuthService.signOut()`, `CoreDataUserService.deleteCurrentUser()`, `AuthCredentialStore.clear()`, all called from tests only), and `SessionPolicyStore` has no delete method at all. The Keychain identifier **survives reinstall**, so leaving it resurrects a deleted identity. PRD is implementation-ready at `01-prd-account-deletion_260731.md` (US-D01-D06: Profile/Settings screen, bulk delete methods, `AccountDeletionService` orchestration, confirmation flow, Apple-credential guidance, optional HealthKit sample removal). **Not started.** This corrects the standing "Rep Today's next step is not more build" assumption: one mandatory build remains before submission is possible, and it gates the rest of the pre-publication checklist (privacy policy, App Store Connect record, trademark clearance, on-device screenshots).
- **✅ EPIC O - POST-v6 REFINEMENTS COMPLETE (US-O01-O04, 2026-07-19 → 2026-07-31).** Four refinement stories were added after the v6 MVP closed and all four landed:
  - **US-O01 - Lottie exercise-demo seam** with an SF-Symbol fallback (#62, 2026-07-19).
  - **US-O02 - fitness-level Start Seed** (`a048b86`, 2026-07-30): capped starting difficulty is now *seeded* rather than only clamped, the exercise library grew **42 → 57 movements** (fifteen Discipline-reachable difficulty 3-4 tiers so the seed band has real chains to rotate over), a **per-side work model** (a per-side movement is charged for both sides), and a **set-aware swap**. Also split the 358-line `CLAUDE.md` into `docs/implementation-log.md`, `docs/test-coverage.md`, and `docs/asset-attribution.md`.
  - **US-O03 - session timer redesign** (#66, 2026-07-30): the always-on session clock is **removed** from the player and rest overlay (the total is revealed once, on the completion summary; measurement is untouched), and timed exercises get a per-exercise **Hold Timer** that counts per-side legs separately. Both the hold and rest timers were collapsed onto one `Countdown` value type (~80 mirrored lines deleted), which is what made a long-standing rest-timer bug fall out as a consequence of the hold fix.
  - **US-O04 - imperial units in onboarding** (#67, 2026-07-31): height/weight collected in ft/in and lb, converted once at the boundary (the app stays metric behind the UI). Shipped a hand-rolled 44pt press-repeat stepper after the platform `Stepper` failed the touch-target floor, plus a new **`RepTodayUITests` XCUITest scheme** - the first place a production control is actually pressed rather than hosted.
  - Followed by **#68** (2026-07-31): Progress-tab calendar id collision, evidence-output portability, and VoiceOver repairs.
- **✅ TESTFLIGHT SUBMISSION PREP DONE (#64/#65, 2026-07-30):** 1024pt app icon, distribution entitlements, and `DEVELOPMENT_TEAM` **signing team now configured** - so entitlement-gated paths (Sign in with Apple, CloudKit sync, HealthKit writes, live purchases) build for device. This closes the signing half of the provisioning list; App Store Connect record, privacy-policy URL, and trademark clearance remain open, now behind the account-deletion blocker.
- **Test suite:** ~829 unit test functions in `RepTodayTests` plus the new out-of-process `RepTodayUITests` bundle. Evidence suites render production screens to PNGs under `artifacts/reports/<story>/` on an opt-in build setting.

- **✅ v6 MVP COMPLETE (2026-07-14), ahead of the 2026-07-18 deadline.** All epics A-N shipped and merged. The final eight stories landed on 2026-07-14: US-L02 (#44), US-M01 (#45), US-M02 (#46), US-N01-N05 (#47-#51). Then the app was **rebranded FitSnack → Rep Today** (US-001-009, PRs #52-#60) with the whole-repo guard passing at **667/667 tests green**.
- **✅ GO-TO-MARKET PACKAGE COMPLETE (2026-07-16, dev-repo PR #61).** A full Rep Today-branded GTM package (superseding the earlier Nonzero-era run-1 GTM plan) lives in the dev repo at `/Users/hcho/Developer/RepToday/gtm/` (front door `recap.html`). Self-graded 2026-07-15 after a red-team pass. Contents: sourced research with 139 cited URLs (competitor teardowns, review mining, category economics, ASO landscape, creator landscape, name collisions), a naming tournament + brand guidelines that passed a fresh-agent test, a landing site verified at mobile/desktop widths, a gated 48s launch video, an investment thesis with explicit kill criteria, a channel plan ranking **ASO #1** (owns the near-empty "micro workout" whitespace; title "Rep Today, Rest Tomorrow", subtitle "Opens to a ready workout"), a 55-objection red-team dossier (30 objections ship verbatim), App Store screenshots, a social launch kit, a review-response playbook, and an investor teaser. **Honesty guardrails held:** everything is local/static, nothing published/deployed/purchased; zero fabricated stats, users, or testimonials; the app is pre-launch (zero users, zero downloads, zero revenue). Its "next up is not more build" call was **partially overturned on 2026-07-31** by the account-deletion audit (see the blocker at the top of Status); signing/`DEVELOPMENT_TEAM` cleared on 2026-07-30, and App Store Connect record, real privacy-policy URL, and trademark + App Store name clearance remain open behind that build.
- **Phase:** MVP, clean rebuild, built story-by-story against the **v6 PRD** (`prd-fitsnack-mvp-v6_0702.md`, which supersedes the v5 `prd-fitsnack-mvp_0626.md`). v6 reframes the MVP as "the Discipline Loop with a daily-adaptive AI Programmer." The previous app (XP/badges/streaks, AI services, SwiftData) was removed and lives only in git history (commit `23fd56f`) as reference.
- **Current state (per the code repo, 2026-07-14): all epics A-N complete; rebrand complete.**
  - **Epic A - Foundation (✅ built):** scaffold, domain enums/models, CoreData stack, service protocols / ServiceContainer / app state.
  - **Epic B - Exercise Library (✅ built):** bundled ~38-movement JSON library + load/integrity-check service.
  - **Epic C - Deterministic Engine, Steps 1-7 + Swap (✅ built):** the full v5 pipeline, including the deterministic exercise swap (the old US-C08 is now folded into a built Epic C).
  - **Epic D - v6 Data Model & Session Policy Foundation (✅ done, US-D01-D04):** `User` gains `why`/`duration`/`coldStart`, `WorkoutLog` gains `requestedMinutes`/`wasReturn`, the always-valid `SessionPolicy`, and the `ReprogramTrigger` service seam.
  - **Epic E - Engine v6 Extensions (✅ done, US-E01-E06):** session shapes extended to 5-60 min, primal promoted to a first-class pillar, the engine consumes SessionPolicy levers, Step 0 cold-start override + capped Starting Difficulty, the Asymmetric Ramp, and the Return override + Re-entry Ramp.
  - **Epic F - AI Programmer at option (C) (✅ done, US-F01-F04):** US-F01 re-program trigger detection with Trigger Precedence (#26), US-F02 plateau diagnosis (Physical Stall vs Disengagement) (#27), US-F03 deterministic Session Policy re-weighting service (#29), US-F04 Default Duration learning + templated policy note (#28). This is the on-device, zero-LLM daily-adaptive AI Programmer that rewrites each user's `SessionPolicy` (never a workout, never on the start path), with a human-readable note explaining each change.
  - **Epic G - Cold-start & Variety Language (✅ done, US-G01-G04):** US-G01 capped Starting Difficulty seeding served gentle (#30), US-G02 First-Week Contrast enforcement (#31), US-G03 the Variety Language slice - the MVP's single LLM call, template-backed via the thin proxy with a deterministic fallback (#32), US-G04 cold-start handoff (#33).
  - **Epic H - Consistency & progression (✅ done, US-H01-H02):** US-H01 the forgiving, Return-protected Consistency Score (single miss dents but never zeroes; 5-min counts as a full show-up) (#34), US-H02 the earned-progression PhaseEvaluator (Strength Phase earned, never settable) (#35).
  - **Epic I - Onboarding (✅ done, US-I01):** the minimal v6 onboarding flow (#36) - collects profile/`why`/`sitsLong`/duration, seeds capped Starting Difficulty + `coldStart` + `SessionPolicy.default`, then routes straight to the Ready Screen with the first session pre-generated (no picker). Single-story epic by design; the detailed flow is deferred to Phase 2.
  - **Epic J - Ready Screen (✅ done, US-J01-J02):** pre-generated session + non-blocking duration chip (#37), felt-personalization (Variety Language line, Consistency, AI note) + re-program-on-open (#38).
  - **Epic K - Active Session (✅ done, US-K01-K04):** active session player (#39), rest timer with haptics (#40), in-session swap (#41), background and resume (#42).
  - **Epic L - Post-Session (✅ done, US-L01-L02):** US-L01 post-session summary and log write (#43); US-L02 rating and perceived-difficulty feedback that feeds the Asymmetric Ramp (#44).
  - **Epic M - Progress Tab (✅ done, US-M01-M02):** US-M01 session calendar + Consistency Score trend (#45); US-M02 pillar balance, chain position, personal bests, and premium gating (#46).
  - **Epic N - Apple Integrations & Thin Proxy (✅ done, US-N01-N05):** Sign in with Apple (#47), CloudKit sync/backup (#48), HealthKit write (#49), StoreKit 2 subscriptions + paywall (#50), and the thin stateless Variety Language proxy (#51).
  - **Epic O - Post-v6 Refinements (✅ done, US-O01-O04):** Lottie demo seam (#62), fitness-level Start Seed + per-side work model + set-aware swap (`a048b86`), session timer redesign / Hold Timer (#66), imperial onboarding units (#67). See the Epic O bullet under Status.
- **Remaining MVP build:** none from epics A-O. **One mandatory pre-submission build remains: account deletion (US-D01-D06), a hard App Store 5.1.1(v) rejection blocker.**
- **Next (in order):** (1) build account deletion, (2) finish pre-submission provisioning - App Store Connect record, privacy policy authored and hosted, trademark + App Store name clearance, on-device submission screenshots, (3) execute the GTM channel test against the thesis kill criteria.
- **Go-to-market (✅ package complete, pre-launch):** the full Rep Today GTM package is done and self-graded (dev-repo PR #61, `/Users/hcho/Developer/RepToday/gtm/`, front door `recap.html`) - see the GTM bullet under Status above. It supersedes both the Nonzero-era run-1 GTM plan (`run-1/gtm/plan.md`) and the earlier 2026-07-01 1-week social launch draft (`posts/01-social-1week-launch_260701.md`), folding their intent into a sourced, red-teamed package with a channel plan (ASO-led), a launch video, and an investment thesis with kill criteria. It remains a positioning + pre-launch asset: nothing is published, deployed, or purchased, and there is no app to download yet.

## Why this project / how it fits

- **Income bet #2 (B2C):** a consumer subscription app is a different revenue shape and a different buyer from the Agentic RAG kit, so it hedges the product path without competing for the same customer. Apple-native stack means near-zero hosting cost (the $99/yr Apple Developer account plus one free-tier stateless proxy for the single Variety Language LLM call).
- **AI-builder portfolio asset:** demonstrates shipped, end-to-end product engineering - SwiftUI + Observation, MVVM with protocol-based DI, CoreData/CloudKit, StoreKit 2, Sign in with Apple, HealthKit. v6 puts a genuine, safety-railed AI story *in the MVP itself*: a daily-adaptive **AI Programmer** that rewrites each user's Session Policy (shipped at **option (C)** - deterministic, on-device, zero LLM calls, templated note), plus one template-backed **LLM "Variety Language" slice** served through a thin stateless proxy (US-N05). The AI writes policy, never the session; the deterministic engine still assembles every workout offline in <100ms. This is a clean production-AI story - an async off-path programmer with a hard deterministic fallback - on top of the validation-rigor angle below.
- **Validation / quality angle (the cross-cutting edge):** the on-device engine is fully deterministic (no network, no LLM, <100ms) and backed by a broad test matrix - engine session-shape/staleness/timing-fit, Consistency Score edge cases (single-miss dents but never zeroes, 5-min counts as a full show-up), PhaseEvaluator promotion rules, persistence round-trips. This is the same validation-rigor differentiator hcho leads with elsewhere, expressed in a consumer app.

## Monetization

Freemium, paywall on **depth** not the core loop (the discipline promise stays free forever):

- **Free tier:** unlimited workouts forever, the full ~38-movement library, Consistency Score, weekly goal, basic history. Never gated.
- **Premium (~$7.99/month or ~$59.99/year, 14-day trial):** the depth layer - full analytics now; Strength-Phase programming, equipment variants, and AI language features as they land. Via StoreKit 2 (subscriptions, paywall, Restore Purchases).

## Product model

- **Two-phase journey:** every user starts in the **Discipline Phase** (consistency is the only goal). The **Strength Phase** is *earned* by sustaining the habit and progressing the movement chains - never user-selectable. At launch no user has earned it, so the MVP ships the Discipline-Phase experience with the `PhaseEvaluator` already in place.
- **Consistency, not gamification:** no XP/levels/badges in the MVP. A rolling, weighted **Consistency Score** replaces the brittle streak; `longestChain` is surfaced as pride, never a threat; all copy is identity-framed ("you're someone who moves").

## Tech stack

| Layer | Technology |
|-------|-----------|
| **Platform** | iOS 17.0+, Swift 5.9, Xcode 16.3; Bundle ID `com.reptoday.app`; `DEVELOPMENT_TEAM` configured (2026-07-30) |
| **UI** | SwiftUI with the Observation framework (`@Observable`, never `ObservableObject`/`@Published`) |
| **Architecture** | MVVM + protocol-based service injection (swap a mock for a real impl by changing one line in `ServiceContainer`) |
| **Persistence** | CoreData backed by `NSPersistentCloudKitContainer` (`CDUser`, `CDWorkoutLog`); local-only until CloudKit sync lands |
| **Engine** | Pure Swift, on-device, deterministic - no network, no LLM, <100ms |
| **Apple integrations** | Sign in with Apple, CloudKit (private DB sync), HealthKit (write), StoreKit 2 |
| **Backend** | One thin stateless proxy (e.g. a Cloudflare Worker) that holds the model API key for the single Variety Language LLM call (US-N05) and stores no user data; no other server, scheduler, or data mirror (`convex/` remains an empty placeholder) |
| **AI** | Daily-adaptive AI Programmer at option (C): deterministic, on-device policy re-weighting (writes `SessionPolicy`, never a workout, never on the start path); one template-backed LLM Variety Language line via the proxy, with a deterministic fallback so the app never blocks on the network |
| **Build** | XcodeGen (`project.yml`); the `RepToday` scheme builds the app and runs `RepTodayTests` (the default run), and since US-O04 a second `RepTodayUITests` scheme runs the XCUITest bundle out of process so the default run never waits on an app launch |

## Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| **MVP (v6)** | Discipline Loop + daily-adaptive AI Programmer at option (C): 5-60 min deterministic engine with first-class primal, Session Policy, cold-start + Return/Re-entry Ramp, Ready Screen, Consistency Score, PhaseEvaluator, onboarding, active/post/progress UI, CoreData/CloudKit, StoreKit 2 paywall, and one template-backed LLM Variety Language slice via a thin proxy | ✅ Complete (all epics A-N shipped by 2026-07-14; rebranded to Rep Today) |
| **Post-v6 (Epic O)** | Lottie demo seam, fitness-level Start Seed (library 42 → 57, per-side work model, set-aware swap), session timer redesign + Hold Timer, imperial onboarding units | ✅ Complete (US-O01-O04, 2026-07-19 → 2026-07-31) |
| **Pre-submission (Epic D)** | Account deletion for App Store Guideline 5.1.1(v): Profile/Settings screen, bulk delete methods, `AccountDeletionService`, confirmation flow, Apple-credential guidance, optional HealthKit sample removal | ⛔ **Blocking, not started** (US-D01-D06, PRD opened 2026-07-31) |
| **Phase 2** | Full option-(B) LLM Programmer (richer diagnosis + narrative notes), full Strength-Phase catalog, equipment variants | Planned |

MVP non-goals: no direct AI generation of sessions (the AI writes policy only; the deterministic engine assembles every workout), no full option-(B) LLM Programmer, no server-side scheduler or user-data mirror, no gamification, no social/leaderboards, no equipment exercises, no Android/widgets/Watch. The only MVP LLM call is the template-backed Variety Language slice. See the PRD's Non-Goals section.

## Source of truth (in the repo)

| Document | Purpose |
|----------|---------|
| `.claude/agent/tasks/FitSnack-PRD-v6_070226.md` | Strategic plan v6 - vision, the AI Programmer wedge, Session Policy, cold-start, phase model, monetization (reconciled to ADRs 0001-0019). |
| `.claude/agent/tasks/prd-fitsnack-mvp-v6_0702.md` | Implementation PRD + live progress tracker - v6 user stories (US-A01 … US-N05) with acceptance criteria; checkboxes flip to `[x]` as stories land. **Supersedes `prd-fitsnack-mvp_0626.md`** (a Mandu copy is kept alongside this README). |
| `.claude/agent/tasks/prd-fitsnack-mvp_0626.md` | Superseded v5 implementation PRD (Epics A-C built; kept for historical reference). |
| `CLAUDE.md` | Repo conventions, build/test commands, and architecture. Trimmed from 358 lines in the US-O02 docs split; the narrative moved to `docs/`. |
| `docs/implementation-log.md` | Story-by-story narrative of what was built and why, including the design reversals Epic O forced. |
| `docs/test-coverage.md` | The test-coverage map: one row per suite, added as the owning story lands. |
| `docs/asset-attribution.md` | Third-party asset source/license ledger; an asset with no cleared row never ships. |
| `gtm/06-redteam/pre-publication-checklist.md` | The blocking pre-publication list (trademark, domain, privacy policy, device benchmark for the "<100ms" claim, real on-device screenshots, subreddit rules, funnel instrumentation). |

The Mandu-side PRD `01-prd-account-deletion_260731.md` (in this folder) is the only PRD authored here rather than in the dev repo; move or copy it into `.claude/agent/tasks/` when the build starts.

Always check the PRD for the relevant story before building a feature.

## How Claude helps

Built, production-shaped product (not tutor mode). Help here means status tracking, story/PRD execution and breakdown, Swift/SwiftUI code review, engine and test design, build/test debugging (xcodebuild/XcodeGen), monetization and App Store release prep, and translating the deterministic-engine + test-rigor story into AI-builder interview and portfolio material.

## Daily tracking (optional)

Not daily-tracked by default. To log a working session, say "log my Rep Today progress" and the `daily-log` skill will create `projects/RepToday/log/<date>.md` on first use.
