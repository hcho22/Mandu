---
type: concept
tags: [evals, hallucination, factuality, rag, nli]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# Factual Consistency (hallucination detection)

From [[evaluate-ai-systems]] ([[chip-huyen]]) and [[llm-evaluation-guidebook]]: the criterion many application developers most want, measuring whether an output's claims are actually supported.

## Two settings

- **Local factual consistency** - output evaluated against a provided context (summary vs source, chatbot vs policy). Much easier to verify, and the central metric for [[rag|RAG]].
- **Global factual consistency** - output evaluated against open knowledge; requires first deciding what the facts are (the hard part), amid internet misinformation and the absence-of-evidence fallacy.

## Detection methods

- **AI judge** - prompt a strong model to check consistency (GPT-3.5/4 outperform prior methods).
- **Self-verification** - SelfCheckGPT: generate N responses; disagreement among them signals hallucination (effective but expensive).
- **Knowledge-augmented** - SAFE: decompose the output into statements, make each self-contained, search, and verify each.
- **Textual entailment / NLI** - classify (premise, hypothesis) as entailment / contradiction / neutral; a specialized scorer (e.g. DeBERTa-NLI) turns factual consistency into a cheap classification task.
- Benchmark: TruthfulQA (817 questions humans get wrong from misconceptions).

## Synthesis

Factual consistency is the highest-stakes member of [[evaluation-criteria]] and the metric that makes [[retrieval-is-the-bottleneck|grounded RAG]] trustworthy - the local setting is exactly "did the answer stay faithful to the retrieved context?"
Framing it as NLI/classification connects it straight to [[ml-metrics]] ([[precision-recall]]) and to the [[guardrails]] pattern (a semantic/factuality guardrail is a factual-consistency check at serving time).
For hcho this is the sharp end of his edge: hallucination detection is a measurable validation problem, and it is the core eval his Agentic RAG harness must own.
Important caveat ([[llm-evaluation-guidebook]]): **LLM judges are bad at detecting hallucinations**, especially partial ones that look close to the truth - so lean on NLI/specialized scorers and [[functional-scorers|functional]] grounding checks rather than a generalist [[llm-as-judge]] for this specific criterion.
