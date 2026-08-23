---
type: concept
tags: [evals, metrics, nlp]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Reference-Based Metrics (and their limits)

From [[llm-patterns]]: the classical automatic metrics that score generated text against gold references - useful, cheap, and often misleading for open-ended LLM tasks.

## The metrics

- **BLEU** - precision-based n-gram overlap (with a brevity penalty); machine translation.
- **ROUGE** - recall-based n-gram overlap; summarization (ROUGE-N/L/S variants).
- **BERTScore** - embedding cosine similarity, so it handles synonyms/paraphrase that BLEU/ROUGE miss.
- **MoverScore** - like BERTScore but soft (many-to-one) alignment via earth-mover distance.

## The three pitfalls

1. **Poor correlation with human judgment** - BLEU/ROUGE correlate weakly (sometimes negatively) with fluency, and poorly on creative/diverse tasks.
2. **Poor adaptability** - exact-match metrics make no sense for dialogue or abstractive summarization, where a good answer can share zero n-grams with the reference.
3. **Poor reproducibility** - high variance across studies; a survey of 2,000 ROUGE studies found scores hard to reproduce and often computed with incorrect implementations.

## Synthesis

This is the "why generic metrics mislead" concept that motivates the whole [[evals]] area's push toward task-specific evals ([[eval-driven-development]]) and, for open-ended tasks, [[llm-as-judge]].
It layers cleanly on [[ml-metrics]]: for classification-shaped LLM tasks, standard precision/recall still apply; the trouble is only with matching-based metrics on generative tasks.
For hcho the lesson is a validation staple - a convenient metric that doesn't correlate with what you care about is worse than none, because it manufactures false confidence.
