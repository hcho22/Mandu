---
type: concept
tags: [evals, llm-as-judge, bias]
date: 2026-06-08
source-count: 5
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

Chip Huyen, [[evaluate-ai-systems]], shows how broadly LLM judges appear inside application evaluation:

- For factual consistency, a judge can compare a generated answer against source context and decide whether the answer is supported. Prior work cited in the chapter found GPT-3.5 and GPT-4 stronger than previous factual-consistency methods.
- Factuality pipelines can combine judges with structure: **self-verification** samples multiple model outputs and checks agreement; **SAFE** decomposes long-form answers into self-contained claims, searches for evidence, and uses AI to decide whether each claim is supported.
- Textual entailment/NLI can be treated as a specialized judge: given a premise and a hypothesis, classify the relation as entailment, contradiction, or neutral. Entailment implies local factual consistency; contradiction implies inconsistency.
- Judges also appear in safety, instruction following, and roleplaying evals. INFOBench converts broad instruction-following requirements into yes/no criteria; RoleLLM uses a judge prompt to compare role style and role-specific knowledge.
- Judge reliability must be evaluated as part of the evaluation pipeline: use clear rubrics and examples, check whether better responses get higher scores, set judge temperature to 0 for reproducibility, and measure whether judge metrics correlate with human or business outcomes.

Clémentine Fourrier, Thibaud Frere, Guilherme Penedo & Thomas Wolf, [[evaluation-guidebook]], give the most complete judge treatment in the wiki so far:

- **Definition and three uses:** a judge model is a neural net used to evaluate another model's output - for *scoring* a generation on a scale, *pairwise* comparison of two outputs, or *similarity* to a reference. Judges shine on nuanced properties (fluency, faithfulness, coherence) that exact-match cannot capture.
- **Where to get one:** a generalist high-capability LLM (easy, but closed judges are non-reproducible black boxes with privacy risk; open models like DeepSeek-R1/Qwen are closing the gap), a *tiny specialist* judge (Prometheus 13B, JudgeLM, Flow-Judge - run locally, need their prompt format), or train/fine-tune your own from preference data (avoid unless niche; starting from a reward model beats an instruct model).
- **Seven catalogued biases + mitigations:** no internal consistency (self-consistency prompting), inconsistent score ranges, self-preference (use a jury), blindness to input perturbation (reason-before-score), position bias (swap order / normalize logprobs), verbosity bias (length-correct), and format bias (match the training prompt format).
- **Design rules:** pairwise comparison correlates with human preference better than absolute scoring; if scoring, use an integer scale with per-point descriptions or an additive rubric; emit reasoning *before* the score; one prompt per capability; a **jury** of several smaller judges beats one big judge.
- **Evaluate your evaluator** before trusting it: pick a small (~50) representative + discriminative + high-quality baseline, pick a metric (accuracy/precision/recall are easy for binary or pairwise; score-correlation is hard), and set a threshold (80-95% pairwise accuracy, ~0.8 Pearson). Judges are notably **bad at detecting hallucinations**, especially partial ones, and correlate only weakly on summarization/faithfulness (see [[hallucination-safety-redteam]]).
- **Reward models** as an alternative judge: Bradley-Terry pairwise models output sigmoid(score_b - score_a); they are fast, deterministic, position-bias-resistant, and need no prompt engineering, but require fine-tuning. For relative-score RMs use **win rates / win probabilities** against a reference rather than averaging raw rewards; tracking win-rate over training can flag degradation and select checkpoints (see [[ci-eval-gates-and-drift]]).

## In my own words (hcho)
