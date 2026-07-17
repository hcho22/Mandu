# Agentic RAG Wiki Log

Event log for this wiki. Each entry begins with `## [YYYY-MM-DD] <op> | <title>` (op is `ingest`, `query`, `lint`, etc.) so entries are greppable and sort by date.

## [2026-06-15] ingest | Agentic RAG Evals

- Source fetched from `https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/evals.md` and saved verbatim to `raw/agentic-rag-evals.md` (checksum recorded before derived edits).
- Created `sources/agentic-rag-evals.md` with summary, key claims, concept links, and provenance.
- Seeded five concept pages from stub to seeded, each source-count 0 to 1:
  - `[[retrieval-eval-suite]]`: corpus, golden set, retrieval metrics, runner outputs, and limitations.
  - `[[ci-eval-gating]]`: PR-vs-main delta workflow and the chunk-size regression catch.
  - `[[ragas-metrics]]`: RAGAS scope, thresholding, rolling medians, and Claude corroboration.
  - `[[security-correctness-eval]]`: no-access/security cells as hard authorization checks rather than soft answer-quality scores.
  - `[[hybrid-retrieval-rrf]]`: vector, keyword, and hybrid modes as measured retrieval alternatives.
- Updated `index.md` with the new source and dropped `(stub)` from the five sourced concepts.
- Seeded `synthesis.md` in full mode and routed interview talking points to `projects/job-search/interview-prep.md`.
- No daily-log pointer added because `projects/Agentic_RAG/log/2026-06-15.md` does not exist.

## [2026-06-15] ingest | Permission-aware RAG

- Source fetched from `https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/permissions-aware-rag.md` via the GitHub API raw-content endpoint and saved verbatim to `raw/permissions-aware-rag.md`.
- Created `sources/permissions-aware-rag.md` with summary, key claims, concept links, and provenance.
- Seeded `[[permissions-aware-retrieval]]` from stub to seeded (source-count 0 to 1): post-filter recall collapse, ACL data model, SQL predicate, grant replay, and granting-principal precedence.
- Extended `[[security-correctness-eval]]` (source-count 1 to 2): no-access security table and hard authorization property.
- Extended `[[retrieval-eval-suite]]` (source-count 1 to 2): viewer/filter strategies, permission-scale benchmark, and 100k+ benchmark follow-up.
- Extended `[[hybrid-retrieval-rrf]]` (source-count 1 to 2): vector/keyword/hybrid modes under ACL filters and the HNSW `ef_search` selectivity interaction.
- Updated `index.md`, `synthesis.md`, and `projects/job-search/interview-prep.md`.
- No daily-log pointer added because `projects/Agentic_RAG/log/2026-06-15.md` does not exist.

## [2026-06-15] ingest | Structured RAG

- Source fetched from `https://raw.githubusercontent.com/hcho22/Agentic_RAG/main/docs/structured-rag.md` via the GitHub API raw-content endpoint and saved verbatim to `raw/structured-rag.md`.
- Created `sources/structured-rag.md` with summary, key claims, concept links, and provenance.
- Seeded `[[text-to-sql-semantic-layer]]` from stub to seeded (source-count 0 to 1): semantic layer, two-step planner/compiler path, deterministic SQL compilation, and 30-question eval.
- Seeded `[[agentic-tools-and-subagents]]` from stub to seeded (source-count 0 to 1): ordered tool use, schema-enforced planning before SQL execution, and fallback behavior for out-of-scope questions.
- Updated `index.md`, `synthesis.md`, and `projects/job-search/interview-prep.md`.
- No daily-log pointer added because `projects/Agentic_RAG/log/2026-06-15.md` does not exist.
