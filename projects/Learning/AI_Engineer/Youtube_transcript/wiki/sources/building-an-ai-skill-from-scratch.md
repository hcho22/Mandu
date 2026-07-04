---
type: source
tags: [skills, evals, memory, claude-code, prompting]
date: 2026-07-03
title: "Building an AI Skill from Scratch: 5 Steps + Advanced Tips"
author: "Behind the Craft (behindthecraft.com)"
url: ""
concepts: [agent-skills, evals-for-agents, agent-memory, human-taste-and-ai-slop]
---

# Building an AI Skill from Scratch: 5 Steps + Advanced Tips

A ~19-minute tutorial that builds an "edit-post" skill live in Claude Code and lays out a five-step method for skills that check and improve their own output.
It treats a skill as a folder of instructions (SKILL.md plus examples, evals.md, memory.md) and emphasizes the eval loop and the human taste needed for the last 10-20%.

## Key claims

- A skill is a folder of instructions the AI can trigger for a task; create it from your best examples plus personal context, and aim for roughly a one-page SKILL.md.
- Keep SKILL.md separate from examples/personal context so the AI does not re-read every example each run (it detects the type and loads only the relevant file) and so the generic skill is shareable. Provide at least a couple of examples or the AI overfits to one.
- Triggering depends on the description: the AI reads only a skill's name and description to decide whether to load the full skill, so the description must say explicitly "Use when XYZ."
- An eval is asking the AI to check its own work. Pass/fail checks beat score-based evals (the model cannot reliably tell a 3/5 from a 5/5 and will make it up).
- Put up to ~10 pass/fail checks in evals.md, and run the evals in a separate agent with a clean context window so grading is not biased by the editing context; loop edits until all checks pass. Live demo converged after 5 loops.
- memory.md improves the skill itself (a concise, reverse-chronological log of lessons), while the eval loop improves each run's output. Keep memory to 2-3 sentences per entry and non-overlapping with evals; use it for vague, taste-level feedback.
- Build a "skill editor" skill that audits all your skills for AI slop and bloat and enforces progressive disclosure, because AI-written skill text accumulates slop if unattended.
- Skills only get output ~80-90% of the way; the final 10-20% is human review and taste. Every skill needs human eyes.

## Connections

- [[agent-skills]] - the canonical 5-step anatomy of a skill (SKILL.md, description/triggering, examples, evals.md, memory.md, skill editor).
- [[evals-for-agents]] - pass/fail over score-based evals, running evals in a separate clean-context grader, and looping until all pass.
- [[agent-memory]] - memory.md as a concise, non-overlapping lessons log that improves the skill over time.
- [[human-taste-and-ai-slop]] - the 80-90% ceiling, the final-10-20% human pass, and the skill editor that strips AI slop.

## Source

- **Author / channel:** Behind the Craft (behindthecraft.com; presenter as heard)
- **Title:** Building an AI Skill from Scratch: 5 Steps + Advanced Tips
- **URL:** not recorded (saved transcript summary; backfill when available)
- **Raw:** `raw/AI_Skill_Tutorial_Summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-07-03
