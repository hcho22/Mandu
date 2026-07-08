---
type: index
last-updated: 2026-07-08
---

# Index

Content catalog of AI_Wiki.
Every page is listed once under its category with a one-line summary.
Read this first when answering a query, then drill into the linked pages.
Updated on every ingest.

Counts: 21 sources, 8 areas, 96 concepts, 20 entities.

## Areas

- [[evals]] - how you measure whether an LLM product works and keep improving it past the demo stage. (3 sources)
- [[agent-saas]] - building and selling agents as products: the business model, build ladder, and trust layer. (1 source)
- [[ai-career]] - navigating an AI-native tech career: staying valuable, positioning, and growth. (1 source)
- [[ml-metrics]] - classical ML evaluation metrics (ROC/AUC, precision/recall, thresholds); the foundations under evals. (1 source)
- [[system-design]] - designing robust, production-ready apps in the AI era: trade-offs, abstraction layers, security boundaries, durability. (1 source)
- [[agentic-web]] - building for a web where AI agents are the customer: the machine-to-machine economy, agent infrastructure, and AEO. (1 source)
- [[rag]] - retrieval-augmented generation: giving models a library to look things up in; the technical core of hcho's flagship. (2 sources)
- [[production-llm]] - the seven patterns that turn an LLM demo into a product: evals, RAG, fine-tuning, caching, guardrails, defensive UX, feedback. (1 source)

## Concepts

### Evals
- [[three-level-eval-framework]] - L1 unit tests / L2 human and model eval / L3 A/B testing, sequenced by product maturity.
- [[llm-unit-tests]] - Level 1: cheap assertions run in CI on every change.
- [[llm-as-judge]] - model-based evaluation, validated against human labels (precision/recall, not raw agreement).
- [[looking-at-your-data]] - remove all friction from inspecting traces; the connective habit of the eval discipline.
- [[pass-fail-over-score-evals]] - prefer binary checks over 1-5 scores when a model is the grader.
- [[skill-eval-loop]] - self-checking loop: a separate grader runs pass/fail checks until output passes.
- [[eval-driven-development]] - build task-specific evals first; run them on every change (test-first for LLMs).
- [[reference-based-metrics]] - BLEU/ROUGE/BERTScore and why they mislead on open-ended tasks.
- [[benchmark-sensitivity]] - the same model scores differently across benchmark implementations; leaderboards aren't comparable.
- [[three-eval-methods]] - automated benchmarks, human as judge, model as judge; how each fails.
- [[purposes-of-evaluation]] - the three reasons to evaluate (non-regression, ranking, capability), usually conflated.
- [[data-contamination]] - eval data leaking into training inflates scores that don't generalize.
- [[evaluation-criteria]] - the four buckets: domain-specific capability, generation, instruction-following, cost/latency.
- [[factual-consistency]] - hallucination detection (local vs global; NLI, SelfCheckGPT, SAFE); the central RAG metric.
- [[model-build-vs-buy]] - self-host open-weight vs commercial API, along seven axes.
- [[evaluation-pipeline]] - assembling methods into a reliable, sliced, business-tied, reproducible pipeline.
- [[benchmark-saturation]] - a benchmark near the ceiling loses discriminative power; decay partner of contamination.
- [[functional-scorers]] - rule-based verifiers (IFEval-style); the interpretable, cheap default over model judges.
- [[score-reproducibility]] - the full checklist of why a reported benchmark score won't reproduce.
- [[contamination-detection]] - the three flavors and five methods for catching benchmark contamination.

### Agent SaaS
- [[agent-saas-sells-work]] - sell the job that disappears, not the tool; the market is labor, not seats.
- [[workflow-with-a-paycheck]] - pick a workflow worth automating: 5 traits + a scoring rubric.
- [[seven-part-agent-spec]] - trigger, context, tools, allowed, approval, escalation, success.
- [[minimal-useful-agent]] - build the smallest useful agent; the draft-to-act ladder.
- [[start-as-a-workflow]] - Anthropic's principle: begin predictable, earn autonomy.
- [[product-wrapper]] - logs, approvals, and a control room create the trust that makes it SaaS.
- [[outcome-based-pricing]] - sell pilots like labor, then productize the repeatable parts.

### Agentic web
- [[agent-native-rebuild]] - every tool category gets an agent-native version; "what's the agent version of this?"
- [[agent-buying-journey]] - the six-stage agent funnel (find, evaluate, trust, transact, use, recommend).
- [[agent-building-blocks]] - what every agent needs: identity, tools, inbox, memory, wallet, receipts.
- [[agent-readable-website]] - expose docs/schemas/endpoints (MCP, SDKs, OAuth, /agents) or be invisible to agents.
- [[aeo-answer-engine-optimization]] - SEO becomes AEO; forms->tool calls, docs->executable support, analytics->agent analytics.

### RAG
- [[retrieval-augmented-generation]] - the chunk -> embed -> store -> retrieve -> ground pipeline, and why it exists.
- [[retrieval-is-the-bottleneck]] - most RAG failures are retrieval failures, not model failures; debug what got retrieved first.
- [[embeddings]] - text as vectors; model choice and ANN indices are upstream of retrieval quality.
- [[hybrid-retrieval]] - combine keyword (BM25) and semantic search; each covers the other's blind spots.

### Production LLM
- [[fine-tuning]] - LoRA/QLoRA, RLHF, the alignment tax; reach for it last, after prompting and retrieval.
- [[guardrails]] - validate input and output for structure, safety, and factuality.
- [[semantic-caching]] - reuse prior generations to cut latency/cost; cache safely, not on similarity alone.
- [[defensive-ux]] - design for the model being wrong: set expectations, easy dismissal, attribution, familiarity.
- [[data-flywheel]] - collect explicit/implicit feedback; data is one of the few LLM moats.

### AI Career and craft
- [[ai-engineer-is-a-builder]] - the growing AI-engineer role builds on existing models; no PhD/transformer-math required.
- [[switchers-edge]] - the bar moved from credential to owned-outcome judgment, which career switchers already have.
- [[career-switch-mistakes]] - the four that end switches in week two; antidote is skill-first/build-first/tool-agnostic/public.
- [[single-call-workflow-or-agent]] - pick the least-powerful architecture that works; knowing when NOT to use an agent.
- [[agentic-engineering]] - the new expertise: context engineering, agentic validations, agentic tooling, compound engineering.
- [[react-loop]] - the agent control loop: reason, act with a tool, observe, repeat.
- [[taste-as-moat]] - as production gets cheap, encoded judgment (taste) is the durable value.
- [[t-shaped-portfolio]] - broad breadth + one deep area; what recruiters want.
- [[build-in-public]] - share unfinished work to finish, improve, and get discovered.
- [[cost-of-being-wrong]] - target domains where errors are expensive; they stay human-led longer.
- [[build-for-the-model-of-the-future]] - design for the next model generation, not today's.
- [[own-the-problem-not-the-code]] - as code gets cheap, own the domain, architecture, and definition of done.
- [[dont-let-ai-be-your-architect]] - humans own architecture, APIs, and interface; AI gets non-core areas.
- [[code-as-sawdust]] - prompts/specs are the durable artifact; code is a regenerable byproduct.

### AI Operating System and agent safety
- [[ai-operating-system]] - a personal second brain you run all work through so context compounds.
- [[context-is-king]] - the model is the engine, your context is the fuel; models are stateless.
- [[four-cs-framework]] - Context to Connections to Capabilities to Cadence, built in order.
- [[capabilities-not-instructions]] - remove the key; do not rely on an instruction for agent safety.
- [[phased-autonomy]] - the bike method: grant autonomy in stages, only once earned.
- [[building-skills]] - build skills forward or by reverse-engineering; evolve them every use.
- [[self-updating-config]] - a skill that mines correction history and improves its own CLAUDE.md.
- [[red-team-your-agent]] - deliberately attack your agent (prompt injection) to verify it holds.

### Agent operations
- [[agents-as-cron-plus-markdown]] - an agent = a deterministic cron + a good skill file.
- [[agent-as-employee]] - give the agent its own identity and scoped permissions; write as itself.
- [[everything-is-a-pr]] - run a full SDLC even solo; every change is a reviewable PR.
- [[build-the-machine-first]] - build the system that does the work, then augment; inverts MVP advice.

### AI-assisted build workflow
- [[phased-implementation]] - research to plan to implement in small, testable phases; each phase = one PR.
- [[context-rot]] - reliability decays as context fills; start each unit of work fresh.
- [[adversarial-code-review]] - a different model (or forced self-critique) hunts for bugs in AI-written code.
- [[ship-fast-learn-from-users]] - ship in days not months; real users reveal edge cases.
- [[get-out-of-the-loop]] - don't review every line; build the automated reviewer instead.
- [[plan-code-validate]] - plan deeply, delegate coding, automate validation; plan depth buys autonomy.
- [[fresh-context-review]] - review AI work in a clean context window; a biased reviewer misses bugs.
- [[agent-testing-instructions]] - write "how I would test this" E2E instructions; agents default to shallow tests.
- [[sub-agents]] - delegate heavy exploration to child agents that return only conclusions.
- [[agent-teams]] - agents that debate through persona panels until they agree (vs parallel sub-agents).
- [[checkpoint-rewind]] - roll code + conversation back to a checkpoint instead of piling corrections.
- [[slop-free-zones]] - human-guaranteed sections where every line is human-reviewed; the counterweight to full automation.
- [[model-selection]] - Opus for creative/new work, Codex for grinding; rate models on intelligence/taste/cost in a config glossary.
- [[model-routing]] - one model orchestrates and "shells out" to a cheaper/specialized model for the grunt work.
- [[reasoning-effort-discipline]] - keep effort at "high"; x-high/max over-reason and over-charge. The biggest cost lever.
- [[time-to-fix-as-health-signal]] - read agent time-to-fix + files-touched as a codebase-health diagnostic.

### Production agent infrastructure
- [[managed-agent-primitives]] - agents, environments, sessions, events; a production agent-infra model.
- [[outcome-rubric-iteration]] - attach a rubric; the agent loops and self-checks until it passes.
- [[agent-observability]] - live-debug agent runs: events, tool-call timing, multi-agent coordination.
- [[credential-vaults]] - inject secrets so they never enter the model's context.

### System design
- [[engineering-trade-offs]] - every design balances scalability, reliability, performance, and cost; no perfect system.
- [[everything-as-code-abstractions]] - rising abstraction layers agents can operate in code; why the modern stack is agent-friendly.
- [[monorepo-for-agent-context]] - one repo so the agent sees the whole system at once.
- [[client-never-touches-the-database]] - the client -> server -> DB security rule.
- [[durable-agent-processes]] - durable execution + queues, because an agent can't stop when the tab closes.

### ML metrics
- [[roc-and-auc]] - classifier performance across all thresholds; AUC as ranking probability.
- [[precision-recall]] - precision, recall, and PR curves for imbalanced data; the rigor behind eval caveats.
- [[classification-threshold]] - set the operating point by the cost of false positives vs false negatives.
- [[ai-slop]] - the checkable low-quality signature of unedited AI output (text and design); what taste removes.

## Entities

- [[hamel-husain]] - ML consultant; foundational voice on LLM evals.
- [[eugene-yan]] - applied/ML engineer and writer; landmark LLM-systems patterns; foundational voice on evals + production LLM.
- [[clementine-fourrier]] - Hugging Face; leads evaluation + leaderboards; benchmarking-side eval authority.
- [[chip-huyen]] - author of AI Engineering / Designing ML Systems; the end-to-end eval + AI-systems reference.
- [[huggingface]] - open-source AI platform; Open LLM Leaderboard, MTEB, OpenEvals; hub of rigorous benchmarking.
- [[anthropic]] - maker of Claude / Claude Code; source of the "start as a workflow, earn autonomy" agent guidance.
- [[andrej-karpathy]] - AI engineer/educator; frames tool-use as a real skill gap.
- [[boris-cherny]] - associated with Claude Code; "build for the model of the future."
- [[claude-code]] - Anthropic's agentic coding tool; substrate for agentic engineering and the AI OS.
- [[openai]] - maker of GPT / Codex; the common cross-checking model in multi-model workflows.
- [[josh-pigford]] - serial solo founder (sold Baremetrics); builds 5 AI products in parallel with agents.
- [[conductor]] - agent-orchestration tool: model switching + automated parallel worktrees.
- [[google]] - maker of Gemini; multimodal (video/image) tasks and the Workspace ecosystem.
- [[ryan-carson]] - solo founder (Untangled); runs a one-person company with agents.
- [[open-claw]] - open-source agent platform run as a personal chief-of-staff.
- [[devin]] - cloud-only engineering agent; VM per task, playbooks, reliable browser testing.
- [[opencode]] - open-source agent harness; easy model-switching.
- [[theo-t3]] - developer/YouTuber; builder of T3 Code; cost-aware Fable 5 + Claude Code workflow.
- [[ross-hey-fabrica]] - developer/agency founder; builder of Pluto; teaches agentic system design.
- [[convex]] - everything-as-code backend + database platform; Pluto's control plane.

## Sources

- [[your-ai-product-needs-evals]] - Hamel Husain (2024-03-29): the three-level eval framework and why evals unlock iteration.
- [[agents-are-the-new-saas]] - Startup Ideas Podcast: an 8-part playbook for building and selling agent-SaaS.
- [[ai-era-50-career-tips]] - Meta Staff Engineer / creator: 50 tips for an AI-era career (judgment, taste, agentic-tool mastery).
- [[ai-operating-system-tutorial]] - Nate: building a personal AI OS / second brain in Claude Code (Four C's, agent safety, skills).
- [[ai-skill-from-scratch]] - Peter (Behind the Craft): a 5-step method for building a self-checking skill with an eval loop and memory.
- [[building-5-ai-products-solo]] - Josh Pigford: an AI-assisted solo-build workflow (phased worktrees, cross-model review, self-updating config, ship fast).
- [[one-person-company-with-agents]] - Ryan Carson: running a whole company on agents (cron + markdown, agents-as-employees, build the machine first).
- [[building-products-with-agents]] - solo L8 builder: get out of the loop, plan-code-validate, fresh-context review (Lavish / No Mistakes).
- [[classification-roc-and-auc]] - Google ML Crash Course: ROC/AUC and evaluating a classifier across thresholds.
- [[production-agent-with-cma]] - Anthropic workshop: building on Claude Managed Agents (primitives, outcomes, vaults, observability).
- [[every-claude-feature-ranked]] - 500-hour tier-ranking of Claude features (Skills #1; a broad tour of the ecosystem).
- [[inside-conductor-workflow]] - Conductor co-founder: voice-first parallel orchestration; slop-free zones; code-as-sawdust.
- [[working-with-fable-5]] - Theo (T3): cost-min-maxing (reasoning effort + model routing) and a live run shipping a month of work in ~5.5h for ~$150.
- [[building-robust-apps-with-ai]] - Ross (Hey Fabrica): production system design taught through the Pluto agent-product architecture.
- [[startups-for-agents]] - Startup Ideas Podcast: the agentic web (agents as customers), agent infrastructure, and SEO->AEO.
- [[zero-to-hireable-ai-engineer]] - @free_ai_guides: a build-first four-month path from zero to hireable AI engineer, with market data.
- [[llm-patterns]] - Eugene Yan: the seven patterns for building LLM products (evals, RAG, fine-tuning, caching, guardrails, defensive UX, feedback).
- [[lets-talk-about-llm-evaluation]] - Clémentine Fourrier (HF): the three eval methods, three purposes, and data contamination.
- [[evaluate-ai-systems]] - Chip Huyen (AI Engineering Ch. 4): evaluation criteria, model selection/build-vs-buy, contamination, and designing an evaluation pipeline.
- [[llm-evaluation-guidebook]] - Fourrier et al. (OpenEvals/HF): the exhaustive eval guidebook - saturation, reproducibility, functional scorers, judge biases, and creating your own eval.
- [[what-is-a-contaminated-llm]] - Jonathan Chavez (llm-stats): the contamination deep-dive - the Codeforces cliff, five detection methods, famous cases, and the 2026 resistant stack.

## Pending pages (linked, not yet written)

None currently - all previously-pending link markers have been written.
