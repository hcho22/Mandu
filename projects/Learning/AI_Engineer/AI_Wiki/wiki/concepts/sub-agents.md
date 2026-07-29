---
type: concept
tags: [agents, context-engineering, agentic-engineering, parallelism]
status: developing
source-count: 2
last-updated: 2026-07-28
---

# Sub-Agents

Delegating work to child agents, primarily to protect the main session's context, from [[building-products-with-agents]] and [[designing-loops-and-workflows]].

## Key points

- **Models rarely self-delegate.** Today's harnesses do not proactively spawn sub-agents, except built-ins like Claude Code's explore agent; usually you must prompt for them explicitly.
- **The real reason to use them is context management:** carve out heavy, exploratory work that would not be meaningful to the main session, and return only the conclusion - keeping the main context small.
- Also good for many isolated tasks in parallel (e.g. spin up 10 sub-agents for 10 independent experiments; a ~200x8 benchmark run).

## The two reasons, from the primary source

[[designing-loops-and-workflows]] (an Anthropic [[claude-code]] team member) gives exactly two reasons to reach for a workflow of sub-agents rather than a single skill, and the second is new to this page:

1. **Context management** - the reason already recorded above.
2. **Avoiding [[self-referential-bias]]** - a model that grades its own output is more lenient about it, so the verifying sub-agent must be a separate instance from the producing one.

That source's prescription is three roles, each with different context *and* a different model: one coordinating, one doing, one verifying.
It notes the split has a second effect beyond bias: each role puts more compute into its own job and is less likely to stop early.

## Budget compute per parallel task

**Give each parallel sub-agent a maximum compute budget.**
Without one, the model spreads verification effort thin across simultaneous outputs and per-output quality degrades, which is the failure mode you would least expect from adding parallelism.
This is the parallel-work analogue of [[reasoning-effort-discipline]]: effort is allocated, not maximized.

Workflows are implemented as a JS file, and that file can be saved into a skill to make a reusable "skill plus workflow" package (see [[building-skills]]).
Which mechanism to use at all is governed by [[verification-signal-picks-the-mechanism]].

## Sub-agents vs agent teams

[[every-claude-feature-ranked]] draws the key contrast: sub-agents work in parallel and only report to the main session, whereas [[agent-teams]] talk to each other and debate. Parallel throughput vs deliberation.

## Synthesis

Sub-agents are the practical defense against [[context-rot]] and a building block of [[get-out-of-the-loop]] scale (many parallel workstreams).
They are part of [[agentic-engineering]]'s "compound engineering" pillar: structuring work across agents so the main thread stays clean and the human supervises breadth rather than depth.
The second source upgrades the rationale materially.
Context management is a performance argument, and on its own it would make sub-agents an optimization; [[self-referential-bias]] is a correctness argument, and it makes the producer/verifier split structurally necessary rather than merely tidy.
That is the version of this concept worth carrying: sub-agents are not primarily a way to go faster, they are the mechanism by which independent checking survives inside an autonomous run.
