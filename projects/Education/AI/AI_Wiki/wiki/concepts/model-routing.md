---
type: concept
tags: [models, workflow, cost-control, orchestration, claude, codex]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Model Routing

From [[working-with-fable-5]]: let one capable model orchestrate while it "shells out" to a cheaper or more specialized model for the token-heavy grunt work.
Theo ([[theo-t3]]) has Fable steer and calls GPT-5.5 through the Codex CLI ([[openai]]) via `bash`, so the expensive model never pays for the cheap work.

## Key points

- **Orchestrator vs worker split:** the smart, tasteful model plans, reviews, and writes the user-facing parts; a cheap high-throughput model does bulk mechanical implementation, log digging, giant-PDF reading, and computer use.
- **The trigger is a config convention:** the phrase "shell out" in `CLAUDE.md` tells the model it may call another CLI through `bash` (which the agent already has).
- **Cost impact is large:** routing the grunt work kept a month-scale run near $150 total; neither subscription passed ~40% usage. Setup took ~1 hour.
- **Quirk:** a Claude Code workflow must call a Claude model, so to use GPT-5.5 inside a workflow you have a cheap Claude model (e.g. Sonnet on low) spawn Codex, collect the result, and report it back. Prefix such sub-agents so you can spot them in logs.
- **Prompt the worker in its own idiom:** Claude tends to prompt Codex as if it were Claude; keep worker prompts simple and skip heavy guardrails Codex does not need.

## Synthesis

Model routing is the operational form of [[model-selection]]: selection says which model fits a task shape; routing is the plumbing that lets a single run use several models at once, each on the sub-task it is best and cheapest at.
It pairs naturally with [[adversarial-code-review]] (route the review to a *different* model for an independent perspective) and with [[reasoning-effort-discipline]] (the other big cost lever in the same source).
For hcho this is a concrete, demonstrable production-engineering skill: cost-aware multi-model orchestration with the expensive model reserved for judgment - exactly the validation-adjacent layer his background supports.
