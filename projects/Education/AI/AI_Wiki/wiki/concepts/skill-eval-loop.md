---
type: concept
tags: [evals, skills, llm-as-judge, agents, self-improvement]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Skill Eval Loop

A pattern from [[ai-skill-from-scratch]] in which a skill grades its own output against a checklist and iterates until it passes, so the AI improves the work while you step away.

## The architecture

1. The **edit (or work) agent** produces output.
2. A **separate grading agent, with a clean context window,** runs the checks in `evals.md` - separation matters so grading is not biased by the work context.
3. **Failures are sent back** to the work agent, which keeps going.
4. Repeat until all checks pass. (Live demo: 3/10 failing on run 1, all passing by run 5.)

## Key points

- Use up to ~10 **pass/fail** checks (see [[pass-fail-over-score-evals]]), grouped by category (intro, voice, substance, tone, CTA).
- **Validate the evals themselves,** not just the output - a bad check silently passes bad work.
- The loop improves each run; a separate `memory.md` improves the skill over time.

## Also a platform primitive

Anthropic's Claude Managed Agents ship this as [[outcome-rubric-iteration]] ("Outcomes"): attach a rubric and the agent loops against it until it passes - the same pattern as a first-class API (see [[production-agent-with-cma]]).

## Synthesis

This is [[evals]] and [[llm-as-judge]] operationalized inside a skill: a self-checking loop that turns "the model usually gets it 80% right" into "the model iterates to passing while you get coffee."
The clean-context separation of grader from worker is a specific case of [[fresh-context-review]], and the same rigor as validating a judge against ground truth - a directly reusable pattern for hcho's own skills and for agent QA.
It is the mechanism that makes [[building-skills]] produce reliable, not just plausible, capabilities.
