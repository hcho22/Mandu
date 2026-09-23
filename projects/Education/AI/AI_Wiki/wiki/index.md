---
type: index
last-updated: 2026-09-23
---

# Index

Content catalog of AI_Wiki.
Every page is listed once under its category with a one-line summary.
Read this first when answering a query, then drill into the linked pages.
Updated on every ingest.

Counts: 36 sources, 10 areas, 161 concepts, 31 entities.
Related subject library: [[projects/Education/Marketing/wiki/index|Marketing]], which owns the new content-source-library guide and is cross-linked rather than duplicated here.

## Areas

- [[evals]] - how you measure whether an LLM product works and keep improving it past the demo stage. (14 sources)
- [[agentic-engineering]] - building software *with* agents: direction, orchestration, verification, context, cost, and what the human is still for. (16 sources)
- [[agent-operations]] - running things *with* agents continuously: loops, routines, fleets, self-improvement, and agents pointed at distribution. (9 sources)
- [[ai-career]] - navigating an AI-native tech career: staying valuable, positioning, growth, and the forward-deployed-engineer role. (4 sources)
- [[agent-saas]] - building and selling agents as products: the business model, build ladder, and trust layer. (1 source)
- [[ml-metrics]] - classical ML evaluation metrics (ROC/AUC, precision/recall, thresholds); the foundations under evals. (1 source)
- [[system-design]] - designing robust, production-ready apps in the AI era: trade-offs, abstraction layers, security boundaries, durability. (2 sources)
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
- [[self-referential-bias]] - a model grades its own output too leniently; vary both the model and the context of the verifier.
- [[evals-saturate-and-get-replaced]] - your own product evals decay too (1-3 model generations); budget for replacement, not maintenance.
- [[offline-vs-online-evals]] - fixed pre-deploy evaluation and live production evaluation as complementary loops.
- [[error-analysis]] - read real outputs, classify bottom-up failures, and turn them into a binary rubric.
- [[rag-evaluation]] - evaluate faithfulness, answer relevance, and context precision/recall separately.
- [[agent-eval-and-stats]] - evaluate task completion, tool calls, trajectories, uncertainty, and sample size.
- [[ci-eval-gates-and-drift]] - block regressions in CI and monitor post-deploy distribution and quality drift.

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
- [[knowledge-graph]] - store entities and relationships (GraphRAG) so multi-hop answers become traversable; fixes what chunk-similarity can't connect. **Seed.**

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
- [[react-loop]] - the agent control loop: reason, act with a tool, observe, repeat.
- [[forward-deployed-engineer]] - the embedded role that pays $150K-$1M for deployment judgment plus eval rigor. **Live career target.**
- [[deployment-is-the-moat]] - intelligence is commoditized; the edge is where, how, and why you apply it.
- [[audit-eval-deployment]] - the three-phase engagement loop, with eval as the load-bearing middle stage.
- [[real-workflow-not-documented]] - the documented process is never the real one; the exceptions are the system.
- [[two-kinds-of-judgment]] - commercial plus technical, and why "good enough at both" fails.
- [[solve-for-the-exceptions]] - one way it goes right, a thousand ways it goes wrong; hcho's QA thesis restated.
- [[build-on-existing-systems]] - never force a migration off the ERP they spent millions on.
- [[do-the-job-before-the-title]] - a checkpointed 30-day spec for manufacturing the proof before applying.
- [[manager-of-agents]] - whatever you were, you manage agents now; it makes you more technical, and decisions become the bottleneck.
- [[taste-as-moat]] - as production gets cheap, encoded judgment (taste) is the durable value.
- [[t-shaped-portfolio]] - broad breadth + one deep area; what recruiters want.
- [[build-in-public]] - share unfinished work to finish, improve, and get discovered.
- [[cost-of-being-wrong]] - target domains where errors are expensive; they stay human-led longer.
- [[build-for-the-model-of-the-future]] - design for the next model generation, not today's.
- [[own-the-problem-not-the-code]] - as code gets cheap, own the domain, architecture, and definition of done.
- [[dont-let-ai-be-your-architect]] - humans own architecture, APIs, and interface; AI gets non-core areas.
- [[code-as-sawdust]] - prompts/specs are the durable artifact; code is a regenerable byproduct.
- [[read-what-the-agent-writes]] - do not exit the loop by skipping the plan; reading explainers is how you keep judgment.

### AI Operating System and agent safety
- [[ai-operating-system]] - a personal second brain you run all work through so context compounds.
- [[skills-vs-plugins]] - a skill is one capability; a plugin bundles skills + MCP servers + scripts to share.
- [[personal-voice-skill]] - a skill that writes in your voice, grounded in your own message history, tuned by audience.
- [[browser-use-vs-computer-use]] - the two automation surfaces: logged-in in-app browser vs OS/app-level control.
- [[context-is-king]] - the model is the engine, your context is the fuel; models are stateless.
- [[four-cs-framework]] - Context to Connections to Capabilities to Cadence, built in order.
- [[capabilities-not-instructions]] - remove the key; do not rely on an instruction for agent safety.
- [[phased-autonomy]] - the bike method: grant autonomy in stages, only once earned.
- [[building-skills]] - build skills forward or by reverse-engineering; evolve them every use.
- [[self-updating-config]] - a skill that mines correction history and improves its own CLAUDE.md; the same loop given discipline and a tool ([[backpass]]).
- [[principles-over-constraints]] - smarter models need fewer rules and examples; Anthropic cut its own system prompt by 80%.
- [[red-team-your-agent]] - deliberately attack your agent (prompt injection) to verify it holds.
- [[agents-md-as-neural-net]] - treat the project AGENTS.md as weights: budget = model size, session = forward pass, transcript loss drives the backward pass.
- [[two-level-agent-memory]] - handwrite the user-level file (your preferences), train the project-level file; opposite treatment.
- [[four-bad-memory-states]] - empty, bloated, stale, drifted; the transactional-append habit is the shared root cause.
- [[skills-as-release-valve]] - budget triage: broad/safety-critical stays, narrow-with-a-trigger becomes a skill, narrow-no-trigger is deleted.

### Agent operations
- [[heartbeat-automation]] - a scheduled agent that reads all your inboxes on a cadence and returns one "what needs attention" briefing.
- [[agents-as-cron-plus-markdown]] - an agent = a deterministic cron + a good skill file.
- [[agent-as-employee]] - give the agent its own identity and scoped permissions; write as itself.
- [[everything-is-a-pr]] - run a full SDLC even solo; every change is a reviewable PR.
- [[build-the-machine-first]] - build the system that does the work, then augment; inverts MVP advice.
- [[self-maintaining-codebase]] - 20-30 daily routines at Anthropic; one-sentence prompts, every routine ends in a PR.
- [[self-improving-agent-loop]] - grade real production traffic against a rubric; failures open their own fix PRs.
- [[production-watchdog]] - a daily digest of what real customers did, each line linked to the live UI.
- [[cloud-agents-over-local]] - a VM per session instead of worktrees. **Contested against local-worktree sources.**
- [[independent-agent-lab-vs-frontier-lab]] - don't build your software factory inside a frontier lab's stack.

### Business loops
- [[business-loops]] - build/measure/learn pointed at business metrics over months; the Lean Startup lineage.
- [[minimal-viable-loop]] - start with the smallest verifiable outcome, not the ambitious goal.
- [[leading-metric-over-vanity-metric]] - pick a number a single iteration can actually move.
- [[loop-cost-discipline]] - tie stop conditions to unit economics; cost scales with run frequency, not lifetime.
- [[creative-entropy]] - loops converge and stagnate silently; inject DNA from outside the loop.

### Agents pointed at distribution
- [[marketing-agent]] - the three requirements that separate an agent from an automation.
- [[unified-data-warehouse-for-agents]] - unified cross-channel data is the precondition, not the model.
- [[test-breadth-over-conviction]] - positioning is empirical; 10-20 variants before concluding.
- [[creative-is-the-targeting]] - the model reads your creative and routes it; the paid-media twin of AEO.

### The context layer in front of the tool
- [[own-the-context-layer]] - the generation tool is a commodity; the project holding your context is not.
- [[three-ps-business-context]] - Pain, Person, Promise: the minimum context that makes generated output specific.
- [[agent-interviews-you-for-context]] - install a skill that interrogates you until the tacit context is on disk.
- [[storyboard-before-you-generate]] - character sheet, then storyboard, then render; plan before the expensive step.
- [[make-the-agent-report-its-cost]] - ask for the dollar cost on every run; the cheapest instrumentation there is.

### AI-assisted build workflow
- [[merge-ready-vs-launch-ready]] - integrating gated code, exposing users, and recovering from failures are distinct readiness questions.
- [[risk-based-agent-governance]] - match verification and human authority to consequence and reversibility.
- [[reproducible-agent-environment]] - reconstructible tooling and shared onboarding, with credentials kept outside version control.
- [[graph-engineering]] - design the work as jobs, arrows, and shared state; the founder-legible name for the whole orchestration pillar, with a manual-first build ladder.
- [[goal-plan-worklog]] - the "ultra goal" triad: an agent-authored, editable goal.md with a verifiable end-state, plus plan and worklog.
- [[phased-implementation]] - research to plan to implement in small, testable phases; each phase = one PR.
- [[context-rot]] - reliability decays as context fills; start each unit of work fresh.
- [[adversarial-code-review]] - a different model (or forced self-critique) hunts for bugs in AI-written code.
- [[ship-fast-learn-from-users]] - ship in days not months; real users reveal edge cases.
- [[get-out-of-the-loop]] - don't review every line; build the automated reviewer instead.
- [[plan-code-validate]] - plan deeply, delegate coding, automate validation; plan depth buys autonomy.
- [[planning-is-removing-unknowns]] - planning is not a phase but continuous exploration; interrogate dependencies, keep implementation notes, re-spec.
- [[verification-signal-picks-the-mechanism]] - choose /loop vs /goal vs a workflow by the shape of your check, not the size of the task.
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
- [[ablation-driven-development]] - delete the whole prompt layer; add back only what repeatedly fails.
- [[product-overhang]] - capability nobody has built a product for, and the hobbling that hides it.
- [[elicitation-over-prompt-engineering]] - the durable skill: a too-hard task plus self-verification.
- [[long-horizon-agent-runs]] - days-to-weeks runs; hard task + self-executable check + stopping condition.
- [[dynamic-workflows-as-test-time-compute]] - fan out, verify, fan out; orchestration as a scaling axis.
- [[one-orchestrator-agent]] - single-threaded human interface over parallel work; steerable crewmates.
- [[review-plans-as-artifacts]] - interactive artifacts beat 351-line markdown; feedback becomes per-element.
- [[define-the-end-to-end-gate]] - a concrete E2E done-condition, stated up front, forces the plan to expose gaps.
- [[agent-over-engineering]] - agents invent env tiers, audit trails, exports; cutting them is human work.
- [[anchor-cost-in-real-pricing]] - make it search real pricing; bad numbers silently drive architecture.
- [[compaction-over-context-window]] - compaction quality beats window size. **In tension with [[context-rot]].**
- [[design-system-not-a-design]] - build the vocabulary, not the screen; let the design agent challenge the PRD.
- [[ramble-then-structure]] - exhaust the constraints; structure is cheap, completeness is not.

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
- [[boris-cherny]] - associated with Claude Code; "build for the model of the future"; author of `simplify`.
- [[tharic]] - Anthropic Claude Code team; the wiki's first primary-source voice on loops, goals, and workflows.
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
- [[kun]] - L8 principal engineer (ex-Meta/Microsoft/Atlassian); builder of First Mate, Lavish, No Mistakes; the wiki's best-documented full build session.
- [[vas]] - founder of Varick Agents; the wiki's primary source on the forward-deployed-engineer role.
- [[cody-schneider]] - marketer/builder (companiesgraph.com); agents pointed at distribution; named the entropy problem.
- [[greg-isenberg]] - founder, host of the Startup Ideas Podcast; the wiki's main founder/operator voice on agents; coined the wiki's [[graph-engineering]] framing.
- [[codex]] - OpenAI's agentic coding tool (ChatGPT Work is a UX view on it); the wiki's best-documented non-Anthropic agent stack.
- [[jason-openai-codex]] - OpenAI Codex / DX team; first primary source from inside OpenAI; runs his life on Codex; rejects the "manager of agents" framing.
- [[obsidian]] - local-first markdown notes app; in the wiki, a structured markdown store an agent reads for context (hcho's own tool of record).
- [[nate-herk]] - AI automation creator teaching non-coders; the wiki's least technical voice, and unusually candid about his own output.
- [[higgsfield]] - multi-model image/video aggregator with a Marketing Studio; driven over MCP rather than through its own UI.
- [[backpass]] - Kun's MIT CLI that trains a project's AGENTS.md from agent session transcripts, one gradient step per run.

## Sources

- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - supplied beginner guide on risk-based review, current-revision evidence, independent scrutiny, and gated rollout; original speaker and video metadata unknown.
- [[kun-agentic-app-development-workflow]] - local reconstruction of four Kun talks; intent, architecture, isolated integrated slices, independent validation, reproducibility, and fleet coordination. Secondary and overlapping evidence, with beginner adaptations marked.
- [[your-ai-product-needs-evals]] - Hamel Husain (2024-03-29): the three-level eval framework and why evals unlock iteration.
- [[ai-evals-error-analysis]] - Peter Yang with Hamel Husain and Shreya Shankar: human-led error discovery, narrow binary judges, and automated-evaluator precision.
- [[agents-are-the-new-saas]] - Startup Ideas Podcast: an 8-part playbook for building and selling agent-SaaS.
- [[ai-era-50-career-tips]] - Meta Staff Engineer / creator: 50 tips for an AI-era career (judgment, taste, agentic-tool mastery).
- [[ai-operating-system-tutorial]] - Nate: building a personal AI OS / second brain in Claude Code (Four C's, agent safety, skills).
- [[ai-skill-from-scratch]] - Peter (Behind the Craft): a 5-step method for building a self-checking skill with an eval loop and memory.
- [[building-5-ai-products-solo]] - Josh Pigford: an AI-assisted solo-build workflow (phased worktrees, cross-model review, self-updating config, ship fast).
- [[one-person-company-with-agents]] - Ryan Carson: running a whole company on agents (cron + markdown, agents-as-employees, build the machine first).
- [[building-products-with-agents]] - solo L8 builder: get out of the loop, plan-code-validate, fresh-context review (Lavish / No Mistakes).
- [[classification-roc-and-auc]] - Google ML Crash Course: ROC/AUC and evaluating a classifier across thresholds.
- [[classification-accuracy-precision-recall]] - Google ML Crash Course: confusion-matrix metrics at one threshold and why accuracy fails under class imbalance.
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
- [[designing-loops-and-workflows]] - Tharic (Anthropic Claude Code team) with Peter Yang: the first primary-source account of /loop, /goal, and workflows - pick the mechanism by your verification signal, split the verifier from the producer, and cut your instructions.
- [[building-at-the-frontier]] - Boris Cherny (Anthropic, creator of Claude Code): ablation, product overhang, elicitation, 11-day and 15-day autonomous rewrites, dynamic workflows as a compute axis, and Claude maintaining Anthropic's own codebases.
- [[running-teams-of-ai-agents]] - Ryan Carson (Untangle), post-PMF: cloud agent fleets, three production automations, decision throughput as the bottleneck, and don't build your factory inside a frontier lab's stack.
- [[agentic-full-stack-build]] - Kun: an entire full-stack app built without reading source code, with the two human interventions isolated (cost anchoring and invented scope).
- [[fde-in-30-days]] - Vas (Varick Agents): the forward-deployed-engineer role, Audit → Eval → Deployment, and a 30-day case-study roadmap. **The most career-actionable source in the wiki.**
- [[loops-to-run-your-business]] - the loop primitive pointed at SEO, ads, and product KPIs over months rather than at a codebase over minutes.
- [[building-marketing-agents]] - Cody Schneider: the deepest technical account of a non-engineering agent, plus the under-discussed entropy problem.
- [[graph-engineering-isenberg]] - Greg Isenberg: "graph engineering" as the work-design layer above prompt/context; agent graphs vs knowledge graphs; a manual-to-automated build ladder.
- [[running-life-on-codex]] - Jason (OpenAI Codex): running work and life on Codex/ChatGPT Work - heartbeat automations, skills vs plugins, browser vs computer use, goal/plan/worklog, and taste as the remaining skill; the wiki's first inside-OpenAI source.
- [[one-person-marketing-team]] - Nate Herk: a Claude Code project driving Higgsfield to produce a brand's full asset set. **The wiki's weakest evidence on distribution and its only itemized creative-production costs.** Fictional brand, nothing published.
- [[agents-md-is-a-neural-net]] - Kun Chen: treat the project AGENTS.md as a neural net you train from session transcripts (weights, budget, forward/backward pass); ships [[backpass]] (MIT). The wiki's third Kun source and its first on maintaining the agent's memory rather than building with it.

## Pending pages (linked, not yet written)

None currently - all previously-pending link markers have been written.

## Open tensions to watch

The 2026-08-01 batch introduced real disagreements between sources. They are recorded on the pages rather than resolved, and are worth revisiting as new sources land.

| Question | Positions | Where |
|---|---|---|
| **Does passing verification replace all code reading?** | [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] retains deep human review for shared or consequential changes, qualifying broad automation claims in [[get-out-of-the-loop]]. | [[risk-based-agent-governance]] |
| **Does context degrade as it fills?** | [[context-rot]] says start fresh; [[compaction-over-context-window]] reports four clean compactions | [[agentic-engineering]] |
| **Local or cloud agents?** | [[cloud-agents-over-local]] vs the local worktrees of [[building-5-ai-products-solo]] and [[inside-conductor-workflow]] | [[agent-operations]] |
| **Is orchestration scaffolding necessary?** | [[verification-signal-picks-the-mechanism]] gives a selection rule; [[building-at-the-frontier]] says `/go` and `/loop` are "helpful but not required" now | [[agentic-engineering]] |
| **Do evals compound?** | The [[evals]] area treats the suite as the compounding asset; [[evals-saturate-and-get-replaced]] gives it a 1-3 generation half-life | [[evals]] |
| **Do instructions compound?** | [[building-skills]] and [[self-updating-config]] treat them as an asset; [[ablation-driven-development]] treats them as debt; [[agents-md-as-neural-net]] calls them weights trained within a budget (ablation = full retrain, backward pass = weekly step) | [[agentic-engineering]] |
| **Is prompt injection still the threat model?** | [[red-team-your-agent]] assumes yes; [[building-at-the-frontier]] says Opus 5 is not demonstrably injectable, with caveats | [[red-team-your-agent]] |
| **Do you still read the agent's code?** | [[read-what-the-agent-writes]] says reading is how you keep judgment; [[running-life-on-codex]] says "a lot of us don't review code anymore" - verification moved onto verifiable-goal oracles, not abandoned | [[read-what-the-agent-writes]] |
| **Manager, or director of taste?** | [[manager-of-agents]] (Ryan Carson, Cody Schneider) says you manage agents now; [[running-life-on-codex]] (Jason, OpenAI) rejects the manager frame and calls the job articulating taste | [[manager-of-agents]] |
| **Vendor concentration** | The input diet is heavily Claude Code-centric; [[independent-agent-lab-vs-frontier-lab]] is the first counter-position, and [[running-life-on-codex]] (2026-08-05) is the first inside-OpenAI source - it reports the *same* patterns, which is itself the finding | - |
| **Can an agent usefully check its own output?** | [[self-referential-bias]] says no, four ways over; [[one-person-marketing-team]] shows a self-QA pass that rejected a real defect - provisionally reconciled as objective defects yes, quality judgments no | [[self-referential-bias]] |
| **What counts as a marketing agent?** | [[marketing-agent]]'s three requirements (data, cadence, infrastructure) exclude the "marketing team" of [[one-person-marketing-team]] entirely; the two sources are opposite halves of one unbuilt system | [[marketing-agent]] |

## Structural note (2026-08-01)

The 2026-07-28 plan to graduate `agentic-engineering` from a concept to an area **has been executed**, after the queued batch of agent-workflow sources landed.
It is now [[agentic-engineering]] (area, 11 sources), and a sibling area [[agent-operations]] was created to hold the distinct activity of running things with agents continuously rather than building software with them.
The boundary between them is documented at the top of [[agent-operations]].

`raw/` has no unprocessed AI sources from the LLM_Evals merge.

## Raw inbox status (2026-09-16)

All canonical AI-engineering sources currently in `raw/` have source summaries, including the new local Kun workflow guide ingested on 2026-09-16.
The 2026-09-15 LLM_Evals merge added two unique raw sources and removed seven byte-identical copies.

Two files added to `raw/` on 2026-08-21 are **not wiki material and were deliberately not ingested**: `dodgeball_double_elim_guide.html` (a tournament station guide) and `MM26_camp_scoreboard.xlsx` (a camp scoreboard).
They are outside this wiki's domain entirely and appear to have been filed here by accident.
They have been left untouched pending a decision on where they belong.
