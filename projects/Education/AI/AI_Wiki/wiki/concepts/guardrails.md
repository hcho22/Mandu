---
type: concept
tags: [production-llm, guardrails, safety, validation, quality]
status: developing
source-count: 3
last-updated: 2026-09-15
---

# Guardrails

From [[llm-patterns]]: validating LLM input and output so it is not just plausible but syntactically correct, factual, safe, and non-adversarial.

## The kinds

- **Structural guidance** - steer the generation to a grammar/schema directly (Microsoft Guidance injects the structural tokens; token healing avoids tokenization bugs). More reliable than asking for JSON in the prompt.
- **Syntactic** - categorical output in an allowed set, numbers in range, generated SQL/Python parses and matches the schema.
- **Content safety** - block harmful/inappropriate output (word lists, profanity/moderation classifiers, or an LLM for nuance).
- **Semantic / factuality** - the output is relevant to and grounded in the input (cosine similarity, or an LLM checking consistency; SelfCheckGPT generates multiple completions and flags disagreement as likely hallucination).
- **Input guardrails** - refuse inappropriate/adversarial prompts before generating (a defense against [[red-team-your-agent|prompt injection]]).

## Safety and red-team evaluation

Guardrails need adversarial tests for prompt injection, jailbreaks, PII leakage, harmful advice, hate speech, violence, stereotypes, and bias.
For RAG and summarization, evaluate local factual consistency against the supplied context separately from global factual consistency against open knowledge.
Useful methods include specialized moderation classifiers, textual entailment, SelfCheckGPT-style consistency probes, search-augmented verification, and narrow LLM judges.
Model judges are weak at partial hallucinations, so safety and factuality should not depend on one judge alone.
Red-team findings should become stable regression cases, while critical failures block release.

## Synthesis

Guardrails are the output-validation face of the [[production-llm]] area and a direct extension of the wiki's verification family ([[adversarial-code-review]], [[skill-eval-loop]]): never ship an unvalidated model output that will take a consequential action.
They pair with structured outputs (schema enforcement) and with [[capabilities-not-instructions]] (least-access tools) - the two together are "make the boundary structural, not hoped-for."
For hcho this is squarely validation engineering: define the invariants the output must satisfy and enforce them mechanically, exactly the QA reflex applied to generation.
