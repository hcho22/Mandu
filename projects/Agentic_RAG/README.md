# Agentic RAG

**Phase 2 one-liner:** a production starter kit that agency and freelance developers can deploy to ship a client's AI feature on a deadline: permission-aware RAG with workspace isolation, answer quality, and access correctness proven by evals.

**Repo:** https://github.com/hcho22/Agentic_RAG (public)

**Current status:** Phase 1 is built and deployable. **The full Phase 2 implementation PRD is complete (workstreams A–F, US-001–112) as of 2026-07-07.** Done: workspace tenant isolation (A, US-001–011), config-driven model surface (B, US-021–028), ingestion parser boundary (C, US-036–045), the escalation + deterministic deflection pipeline (D, US-046–059), the **full support surface (E, widget runtime + conversation/handoff + teams, US-066–093)**, and the **eval gate + golden-set genericization (F, US-101–112)** — US-110–112 (golden-set genericization, seed→eval ships the 1.000 no-leak table, demo corpora) landed last (`#69/#71/#72` in the dev repo). Remaining Phase 2 work is everything the implementation PRD explicitly held out of scope: self-hosted observability (O1–O4, CONTEXT-only), the F2 typed TS client + F3 capability matrix, and the **P-series productization** (template-ization, license/delivery terms, open-core split, landing page, threat-model doc) — none started. The goal is to productize the now-complete built system into a **Permission-Aware RAG + AI-Support Starter Kit** with a knowledge-assistant face and a B2B support-platform face. Go-to-market validation is now live: flagship post #1 (`posts/01-permission-aware-rag.md`) is published on X (https://x.com/hyungjcho/status/2074233331236167799), the Tally waitlist (https://tally.so/r/vGbO0A) is up, and the 5-day X/Reddit launch campaign (`posts/02-social-5day-launch_260701.md`) is running (Days 1–2 live). One bounded build exception to the productization gate is in flight: the **retrieval-quality pass** (US-113–118, `raw/prd-phase2-retrieval-quality-pass-071026.md`) — US-113–116 merged (#79–#82), US-117 in PR review (#84), US-118 remaining; deadline to complete: 2026-07-18.

**Phase 2 source of truth:** `projects/Agentic_RAG/raw/PRD_phase2_agentic_rag_kit.md` (copied from `/Users/hcho/Developer/Agentic_RAG/.claude/agent/tasks/PRD_phase2_agentic_rag_kit.md`).

## Why this project / how it fits

This is the **flagship portfolio and productization track for the AI Eval / Quality Engineer target**. The differentiator is not "another RAG app"; it is rigor demonstrated by runnable evals:

- **Access correctness:** permission-aware retrieval already proves zero gold-chunk leakage for unauthorized viewers (`no_access` = 1.000 with SQL pre-filter).
- **Retrieval quality:** 50-question golden set with recall@k, MRR, nDCG@5, vector/keyword/hybrid comparisons, and PR-vs-`main` CI comments.
- **Regression proof:** CI caught a -0.510 recall@5 drop from a one-line chunk-size change.
- **Answer quality:** generation evals, RAGAS weekly metrics, and cross-family LLM judging are already in place.
- **Structured-data correctness:** semantic-layer text-to-SQL improved from 10% naive accuracy to 100% semantic accuracy on the 30-question structured eval.

Phase 2 turns those proof points into a reusable starter kit for buyers who need to tell a client exactly what the system can and cannot safely promise.

## Buyer and positioning

**Buyer:** agency or freelance developers who sold a client an AI feature and need to ship it defensibly.

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
7. **Productization (⬜ next phase — the sole remaining Phase-2 build track now that A–F are done):** template-ization, license/delivery terms, open-core split, landing page, threat-model doc, and buyer-facing positioning rewrite. (The waitlist half of "landing page/waitlist" is already live via Tally.) Gated behind buyer validation per the 2026-06-18 strategy; self-hosted observability (O-series) and the F2/F3 client+matrix remain in a follow-up PRD.

## Deep-dive docs

Local wiki/source copies live under `projects/Agentic_RAG/raw/` and `projects/Agentic_RAG/wiki/`.

- `docs/permissions-aware-rag.md` — post-filter recall collapse, ACL data model, SQL predicate, HNSW/selectivity interaction, security evals, and v0 cuts.
- `docs/evals.md` — retrieval corpus, golden set, metrics, RAGAS comparison, and CI regression catch.
- `docs/structured-rag.md` — semantic-layer text-to-SQL planner/compiler, read-only execution boundary, and 30-question eval.
- `PRD_phase2_agentic_rag_kit.md` — Phase 2 productization plan and build sequence.

## How Claude helps

This is a **built, production-shaped portfolio project moving into productization**, not a learn-by-hand tutorial. Help here means implementation planning, issue breakdown, code review, docs, demo prep, Phase 2 build execution, and translating the eval/security story into interview and buyer-facing material.

## Daily tracking (optional)

Not daily-tracked by default. To log progress, say "log my Agentic RAG progress" and the `daily-log` skill will create `projects/Agentic_RAG/log/<date>.md` on first use.
