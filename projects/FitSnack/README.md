# FitSnack

**One-liner:** A discipline-first micro-workout iOS app. Open it, say how many minutes you have (5-30), press play; a deterministic on-device engine builds a complete zero-equipment session (warm-up, main work, cooldown) that lands within ±1 min of the requested time. No browsing, no choosing, no thinking.

**Repo:** https://github.com/hcho22/FitSnack (private)

**Strategic role:** **Second income bet** alongside the Agentic RAG flagship, and an **AI-builder portfolio asset** for the job search. Where Agentic RAG is the B2B starter kit sold to agency/freelance devs, FitSnack is the B2C consumer freemium play (see Monetization). The two run as parallel revenue paths under the same income-by-end-of-2026 north star; Agentic RAG remains the primary flagship.

---

## Status

_Update this line as the project moves. Last reviewed: 2026-06-27._

- **Phase:** MVP, clean rebuild in progress, built story-by-story against the PRD.
  The previous app (XP/badges/streaks, AI services, SwiftData) was removed and lives only in git history (commit `23fd56f`) as reference.
- **Current state (per the repo PRD progress tracker):** Epic A (foundation) landed - US-A01 scaffold, US-A02 domain enums, US-A03 domain models, US-A04 CoreData stack, US-A05 app shell. `ViewModels/` is still empty; the deterministic engine (Epic C), screens, Consistency Score, PhaseEvaluator, CloudKit sync, and StoreKit are the bulk of the remaining stories.
- **Confirm with hcho:** which story is next, and the real blocker list.

## Why this project / how it fits

- **Income bet #2 (B2C):** a consumer subscription app is a different revenue shape and a different buyer from the Agentic RAG kit, so it hedges the product path without competing for the same customer. Apple-native stack means near-zero hosting cost (only the $99/yr Apple Developer account).
- **AI-builder portfolio asset:** demonstrates shipped, end-to-end product engineering - SwiftUI + Observation, MVVM with protocol-based DI, CoreData/CloudKit, StoreKit 2, Sign in with Apple, HealthKit - and a Phase 2 LLM roadmap (language-only summaries/narratives). Note the MVP is deliberately LLM-free; the "AI" story here is the AI roadmap plus the build being done AI-assisted (Claude Code), not AI in the core loop.
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
| **Backend** | None in the MVP (`convex/` is an empty placeholder); an LLM API-key proxy is deferred to Phase 2 |
| **Build** | XcodeGen (`project.yml`); single `FitSnack` scheme builds the app and runs `FitSnackTests` |

## Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| **MVP** | Discipline-Phase loop: deterministic engine, Consistency Score, PhaseEvaluator, onboarding, CoreData/CloudKit, StoreKit 2 paywall | In progress |
| **Phase 2** | Language-only LLM features (template-free summaries, weekly narratives), full Strength-Phase catalog, equipment variants | Planned |

MVP non-goals: no LLM in the core loop (summaries are template-based), no custom backend, no gamification, no social/leaderboards, no equipment exercises, no Android/widgets/Watch. See the PRD's Non-Goals section.

## Source of truth (in the repo)

| Document | Purpose |
|----------|---------|
| `.claude/agent/tasks/FitSnack-PRD-v5.md` | Strategic plan - vision, domain concepts, engine design, phase model, monetization (ADRs referenced inline). |
| `.claude/agent/tasks/prd-fitsnack-mvp_0626.md` | Implementation PRD + live progress tracker - 30 user stories (US-A01 … US-J04) with acceptance criteria; checkboxes flip to `[x]` as stories land. |
| `CLAUDE.md` | Repo conventions and architecture for contributors and AI assistants. |

Always check the PRD for the relevant story before building a feature.

## How Claude helps

Built, production-shaped product (not tutor mode). Help here means status tracking, story/PRD execution and breakdown, Swift/SwiftUI code review, engine and test design, build/test debugging (xcodebuild/XcodeGen), monetization and App Store release prep, and translating the deterministic-engine + test-rigor story into AI-builder interview and portfolio material.

## Daily tracking (optional)

Not daily-tracked by default. To log a working session, say "log my FitSnack progress" and the `daily-log` skill will create `projects/FitSnack/log/<date>.md` on first use.
