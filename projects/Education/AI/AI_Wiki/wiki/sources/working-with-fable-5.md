---
type: source
title: "Working With Fable 5 in Claude Code"
source-type: tutorial-summary
author: "Theo (T3 / soydev)"
url: "local"
date-ingested: 2026-07-08
date-created: unknown
tags: [claude-code, fable, model-routing, cost-control, sub-agents, workflow, codex]
---

# Working With Fable 5 in Claude Code

A summarized YouTube walkthrough by Theo ([[theo-t3]]) of how he rebuilt his agentic-coding workflow around [[anthropic|Anthropic's]] Fable 5 model.
His thesis: Fable is not "a better Opus" - reusing Opus-era prompts wastes it; the real gain is how far it can go on end-to-end work and how well it decomposes tasks into [[sub-agents]] and workflows.
The first half is cost min-maxing; the second half is a live run that cleared a 16-PR backlog and shipped a month of planned work in ~5.5 hours for ~$150 across all models.

## Key claims

- **Fable is a new era, not a drop-in upgrade** ([[build-for-the-model-of-the-future]]): to benefit, restructure work around longer autonomous runs and sub-agent decomposition instead of feeding it old prompts.
- **[[reasoning-effort-discipline]]:** keep effort in the low-to-high range; high is the best value. x-high / max / "Ultra Code" second-guess themselves, over-engineer, and cost far more. Effort is per-step overthinking, not more steps or harder problems. (Ultra Code reportedly runs many "high" passes under the hood.)
- **[[model-routing]]:** teach Claude Code to "shell out" to GPT-5.5 via the Codex CLI ([[openai]]) for token-heavy or specialized work (computer use, log digging, giant PDFs), so Fable orchestrates but does not pay for the grunt work. Total big-run spend ~$150, inside two subscriptions.
- **[[model-selection]] as a `CLAUDE.md` glossary:** rate each model on intelligence / taste / cost, define what those terms mean to you, and let the model pick per task. Ratings are defaults, not limits ("judge the output, not the price tag").
- **Skills as cross-model bridges:** Codex Review (independent review of a diff/branch), Codex Implementation, and Computer Use skills; verify Codex's claims against the code before trusting them. The model only sees a skill's description until it invokes it, so the description must carry enough to trigger it.
- **The live workflow:** a triage prompt spawned a workflow (48 agents: 16 PR investigators, each verdict stress-tested by a Fable+Opus judge panel; 14/16 unanimous), then a long-running "goal" ran ~5 hours, merging a month of work. He burned more tokens verifying than producing ([[get-out-of-the-loop]]).
- **Safety architecture:** aggressive auto-merge is only sane because merging to main deploys to **staging only**; production stays human-gated. Set the guardrail before letting an agent "merge with confidence."
- **[[time-to-fix-as-health-signal]]:** use how long an agent takes (and how many files it touches) as a diagnostic of codebase health and problem difficulty - <3 min likely simple, ~15 min worth attention, an hour+ suggests an architecture problem. Too-fast can also be wrong.
- **Tooling:** T3 Code (web + desktop + open-source mobile) + Tailscale + git worktrees to parallelize and drive agents across machines from a phone; Vibe Proxy to split traffic across accounts.

## Connections

- [[model-routing]], [[reasoning-effort-discipline]], [[time-to-fix-as-health-signal]] - the three concepts this source introduces.
- [[model-selection]] - heavily extended here (the intelligence/taste/cost glossary, defaults-not-limits).
- [[get-out-of-the-loop]] / [[plan-code-validate]] / [[everything-is-a-pr]] - the long-running "goal", to-do.md checklist, and PR-triage workflow are this cluster at scale.
- [[adversarial-code-review]] - Codex Review and the automated merge-gate reviewers (Bugbot, Macroscope, CodeRabbit) are cross-model review productionized.
- [[agent-teams]] / [[sub-agents]] - the 48-agent triage (per-PR investigators + Fable/Opus judge panel).
- [[phased-autonomy]] / [[capabilities-not-instructions]] - staging-only merge is autonomy earned behind a physical prod boundary.
- [[building-skills]] / [[self-updating-config]] - iterate skills and config from real failures; don't copy-paste others'.
- [[anthropic]], [[openai]], [[claude-code]], [[theo-t3]] - entities.

## Source

- **Author/Speaker:** Theo (T3 / soydev), builder of T3 Code
- **Title:** Working With Fable 5 in Claude Code
- **Format:** YouTube tutorial (auto-caption transcript), condensed to a reference summary
- **Tools cited:** Claude Code, Fable 5, GPT-5.5 / Codex CLI, T3 Code, Tailscale, git worktrees, Vibe Proxy; automated reviewers Bugbot, Macroscope, CodeRabbit
- **Raw:** [[Fable5_ClaudeCode_Workflow_Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
