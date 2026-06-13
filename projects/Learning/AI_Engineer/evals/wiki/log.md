# Evals Wiki Log

Event log for this wiki. Each entry begins with `## [YYYY-MM-DD] <op> | <title>` (op is `ingest`, `query`, `lint`, etc.) so entries are greppable and sort by date.

## [2026-06-10] ingest | What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide

- Source already in `raw/What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide.md` (clipped markdown copy of https://llm-stats.com/blog/research/what-is-a-contaminated-llm, immutable); used as-is.
- Created `sources/what-is-a-contaminated-llm-detection-famous-cases-2026-guide.md` (summary, key claims, connections, provenance).
- Extended `[[llm-benchmarks-contamination]]` (source-count 3 to 4): direct/indirect/latent contamination, detection methods, famous cases, dose-response effects, and contamination-resistant benchmark design.
- Extended `[[data-leakage-and-splits]]` (source-count 1 to 2): cutoff splits, membership inference, Time Travel, ConStat, canaries, and private/rotating holdout discipline.
- Extended `[[offline-vs-online-evals]]` (source-count 4 to 5): public offline benchmarks as bounded signals and private/application-specific evals as the product-selection path.
- Extended `[[production-eval-tooling]]` (source-count 1 to 2): benchmark provenance, private holdouts, rotating evals, and contamination checks as pipeline/tooling concerns.
- Extended `[[ci-eval-gates-and-drift]]` (source-count 3 to 4): stale public benchmarks as weak gates, with fresh/private/versioned eval sets as stronger regression signal.
- Updated `index.md` (added the source; bumped five concept counts).
- `## In my own words (hcho)` sections left for hcho on all concept pages (mode: split). No daily-log pointer added because `log/2026-06-10.md` does not exist.

## [2026-06-09] ingest | Evaluate AI Systems

- Source already in `raw/Evaluate AI Systems.md` (raw chapter markdown, immutable); used as-is.
- Created `sources/evaluate-ai-systems.md` (summary, key claims, connections, provenance).
- Seeded `[[data-leakage-and-splits]]` (source-count 0 to 1, stub to seeded): benchmark contamination as leakage, n-gram/perplexity checks, clean-sample reporting, slicing, and bootstrap checks.
- Seeded `[[production-eval-tooling]]` (source-count 0 to 1, stub to seeded): component/turn/task evals, guidelines, rubrics, annotated data, slices, sampled human review, and experiment tracking.
- Extended `[[offline-vs-online-evals]]`, `[[classification-metrics]]`, `[[llm-benchmarks-contamination]]`, `[[llm-as-judge]]`, `[[rag-evaluation]]`, `[[hallucination-safety-redteam]]`, `[[agent-eval-and-stats]]`, and `[[ci-eval-gates-and-drift]]`.
- Updated `index.md` (added the source; bumped all ten concept counts; dropped `(stub)` on S3 and S7).
- `## In my own words (hcho)` sections left for hcho on all concept pages (mode: split). No daily-log pointer added because `log/2026-06-09.md` does not exist.

## [2026-06-06] ingest | Your AI Product Needs Evals

- Saved `raw/your-ai-product-needs-evals.md` (clipped markdown copy of https://hamel.dev/blog/posts/evals/, immutable).
- Created `sources/your-ai-product-needs-evals.md` (summary, key claims, connections, provenance).
- Extended concepts `[[offline-vs-online-evals]]` and `[[llm-as-judge]]` (each source-count 0 to 1, status stub to seeded); `## In my own words (hcho)` sections left for hcho.
- Updated `index.md` (added the source; dropped `(stub)` on the two concepts).

## [2026-06-08] ingest | Let's talk about LLM evaluation

- Source already in `raw/Let's talk about LLM evaluation.md` (clipped markdown copy of https://huggingface.co/blog/clefourrier/llm-evaluation, immutable); used as-is.
- Created `sources/lets-talk-about-llm-evaluation.md` (summary, key claims, connections, provenance).
- Seeded `[[llm-benchmarks-contamination]]` (source-count 0 to 1, stub to seeded): benchmark anatomy, generalization/overfitting, multiple-choice order bias, contamination + canary/gating/dynamic benchmarks.
- Extended `[[llm-as-judge]]` (1 to 2): model-as-judge flavors and biases (self-preference, inconsistent score ranges, reason-before-score, weak human-ranking correlation).
- Extended `[[offline-vs-online-evals]]` (1 to 2): the three eval methods and the three distinct purposes (non-regression, leaderboards, capability claims).
- Seeded `[[ci-eval-gates-and-drift]]` (0 to 1, stub to seeded): non-regression testing via trajectories and ranges, high signal-to-noise benchmarks.
- Seeded `[[agent-eval-and-stats]]` (0 to 1, stub to seeded): score instability vs ranking stability, perturbation experiments, wisdom-of-crowds aggregation.
- Updated `index.md` (added the source; bumped five concept counts; dropped `(stub)` on three concepts).
- `## In my own words (hcho)` sections left for hcho on all five concept pages (mode: split).

## [2026-06-08] ingest | Patterns for Building LLM-based Systems & Products

- Source already in `raw/Patterns for Building LLM-based Systems & Products.md` (clipped markdown copy of https://eugeneyan.com/writing/llm-patterns/, immutable); used as-is.
- Created `sources/patterns-for-building-llm-based-systems-and-products.md` (summary, key claims, connections, provenance).
- Seeded `[[classification-metrics]]` (0 to 1, stub to seeded): classification metrics for classification-like tasks, classical reference-based generation metrics (BLEU/ROUGE/BERTScore/MoverScore) and their three pitfalls.
- Seeded `[[rag-evaluation]]` (0 to 1, stub to seeded): retrieval precision driving end-to-end accuracy, MTEB embedding eval, ANN index eval factors, reference-based vs reference-free split.
- Seeded `[[hallucination-safety-redteam]]` (0 to 1, stub to seeded): guardrail taxonomy, SelfCheckGPT self-consistency hallucination detection, input guardrails, validate-vs-steer enforcement.
- Extended `[[llm-as-judge]]` (2 to 3): the three named biases (position, verbosity, self-enhancement) and mitigations, plus G-Eval/Vicuna/QLoRA human-alignment evidence.
- Extended `[[llm-benchmarks-contamination]]` (1 to 2): benchmark families (MMLU, HELM, EleutherAI harness, AlpacaEval) and implementation sensitivity (same model, different scores).
- Extended `[[offline-vs-online-evals]]` (2 to 3): Eval-Driven Development and task-specific evals; user feedback and monitoring as the online signal.
- Extended `[[ci-eval-gates-and-drift]]` (1 to 2): evals to detect regressions at scale, the data flywheel, production monitoring (12x-losses A/B anecdote).
- Updated `index.md` (added the source; bumped seven concept counts; dropped `(stub)` on three more concepts - S2, S6, S8).
- `## In my own words (hcho)` sections left for hcho on all seven concept pages (mode: split). Did not spread to S3 (data-leakage-and-splits) or S7 (production-eval-tooling), which the source does not substantively cover.

## [2026-06-08] ingest | Classification: Accuracy, recall, precision, and related metrics

- Source already in `raw/Classification Accuracy, recall, precision, and related metrics    Machine Learning.md` (clipped markdown copy of the Google ML Crash Course classification page, immutable); used as-is.
- Created `sources/classification-accuracy-precision-recall.md` (summary, key claims, connections, provenance).
- Extended `[[classification-metrics]]` (source-count 1 to 2): single-threshold confusion-matrix metrics (accuracy, recall/TPR, FPR, precision, F1), the precision-recall tradeoff, class-imbalance failure of accuracy, and cost-driven metric choice.
- Updated `index.md` (added the source; bumped S2 to 2 sources).
- Scoped to S2 only (foundational ML metrics); `## In my own words (hcho)` left for hcho (mode: split).

## [2026-06-08] ingest | Classification: ROC and AUC

- Source already in `raw/Classification ROC and AUC    Machine Learning.md` (clipped markdown copy of the Google ML Crash Course ROC/AUC page, immutable); used as-is.
- Created `sources/classification-roc-and-auc.md` (summary, key claims, connections, provenance).
- Extended `[[classification-metrics]]` (source-count 2 to 3): threshold-independent evaluation - the ROC curve (TPR vs FPR), AUC as a ranking probability, PR-AUC for imbalanced data, and threshold/model selection.
- Updated `index.md` (added the source; bumped S2 to 3 sources).
- Scoped to S2 only; sequel to the accuracy/precision/recall page; `## In my own words (hcho)` left for hcho (mode: split).
