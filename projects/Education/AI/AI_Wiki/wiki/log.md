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

## [2026-07-28] ingest | Designing Loops & Workflows in Claude Code (Tharic, Anthropic Claude Code team)
- Source: [[designing-loops-and-workflows]] (Peter Yang podcast interview; **the wiki's first primary-source Claude Code material** - every prior account of loops/goals/workflows came from outside practitioners). Ends the 20-day pause since the 2026-07-08 batch; four more raw sources remain queued.
- Concepts created: [[verification-signal-picks-the-mechanism]] (the source's central rule: deterministic check takes `/goal`, subjective check takes a workflow with a rubric and a separate verifier), [[self-referential-bias]], [[planning-is-removing-unknowns]], [[principles-over-constraints]] (Anthropic cut the Claude Code system prompt by 80%), [[read-what-the-agent-writes]].
- Entity created: [[tharic]] (Anthropic Claude Code team; first insider voice). Held from thin pages per prior discipline: Peter Yang, Remotion, Whisper, Figma MCP.
- Extended: [[sub-agents]] (2 sources; the second reason to fan out is bias-avoidance, not just context, plus per-task compute budgets), [[agentic-engineering]] (2; primary-source fill-in of three pillars), [[plan-code-validate]] (2), [[fresh-context-review]] (2; fresh context is half the fix, vary the model too), [[llm-as-judge]] (6; self-enhancement bias reached independently from agent tooling), [[building-skills]] (4; workflows are a JS file packageable into a skill; most skills too long), [[reasoning-effort-discipline]] (2; the fan-out analogue), [[ai-slop]] (3), [[agent-as-employee]] (3), [[get-out-of-the-loop]] (3). Entities: [[claude-code]] (6, now established), [[anthropic]] (6), [[boris-cherny]] (2; author of `simplify`), [[andrej-karpathy]] (2).
- **Three tensions flagged explicitly, not overwritten** (both dates recorded in each case): planning as a front-loaded phase ([[plan-code-validate]], 2026-07-08) vs continuous exploration (2026-07-28); parallelism as a forcing function ([[get-out-of-the-loop]], 2026-07-08) vs Tharic cutting back from ~5 parallel sessions to 1 (2026-07-28); the agent-as-coworker metaphor called "helpful but also limiting," with memory described as "spiky." Also a tempering of [[ai-slop]] for internal code (cleanliness is use-case dependent) that leaves the human-facing claim intact.
- Convergence worth noting: [[self-referential-bias]] is now the third independent arrival at the same finding (eval literature measured it, a code-review product attributed it to shared context, Anthropic's tooling team treats it as an architecture constraint). No source cites another.
- Synthesis revised: the verification signal gating the orchestration mechanism makes the eval spine *upstream* of agentic engineering rather than parallel to it; also records the review-loop vs judgment-loop distinction and the instruction-volume reversal. No contradictions between sources, only refinements.
- Updated [[index]] (22 sources, 8 areas, 101 concepts, 21 entities) and logged the open structural question: graduate [[agentic-engineering]] into an area after the remaining four queued sources, not now.

## [2026-08-01] ingest | Six-source batch: agent workflows, agent operations, and the FDE role

Closed the `raw/` inbox. Six sources ingested in one pass at hcho's direction (the skill default is one at a time; he chose the full batch so the queued agent-workflow material could shape the hub once from complete evidence).

**Sources filed:** [[building-at-the-frontier]] (Boris Cherny, Anthropic - Opus 5, ablation, unhobbling), [[running-teams-of-ai-agents]] ([[ryan-carson]], post-PMF), [[agentic-full-stack-build]] ([[kun]]), [[fde-in-30-days]] ([[vas]], Varick Agents), [[loops-to-run-your-business]], [[building-marketing-agents]] ([[cody-schneider]]).

**Structural changes:**
- **[[agentic-engineering]] graduated from concept to area** (11 sources), executing the plan recorded in [[index]] on 2026-07-28. The concept page at `concepts/agentic-engineering.md` was removed and its content rebuilt as the area hub; all existing `[[agentic-engineering]]` links resolve unchanged.
- **[[agent-operations]] created** as a sibling area (6 sources), for running things with agents continuously rather than building software with them. Boundary documented at the top of that page.

**New pages:** 37 concepts, 2 areas, 3 entities ([[kun]], [[vas]], [[cody-schneider]]).
Counts now 28 sources, 10 areas, 137 concepts, 24 entities.

**Contradictions flagged** (recorded on both sides, not smoothed over):
- [[context-rot]] vs [[compaction-over-context-window]] - four clean auto-compactions reported against the "start fresh" rule. Probably concedes the capacity claim, not the contamination claim; counter-evidence is one session, one model, one harness.
- [[cloud-agents-over-local]] vs [[building-5-ai-products-solo]] and [[inside-conductor-workflow]] - "if you are working locally you are a caveman" against two sources running local worktrees deliberately. Ryan Carson's evidence is real but *n* of 1 from a paying Devin customer.
- [[evals-saturate-and-get-replaced]] vs the [[evals]] area's compounding-asset framing - private product evals given a 1-3 model-generation half-life. Reconciled as "the eval skill is durable, the eval artifact is not," stated explicitly on both pages.
- [[red-team-your-agent]] - Opus 5 reported as not demonstrably prompt-injectable, with Boris Cherny's own caveats preserved (Anthropic's own red-teaming; two of three defense layers live in the serving stack, not the weights).
- [[verification-signal-picks-the-mechanism]] tempered - `/go` and `/loop` now "helpful but not required"; likely a model-tier difference, which is inference not source claim.
- [[independent-agent-lab-vs-frontier-lab]] - the wiki's first explicit counter-position to its own Claude Code-centric input diet. Logged as a source-diet correction in [[synthesis]].
- [[sub-agents]] - steerability/observability named as the pattern's weakness by [[agentic-full-stack-build]]; scale ceiling corrected upward by orders of magnitude by [[building-at-the-frontier]].

**Fact correction:** [[ryan-carson]]'s company recorded as "Untangled" from the first source; the second source consistently gives **Untangle**. Entity page and index corrected; noted in the provenance section of [[running-teams-of-ai-agents]].

**Identification:** the "solo L8 builder" of [[building-products-with-agents]] is named as **Kun** by [[agentic-full-stack-build]]; entity created and both sources cross-linked.

**Existing pages extended:** [[principles-over-constraints]] (2nd primary source + the ablation method behind the 80% cut), [[agents-as-cron-plus-markdown]] (4 sources; matured from cron+markdown to cloud playbooks and lab routines), [[get-out-of-the-loop]] (6 sources; the rule is now "you can exit any loop you can replace with a check"), [[credential-vaults]], [[eval-driven-development]], [[phased-autonomy]], [[agent-observability]], [[t-shaped-portfolio]], [[build-for-the-model-of-the-future]], [[sub-agents]], [[verification-signal-picks-the-mechanism]], [[context-rot]], [[red-team-your-agent]], plus the [[evals]] and [[ai-career]] area hubs.

**[[synthesis]] revised** with a new section on what the batch changed: verification promoted from a practice to *the* binding constraint; the eval inverted from a gate into a source of work; and the career half acquiring a specific target in [[forward-deployed-engineer]], whose two required capabilities map unusually cleanly onto a hardware-validation background.

**Noted, not filed:** roughly a third of [[building-marketing-agents]] is a startup pitch (an AI-first WordPress plugin bundle) used as its worked example. It is a specific opportunity rather than durable knowledge, so no page was created; it remains in the raw file.

**Follow-ups logged in [[synthesis]]:** a lint pass (overdue after a batch this size), correcting the Claude Code/Anthropic weighting in the source diet, an FDE role page in the Job-Search Roles wiki, and an [[ablation-driven-development]] audit of Mandu's own `CLAUDE.md` and skills.

## [2026-08-05] ingest | Graph Engineering, Clearly Explained (Greg Isenberg)
- Source: [[graph-engineering-isenberg]] (Greg Isenberg, Startup Ideas Podcast; local raw file, auto-caption summary).
- New concepts: [[graph-engineering]] (the work-design layer: jobs, arrows, state; agent graphs vs knowledge graphs; manual -> file-based -> automated ladder; smallest graph that improves quality) and [[knowledge-graph]] (GraphRAG; the multi-hop complement to chunk-similarity RAG, seed).
- New entity: [[greg-isenberg]] (the wiki's main founder/operator voice; same show as [[agents-are-the-new-saas]] and [[startups-for-agents]]).
- Extended with cross-links: [[self-referential-bias]] (added the operator-language framing "same model writes and grades," now named four ways), [[start-as-a-workflow]] ("draw the graph before you automate it"), [[agent-teams]] (the planner/researcher/skeptic/merge structure as an agent graph).
- Areas: [[agentic-engineering]] (+concept, +source, now 12 sources), [[rag]] (+knowledge-graph, +source, now 3), [[agent-operations]] cross-referenced.
- No new contradictions; the source is independent operator-side *confirmation* of the split-doing-from-verifying and understand-before-automating pillars. Updated [[index]] and [[synthesis]].

## [2026-08-05] ingest | Running Your Life on Codex (Jason, OpenAI Codex team)
- Source: [[running-life-on-codex]] (Jason, OpenAI Codex/DX team; local raw file, auto-caption summary). The wiki's first primary source from inside OpenAI.
- New concepts: [[heartbeat-automation]], [[personal-voice-skill]], [[skills-vs-plugins]], [[browser-use-vs-computer-use]], [[goal-plan-worklog]].
- New entities: [[codex]], [[jason-openai-codex]], [[obsidian]]; extended [[openai]] (now 3 sources).
- Extended with cross-links: [[reasoning-effort-discipline]] (OpenAI-side confirmation: medium for admin, ultra for builds), [[self-improving-agent-loop]] (the self-improve skill / bloat audit), [[taste-as-moat]] ("the only job left is to understand what you don't like and put it into words"), [[compaction-over-context-window]] (second source, other vendor), [[monorepo-for-agent-context]] (the Obsidian vault as agent memory).
- Contradictions flagged, not resolved: (1) "a lot of us don't review code anymore" vs [[read-what-the-agent-writes]] - recorded as verification relocated to executable goal oracles, not abandoned; (2) Jason rejects the [[manager-of-agents]] self-image, calling the job "articulating taste" - recorded as a metaphor split. Both added to the [[index]] Open-tensions table.
- Areas: [[agent-operations]] (+heartbeat-automation, +source, now 7), [[agentic-engineering]] (+3 concepts, +source, now 13), [[ai-career]] (+source, now 5). Updated [[index]] and [[synthesis]].

## [2026-08-21] ingest | Turning Claude into a One-Person Marketing Team (Nate Herk)
- Source: [[one-person-marketing-team]] (Nate Herk; local raw file `raw/claude-higgsfield-marketing-team.md`, auto-caption summary with its own corrections appendix). A Claude Code project driving [[higgsfield]] over MCP to produce a fictional brand's website, 18 ad creatives, a sizzle reel, 5 carousels, UGC video ads, and a creative tracker.
- **Evidence grade, stated up front:** the wiki's weakest source on distribution. Fictional brand, nothing published, no ad served, no performance data. Its durable contribution is itemized production cost and a clean statement of why an agent belongs in front of a generation tool.
- New concepts: [[own-the-context-layer]] (the source's thesis: the tool is commodity, the project holding your context is not), [[three-ps-business-context]] (Pain/Person/Promise as minimum viable context), [[agent-interviews-you-for-context]] (the `grill me` pattern), [[make-the-agent-report-its-cost]] (the four-part prompt pattern, plus the wiki's only per-asset dollar figures), [[storyboard-before-you-generate]] (character sheet then board then render).
- New entities: [[nate-herk]], [[higgsfield]].
- Extended with cross-links: [[marketing-agent]] (the definition tested and found to *exclude* this source, which is the useful result), [[test-breadth-over-conviction]] ("volume negates luck," plus the copy-separated-from-art reuse habit and the volume-without-measurement trap), [[creative-is-the-targeting]] (the Three Ps as the input format that produces routable specificity), [[design-system-not-a-design]] (a *supplied* system propagates as well as a generated one, unprompted, into an Excel file), [[ai-slop]] (context removes the generic failure and leaves the taste failure), [[building-skills]] (build the skill the moment you like one output), [[context-is-king]] (the router-plus-context-files file structure), [[unified-data-warehouse-for-agents]] (the spreadsheet version, with its performance tab empty), [[elicitation-over-prompt-engineering]] (elicitation pointed at the human), [[claude-code]] (7th source; first that uses it for no coding at all).
- **Contradictions flagged, not resolved:** (1) an agent self-QA pass that *rejected* its own defective clip, against [[self-referential-bias]]'s four-way-corroborated position - provisionally reconciled as self-review being plausible for objective defects and unreliable for quality judgments, on a single uninstrumented anecdote; (2) this source's "marketing team" satisfies none of [[marketing-agent]]'s three requirements. Both added to the [[index]] tensions table.
- **Area finding:** [[agent-operations]] now holds two marketing sources that are opposite halves of one system - Cody has the loop and the data with the context layer implicit, Nate has the context layer with neither. The union is documented nowhere. Also recorded there: generation cost has collapsed while measurement cost has not, which is now the binding constraint on every loop in the area.
- **Open question logged, not merged:** the "Nate" of [[ai-operating-system-tutorial]] (2026-07-08) is probably this Nate Herk, on framework-teaching style, audience, and subject matter. Unconfirmed - neither raw file states the earlier surname. Entity page carries the evidence; the older source's author field is annotated rather than rewritten.
- **Not ingested:** two files landed in `raw/` the same day that are outside this wiki's domain - `dodgeball_double_elim_guide.html` and `MM26_camp_scoreboard.xlsx`. Left untouched; noted in [[index]].
- Areas: [[agent-operations]] (+5 concepts, +source, now 8; index count corrected from a stale 6). Updated [[index]] and [[synthesis]].

## [2026-08-27] ingest | Your AGENTS.md is a Neural Net (Kun Chen)
- Source: [[agents-md-is-a-neural-net]] (Kun Chen; first-party blog, `blog.kunchenguid.com`, published 2026-08-22; raw file `raw/Your AGENTS.md is a Neural Net.md`). The wiki's third [[kun]] source and the first purely about maintaining the agent's memory rather than building with it. Clean prose source, no caption-correction caveats.
- New concepts: [[agents-md-as-neural-net]] (the central metaphor and the forward/backward-pass mapping), [[two-level-agent-memory]] (handwrite the user file, train the project file), [[four-bad-memory-states]] (empty/bloated/stale/drifted + the transactional-editing root), [[skills-as-release-valve]] (the budget-triage rule).
- New entity: [[backpass]] (Kun's MIT CLI that automates the backward pass; one run = one gradient step; reuses Lavish for the human-gated apply).
- **Tension resolved, not just recorded:** the [[agentic-engineering]] "do instructions compound?" question ([[building-skills]]/[[self-updating-config]] asset vs [[ablation-driven-development]] debt) gets a third position - instructions are *weights* trained within a budget. Ablation = periodic full retrain on a model release; backward pass = weekly gradient step from transcripts. Updated the tension row in both [[index]] and [[agentic-engineering]].
- **Existing pages extended:** [[self-updating-config]] (promoted seed -> developing, 2nd source; the rigorous/tooled version of Pigford's learnings-skill), [[ablation-driven-development]] (added the complementary-method note), [[principles-over-constraints]] (3rd source; the "instruction re-read every invocation" cost restated as an explicit token budget = model size), [[building-skills]] (6th source; skills reframed as the memory-budget release valve), [[skills-vs-plugins]] (the atom is also what you extract to under budget), [[kun]] entity (3rd source; **recovered his full name Kun Chen and handle/domain `kunchenguid`**, previously left deliberately blank; added backpass to his tools).
- **Identifier recovery:** the [[kun]] entity's long-standing "handle and domain not recoverable, not guessed" note is now closed by a byline - `blog.kunchenguid.com` and `github.com/kunchenguid/backpass`.
- **Reflexive note (recorded in [[synthesis]]):** the source describes exactly Mandu's own long `CLAUDE.md`/skill files, and the ingest was run from inside First Mate (Kun's orchestrator). Also a mild dent in the vendor-concentration caveat: backpass reads Claude Code, Codex, pi, opencode, grok, and Cursor transcripts, so the method is stated harness-agnostic despite being a third Kun source.
- Areas: [[agentic-engineering]] (+4 concepts in a new "Training the memory file" cluster, +source, now 14; removed a duplicate [[self-updating-config]] listing). Updated [[index]] (counts now 32 sources / 153 concepts / 31 entities) and [[synthesis]].
- **Action surfaced for hcho, not executed:** put a token budget on the global `CLAUDE.md`, lint it against [[four-bad-memory-states]], separate the handwritten user file from the trainable project files ([[two-level-agent-memory]]), and either run [[backpass]] or reproduce its budgeted backward pass by hand. Fits the already-open "audit Mandu's own configuration" thread.

## [2026-09-15] merge | Fold LLM_Evals into the canonical AI knowledge graph
- Moved the two unique raw sources and their summaries into AI_Wiki; removed seven byte-identical raw copies.
- Added [[agent-eval-and-stats]], [[ci-eval-gates-and-drift]], [[error-analysis]], [[offline-vs-online-evals]], and [[rag-evaluation]] as canonical concepts.
- Folded overlapping classification, contamination, safety, judge, and production-tooling pages into their existing canonical concepts.
- Preserved hcho's `## In my own words (hcho)` contamination section verbatim in [[data-contamination]].
- Retired the parallel `LLM_Evals/wiki/`; `LLM_Evals/` now retains only its curriculum, `Exercise/`, and `log/`.
- Updated [[evals]], [[index]], [[synthesis]], the wiki schema, and Mandu's active-wiki registry.

## [2026-09-16] ingest | Agentic App Development Workflow (Kun reconstruction)
- Source: [[kun-agentic-app-development-workflow]]; immutable raw file preserved byte-identical.
- Created source summary plus [[risk-based-agent-governance]] and [[reproducible-agent-environment]].
- Extended concepts: [[plan-code-validate]], [[one-orchestrator-agent]], [[fresh-context-review]], [[phased-implementation]], [[agent-testing-instructions]], [[ramble-then-structure]], [[design-system-not-a-design]], [[skills-as-release-valve]], [[define-the-end-to-end-gate]], [[review-plans-as-artifacts]], [[client-never-touches-the-database]].
- Updated [[kun]], [[agentic-engineering]], [[agent-operations]], and [[system-design]], plus [[index]], [[synthesis]], and this [[log]].
- Flagged secondary provenance, unavailable original URLs/dates, likely overlap with earlier Kun sources, and compiler-authored beginner recommendations.
- Qualified the server-authority connection: the wallet example does not prove a universal ban on secured client database access.
- Counts: 35 sources, 10 areas, 160 concepts, 31 entities; corrected the stale agentic-engineering index count to match its metadata plus this source.
- No daily-log pointer added: no corresponding daily log exists for 2026-09-16.

## [2026-09-23] ingest | Reviewing AI-Generated Code Safely
- Preserved `092326_agentic-code-review-guide.md` byte-identical at [[projects/Education/AI/AI_Wiki/raw/agentic-code-review-guide|the raw source]] and cleared it from the shared inbox.
- Created [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] and [[merge-ready-vs-launch-ready]].
- Extended [[risk-based-agent-governance]], [[adversarial-code-review]], [[fresh-context-review]], [[agent-testing-instructions]], and [[get-out-of-the-loop]], plus [[agentic-engineering]], [[projects/Education/AI/AI_Wiki/wiki/index|index]], and [[projects/Education/AI/AI_Wiki/wiki/synthesis|synthesis]].
- Recorded a substantive tension: automated verification does not establish a universal exemption from reading high-risk shared code.
- Source provenance remains incomplete; the compiler's examples, subjective 80/20 estimate, and AI-review superiority claim are not treated as independently verified facts.
- Corrected adversarial-code-review's pre-existing source-count omission: its body already cited building-robust-apps-with-ai, so the new count is four including this guide.
- Counts: 36 sources, 10 areas, 161 concepts, 31 entities. No corresponding daily study log exists for a pointer.

## [2026-09-23] ingest | Cross-links from Marketing's digital-brain guide
- The source is owned once in [[projects/Education/Marketing/wiki/sources/build-a-digital-brain-guide|Marketing]], with its own raw file, source summary, concepts, entity, index, synthesis, and log.
- Extended [[personal-voice-skill]] and [[ai-operating-system]] with author-endorsement and content-library scope boundaries, and updated [[projects/Education/AI/AI_Wiki/wiki/synthesis|synthesis]].
- Their source counts include the linked Marketing source; AI_Wiki's catalog count remains 36 because no duplicate summary was created here.
- Existing general-AI knowledge stays in this wiki; Home, Education, and Mandu's registry link the new Marketing subject.
