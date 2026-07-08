---
type: source
tags: [claude-code, fable-5, model-routing, sub-agents, workflows, worktrees, cost-control, codex]
date: 2026-07-07
title: "Working With Fable 5 in Claude Code"
author: "Theo (T3 / soydev)"
url: ""
concepts: [model-routing-and-cost-control, agentic-coding-workflow, sub-agents-and-multi-agent, parallel-agent-orchestration, evals-for-agents, agent-skills, agent-permissions-and-safety, scheduled-agent-autonomy]
---

# Working With Fable 5 in Claude Code

Theo (T3) walks through adapting his entire agentic-coding workflow to exploit Anthropic's Fable 5: cost min-maxing (reasoning-effort discipline and routing token-heavy work to cheaper models), a model-selection glossary in CLAUDE.md, a few Codex-backed skills, and a live run that cleared a 16-PR backlog and shipped ~a month of planned work in ~5.5 hours for ~$150.
His thesis: Fable is not "a better Opus" - the unlock is how far it can go on end-to-end work and how well it decomposes tasks into sub-agents and workflows, so the prompts and mindset have to change to match.

## Key claims

- Fable is a new era, not a drop-in upgrade: reusing Opus-era prompts wastes it; restructure work around longer autonomous runs and sub-agent decomposition. He reported doing more in one day than in the prior month.
- Reasoning-effort discipline is the single biggest cost lever: keep effort in the low->high range; "high" is the best value and the default. The x-high / max / "Ultra Code" tiers second-guess themselves, loop, and over-engineer - effort applies per tool call, not to how long the agent runs, so higher effort just overthinks each step rather than solving harder problems.
- Cost routing: teach Claude Code to "shell out" (the literal CLAUDE.md trigger word) to GPT-5.5 via the Codex CLI for token-heavy or specialized work - computer use, digging through logs, reading giant PDFs/specs - so Fable orchestrates but doesn't pay for the grunt work. Total spend on the big run was ~$150 across all models; neither subscription broke 40%.
- The model-selection glossary: rate each model on intelligence, taste, and cost, and encode it in CLAUDE.md because Fable was trained before GPT-5.5/Opus 4.8 and doesn't know their current strengths. Ratings are defaults, not limits - the model may override them and re-run with a smarter model without asking ("judge the output, not the price tag").
- He disagreed live with a model-written config line that made cost a hard priority axis - a demonstration of reviewing model-generated config rather than trusting it.
- Fable now invents sub-agent archetypes per task (reviewer, adversarial reviewer, exploratory), so hand-defining fixed archetypes is no longer worth it. Sub-agents vs. workflows: sub-agents spawn helper agents; a workflow is a JavaScript file the model writes to define multi-stage fan-out-and-verify programmatically.
- Skills he keeps are Codex-backed (review, implementation, computer use); the model sees only a skill's description until it invokes it, so the description must carry enough to decide. Practical lessons: get the commands inside a skill right, prompt Codex simply (don't prompt it like Claude), and handle the empty-result case explicitly. "Don't blindly copy someone else's skills/config" - build your own and be unafraid to edit and break things.
- The live triage: "investigate and review the open PRs... use a workflow to break up the work into multiple reviewers." The model ran 48 agents (16 investigators, one per PR) each stress-tested by a Fable+Opus judge panel; 14/16 verdicts were unanimous and it resolved the 2 contested ones, returning a suggested order of operations.
- The "goal" long-running loop: he granted explicit permission to create worktrees, rebase, branch, merge and close PRs, work step-by-step against a repo `to-do.md`, and - crucially - not merge until automated reviewers (Bugbot, Macroscope, Code Rabbit) approve. It ran ~5 hours and merged a month's roadmap. He burned more tokens verifying than producing.
- Aggressive auto-merge is only safe because production stays human-gated: merging to main deploys to staging only; the agent cannot touch prod.
- Parallelization: T3 Code (web/desktop/open-source mobile) plus Tailscale drives agents across machines, including from his phone; any bug/idea spins up a new worktree or workflow. He had Fable merge changes from all worktrees into one conflict-resolved branch in ~5 minutes.
- Time-to-fix and files-touched as a codebase-health diagnostic: under ~3 min likely simple, ~15 min worth attention, an hour+ suggests an architecture problem; a too-fast fix is also suspect. When unsure, ask the model questions.
- Vibe Proxy auto-splits traffic across accounts to avoid usage caps, at the cost of some built-in Claude Code features (it uses the API-key version).

## Connections

- [[model-routing-and-cost-control]] - the core of this source: reasoning-effort discipline, routing token-heavy work to GPT-5.5/Codex, the intelligence/taste/cost glossary, "judge the output not the price tag," and Vibe Proxy.
- [[agentic-coding-workflow]] - "Fable is a new era" mindset, the run-until-done "goal", aligning by asking the model questions, a repo `to-do.md` as a durable checklist, and time-to-fix as a health signal.
- [[sub-agents-and-multi-agent]] - the model inventing sub-agent archetypes per task, Codex-backed sub-agents, and the 48-agent triage (investigators + judge panel).
- [[parallel-agent-orchestration]] - workflows vs. worktrees (a single workflow is the wrong tool for checkpoint-driven work), multi-machine T3 Code + Tailscale, and merging many worktrees into one branch.
- [[evals-for-agents]] - the Fable+Opus judge panel over 16 investigators, independent Codex review with claims verified against the code, and automated reviewers gating every merge.
- [[agent-skills]] - Codex review/implementation/computer-use skills, description-first loading, commands mattering most, and "don't blindly copy config."
- [[agent-permissions-and-safety]] - staging-only auto-merge with prod human-gated, explicit capability grants for the goal run, and reviewer-approval-before-merge.
- [[scheduled-agent-autonomy]] - the "goal" as a run-until-conditions-pass loop with an objective definition of done.

## Source

- **Author / channel:** Theo (T3 / soydev)
- **Title:** Working With Fable 5 in Claude Code
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/Fable5_ClaudeCode_Workflow_Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-07
