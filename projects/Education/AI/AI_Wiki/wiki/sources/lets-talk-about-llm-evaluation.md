---
type: source
title: "Let's talk about LLM evaluation"
source-type: blog
author: "Clémentine Fourrier (Hugging Face)"
url: "https://huggingface.co/blog/clefourrier/llm-evaluation"
date-ingested: 2026-07-08
date-created: 2024-05-23
tags: [evals, benchmarks, contamination, leaderboards, human-eval, llm-as-judge]
---

# Let's talk about LLM evaluation

Clémentine Fourrier ([[clementine-fourrier]]), who leads evaluation and leaderboards at [[huggingface]], distills how and why LLM evaluation is done.
Two organizing frames: three *methods* of evaluation ([[three-eval-methods]]) and three distinct *purposes* it serves ([[purposes-of-evaluation]]), which are usually conflated but answer different questions.

## Key claims

### The three methods ([[three-eval-methods]])
- **Automated benchmarks:** samples (+ optional gold reference) and a metric; test on data *not* in training so you measure generalization, not memorization. Good for well-defined tasks; capabilities ("good at math?") can only be measured by a proxy task (GSM8K), so both success and failure are hard to interpret. Prone to multi-choice order bias and unfair normalization, and to [[data-contamination]].
- **Human as judge:** vibes-checks (anecdotal, confirmation-bias-prone), arenas (LMSYS Elo, "wisdom of the crowd" but culturally biased), and systematic annotations (ScaleAI-style; expensive, still biased). Key finding: humans judge on first impressions and tone - they **underestimate errors in confident/assertive answers** and prefer answers that align with their own views (sycophancy). Any factuality task needs a more robust check than crowdsourced humans.
- **Model as judge:** generalist strong models or small specialist classifiers; correlates with human preference but has self-preference bias, inconsistent score ranges (improved by reasoning-before-scoring), and imperfect agreement with human rankings. Fourrier's worry: using LLMs to select/train LLMs risks subtle "crossbreeding" bias compounding over generations.

### The three purposes ([[purposes-of-evaluation]])
1. **Non-regression testing** - is my training method sound? Care about score *trajectories* and *ranges*, not exact numbers (a 7B should hit ~50-65 on MMLU; 20-30 means no learning).
2. **Leaderboards / rankings** - which model is best? Scores are unstable to minute prompting changes, so *rankings* over robust evaluation groups are the trustworthy signal - though even Open LLM Leaderboard and Chatbot Arena rankings aren't fully stable to perturbation.
3. **Capability measurement** - "can my model do X?" We can't actually do this: we lack a definition of "capability," so we can only say "best on this task we *hope* proxies the capability, without guarantee."

### Contamination ([[data-contamination]])
- Public benchmarks leak into training sets (often accidentally); a contaminated model scores high without generalizing. Mitigations: canary strings, encrypted/gated benchmarks, and dynamic benchmarks (refreshed data), though the last is costly. Closed black-box APIs give no guarantee your eval data won't be trained on.

## Connections

- [[three-eval-methods]], [[purposes-of-evaluation]], [[data-contamination]] - concepts introduced here.
- [[evals]] area - this source gives it its organizing taxonomy and purpose framing.
- [[benchmark-sensitivity]] - directly reinforced (scores unstable, rankings more stable); the contamination bridge to [[what-is-a-contaminated-llm]] (coming).
- [[llm-as-judge]] - extended (self-preference, inconsistent scores, reasoning-before-score).
- [[pass-fail-over-score-evals]] - "ask the model to reason before scoring" is the same fix for score noise.
- [[looking-at-your-data]] / [[eval-driven-development]] - the practitioner comment agrees: nothing beats testing on your own use case with your own metrics.
- Cross-wiki: this taxonomy underlies hcho's own eval synthesis in the evals-pilot wiki; cross-link, don't duplicate.

## Source

- **Author:** Clémentine Fourrier, evaluation + leaderboards lead at Hugging Face
- **Title:** Let's talk about LLM evaluation · **Published:** 2024-05-23
- **URL:** https://huggingface.co/blog/clefourrier/llm-evaluation
- **Raw:** [[Let's talk about LLM evaluation]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
