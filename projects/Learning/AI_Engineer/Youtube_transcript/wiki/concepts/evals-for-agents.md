---
type: concept
tags: [evals, validation, adversarial-review, self-critique, quality]
date: 2026-07-03
source-count: 5
status: seeded
---

# Evals for Agents

Practical evaluation of agent output in the build loop: pass/fail checks against real examples, a rubric the agent iterates against, and adversarial review by a fresh or different model that reliably catches bugs the builder model missed.

## From the sources

[[building-an-ai-skill-from-scratch]] gives the sharpest formulation:

- An eval is asking the AI to check its own work; pass/fail checks beat score-based evals because the model cannot reliably tell a 3/5 from a 5/5 and will make it up.
- Put up to ~10 pass/fail checks in evals.md and run them in a separate agent with a clean context window so grading is not biased by the editing context; loop edits until all pass (the live demo converged after 5 loops).
- The evals themselves must be verified - a run exposed problems with the checks, not just the output.

[[agents-are-the-new-saas]] frames evals as the agent's "gym" and a sales asset:

- Take ~50 real examples of the job, mark the right answers, and score the agent (e.g., 42 correct / 6 flagged / 2 wrong); every prompt/model/tool change sends it back through the gym.
- The results build trust with buyers - transparency about what it got right, flagged, and missed is persuasive.

[[building-5-ai-products-solo]] uses cross-model adversarial review:

- Claude Opus builds, then GPT-5.5 runs an adversarial review of the worktree and "invariably finds 3-5 bugs Opus overlooked"; the but-for-real skill forces the builder model to re-review itself and finds 3-5 more, separate from the GPT pass.

[[building-products-with-coding-agents]] reviews in a fresh context window:

- No Mistakes reviews in a fresh context because reviewing in the same session biases the agent toward believing the work is correct; it splits obvious bugs (auto-fixed) from product-implication fixes (escalated) and attaches a low/medium/high risk score with test evidence.
- AGENTS.md testing instructions push agents past shallow unit tests into end-to-end validation, and recurring flows become Playwright E2E tests.

[[claude-managed-agents]] builds self-checking in as a primitive:

- An "outcome" passes Claude a file/blob that acts as a spec/rubric; Claude does a first pass then iterates and checks its own work against the rubric until it satisfies it, with console observability to debug the run.

## Synthesis

This is the concept that connects the video diet directly to hcho's positioning, and the builders' folk practices line up with the evals discipline the other two wikis formalize. Three techniques recur and each has a principled reason. **Pass/fail over scores**: a graded rubric is only as good as the grader's calibration, and an LLM grading its own 1-5 scale is uncalibrated, so binary checkable assertions are more reliable - the same reason production suites prefer hard checks (compare [[llm-as-judge]] and [[agent-eval-and-stats]] in the evals wiki). **Fresh / independent context**: a reviewer that saw every step of the work is biased toward believing it is correct, so isolation (a separate grading agent, a cross-family model, a "bully it into re-reviewing" pass) is what surfaces bugs - a debiasing argument, not a redundancy one. **A golden set of real examples**: the "50 real jobs" gym is exactly a golden set with marked answers, and re-running on every change is [[ci-eval-gates-and-drift]] applied to an agent. The agent-specific additions the videos contribute over classic evals are the **rubric-iteration loop** (CMA outcomes; the skill eval loop) where the agent self-corrects until it passes, and **risk-based attention** where validation output carries a severity so humans spend judgment where it matters. In a real RAG system this same machinery is [[retrieval-eval-suite]] plus [[security-correctness-eval]] in the Agentic RAG wiki. The through-line for interviews: agent quality is not vibes; it is a golden set, an independent grader, and a gate on every change - which is a decade of hardware validation rigor pointed at LLMs.
