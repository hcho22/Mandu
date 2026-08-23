---
type: concept
tags: [evals, hallucination, safety, red-team]
date: 2026-06-08
source-count: 3
status: seeded
session: "S8 - Hallucination, safety, red-teaming, guardrails"
---

# Hallucination, Safety, and Red-Teaming

Detecting hallucinations and running adversarial red-team probes (prompt injection, jailbreaks, PII leakage) plus guardrail design.

## From the sources

Eugene Yan, [[patterns-for-building-llm-based-systems-and-products]], frames guardrails as validating LLM output for correctness, safety, and adversarial input:

- **Guardrail taxonomy:** single-value checks (output is one of N choices, within a range, a complete sentence); **syntactic** (valid/reachable URLs, runnable SQL and code, schema-correct columns); **semantic/factuality** (output is similar to the source via cosine or fuzzy matching); **safety** (moderation classifiers, banned-word lists); and **input guardrails** that block adversarial or NSFW prompts before generation.
- **Hallucination detection by self-consistency:** SelfCheckGPT (used by NeMo-Guardrails) samples multiple completions for the same prompt; if they disagree with one another, the original is likely a hallucination. With a knowledge base, instead ask the LLM whether its answer is supported by the retrieved documents (fact-checking).
- **Two enforcement styles:** validate-after-generation (the Guardrails package, Pydantic-style, can filter or regenerate on failure) vs steer-during-generation (Microsoft Guidance injects structural tokens to guarantee valid syntax, e.g. always-valid JSON; token healing avoids tokenization bugs).
- Prompt-level safety: Anthropic's helpful/harmless/honest (HHH) prompting steers models away from harmful output; nuanced moderation needs an LLM evaluator since heuristics fall short.
- Input guardrails and jailbreak detection are the red-team-facing side: limit what input the model will respond to, mitigating prompt injection and harmful generations.

Chip Huyen, [[evaluate-ai-systems]], expands the factuality and safety measurement side:

- **Local factual consistency** evaluates output against provided context; **global factual consistency** evaluates output against open knowledge. Local checks are easier and matter for summarization, support bots, business analysis, and RAG.
- Hallucination evals should be built from observed failure slices. The chapter gives two common slices: niche knowledge and questions about nonexistent facts, such as asking what a person said about a topic they never discussed.
- Factuality methods include LLM judges, **SelfCheckGPT**-style self-verification, **SAFE** search-augmented verification, textual entailment/NLI, specialized factual-consistency scorers, and benchmarks such as **TruthfulQA**.
- Safety categories include inappropriate language, harmful recommendations or tutorials, hate speech, violence, stereotypes, and political or religious bias.
- Safety evaluation can use general-purpose judges, provider moderation tools, smaller specialized classifiers, and benchmarks such as **RealToxicityPrompts** and **BOLD**. Smaller classifiers may be cheaper and faster than general-purpose judges for narrow safety tasks.

Clémentine Fourrier, Thibaud Frere, Guilherme Penedo & Thomas Wolf, [[evaluation-guidebook]], add several safety- and hallucination-measurement points:

- **Non-compliance is its own axis:** **CoCoNot** tests whether models correctly *refuse* incomplete, unanswerable, or unsafe requests - framed as a classification problem, the complement of instruction following.
- **Model judges are weak hallucination detectors,** especially of *partial* hallucinations that look close to the ground truth; safety/factuality tasks should not lean on a judge alone (see [[llm-as-judge]]). **Calibration** (do correct answers get the highest probability?) is measurable via log-likelihood eval and is a useful honesty signal.
- **Games as safety probes:** deception games like **Town of Salem** / Werewolf test a model's deceptive vs honest behavior (e.g. Claude Opus 4 reportedly cannot win as a deceptive role but does fine as an honest one) - an adversarial, un-contaminable behavior eval.
- **Vibe-checks** (and Elo arenas) are a cheap way to surface safety edge cases by leveraging user creativity, but carry confirmation bias; **human evaluation itself has documented biases** (first-impression/formatting, assertive-wrong-over-neutral-correct tone bias, self-preference, identity-based toxicity-rating differences) that any safety eval relying on human labels must account for.

## In my own words (hcho)
