# Log

Append-only chronological record of wiki operations (ingest, query, lint).
Each entry starts with `## [YYYY-MM-DD] <op> | <title>` so it is greppable: `grep "^## \[" log.md | tail -5`.
Never edit or delete past entries. Only append.

## [2026-07-08] setup | Wiki created
- Stood up the Job-Search Roles Wiki inside `projects/Job_Search/`.
- Created the schema [[CLAUDE]], [[README]], [[index]], [[synthesis]], and the `roles/ skills/ companies/ sources/` folders with a sibling `../raw/` inbox.
- Mode: full. Domain: target roles, their qualifications/skills, and hcho's path into them.

## [2026-07-08] ingest | Applied AI Engineer role research
- Ingested [[applied-ai-engineer-role-research]] (research pull, raw/applied-ai-engineer-role-research-2026-07-08.md).
- Created role [[applied-ai-engineer]] (fit 4/5, AI builder bucket).
- Created skills [[rag-systems]] (strong), [[eval-pipeline-design]] (strong, differentiator), [[mlops-deployment]] (working, largest gap), [[python]] (working).
- Left [[agent-orchestration]] and [[llm-application-development]] as to-do link markers.
- Updated [[index]]; revised [[synthesis]] (top role + highest-leverage gap = deployment/cloud).
- No contradictions (first content ingest).

## [2026-07-08] ingest | Real job-posting batch (15 postings, 8 companies)
- Batch-ingested 15 real job postings uploaded to raw/ (one non-posting, react-pattern-primer, left untouched in raw/).
- Sources: [[anthropic-applied-ai-engineer-beneficial-deployments]], [[cohere-applied-ai-engineer]], [[anthropic-forward-deployed-engineer-applied-ai]], [[vercel-forward-deployed-engineer]], [[vercel-forward-deployed-engineer-v0]], [[langchain-deployed-engineer]], [[cohere-fde-agentic-platform]], [[cohere-fde-prompt-specialist]], [[cohere-fde-sovereign-ai]], [[closure-founding-forward-deployed-engineer]], [[hex-ai-research-engineer]], [[hex-ai-research-engineer-search-and-context]], [[llamaindex-ai-content-engineer]], [[cresta-ml-engineer-ai-agents]], [[closure-founding-ai-engineer-mts]].
- Roles: extended [[applied-ai-engineer]] (now 3 sources, established); created [[forward-deployed-engineer]] (8 sources, dominant archetype), [[ai-research-engineer]], [[ai-content-engineer]], [[ml-engineer-ai-agents]], [[founding-ai-engineer]].
- Companies (new): [[anthropic]], [[cohere]], [[vercel]], [[hex]], [[langchain]], [[cresta]], [[closure]], [[llamaindex]].
- Skills: extended [[rag-systems]], [[eval-pipeline-design]], [[mlops-deployment]], [[python]] (real demand counts); created [[agent-orchestration]], [[llm-application-development]], [[customer-facing-delivery]], [[typescript]], [[prompt-engineering]], [[distributed-systems]], [[nextjs-react]], [[technical-writing-benchmarking]].
- Contradiction flagged: first ingest framed MLOps/cloud as the single biggest gap; real postings weight customer-facing delivery + agentic architectures at least as heavily. [[customer-facing-delivery]] is now the primary blocker. Both tracked in [[applied-ai-engineer]] and [[synthesis]].
- Key finding: evaluation is a named requirement in nearly every posting - confirms evals as hcho's headline differentiator at scale.
- Updated [[index]] and [[synthesis]] (re-ranked roles, split real vs visibility gaps, 5-step plan).

## [2026-07-08] query | Why RAG matters for landing an AI role
- Answered why RAG is a strong hiring signal (dominant private-data pattern, +10-15% comp, ~340% posting growth, bundles the hard parts).
- Filed the answer back as a "Why it matters for landing a role" section on [[rag-systems]] (schema has no concepts/ folder, so enriched the skill page rather than create an orphan).
- Cross-linked [[eval-pipeline-design]], [[applied-ai-engineer-role-research]], [[cohere]], [[hex]], [[closure]], [[forward-deployed-engineer]].
