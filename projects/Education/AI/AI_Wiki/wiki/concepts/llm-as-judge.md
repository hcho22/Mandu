---
type: concept
tags: [evals, llm-as-judge, model-based-eval, alignment]
status: established
source-count: 7
last-updated: 2026-09-15
---

# LLM-as-Judge

Using a language model to evaluate the outputs of another language model, the automated half of Level 2 in the [[three-level-eval-framework]] and one of the [[three-eval-methods]].
First filed from [[your-ai-product-needs-evals]] by [[hamel-husain]]; extended by [[ai-skill-from-scratch]], [[llm-patterns]], [[lets-talk-about-llm-evaluation]], and most completely by [[llm-evaluation-guidebook]].

## Key points

- **Do not replace human evaluation with it.** Track the correlation between the model judge and human labels, and use human critiques to iterate on the judge's prompt until they align.
- **Iterate the judge like a mini eval system.** Collect model responses, model critiques, and binary outcomes next to human judgments (a spreadsheet works), then refine the critique prompt to improve agreement.
- **Use the most capable affordable model** for critiquing, and monitor model-human agreement periodically.
- **Agreement caveat:** raw agreement is misleading on imbalanced datasets. Measure [[precision-recall|precision and recall]] separately instead (the same imbalance problem that makes PR curves beat [[roc-and-auc|AUC]]).
- **Prefer binary checks** when the model grades: it cannot reliably tell a 3/5 from a 4/5, so use [[pass-fail-over-score-evals|pass/fail over score-based]] evals.
- **Isolate the grader:** run the judge in a separate agent with a clean context window so grading is not biased by the generation context (see [[skill-eval-loop]]).

## Validated approaches and known biases ([[llm-patterns]])

- **It can work:** G-Eval (CoT + form-filling) reached 0.514 Spearman with humans; on the Vicuna benchmark, GPT-4's single-answer grading agreed with humans (85%) more than humans agreed with each other (81%). So a strong LLM as a reference-free judge is a viable, cheaper alternative to human eval.
- **Three biases to mitigate:**
  - *Position bias* - favors the first response; evaluate both orderings and only count a consistent winner.
  - *Verbosity bias* - favors longer answers; keep compared responses similar in length.
  - *Self-enhancement bias* - favors its own outputs (GPT-4 +10%, Claude-v1 +25% self-win rate); don't grade with the same model that generated.
- **Prefer comparison to direct scoring:** giving the judge a reference and asking for a comparison is less noisy than asking for an absolute score (reinforces [[pass-fail-over-score-evals]]).
- **The deeper worry ([[lets-talk-about-llm-evaluation]]):** model judges are bad at consistent score ranges (ask them to reason *before* scoring to help), only moderately agree with human rankings, and favor their own outputs. Fourrier's caution: using LLMs to select and train LLMs risks subtle, uninterpretable "crossbreeding" bias that compounds over generations - a reason to prefer small specialist classifiers where possible.

## The full bias catalog and mitigations ([[llm-evaluation-guidebook]])

Seven documented judge biases, each with a mitigation: no internal consistency (self-consistency prompting, majority vote), no consistent score ranges (use binary/pairwise), self-preference (use a jury), blindness to input perturbation (reason before scoring), position bias (swap orderings / use logprobs), verbosity bias (control for length), and format bias (match the judge's training prompt format).
Practical guidance: **pairwise comparison correlates with humans better than scoring**; use one prompt per capability; a **jury** of several (even small) judges beats one big model; and always **evaluate your evaluator** against a small (~50) representative baseline before trusting it. Judges are notably **bad at detecting hallucinations** (especially partial ones), so don't lean on them for [[factual-consistency]].
Related: **reward models** (Bradley-Terry pairwise or absolute-score) are fast, deterministic, position-bias-free, and prompt-free, but need fine-tuning; use win rates/probabilities, not raw averages.

## Judges after error analysis ([[ai-evals-error-analysis]])

Narrow, binary criteria are the judge's sweet spot.
Each bottom-up failure mode discovered by a human can become one focused judge, while a single prompt containing many criteria tends to wash out individual checks.
Fan out one judge per criterion, and score every judge against the labeled examples produced during annotation with precision and recall.
The judge scales the team's taste; it does not invent the product-specific taste that only comes from reading real outputs.

## Synthesis

The trap this concept guards against is trusting a judge that was never validated against humans.
The rigorous move, which is exactly hcho's validation instinct, is to treat the evaluator itself as a system under test: measure it with precision/recall, not raw agreement, and keep a human-labeled calibration set.
Later sources on judge design, rubric prompting, and bias should attach here.

## The same bias, arrived at from agent tooling ([[designing-loops-and-workflows]], 2026-07-28)

Self-enhancement bias is not only an eval-methodology finding.
An Anthropic [[claude-code]] team member ([[tharic]]) names it independently as **[[self-referential-bias]]** and treats it as a design constraint on agent architecture: "When a model prefers its own outputs, it's going to be more lenient at verifying it."
His prescription is the structural version of the mitigation this page already records, applied to workflows rather than benchmarks: split coordinating, doing, and verifying into three agents with different context and different models.

This is a notable convergence.
The measured finding here (GPT-4 about +10%, Claude-v1 about +25% self-win rate), the code-review finding in [[fresh-context-review]], and Anthropic's own tooling guidance all reach the same conclusion without citing one another, which raises confidence that "do not let the producer grade itself" is a property of the models rather than an artifact of any one evaluation setup.
The practical bridge is that the jury recommendation on this page and the separate-verifier-agent recommendation there are the same countermeasure at different scales.
