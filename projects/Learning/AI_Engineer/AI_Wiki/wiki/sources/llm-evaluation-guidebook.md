---
type: source
title: "The LLM Evaluation Guidebook (OpenEvals / Hugging Face)"
source-type: guidebook
author: "Clémentine Fourrier, Thibaud Frere, Guilherme Penedo, Thomas Wolf (Hugging Face)"
url: "https://huggingface.co/spaces/OpenEvals/evaluation-guidebook"
date-ingested: 2026-07-08
date-created: 2025-12-03
tags: [evals, benchmarks, contamination, saturation, llm-as-judge, reproducibility, functional-testing]
---

# The LLM Evaluation Guidebook (OpenEvals / Hugging Face)

The exhaustive HuggingFace/OpenEvals guidebook by [[clementine-fourrier]] et al. ([[huggingface]]), distilling lessons from scoring 15,000 models over 3 years.
It runs from why we evaluate (builder vs user), through LLM basics (tokenization, inference), the 2025 benchmark landscape, why you can't reproduce reported scores, and how to create and score your own evaluation.

## Key claims

- **Two lifecycle threats:** [[data-contamination]] (eval data leaked into training inflates scores) and [[benchmark-saturation]] (all models near the ceiling, so the benchmark loses discriminative power). Both mean a benchmark "stops being useful as soon as it becomes public."
- **Two eval mechanics:** log-likelihood evaluations (compare choice probabilities; task formulations MCF/CF/FG) vs generative evaluations (score the generated text). Most API models force generative because they hide logprobs.
- **Perspectives:** model builders need fast, high-signal, cheap benchmarks for ablations (with monotonicity, low noise/high SNR, non-random performance, and stable model ordering - the FineWeb selection method); model users need benchmarks matching their use case. Rankings are more stable than scores.
- **[[score-reproducibility]]:** you usually can't reproduce a reported score - different code base, random seeds, metric definitions (exact vs prefix vs quasi match), normalization, prompt format (7-point swings on semantically-equivalent prompts), few-shot count/order, hardware, inference library, batch size, and precision all move results.
- **Scoring free-form text** is the core challenge: match-based metrics (exact match, BLEU, ROUGE, TER, BLEURT) for ground-truth tasks; sampling metrics (pass@k, maj@n, cot@n, avg@n); and [[functional-scorers]] (rule-based verifiers, IFEval-style) which are unambiguous, cheap, contamination-resistant, and the guidebook's recommended default.
- **The three methods, fully treated** ([[three-eval-methods]]): automated benchmarks; humans (vibe-checks, arenas, systematic annotation) with biases (first-impression, tone/assertiveness, self-preference, identity); and [[llm-as-judge|judge models]] with seven biases (no internal consistency, no consistent score ranges, self-preference, blindness to perturbation, position, verbosity, format) and their mitigations. Judges are bad at detecting hallucinations - a warning for [[factual-consistency]].
- **Creating your own eval:** reuse/aggregate existing data (watch redundancy/balance), human annotation (guideline design dominates - GAIA), or synthetic (rule-based procedural generation to avoid contamination; model-generated with verification). Always look at your data.
- **Evaluate your evaluator:** pick a baseline (50 representative, discriminative, high-quality examples suffice), a metric (easier if binary/pairwise), and an acceptance threshold; pairwise correlates with humans better than scoring; a jury of judges beats one.
- **Forgotten children:** report confidence intervals (bootstrapping), and cost/efficiency/environmental footprint (tokens, time) alongside scores.

## Connections

- [[benchmark-saturation]], [[functional-scorers]], [[score-reproducibility]] - concepts introduced here.
- [[data-contamination]] (3rd source; procedural generation to avoid it), [[three-eval-methods]] (fullest treatment), [[llm-as-judge]] (the definitive bias catalog + mitigations, jury, evaluate-your-evaluator, reward models), [[factual-consistency]] (judges are weak at hallucination detection), [[evaluation-pipeline]] (create-your-own-eval + sampling + statistical validity), [[benchmark-sensitivity]] (prompt-format swings), [[pass-fail-over-score-evals]] (pairwise > scoring).
- [[looking-at-your-data]] - "always look at your data, don't prompt an LLM to find unusual stuff for you."
- Cross-wiki: the deepest benchmarking-side reference; hcho's own synthesis lives in the evals-pilot wiki.

## Source

- **Authors:** Clémentine Fourrier, Thibaud Frere, Guilherme Penedo, Thomas Wolf (Hugging Face / OpenEvals)
- **Title:** The LLM Evaluation Guidebook · **Published:** 2025-12-03
- **URL:** https://huggingface.co/spaces/OpenEvals/evaluation-guidebook
- **Note:** the most complete single reference on the benchmarking/leaderboard side of evals; a large 2025 benchmark catalog (mostly reference material, not summarized here).
- **Raw:** [[Evaluation Guidebook - a Hugging Face Space by OpenEvals]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
