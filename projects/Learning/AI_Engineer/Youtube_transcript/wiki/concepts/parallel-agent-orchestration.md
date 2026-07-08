---
type: concept
tags: [parallelism, worktrees, orchestration, throughput, isolation]
date: 2026-07-03
source-count: 5
status: seeded
---

# Parallel Agent Orchestration

Running many coding agents at once - across and within projects - using git worktrees for isolation so parallel work never collides, with the human acting as an orchestrator who jumps into whichever thread needs judgment.

## From the sources

[[building-products-with-coding-agents]] treats parallelism as the core productivity lever:

- Because the human is needed only at the start (plan) and end (judgment) of a task, he runs 5+ sessions and 20-30 agents at once, across different projects and within the same project.
- Treehouse is a "dead simple" worktree manager that drops you into a fresh worktree from a pool with dependencies already installed, removing the cognitive load and reinstall cost of manual worktrees.
- Increasing concurrent sessions is itself the lever for getting more done; context-switching between agent threads beats meeting-driven switching.

[[building-5-ai-products-solo]] automates worktree setup for parallelism:

- Conductor opens a worktree with a setup command that assigns a unique port, copies env vars, and starts processes, so ~10 agents run simultaneously, each in its own browser.
- Fresh worktrees also serve as isolated per-phase checkpoints (see [[context-engineering]]).

[[inside-conductor-agent-orchestration]] is the orchestration tool's own view:

- A workspace is an abstraction around a git worktree; kick off tasks with Command-N, keep several agents busy, and review their PRs in-app. Treat workspaces as cheap, disposable experiments and promote only the good ones.
- The aspiration is being "the CEO of a little company" whose agents bring back digestible reports you redirect or merge.

[[every-claude-feature-ranked]] names the enabling primitive:

- Git worktrees run isolated copies of a codebase so parallel work never collides, then merge back - especially important when sharing a codebase or juggling multiple features.

[[working-with-fable-5-in-claude-code]] separates workflows from worktrees and adds a multi-machine layer:

- Two distinct parallelism tools: *workflows* (a JavaScript file the model writes for programmatic multi-stage fan-out-and-verify) versus *worktrees* (isolated checkouts for checkpoint-driven work). A single workflow is the wrong tool for review-gated PR work where each step needs CI + human review + merge before the next rebase - there, orchestrate from the session and spawn worktrees, using workflows only for multi-agent review passes.
- T3 Code + Tailscale drive agents across multiple machines (even from a phone), so any bug or idea spins up a new worktree/workflow anywhere; he later had Fable merge changes from all worktrees into one conflict-resolved branch in ~5 minutes.

## Synthesis

Parallelism is what turns "get out of the loop" from a slogan into throughput: if the human is only needed at the two ends of a task, the bottleneck becomes how many tasks can be in flight, so the builders push concurrency hard (20-40 PRs/day). The enabling primitive is the **git worktree** - an isolated checkout so agents do not step on each other in one directory - and the recurring product insight is that manual worktrees have real friction (naming them, reinstalling dependencies), so every serious setup *automates* worktree lifecycle (Treehouse's pool, Conductor's per-workspace port/env setup). The human role shifts from author to **orchestrator**: the consistent metaphor is a CEO or conductor who supervises many workstreams and drops into whichever needs a decision, which only works because each stream lands as an isolated, reviewable PR (see [[agentic-coding-workflow]]). This is the session-level cousin of [[sub-agents-and-multi-agent]]: parallel *sessions/workspaces* run whole independent tasks in separate worktrees, while sub-agents run delegated subtasks inside one session to protect its context. Both are the same bet - concurrency is cheap, human attention is the scarce resource, so isolate work so it can run unattended and only pull the human in for judgment.
