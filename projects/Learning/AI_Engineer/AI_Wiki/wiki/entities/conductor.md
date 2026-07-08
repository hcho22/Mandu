---
type: entity
tags: [tool, orchestration, worktrees, code-review]
status: seed
source-count: 2
last-updated: 2026-07-08
---

# Conductor

A Mac app for orchestrating many coding agents ([[claude-code]] + Codex) in parallel; YC Summer 2024.
Cited in [[building-5-ai-products-solo]] and detailed in [[inside-conductor-workflow]] (co-founder Charlie).

## What it does

- **Model switching** with a "review" button and a settable review model (enables [[adversarial-code-review]], e.g. GPT-5.5 reviewing Opus).
- **Automated git worktree setup:** opening a worktree assigns a unique port, copies env vars, and starts processes, so ~10 agents run in parallel (supports [[phased-implementation]] and mitigates [[context-rot]]).
- Positioned by Josh Pigford as easier than Codex / Claude Code for parallel worktree management.

## From the co-founder deep dive ([[inside-conductor-workflow]])

- Core unit is a **workspace** (an abstraction over a git worktree); workspaces are cheap, disposable experiments promoted only if they earn it.
- **Enforced PR workflow:** you cannot edit files directly - every workspace must create a PR you merge ([[everything-is-a-pr]]).
- Voice-first orchestration (dictate, Command-N, review PRs in-app, dispatch from phone via "Conduct").
- Product philosophy: [[dont-let-ai-be-your-architect]], [[slop-free-zones]], and a crafted human-owned core; conviction from dogfooding + gut feel.
- Runs Claude with skip-permissions by default inside its sandboxed worktrees; always fast mode.
- Vision: cloud workspaces (longer-running agents) and [[code-as-sawdust]] / malleable "moddable" software.
- Stack: Tauri + native Safari renderer, Rust backend, ~90-95% TypeScript desktop, Elixir/Phoenix web.
