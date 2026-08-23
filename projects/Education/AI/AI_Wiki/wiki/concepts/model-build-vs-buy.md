---
type: concept
tags: [model-selection, production-llm, open-source, api, decision]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Model Build vs Buy (host open-source vs use an API)

From [[evaluate-ai-systems]] ([[chip-huyen]]): the recurring decision of whether to self-host an open-source (open-weight) model or call a commercial model API, which significantly narrows your candidate pool.

## The seven axes

- **Data privacy** - APIs mean sending data out (Samsung's ChatGPT leak); self-hosting keeps it in.
- **Data lineage / copyright** - commercial contracts can shield IP risk; fully-open models let you inspect training data.
- **Performance** - the strongest models stay proprietary; the gap to open is closing but persists.
- **Functionality** - APIs more often support scaling, function calling, structured outputs; self-hosting exposes logprobs and internals (useful for classification/eval/interpretability) and lets you finetune freely.
- **Cost** - API cost per token vs the engineering cost to host, optimize, and maintain.
- **Control / transparency** - APIs bring rate limits, silent model changes, and risk of losing access; open weights you can freeze and inspect.
- **On-device** - only self-hosting runs offline/on-device.

Also note license terms: commercial use, usage caps (Llama's 700M MAU clause), and whether outputs may train other models (distillation).

## Synthesis

This is a distinct axis from [[model-selection]] (which model's temperament fits the task) - build-vs-buy is which *family and host*, and it sits in the [[production-llm]] and [[system-design]] space as an [[engineering-trade-offs]] decision with no universal answer.
The recurring warning is the transparency one: a silently-updated commercial model can break your prompts with no notice, which is a reliability/validation concern (pin versions, keep an eval set to detect drift).
For hcho's product bets it is a concrete, interview-legible decision framework, and the "expose logprobs" point ties back to [[evaluation-pipeline]] (logprobs power confidence-based evaluation).
