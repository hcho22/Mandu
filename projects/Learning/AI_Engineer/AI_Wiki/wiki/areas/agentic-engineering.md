---
type: area
tags: [agentic-engineering, agents, craft, tooling, orchestration, verification]
status: established
source-count: 11
last-updated: 2026-08-01
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

### Planning and review
- [[planning-is-removing-unknowns]] - planning as continuous exploration, not a phase.
- [[plan-code-validate]] - plan deeply, delegate coding, automate validation.
- [[phased-implementation]] - research to plan to implement in small testable phases.
- [[review-plans-as-artifacts]] - interactive artifacts beat 351-line markdown, because feedback becomes per-element.
- [[read-what-the-agent-writes]] - don't exit the loop by skipping the plan.
- [[fresh-context-review]] - review in a clean context; a biased reviewer misses bugs.
- [[adversarial-code-review]] - a different model hunts for bugs in AI-written code.

### Orchestration
- [[dynamic-workflows-as-test-time-compute]] - fan out, verify, fan out; a new scaling axis.
- [[verification-signal-picks-the-mechanism]] - pick /loop vs /goal vs a workflow by the shape of your check.
- [[sub-agents]] - delegate heavy exploration to children that return conclusions.
- [[one-orchestrator-agent]] - single-threaded human interface over parallel work; steerable crewmates over spawned sub-agents.
- [[agent-teams]] - persona panels that debate until they agree.
- [[long-horizon-agent-runs]] - days-to-weeks runs, and the three ingredients that enable them.

### Verification and the human's remaining job
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
- [[time-to-fix-as-health-signal]] - read agent time-to-fix as a codebase-health diagnostic.

### Artifacts and craft
- [[building-skills]] - build skills forward or by reverse-engineering.
- [[self-updating-config]] - a skill that mines corrections and improves its own config.
- [[design-system-not-a-design]] - a vocabulary, not a screen; let the design agent challenge the PRD.
- [[code-as-sawdust]] - prompts and specs are durable; code is a regenerable byproduct.
- [[ship-fast-learn-from-users]] - ship in days; real users reveal edge cases.
- [[ai-slop]] - the checkable signature of unedited AI output.

## Sources

- [[ai-era-50-career-tips]] - names the discipline and its four pillars.
- [[designing-loops-and-workflows]] - Tharic (Anthropic): the first primary source; mechanism selection, self-referential bias, planning as unknown-removal.
- [[building-at-the-frontier]] - Boris Cherny (Anthropic): ablation, overhang, elicitation, 11-day and 15-day runs, dynamic workflows as a compute axis.
- [[agentic-full-stack-build]] - Kun: an entire full-stack build with the three human interventions isolated.
- [[building-products-with-agents]] - Kun: the principles behind that build.
- [[building-5-ai-products-solo]] - Josh Pigford: phased local worktrees, cross-model review, context rot.
- [[inside-conductor-workflow]] - Conductor: voice-first parallel orchestration, slop-free zones.
- [[working-with-fable-5]] - Theo: cost min-maxing via reasoning effort and model routing.
- [[every-claude-feature-ranked]] - the broad feature tour of the ecosystem.
- [[production-agent-with-cma]] - Anthropic: production agent primitives and outcome rubrics.
- [[building-robust-apps-with-ai]] - Ross: why agent-operable infra makes any of this possible.

## Open tensions

The area is not internally consistent, and the disagreements are the interesting part.

| Question | Positions |
|---|---|
| **Does context degrade?** | [[context-rot]] says start fresh; [[compaction-over-context-window]] reports four clean compactions. Probably capacity versus contamination, but unresolved. |
| **Is orchestration scaffolding necessary?** | [[verification-signal-picks-the-mechanism]] gives a selection rule; [[building-at-the-frontier]] says `/go` and `/loop` are "helpful but not required" now. Likely a model-tier difference. |
| **Local or cloud?** | [[cloud-agents-over-local]] versus the local worktrees of [[building-5-ai-products-solo]] and [[inside-conductor-workflow]]. Filed under [[agent-operations]]. |
| **More agents or fewer?** | [[dynamic-workflows-as-test-time-compute]] scales to thousands; [[designing-loops-and-workflows]] reports Tharic cutting from five sessions to one; [[one-orchestrator-agent]] keeps many agents but one interface. |
| **Do instructions compound?** | [[building-skills]] and [[self-updating-config]] treat them as an asset; [[ablation-driven-development]] treats them as debt with a one-generation half-life. |

## Synthesis

The through-line across eleven sources is that **the scarce skill is designing a check the machine can run on itself, and everything else is being absorbed by the harness.**

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
