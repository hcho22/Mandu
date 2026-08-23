---
type: concept
tags: [evals, traces, data-inspection, principle]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Looking At Your Data

The principle that you must remove all friction from the process of inspecting your model's actual inputs and outputs.
Stated bluntly by [[hamel-husain]] in [[your-ai-product-needs-evals]]: "You must remove all friction from the process of looking at data," and "you can never stop looking at data - no free lunch exists."

## Key points

- **Render traces in a domain-specific way.** A trace groups the events of one interaction (user messages, LLM responses, tool calls); build a custom viewer that shows the feature/scenario, whether input is synthetic or real, filters, and links back to source systems.
- **Cheap to build.** Lightweight frameworks (Gradio, Streamlit, Shiny) produce such a viewer in under a day.
- **Start binary.** Use good/bad labels before granular rating scales.
- **How much to look:** examine every trace early; sample more as volume grows; stop sampling a slice only when you stop learning from it.

## Synthesis

This is the connective tissue of the whole eval discipline: [[llm-unit-tests]] and [[llm-as-judge]] are only as good as the failure modes you have actually seen by reading outputs.
At runtime this generalizes to [[agent-observability]] - inspecting an agent's live events, tool calls, and traces is the same discipline applied to execution rather than outputs.
It is also the clearest place hcho's hardware-validation background transfers directly, since disciplined data inspection is the same habit that finds hardware defects.
Treat "build the trace viewer early" as a default recommendation whenever a new source discusses eval or debugging workflows.
