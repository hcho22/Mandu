---
type: concept
tags: [claude-code, skills, agentic-engineering, workflow]
status: established
source-count: 4
last-updated: 2026-07-28
---

# Building Skills

The practice, from [[ai-operating-system-tutorial]], [[ai-skill-from-scratch]], and [[every-claude-feature-ranked]], of turning your recurring work into reusable [[claude-code]] skills (the Capabilities layer of the [[four-cs-framework]]).
[[every-claude-feature-ranked]] ranks skills the #1 feature: a skill is "a recipe" that makes the agent perform far more consistently than a re-typed prompt, works across Code/chat/Cowork, can chain to other skills, and can be bundled with hooks/MCP as plugins.

## Two ways to build a skill

- **Forward:** look at your cadence (what you do every day / week / many times a day), tell Claude Code to use the skill creator, give it the end goal plus the tools and considerations you hold in mind, then build, correct, and iterate (a skill may take ~50 tries to like).
- **Reverse-engineer (often easier):** do a task end-to-end, then ask Claude Code to look back over the conversation - what did we do, what did you think about, what tools and questions came up - and build a skill that reliably reproduces that output.

## The five-step method and skill anatomy

[[ai-skill-from-scratch]] details the build: (1) create from separate example files + context, (2) write an explicit "Use when XYZ" description (the AI reads only name + description to decide whether to load the skill), (3) add a [[skill-eval-loop]] via `evals.md`, (4) add a concise `memory.md`, (5) run a skill-editor skill to strip [[ai-slop]] and enforce progressive disclosure.
A mature skill folder is therefore: `SKILL.md` (workflow + "use when" description), example files (kept separate), `evals.md` (pass/fail checks), `memory.md` (lessons).

## Rules

- **Evolve every use:** give feedback after each run and update the skill.
- A skill is not only a big workflow or SOP; even a repeated prompt deserves to become a skill / slash command (e.g. a global `session-handoff` skill).
- **Keep it human-reviewable:** favor concise, progressive-disclosure skills over long ones no one reads.

## From the primary source ([[designing-loops-and-workflows]])

[[tharic]], on Anthropic's [[claude-code]] team, adds three points:

- **Skill plus workflow is one artifact.** Workflows are implemented as a JS file, and that file can be saved into a skill, so a skill can carry its own [[sub-agents]] fan-out and verification structure rather than being a single-agent recipe.
- **Understand before you package.** He deliberately had *not* turned a working pipeline into a skill yet, preferring to fully understand what he wants and surface the edge cases first. This is the same instinct as the reverse-engineering method above, held one step longer.
- **Most skills are too long.** He judges this true of skills and of `CLAUDE.md` files alike, which is insider confirmation of the "keep it human-reviewable" rule and the reason [[principles-over-constraints]] now exists as its own page.

## Synthesis

Skills are how tacit "how I work" knowledge becomes a durable capability, which is the concrete mechanism behind [[agentic-engineering]] and the reason an [[ai-operating-system]] gets better over time.
The reverse-engineering method pairs naturally with [[phased-autonomy]]: build the skill from a supervised success, then widen its autonomy as it proves out.
The fourth source pushes in the opposite direction from the wiki's earlier accumulate-more-detail instinct: a skill's quality is now better measured by what it leaves out than by what it specifies, since the model already knows most of what a long skill file is telling it.
The durable content is the workflow structure, the "use when" description, and the pass/fail checks; the prose around them is the part to cut.
