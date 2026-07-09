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

## AI Engineering (from talks & tutorials)

_Talking points distilled from the YouTube-transcript wiki (`projects/Learning/AI_Engineer/Youtube_transcript/wiki/`). Populated as transcripts are ingested._

- Agent quality is engineered, not vibed: the strongest builder practice is a golden set of ~50 real examples with marked answers, pass/fail checks (not 1-5 scores an LLM can't calibrate), run as a gate on every prompt/model/tool change. This is the same rigor a decade of hardware validation trains, pointed at LLMs.
- Bugs are caught by independent review, not self-review: a reviewer that saw every step is biased toward believing the work is correct, so the reliable pattern is a fresh context window or a different model (e.g., Opus builds, a second model adversarially reviews and reliably finds 3-5 missed bugs). Debiasing, not redundancy.
- Agent safety is a property of capabilities, not instructions: "never send emails" is not a control if the send-email tool is on the key ring; a real incident had an agent proactively email 150k inboxes. The fix is least-privilege - remove the capability, gate dangerous tools behind per-tool approval, isolate credentials, and red-team before trusting. This maps directly to my Agentic RAG permissions-aware retrieval and no-access security cells.
- The production build loop keeps plan -> code -> validate but moves the human off the critical path: everything lands as a reviewable PR, plan depth determines how long agents run autonomously, and validation is automated with risk-based attention (low/medium/high) plus test evidence.
- Context is the scarce resource: models are stateless, so you engineer what's loaded (CLAUDE.md/skills), keep it fresh to avoid "context rot" and hallucination, and offload heavy work to sub-agents that return only a conclusion. Sub-agents (report to a caller) differ from agent teams (debate each other).
- Skills are the reusable unit of agentic work - a markdown SKILL.md an agent triggers, with progressive disclosure (short skill, separate examples), a description that gates triggering, and an eval + memory loop so it improves. I build and maintain skills in my own assistant repo, so this is demonstrable, not theoretical.
- Shipping an agent is a systems problem, not a prompting problem: durable execution (it can't stop when the user closes the tab), per-agent sandboxed compute, sessions-as-event-streams, and observability from day one - the same list whether you buy it managed (Claude Managed Agents) or assemble it (Convex/Daytona).
- System design still decides robustness: the gap between a vibe-coded app that dies at ~10 users and a robust one is deliberate trade-off analysis (scalability/reliability/performance/cost), secure data flow (never client -> DB directly), and a monorepo so the agent has whole-codebase context.
- Two market-side shifts worth naming: agents as labor (sell a completed job, not software seats; price on outcomes) and agents as customers (the agent-readable web, MCP tools/SDKs/receipts, and SEO -> AEO).
- Where the human stays: AI output asymptotes at ~80-90%, and the last 10-20% is taste and review. The mature move is bounded human-owned zones (core APIs, contracts, brand) with AI given free rein only in separated non-core areas. This is a QA instinct - decide where the human gate goes and prove the rest.
