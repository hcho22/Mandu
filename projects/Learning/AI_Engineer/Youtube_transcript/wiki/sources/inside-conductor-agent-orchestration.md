---
type: source
tags: [orchestration, worktrees, voice-first, claude-code, codex, product-design]
date: 2026-07-03
title: "Inside Conductor: Voice-First Agent Orchestration"
author: "Charlie, co-founder of Conductor (YC S2024)"
url: ""
concepts: [agentic-coding-workflow, parallel-agent-orchestration, context-engineering, agent-permissions-and-safety, sub-agents-and-multi-agent, human-taste-and-ai-slop]
---

# Inside Conductor: Voice-First Agent Orchestration

A behind-the-scenes tour with Charlie, co-founder of Conductor (a Mac app for orchestrating many coding agents - Claude Code and Codex - at once), showing a near-zero-typing, voice-first workflow.
He "conducts" agents like an orchestra, shares the customizations that matter, his Claude-vs-Codex heuristics, and a closing thesis that code is becoming "sawdust" while prompts are the durable artifact.

## Key claims

- The core unit is a workspace, currently an abstraction around a git worktree; every workspace must create a PR you then merge - you cannot edit files directly, so no change bypasses review.
- Voice-first: kick off tasks with Command-N, dictate a prompt, and keep several agents busy at once, reviewing PRs in-app with GitHub-style inline comments; treat workspaces as cheap, disposable experiments and only promote the ones that earn it.
- Customizations that matter: a few-hundred-line CLAUDE.md plus skills files ("we're a startup - don't write enterprise code"), always fast mode ("if you're trying to token max, you have to be in fast mode"), Context7 MCP for docs, and running Claude with "dangerously accept all permissions" as Conductor's default.
- "Slop-free zones": clearly bounded, human-written sections where every line must be read by a human, some marked "do not touch if you are an AI - human eyes only." Without boundaries the AI can enter a vicious cycle - it sees bad code and writes more.
- Don't let the AI be your architect: humans own the core concepts, APIs/contracts, and interface; AI-made UI choices tend not to feel "crafted." Give the AI free rein only in clearly separated, non-core areas. Conviction comes from dogfooding and gut feel, not A/B tests.
- Claude vs. Codex heuristic: reach for Opus when building something new/creative (more of a partner, more back-and-forth); reach for Codex as the workhorse to grind through a long, specific debugging problem.
- Token-max aggressively (fast mode, high effort everywhere) but keep lines of code minimal - spend on thinking, not output volume; unchecked LOC growth spirals a codebase out of control. Peak spend was ~$22k on tokens in one month.
- Open questions on the future: cloud workspaces so agents run ~10x longer unconstrained by your machine, whether you should talk to sub-agents or have multiplayer chats, and "code as sawdust" - you craft the description and rerun prompts on next-gen models, so prompts, not code, are what matter.

## Connections

- [[agentic-coding-workflow]] - the enforced workspace -> PR -> merge loop and reviewing PRs in-app.
- [[parallel-agent-orchestration]] - conducting many agents at once, workspaces as disposable worktree-backed experiments, and the "CEO of a little company" metaphor.
- [[context-engineering]] - a tuned CLAUDE.md + skills files, fast mode for token-maxing, and Context7 MCP for docs.
- [[agent-permissions-and-safety]] - "dangerously accept all permissions" as a default, and slop-free / "human eyes only" zones as guardrails.
- [[sub-agents-and-multi-agent]] - open questions about talking to sub-agents and multiplayer agent collaboration.
- [[human-taste-and-ai-slop]] - don't-let-the-AI-be-your-architect, crafted UI, slop-free zones, and conviction from gut feel.

## Source

- **Author / channel:** Charlie, co-founder of Conductor (YC Summer 2024)
- **Title:** Inside Conductor: Voice-First Agent Orchestration
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/Conductor-Workflow-Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-03
