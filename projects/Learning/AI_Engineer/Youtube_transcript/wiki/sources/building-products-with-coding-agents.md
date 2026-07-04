---
type: source
tags: [coding-agents, parallel, sub-agents, validation, testing]
date: 2026-07-03
title: "Building Products with Coding Agents"
author: "Guest: former L8 engineer (solo AI builder); Host: Peter"
url: ""
concepts: [agentic-coding-workflow, parallel-agent-orchestration, sub-agents-and-multi-agent, evals-for-agents, context-engineering]
---

# Building Products with Coding Agents

A live screen-share interview with a former L8 (Meta/Microsoft) engineer, now a solo AI builder, on a production workflow that ships ~20-40 PRs a day across 20-30 agents in 5+ parallel sessions.
The through-line is "get out of the loop": keep the plan -> code -> validate loop but move the human off the critical path, demoed with three home-built tools (Lavish, Treehouse, No Mistakes).

## Key claims

- If you review every line of code you become the bottleneck; agents now write ~10x more PRs than a human used to, so the old human-in-the-loop process does not scale. He no longer reads first-pass code and reports he "never catches anything the agents don't catch."
- Same plan -> code -> validate loop, different effort distribution: most time in planning, coding almost entirely to agents, validation mostly automated. The depth of the plan determines how long agents run autonomously (short prompt -> spec -> measurable goal).
- Parallelize sessions across and within projects because the human is only needed at the start (plan) and end (judgment); context-switching between agent threads is faster than meeting-driven switching.
- Sub-agents are mainly for keeping the main session's context window from blowing up: carve heavy, exploratory investigation out to a sub-agent that returns only its conclusion. Today's models rarely self-delegate (built-in "explore" is an exception), so you must prompt for sub-agents.
- Testing lives in a per-project AGENTS.md: agents default to shallow code-based unit tests, so you write "how I would test this myself" instructions for end-to-end validation (drive the app via browser, screenshot, check errors) and turn recurring flows into Playwright E2E tests.
- No Mistakes is a validation pipeline that reviews in a fresh context window (branch, intent, rebase, review, test, docs, lint, push, PR). Reviewing in the same session biases the agent toward believing the work is correct; a fresh reviewer catches far more edge cases.
- No Mistakes splits findings into obvious bugs (auto-fixed) vs. fixes with product implications (escalated), and attaches a low/medium/high risk assessment plus test evidence so attention is risk-based; he does not run it on trivial changes.
- Team processes built for ~10-15 PRs/month break at 10x volume; some teams have effectively stopped peer PR review, trending toward less stable products - an argument for automated review.

## Connections

- [[agentic-coding-workflow]] - get-out-of-the-loop, the plan -> code -> validate loop, plan-depth = autonomy length, and No Mistakes as the validate stage.
- [[parallel-agent-orchestration]] - 5+ sessions and 20-30 agents at once, Treehouse worktree management, and parallelism as the core productivity lever.
- [[sub-agents-and-multi-agent]] - sub-agents for context isolation, returning only conclusions, and models rarely self-delegating.
- [[evals-for-agents]] - fresh-context adversarial review, AGENTS.md testing instructions, E2E tests, and risk-based validation with evidence.
- [[context-engineering]] - AGENTS.md project context, sub-agents to protect the main context window, and fresh-context review.

## Source

- **Author / channel:** Guest - former L8 (Meta/Microsoft) engineer, now solo AI builder; Host - Peter
- **Title:** Building Products with Coding Agents
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/Building-Products-with-Agents-Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-03
