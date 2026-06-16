# Interview Prep

Canonical home for interview talking points consolidated across projects and wikis. Project wikis can point here or add points here, rather than maintaining separate per-wiki prep lists.

## Agentic RAG

- Built a retrieval eval suite around a fixed corpus and 50-question golden set, scoring vector, keyword, and hybrid retrieval with recall@k, MRR, and nDCG@5.
- CI runs the retrieval suite against PR head and `main`, then posts a delta table so retrieval regressions are visible in code review.
- Demonstrated the gate with a real chunk-size regression: changing chunk size from 500 to 100 drove vector/hybrid recall@5 from 0.860 to 0.350, especially hurting multi-hop and paraphrase questions.
- Separated retrieval quality, answer quality, and permission correctness: retrieval metrics cover gold chunks, RAGAS/Claude cover generated answer behavior, and no-access cells stay a hard security check.
- Added RAGAS as standardized vocabulary while keeping an independent Claude judge for corroboration, avoiding overreliance on a same-family judge.
- Designed permissions-aware retrieval by pushing ACLs into the SQL predicate, avoiding post-filter recall collapse for sparse viewers and making authorization part of candidate ranking.
- Built an ACL model with per-chunk grants, group principals, RLS-compatible helper functions, granting-principal display, and snapshot-and-replay for re-chunking shared documents.
- Evaluated permission correctness separately from quality: no-access viewers returned zero gold chunks across vector, keyword, and hybrid modes.
- Replaced naive text-to-SQL with a semantic-layer planner plus deterministic SQL compiler; the structured eval improved from 10% naive accuracy to 100% semantic accuracy on 30 questions.
- Constrained the database tool path through tool schemas: `plan_query` must produce a validated plan before `sql_search` can compile and execute read-only SQL.
