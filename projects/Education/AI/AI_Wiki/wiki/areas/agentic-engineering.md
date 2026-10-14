---
type: area
tags: [agentic-engineering, agents, craft, tooling, orchestration, verification]
status: established
source-count: 20
last-updated: 2026-10-14
---

# Agentic Engineering

The durable hub for **building software with agents**: how you direct them, how you verify their work, how you manage context and cost, and what the human is still for.

Graduated from a concept page to an area on 2026-08-01, after the batch of five agent-workflow sources ingested that day.
The plan recorded in [[index]] on 2026-07-28 was to shape the hub once from the full evidence rather than reshaping it after each source, and that is what this page is.

## Why it matters

Named in [[ai-era-50-career-tips]] as one of the most important new skills, and the claim there was that tool mastery alone can get you hired.
Two years of sources later, the more defensible version is narrower and more interesting: as models improve, **the leverage moves out of writing code and into designing the verification loop the model runs against.**

## The four pillars, and what the evidence did to them

The original framing (from [[ai-era-50-career-tips]]) was context engineering, agentic validations, agentic tooling, and compound engineering.
The sources have not overturned it, but they have reordered it.

- **Agentic validations turned out to be upstream, not downstream.**
[[verification-signal-picks-the-mechanism]] says the shape of your check decides which orchestration primitive you can use.
[[elicitation-over-prompt-engineering]] says verification is "the single most important thing that people do not get right."
[[long-horizon-agent-runs]] shows an 11-day autonomous rewrite that worked only because a mature test suite existed.
**What you can measure determines what you can automate**, so the eval skill gates the agentic-engineering skill rather than polishing it.
- **Context engineering is being absorbed by the harness.**
[[principles-over-constraints]] and [[ablation-driven-development]] say most instructions are debt against a model that no longer exists.
[[compaction-over-context-window]] says window management is becoming an implementation detail, contradicting [[context-rot]].
What survives is [[ramble-then-structure]] (say the constraints, not the structure) and persisting state to files.
- **Compound engineering got a scaling story.**
[[dynamic-workflows-as-test-time-compute]] reframes orchestration as a way to spend more compute on one problem, not as a convenience.
- **Agentic tooling** remains the least-changed pillar; the [[react-loop]] is still the mechanism.

## Concepts in this area

### Direction and prompting
- [[elicitation-over-prompt-engineering]] - the durable skill: a too-hard task plus self-verification.
- [[ablation-driven-development]] - delete everything, add back only repeated failures.
- [[principles-over-constraints]] - smarter models need fewer rules; Anthropic cut its system prompt 80%.
- [[product-overhang]] - capability nobody has built a product for, and the hobbling that hides it.
- [[ramble-then-structure]] - exhaust the constraints; let the agent impose structure.
- [[build-for-the-model-of-the-future]] - design for the next generation, not today's.
- [[delegate-the-problem-not-the-solution]] - bring the agent in when you start thinking; its failure tells you the problem deserves your attention.

### Training the memory file
- [[agents-md-as-neural-net]] - treat the project `AGENTS.md` as weights: budget, forward pass, loss, backward pass.
- [[two-level-agent-memory]] - handwrite the user-level file, train the project-level one; opposite treatment.
- [[four-bad-memory-states]] - empty, bloated, stale, drifted, and the transactional-editing root cause.
- [[skills-as-release-valve]] - the budget-triage rule for what stays, what becomes a skill, and what gets deleted.
- [[self-updating-config]] - a skill that mines corrections and improves its own config; the same loop, given discipline and a tool ([[backpass]]).

### Planning and review
- [[planning-is-removing-unknowns]] - planning as continuous exploration, not a phase.
- [[goal-plan-worklog]] - the "ultra goal" triad: an agent-authored, editable goal.md with a verifiable end-state, plus plan and worklog.
- [[plan-code-validate]] - plan deeply, delegate coding, automate validation.
- [[phased-implementation]] - research to plan to implement in small testable phases.
- [[review-plans-as-artifacts]] - interactive artifacts beat 351-line markdown, because feedback becomes per-element.
- [[read-what-the-agent-writes]] - don't exit the loop by skipping the plan.
- [[fresh-context-review]] - review in a clean context; a biased reviewer misses bugs.
- [[adversarial-code-review]] - a different model hunts for bugs in AI-written code.

### Orchestration
- [[graph-engineering]] - designing the work as jobs, arrows, and shared state; the founder-legible name for this whole pillar, with a manual-first build ladder.
- [[dynamic-workflows-as-test-time-compute]] - fan out, verify, fan out; a new scaling axis.
- [[verification-signal-picks-the-mechanism]] - pick /loop vs /goal vs a workflow by the shape of your check.
- [[sub-agents]] - delegate heavy exploration to children that return conclusions.
- [[one-orchestrator-agent]] - single-threaded human interface over parallel work; steerable crewmates over spawned sub-agents.
- [[agent-threads-as-inbox]] - many threads, surfaced only when done or blocked; cleared like an email inbox.
- [[agent-teams]] - persona panels that debate until they agree.
- [[long-horizon-agent-runs]] - days-to-weeks runs, and the three ingredients that enable them.

### Verification and the human's remaining job
- [[merge-ready-vs-launch-ready]] - integration, user exposure, and operational recovery need distinct evidence.
- [[feature-gating-from-day-one]] - gate every feature while planning; rollback ability is what licenses a lighter review later.
- [[proof-in-the-pr]] - the agent attaches tests, logs, screenshots, and confidence levels so the reviewer reads evidence before code.
- [[define-the-end-to-end-gate]] - a concrete E2E done-condition, stated up front, forces the plan to expose gaps.
- [[agent-testing-instructions]] - agents default to shallow tests; write how you would test it.
- [[get-out-of-the-loop]] - don't review every line; build the automated reviewer.
- [[agent-over-engineering]] - agents invent env tiers, audit trails, and exports; cutting them is human work.
- [[anchor-cost-in-real-pricing]] - make it search real pricing; bad numbers silently drive architecture.
- [[slop-free-zones]] - human-guaranteed sections as the counterweight to full automation.
- [[dont-let-ai-be-your-architect]] - humans own architecture, APIs, and interface.

### Context and cost
- [[compaction-over-context-window]] - compaction quality beats raw window size; the file system is the memory.
- [[context-rot]] - reliability decays as context fills. **In tension with the above; see below.**
- [[checkpoint-rewind]] - roll code and conversation back instead of piling corrections.
- [[model-selection]] - match model tier to task; a full production build ran on a non-frontier model.
- [[model-routing]] - orchestrate with one model, shell out to a cheaper one.
- [[reasoning-effort-discipline]] - keep effort at high; x-high over-reasons and over-charges.
- [[subscription-vs-api-tokens]] - metered billing rewards thrift, an expiring flat allowance rewards utilization; know which regime a workload is in.
- [[time-to-fix-as-health-signal]] - read agent time-to-fix as a codebase-health diagnostic.

### Artifacts and craft
- [[building-skills]] - build skills forward or by reverse-engineering.
- [[skills-vs-plugins]] - a skill is one capability; a plugin bundles skills + MCP servers + scripts to share.
- [[personal-voice-skill]] - a skill that writes in your voice, grounded in your own message history, tuned by audience.
- [[browser-use-vs-computer-use]] - the two automation surfaces (logged-in web vs OS/app level) and when each applies.
- [[design-system-not-a-design]] - a vocabulary, not a screen; let the design agent challenge the PRD.
- [[code-as-sawdust]] - prompts and specs are durable; code is a regenerable byproduct.
- [[ship-fast-learn-from-users]] - ship in days; real users reveal edge cases.
- [[ai-slop]] - the checkable signature of unedited AI output.

## Sources

- [[agentic-coding-workflow-idea-to-review]] - uncredited playbook merging John's two talks with the Kun reconstruction into 11 gated phases, with a three-tier risk table and the Claude Code and Codex commands checked on 2026-10-12. Third-order; no new primary evidence.
- [[stop-prompting-design-loops-and-goals]] - John (Meta): attention as the bottleneck, loops and goals with agent-verifiable exit criteria, and a 22-hour goal enabled by tooling, context, and design screens; review becomes the next bottleneck.
- [[agentic-code-review-strategies]] - John (Meta): review depth as a gradient set by blast radius, gates from day one, proof in every PR, a fresh-context reviewer, and merge-ready is not launch-ready. Most likely the same talk as the guide below.
- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - derived guide on blast radius, requirement-linked evidence, independent review, feature gates, and gradual release; original speaker and video details missing.
- [[kun-agentic-app-development-workflow]] - local secondary reconstruction of four talks, with explicitly identified beginner adaptations.
- [[ai-era-50-career-tips]] - names the discipline and its four pillars.
- [[designing-loops-and-workflows]] - Tharic (Anthropic): the first primary source; mechanism selection, self-referential bias, planning as unknown-removal.
- [[building-at-the-frontier]] - Boris Cherny (Anthropic): ablation, overhang, elicitation, 11-day and 15-day runs, dynamic workflows as a compute axis.
- [[agentic-full-stack-build]] - Kun: an entire full-stack build with the three human interventions isolated.
- [[building-products-with-agents]] - Kun: the principles behind that build.
- [[building-5-ai-products-solo]] - Josh Pigford: phased local worktrees, cross-model review, context rot.
- [[inside-conductor-workflow]] - Conductor: voice-first parallel orchestration, slop-free zones.
- [[working-with-fable-5]] - Theo: cost min-maxing via reasoning effort and model routing.
- [[token-maxing-with-agents]] - Theo again: flat-rate subscriptions as the funding model, verification as 85-90% of spend, problem-first delegation, and threads as an inbox.
- [[every-claude-feature-ranked]] - the broad feature tour of the ecosystem.
- [[production-agent-with-cma]] - Anthropic: production agent primitives and outcome rubrics.
- [[building-robust-apps-with-ai]] - Ross: why agent-operable infra makes any of this possible.
- [[graph-engineering-isenberg]] - Greg Isenberg: names the work-design layer ("graph engineering") for a founder audience; independent operator-side confirmation of the split-doing-from-verifying and understand-before-automating pillars.
- [[running-life-on-codex]] - Jason (OpenAI Codex): the OpenAI-side practitioner account - skills/plugins, browser vs computer use, the goal/plan/worklog build workflow, effort discipline, and taste as the remaining skill; the wiki's first non-Anthropic confirmation that these practices are converging across vendors.
- [[agents-md-is-a-neural-net]] - Kun: treat the project memory file as weights and train it from session transcripts; the discipline behind [[self-updating-config]] and the tool ([[backpass]]) that runs it.

## Open tensions

The area is not internally consistent, and the disagreements are the interesting part.

| Question | Positions |
|---|---|
| **Can humans stop reading code?** | [[get-out-of-the-loop]] favors automated replacement of review; [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] reserves deep human inspection for consequential shared behavior. Review depth depends on risk, not merely passing checks. [[agentic-code-review-strategies]] (2026-10-14) names the speaker, who reads more code than before and lets rollback ability decide the depth. |
| **Does context degrade?** | [[context-rot]] says start fresh; [[compaction-over-context-window]] reports four clean compactions. Probably capacity versus contamination, but unresolved. |
| **Is orchestration scaffolding necessary?** | [[verification-signal-picks-the-mechanism]] gives a selection rule; [[building-at-the-frontier]] says `/go` and `/loop` are "helpful but not required" now. Likely a model-tier difference. [[stop-prompting-design-loops-and-goals]] calls loops and goals "pretty interchangeable" while using them for different jobs. |
| **Local or cloud?** | [[cloud-agents-over-local]] versus the local worktrees of [[building-5-ai-products-solo]] and [[inside-conductor-workflow]]. Filed under [[agent-operations]]. |
| **More agents or fewer?** | [[dynamic-workflows-as-test-time-compute]] scales to thousands; [[designing-loops-and-workflows]] reports Tharic cutting from five sessions to one; [[one-orchestrator-agent]] keeps many agents but one interface; [[token-maxing-with-agents]] runs ten or more threads across five subscriptions and filters them through [[agent-threads-as-inbox]]; [[stop-prompting-design-loops-and-goals]] puts the active ceiling at 2-3 instances and answers it with longer goals, not more terminals. |
| **Minimize tokens or burn them?** | [[reasoning-effort-discipline]] and [[loop-cost-discipline]] minimize; [[token-maxing-with-agents]] says spend the whole allowance. Reconciled by billing model in [[subscription-vs-api-tokens]]; effort discipline survives on subscriptions because over-engineering costs review attention. |
| **Do instructions compound?** | [[building-skills]] and [[self-updating-config]] treat them as an asset; [[ablation-driven-development]] treats them as debt with a one-generation half-life. [[agents-md-as-neural-net]] proposes a third position: they are **weights**, trained continuously within a fixed budget - ablation is the periodic full retrain, the backward pass the weekly gradient step. |

## Workflow reconstruction (2026-09-16)

The secondary guide [[kun-agentic-app-development-workflow]] adds a beginner sequence for the existing direction, isolation, and verification practices.
[[risk-based-agent-governance]] makes the review decision explicit, and [[reproducible-agent-environment]] connects onboarding to reconstructible tooling.
It is overlapping evidence rather than four new independent confirmations, and its staged checklist still allows architecture review during integration.

## Workflow playbook (2026-10-14)

[[agentic-coding-workflow-idea-to-review]] assembles this area's build practice into one procedure: intent, research, architecture with a trunk/leaf map, prototype, a contract with scenarios and risk tiers, atomic gated tasks, bounded goals, proof in the PR, layered review, and a separately gated launch.
Its structural contribution is that one set of acceptance scenarios serves as exit criterion, evidence checklist, and review yardstick ([[define-the-end-to-end-gate]]), and that review depth is fixed by a tier assigned before the code exists ([[risk-based-agent-governance]]).
It is built from secondary material, so it organizes the area's claims without strengthening them.

## Synthesis

The through-line across these sources is that **the scarce skill is designing a check the machine can run on itself, and everything else is being absorbed by the harness.**

Prompting was demoted (elicitation replaced it), context management is being demoted (compaction is eating it), and orchestration primitives are being partially demoted at the frontier (the model sustains long runs unaided).
What has *not* been demoted, in any source, is verification.
Every capability jump documented here - the 11-day Bun rewrite, the pixel-comparison Swift port, the rubric-graded self-improvement loop - was unlocked by an oracle the agent could run without a human.

The second through-line is about what the human keeps.
[[agentic-full-stack-build]] is the cleanest natural experiment available: a principal engineer built an entire full-stack app without reading source code, and needed exactly two interventions - a cost estimate anchored in stale data, and a scope class the agent invented.
Neither is a correctness judgment.
Both are judgments about *how much system this situation deserves*, which depends on facts outside the repo.
That is a narrower and more honest account of the human's role than [[own-the-problem-not-the-code]] manages, and it is consistent with Boris Cherny's answer to what separates the best: **being empirical, and letting go of your priors.**

For hcho this area is the direct professional bet.
It reframes "learn Claude Code deeply" from a productivity tip into a hireable competency, and its verification pillar is a decade of validation experience restated in the newest vocabulary.
The cross-links that matter are [[evals]] (validation as the upstream skill), [[agent-operations]] (running the resulting systems continuously), and [[ai-career]] (where [[forward-deployed-engineer]] pays for exactly this combination).
