---
type: concept
tags: [production-llm, fine-tuning, lora, training]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Fine-Tuning

From [[llm-patterns]]: refining a pre-trained model on a task-specific dataset to improve performance, control, and independence from third-party APIs.

## The kinds (the term is used loosely)

- **Continued pre-training** - same pre-training objective on domain data.
- **Instruction fine-tuning** - teach a base model to follow instructions (InstructGPT).
- **Single-task fine-tuning** - hone for one narrow task (classification, summarization).
- **RLHF** - instruction tuning plus a reward model trained on human preferences (PPO).

## Efficient techniques and trade-offs

- **LoRA / QLoRA** are the practical starting points: adapters as low-rank matrices (LoRA) and a 4-bit quantized base (QLoRA) cut memory from ~780GB to ~48GB for a 65B model with comparable quality.
- Also soft-prompt tuning, prefix tuning, adapters - all update a tiny fraction of parameters.
- **The alignment tax:** fine-tuning on one task can regress others (InstructGPT lost ground on SQuAD, HellaSwag). A workaround is many small specialized models.
- Needs significant demonstration data (InstructGPT: 13k SFT samples), and some provider ToS forbid using outputs to train competing models.

## Synthesis

The load-bearing judgment is **when**, not how: reach for fine-tuning last, after prompting and [[retrieval-augmented-generation|retrieval]] genuinely can't hit the quality bar - the same ladder [[zero-to-hireable-ai-engineer]] and [[single-call-workflow-or-agent]] prescribe (least-powerful tool first).
It sits in the [[production-llm]] area as the highest-effort, highest-control lever, and it depends entirely on [[evals]] to know whether it actually helped and whether the alignment tax bit.
For hcho this is mostly a "know when not to" concept: most product problems are solved before fine-tuning, and reaching for it early is a common, expensive mistake.
