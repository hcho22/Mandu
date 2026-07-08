---
type: entity
tags: [org, platform, evals, open-source, leaderboards]
status: seed
source-count: 3
last-updated: 2026-07-08
---

# Hugging Face

The open-source AI platform (models, datasets, Spaces) and home of widely-used evaluation infrastructure: the Open LLM Leaderboard, the MTEB embedding leaderboard, and the OpenEvals evaluation work.

## What shows up in the wiki

- [[llm-patterns]] - the MTEB leaderboard (embedding-model ranking) and the analysis showing MMLU scores differ across implementations ([[benchmark-sensitivity]]) both come from HF.
- [[lets-talk-about-llm-evaluation]] - [[clementine-fourrier]]'s team runs HF's evaluation + leaderboards; source of the [[three-eval-methods]] / [[purposes-of-evaluation]] framing.
- [[llm-evaluation-guidebook]] - HF/OpenEvals' exhaustive guidebook (Fourrier, Frere, Penedo, Thomas Wolf - HF co-founder), distilling 3 years / 15,000 models scored; also home of `lighteval`, the FineWeb benchmark-selection method, and the `outlines` structured-generation work referenced there.

## Notes

HF is the institutional hub for the "rigorous benchmarking" side of [[evals]], as distinct from the product-eval practitioners ([[hamel-husain]], [[eugene-yan]]).
