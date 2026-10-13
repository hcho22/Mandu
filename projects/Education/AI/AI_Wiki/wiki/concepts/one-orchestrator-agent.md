---
type: concept
tags: [agentic-engineering, orchestration, sub-agents, cognitive-load]
status: developing
source-count: 3
last-updated: 2026-10-02
---

# One Orchestrator Agent

**Talk to exactly one agent. Let it juggle everything else.**

The "First Mate" model from [[agentic-full-stack-build]]: you are the captain, you address a single agent, and it dispatches work to "crewmates."

## Why one

- **It cuts cognitive load and context-switching burden.**
Kun's own statement of the benefit: "I don't have the mental load to worry about which agent needs to be steered versus not. I just talk to First Mate."
- Worked example from the session: he mis-stated a secret's name, and separately renamed the product from "Eddie's Wallet" to "Edie's Wallet" in one sentence.
The orchestrator handled the local repo rename, the GitHub repo rename, the project description, and a PR correcting every occurrence.
He never had to sequence it.
- When he interrupted to redirect the VPS workstream toward OpenTofu, the orchestrator **redirected the relevant workstream without him needing to know which agent was affected.**

## Crewmates versus sub-agents

Kun's criticism of the conventional [[sub-agents]] pattern is specific and worth taking seriously:

> "It's really hard for you to look at what a sub-agent is doing, and it's also hard to steer a sub-agent."

His crewmates are **ordinary agent sessions in ordinary terminal tabs**.
You can drop into any one and steer it in plain language.
When a crewmate finishes its report, the orchestrator closes the tab automatically.

So the pattern keeps the fan-out benefits of [[sub-agents]] - parallelism, clean context per task - while restoring two things a spawned sub-agent gives up: **observability and steerability**.

## Supporting practices

- **Lay down ground rules in the very first prompt** - model, reasoning level, and harness for all delegated work - before any real work starts.
- He runs **calm mode** by default, hiding all tool calls, script runs, and skill invocations, so the terminal shows only his prompt and the orchestrator's response.
His reasoning: with the weaker models of one or two years ago, watching tool calls was genuinely useful for catching wrong turns; with today's models he rarely needs to, so **the noise is no longer worth reading**.
- **Persist dispatched task state to files.** That is what makes the pattern survive compaction ([[compaction-over-context-window]]).

## Workflow reconstruction (2026-09-16)

[[kun-agentic-app-development-workflow]] extends one human interface to project-scoped Second Mates with their own crews, remote placement, and fleet digests.
This is a coordination pattern rather than proof that more hierarchy improves throughput; the guide recommends adding it only for a real bottleneck.

## The inbox alternative (2026-10-02)

[[token-maxing-with-agents]] reaches the same diagnosis - the human is single-threaded and is the bottleneck - and keeps many directly addressed threads instead of one orchestrator.
Its answer is a filtering interface: threads surface only when done or blocked, and finished threads leave view ([[agent-threads-as-inbox]]).
Kun pushes coordination down into an agent; Theo filters it in the UI.

## Synthesis

The interesting claim is not "use an orchestrator" - [[agent-teams]] and [[sub-agents]] already cover multi-agent shapes - it is that **the human's interface should be single-threaded even when the work isn't.**

That is a direct answer to the cost [[manager-of-agents]] documents.
[[ryan-carson]] tiles eight panes and checks threads every 25 minutes to keep 5-10 cloud agents straight, and says openly that it is tiring and that you will work more.
Kun's alternative is to push the coordination *down* into an agent rather than absorbing it himself.
Both are running many parallel efforts; they differ on whether the human is the scheduler.

The wiki now holds three positions on parallelism worth reading together: [[get-out-of-the-loop]] (fewer decisions), [[manager-of-agents]] (faster decisions), and this (fewer *interfaces*).
They are complementary rather than competing, and the third is the least discussed elsewhere.

Note also the deliberate reversal on tool-call watching.
[[read-what-the-agent-writes]] warns against skipping the plan; calm mode hides the execution trace entirely.
These are consistent - read the *plan*, ignore the *tool calls* - but the distinction has to be stated, because "watch what your agent does" is usually given as undifferentiated advice.
