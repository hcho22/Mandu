# Agentic RAG

**Phase 2 one-liner:** a production starter kit that agency and freelance developers can deploy to ship a client's AI feature on a deadline: permission-aware RAG with workspace isolation, answer quality, and access correctness proven by evals.

**Repo:** https://github.com/hcho22/Agentic_RAG (public)

**Current status:** Phase 1 is built and deployable. Phase 2 is active and well underway: the implementation PRD is **complete through US-089** (last reviewed 2026-07-01). Done: workspace tenant isolation (A, US-001–011), config-driven model surface (B, US-021–028), ingestion parser boundary (C, US-036–045), and the escalation + deterministic deflection pipeline (D, US-046–059). In progress: the support surface (E, widget runtime + conversation/handoff, US-066–093) is built through US-089 — the deflection turn, escalation latch + human-handoff loop, and the embeddable widget shell + chat UI are done; US-090–093 remain. Not started: the eval gate + golden-set genericization (F, US-101–112) and productization. The goal is to productize the built system into a **Permission-Aware RAG + AI-Support Starter Kit** with a knowledge-assistant face and a B2B support-platform face. Go-to-market validation content is drafted: flagship post #1 (`posts/01-permission-aware-rag.md`) and a 5-day X/Reddit launch campaign (`posts/02-social-5day-launch_260701.md`), ready to schedule once the Tally waitlist link is live.

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

Status as of 2026-07-01 (implementation PRD complete through US-089). This list follows the go-to-market phasing; the implementation PRD orders by hard build dependency (A→B→C→D→E→F), so completed work spans several items here.

1. **Workspace layer (✅ done, A/US-001–011):** workspace entity, workspace-boundary RLS, workspace correctness evals, and auth attack tests.
2. **Escalation capability (✅ done, D/US-046–059):** retrieval-first cascade for answer-vs-escalate decisions, escalation golden set, false-resolve/false-escalate metrics, and support handoff states.
3. **Self-hosted observability (⬜ not started, CONTEXT-only — excluded from the implementation PRD):** Postgres trace store, standalone ops dashboard, OTel exporter facade, and error capture through the same trace path.
4. **Eval genericization + gate (⬜ not started, F/US-101–112):** configurable CI gate (`off | comment | fail`), buyer-facing golden dataset format, and reusable demo corpus seeders.
5. **Model / contract / boundary polish (✅ done, B/US-021–028 + C/US-036–045):** Azure OpenAI verification, embedding model config, narrow ingestion boundary, commercial parser adapter, OpenAPI polish, typed TS client, and capability matrix.
6. **Support surface (🔄 in progress, E/US-066–093 — built through US-089; US-090–093 remain):** embeddable widget, conversation state, human handoff, and teams within a workspace.
7. **Productization (⬜ not started):** template-ization, license/delivery terms, open-core split, landing page/waitlist, threat-model doc, and buyer-facing positioning rewrite.

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
