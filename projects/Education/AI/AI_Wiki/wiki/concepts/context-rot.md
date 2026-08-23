---
type: concept
tags: [context-engineering, agents, craft]
status: developing
source-count: 2
last-updated: 2026-08-01
---

# Context Rot

The degradation in an agent's reliability as its context window fills with accumulated, increasingly noisy history, named in [[building-5-ai-products-solo]] as a driver of hallucination.

## Key points

- A long-running session accumulates stale detail; the model hallucinates more as the signal-to-noise of its context drops.
- Mitigation: start each unit of work with **fresh context** (a new git worktree per phase; a clean session), carrying only a compact progress/decisions file forward.
- This is the operational reason behind [[phased-implementation]]'s fresh-worktree-per-phase rule.
- Two practical tools from [[every-claude-feature-ranked]]: watch a **status line** (model, effort, context %) to know when to `/clear` or `/compact`, and prefer [[checkpoint-rewind]] over piling corrections onto a wrong turn.

## Challenged (2026-08-01)

[[agentic-full-stack-build]] reports the opposite experience and it has to be recorded rather than smoothed over.
Kun ran an entire full-stack build through **four auto-compactions with no visible degradation** - at one point context dropped from ~70% of 272K to 9.5%, and the agent still knew exactly what was being built.
His conclusion: "compaction is really becoming an implementation detail that most people should not worry about anymore," and Claude's 1M-token window matters less than compaction *quality*.
See [[compaction-over-context-window]].

| Position | Source | Date |
|---|---|---|
| Reliability decays as context fills; start fresh | [[building-5-ai-products-solo]] | ingested 2026-07-08 |
| Four clean compactions, no visible degradation; stop managing it | [[agentic-full-stack-build]] | ingested 2026-08-01 |

**How much this actually concedes.**
Probably the capacity claim and not the contamination claim.
[[fresh-context-review]] wants a clean context because a *biased* reviewer misses bugs, which compaction does not fix - a compacted summary of your own reasoning is still your own reasoning.
The mitigation that survives in both accounts is **persist decisions and progress to files**, which this page already recommended and which is exactly what Kun credits for making compaction safe.

Two reasons not to fully concede yet: the counter-evidence is one session, on one model, in one harness, judged subjectively by someone deliberately not reading tool calls; and [[sub-agents]] exists partly to keep context clean, a rationale no source has retracted.

## Synthesis

Context rot is the failure mode that [[context-is-king]] guards against from the other side: not just "give good context," but "keep context clean."
It motivates practices across the wiki - [[fresh-context-review]], fresh graders in the [[skill-eval-loop]], [[sub-agents]] that return only conclusions, session-handoff skills in [[building-skills]], and per-phase worktrees - all of which trade accumulated context for reliability.

As of the second source the honest position is narrower than the first: **the window is a cache, the file system is the memory**, and the practices worth keeping are the ones that write state down rather than the ones that ration context.
Whether raw capacity degradation is still a live concern at the frontier is an open question in [[agentic-engineering]], not a settled one.
