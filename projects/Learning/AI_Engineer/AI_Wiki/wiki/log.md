# Log

Append-only, chronological record of operations against this wiki.
Every entry starts with `## [YYYY-MM-DD] <op> | <title>` so the log stays greppable:
`grep "^## \[" log.md | tail -5`.

Never edit or delete past entries. Only append.

## [2026-07-08] setup | Schema retuned + consolidated
- AI_Wiki adopted the LLM-wiki schema, retuned from the generic Second Brain scaffold to its real domain: AI engineering practice + hcho's AI-native career pivot.
- Made this directory the canonical home; the empty `projects/SecondBrain/` duplicate was retired.
- Registered in the Mandu `CLAUDE.md` Active wikis list. `mode: full`.
- Open decision: the YouTube-transcript wiki shares this domain (video-transcript diet); AI_Wiki is the consolidation target, cross-linked for now, full merge to be confirmed with hcho.

## [2026-07-08] ingest | Your AI Product Needs Evals (Hamel Husain)
- Source: [[your-ai-product-needs-evals]] (Hamel Husain, hamel.dev, 2024-03-29).
- Created hub [[evals]]; concepts [[three-level-eval-framework]], [[llm-unit-tests]], [[llm-as-judge]], [[looking-at-your-data]]; entity [[hamel-husain]].
- Updated [[index]] (1 source, 1 area, 4 concepts, 1 entity) and [[synthesis]].
- No contradictions (first content source). Cross-linked to the evals pilot wiki (`projects/Learning/AI_Engineer/evals/`, hcho's own synthesis layer).

## [2026-07-08] setup | Folded in the YouTube-transcript wiki
- Resolved the open consolidation item from the genesis entry: the planned YouTube-transcript wiki (2026-07-03 PRD/decision) was never physically built, and AI_Wiki already realizes its scope (full mode, organic concepts, AI-engineering talk/tutorial/transcript diet).
- Fold is bookkeeping, not a content migration: no separate directory existed to move pages from.
- Removed the phantom YouTube-transcript entry from CLAUDE.md Active wikis; AI_Wiki now formally owns the transcript diet. Schema updated. PRD banner-marked superseded.

## [2026-07-08] ingest | Agents Are the New SaaS (Startup Ideas Podcast)
- Source: [[agents-are-the-new-saas]] (tutorial summary).
- Created hub [[agent-saas]]; concepts [[agent-saas-sells-work]], [[workflow-with-a-paycheck]], [[seven-part-agent-spec]], [[minimal-useful-agent]], [[start-as-a-workflow]], [[product-wrapper]], [[outcome-based-pricing]]; entity [[anthropic]].
- Cross-linked into [[evals]] (the "agent's gym" = 50-example eval set as quality gate + sales asset); updated [[synthesis]] to connect the evals and agent-saas hubs through quality.
- Updated [[index]] (2 sources, 2 areas, 11 concepts, 2 entities). No contradictions.

## [2026-07-08] ingest | 50 AI-Era Career Tips (Meta Staff Engineer / creator)
- Source: [[ai-era-50-career-tips]] (tutorial summary, 50 tips in 5 themes).
- Created hub [[ai-career]]; concepts [[agentic-engineering]], [[react-loop]], [[taste-as-moat]], [[t-shaped-portfolio]], [[build-in-public]], [[cost-of-being-wrong]]; entities [[andrej-karpathy]], [[boris-cherny]].
- Folded ~50 one-off tips into the hub by theme (no thin per-tip pages); left [[own-the-problem-not-the-code]] and [[build-for-the-model-of-the-future]] as valid to-do link-markers.
- Cross-linked into [[evals]] ("learn where AI fails, keep a log"; "agentic validations") and extended [[anthropic]] (Claude Code / Opus 4.5). Updated [[synthesis]] (career half now open, same quality/judgment spine).
- Updated [[index]] (3 sources, 3 areas, 17 concepts, 4 entities). No contradictions.

## [2026-07-08] ingest | Building Your Own AI Operating System (Nate)
- Source: [[ai-operating-system-tutorial]] (tutorial summary).
- Created concepts [[ai-operating-system]], [[context-is-king]], [[four-cs-framework]], [[capabilities-not-instructions]], [[phased-autonomy]], [[building-skills]]; new entity [[claude-code]].
- Opened an agent-safety spine in [[synthesis]] (capabilities-not-instructions + phased-autonomy joining start-as-a-workflow + MUA); noted the AIOS meta-frame (this is what AI_Wiki + Mandu already are). Extended [[anthropic]].
- Updated [[index]] (4 sources, 3 areas, 23 concepts, 5 entities). No contradictions.

## [2026-07-08] ingest | Building an AI Skill from Scratch (Peter, Behind the Craft)
- Source: [[ai-skill-from-scratch]] (tutorial summary, 5-step skill method).
- Created concepts [[skill-eval-loop]], [[pass-fail-over-score-evals]], [[ai-slop]].
- Deepened existing pages (compounding, not sprawl): [[building-skills]] (2 sources, +5-step method & file anatomy), [[llm-as-judge]] (2 sources, +binary checks & isolated grader), [[evals]] hub (4 sources).
- Updated [[synthesis]]: eval discipline now shown at three scales (product / agent business / single skill). Updated [[index]] (5 sources, 3 areas, 26 concepts, 5 entities). No contradictions.

## [2026-07-08] ingest | Building 5 AI Products Solo (Josh Pigford)
- Source: [[building-5-ai-products-solo]] (interview summary).
- Created concepts [[adversarial-code-review]], [[phased-implementation]], [[context-rot]], [[self-updating-config]], [[ship-fast-learn-from-users]]; entities [[josh-pigford]], [[conductor]], [[openai]].
- Extended [[ai-slop]] (2 sources; +brand-first design as visual slop avoidance).
- Synthesis: added a 4th verification scale (code) and an AI-assisted build-workflow cluster; flagged the ship-fast vs validation-first tension against hcho's Agentic RAG plan.
- Updated [[index]] (6 sources, 3 areas, 31 concepts, 8 entities). No contradictions (one tension noted, not a contradiction).

## [2026-07-08] ingest | Running a One-Person Company with AI Agents (Ryan Carson)
- Source: [[one-person-company-with-agents]] (walkthrough summary).
- Created concepts [[agents-as-cron-plus-markdown]], [[agent-as-employee]], [[build-the-machine-first]], [[everything-is-a-pr]], [[red-team-your-agent]]; entities [[ryan-carson]], [[open-claw]], [[devin]], [[google]].
- Extended [[capabilities-not-instructions]] (linked the identity + red-team facets); opened an agent-operations cluster and completed a 4-part agent-safety spine in [[synthesis]]; sharpened the MVP-inversion tension into a triangle (ship-fast / build-the-machine / validate-first).
- Updated [[index]] (7 sources, 3 areas, 36 concepts, 12 entities). No contradictions.

## [2026-07-08] ingest | Building Products with Coding Agents (solo L8 builder)
- Source: [[building-products-with-agents]] (walkthrough summary; tools Lavish + No Mistakes are in this very session).
- Created concepts [[get-out-of-the-loop]], [[plan-code-validate]], [[fresh-context-review]], [[agent-testing-instructions]], [[sub-agents]]; entity [[opencode]].
- Tightened the verification cluster: [[fresh-context-review]] now unifies [[skill-eval-loop]] (isolated grader), [[context-rot]], [[sub-agents]], and [[adversarial-code-review]]; back-linked all three.
- Synthesis: named the governing philosophy (get out of the loop) and reframed hcho's edge as "build the automated reviewer."
- Updated [[index]] (8 sources, 3 areas, 41 concepts, 13 entities). No contradictions.

## [2026-07-08] ingest | Classification: ROC and AUC (Google ML Crash Course)
- Source: [[classification-roc-and-auc]] (doc; first classical-ML-metrics source).
- Created area [[ml-metrics]]; concepts [[roc-and-auc]], [[precision-recall]], [[classification-threshold]].
- Cross-linked into the eval spine: gave [[precision-recall]] a home for the long-recurring "precision/recall not raw agreement" caveat ([[llm-as-judge]], [[pass-fail-over-score-evals]]); tied [[classification-threshold]] to [[cost-of-being-wrong]]; linked [[evals]] hub to the classical foundations. Extended [[google]] (2 sources).
- Updated [[index]] (9 sources, 4 areas, 44 concepts, 13 entities). No contradictions.

## [2026-07-08] ingest | Build a Production-Ready Agent with Claude Managed Agents (Anthropic)
- Source: [[production-agent-with-cma]] (workshop summary).
- Created concepts [[managed-agent-primitives]], [[outcome-rubric-iteration]], [[agent-observability]], [[credential-vaults]], and resolved the pending marker [[build-for-the-model-of-the-future]] (now 2 sources).
- Extended [[capabilities-not-instructions]] (per-tool permissions, deny web access), [[skill-eval-loop]] (Outcomes = platform version), [[looking-at-your-data]] (-> observability), [[anthropic]] (CMA, 4 sources), [[claude-code]] (Claude API skill, 3 sources).
- Synthesis: hand-built patterns are becoming platform primitives; durable skill is rubric/permissions/traces judgment, not the plumbing.
- Updated [[index]] (10 sources, 4 areas, 49 concepts, 13 entities); removed build-for-the-model from pending markers. No contradictions.

## [2026-07-08] ingest | Every Claude Feature Ranked (AI Automation Society)
- Source: [[every-claude-feature-ranked]] (tier-ranking summary; deepening source).
- Created concepts [[agent-teams]] (debate boards) and [[checkpoint-rewind]] (/rewind).
- Deepened (compounding): [[building-skills]] (3 sources, now established; Skills = #1 feature), [[self-updating-config]] (auto-memory), [[sub-agents]] (parallel-vs-debate contrast), [[plan-code-validate]] (/goal + definition of done), [[context-rot]] (status line + rewind), [[agents-as-cron-plus-markdown]] (routines), [[claude-code]] (4 sources).
- Updated [[index]] (11 sources, 4 areas, 51 concepts, 13 entities). No contradictions.

## [2026-07-08] ingest | Inside Conductor (Charlie, co-founder)
- Source: [[inside-conductor-workflow]] (deep-dive summary).
- Created concepts [[slop-free-zones]], [[dont-let-ai-be-your-architect]], [[code-as-sawdust]], [[model-selection]], and resolved the last pending marker [[own-the-problem-not-the-code]] (2 sources).
- Heavily extended [[conductor]] (2 sources: workspace/worktree model, enforced PR flow, product philosophy, stack); cross-linked [[taste-as-moat]].
- Synthesis: added the human-owns-the-important-parts counterweight to get-out-of-the-loop ("delegate the code, own the judgment"); index pending-markers list now empty.
- Updated [[index]] (12 sources, 4 areas, 56 concepts, 13 entities). No contradictions.

## [2026-07-08] ingest | Working With Fable 5 in Claude Code (Theo / T3)
- Source: [[working-with-fable-5]] (YouTube tutorial summary; cost-min-maxing + a live 16-PR-backlog/month-in-a-day run).
- Created concepts [[model-routing]], [[reasoning-effort-discipline]], [[time-to-fix-as-health-signal]]; entity [[theo-t3]].
- Heavily extended [[model-selection]] (2 sources; the intelligence/taste/cost glossary, ratings-are-defaults-not-limits, "judge the output not the price tag"); extended [[adversarial-code-review]] (2 sources; Codex Review skill + automated merge-gate reviewers) and [[get-out-of-the-loop]] (2 sources; the long-running "goal" behind a staging-only boundary). Extended entities [[anthropic]] (5), [[openai]] (2), [[claude-code]] (5).
- Synthesis: added the economics dimension to the workflow arc (get-out-of-the-loop made affordable by reasoning-effort + routing, made safe by a physical staging/prod boundary). No contradictions.
- Updated [[index]] (13 sources, 4 areas, 59 concepts, 14 entities).

## [2026-07-08] ingest | Building Robust Applications with AI / Pluto (Ross, Hey Fabrica)
- Source: [[building-robust-apps-with-ai]] (system-design tutorial via the Pluto architecture; one sponsored segment, Greptile).
- Created area [[system-design]]; concepts [[engineering-trade-offs]], [[everything-as-code-abstractions]], [[monorepo-for-agent-context]], [[client-never-touches-the-database]], [[durable-agent-processes]]; entities [[ross-hey-fabrica]], [[convex]].
- Extended [[open-claw]] (2 sources; OpenClaw now seen at two independent builders), [[agent-observability]] (2 sources; Sentry/PostHog/Daytona, app-level + wire-early), [[agentic-engineering]] (agents depend on everything-as-code), [[adversarial-code-review]] (Greptile confidence-score gate).
- Synthesis: opened the architecture layer under the workflow arc; same conclusion from the other side (durable value = trade-off/boundary/failure-mode judgment). No contradictions.
- Updated [[index]] (14 sources, 5 areas, 64 concepts, 16 entities).

## [2026-07-08] ingest | Startups for Agents (Startup Ideas Podcast)
- Source: [[startups-for-agents]] (agentic-web primer; same show as [[agents-are-the-new-saas]]).
- Created area [[agentic-web]]; concepts [[agent-native-rebuild]], [[agent-buying-journey]], [[agent-building-blocks]], [[agent-readable-website]], [[aeo-answer-engine-optimization]].
- Framed [[agentic-web]] as the mirror of [[agent-saas]] (build for agents-as-buyers vs sell agents-as-labor); cross-linked both areas. Extended [[agent-as-employee]] (2 sources; employee model reappears as an agent-infra spec).
- No new entities (AgentMail/Moltbook/Stripe-wallet/MCP named in-source; held from thin pages). No contradictions.
- Synthesis: even the most business-flavored source lands on measurement + trust as the scarce work. Updated [[index]] (15 sources, 6 areas, 69 concepts, 16 entities).

## [2026-07-08] ingest | Zero to Hireable AI Engineer in 4 Months (@free_ai_guides)
- Source: [[zero-to-hireable-ai-engineer]] (X long-form; build-first four-month career-switch curriculum + market data).
- Opened the [[rag]] area (long-empty gap); concepts [[retrieval-augmented-generation]], [[retrieval-is-the-bottleneck]].
- Career concepts: [[ai-engineer-is-a-builder]], [[switchers-edge]], [[career-switch-mistakes]], [[single-call-workflow-or-agent]].
- Deepened [[ai-career]] (2 sources; PwC/Glassdoor data + the four-month arc), [[build-in-public]] (2; public from day 1, the honest README), [[t-shaped-portfolio]] (2; pick-a-direction), [[start-as-a-workflow]] (build-time twin cross-linked).
- No new entities (curriculum names many tools; held from thin pages; strengthened [[anthropic]] "Building Effective Agents" tie via cross-links). No contradictions.
- Synthesis: most hcho-relevant source yet - hardens the switcher's edge with data and opens RAG; a beginner curriculum converges on the same spine (build-don't-watch, evals-gate-changes, skills-outlast-tools).
- Updated [[index]] (16 sources, 7 areas, 75 concepts, 16 entities).

## [2026-07-08] ingest | Patterns for Building LLM-based Systems & Products (Eugene Yan)
- Source: [[llm-patterns]] (landmark 2023 seven-pattern reference; dated specifics, durable patterns).
- Opened area [[production-llm]]; concepts [[fine-tuning]], [[guardrails]], [[semantic-caching]], [[defensive-ux]], [[data-flywheel]]; entity [[eugene-yan]] (2nd foundational eval voice with [[hamel-husain]]).
- Evals concepts: [[eval-driven-development]], [[reference-based-metrics]], [[benchmark-sensitivity]] (bridge to the coming contamination source). RAG concepts: [[embeddings]] (2 sources), [[hybrid-retrieval]].
- Deepened [[llm-as-judge]] (3 sources; G-Eval + position/verbosity/self-enhancement biases + comparison-over-scoring), [[evals]] area (5 sources), [[rag]] area (2 sources; DPR/FiD/RETRO/HyDE).
- Synthesis: first true systems reference; productionizing an LLM is mostly non-LLM (reliability/cost/trust) engineering - hcho's surface. Convergence across 2023 systems doc + 2026 career guide + workflow talks on the same measure-before-trust spine. No contradictions.
- Updated [[index]] (17 sources, 8 areas, 85 concepts, 17 entities).

## [2026-07-08] ingest | Let's Talk About LLM Evaluation (Clémentine Fourrier, HF)
- Source: [[lets-talk-about-llm-evaluation]] (the benchmarking/leaderboard side of evals).
- Concepts [[three-eval-methods]], [[purposes-of-evaluation]], [[data-contamination]]; entities [[clementine-fourrier]], [[huggingface]].
- Deepened [[benchmark-sensitivity]] (2 sources; rankings-over-scores), [[llm-as-judge]] (4 sources; self-preference, inconsistent scores, crossbreeding-bias worry), [[pass-fail-over-score-evals]] (2 sources; reason-before-scoring), [[evals]] area (6 sources; now has its organizing taxonomy).
- Synthesis: gave evals two organizing frames (three methods, three purposes); every method is biased, so triangulate + measure. Non-regression testing = hcho's native register. No contradictions.
- Updated [[index]] (18 sources, 8 areas, 88 concepts, 19 entities).

## [2026-07-08] ingest | Evaluate AI Systems / AI Engineering Ch.4 (Chip Huyen)
- Source: [[evaluate-ai-systems]] (the most complete eval reference in the wiki).
- Concepts [[evaluation-criteria]], [[factual-consistency]], [[model-build-vs-buy]], [[evaluation-pipeline]]; entity [[chip-huyen]] (4th foundational eval voice).
- Deepened [[eval-driven-development]] (2 sources), [[data-contamination]] (2; n-gram/perplexity detection, "pretraining on the test set"), [[benchmark-sensitivity]] (3; MCQ sensitivity, benchmark correlation, aggregation), [[model-selection]] (3; build-vs-buy cross-link), [[evals]] area (7 sources).
- Synthesis: closed the "CI-gating in practice" open thread via evaluation-pipeline; four eval authorities (Husain/Yan/Fourrier/Huyen) converge without contradiction (define criteria up front, triangulate, measure reproducibly). The pipeline is validation engineering rebadged = hcho's edge as a build. No contradictions.
- Updated [[index]] (19 sources, 8 areas, 92 concepts, 20 entities).

## [2026-07-08] ingest | The LLM Evaluation Guidebook (OpenEvals / Hugging Face)
- Source: [[llm-evaluation-guidebook]] (Fourrier/Frere/Penedo/Thomas Wolf; exhaustive benchmarking-side reference, 15k models / 3 yrs).
- Concepts [[benchmark-saturation]], [[functional-scorers]], [[score-reproducibility]].
- Heavily deepened [[llm-as-judge]] (5 sources, now established; 7-bias catalog + mitigations, jury, evaluate-your-evaluator, reward models), [[data-contamination]] (3, now established; procedural generation), [[three-eval-methods]] (2), [[factual-consistency]] (2; judges weak at hallucination), [[evaluation-pipeline]] (2; create-your-own + sampling + statistical validity), [[benchmark-sensitivity]] (cross-linked), [[evals]] area (8 sources, now established). Extended [[clementine-fourrier]] (2), [[huggingface]] (3).
- Synthesis: hardens the mature eval area; states its north star (functional testing over judges) and its closing frame ("models are only as good as our ability to measure what matters"). No contradictions.
- Updated [[index]] (20 sources, 8 areas, 95 concepts, 20 entities).

## [2026-07-08] ingest | What Is a Contaminated LLM? (Jonathan Chavez, llm-stats)
- Source: [[what-is-a-contaminated-llm]] (dedicated contamination deep-dive; the last of the 9-source batch).
- Concept [[contamination-detection]] (three flavors: direct/indirect/latent; five methods: time-partition, Min-K% Prob, Time Travel, ConStat, canary GUIDs).
- Deepened [[data-contamination]] (4 sources; functional definition, latent/Goodhart flavor, Codeforces cliff, dose-response, retired benchmarks) and [[benchmark-saturation]] (2; distrust-near-ceiling, 2026 resistant stack). No new entity (blog author; noted in source, consistent with @free_ai_guides).
- Synthesis: closes the eval arc on its deepest validity threat; the steady-state defense is "evaluate on your own data the labs can't have seen" = test-set hygiene = hcho's edge. No contradictions.
- Updated [[index]] (21 sources, 8 areas, 96 concepts, 20 entities). **`raw/` inbox now fully ingested.**
