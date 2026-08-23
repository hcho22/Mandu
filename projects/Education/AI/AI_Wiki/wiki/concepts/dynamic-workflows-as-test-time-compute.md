---
type: concept
tags: [agentic-engineering, orchestration, workflows, scaling, anthropic]
status: seed
source-count: 1
last-updated: 2026-08-01
---

# Dynamic Workflows as a Test-Time Compute Axis

[[boris-cherny]] in [[building-at-the-frontier]] frames agent orchestration not as a convenience feature but as **a new axis of scaling**.

Scaling laws historically ran on neural net size, training data, and training FLOPs.
**Test-time compute** - how many tokens are generated at inference - was added recently.
Dynamic workflows are a new way to **orchestrate and dramatically ramp up test-time compute on a single hard task**.
Boris notes this has not been written about much.

## How it works

- **Invocation is literally "use a workflow."** Claude triggers the dynamic workflow itself.
- Mechanically, Anthropic uses the **Bun** runtime as a sandbox, starts a VM inside it, and lets Claude start and orchestrate many agents there.
- It is not one agent, and not ten parallel agents.
For a codebase rewrite, deep data analysis, or a multi-stage feature spanning dozens of PRs it will **fan out** agents for a first pass, run a **second stage that verifies or summarizes** that work, fan out again for a third stage, and so on.
- Boris's background is functional programming, so the design is **an algebra for agents**: primitives for running agents in sequence and in parallel, with tools for Claude to orchestrate them token-efficiently.
- The Electron-to-Swift run ([[long-horizon-agent-runs]]) has spawned an estimated **thousands to tens of thousands** of agents this way.

## Workflow versus loop versus routine

The clearest statement of the distinction in the wiki so far:

| Primitive | Shape | Context |
|---|---|---|
| **Dynamic workflow** | *One* task broken into chunks | Shares context across chunks |
| **Loop** | *One repetitive* task, run over and over, locally (a cron job for Claude) | Does **not** share context; may share memory |
| **Routine** | The same as a loop, but in the cloud so you can close your laptop | Does **not** share context; may share memory |

## Synthesis

The reframe is the valuable part.
Treating orchestration as a scaling axis rather than a productivity feature explains why the fan-out/verify/fan-out shape keeps recurring across otherwise unrelated sources - it is not a design preference, it is the mechanism by which you spend more compute on one problem.

This completes a picture the wiki had in pieces.
[[verification-signal-picks-the-mechanism]] gave the selection rule between primitives; [[sub-agents]] gave the context-hygiene argument for fanning out; [[self-referential-bias]] gave the reason the verify stage must be a *different* agent.
This page supplies the reason all three exist together: the verify stage is not quality control bolted onto parallelism, it is **half of the compute-spending structure**.

The local/cloud split (loop versus routine) also resolves an ambiguity the wiki carried from [[business-loops]] and [[agents-as-cron-plus-markdown]], both of which describe scheduled repetitive work without naming whose machine it runs on.
