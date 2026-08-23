---
type: concept
tags: [evals, testing, ci, assertions]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# LLM Unit Tests

Level 1 of the [[three-level-eval-framework]]: cheap, fast assertions over LLM behavior that run on every code change, the way ordinary unit tests do.
Introduced in [[your-ai-product-needs-evals]] by [[hamel-husain]].

## Key points

- **Scope tests per feature and scenario.** Break the LLM's functionality into features, then enumerate scenarios and their assertions (e.g. for a listing finder: exactly-one-match implies `len(listing_array) == 1`, no-match implies `== 0`).
- **Generic assertions apply broadly.** For example, a regex assertion that a UUID never appears in a response when the prompt forbids it.
- **Generate test cases with LLMs.** Prompt a model for dozens of realistic user instructions to produce synthetic cases; you do not need to wait for production data.
- **Run in existing CI** (GitHub Actions, GitLab Pipelines) with minimal friction, and track pass rates over time in an analytics tool (e.g. Metabase). Not every test needs a 100% pass rate; tolerance depends on the feature.
- **Update continuously** as new failure modes appear in production.

## Synthesis

This is the highest-leverage, lowest-cost eval layer and the natural entry point for someone with a QA background: it turns fuzzy "the model got worse" regressions into a deterministic CI signal.
It also sets up the higher levels, since the same synthetic-generation and assertion machinery feeds [[llm-as-judge]] and fine-tuning data curation.
