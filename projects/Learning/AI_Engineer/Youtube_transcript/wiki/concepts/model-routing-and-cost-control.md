---
type: concept
tags: [model-routing, cost-control, reasoning-effort, multi-model, orchestration, economics]
date: 2026-07-07
source-count: 1
status: seeded
---

# Model Routing and Cost Control

Treating the model itself as a routing decision rather than a fixed choice: pick reasoning effort deliberately, send each unit of work to the cheapest model that clears the quality bar, and let a smart-but-expensive model orchestrate while cheaper models do the token-heavy grunt work - so cost tracks value instead of exploding.

## From the sources

[[working-with-fable-5-in-claude-code]] is the sharpest treatment of routing and cost as a first-class skill:

- **Reasoning-effort discipline is the biggest single lever.** Keep effort in the low->high range; "high" is the best value and the default. The x-high / max / "Ultra Code" tiers second-guess themselves, run in loops, and over-engineer. The key mental model: effort applies *per tool call / per change*, not to how long the agent can run overall - a 500-step task doesn't get more steps from max, each step just overthinks. He estimates leaving effort on "high" halves many people's bills, and reads Ultra Code's "many highs under the hood" as Anthropic itself agreeing high is the sweet spot.
- **Route token-heavy work to a cheaper model.** Teach Claude Code to "shell out" (the literal CLAUDE.md trigger word) to GPT-5.5 via the Codex CLI for computer use, log-digging, and giant-PDF/spec reading, so the expensive model orchestrates but doesn't pay for the grunt work. On the big run, total spend across all models was ~$150 and neither subscription broke 40%.
- **Encode a model-selection glossary in CLAUDE.md.** Because Fable was trained before GPT-5.5/Opus 4.8, it doesn't know their current strengths, so he rates each model on three axes he cares about - intelligence (hardest problem it handles unsupervised), taste (UI/UX, API design, copy), and cost - and defines what those terms mean so the config is a glossary the model applies when choosing which model to call.
- **Ratings are defaults, not limits; judge the output, not the price tag.** The model has standing permission to override a cheap-model choice and re-run with a smarter one without asking if the output misses the bar. He explicitly disagreed, live, with a model-written config line that made cost a hard priority axis - use cheap models to gather info and try things, then move the real work to a more expensive model.
- **Escape hatches for usage caps.** Vibe Proxy auto-splits traffic across accounts (at the cost of some built-in Claude Code features, since it uses the API-key version). A workflow quirk: workflows must call a Claude model, so to use GPT-5.5 inside one he has Sonnet-on-low spawn Codex and report the result back.

## Synthesis

This concept reframes "which model should I use?" from a one-time default into a per-task routing decision with an economic objective: **spend tokens where they buy quality and nowhere else.** Three moves make that concrete. **Effort is a cost dial, not an intelligence dial** - the load-bearing insight is that reasoning effort is spent per step, so the top tiers mostly buy over-reasoning and over-editing rather than harder-problem-solving; "high and stop thinking about it" is the default for a reason. **Orchestrate expensive, execute cheap** - a capable model plans and reviews while a cheaper model (GPT-5.5 via Codex) grinds through high-token investigation and computer use, which is the same expensive-thinking / cheap-output split that [[parallel-agent-orchestration]] and [[sub-agents-and-multi-agent]] make at the agent level, applied across model families. **Encode judgment as a glossary the model can act on** - naming your quality axes (intelligence, taste, cost) in CLAUDE.md is a [[context-engineering]] act that lets the agent route on your behalf, and keeping cost a tiebreaker rather than a gate ("judge the output, not the price tag") ties routing back to [[human-taste-and-ai-slop]] and the independent-review discipline of [[evals-for-agents]]: the price is only acceptable if the output passes. For hcho's positioning this is a validation-and-cost-engineering surface - the same "measure the boundary, don't assume it" instinct pointed at inference spend, and a concrete talking point about running multi-model agent systems economically. (Single-source for now; watch whether later transcripts extend it or it folds into [[context-engineering]].)
