---
type: concept
tags: [evals, agents, rubric, self-improvement, anthropic]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Outcome / Rubric Iteration

A Claude Managed Agents capability, from [[production-agent-with-cma]]: pass Claude a file or blob that acts as a spec/rubric, and it does a first-pass implementation, then iterates and checks its own work against the rubric repeatedly until it satisfies it.

## Key points

- The rubric is supplied as an "outcome" attached to a session; the agent enters a mode that loops against it and emits an outcome evaluation when it concludes.
- Session events signal when the agent enters this rubric-iteration mode, so it is observable.
- Described as a very powerful way to set agents up for success.

## Synthesis

This is Anthropic's first-class version of the [[skill-eval-loop]]: rubric plus loop-until-pass, now a platform primitive rather than a hand-built skill.
It sits in the same verification family as [[fresh-context-review]] and [[pass-fail-over-score-evals]] - the recurring lesson that AI output should be checked against explicit criteria until it passes.
For hcho, the durable point is that "spec/rubric + self-check loop" is becoming standard infrastructure, so fluency in writing good rubrics (a validation skill) is exactly the leverage.
