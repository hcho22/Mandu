---
type: concept
tags: [agentic-engineering, context-engineering, compaction, contradiction]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Compaction Quality Beats Context-Window Size

**"Compaction is really becoming an implementation detail that most people should not worry about anymore.**
Just let the agent run, let the agent compact when needed, and it will just keep going."

Kun in [[agentic-full-stack-build]], after a full-stack build that ran through **four auto-compactions with no visible degradation**.

## The evidence

- At one point context sat at ~**70% of 272K**; after compaction it dropped to **9.5%**, and the agent still knew exactly what was being built.
- He relies entirely on **auto**-compaction and never triggers it proactively.
- **Claude's 1M-token context window doesn't make much practical difference here**, because compaction quality matters more than raw window size.

## What actually makes it safe

The claim is not "context management is solved," it is "context management has moved into the harness *provided you do one thing*":

**Persist important state to files.**
Because dispatched crewmate tasks are documented to files ([[one-orchestrator-agent]]), anything lost in compaction can be retrieved when the agent actually needs it.
The file system is the durable memory; the context window is a cache.

Mechanics worth knowing:
Codex has a **server-side compaction** capability better than any other he knows of, but running GPT models in a third-party harness does *not* get it automatically - the harness uses its own algorithm unless you install the extension that restores it.
He also caps requests at **272K** deliberately, citing a reported billing bug where requests exceeding the context cap are charged higher than usual.

## The contradiction to hold

This directly tensions with [[context-rot]], which the wiki records from [[building-5-ai-products-solo]]: **reliability decays as context fills, so start each unit of work fresh.**

| Position | Source | Claim |
|---|---|---|
| [[context-rot]] | [[building-5-ai-products-solo]] | Degradation is real; manage it by starting fresh |
| This page | [[agentic-full-stack-build]] | Four compactions, no visible degradation; stop managing it |

The reconciliation is probably that **both are true at different layers.**
[[fresh-context-review]] argues for a clean context because a *biased* reviewer misses bugs - that is about contamination, not capacity, and compaction does not fix it.
[[context-rot]] as originally recorded is about capacity degradation, and that is the claim compaction quality has plausibly eroded.

But this should be held as an open question, not resolved.
The evidence here is a single session on one model in one harness, and "no visible degradation" is a subjective read by someone who deliberately was not reading tool calls.
[[sub-agents]] exists partly to keep context clean, and if compaction were fully solved that rationale would weaken - which no source claims.

## Synthesis

The useful reframe is that **the context window is not the unit of memory - the file system is.**
Once state is durable on disk, compaction stops being a loss event and becomes an eviction from cache, which is a much less frightening thing.

That reframe also explains why the practices that make compaction safe are the same ones that make [[sub-agents]] and [[one-orchestrator-agent]] work: write down what you decided.
The wiki's own daily-log and decision-log conventions are the human version of the same discipline.

Practically, this argues against hand-managing context and in favor of investing in the artifacts - implementation notes, decision records, task files - that survive it.
