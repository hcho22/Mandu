# FitSnack

**One-liner:** A discipline-first micro-workout iOS app. Open it and a complete zero-equipment session (5-60 min) is already waiting - a deterministic on-device engine blends strength, mobility, and primal movement to land within ±1 min of your Default Duration. No browsing, no choosing, no thinking. Between sessions a daily-adaptive AI Programmer quietly rewrites each user's Session Policy (progression, pillar weighting, variety); it shapes the program, never the workout, and is never on the path to pressing start.

**Repo:** https://github.com/hcho22/FitSnack (private)

**Strategic role:** **Second income bet** alongside the Agentic RAG flagship, and an **AI-builder portfolio asset** for the job search. Where Agentic RAG is the B2B starter kit sold to agency/freelance devs, FitSnack is the B2C consumer freemium play (see Monetization). The two run as parallel revenue paths under the same income-by-end-of-2026 north star; Agentic RAG remains the primary flagship.

---

## Status

_Update this line as the project moves. Last reviewed: 2026-07-08._

- **Phase:** MVP, clean rebuild, built story-by-story against the **v6 PRD** (`prd-fitsnack-mvp-v6_0702.md`, which supersedes the v5 `prd-fitsnack-mvp_0626.md`). v6 reframes the MVP as "the Discipline Loop with a daily-adaptive AI Programmer." The previous app (XP/badges/streaks, AI services, SwiftData) was removed and lives only in git history (commit `23fd56f`) as reference.
- **Current state (per the repo v6 progress tracker): complete through US-I01 - Epics A-I done.**
  - **Epic A - Foundation (✅ built):** scaffold, domain enums/models, CoreData stack, service protocols / ServiceContainer / app state.
  - **Epic B - Exercise Library (✅ built):** bundled ~38-movement JSON library + load/integrity-check service.
  - **Epic C - Deterministic Engine, Steps 1-7 + Swap (✅ built):** the full v5 pipeline, including the deterministic exercise swap (the old US-C08 is now folded into a built Epic C).
  - **Epic D - v6 Data Model & Session Policy Foundation (✅ done, US-D01-D04):** `User` gains `why`/`duration`/`coldStart`, `WorkoutLog` gains `requestedMinutes`/`wasReturn`, the always-valid `SessionPolicy`, and the `ReprogramTrigger` service seam.
  - **Epic E - Engine v6 Extensions (✅ done, US-E01-E06):** session shapes extended to 5-60 min, primal promoted to a first-class pillar, the engine consumes SessionPolicy levers, Step 0 cold-start override + capped Starting Difficulty, the Asymmetric Ramp, and the Return override + Re-entry Ramp.
  - **Epic F - AI Programmer at option (C) (✅ done, US-F01-F04):** US-F01 re-program trigger detection with Trigger Precedence (#26), US-F02 plateau diagnosis (Physical Stall vs Disengagement) (#27), US-F03 deterministic Session Policy re-weighting service (#29), US-F04 Default Duration learning + templated policy note (#28). This is the on-device, zero-LLM daily-adaptive AI Programmer that rewrites each user's `SessionPolicy` (never a workout, never on the start path), with a human-readable note explaining each change.
  - **Epic G - Cold-start & Variety Language (✅ done, US-G01-G04):** US-G01 capped Starting Difficulty seeding served gentle (#30), US-G02 First-Week Contrast enforcement (#31), US-G03 the Variety Language slice - the MVP's single LLM call, template-backed via the thin proxy with a deterministic fallback (#32), US-G04 cold-start handoff (#33).
  - **Epic H - Consistency & progression (✅ done, US-H01-H02):** US-H01 the forgiving, Return-protected Consistency Score (single miss dents but never zeroes; 5-min counts as a full show-up) (#34), US-H02 the earned-progression PhaseEvaluator (Strength Phase earned, never settable) (#35).
  - **Epic I - Onboarding (✅ done, US-I01):** the minimal v6 onboarding flow (#36) - collects profile/`why`/`sitsLong`/duration, seeds capped Starting Difficulty + `coldStart` + `SessionPolicy.default`, then routes straight to the Ready Screen with the first session pre-generated (no picker). Single-story epic by design; the detailed flow is deferred to Phase 2.
- **Remaining (Epics J-N, not started):** J - Ready Screen (the state the app opens to); K - active session; L - post-session; M - progress tab; N - Apple integrations (Sign in with Apple, CloudKit, HealthKit, StoreKit 2) + the thin stateless proxy.
- **Next story:** US-J01 (Ready Screen with pre-generated session and non-blocking duration chip) - the first story of Epic J, the state the app opens to (ADR-0016), replacing the v5 Home screen.
- **Go-to-market (pre-launch):** a build-in-public 1-week social launch plan (IG/X/TikTok, "discipline over content" wedge) is drafted at `posts/01-social-1week-launch_260701.md`, grounded in a 2026-07-01 market scan. It runs as a positioning + waitlist play before the MVP ships (no app to download yet).

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
| **Platform** | iOS 17.0+, Swift 5.9, Xcode 16.3; Bundle ID `com.fitsnack.app` |
| **UI** | SwiftUI with the Observation framework (`@Observable`, never `ObservableObject`/`@Published`) |
| **Architecture** | MVVM + protocol-based service injection (swap a mock for a real impl by changing one line in `ServiceContainer`) |
| **Persistence** | CoreData backed by `NSPersistentCloudKitContainer` (`CDUser`, `CDWorkoutLog`); local-only until CloudKit sync lands |
| **Engine** | Pure Swift, on-device, deterministic - no network, no LLM, <100ms |
| **Apple integrations** | Sign in with Apple, CloudKit (private DB sync), HealthKit (write), StoreKit 2 |
| **Backend** | One thin stateless proxy (e.g. a Cloudflare Worker) that holds the model API key for the single Variety Language LLM call (US-N05) and stores no user data; no other server, scheduler, or data mirror (`convex/` remains an empty placeholder) |
| **AI** | Daily-adaptive AI Programmer at option (C): deterministic, on-device policy re-weighting (writes `SessionPolicy`, never a workout, never on the start path); one template-backed LLM Variety Language line via the proxy, with a deterministic fallback so the app never blocks on the network |
| **Build** | XcodeGen (`project.yml`); single `FitSnack` scheme builds the app and runs `FitSnackTests` |

## Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| **MVP (v6)** | Discipline Loop + daily-adaptive AI Programmer at option (C): 5-60 min deterministic engine with first-class primal, Session Policy, cold-start + Return/Re-entry Ramp, Ready Screen, Consistency Score, PhaseEvaluator, onboarding, active/post/progress UI, CoreData/CloudKit, StoreKit 2 paywall, and one template-backed LLM Variety Language slice via a thin proxy | In progress (Epics A-I done; engine, AI Programmer, cold-start + Variety Language, Consistency Score + PhaseEvaluator, and onboarding all built - remaining is the UI shell J-M and Apple integrations N) |
| **Phase 2** | Full option-(B) LLM Programmer (richer diagnosis + narrative notes), full Strength-Phase catalog, equipment variants | Planned |

MVP non-goals: no direct AI generation of sessions (the AI writes policy only; the deterministic engine assembles every workout), no full option-(B) LLM Programmer, no server-side scheduler or user-data mirror, no gamification, no social/leaderboards, no equipment exercises, no Android/widgets/Watch. The only MVP LLM call is the template-backed Variety Language slice. See the PRD's Non-Goals section.

## Source of truth (in the repo)

| Document | Purpose |
|----------|---------|
| `.claude/agent/tasks/FitSnack-PRD-v6_070226.md` | Strategic plan v6 - vision, the AI Programmer wedge, Session Policy, cold-start, phase model, monetization (reconciled to ADRs 0001-0019). |
| `.claude/agent/tasks/prd-fitsnack-mvp-v6_0702.md` | Implementation PRD + live progress tracker - v6 user stories (US-A01 … US-N05) with acceptance criteria; checkboxes flip to `[x]` as stories land. **Supersedes `prd-fitsnack-mvp_0626.md`** (a Mandu copy is kept alongside this README). |
| `.claude/agent/tasks/prd-fitsnack-mvp_0626.md` | Superseded v5 implementation PRD (Epics A-C built; kept for historical reference). |
| `CLAUDE.md` | Repo conventions and architecture for contributors and AI assistants. |

Always check the PRD for the relevant story before building a feature.

## How Claude helps

Built, production-shaped product (not tutor mode). Help here means status tracking, story/PRD execution and breakdown, Swift/SwiftUI code review, engine and test design, build/test debugging (xcodebuild/XcodeGen), monetization and App Store release prep, and translating the deterministic-engine + test-rigor story into AI-builder interview and portfolio material.

## Daily tracking (optional)

Not daily-tracked by default. To log a working session, say "log my FitSnack progress" and the `daily-log` skill will create `projects/FitSnack/log/<date>.md` on first use.
