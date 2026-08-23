---
type: source
title: "Building an AI Skill from Scratch: 5 Steps + Advanced Tips"
source-type: tutorial-summary
author: "Peter (Behind the Craft)"
url: "https://behindthecraft.com"
date-ingested: 2026-07-08
date-created: unknown
tags: [skills, claude-code, evals, llm-as-judge, ai-slop, agentic-engineering]
---

# Building an AI Skill from Scratch: 5 Steps

A summarized ~19-minute tutorial in which the presenter builds an "edit-post" skill live in [[claude-code]] and shares a five-step method for skills that check and improve their own output.
It is a hands-on deepening of [[building-skills]], and its center of gravity is an eval loop: the skill grades itself and iterates until it passes.

## The five steps

1. **Create** the skill from your best examples and personal context; keep `SKILL.md` separate from the example files (so the AI loads only the relevant example per run, and you can share the generic skill without exposing personal data). Provide at least a couple of examples or the AI overfits.
2. **Trigger:** the AI reads only a skill's name and description to decide whether to load it, so the description must be an explicit "Use when XYZ."
3. **Evals:** test manually, then have it write `evals.md` with up to ~10 pass/fail checks; run the evals in a **separate agent with a clean context window** so grading is not biased by the editing context, and loop the edit agent until all checks pass. See [[skill-eval-loop]].
4. **Memory:** add `memory.md` (concise, 2-3 sentences per lesson, non-overlapping with evals) so the skill improves from past conversations; best for vague, taste-level feedback that cannot be a pass/fail check.
5. **Skill editor:** build or copy a skill that audits your skills - removing [[ai-slop]], tightening wording, enforcing progressive disclosure.

## Key claims

- **Pass/fail checks beat score-based evals** ([[pass-fail-over-score-evals]]): the model cannot reliably tell a 3/5 from a 4/5 and will make it up; binary checks are more reliable.
- The self-grading loop is "where the magic is": in the live demo, 3 of 10 checks failed on run 1 and all passed by run 5 (removing em dashes and "this is X, not Y" slop).
- **You must also validate the evals themselves** - the run exposed problems with the checks, not just the output.
- The **eval loop improves each run's output; `memory.md` improves the skill itself.**
- Skills only get output ~80-90% of the way; the final 10-20% is human review and [[taste-as-moat|taste]]. Every skill needs human eyes.

## Connections

- [[building-skills]] - this is the detailed method behind that concept (second source; adds the file anatomy SKILL.md / examples / evals.md / memory.md).
- [[skill-eval-loop]] - the self-checking loop is the source's core contribution.
- [[evals]] / [[llm-as-judge]] - a concrete, agent-based application of self-evaluation; sharpens the pass/fail-vs-score point and the "separate grader context" trick.
- [[ai-slop]] - the quality failure mode the skill editor removes; ties to [[taste-as-moat]].
- [[agentic-engineering]] - "agentic validations" made concrete.

## Source

- **Author:** Peter (Behind the Craft newsletter; paid skill library at behindthecraft.com)
- **Title:** Building an AI Skill from Scratch: 5 Steps + Advanced Tips
- **URL:** https://behindthecraft.com (YouTube tutorial)
- **Tools cited:** Claude Code (or Codex), Wispr Flow (dictation).
- **Raw:** [[AI_Skill_Tutorial_Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
