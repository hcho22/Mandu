# Evals Wiki Log

Event log for this wiki. Each entry begins with `## [YYYY-MM-DD] <op> | <title>` (op is `ingest`, `query`, `lint`, etc.) so entries are greppable and sort by date.

## [2026-08-26] edit | Added error-analysis concept page (S11)

- Created `concepts/error-analysis.md` (source-count 4; the read-your-data / build-a-rubric practice that fronts the eval workflow). Definition + `## From the sources`; `## In my own words (hcho)` left for hcho (mode: split).
- Cited four sources that substantively cover reading outputs and building a rubric: `[[ai-evals-error-analysis]]` (primary - top-down vs bottom-up, Error Discovery Skill, free labeled set), `[[your-ai-product-needs-evals]]` (Level 2 trace review + binary labels), `[[evaluate-ai-systems]]` (human-validated rubrics, annotate/slice, sampled daily review), `[[patterns-for-building-llm-based-systems-and-products]]` (human vibe check, Eval-Driven Development).
- Added bidirectional backlinks: `[[error-analysis]]` added to the `concepts:` frontmatter and `## Connections` of all four cited source pages.
- Updated `index.md` (added S11 to the Concepts list).
- Prompted by captain after the ingest below; folds the ingest's error-analysis material out of the four extended pages into a first-class concept.

## [2026-08-26] ingest | Automating AI Evals the Right Way - with Error Analysis

- Source already in `raw/ai-evals-error-analysis.md` (formatted notes on a YouTube podcast: Peter Yang interviewing Hamel Husain & Shreya Shankar, with a caption-correction appendix); used as-is, immutable.
- Created `sources/ai-evals-error-analysis.md` (summary, key claims, connections, provenance). No stable URL captured in the raw source.
- Practitioner/workflow source - extended four concept pages (each source-count +1):
  - `[[llm-as-judge]]` (5 to 6): narrow criteria as the judge sweet spot, each failure mode becoming a judge, one sub-agent per criterion (agent-era jury), evaluating judges with the free labeled set.
  - `[[production-eval-tooling]]` (3 to 4): the "do automated evals work?" benchmark (Braintrust Loop, Arize Alex, LangSmith, coding agents), bespoke agent-built review UIs vs generic eval SaaS.
  - `[[classification-metrics]]` (5 to 6): precision-not-just-recall for the eval tools themselves (~80-90% precision, 10-20% red herrings), benchmarking a rubric against its labels, yes/no over numeric scores.
  - `[[offline-vs-online-evals]]` (6 to 7): error analysis on real data as the durable first step, top-down vs bottom-up evals, evals as iterative and never "done."
- Updated `index.md` (added the source; bumped S1, S2, S5, S7 counts). No `(stub)` markers to drop (all four already seeded).
- Did not spread to S3 (data-leakage), S4 (contamination), S6 (rag), S9 (agent-eval), S10 (ci/drift), or S8 (safety) beyond cross-links: the source touches CI/drift and safety only via a one-line course-syllabus mention, so those stay as `[[links]]` from the four edited pages rather than thin standalone paragraphs.
- `## In my own words (hcho)` sections left for hcho on all four pages (mode: split); `synthesis.md` untouched.

## [2026-06-15] ingest | The LLM Evaluation Guidebook

- Source re-clipped into `raw/Evaluation Guidebook - a Hugging Face Space by OpenEvals.md` (full 1,555-line guidebook text; the prior clip captured only the iframe shell and was never ingested). Used as-is, immutable.
- Created `sources/evaluation-guidebook.md` (summary, key claims, connections, provenance). Author: Clémentine Fourrier, Thibaud Frere, Guilherme Penedo, Thomas Wolf (Hugging Face / OpenEvals, Dec 2025).
- Foundational survey - extended all ten concept pages (each source-count +1):
  - `[[llm-benchmarks-contamination]]` (4 to 5): 2025 benchmark tour by capability, saturation vs contamination, integrated assistant tasks, Nov-2025 recommendation set.
  - `[[llm-as-judge]]` (4 to 5): judge definition/uses, getting a judge, the seven biases + mitigations, evaluating your evaluator, reward models.
  - `[[classification-metrics]]` (4 to 5): automatic match metrics (exact/BLEU/ROUGE/TER/BLEURT), aggregation, accuracy normalization, sampling metrics, functional scorers.
  - `[[offline-vs-online-evals]]` (5 to 6): builder vs user perspectives, log-likelihood vs generative methods, MCF/CF/FG formulations.
  - `[[data-leakage-and-splits]]` (2 to 3): contamination management - canary/gating/procedural generation, overfitting vs generalization.
  - `[[agent-eval-and-stats]]` (2 to 3): tool-calling/agent benchmarks (TauBench, BFCL, MCP-Universe) and statistical validity (confidence intervals, bootstrapping).
  - `[[ci-eval-gates-and-drift]]` (4 to 5): ablations/checkpoint evals and the FineWeb benchmark-selection criteria (monotonicity, SNR, non-random, Kendall's tau).
  - `[[production-eval-tooling]]` (2 to 3): standard harnesses + reproducibility factors, structured generation, annotation tooling, cost/efficiency reporting.
  - `[[rag-evaluation]]` (2 to 3): long-context benchmark lineage (NIAH, RULER, HELMET) and the closed-book to open-book shift.
  - `[[hallucination-safety-redteam]]` (2 to 3): non-compliance (CoCoNot), judges as weak hallucination detectors, calibration, games as safety probes, human-eval biases.
- Updated `index.md` (added the source; bumped all ten concept counts).
- `## In my own words (hcho)` sections left for hcho on all ten concept pages (mode: split). No daily-log pointer added because `log/2026-06-15.md` does not exist.

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
