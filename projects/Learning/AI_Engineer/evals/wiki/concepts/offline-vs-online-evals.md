---
type: concept
tags: [evals, offline-evals, online-evals, fundamentals]
date: 2026-06-06
source-count: 1
status: seeded
session: "S1 - What evals are and why they matter"
---

# Offline vs Online Evals

The distinction between evaluating a model on a fixed dataset before deploy (offline) versus on live traffic after deploy (online), plus human-in-the-loop grading.

## From the sources

Hamel Husain, [[your-ai-product-needs-evals]], frames evals as a three-level progression that spans the offline-to-online boundary:

- **Level 1 (offline):** fast, cheap unit-test assertions run in CI on every change.
- **Level 2 (offline and sampled):** human and model-graded review of logged traces; align the LLM judge to human labels.
- **Level 3 (online):** A/B testing on live traffic, deferred until product-market fit is clearer.

The takeaway for this concept: offline evals (Levels 1-2) are where iteration speed comes from, and online evaluation (Level 3) is a later-stage validation, not the starting point.

## In my own words (hcho)
