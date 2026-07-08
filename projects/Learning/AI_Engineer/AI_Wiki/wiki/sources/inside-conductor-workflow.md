---
type: source
title: "Inside Conductor: Charlie's Voice-First Agent-Orchestration Workflow"
source-type: tutorial-summary
author: "Charlie (co-founder, Conductor)"
url: "local"
date-ingested: 2026-07-08
date-created: unknown
tags: [conductor, agent-orchestration, workflow, code-quality, model-selection, future]
---

# Inside Conductor: Charlie's Voice-First Agent-Orchestration Workflow

A summarized walkthrough with Charlie, co-founder of [[conductor]] (YC Summer 2024), a Mac app for orchestrating many coding agents ([[claude-code]] + Codex) in parallel.
He "conducts" agents like an orchestra via a near-zero-typing, voice-first workflow, and closes with a thesis that [[code-as-sawdust|code is becoming sawdust]] - a byproduct of the prompts that actually matter.

## Key claims

- **Voice-first, parallel orchestration:** kick off tasks constantly (Command-N, dictate, Enter), keep several agents busy, review PRs in-app with inline comments, and dispatch work from a phone ("Conduct").
- **Workspaces as cheap, disposable experiments:** each workspace is a git worktree; most are throwaway, and only ideas that earn it get promoted (internal to experimental). Status pipeline: In progress to In review (PR) to Done (merged).
- **Enforced PR workflow:** you cannot edit files directly - every workspace must create a PR you then merge (a hard version of [[everything-is-a-pr]]).
- **[[slop-free-zones]]:** clearly bounded, human-written sections where every line is human-reviewed, some marked "do not touch if you are an AI." Without boundaries the AI falls into a vicious cycle (sees bad code, writes more).
- **[[dont-let-ai-be-your-architect]]:** humans own the architecture, APIs/contracts, and interface; give AI free rein only in clearly separated non-core areas. AI-made UI choices do not feel "crafted."
- **[[model-selection]]:** Codex is the "workhorse" (grinds through a specific problem, many tool calls, long debugging); Claude/Opus is more of a creative "partner" (build something new).
- **Token maxing but minimal LOC:** always fast mode, high effort ("spend on thinking, not output volume"); keep lines of code minimal or the codebase spirals. Peak spend was ~$22k on tokens in one month.
- **[[code-as-sawdust]] / the future:** code used to be crafted; now you craft the description and code is the byproduct, so prompts are the durable artifact (rerun them on next-gen models). Cloud workspaces (in development) will run agents ~10x longer, unconstrained by your machine. "Malleable software" like moddable games: a crafted shared core plus user mods.
- Conviction comes from dogfooding + gut feel, not A/B tests ("when I click this, it feels right"); GUI over terminal because humans are visual, spatial creatures.

## Connections

- [[conductor]] - this source is the deep dive on it.
- [[slop-free-zones]], [[dont-let-ai-be-your-architect]], [[own-the-problem-not-the-code]] - the human-owns-the-important-parts cluster; the deliberate counterweight to [[get-out-of-the-loop]].
- [[code-as-sawdust]] - extends [[build-for-the-model-of-the-future]] (prompts, not code, are durable).
- [[everything-is-a-pr]] / [[phased-implementation]] - worktree-to-PR-to-merge, enforced.
- [[model-selection]] - Opus vs Codex ([[anthropic]] vs [[openai]]).
- [[ai-slop]] / [[taste-as-moat]] - slop-free zones and crafted UI as quality boundaries.

## Source

- **Author:** Charlie, co-founder of Conductor (YC Summer 2024)
- **Title:** Inside Conductor: Charlie's Voice-First Agent-Orchestration Workflow
- **Tools/stack cited:** Conductor, Claude Code, Codex, Context7 MCP, Spokenly/Parakeet (local dictation), Telegram; Tauri + Rust + TypeScript + Elixir/Phoenix.
- **Raw:** [[Conductor-Workflow-Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
