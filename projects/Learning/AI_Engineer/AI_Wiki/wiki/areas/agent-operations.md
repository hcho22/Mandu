---
type: area
tags: [agent-operations, agents, loops, automation, cost, business]
status: developing
source-count: 7
last-updated: 2026-08-05
---

# Agent Operations

The durable hub for **running things with agents continuously** - as opposed to [[agentic-engineering]], which is about using agents to build software.

Created 2026-08-01, when four sources in one batch turned a loose cluster of concepts into a real topic.
The distinguishing question is not "what did the agent build" but **"what does the agent do every day, and how do you know it did it."**

## The boundary with [[agentic-engineering]]

| | [[agentic-engineering]] | Agent operations |
|---|---|---|
| Object | A codebase, a feature, a build | A metric, a workflow, a business |
| Horizon | Minutes to weeks, one task | Months to years, repeated |
| Context | Shared across the task | Not shared between runs; memory persists in files |
| Success | The thing works | The number moved |
| Failure mode | Wrong output | **Silent convergence** ([[creative-entropy]]) |

The primitive distinction from [[dynamic-workflows-as-test-time-compute]] draws the line cleanly: a **workflow** is one task broken into chunks that share context, while a **loop** or **routine** is one repetitive task run over and over that does not.
This area owns the second column.
People routinely span both - [[ryan-carson]] runs a cloud engineering fleet *and* three production automations - so the split is by activity, not by person.

## Concepts in this area

### The loop as an operating primitive
- [[business-loops]] - build/measure/learn pointed at business metrics over months; the Lean Startup lineage.
- [[minimal-viable-loop]] - start with the smallest verifiable outcome, not the ambitious goal.
- [[leading-metric-over-vanity-metric]] - pick a number a single iteration can move.
- [[loop-cost-discipline]] - tie stop conditions to real unit economics; cost scales with run frequency, not lifetime.
- [[creative-entropy]] - loops converge and stagnate silently; inject DNA from outside the loop.

### Running agents in production
- [[heartbeat-automation]] - a scheduled agent that reads all your inboxes on a cadence and hands back one "what needs attention" briefing (the "Chief of Staff" pattern).
- [[agents-as-cron-plus-markdown]] - an agent = a deterministic cron + a good skill file.
- [[self-maintaining-codebase]] - 20-30 daily routines at Anthropic; one-sentence prompts, every routine ends in a PR.
- [[self-improving-agent-loop]] - grade real production traffic against a rubric; failures open their own fix PRs.
- [[production-watchdog]] - a daily digest of what real customers did, linked back to the live UI.
- [[agent-as-employee]] - give the agent its own identity and scoped permissions.
- [[everything-is-a-pr]] - run a full SDLC even solo; the human gate is review, not authorship.
- [[build-the-machine-first]] - build the system that does the work, then augment.

### Fleets, vendors, and cost
- [[manager-of-agents]] - the role reframe; decision throughput becomes the bottleneck.
- [[cloud-agents-over-local]] - a VM per session instead of worktrees. **Contested; see below.**
- [[independent-agent-lab-vs-frontier-lab]] - don't build your software factory inside a frontier lab's stack.
- [[model-routing]] - route grunt work to cheaper models once spend passes ~$5K/month/engineer.

### Agents pointed at distribution
- [[marketing-agent]] - the three requirements that separate an agent from an automation.
- [[unified-data-warehouse-for-agents]] - unified cross-channel data is the precondition, not the model.
- [[test-breadth-over-conviction]] - positioning is empirical; 10-20 variants before concluding.
- [[creative-is-the-targeting]] - the model reads your creative and routes it; the paid-media twin of [[aeo-answer-engine-optimization]].

### Infrastructure underneath
- [[managed-agent-primitives]] - agents, environments, sessions, events.
- [[agent-observability]] - "observability is the hard part, not the automation."
- [[credential-vaults]] - secrets that never enter the model's context; never give agents prod write keys.
- [[durable-agent-processes]] - durable execution and queues, because an agent can't stop when the tab closes.
- [[outcome-rubric-iteration]] - attach a rubric; the agent loops until it passes.

## Sources

- [[one-person-company-with-agents]] - Ryan Carson: the original cron-plus-markdown account of running a company on agents.
- [[running-teams-of-ai-agents]] - Ryan Carson again, post-PMF: cloud fleets, three production automations, vendor strategy, token economics.
- [[loops-to-run-your-business]] - the loop primitive pointed at SEO, ads, and product KPIs over months.
- [[building-marketing-agents]] - Cody Schneider: the deepest technical account of a non-engineering agent, plus the entropy problem.
- [[building-at-the-frontier]] - Boris Cherny: Anthropic's 20-30 daily self-maintenance routines, and the loop/routine/workflow distinction.
- [[production-agent-with-cma]] - Anthropic: the production agent-infrastructure primitives underneath all of it.
- [[running-life-on-codex]] - Jason (OpenAI Codex): the personal-operations version - a scheduled "Chief of Staff" heartbeat, a self-improving skill library, and a markdown vault as the agent's memory; the OpenAI-side confirmation that these patterns are not Anthropic-specific.

## Open tensions

- **Local versus cloud** ([[cloud-agents-over-local]]): [[running-teams-of-ai-agents]] calls local development a "caveman" practice; [[building-5-ai-products-solo]] and [[inside-conductor-workflow]] both run local worktrees deliberately. Ryan's evidence is real but is *n* of 1 from a paying Devin customer at PMF scale.
- **How much infrastructure a real agent needs**: [[agents-as-cron-plus-markdown]] says a cron and a markdown file; [[marketing-agent]] says that is insufficient without a unified data warehouse. Probably resolved by whether the decision needs cross-channel context.
- **Spend posture**: [[running-teams-of-ai-agents]] reports ~$20K/month and says spend first, optimize later; [[loop-cost-discipline]] says a well-scoped loop is under $5 a run. Both are right at their own scale.

## Synthesis

Three findings recur across sources that had no contact with each other, and they are the area's actual content.

**First, point agents at maintenance before features.**
Anthropic's routines target dead code, stale flags, junk tests, and drifted abstractions ([[self-maintaining-codebase]]).
Ryan Carson's automations target production bugs, customer-activity digests, and rubric-failing conversations ([[self-improving-agent-loop]], [[production-watchdog]]).
Both independently chose the work that is individually low-value, collectively enormous, well-specified, and permanently deferred.
That is where scheduled agents pay off first, not in feature development.

**Second, the eval stopped being a gate and became a source of work.**
[[self-improving-agent-loop]] grades real traffic against a rubric and the *output is a pull request*.
[[business-loops]] uses an eval threshold as a loop's stop condition.
This is the most important idea in the area for hcho: the standard case for evals is defensive, and this inverts it - a good rubric plus real traffic plus an agent that can open PRs turns the eval system into the thing that generates the roadmap.

**Third, observability is the hard half.**
Every source that has actually run these systems says the automation is easy and knowing what it did is not.
Ryan Carson states it outright; Boris Cherny's routines all terminate in PRs precisely so there is a human-legible artifact; the production watchdog exists solely to compress events into something a person will actually read.
An agent operation without an observability path is not a system, it is a background process nobody watches.

The fourth thing is a warning rather than a finding: **[[creative-entropy]]**.
Every loop in this area is a hill climber, and hill climbers converge and then keep running while their own metrics look fine.
No source except [[building-marketing-agents]] names this, and it applies to all of them.

Cross-links: [[agentic-engineering]] for building with agents rather than operating them, [[evals]] for the rubric and measurement discipline that every loop here depends on, and [[agent-saas]] for turning an operated agent into something you sell.
