# Synthesis

Interview talking points are not kept here; they consolidate in the single job-search prep surface at `projects/job-search/interview-prep.md` (see the Agentic RAG section).

## Thesis (one paragraph)

Agentic RAG is strongest as a portfolio project when the retrieval system is treated as measured infrastructure, not a demo feature: [[hybrid-retrieval-rrf]] gives the app multiple retrieval strategies, [[retrieval-eval-suite]] makes their quality falsifiable, [[ci-eval-gating]] turns quality into a regression signal, [[ragas-metrics]] extends evaluation from retrieval into answer/context behavior, and [[security-correctness-eval]] keeps permissions as a hard correctness property rather than a soft answer-quality score.

## How the concepts connect

- [[hybrid-retrieval-rrf]] is the retrieval surface being tested: vector, keyword, and hybrid modes are useful only if their trade-offs can be compared.
- [[retrieval-eval-suite]] is the measurement backbone: fixed corpus, stable gold chunks, category slices, and ranking metrics make retrieval changes reviewable.
- [[ci-eval-gating]] operationalizes the suite by comparing PR head against `main` and showing mode/category deltas when a retrieval change regresses quality.
- [[ragas-metrics]] adds generation-side and context-side scoring for selected hybrid cells, but keeps the custom Claude judge as the independent corroborating signal.
- [[security-correctness-eval]] sits beside the quality metrics: no-access behavior is an authorization invariant, not something to average into RAGAS or a retrieval score.

## Open questions

- How large should the golden set become before per-category changes are statistically meaningful enough to gate merges?
- Should the retrieval suite add latency, cost, and reranker-specific metrics, or keep those in a separate performance eval?
- What is the right corpus strategy beyond the current 7-document Acme set: larger synthetic policy corpora, real docs, or multiple domain slices?
- Should embedding model fingerprints be captured so silent provider-side model updates are visible in eval history?
- How should the security table and RAGAS tables be presented together so reviewers see quality regressions and permission failures as separate classes of risk?
