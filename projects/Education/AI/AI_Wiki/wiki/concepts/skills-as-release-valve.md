---
type: concept
tags: [agentic-engineering, skills, agents-md, claude-md, budget, context-engineering, method]
status: developing
source-count: 2
last-updated: 2026-09-16
---

# Skills as the Release Valve

The budget-triage rule from [[agents-md-is-a-neural-net]] ([[kun]]): once you put an explicit token budget on the always-loaded memory file, updates near that budget are **zero-sum** - every addition has to name the removal or extraction that pays for it.
Skills are the release valve that makes this survivable, because they hold knowledge that would otherwise blow the budget while keeping it out of the always-loaded context.

## The triage

For each candidate unit of instruction, decide by breadth and trigger:

- **Broad** (matters in roughly 20% or more of sessions, or is safety-critical) -> **stays in the memory file.** It is loaded every session because it is relevant every session.
- **Narrow but with a detectable trigger** -> **becomes a [[building-skills|skill]].** It loads only when its "use when" condition fires, so it costs nothing on the sessions it does not apply to.
- **Narrow with no detectable trigger** -> **deletion candidate.** If it is rarely relevant and nothing reliably signals when, it cannot earn its always-loaded cost and cannot be cleanly extracted, so it goes.

## Why the budget makes skills load-bearing

Without a budget, every rule looks free, so everything is appended and the file drifts into [[four-bad-memory-states|bloat]].
With a budget, the memory file and the skill library become two halves of one system: the file carries the broad steering, and the skills carry the long tail of narrow, triggerable capability.
This is the concrete mechanism behind the wiki's existing advice to keep memory files short - [[principles-over-constraints]] says most `CLAUDE.md` files are too long, and this rule says *where the trimmed content goes* rather than only that it should be trimmed.

## Workflow reconstruction (2026-09-16)

[[kun-agentic-app-development-workflow]] places conditional skills beside a small shared onboarding file and reproducible configuration across harnesses.
This reinforces progressive loading without supplying a new numeric budget or a fresh evaluation of the memory-training claims.

## Synthesis

This is the operational bridge the wiki was missing between [[building-skills]] (skills as capability) and [[principles-over-constraints]] (memory files are too long).
It reframes a skill not just as "a reusable recipe" but as **the budget-management primitive for the always-loaded context**: the thing you extract to when a unit is worth keeping but not worth loading every time.
It also sharpens [[skills-vs-plugins]] - the skill is the atom you extract to, the plugin is how you share a bundle of them - and it gives [[self-updating-config]] its exit valve, since a backward pass that can only add or delete would eventually starve, but one that can also *extract to a skill* stays inside budget indefinitely.
For hcho it turns "trim Mandu's CLAUDE.md" into a decision procedure: broad and safety-critical stays, narrow-with-a-trigger moves to a skill (Mandu already has `ingest`, `daily-log`, `prd`, `job-hunter`), and narrow-without-a-trigger is a delete.
