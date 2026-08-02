---
type: concept
tags: [agents, context-engineering, agentic-engineering, parallelism]
status: established
source-count: 4
last-updated: 2026-08-01
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

## The criticism, and the scale (2026-08-01)

**Steerability is the named weakness** ([[agentic-full-stack-build]]).
Kun rejects the conventional spawned-sub-agent pattern on operational grounds:

> "It's really hard for you to look at what a sub-agent is doing, and it's also hard to steer a sub-agent."

His alternative keeps the fan-out and drops the opacity: "crewmates" are **ordinary agent sessions in ordinary terminal tabs** that you can drop into and redirect in plain language, dispatched by a single orchestrator you talk to ([[one-orchestrator-agent]]).
This is a real gap in the pattern as recorded above - context management and bias avoidance are both arguments about *output quality*, and neither addresses what you do when a child is going wrong mid-run.

**The scale ceiling is much higher than this page assumed** ([[building-at-the-frontier]]).
The "10 sub-agents for 10 experiments" figure above is off by orders of magnitude at the frontier: a single 15-day run has spawned an estimated **thousands to tens of thousands** of agents, in repeated fan-out / verify / fan-out stages inside a sandboxed VM.
[[boris-cherny]] frames the design as **an algebra for agents** - primitives for sequencing and parallelizing - and the point of the scale is compute, not throughput ([[dynamic-workflows-as-test-time-compute]]).

**A counterweight worth keeping in view:** [[designing-loops-and-workflows]] records Tharic cutting from five parallel Claude Code sessions to one, and [[get-out-of-the-loop]] pushes the same direction for the human. More agents is not more leverage for the *human*; it is more compute for the *task*.

## Synthesis

Sub-agents are the practical defense against [[context-rot]] and a building block of [[get-out-of-the-loop]] scale (many parallel workstreams).
They are part of [[agentic-engineering]]'s "compound engineering" pillar: structuring work across agents so the main thread stays clean and the human supervises breadth rather than depth.
The second source upgrades the rationale materially.
Context management is a performance argument, and on its own it would make sub-agents an optimization; [[self-referential-bias]] is a correctness argument, and it makes the producer/verifier split structurally necessary rather than merely tidy.
That is the version of this concept worth carrying: sub-agents are not primarily a way to go faster, they are the mechanism by which independent checking survives inside an autonomous run.

Four sources in, the open design question is **observability of the children**.
Every source agrees on fanning out and on splitting producer from verifier; they disagree on whether a child should be an opaque function call that returns a conclusion or an inspectable session you can walk into.
The frontier answer scales the first to thousands; the practitioner answer keeps the second because a human still has to intervene sometimes.
Both are right about their own workload, and which one applies depends on whether you expect to steer.
