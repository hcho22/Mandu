# Agentic RAG

**One-liner:** A production-shaped, permissions-aware Retrieval-Augmented Generation app where per-document sharing is part of the retrieval predicate itself, not a post-hoc filter. Multi-user from day one: every chunk carries an ACL, every retrieval call runs under the viewer's JWT.

**Repo:** https://github.com/hcho22/Agentic_RAG (public)

**Status:** Built and deployable. Landed in 11 progressive modules (app shell / auth / streaming chat through hybrid retrieval, agentic tools, sub-agents, text-to-SQL, the retrieval eval suite, and permission-aware retrieval). Actively maintained: nightly eval workflows run on schedule.

## Why this project / how it fits

This is the **flagship portfolio piece for the AI Eval / QA Engineer target.** It is not just a RAG demo; it ships a real evaluation apparatus that mirrors the day-to-day of an evals role:

- **Retrieval eval suite:** 50-question golden set, recall@k / MRR / nDCG@5, optional generation + LLM-judge step.
- **CI-integrated evals:** a PR workflow runs the golden set against PR head and `main` and posts a delta-vs-`main` comment; nightly snapshots publish to `docs/nightly/`.
- **Regression alarms:** the permissions-scale nightly workflow fails the build if a configured recall floor is breached.
- **RAGAS metrics:** Faithfulness, Answer Relevancy, Context Precision, Context Recall computed weekly.
- **A worked regression catch:** CI caught a Δ -0.510 drop in recall@5 from a one-line chunk-size change (written up in `docs/evals.md`).
- **Security-correctness eval:** proves the ACL property holds (fraction of `no_access` runs returning zero gold chunks = 1.000 with the SQL pre-filter).

Interview talking points: eval design (what each metric measures and what it does not), CI eval gating, regression detection, and proving a security property with an eval rather than asserting it.

## Stack

- **Backend:** FastAPI; raw OpenAI SDK + Pydantic (no LLM frameworks)
- **Frontend:** React + Vite + Tailwind
- **Data:** Supabase (Postgres + pgvector + Auth + Storage + Realtime); RLS-enforced per-user visibility
- **Retrieval:** hybrid vector (pgvector HNSW) + keyword (Postgres full-text) fused via Reciprocal Rank Fusion; optional reranker (Cohere / Voyage / LLM-as-judge)
- **Observability:** LangSmith tracing
- **Deploy:** Vercel (frontend) + Railway or Fly (backend) + Supabase (DB / Auth / Storage)

## Key components

- **Permissions-aware retrieval:** per-chunk ACLs pushed into the SQL predicate so the planner ranks among visible candidates from the start. Solves the post-filter recall collapse on selective ACLs (at 5% selectivity, top-10 yields ~0.5 visible chunks on average, so a naive post-filter most often returns nothing).
- **Agentic tools:** streaming, tool-using chat loop with `query_database` (text-to-SQL over an allowlisted read-only schema), a `web_search` fallback, and `spawn_document_agent` sub-agents with isolated context.
- **Ingestion:** drag-and-drop multi-format (txt / md / pdf / docx / html via docling), chunk + embed + index, live status via Supabase Realtime, LLM structured-output metadata extraction.

## Deep-dive docs (in the repo)

- `docs/permissions-aware-rag.md` — the post-filter recall problem, the four-table data model, the SQL predicate, the HNSW interaction, the eval tables, and deliberate v0 scope cuts.
- `docs/evals.md` — corpus design, the golden set, metric semantics, the worked CI-regression example, and an honest list of the eval's limitations.
- `docs/structured-rag.md` — the semantic-layer-aware text-to-SQL compiler and the read-only role boundary.

## How Claude helps

This is a **built, production-shaped portfolio project**, not a learn-by-hand tutorial (contrast with HabitLoop's tutor mode). Help here means code review, polishing, documentation, demo prep, and especially translating the eval work into interview talking points and resume / portfolio framing for the AI Evals job search.

## Daily tracking (optional)

Not daily-tracked by default. To log progress, say "log my Agentic RAG progress" and the `daily-log` skill will create `projects/Agentic_RAG/log/<date>.md` on first use.
