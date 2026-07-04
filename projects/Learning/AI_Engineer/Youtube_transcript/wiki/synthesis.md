# Synthesis

Interview talking points are not kept here; they consolidate in the single job-search prep surface at `projects/job-search/interview-prep.md` (see the `## AI Engineering (from talks & tutorials)` section).

## Thesis (one paragraph)

The first eleven transcripts converge on one shift: with a capable model as a commodity, the differentiator moves to the *system around the model* - the context you load, the skills you encode, the permissions you grant, the evals that gate quality, and the schedule that runs it all. Practically, this plays out as an inversion of the human's job. The [[agentic-coding-workflow]] keeps the old plan -> code -> validate loop but moves the human off the critical path, coordinating many isolated agents ([[parallel-agent-orchestration]], [[sub-agents-and-multi-agent]]) whose behavior is defined once as reusable [[agent-skills]] and whose context is deliberately budgeted ([[context-engineering]]) and persisted ([[agent-memory]]). What keeps that safe and good rather than fast and wrong is a validation-and-safety spine: [[evals-for-agents]] (pass/fail checks, rubric iteration, independent review), [[agent-permissions-and-safety]] (least-privilege capabilities, not instructions), and a human gate on taste ([[human-taste-and-ai-slop]]). Above the build sit the productization and runtime layers - [[agents-as-labor]] and [[agentic-web-and-aeo]] on the market side, [[production-agent-infrastructure]] and [[agentic-system-design]] on the systems side. The recurring lesson for someone positioning on validation rigor: agent quality is engineered - golden sets, independent graders, capability boundaries, observability - not vibed.

## How the concepts connect

- **The build loop is the spine.** [[agentic-coding-workflow]] (get out of the loop, everything is a PR) depends on [[parallel-agent-orchestration]] for throughput and [[sub-agents-and-multi-agent]] for delegation; both isolate work so it can run unattended.
- **Skills are the reusable unit.** [[agent-skills]] is what an agent *is* made of; [[scheduled-agent-autonomy]] is a skill plus a cron, and an agent (in [[production-agent-infrastructure]]) is a skill set plus permissions plus a runtime.
- **Context and memory are the token economy.** [[context-engineering]] budgets the in-session window (fresh context, sub-agents, compaction); [[agent-memory]] persists what should survive between sessions. They are the transient/durable halves of the same resource.
- **Evals, permissions, and taste are the quality spine.** [[evals-for-agents]] proves correctness with independent graders, [[agent-permissions-and-safety]] bounds capability (safety is about capabilities, not instructions), and [[human-taste-and-ai-slop]] keeps a human gate on the final 10-20%. These are the through-line to the evals and Agentic RAG wikis.
- **Business and systems layers sit above the build.** [[agents-as-labor]] and [[agentic-web-and-aeo]] are the supply and demand sides of the agent economy; [[agentic-system-design]] and [[production-agent-infrastructure]] are the architecture and runtime that make an agent a product, not a demo.
- **Cross-wiki spine.** [[evals-for-agents]] links to [[llm-as-judge]], [[agent-eval-and-stats]], and [[ci-eval-gates-and-drift]] (evals wiki) and to [[retrieval-eval-suite]] / [[security-correctness-eval]] (Agentic RAG); [[agent-permissions-and-safety]] links to [[hallucination-safety-redteam]] and [[permissions-aware-retrieval]]; [[sub-agents-and-multi-agent]] links to [[agentic-tools-and-subagents]]; [[production-agent-infrastructure]] links to [[observability-langsmith]].

## Open questions

- Is the standard source template sufficient for video, or does timestamp-aware citation ("at 12:34") earn a transcript-specific template once ~5 more transcripts are in? (Deferred per the PRD.)
- Several sources are creator/marketing-driven (Skool/newsletter plugs, sponsor segments). What is the rule of thumb for separating durable engineering practice from promotional claims when ingesting, so the wiki stays trustworthy?
- Two concepts are single-source ([[agentic-system-design]], [[agentic-web-and-aeo]]). Do they hold as standalone pages, or fold into neighbors if the next transcripts do not extend them?
- Provenance is incomplete: none of the 11 sources has a recorded URL, and a few author/channel names are best-guesses. Backfill URLs so `## Source` sections are verifiable.
- When a transcript overlaps a topic the evals or Agentic RAG wiki already owns (evals, permissions, observability), the current rule is cross-link rather than duplicate. Does that stay clean as the index grows, or does it need a lightweight topic grouping?
