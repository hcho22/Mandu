---
type: concept
tags: [evals, functional-testing, verifiers, unit-tests, quality]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Functional Scorers (rule-based verifiers)

From [[llm-evaluation-guidebook]]: instead of comparing generated text to a reference by fuzzy string matching, functional testing checks whether the output satisfies specific verifiable constraints - the guidebook's recommended default.

## Key points

- **IFEval / IFBench** are the canonical example: "include exactly 3 bullet points," "use the word X twice," "output valid JSON with keys A and B" - each checkable by a specific rule-based verifier, so a free-form generative task gets a strict score with no model judge.
- Advantages: unambiguous, interpretable, fast, cheap, and easy to regenerate to resist contamination.
- Directly inspired by code evaluation (unit tests / functional correctness): does the output do the right thing, not does it look like the reference.
- Caveat: modern LLMs can "cheat" too-easy unit tests (e.g. overwriting globals in Python) - design tests defensively.

## Synthesis

Functional scoring is the guidebook's north star ("prefer interpretable functional testing over model judges"), and it is the eval family most native to hcho: it *is* validation/QA - assert the invariants the output must satisfy and check them mechanically.
It is the rigorous end of the same spectrum as [[pass-fail-over-score-evals]] and the eval-time twin of [[guardrails]] (a guardrail is a functional check at serving time).
Where it applies, it dominates [[llm-as-judge]] on cost, reproducibility, and interpretability - so the craft is extending the functional-testing surface (finding the programmatically-verifiable aspects of a task) rather than defaulting to a judge.
