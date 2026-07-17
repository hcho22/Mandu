# Current Priorities

_Last updated: 2026-07-15. Update this file when your focus shifts._

**This week (by 2026-07-18), per hcho 2026-07-12:** finish both in-flight PRDs. ✅ **BOTH DONE.**
✅ **Agentic RAG retrieval-quality pass DONE** (2026-07-13, two days early - all six
stories US-113-118 merged, manual QA passed).
✅ **FitSnack v6 MVP DONE** (2026-07-14, four days early - final 8 stories US-L02, M01-M02,
N01-N05 merged; all epics A-N shipped). Immediately followed by the **FitSnack → Rep Today
rebrand** (US-001-009, PRs #52-#60, complete 2026-07-14; 667/667 tests green). Both build
tracks for the week are closed. ✅ **Rep Today GO-TO-MARKET PACKAGE DONE (2026-07-16,
dev-repo PR #61):** a full sourced, red-teamed, Rep Today-branded GTM package
(`/Users/hcho/Developer/RepToday/gtm/`, front door `recap.html`) - research (139 cited
URLs), naming tournament + brand guidelines, landing site, 48s launch video, investment
thesis with kill criteria, an ASO-led channel plan, a 55-objection red-team dossier, App
Store assets + social launch kit; self-graded 2026-07-15, honesty guardrails held (pre-launch,
zero users/downloads/revenue, nothing published). It supersedes the run-1 GTM plan. Rep Today's
next step is not more build or planning - it is pre-submission
provisioning (signing/`DEVELOPMENT_TEAM`, App Store Connect record, privacy-policy URL,
trademark + App Store name clearance which the GTM self-grade flags as UNVERIFIED) and then
executing the channel test against the thesis kill criteria. With both passes closed, Agentic RAG returns to purely validation
(the standing #1). **New in-flight (opened 2026-07-15): the "Purvia" rebrand**
(`projects/Agentic_RAG/raw/prd-rebrand-purvia-2026-07-14.md`) - the product's
first real brand, a tight display-only rename (6 vendor-facing "Agentic RAG"
strings → "Purvia") plus a naming ADR, zero behavior/RLS/contract change. PRD
authored + committed to the dev repo (PR #87); implementation US-001-006 not yet
started. Pre-launch branding prep, not a productization build track.

1. **Agentic RAG Phase 2 as the primary income + portfolio flagship (top focus):** Model A,
   sell the starter kit to agency/freelance AI devs, built in public. **The full Phase 2
   implementation PRD is now complete (A-F, US-001-112, done 2026-07-07)**, so there is no
   core build left to compete for attention - focus is now *purely* validation, then gated
   productization. Done: post #1 published on X, waitlist live (Tally), 5-day campaign running
   (Days 1-2 out). Remaining validation = **book the 10 buyer interviews** (still 0; the
   constraint is no warm network, so route through communities hcho belongs to - FourthBrain,
   Omdena, r/RAG - plus campaign engagers and a free "permission-RAG teardown" on-ramp, not
   warm intros) and drive waitlist signups. Only after findings: P-series productization
   (template-ization, license/delivery, open-core split, landing page, threat-model) - the
   sole remaining build track, and it stays gated. (Separate from that gate, a small
   display-only "Purvia" rebrand opened 2026-07-15 - see the "This week" block above.)
   Observability O-series and F2/F3 are a
   later follow-up PRD.
2. **FitSnack as the second income bet (B2C):** discipline-first micro-workout iOS app,
   freemium (free unlimited core loop, premium "depth" paywall at $9.99/mo or $59.99/yr
   via StoreKit 2, per the run-1 pricing lock). **MVP build COMPLETE (2026-07-14):** all
   epics A-N shipped story-by-story against the v6 PRD; Apple-native stack so near-zero
   hosting cost. **Rebranded FitSnack → Rep Today (2026-07-14):** name now locked as
   **Rep Today** (App Store listing "Rep Today, Rest Tomorrow"), superseding the interim
   "Nonzero" placeholder; `com.reptoday.app` identifiers baked in pre-public. The Mandu
   tracker folder was renamed `projects/FitSnack → projects/RepToday` on 2026-07-16 to match.
   **GTM package COMPLETE (2026-07-16, dev-repo PR #61):** a full sourced, red-teamed,
   Rep Today-branded go-to-market package (`/Users/hcho/Developer/RepToday/gtm/`, front door
   `recap.html`) - research with 139 cited URLs, naming tournament + brand guidelines,
   landing site, 48s launch video, an investment thesis with kill criteria, an ASO-led
   channel plan, a 55-objection red-team dossier, App Store assets + social launch kit;
   self-graded 2026-07-15. It supersedes the earlier run-1 GTM plan and the 2026-07-01 social
   launch draft. Honesty guardrails held: pre-launch, zero users/downloads/revenue, nothing
   published or purchased, no fabricated stats.
   **Open call for hcho (unchanged):** the red team's corrected funnel math says income-relevance
   needs 10-20k installs/month sustained, so until the channel test clears its
   30/60/90-day gates the honest label is "portfolio asset with revenue upside," not a
   proven income pillar. Ranking left unchanged pending
   that call. Also feeds the build: PRD US-H01 amendment recommended (per-day score
   credit, so "miss a day, your score dents" stays true).
   (Ranked above the job-search hedge per hcho's 2026-06-27 call; swap if applications slip.)
3. **Job search as the parallel income hedge:** sustained applications at 5/week against
   Tier A/B/C, plus interview prep. Non-negotiable minimum given the 6-12 month runway.
   Two-bucket targeting (AI builder + AI evals/quality), pitched on validation rigor.
4. **Evals as the edge, not a study track:** express it through Agentic RAG's eval harness
   (leak suite, escalation golden set, CI gate), not a standalone 20-hour study plan.
5. **Second brain / AI OS:** lowest; an enabler, maintained not pushed.

## Demoted / paused

- **CreativeBridge:** portfolio-only; finish TestFlight opportunistically, not a focus.
- **CompeteIntel:** backlog/paused while Agentic RAG and FitSnack are the product bets.

## Recently completed

- **F2F** and **HabitLoop** (unchanged; see archives/).

## Active deadlines

- Income by end of 2026 (app revenue or a full-time role).
- Agentic RAG: open-core public + waitlist (Q3 2026).
- FitSnack: MVP shipped (TestFlight / App Store; date TBD).
