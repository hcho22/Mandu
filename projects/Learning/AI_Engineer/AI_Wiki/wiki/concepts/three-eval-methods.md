---
type: concept
tags: [evals, benchmarks, human-eval, llm-as-judge, taxonomy]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# The Three Evaluation Methods

From [[lets-talk-about-llm-evaluation]] ([[clementine-fourrier]]) and the fuller [[llm-evaluation-guidebook]]: there are three ways to evaluate an LLM, each with its own reason for existing and its own limits.

## The three

- **Automated benchmarks** - samples (+ optional gold reference) scored by a metric. Best for well-defined tasks; must test on data outside training to measure generalization, not memorization. Weaknesses: capabilities can only be measured by a proxy task (so success/failure is hard to interpret), sensitivity to answer order and normalization, and [[data-contamination]].
- **Human as judge** - vibes-checks (anecdotal, confirmation-biased), arenas (LMSYS Elo; wisdom-of-crowd but culturally biased), systematic annotations (rigorous but expensive). Critical bias: humans judge on tone and first impressions - they **miss errors in confident answers** and prefer views that match their own (sycophancy). So factuality tasks need more than crowdsourced humans.
- **Model as judge** - a strong generalist or a small specialist classifier; correlates with human preference but carries self-preference bias, inconsistent scoring, and only moderate agreement with humans (see [[llm-as-judge]]).

## Synthesis

This is the organizing taxonomy for the whole [[evals]] area: every eval technique in the wiki is one of these three, and each fails differently, so serious evaluation combines them rather than trusting one.
The through-line is that **no single method is unbiased** - benchmarks leak, humans are swayed by tone, models favor themselves - which is why [[eval-driven-development]] (your own task-specific set) and triangulation matter.
For hcho the human-judge sycophancy finding is a sharp, interview-ready point: a confident wrong answer is the hardest failure to catch, and catching it is exactly a validation job.
