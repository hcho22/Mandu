---
type: concept
tags: [claude-code, skills, agentic-engineering, workflow]
status: established
source-count: 6
last-updated: 2026-08-27
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

## Reverse-engineering, shrunk to a single artifact ([[one-person-marketing-team]], 2026-08-21)

The fifth source adds nothing to the theory and sharpens the trigger, which is the part people get wrong.

**Build the skill the moment you like an output, not before.**
Its instruction is literally that: when a deliverable comes back the way you wanted it, say *"I loved carousel 2, let's make a skill around that one so I can do that style again."*
The negative form is used the same way: *"I don't like carousel 3, never make them like that again."*

That is the reverse-engineering method above, applied to **one artifact rather than one workflow**, and it lowers the bar for when packaging is worth it.
The existing method waits for a completed end-to-end task; this waits only for a single result you would want repeated.
It also sits neatly between the page's two existing poles - the forward method's "design it from your cadence" and [[tharic]]'s "understand it fully before you package" - because a liked output is concrete evidence of what good looks like without requiring you to have articulated it.

Two smaller additions:

- **Skills are for intake, not only for generation.** The source's most-used skill is `grill me`, whose entire job is to interview the human ([[agent-interviews-you-for-context]]). Discovery is a repeatable workflow and deserves the same treatment as a production recipe.
- **A liked output plus a negative example is a cheap rubric.** "Like carousel 2, never carousel 3" is the raw material for a [[skill-eval-loop]] pass/fail check, captured at the moment the judgment is fresh.

## Skills as the memory-budget release valve ([[agents-md-is-a-neural-net]], 2026-08-27)

The sixth source gives skills a job the earlier five did not name: they are **the release valve on the always-loaded memory file's budget** ([[skills-as-release-valve]]).
[[kun]]'s triage decides what becomes a skill by breadth and trigger - broad or safety-critical instructions stay in `AGENTS.md`, **narrow instructions with a detectable trigger become a skill**, and narrow ones with no trigger are deletion candidates.
That is the same "use when XYZ" description this page already treats as a skill's core, now load-bearing for a different reason: the trigger is what lets the content leave the always-loaded context without being lost.
So a skill is not only a reusable recipe, it is where you *extract to* when a unit is worth keeping but not worth paying for on every session - the mechanism that keeps a trained memory file inside budget indefinitely.

## Synthesis

Skills are how tacit "how I work" knowledge becomes a durable capability, which is the concrete mechanism behind [[agentic-engineering]] and the reason an [[ai-operating-system]] gets better over time.
The reverse-engineering method pairs naturally with [[phased-autonomy]]: build the skill from a supervised success, then widen its autonomy as it proves out.
The fourth source pushes in the opposite direction from the wiki's earlier accumulate-more-detail instinct: a skill's quality is now better measured by what it leaves out than by what it specifies, since the model already knows most of what a long skill file is telling it.
The durable content is the workflow structure, the "use when" description, and the pass/fail checks; the prose around them is the part to cut.
