---
type: concept
tags: [evals, llm-as-judge, bias]
date: 2026-06-06
source-count: 1
status: seeded
session: "S5 - LLM-as-judge: the workhorse method"
---

# LLM-as-Judge

Using an LLM to grade outputs against a rubric, including its position, verbosity, and self-enhancement biases and their mitigations.

## From the sources

Hamel Husain, [[your-ai-product-needs-evals]], treats the LLM judge as Level 2's "automated evaluation w/ LLMs":

- Do not eliminate human evaluation; keep humans in the loop and track model-human agreement over time.
- Align the judge by iterating on its critique prompt against human judgments (a spreadsheet of responses, model critiques, and human labels works).
- Use the most capable affordable model as the judge, and run a mini-eval on the judge itself.
- Do not use raw agreement on imbalanced data; report precision and recall separately.

## In my own words (hcho)
