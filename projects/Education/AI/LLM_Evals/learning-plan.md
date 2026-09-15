# A 20-Hour Learning Plan for AI Eval/QA (2026 Edition)

> This file is the curriculum for the parked LLM_Evals learning track.
> Canonical source summaries and reusable concepts live in the [AI_Wiki evals area](../AI_Wiki/wiki/areas/evals.md).
> Exercises belong in `Exercise/`; study history belongs in `log/`.

## TL;DR
- **The fastest path to competence in AI eval/QA is to master ~10 high-leverage concepts** (the offline/online split, golden datasets, classification metrics with class imbalance, LLM-as-judge with its biases, RAG metrics, regression testing, drift, agent trajectory eval, statistical noise, and red-teaming) and to practice each in a real tool — **Promptfoo + DeepEval + RAGAS + Arize Phoenix or LangSmith** cover the vast majority of production needs.
- **The single most-cited modern playbook is Hamel Husain's "Your AI Product Needs Evals" plus his Maven course with Shreya Shankar**; pair it with Chip Huyen's *AI Engineering* (2025) Chapters 3–4 for foundation, and Clémentine Fourrier's Hugging Face Evaluation Guidebook for benchmark theory. These three sources alone deliver the Pareto-80%.
- **Skip what's saturated**: don't spend hours on MMLU/HellaSwag/GSM8K methodology — those benchmarks are largely contaminated and retired for frontier work. Spend that time instead on error analysis, LLM-judge alignment, and CI/CD eval gates, which is where production teams actually differentiate.

---

## SECTION 1 — 20-Hour Learning Plan (10 × 2-hour sessions)

Each session has: Learning Objectives, Resources (with links), Hands-On Exercise, and a 15-minute end-of-session Review Activity.

### Session 1 (Hours 0–2): What evals are and why they matter
**Objectives:** Define evals; distinguish offline vs online vs human-in-the-loop; understand why "vibe checks" fail at scale; map the eval flywheel.
**Resources:**
- Hamel Husain, *Your AI Product Needs Evals* — https://hamel.dev/blog/posts/evals/ (read fully)
- Eugene Yan, *Patterns for Building LLM-based Systems & Products* — https://eugeneyan.com/writing/llm-patterns/ (read the "Evals" section)
- Clémentine Fourrier, *Let's Talk About LLM Evaluation* — https://huggingface.co/blog/clefourrier/llm-evaluation
**Hands-on:** Take an LLM app you've used (ChatGPT, Claude, a chatbot at work). Write 10 inputs, run them, and label each output good/bad. Write a 2-sentence rationale for each label. This is your first eval set.
**15-min Review:** Re-explain the Level 1 / Level 2 / Level 3 evals framework from Hamel's post out loud (assertions → model-graded → human). Identify which level your 10 labels belong to.

### Session 2 (Hours 2–4): Classical ML metric foundations (still essential)
**Objectives:** Master the confusion matrix; compute accuracy, precision, recall, F1, ROC-AUC, PR-AUC; understand when each fails (esp. class imbalance); review MAE/RMSE/R² for regression.
**Resources:**
- Google ML Crash Course — *Classification: Accuracy, Precision, Recall* — https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
- Google ML Crash Course — *ROC and AUC* (same site)
- scikit-learn docs — `sklearn.metrics` page
**Hands-on:** In a Jupyter notebook, take an imbalanced dataset (e.g., credit-card fraud from Kaggle) and train a logistic regression. Compute accuracy, precision, recall, F1, and plot the PR curve. Find the threshold that maximizes F1.
**15-min Review:** Without looking, write the formulas for precision, recall, F1, and explain in one sentence why F1 is a harmonic mean and not arithmetic.

### Session 3 (Hours 4–6): Data splits, leakage, baselines, cross-validation
**Objectives:** Understand train/val/test discipline; spot data leakage; build baseline models; use k-fold CV; understand contamination/benchmark leakage in LLMs.
**Resources:**
- Chip Huyen, *Designing Machine Learning Systems* (Ch. 4, "Training Data") OR *AI Engineering* (Ch. 4 "Evaluate AI Systems")
- LLM-stats.com, *What Is a Contaminated LLM?* — https://llm-stats.com/blog/research/what-is-a-contaminated-llm
- scikit-learn docs — Cross-validation user guide
**Hands-on:** Build a stratified k-fold CV pipeline on the dataset from Session 2. Then deliberately introduce leakage (compute target-mean encoding before the split) and watch test scores inflate. Fix it.
**15-min Review:** Draw the data-splits diagram from memory (train/val/test + nested CV), and write down two real ways LLM benchmarks have been contaminated (e.g., GSM8K leakage in Mistral/Phi via ConStat detection; Codeforces score cliff after GPT-4 training cutoff).

### Session 4 (Hours 6–8): LLM benchmarks — what they measure and what they don't
**Objectives:** Know the major benchmark families (MMLU, HellaSwag, ARC, GSM8K, MATH, GPQA-Diamond, HumanEval/SWE-bench, BIG-bench, HELM, Humanity's Last Exam, MT-Bench, Chatbot Arena/LMArena) and their saturation/contamination status.
**Resources:**
- Hugging Face Evaluation Guidebook — https://github.com/huggingface/evaluation-guidebook (current home: huggingface.co/spaces/OpenEvals/evaluation-guidebook)
- EvidentlyAI's *30 LLM Evaluation Benchmarks* — https://www.evidentlyai.com/llm-guide/llm-benchmarks
- LMArena leaderboard — https://lmarena.ai/ (browse current top models)
**Hands-on:** Install `lm-evaluation-harness` (github.com/EleutherAI/lm-evaluation-harness) and run a small open model (e.g., Qwen-1.5B) on 2 tasks: `arc_easy` and `gsm8k`. Compare to published scores.
**15-min Review:** For each of MMLU, HellaSwag, GSM8K, MT-Bench, Chatbot Arena, write one sentence: what it measures, and whether it's still useful in 2026.

### Session 5 (Hours 8–10): LLM-as-judge — the workhorse method
**Objectives:** Set up an LLM-judge; understand and mitigate position, verbosity, and self-enhancement bias; align a judge to human labels; know when to use pairwise vs single-score grading.
**Resources:**
- Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, NeurIPS 2023 — https://arxiv.org/abs/2306.05685 (read §3 on biases)
- Hamel Husain, *Creating a LLM-as-a-Judge that Drives Business Results* — https://hamel.dev/blog/posts/llm-judge/
- Eugene Yan, *Evaluating the Effectiveness of LLM-Evaluators* — https://eugeneyan.com/writing/llm-evaluators/
**Hands-on:** Take the 10 labels from Session 1. Write an LLM-judge prompt with a 3-point rubric (pass/borderline/fail) and run it via OpenAI or Anthropic API. Compute agreement (Cohen's kappa) with your human labels. Swap the order of the two compared answers and check for position bias.
**15-min Review:** Recite the three main LLM-judge biases (position, verbosity, self-enhancement) and one mitigation for each.

### Session 6 (Hours 10–12): RAG evaluation
**Objectives:** Decompose a RAG system into retrieval + generation; measure context precision, context recall, faithfulness/groundedness, answer relevance; understand when to use reference-based vs reference-free metrics.
**Resources:**
- RAGAS documentation — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
- Jason Liu, *There Are Only 6 RAG Evals* — https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/
- TruLens documentation (RAG triad page)
**Hands-on:** Build a tiny RAG over 20 PDFs of your choice using LlamaIndex or LangChain. Generate 15 Q-A-Context triples. Use RAGAS to score `faithfulness`, `context_precision`, `context_recall`, and `answer_relevancy`. Identify your single weakest metric.
**15-min Review:** Draw the Q–C–A triangle from Jason Liu's framework and label the six conditional relationships (A|C, A|Q, C|Q, C|A, Q|A, Q|C) with what each measures.

### Session 7 (Hours 12–14): Production tooling — Promptfoo, DeepEval, Phoenix
**Objectives:** Run a YAML-driven eval suite in CI; integrate model-graded metrics into pytest; trace and inspect failures in an observability tool.
**Resources:**
- Promptfoo docs — https://www.promptfoo.dev/docs/intro/ (run `npx promptfoo@latest init`)
- DeepEval docs — https://deepeval.com/ (or docs.confident-ai.com)
- Arize Phoenix docs — https://arize.com/docs/phoenix
**Hands-on:** (a) Write a `promptfooconfig.yaml` with 5 prompts and 10 test cases comparing GPT-4o-mini vs Claude Haiku. (b) Wrap one of the test cases in a DeepEval `pytest` test using the `HallucinationMetric`. (c) Instrument a small LangChain app with Phoenix's OpenInference tracer and view spans in the UI.
**15-min Review:** List in one paragraph which tool you'd reach for in three scenarios: (1) solo dev pre-commit eval; (2) RAG pipeline retrieval diagnosis; (3) production debugging of a single bad user trace.

### Session 8 (Hours 14–16): Hallucination, safety, red-teaming, guardrails
**Objectives:** Detect hallucinations via NLI / SelfCheckGPT; check toxicity and bias; run adversarial/red-team probes for prompt injection, jailbreaks, PII leakage; design guardrails.
**Resources:**
- DeepLearning.AI short course, *Red Teaming LLM Applications* — https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/
- Eugene Yan, *Task-Specific LLM Evals That Do & Don't Work* — https://eugeneyan.com/writing/evals/ (NLI for factuality section)
- Promptfoo Red Team docs — https://www.promptfoo.dev/docs/red-team/
**Hands-on:** Run `promptfoo redteam` against your YAML config from Session 7. Inspect the report for prompt injection and PII categories. Then add an input guardrail (regex or moderation classifier) and re-run.
**15-min Review:** Write down the top 5 OWASP LLM Top 10 risks (prompt injection, insecure output handling, training data poisoning, model DoS, supply-chain) and one eval probe for each.

### Session 9 (Hours 16–18): Agent evaluation + statistical rigor
**Objectives:** Evaluate multi-step agents (task completion, tool-call correctness, trajectory order); compute confidence intervals on eval scores; reason about sample size and noise.
**Resources:**
- Yao et al., *τ-bench: A Benchmark for Tool-Agent-User Interaction* — https://arxiv.org/abs/2406.12045
- UK AISI's Inspect framework — https://inspect.aisi.org.uk/
- Chip Huyen, *AI Engineering* (2025), Ch. 4 § on "Comparative Evaluation" and statistical reliability
**Hands-on:** Install `inspect-ai` (`pip install inspect-ai`). Run one of the 200+ pre-built evals (e.g., a small math task) on two models. Compute bootstrap 95% confidence intervals on the score difference. Decide whether the difference is statistically significant.
**15-min Review:** Explain in one paragraph: if Model A scores 78% and Model B scores 80% on 100 examples, what is the rough 95% CI for each, and can you declare B better?

### Session 10 (Hours 18–20): CI/CD evals, drift monitoring, putting it all together
**Objectives:** Build a GitHub Actions workflow that runs evals on every PR; set up production drift detection; design an eval golden dataset and a regression policy; sketch a flywheel.
**Resources:**
- DeepLearning.AI short course, *Automated Testing for LLMOps* — https://www.deeplearning.ai/short-courses/automated-testing-llmops/
- Evidently AI, *Data Drift* and *Concept Drift* — https://www.evidentlyai.com/ml-in-production/data-drift
- Hamel Husain & Shreya Shankar, *LLM Evals: Everything You Need to Know* (FAQ) — https://hamel.dev/blog/posts/evals-faq/
**Hands-on:** Add a `.github/workflows/evals.yml` that runs your Promptfoo suite on every PR, fails the build if pass rate drops by >5 percentage points vs main, and posts a comment with the diff. Optional: wire a simple PSI-based drift check into a daily cron job over logged production inputs.
**15-min Review:** Capstone — sketch on one page your end-to-end eval architecture for a hypothetical customer-support RAG bot: golden set creation, offline judge, CI gate, online observability, drift monitor, red-team schedule. Identify the single weakest link.

---

## SECTION 2 — One-Page Cheat Sheet (5-minute review)

### Core Definitions
- **Eval** = a repeatable measurement of model/system output quality against a defined criterion.
- **Offline eval** = run on a fixed dataset before deploy (golden set, CI).
- **Online eval** = run on live traffic post-deploy (A/B, shadow, guardrails, observability).
- **Human-in-the-loop** = expert annotators grade samples and align judges.

### The Eval Flywheel (Hamel's framework)
```
[ Logs / Traces ] → [ Error Analysis / Labeling ]
        ↑                       ↓
[ Ship to Prod ]   ←   [ Eval & Curation ]   ←   [ Synthetic Data ]
        ↑                       ↓
[ CI / Regression ]  ←  [ Fix: prompt, RAG, model ]
```

### Classical Metrics (formulas)
- **Accuracy** = (TP+TN)/(TP+TN+FP+FN)
- **Precision** = TP/(TP+FP) — "of what I flagged, how much was right"
- **Recall** = TP/(TP+FN) — "of what was actually positive, how much did I catch"
- **F1** = 2·P·R/(P+R) — harmonic mean
- **ROC-AUC** = ranking quality across thresholds (use when balanced)
- **PR-AUC** = use when **class-imbalanced** (rare positives)
- **MAE / RMSE / R²** for regression. RMSE punishes large errors; R² is variance explained.

### LLM/GenAI Metrics
- **Reference-based:** BLEU, ROUGE, METEOR, BERTScore (mostly weak signals for open-ended)
- **Reference-free / model-graded:** G-Eval, LLM-as-judge (single-score or pairwise)
- **RAG triad:** Faithfulness (A vs C) • Answer Relevance (A vs Q) • Context Precision/Recall (C vs Q)
- **Agent:** Task success, tool-call F1, trajectory edit distance, pass^k

### LLM-as-Judge — Three biases to mitigate
1. **Position bias** → randomize order or run both orders, declare tie if inconsistent
2. **Verbosity bias** → cap response length in prompt; include "ignore length" instruction
3. **Self-enhancement bias** → use a different family of model as judge

### Conceptual Diagrams (described for rendering)

**Diagram A — Confusion Matrix (2×2 grid):**
| | Pred Positive | Pred Negative |
|---|---|---|
| Actual Positive | TP (green) | FN (red) |
| Actual Negative | FP (red) | TN (green) |
Annotate margins: Precision = column-1 ratio; Recall = row-1 ratio.

**Diagram B — RAG Triad (triangle):**
Three nodes: Question (Q, top), Context (C, bottom-left), Answer (A, bottom-right).
- Edge Q↔C: Context Precision/Recall (retrieval quality)
- Edge C↔A: Faithfulness/Groundedness (no hallucination)
- Edge Q↔A: Answer Relevance (on-topic)

**Diagram C — Eval Pyramid (3 levels, like the test pyramid):**
- Base (broad/cheap): **Level 1 assertions** — regex, JSON-schema, exact-match (run on every commit)
- Middle: **Level 2 model-graded** — LLM-as-judge rubric (run nightly/on PRs)
- Top (narrow/expensive): **Level 3 human review** — domain experts (run weekly + after major changes)

### Concrete Examples
- **Class imbalance trap:** Fraud detection where 0.1% of txns are fraud. A model predicting "never fraud" hits 99.9% accuracy. Use PR-AUC + recall@fixed-precision.
- **Hallucination test:** Ask a RAG bot a question whose answer is *not* in the corpus. A faithful system says "I don't know"; a hallucinator confabulates. Score with an NLI model: premise=retrieved context, hypothesis=answer.
- **Position-bias check:** Ask judge: "Which is better, A or B?" If A wins 90% in order (A,B) but only 40% in (B,A), the judge is biased toward position 1.

### Red Flags in 2026
- Reporting only **MMLU/HellaSwag/GSM8K** for a frontier model → likely contaminated (all four — MMLU, HumanEval, HellaSwag, original GSM8K — are documented as effectively retired for frontier ranking, per the LLM-Stats contamination analysis).
- Reporting a single accuracy number with **no confidence interval** → noise may dominate.
- Using **GPT-4 to judge GPT-4** → self-enhancement bias.
- **No human alignment** of an LLM-judge → you're measuring the judge, not the system.

---

## SECTION 3 — Quiz (10 progressively harder questions)

### Q1 (Beginner). What does the F1-score measure, and what is its formula?
**Answer:** F1 is the harmonic mean of precision and recall: F1 = 2·P·R / (P + R). It is high only when **both** precision and recall are high.
**Strong answer includes:** formula; statement that it's a harmonic (not arithmetic) mean; explanation that the harmonic mean penalizes extreme imbalance between P and R; note that F1 is preferred over accuracy on imbalanced datasets.
**Common mistakes:** confusing F1 with average of P and R; computing it from raw counts incorrectly; assuming F1 always equals accuracy.

### Q2 (Beginner). What's the difference between offline and online evaluation?
**Answer:** Offline evals are run on a fixed pre-collected dataset before deployment (golden sets, CI suites). Online evals are run on live production traffic (A/B tests, shadow deployments, real-time guardrails, observability tracing).
**Strong answer includes:** mention of golden datasets; CI integration for offline; latency/cost constraints for online; that online catches drift and distribution shift the offline set never saw.
**Common mistakes:** thinking online means "the model is online" (it means evaluation happens online); skipping that you typically need both.

### Q3 (Beginner-Intermediate). When should you prefer PR-AUC over ROC-AUC?
**Answer:** When classes are imbalanced and you care primarily about the positive (minority) class. ROC-AUC can look misleadingly high on imbalanced data because TN dominates the False Positive Rate denominator.
**Strong answer includes:** definitions of TPR/FPR/precision/recall; example (fraud, medical screening); statement that PR curve focuses entirely on the positive class.
**Common mistakes:** claiming ROC-AUC is "always" worse; conflating "imbalance" with "high accuracy"; missing that PR-AUC has no random baseline of 0.5 — it equals the positive class prevalence.

### Q4 (Intermediate). What is data leakage, and name two ways it commonly happens?
**Answer:** Leakage occurs when information from the test/future is improperly available during training, inflating evaluation scores. Common causes: (1) computing features (e.g., target encoding, normalization stats) before splitting; (2) duplicates across train and test; (3) temporal leakage where test rows precede training rows in time; (4) benchmark contamination from pretraining corpora.
**Strong answer includes:** at least two concrete examples; mention of LLM benchmark contamination (e.g., GSM8K in Mistral/Phi found via ConStat); recommendation to fit transformers inside CV folds.
**Common mistakes:** confusing leakage with overfitting; forgetting that LLM pretraining contamination is also leakage.

### Q5 (Intermediate). Name the three main biases of LLM-as-a-judge identified by Zheng et al. (2023), and one mitigation each.
**Answer:**
1. **Position bias** — preference for the first (or last) candidate. Mitigation: evaluate both orders; declare tie if inconsistent.
2. **Verbosity bias** — preference for longer answers regardless of content. Mitigation: instruct judge to ignore length; cap length; control for length in analysis.
3. **Self-enhancement bias** — preference for outputs from a model of the same family. Mitigation: use a judge from a different model family; cross-validate with a second judge.
**Strong answer includes:** citation of the MT-Bench paper; note that "strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans" (Zheng et al., NeurIPS 2023); bonus for mentioning limited math/reasoning grading as a fourth limitation.
**Common mistakes:** missing self-enhancement; not knowing the standard order-swap mitigation; not mentioning that few-shot examples reduce position bias.

### Q6 (Intermediate). Describe the RAG triad of metrics.
**Answer:** Faithfulness (Answer↔Context): does the answer follow from the retrieved context? Answer Relevance (Answer↔Question): is the answer on-topic? Context Precision/Recall (Context↔Question): did the retriever return relevant documents, and did it cover the necessary ones?
**Strong answer includes:** mapping to RAGAS metric names; explanation that faithfulness catches hallucination; that high precision with low recall means the retriever is conservative; that you cannot optimize one metric alone without hurting the others.
**Common mistakes:** confusing faithfulness with relevance; ignoring context recall; assuming a single "RAG score" is sufficient.

### Q7 (Intermediate-Advanced). You have 100 eval examples; Model A scores 78%, Model B scores 80%. Can you declare B better? Walk through the reasoning.
**Answer:** Probably not. With n=100 and p≈0.8, the standard error per model is √(0.8·0.2/100) ≈ 0.04 (4 percentage points). A 95% CI around each score is roughly ±8 pp. The difference of 2 pp is well inside the noise. You'd need either (a) ~1000+ examples, (b) paired analysis using McNemar's test on per-example wins/losses, or (c) bootstrap CI on the score difference.
**Strong answer includes:** computed SE; mention of paired (per-example) tests being more powerful than two-sample tests; recognition that LLM eval scores also have *generation* noise from sampling temperature — re-running can yield different scores.
**Common mistakes:** declaring B better; using a two-sample test instead of a paired test; forgetting sampling/temperature variance on top of dataset noise.

### Q8 (Advanced). Why is GSM8K no longer a useful frontier benchmark in 2026, and what replaced it?
**Answer:** GSM8K (8,500 grade-school math problems, Cobbe et al. 2021) has been saturated by frontier models (>95%) and is documented to be contaminated in several open models' training data (e.g., Mistral-7B on GSM8K detected via ConStat). Replacements: **MATH** (competition-level), **GSM1K** (novel held-out variants), **AIME 2024/2025**, **FrontierMath** (350 problems across four tiers developed in collaboration with "over 60 mathematicians from leading institutions, including professors, IMO question writers, and Fields medalists," per Epoch AI's FrontierMath page, Nov 2024 — at launch frontier models scored below 2%), and **LiveCodeBench / LiveBench** (continuously refreshed problems with release dates so you can score only on post-cutoff items; LiveCodeBench at ICLR 2025).
**Strong answer includes:** the words "saturation" and "contamination"; at least two replacements; the time-based partitioning idea used by LiveCodeBench and LiveBench.
**Common mistakes:** thinking GSM8K is still definitive; not knowing about the contamination literature; not mentioning the time-partition fix.

### Q9 (Advanced). You're shipping a customer-support RAG bot. Design an eval architecture covering CI, online monitoring, and red-teaming. What metrics fire what alerts?
**Answer:** A defensible design has four layers:
1. **Golden set (offline, CI):** ~100–300 hand-curated Q-A-Context triples, run on every PR via Promptfoo or DeepEval. Metrics: faithfulness, answer relevance, context recall, plus 15 deterministic assertions (no PII, valid JSON, no profanity). Gate deploys at a pass-rate threshold (e.g., faithfulness ≥ 0.85).
2. **LLM-judge rubric (offline + sampled online):** A 3-point rubric aligned to human labels with κ > 0.6, run on a daily sample of 500 production conversations.
3. **Online observability (Phoenix or LangSmith):** Trace every request; alert if p95 latency > 3s, retrieval-empty rate > 5%, or "I don't know" rate jumps > 2σ over baseline (drift signal).
4. **Red-team (weekly + pre-release):** Run `promptfoo redteam` for prompt injection, jailbreaks, PII leakage, hallucination probes. Block release if any critical-severity probe succeeds.
**Strong answer includes:** an explicit golden-set size; CI gating; an alignment step for the judge; both drift and quality alerts; a security gate. Bonus for mentioning shadow deployment and a rollback plan.
**Common mistakes:** conflating offline and online into one bucket; no human alignment of the judge; no statistical thresholding on alerts (they become noisy); skipping red-teaming entirely.

### Q10 (Advanced). Why does optimizing a single LLM-judge score risk Goodhart's Law, and how do you defend against it?
**Answer:** Goodhart's Law: "when a measure becomes a target, it ceases to be a good measure." LLM-judge scores can be gamed because the judge has biases (verbosity, format, sycophancy) and limited reasoning. Optimizing prompts/models against a single judge will yield outputs that exploit the judge's biases (e.g., longer answers, confident tone) without improving real quality. This is empirically observed on Chatbot Arena/LMArena, where LMSYS's August 2024 Style Control analysis found that "response length emerged as the overwhelmingly dominant style factor… models that generated longer, more formatted responses tended to win more battles, not necessarily because their content was better." LMSYS introduced four style-feature regression controls in response.
**Defenses:** (1) Use multiple diverse judges and average; (2) periodically re-align the judge against fresh human labels; (3) maintain a held-out golden set the judge never sees; (4) monitor for distribution shift in *outputs* (e.g., mean answer length) as a Goodhart canary; (5) include adversarial test cases designed to break the judge; (6) combine model-graded metrics with deterministic assertions and human spot checks.
**Strong answer includes:** the Goodhart definition; at least three defenses; reference to length/style confounding on Chatbot Arena and the Style Control fix; recognition that the judge itself can drift when the underlying model is updated by the provider.
**Common mistakes:** treating LLM-judge as ground truth; relying on one judge family (e.g., always GPT-4); not realizing the judge can change silently when the API model is updated.

---

## SECTION 4 — Learning Ladder (5 levels)

### Level 1 — Beginner (0–4 hours in)
**Learn:** What an eval is; offline vs online vs human-in-the-loop; confusion matrix; accuracy/precision/recall/F1; the idea of a golden test set; "vibe check" as a starting point but not a stopping point.
**Resources:** Hamel's "Your AI Product Needs Evals"; Google ML Crash Course classification section.
**Milestone:** You can hand-label 20 outputs from any LLM app good/bad with a written rationale, and you can compute precision and recall from a 2×2 confusion matrix without looking up the formula.
**Progress to Level 2 when:** You can articulate why accuracy fails on a 99/1 imbalanced dataset, and you've built one CSV-based eval set.

### Level 2 — Practitioner (4–10 hours)
**Learn:** ROC-AUC vs PR-AUC; MAE/RMSE/R²; data splits and cross-validation; data leakage; baseline models; major LLM benchmarks (MMLU, GSM8K, MT-Bench, Chatbot Arena) and their limitations; basic RAG metrics (faithfulness, context recall).
**Resources:** Chip Huyen, *AI Engineering* Ch. 3–4; Hugging Face Evaluation Guidebook; RAGAS docs.
**Milestone:** You can run a classification eval end-to-end with stratified CV and explain leakage to a peer; you have written and run at least 10 test cases through RAGAS or a similar framework.
**Progress to Level 3 when:** You can explain why MMLU scores in the high 80s no longer differentiate frontier models, and you've shipped an eval set used by your team.

### Level 3 — Intermediate (10–16 hours)
**Learn:** LLM-as-judge methodology and its three biases (position, verbosity, self-enhancement); rubric design; human-judge alignment (Cohen's kappa); using Promptfoo / DeepEval / Phoenix; instrumenting traces with OpenTelemetry/OpenInference; basic red-teaming (prompt injection, jailbreaks).
**Resources:** Zheng et al. MT-Bench paper; Hamel's "Creating a LLM-as-a-Judge that Drives Business Results"; Promptfoo and DeepEval docs.
**Milestone:** You have built an LLM-judge whose agreement with your human labels exceeds κ = 0.6, you have detected and fixed at least one judge bias on your data, and you have run a red-team probe against your own application.
**Progress to Level 4 when:** Your LLM-judge scores correlate ≥0.7 with expert human judgments on a held-out sample, and you've integrated an eval step into your CI.

### Level 4 — Advanced (16–22 hours)
**Learn:** CI/CD eval gates and regression policies; drift detection (PSI, KS-test, embedding drift); A/B and shadow deployments; statistical rigor (confidence intervals, paired tests, bootstrap, sample-size calculations); agent evaluation (τ-bench, trajectory metrics); benchmark contamination detection (Min-K%, ConStat, time-partitioning).
**Resources:** DeepLearning.AI's *Automated Testing for LLMOps*; UK AISI's Inspect framework; τ-bench paper; Evidently AI's drift articles.
**Milestone:** You have a CI workflow that gates merges on eval pass-rate, a daily drift monitor on production inputs, and you can compute bootstrap CIs and a paired McNemar test on a model A vs B comparison.
**Progress to Level 5 when:** You have authored a complete eval architecture diagram for a production system that has caught at least one real regression before it shipped.

### Level 5 — Expert (22+ hours, ongoing)
**Learn:** Designing custom benchmarks resistant to contamination; multi-judge ensembles; eval cost-benefit analysis; eval data flywheels with active learning; safety evaluation taxonomies (OWASP LLM Top 10, NIST AI RMF); cross-lingual and multimodal evals; agent safety / trajectory-level evaluation (ATBench, TRAJECT-Bench); fine-tuning custom judges (Prometheus, JudgeLM); evals as a research discipline.
**Resources:** UK AISI Autonomous Systems Evaluation Standard; Inspect Evals catalogue (200+ pre-built); papers from Anthropic, OpenAI, and METR; eugeneyan.com long-form survey posts.
**Milestone:** You have built a contamination-resistant, multi-judge eval system that another team relies on, published or open-sourced an eval suite, and you are the person other engineers ask for help on eval design.
**Progress beyond Level 5:** Contribute to or curate a public benchmark (e.g., HELM, Inspect Evals, BIG-bench), or publish a paper / influential blog post on eval methodology.

---

## SECTION 5 — Top 5 Learning Resources

### 1. Hamel Husain — Blog + "AI Evals for Engineers & PMs" Maven course (with Shreya Shankar)
**URL:** https://hamel.dev/ • https://maven.com/parlance-labs/evals
**Why it's worth the time:** Hamel's "Your AI Product Needs Evals" is the single most-referenced practitioner playbook for LLM evals; the Maven course, co-taught with UC Berkeley researcher Shreya Shankar, is described in Lenny's Newsletter (Sep 2025) as "the #1 highest-grossing course on Maven," with Hamel and Shreya having "trained more than 2,000 PMs and engineers, and leaders at over 500 companies" including the major AI labs. Material is opinionated, case-study driven (Rechat's "Lucy" assistant), and immediately actionable. The blog alone gives you ~70% of what the paid course covers. Hamel and Shankar's January 2026 FAQ post quantifies the work involved: "In the projects we've worked on, we've spent 60–80% of our development time on error analysis and evaluation."

### 2. Chip Huyen — *AI Engineering: Building Applications with Foundation Models* (O'Reilly, 2025)
**URL:** https://huyenchip.com/books/ (also on Amazon/O'Reilly)
**Why:** Per Chip Huyen's own site, "It's been the most read book on O'Reilly since its release" (January 2025). Chapters 3 ("Evaluation Methodology") and 4 ("Evaluate AI Systems") give you the conceptual scaffolding — perplexity, similarity metrics, AI-as-judge, comparative evaluation — without drowning in code. Pair it with her earlier *Designing Machine Learning Systems* (2022) for the classical ML side. Endorsed by Luke Metz (co-creator of ChatGPT) and Andrei Lopatenko.

### 3. Hugging Face Evaluation Guidebook — Clémentine Fourrier
**URL:** https://github.com/huggingface/evaluation-guidebook (current canonical: https://huggingface.co/spaces/OpenEvals/evaluation-guidebook)
**Why:** Free, regularly updated (latest deep-dive Sept 2025), and written by the researcher who runs Hugging Face's Open LLM Leaderboard and designed `lighteval`. Best treatment of the theory side: benchmark design, model-as-judge limits, contamination, statistical signal in evals. Multilingual (English, Chinese), with both beginner and advanced tracks.

### 4. EleutherAI lm-evaluation-harness + Inspect AI (UK AISI)
**URLs:** https://github.com/EleutherAI/lm-evaluation-harness • https://inspect.aisi.org.uk/
**Why:** The two open-source frameworks every serious practitioner should know. Per the official EleutherAI/lm-evaluation-harness GitHub README: "The Language Model Evaluation Harness is the backend for 🤗 Hugging Face's popular Open LLM Leaderboard, has been used in hundreds of papers, and is used internally by dozens of organizations including NVIDIA, Cohere, BigScience, BigCode, Nous Research, and Mosaic ML" — install it once and you can run MMLU, ARC, HellaSwag, GSM8K, TruthfulQA, PIQA, WinoGrande and 100+ other tasks with a single CLI command. **Inspect** (released by the UK AI Security Institute in May 2024) ships 200+ pre-built evals, sandboxed code execution, multi-agent workflows, and is the standard for frontier-model auditing (used by METR, Apollo Research, multiple AISIs).

### 5. Production tooling triad — Promptfoo + DeepEval + RAGAS (plus one observability tool)
**URLs:** https://www.promptfoo.dev/ • https://deepeval.com/ • https://docs.ragas.io/ • plus https://arize.com/docs/phoenix (or https://smith.langchain.com/ if you're on LangChain)
**Why:** Together these four cover the vast majority of production AI-eval workflows in 2026. **Promptfoo** is the fastest CLI/YAML way to compare prompts and run red-team probes. **DeepEval** plugs into pytest with 50+ metrics for Python teams. **RAGAS** is the canonical RAG metric library (faithfulness, context precision, context recall, answer relevance). **Phoenix** (open-source from Arize) or **LangSmith** (LangChain's hosted tool) handle the tracing/observability layer. The "two-tool pattern" — one CI-time framework plus one production-time observability platform — is the de facto standard.

**Honorable mentions (use as supplements):**
- **Eugene Yan** — *Patterns for Building LLM-based Systems & Products* (eugeneyan.com/writing/llm-patterns/) and *Task-Specific LLM Evals That Do & Don't Work*. Best long-form practitioner essays.
- **Jason Liu** — *There Are Only 6 RAG Evals* (jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/). A compact mental model from the creator of the Instructor library reducing all RAG evaluation to six conditional relationships between Question, Context, and Answer: "The power of focusing on Question (Q), Context (C), and Answer (A) is that these three components, and their conditional relationships, cover every possible aspect of RAG evaluation."
- **DeepLearning.AI short courses** — *Automated Testing for LLMOps* (with CircleCI, ~1 hr) and *Red Teaming LLM Applications* are excellent 1–2-hour video introductions. Andrew Ng's older *Evaluating and Debugging Generative AI* (with W&B) is still useful for experiment tracking. ("Quality and Safety for LLM Applications" was officially deprecated by DeepLearning.AI — skip it.)
- **OpenAI Evals** — github.com/openai/evals and platform.openai.com/docs/guides/evals. Per the OpenAI Platform docs: "Evaluations (often called evals) test model outputs to ensure they meet style and content criteria that you specify." Per the GitHub README: "Evals provide a framework for evaluating large language models (LLMs) or systems built using LLMs." Useful if you're already in the OpenAI ecosystem.
- **Zheng et al. (2023), *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*** — arxiv.org/abs/2306.05685. Primary source for the position/verbosity/self-enhancement biases.

---

## SECTION 6 — Feynman Technique Walkthrough

### Step 1 — The simplest possible explanation
**Imagine you hired a new assistant who writes emails for you.** How do you know they're any good? You'd do three things:
1. **Test them on stuff you know the right answer to.** ("Reply to my mom's birthday email." If the reply is rude, they failed.) → This is an **eval**.
2. **Spot-check their real work occasionally.** (Read a few of their actual sent emails.) → This is **production monitoring**.
3. **Try to trip them up.** ("What if a stranger emails you pretending to be me?") → This is **red-teaming**.

**AI eval/QA is exactly the same thing**, applied to AI models instead of assistants. You build a set of questions where you know what a good answer looks like (the "golden set"). You run the AI on them. You measure how often it got it right. When the AI is good enough, you let it loose on real users — but you keep watching, because the world changes (new email styles, new scams), and what was good yesterday may not be good today (**drift**).

Three twists make AI eval harder than evaluating a human assistant:
- **Speed:** the AI handles millions of requests, so you can't read every one. You need automated grading.
- **Subjectivity:** there's often no single right answer (e.g., "summarize this article"). So you either pay humans to grade, or you use **another AI as the judge** — which has its own biases (it prefers longer answers, prefers its own family's outputs, prefers whichever answer comes first).
- **Sneakiness:** the AI can be confidently wrong (**hallucinations**), so you specifically need tests that catch *plausible-but-false* answers, not just *obviously broken* ones.

That's it. Everything else — F1 scores, RAGAS, LLM-as-judge, drift detection, CI gates — is just **techniques for doing those three things at scale and without fooling yourself**.

### Step 2 — Re-Explanation Script (for the learner to use)

Use this script to teach AI eval/QA to a friend, a rubber duck, or yourself out loud. Pause at each `[CHECK]` and notice if you stumble.

> **Opening (30 sec):** "AI eval/QA is the discipline of measuring whether an AI system is good enough — before you ship it, while it's running, and after it fails. Without it, you're flying blind, because AI outputs are non-deterministic and AI mistakes look confident."
>
> **[CHECK 1]** Can you give a one-sentence definition of "eval" without using the word "evaluate"?
>
> **The three loops (1 min):**
> "There are three loops you need.
> First, the **offline loop**: I have a fixed set of test inputs with known good answers — a golden set — and I run my AI on them every time I change a prompt or a model, just like unit tests in software. I score the answers using either deterministic rules (regex, exact match, JSON schema), or by asking another AI to grade them with a rubric, or by having a human grade them.
> Second, the **online loop**: in production, I trace every request, sample a small percentage, score that sample, and watch for drift — if the inputs or outputs start to look different from yesterday, something changed.
> Third, the **red-team loop**: I deliberately try to break my own system with prompt injections, jailbreaks, edge cases, and adversarial inputs. I do this on a schedule and before every release."
>
> **[CHECK 2]** Can you name one tool you'd use for each loop?
> *(Example: Promptfoo / DeepEval for offline; Phoenix or LangSmith for online; Promptfoo's red-team mode or Inspect for red-team.)*
>
> **The metrics (1 min):**
> "Classical ML metrics still matter: precision, recall, F1 for classification — and you use precision-recall (not ROC) when the data is imbalanced. MAE and RMSE for regression. For generative AI, reference-based metrics like BLEU and ROUGE mostly don't work for open-ended tasks, so we use **LLM-as-judge** — but LLM judges have three known biases I have to mitigate: position (prefers first answer), verbosity (prefers longer), and self-enhancement (prefers its own family). For RAG, I use a triad: faithfulness (answer matches context), answer relevance (answer matches question), context precision/recall (retrieved docs match question)."
>
> **[CHECK 3]** Can you draw the RAG triad and label each edge with what it measures?
>
> **The honest part (45 sec):**
> "The biggest mistake teams make isn't picking the wrong metric — it's not looking at data. As Hamel Husain and Shreya Shankar put it in their January 2026 FAQ: 'In the projects we've worked on, we've spent 60–80% of our development time on error analysis and evaluation.' The metric you compute is downstream of the *taxonomy of failures* you build by reading data. Without that, even a great metric tells you nothing."
>
> **[CHECK 4]** Can you name one type of failure you'd find by reading 30 actual outputs of an AI system?
>
> **The trap (30 sec):**
> "Finally — Goodhart's Law. The moment a single eval score becomes a target, people start gaming it (often unintentionally). Defenses: multiple diverse judges, periodic re-alignment to fresh human labels, deterministic assertions alongside model-graded scores, and a held-out golden set the judge never sees. And always report confidence intervals: a 2-point gap on 100 examples is usually noise."

### Step 3 — Gap-Finder Prompts (where most learners stumble)
After re-explaining, ask yourself these questions. If you can't answer in 1–2 sentences, **go back to the cited source**.

1. **"Why is F1 a harmonic mean and not an average?"** *(Stumble? → Re-read Google ML Crash Course on accuracy/precision/recall.)*
2. **"What's the difference between data drift and concept drift?"** *(Stumble? → Re-read Evidently AI's data-drift and concept-drift posts.)*
3. **"Name the three LLM-judge biases and a mitigation for each."** *(Stumble? → Re-read Zheng et al. 2023, §3.)*
4. **"What's the RAGAS faithfulness metric actually computing under the hood?"** *(Stumble? → It uses an LLM to break the answer into atomic claims and check each against the context. Re-read RAGAS docs.)*
5. **"Why is reporting MMLU on a 2026 frontier model misleading?"** *(Stumble? → Re-read the contamination article on llm-stats.com and the Hugging Face guidebook.)*
6. **"You see 78% vs 80% — is B better?"** *(Stumble? → Re-do the SE calculation: √(p·(1−p)/n) ≈ 0.04. CI ≈ ±8 pp. Likely noise.)*
7. **"What's the difference between an offline eval and a CI eval gate?"** *(Stumble? → They're related but not identical. CI gating is *using* offline evals to *block* a merge. Re-read the *Automated Testing for LLMOps* lesson notes.)*
8. **"Why is using GPT-4 to judge GPT-4 a problem?"** *(Stumble? → Self-enhancement bias. Use a different judge family.)*

### Step 4 — Re-teach the Tricky Parts
If any check above fails, write a one-paragraph explanation of the failing concept **as if explaining it to a smart 12-year-old**, using a concrete example from your own domain. Do not move on until you can explain it without notes.

---

## Recommendations (decision-ready, staged)

**If you have only 4 hours this week → "Get unstuck"**
1. Read Hamel's "Your AI Product Needs Evals" end-to-end (1 hr).
2. Hand-label 20 outputs from your real AI product good/bad with reasons (2 hrs).
3. Run `npx promptfoo@latest init` and convert 5 of those labels into a YAML config (1 hr).
**Benchmark to upgrade your plan:** if you can now name your top 3 failure modes, move to Sessions 5–7 of the 20-hour plan next.

**If you have 20 hours → execute Section 1 sequentially.** Do not skip Session 5 (LLM-as-judge alignment) — it's where most teams stall. Defer Sessions 8–9 only if you don't operate a production system yet.

**If you have a team and 4 weeks → enroll in Hamel & Shreya's Maven cohort** (next cohort listed as January 2026; lifetime access). Threshold to justify this spend: your AI feature is in production with paying users and you've already burned a week debugging a regression you couldn't reproduce.

**If you operate a frontier or regulated system → adopt Inspect (UK AISI)** as your evaluation framework. It's the de facto standard for safety auditing and is required for UK AISI's Autonomous Systems evaluation standard.

**Thresholds that would change these recommendations:**
- If your AI app handles regulated data (HIPAA, GDPR Article 22, EU AI Act high-risk) → upgrade observability to a self-hosted Langfuse or Phoenix instance before launching, not after.
- If your LLM-judge κ-agreement with humans is < 0.4 → stop trusting the judge; re-design the rubric and re-align before using it for any go/no-go decision.
- If you ever see a 95% MMLU/HellaSwag score on a model and no other benchmark → don't trust the model card. Run lm-eval-harness yourself or wait for LMArena's Elo.

---

## Caveats

- **The tool landscape moves fast.** As of May 2026, the recommended tools (Promptfoo, DeepEval, RAGAS, Phoenix, LangSmith, Braintrust, Inspect) are well-established, but new entrants appear monthly. The principles (golden sets, LLM-judge alignment, CI gates, drift monitoring, red-teaming) are stable; specific tool choices are not.
- **DeepLearning.AI's *Quality and Safety for LLM Applications* was officially deprecated.** It was a useful course in 2024 but should not be a starting point in 2026.
- **Benchmark scores reported by model vendors must be read with caution.** Vendor-reported SWE-bench/τ-bench/AIME numbers in late 2025 and early 2026 commonly cross 80%, but scaffold, scratchpad, tool setup, and grading protocol vary across reports and are not directly comparable. Always check whether the score is from the official Verified subset and a third-party run.
- **LMSYS Chatbot Arena was rebranded to LMArena (Arena) in 2024–2026** and incorporated as Arena Intelligence Inc. in April 2025. The leaderboard is still the closest thing to a "ground truth" for general LLM preference, but it is influenced by style/length (now partially controlled via the August 2024 Style Control regression).
- **Confidence intervals and significance testing for LLM evals are underused in industry.** Most "Model A vs B" claims in 2024–2026 fail basic statistical scrutiny. Apply Q7-style reasoning before believing a comparison.
- **Some quantitative claims here** (e.g., the 60–80% error-analysis figure, Maven course rankings, contamination percentages, FrontierMath difficulty tiers) come from practitioner blog posts, vendor pages, or working papers, not peer-reviewed research. They are directionally accurate and traceable to named sources cited above, but should not be cited as definitive academic statistics.
