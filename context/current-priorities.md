# Current Priorities

_Last updated: 2026-08-02. Update this file when your focus shifts._

**Now (2026-08-02, from a dev-repo sync of both projects).** Two corrections to what this file said:

⛔ **Rep Today has one mandatory build left, and it is a hard App Store rejection blocker.**
An audit on 2026-07-31 found the app ships Sign in with Apple with **zero account-deletion path**
(no Delete Account, no Delete my data, no reachable sign-out; the Profile tab is still a
placeholder), which violates **App Store Guideline 5.1.1(v)**. Optional sign-in does not exempt
it - Apple treats *supporting account creation* as triggering the requirement. The teardown
capability exists only as unreachable dead code, and the Keychain identifier survives reinstall,
so a partial implementation resurrects deleted identities. PRD is implementation-ready
(`projects/RepToday/01-prd-account-deletion_260731.md`, US-D01-D06), **not started**. This
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

⚠️ **Purvia has been idle since 2026-07-16, and its own kill criterion 4 is half-true.** The
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
(`/Users/hcho/Developer/RepToday/gtm/`, front door `recap.html`) - research (139 cited
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

1. **Purvia (Agentic RAG) Phase 2 as the primary income + portfolio flagship (top focus):**
   Model A, sell the starter kit, built in public. **⚠️ Buyer definition is contested as of
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
   later follow-up PRD. **Maintenance debt now competes for this slot:** the nightly evals
   stopped 2026-07-16 and the permissions-scale benchmark has been red since 2026-06-19, which
   is the thesis's own kill criterion 4 in slow motion. Restarting and annotating them is
   cheap and is launch preconditions 1 and 2.
2. **Rep Today as the second income bet (B2C):** discipline-first micro-workout iOS app,
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
   **✅ Epic O post-v6 refinements COMPLETE (US-O01-O04, 2026-07-19 → 2026-07-31)** and
   **TestFlight signing prep done (#64/#65, 2026-07-30)** - see the block at the top of this
   file. **⛔ One mandatory build remains before submission: account deletion (US-D01-D06,
   App Store Guideline 5.1.1(v)), not started.** It blocks submission outright and gates the
   privacy policy, App Store Connect record, trademark clearance, and on-device screenshots
   behind it.
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
- Purvia: open-core public + waitlist (Q3 2026). Public launch is hard-gated on eight RED
  launch preconditions (nightly fixed, README dated, branch protection, USPTO clearance,
  bio verified, SECURITY.md, repo hygiene, career read).
- Rep Today: MVP shipped (TestFlight / App Store; date TBD). Blocked on account deletion
  (US-D01-D06), then provisioning.
