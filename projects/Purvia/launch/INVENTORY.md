# INVENTORY.md - what Purvia actually is, proved from source

Phase 0 deliverable. Every entry cites repo evidence (`file:line` relative to repo root).
Status vocabulary: **shipped** = wired end-to-end in code; **specced** = documented or scaffolded but not live; **cut** = deliberately out of scope, stated in docs.
Generated 2026-08-27 against the working tree at commit `a04cee8`.

## The product in three sentences

Purvia is a permissions-aware RAG platform: per-document sharing is part of the SQL retrieval predicate itself, not a filter applied after vector search (`README.md:3-8`).
It has two surfaces under one roof: an owner-only knowledge assistant, and a white-labeled embeddable support widget with a deterministic escalate-vs-answer pipeline (`docs/adr/0011-product-name.md:14-21`).
The name Purvia is settled by ADR-0011 (coined from *purview*); the technical namespace deliberately stays `agentic-rag` (`docs/adr/0011-product-name.md:28-61`).

## Shipped (proved from source)

| Capability | Evidence |
|---|---|
| ACL-in-the-predicate retrieval: per-chunk ACLs AND-ed into `match_chunks`/`keyword_search` under the viewer's JWT, `SECURITY INVOKER`, RLS-mirrored | `README.md:3-8`, `docs/permissions-aware-rag.md` §3 (lines 104-175), Module 11 rows in `README.md:493-505` |
| Workspace tenant isolation above per-doc sharing; membership clause from JWT, never a backend-passed tenant id | `docs/adr/0002-workspace-tenant-isolation.md`, `README.md:126` |
| Hybrid retrieval: pgvector HNSW + Postgres FTS fused by RRF, query-adaptive fusion weight (`HYBRID_FUSION_ALPHA=auto`) | `README.md:124,245`, US-116 status "Code-complete" in `.claude/agent/tasks/prd-retrieval-quality-pass.md:118` |
| Keyword OR-fallback (revived lexical leg) | `docs/adr/0009-keyword-or-fallback.md`, US-114 in `prd-retrieval-quality-pass.md:3` |
| Chat streaming (Responses/Completions), multi-format ingestion via docling (`.txt/.md/.pdf/.docx/.html`), LLM metadata extraction, Realtime status | `README.md:122-123` |
| Per-document share dialog + per-chunk "via owner / via direct grant / via {group}" attribution badges | `README.md:14-16,125` |
| Support widget: cross-origin iframe embed, opaque per-conversation tokens, per-key origin allowlist, rate limits, per-workspace circuit breaker, SSE streaming + agent replies, operator queue | `README.md:294-397` (API table + embed section) |
| Deterministic escalate-vs-answer deflection pipeline; two fail-closed content gates (faithfulness + answer-completeness), `JUDGE_TEMPERATURE` pinned 0 | `AGENTS.md` invariant 8, `backend/escalation.py`, `README.md:319` |
| Deflection derivable, not stored: `resolved AND escalated_at IS NULL` => deflected; DB trigger owns the latch | `AGENTS.md` invariants 5-6 |
| Structured RAG text-to-SQL with semantic layer, allowlisted schemas, read-only role | `README.md:127`, `docs/structured-rag.md` |
| Web-search fallback, document sub-agents | `README.md:128-129` |
| Model surface: provider per role (answerer/embedder/judge), OpenAI + Azure tested, `base_url` for compatible endpoints | `README.md:262-284`, `docs/model-surface.md` |
| Parser adapters: docling default, llamaparse, unstructured; buyer-written adapter guide | `README.md:225`, `docs/ingestion-parser-adapters.md` |
| Eval suite: 60-question content-anchored golden set (5 categories), recall@k / MRR / nDCG@5, E4 leak matrix derived from gold, E6 cross-workspace gate, E7 escalation suite, AU4 API auth attacks, RLS-hardening regression | `docs/evals.md:23-45` (§2.2), `README.md:399-437` |
| "Measured nothing is never a measurement": `EmptyGoldError` / `ZeroResolveError` / `DegenerateRunError` guards, pinned by offline CI job | `AGENTS.md` invariant 12, `docs/evals.md:248`, `evals/permissions_scale/test_degenerate_guard.py` |
| Security gates pinned `fail`, un-downgradable; silence only by deleting the eval | `docs/evals.md:358-366` (US-102), `evals/gate/security.py` |
| Ship-green CI: fresh seed -> eval on shipped artifacts must reproduce the 1.000 no-leak table, on every relevant PR and on main | `docs/evals.md:157-165` (§2.7), `.github/workflows/ship-green.yml` |
| Nightly + weekly eval publishing with three-state outcomes (green / red / UNMEASURED) and stranded-publish alarms | `README.md:403-408`, `docs/evals.md:320-347` |
| Permissions scale benchmark: 10k-chunk Wikipedia filler, ef_search x selectivity sweep, recall-floor alarm, `DEGENERATE RUN` refusal path | `README.md:132`, `docs/permissions-aware-rag.md` §5b, `docs/permissions-scale-nightly/2026-08-27.md` |
| Generic seeder for buyer corpora (production chunk/embed path, zero test principals baked in) | `docs/evals.md:129-155` (§2.6), `db_seed/generic_seed.py` |
| Reranker layer (cohere / voyage / llm) behind `RERANKER`, default `none`; LLM backend measured in a bake-off | `README.md:246-249`, `docs/reranker-bakeoff.md` |
| MIT license on the whole repo | `LICENSE:1-5` |

## Specced but NOT shipped (must never be sold as live)

| Item | Reality | Evidence |
|---|---|---|
| RAGAS metric computation | `score_with_ragas()` is a scaffold that returns `[]` unconditionally: "The RAGAS evaluation pipeline ... lands in a later story. US-001 ships scaffold only." The weekly "RAGAS" page renders an all-dashes RAGAS table; its retrieval and Claude-judge numbers are real. | `evals/retrieval/ragas.py:139-157`, `docs/ragas-weekly/2026-08-28.md:25-40` |
| README's RAGAS bullet ("computed weekly ... published to docs/ragas-weekly/") | Overclaims: gates, bindings, and publishing exist; the four scores are never computed. This is the one place the README contradicts source. Fixed in `README.proposed.md`. | `README.md:131` vs `evals/retrieval/ragas.py:157` |
| Cohere / Voyage reranker measurements | Code path shipped, never measured - "not measured: no COHERE_API_KEY / VOYAGE_API_KEY in the local environment" | `docs/reranker-bakeoff.md:21` |
| Gate loudness/placement wiring onto the escalation runner's own call sites | "until those predicates are wired ... they remain advisory" | `docs/evals.md:354` |

## Deliberately cut (honest "who should not buy" material)

From `docs/permissions-aware-rag.md` §6 (lines 506-521): share autocomplete, **role hierarchies (every grant is read-only access; no owner/editor/viewer tiers)**, **nested group membership (flat groups only)**.
Single-family evals must not be cited as "proven" (`docs/golden-set-authoring.md:211-229`).
Corpus swaps break the example golden set's anchors loudly and by design - "replace the corpus" and "author a new golden set" are the same step (`docs/demo-corpora.md:7-16`).
Recall-curve at true scale: at 10k chunks the planner sidesteps HNSW, so the scale table is trivially 1.000; the curve only surfaces at tens-to-hundreds-of-thousands of visible chunks, which is unmeasured (`README.md:85-98`, `docs/permissions-aware-rag.md:444-447`).
Content-leg false-resolve regressions carry an accepted up-to-a-week detection latency (weekly LLM-judged sweep, mitigated by the deterministic per-PR tripwire) (`docs/evals.md:415-431`).

## The numbers (every one travels with its denominator)

| # | Number | Denominator / context | Source |
|---|---|---|---|
| N1 | Security no-leak table all **1.000**, pre- and post-filter, all 3 modes | 60 questions x 3 modes x 3 viewer setups on the 16-chunk / 8-doc e-commerce demo corpus | `README.md:24-31`; reproduced nightly, `docs/nightly/2026-08-27.md:39-45` |
| N2 | **42 days of measured 0.000** under a green hand-copied table (2026-06-19 to 2026-07-30), red floor alarm firing nightly the whole time; 18 prior days republished the stale table after the runner died (from 2026-06-01); recovered 2026-07-31 | The permissions scale benchmark; the README's own words: "the failure that mattered" | `README.md:41-77` |
| N3 | Scale recall@5 all **1.000** across ef_search {40,80,200,500} x selectivity {50%,10%,1%} | 15 multi-hop queries, 10k-chunk synthetic Wikipedia corpus, 77.76s wall; trivially saturated because the planner bitmap-scans the ACL and sidesteps HNSW (EXPLAIN-confirmed) | `docs/permissions-scale-nightly/2026-08-27.md`, `README.md:85-98` |
| N4 | CI caught **Δ -0.510 recall@5** (0.860 -> 0.350 vector/hybrid) from a one-line chunk-size change, posted in 4 minutes, no human | Staged throwaway PR #14 (closed unmerged); 50 questions x 3 modes at the time; cause contrived, catch real | `docs/evals.md:204-232` |
| N5 | The dead lexical leg the harness caught: keyword recall@5 **0.140** overall, **0.000** on paraphrase; hybrid MRR **0.786** vs vector **0.796**; adversarial **0.453** vs **0.503** | Nightly of 2026-07-09, 50-question golden set, before the US-113-118 pass | `.claude/agent/tasks/prd-retrieval-quality-pass.md:10-12`, `docs/nightly/2026-07-09.md` |
| N6 | After the fix: keyword paraphrase recall@5 **0.800**, keyword lexical **1.000**, hybrid recall@5 >= vector in every category (hybrid paraphrase MRR still trails vector, 0.767 vs 1.000), hybrid full-access recall@5 **0.950** vs baseline 0.950 | Nightly of 2026-08-27, 60-question golden set, 16-chunk corpus | `docs/nightly/2026-08-27.md:3-33,70-76` |
| N7 | LLM-judge generation quality: faithfulness **4.83/5**, helpfulness **4.00/5** | n=60, cross-family judge (Claude scoring gpt-5.6-luna answers), weekly snapshot | `docs/ragas-weekly/2026-08-28.md:19-23` |
| N8 | E7 escalation: P1a 3/3 escalated, P1b 4/4 zero gold leaked, non-disclosure byte-equality PASS, P2 deflection 4/4, **false-resolve 0% (0/9)** vs 5% ceiling | Tiny populations by design (3 / 4 / 4 / 9 rows); weekly sweep 2026-08-27, offline judge claude-haiku-4-5 | `docs/escalation-weekly/2026-08-27.md:64-82` |
| N9 | LLM reranker bake-off: overall MRR 0.858 -> 0.899, adversarial recall@5 0.800 -> 0.900, at **27x wall-clock cost** (12.6s -> 343.6s); recommendation: keep `RERANKER=none` | 60 questions, hybrid mode, full viewer, 16-chunk corpus; Cohere/Voyage unmeasured (no keys) | `docs/reranker-bakeoff.md:45,58,65` |
| N10 | Post-filter math: at 5% ACL selectivity, top-10 post-filtering expects **0.5 visible chunks** (k x selectivity) | Arithmetic in the README, the "why this is hard" argument | `README.md:100-118` |

## Claim caps (the docs' own words that bound all marketing)

1. "A single-family eval ... is **not** evidence you may present as 'proven.'" - `docs/golden-set-authoring.md:211-229`, esp. line 217.
2. "Swapping in your own corpus makes the example golden set's anchors fail loud. ... a format template to learn from, not a survives-the-swap artifact." - `docs/demo-corpora.md:9-11`.
3. "The golden set is 60 questions. ... per-category cells ... have low statistical power. Treat per-category numbers as directional, not precise." - `docs/evals.md:238`.
4. "LLM-drafted questions may inflate scores." / "The seeded corpus may not generalise." / "No human-rater inter-annotator agreement." - `docs/evals.md:240-246`.
5. Every cell of the scale table is 1.000 because the planner sidesteps HNSW at 10k chunks; the recall curve at real scale is unmeasured. - `README.md:85-98`.
6. Trademark: "A paid USPTO Class 9 + 42 trademark clearance is still pending." - `docs/adr/0011-product-name.md:69-71`.

## Demo-ability constraints (no-new-spending rule)

Keys present in `.env`: Supabase (URL, anon, service-role, project ref), `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, Google OAuth pair.
Absent: `COHERE_API_KEY`, `VOYAGE_API_KEY`, `LLAMA_CLOUD_API_KEY`, `LANGSMITH_API_KEY`.
Consequence: anything requiring Cohere/Voyage/LlamaParse/LangSmith is demo-off-limits; assets must not depend on them.
