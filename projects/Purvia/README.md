# Purvia (formerly Agentic RAG)

**Phase 2 one-liner:** a production starter kit that agency and freelance developers can deploy to ship a client's AI feature on a deadline: permission-aware RAG with workspace isolation, answer quality, and access correctness proven by evals.

**Name:** **Purvia**, the product's first real brand, coined from *purview* ("the scope of what one is authorized to see"). Rebrand **complete 2026-07-17** (US-001-007, dev-repo PRs #87-#92) as a display-only rename: 6 vendor-facing "Agentic RAG" strings, plus naming ADR-0011 and the GitHub repo rename. Zero behavior, RLS, or contract change; the technical namespace (`agentic-rag`, `ar-support:*`) is deliberately untouched. USPTO Class 9+42 clearance for "Purvia" is **still pending** and is a named launch precondition - a same-name consumer AI face-swap app is the highest-risk collision.

**Repo:** https://github.com/hcho22/Purvia (public; formerly `hcho22/Agentic_RAG`)

**Last dev-repo activity:** 2026-07-16. Nothing has landed in roughly 2.5 weeks, including the nightly evals - see "Standing risks" below.

**Strategic role (changed 2026-08-02): ranked priority #2, behind Rep Today, and still a live income bet - not portfolio-only.** The paid starter kit and the 10 buyer interviews stay on the board, just behind Rep Today's launch. What changed is the honest read on which value is nearer. Purvia is the strongest technical evidence hcho can put in front of an AI hiring manager, so **job-search leverage is now its most reliable payoff**, while its revenue path has been blocked for six weeks on a buyer who has not been reachable. Ranking it second rather than shelving it is deliberate: if Rep Today's kill criteria fire, Purvia is still standing as a revenue path instead of something to restart. Logged in `decisions/log.md`.

Practically, at #2 the cheap standing obligation is **keeping the eval receipts alive** (see Standing risks). That is what the interview story rests on, and it costs little compared to chasing productization or a launch that is gated on eight preconditions anyway.

---

## Status (2026-08-02)

**Phase 2 implementation is complete (A-F, US-001-112), and both the rebrand and a full go-to-market launch package are done. There is zero in-flight build.** The project is purely in buyer validation, and validation is exactly where it is stuck: **0 of the 10 target buyer interviews are booked.** Two things landed since the last tracker sync:

- **✅ Purvia rebrand complete (2026-07-17)** - see Name above.
- **✅ Go-to-market launch package complete (2026-07-16, `.claude/launch/` in the dev repo, front door `recap.html`; `gtm/` and `launch/` are gitignored so nothing publishes by reflex).** A sourced, red-teamed launch build: a falsifiable `THESIS.md`, a 385-line `RED_TEAM.md`, a claims ledger with per-claim IDs (`evidence/claims.md` plus sourced files on competitors, pricing, prior art, production pain, naming/domains), brand guidelines + a naming tournament + SVG marks and design tokens, a landing site verified at 390 and 1440, a datasheet, X/LinkedIn profile assets, and a social content calendar **hard-gated on the launch preconditions below**.
  - **The pitch it settled on:** the buyer is a production-minded engineer or 2-5 person team adding RAG to a real multi-user product, whose creed is "you don't need a framework." So the pitch is never "adopt my abstraction" - it is *you will build the retrieval loop yourself anyway, and you should; what you will not cheaply build is the proof* (the golden set, the zero-leak evals, the attack suite, the escalation gate with a measurable safety ceiling).
  - **The falsifiable core:** receipts change adoption behavior. If eval receipts do not measurably out-convert feature lists for this ICP, the thesis is wrong however good the engineering is.
  - **The centerpiece story is the honest version of a failure:** the lexical leg of hybrid retrieval shipped dead, and the nightly harness published that fact for **seven weeks across 33 consecutive snapshots** before anyone read it. What it sells is "publication is not detection," not heroics - and US-118's one-sided alarm exists because of that lesson.
  - **Pricing was pulled from every surface.** The red team's objection (CAR-4/BR-8): a priced tier with admitted-empty contents reads as "a price tag on an empty box" to buyers and as commercial incompetence to hiring managers. The $149-$249 one-time band survives only as the hypothesis the first 20 buyer conversations exist to test. Stated plainly in the thesis - everything currently in the repo is MIT and irrevocably granted, so the pro tier can only ever gate things that do not exist yet.

### Launch preconditions (all RED, owner actions, gating any public launch)

The content calendar will not assign a real date to a single post until these are green. Launching over them would ship a receipts story with broken receipts.

1. **The permissions-scale nightly is red and has been since 2026-06-19** (0.000 in every cell). Fix the benchmark's workspace membership, or commit a dated breakage annotation. The red team rated launching without this a kill.
2. **The README contradicts the repo's own nightly directory** - it shows the all-1.000 scale table undated with a present-tense "fails loudly" claim while the benchmark publishes 0.000. The repo must be at least as honest as the landing page about the repo.
3. **No branch protection on main.** Enable a ruleset requiring the E6/AU4/E7 checks; until then all copy must say "fails the required CI check."
4. **USPTO Class 9+42 clearance for "Purvia" pending**, plus a 10-person cold SERP/pronunciation test with ICP engineers.
5. **The founder biography is ledgered as owner-supplied and unverified.** Verify years, titles, and the employer reference against the resume; round down if in doubt.
6. **No security disclosure channel.** Enable GitHub private vulnerability reporting and commit a `SECURITY.md`.
7. **Repo hygiene** - decide which launch artifacts to deliberately publish; clean `supabase/snippets/` and the uncommitted `frontend/widget-host-example.html` edit.
8. **Pre-launch career read** from five named staff-engineer/hiring-manager contacts; three or more "inflated/fluffy" verdicts sends the package back for de-hyping.

### Kill criteria (post-launch, from the thesis)

1. **Receipts don't convert** - within 30 days, fewer than 5 of the first 20 inbound contacts cite the eval artifacts unprompted (primary), or under 150 new stars and under 10 ICP-fit conversations. Action: stop growth investment, keep the repo as a portfolio artifact, the job search keeps the technical story.
2. **Nobody pays** - within 90 days or 20 substantive ICP conversations, zero real willingness-to-pay signals (a budgeted current alternative, procurement questions, a prior comparable purchase). Hypothetical "yes I'd pay" counts in neither direction. Action: kill the pro tier within a week.
3. **The moat closes** - a comparable open kit ships chunk-level ACL enforcement in the retrieval predicate plus blocking leak evals, free (watch Onyx CE, AuthZed). Re-anchor on the escalation gate + eval-authoring story; second-order kill if that also fails criterion 1.
4. **The receipts rot** - the nightly series stops publishing, or a security gate goes red without a same-week fix or annotation, while strangers are reading the artifacts.

### Standing risks

- **Kill criterion 4 is already half-true internally.** The nightly eval series stopped at **2026-07-16** and the permissions-scale benchmark has been red since **2026-06-19**. It does not fire yet only because nobody is reading the artifacts - which is the same "publication is not detection" failure the thesis sells the lesson from, now running a third time. Fixing or annotating this is precondition 1 and the cheapest credibility item on the list.
- **Buyer validation has not moved.** Still 0 of 10 interviews. The launch package is a stronger on-ramp than what existed before, but it does not book conversations by itself.

**Historical detail (through 2026-07-13):** Phase 1 is built and deployable. **The full Phase 2 implementation PRD is complete (workstreams A–F, US-001–112) as of 2026-07-07.** Done: workspace tenant isolation (A, US-001–011), config-driven model surface (B, US-021–028), ingestion parser boundary (C, US-036–045), the escalation + deterministic deflection pipeline (D, US-046–059), the **full support surface (E, widget runtime + conversation/handoff + teams, US-066–093)**, and the **eval gate + golden-set genericization (F, US-101–112)** — US-110–112 (golden-set genericization, seed→eval ships the 1.000 no-leak table, demo corpora) landed last (`#69/#71/#72` in the dev repo). Remaining Phase 2 work is everything the implementation PRD explicitly held out of scope: self-hosted observability (O1–O4, CONTEXT-only), the F2 typed TS client + F3 capability matrix, and the **P-series productization** (template-ization, license/delivery terms, open-core split, landing page, threat-model doc) — none started. The goal is to productize the now-complete built system into a **Permission-Aware RAG + AI-Support Starter Kit** with a knowledge-assistant face and a B2B support-platform face. Go-to-market validation is now live: flagship post #1 (`posts/01-permission-aware-rag.md`) is published on X (https://x.com/hyungjcho/status/2074233331236167799), the Tally waitlist (https://tally.so/r/vGbO0A) is up, and the 5-day X/Reddit launch campaign (`posts/02-social-5day-launch_260701.md`) is running (Days 1–2 live). One bounded build exception to the productization gate ran and is now **complete**: the **retrieval-quality pass** (US-113–118, `raw/prd-phase2-retrieval-quality-pass-071026.md`) — all six stories merged (#79–#82, #84), US-118 landed, manual QA passed; closed 2026-07-13, two days ahead of the 2026-07-18 deadline. The **"Purvia" rebrand** (`raw/prd-rebrand-purvia-2026-07-14.md`, PR #87) opened 2026-07-15 and closed 2026-07-17 - see Name and Status above. It was pre-launch branding prep, not a productization build track; the productization gate remains buyer-validation-gated.

**Phase 2 source of truth:** `projects/Purvia/raw/PRD_phase2_agentic_rag_kit.md` (copied from `/Users/hcho/Developer/Purvia/.claude/agent/tasks/PRD_phase2_agentic_rag_kit.md`).

**Go-to-market source of truth:** `/Users/hcho/Developer/Purvia/.claude/launch/` - `THESIS.md` (bet, preconditions, kill criteria, weaknesses), `RED_TEAM.md`, `BUILD_LOG.md` (decisions and cuts), `evidence/claims.md` (the per-claim ledger every load-bearing statement cites).

## Why this project / how it fits

This is the **flagship portfolio and productization track for the AI Eval / Quality Engineer target**. The differentiator is not "another RAG app"; it is rigor demonstrated by runnable evals:

- **Access correctness:** permission-aware retrieval already proves zero gold-chunk leakage for unauthorized viewers (`no_access` = 1.000 with SQL pre-filter).
- **Retrieval quality:** 50-question golden set with recall@k, MRR, nDCG@5, vector/keyword/hybrid comparisons, and PR-vs-`main` CI comments.
- **Regression proof:** CI caught a -0.510 recall@5 drop from a one-line chunk-size change.
- **Answer quality:** generation evals, RAGAS weekly metrics, and cross-family LLM judging are already in place.
- **Structured-data correctness:** semantic-layer text-to-SQL improved from 10% naive accuracy to 100% semantic accuracy on the 30-question structured eval.

Phase 2 turns those proof points into a reusable starter kit for buyers who need to tell a client exactly what the system can and cannot safely promise.

## Buyer and positioning

**Buyer (sharpened by the 2026-07-16 launch package, and it moved):** a **production-minded engineer, or a 2-5 person team**, adding RAG to a real multi-user product - a SaaS app, an internal tool with real permissions, a customer support surface - who has users whose documents must not leak to each other. Explicitly **not** the buyer: no-code builders, agencies, B2B SMB automation buyers. Note this narrows the older "agency or freelance developer" framing that the rest of this README and `context/current-priorities.md` still carry; the launch package's exclusions are the current read, and reconciling the two is an open item.

The framing that follows from it: this buyer's creed is "you don't need a framework," so the pitch is never "adopt my abstraction." It is *you will build the retrieval loop yourself anyway, in a few hundred lines on the raw SDK, and you should; what you will not cheaply build is the proof.* Take the kit whole, or treat it as the reference implementation plus the test harness for the one you build.

**Product shape:** one engine, two demoable faces:

- **Knowledge assistant:** internal "chat with your docs," based on the current reference app.
- **Support platform:** customer-facing deflection with escalate-to-human, an embeddable widget, workspace/team structure, and eval-backed auto-resolve decisions.

**Headline direction:** production RAG + AI-support starter kit: permission-aware retrieval, isolation, and answer quality proven by evals, with no framework lock-in.

## Stack

- **Backend:** FastAPI; raw OpenAI SDK + Pydantic; no LangChain or LLM framework dependency.
- **Frontend:** React + Vite + Tailwind + shadcn reference app.
- **Data:** Supabase Postgres, pgvector, Auth, Storage, Realtime; RLS-enforced visibility.
- **Retrieval:** hybrid vector search (pgvector HNSW) + keyword search (Postgres full-text) fused by Reciprocal Rank Fusion; optional rerankers.
- **Eval / quality:** retrieval golden set, permission correctness eval, scale benchmark, RAGAS, generation judge, planned escalation eval.
- **Observability:** currently LangSmith-specific; Phase 2 direction is a self-hosted Postgres trace store plus optional OTel exporters.
- **Deploy:** Vercel frontend, Railway/Fly backend, Supabase database/auth/storage.

## Built baseline

- App shell, auth, streaming chat, citations, document upload, and share dialog.
- Hybrid retrieval and optional reranker layer.
- Per-document/per-chunk ACLs inside the retrieval predicate, including granting-principal badges.
- Snapshot-and-replay ACL preservation during re-ingestion.
- Multi-format ingestion via docling, chunking, embedding, indexing, Realtime status, content-hash dedup, and LLM metadata extraction.
- Agentic optional modules: text-to-SQL semantic layer, web search fallback, and document sub-agents.
- Retrieval, generation, RAGAS, permission correctness, and scale/nightly evals.

## Phase 2 build sequence

Status as of 2026-07-07 (implementation PRD complete — all of A–F, US-001–112). This list follows the go-to-market phasing; the implementation PRD orders by hard build dependency (A→B→C→D→E→F), so completed work spans several items here.

1. **Workspace layer (✅ done, A/US-001–011):** workspace entity, workspace-boundary RLS, workspace correctness evals, and auth attack tests.
2. **Escalation capability (✅ done, D/US-046–059):** retrieval-first cascade for answer-vs-escalate decisions, escalation golden set, false-resolve/false-escalate metrics, and support handoff states.
3. **Self-hosted observability (⬜ not started, CONTEXT-only — excluded from the implementation PRD):** Postgres trace store, standalone ops dashboard, OTel exporter facade, and error capture through the same trace path.
4. **Eval genericization + gate (✅ done, F/US-101–112):** configurable CI gate (`off | comment | fail`), buyer-facing golden dataset format, and reusable demo corpus seeders. US-110–112 (golden-set genericization, seed→eval shipping the 1.000 no-leak table, three role-specific demo corpora) closed the workstream and the implementation PRD.
5. **Model / contract / boundary polish (✅ done, B/US-021–028 + C/US-036–045):** Azure OpenAI verification, embedding model config, narrow ingestion boundary, commercial parser adapter, OpenAPI polish, typed TS client, and capability matrix.
6. **Support surface (✅ done, E/US-066–093):** embeddable widget, conversation state, human handoff, and teams within a workspace.
7. **Productization (⬜ next phase — the sole remaining Phase-2 build track now that A–F are done):** template-ization, license/delivery terms, open-core split, landing page, threat-model doc, and buyer-facing positioning rewrite. **The 2026-07-16 launch package pre-answered three of these on paper:** the landing page exists (unpublished, in `.claude/launch/site/`), the buyer-facing positioning rewrite is done (`THESIS.md` + brand guidelines), and the open-core/license question got a hard answer that constrains the rest - everything currently in the repo is MIT and irrevocably granted, so a paid tier can only gate work that does not exist yet. Template-ization and the threat-model doc are untouched. Still gated behind buyer validation per the 2026-06-18 strategy; self-hosted observability (O-series) and the F2/F3 client+matrix remain in a follow-up PRD.

## Deep-dive docs

Local wiki/source copies live under `projects/Purvia/raw/` and `projects/Purvia/wiki/`.

- `docs/permissions-aware-rag.md` — post-filter recall collapse, ACL data model, SQL predicate, HNSW/selectivity interaction, security evals, and v0 cuts.
- `docs/evals.md` — retrieval corpus, golden set, metrics, RAGAS comparison, and CI regression catch.
- `docs/structured-rag.md` — semantic-layer text-to-SQL planner/compiler, read-only execution boundary, and 30-question eval.
- `PRD_phase2_agentic_rag_kit.md` — Phase 2 productization plan and build sequence.

## How Claude helps

This is a **built, production-shaped portfolio project moving into productization**, not a learn-by-hand tutorial. Help here means implementation planning, issue breakdown, code review, docs, demo prep, Phase 2 build execution, and translating the eval/security story into interview and buyer-facing material.

## Daily tracking (optional)

Not daily-tracked by default. To log progress, say "log my Purvia progress" and the `daily-log` skill will create `projects/Purvia/log/<date>.md` on first use.
