---
type: concept
tags: [evals, llm-as-judge, bias]
date: 2026-06-08
source-count: 3
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

Clémentine Fourrier, [[lets-talk-about-llm-evaluation]], frames model-as-judge as one of three eval methods (alongside benchmarks and human judges) and catalogs its limits:

- Two flavors: **generalist high-capability judges** (well-correlated with human preference, but usually closed-source, drift behind APIs, and uninterpretable) and **small specialist judges** trained on preference data (e.g. toxicity classifiers), which she suspects carry less subtle bias.
- Known biases: judges **favor their own outputs** (self-preference), are **bad at consistent score ranges** (mitigated by asking the model to explain its reasoning *before* giving a score), and correlate only weakly with human rankings.
- Caution: using LLMs to select and train LLMs can introduce minute, hard-to-interpret biases that compound over model generations.
- Contrast with **human judges** (vibes-checks, Elo arenas, paid systematic annotation), which reduce contamination but bring their own biases (sycophancy, assertiveness, cultural preference); see [[offline-vs-online-evals]] for the full method taxonomy.

Eugene Yan, [[patterns-for-building-llm-based-systems-and-products]], gives the operational playbook for the judge, including the three named biases this concept is about and how to mitigate each:

- Evidence that LLM judges align with humans: **G-Eval** (CoT + form-filling, Spearman 0.514), the **Vicuna** setup where GPT-4 single-answer grading agreed with humans 85% (above the 81% human-human agreement), and **QLoRA** (GPT-4 vs gpt-3.5-turbo, Spearman 0.55). LLM judgments are *less* noisy than humans but *more* biased - and because the bias is systematic, it can be corrected.
- **Position bias:** judges favor the first response. Mitigation: evaluate the pair twice with swapped order; only count a win if the same response wins both orders, else call it a tie.
- **Verbosity bias:** judges favor longer answers even when a shorter one is better. Mitigation: keep compared responses similar in length.
- **Self-enhancement bias:** judges favor their own outputs (GPT-4 +10% win rate, Claude-v1 +25%). Mitigation: don't judge a model with itself.
- Prefer giving the judge a **reference and asking for a comparison** over asking for a raw absolute score; it reduces noise (consistent with Fourrier's reason-before-score point above).

## In my own words (hcho)
