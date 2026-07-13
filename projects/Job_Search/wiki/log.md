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

## [2026-07-13] ingest | Cohere FDE, Agentic Platform (West Coast)
- Ingested [[cohere-fde-agentic-platform-west-coast]] (raw/Forward Deployed Engineer, Agentic Platform (West Coast).md), a West-Coast/remote variant of the already-ingested [[cohere-fde-agentic-platform]] (distinct Ashby URL). Surfaced in the 2026-07-13 job-hunter scan at Fit 5.
- Durable new signal: the variant is remote with **Los Angeles among eligible locations** - first Cohere FDE that is LA-local-eligible for hcho - plus an unusually explicit eval-framework requirement ("robust evaluation frameworks to measure agent accuracy, safety, and latency").
- Pages touched: created source [[cohere-fde-agentic-platform-west-coast]]; extended role [[forward-deployed-engineer]] (source-count 8->9, added West Coast variant, added location-no-longer-a-blocker note to fit/gap); [[cohere]] company (count 4->5, added variant + LA-remote, fixed stale "not in companies.yaml" cross-ref -> now on the list); [[eval-pipeline-design]] (count 8->9, added the verbatim-bar framing tip); [[index]] and [[synthesis]] (FDE entry points now lead with the LA-eligible West Coast FDE).
- No contradictions. Reinforces (does not challenge) the standing read: FDE technical core is in reach, [[customer-facing-delivery]] + 20-40% travel remain the gaps; evals is the differentiator to lead with.

## [2026-07-13] maintenance | Collapsed the two Cohere Agentic Platform FDE source pages into one
- Per hcho: merged the West Coast variant page into the canonical [[cohere-fde-agentic-platform]], which now covers BOTH postings (general/on-prem + West Coast) with both URLs and both raw files listed under "Postings covered." Deleted `sources/cohere-fde-agentic-platform-west-coast.md`.
- Both raw files remain untouched in `../raw/` (immutability preserved).
- Repointed all live backlinks from [[cohere-fde-agentic-platform-west-coast]] to [[cohere-fde-agentic-platform]] in [[forward-deployed-engineer]], [[cohere]], [[eval-pipeline-design]], [[index]], [[synthesis]].
- Reverted the source-page counts bumped in the prior ingest entry (they counted the now-merged page as separate): [[forward-deployed-engineer]] 9->8, [[eval-pipeline-design]] 9->8, [[cohere]] 5->4. Posting counts in prose are unchanged (FDE still informed by 9 postings; Cohere still 5 postings) - only the source-*page* counts changed.
- The 2026-07-13 ingest entry above retains its original [[cohere-fde-agentic-platform-west-coast]] references as historical record (log is append-only); that slug no longer resolves to a page by design.
