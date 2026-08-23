---
type: concept
tags: [agentic-engineering, workflow, verification, claude-code, orchestration]
status: established
source-count: 3
last-updated: 2026-08-01
---

# The Verification Signal Picks the Mechanism

The selection rule from [[designing-loops-and-workflows]], stated by a member of Anthropic's [[claude-code]] team: when choosing how to orchestrate long-running agent work, decide by **what kind of verification signal you have**, not by how big or complex the task is.

## The three mechanisms

- **`/loop`** - the general mechanism for iterative, orchestrated work: a way of feeding the agent feedback so it can run for long periods.
- **`/goal`** - reminds the agent of its exit condition so it does not stop early.
Use it when spec and exploration are already done and you want execution, including gap-filling when the agent hits something unexpected.
- **Workflows** - the most powerful of the three.
Spin up [[sub-agents]] that both do the work in parallel and verify it, turning a non-deterministic task into something closer to deterministic.
Implemented as a JS file, which can be packaged into a skill (see [[building-skills]]).

## The rule

| Verification signal | Mechanism | Example from the source |
|---|---|---|
| Deterministic, checkable | `/goal` | "Make sure the rendered design matches the Figma MCP" |
| Squishy, subjective judgment | Workflow with a rubric and a dedicated verification agent | Comparing an output against a screenshot; grading five generated video clips |

The source is explicit that outcomes are "very dependent on the task" and there is no universally right mechanism.
The only question that generalizes is what feedback signal is available.

## Key points

- **Budget compute per parallel task.** Without a maximum compute budget per sub-agent, the model spreads verification effort thin across simultaneous outputs and per-output quality drops.
This is the parallel-work analogue of [[reasoning-effort-discipline]]: effort is a resource you allocate deliberately, not a dial you max out.
- The workflow branch carries a rubric because a squishy signal has to be made explicit before an agent can check against it, which is the same move as [[outcome-rubric-iteration]] and [[pass-fail-over-score-evals]].
- Two reasons workflows beat a single skill: context management (sub-agents keep the main session clean, see [[context-rot]]) and avoiding [[self-referential-bias]].

## Confirmed from outside, and tempered from inside (2026-08-01)

**Independent confirmation.** [[loops-to-run-your-business]] arrives at the same rule from the business side with no Anthropic contact: "**pick the number first, then build the loop around it**," and it explicitly generalizes past software - Google ranking, ad ROAS, and retention close a loop as well as a passing test does.
Two unrelated sources concluding that the available feedback signal is *the* design constraint is the strongest agreement in this part of the wiki.

**A tempering from the frontier.** [[building-at-the-frontier]] says the orchestration layer is becoming optional.
[[boris-cherny]] reports Opus 5 sustaining 11-day and 15-day autonomous runs and names `/go` and `/loop` as **"helpful but not required"** - the model keeps going because it understands the task needs finishing, not because scaffolding forces it to.
His recipe for a long run is three ingredients with no primitive named: a hard task, a verification loop the model can execute itself, and a stopping condition ([[long-horizon-agent-runs]]).

This does **not** overturn the rule; it narrows what the rule is choosing between.
Both sources agree the signal is what matters.
They disagree on how much machinery has to wrap it, and the likely explanation is model tier - the scaffolding earns its keep below the frontier and is absorbed above it.
That is inference, not something either source states.

Boris also adds a fourth mechanism this page did not have: **dynamic workflows** as a way to ramp test-time compute on one task, distinct from a loop or routine ([[dynamic-workflows-as-test-time-compute]]).

## Synthesis

This is the first explicit selection criterion in the wiki for the orchestration primitives that [[working-with-fable-5]] and [[every-claude-feature-ranked]] described only from the outside, and it inverts the intuitive framing.
The usual instinct is to pick a mechanism by task difficulty.
The actual constraint is measurability: you can only hand an agent a long leash to the degree you can define what "done and correct" means, so the design work is upstream, in constructing the signal.

For hcho this is the most directly transferable idea in the source.
"Figure out what the pass criterion is, then let the machine run against it" is hardware validation stated in agent vocabulary, and it says his edge determines *which* orchestration primitive is even available: teams that cannot express a check are stuck with subjective workflows and rubric-writing, while a team that can build a deterministic oracle gets the cheaper, tighter `/goal` loop.
It also gives Purvia's eval harness a design brief, since the leak suite and escalation golden set are exactly the deterministic-signal end of this table.

The frontier tempering makes that point *more* pressing rather than less.
If good scaffolding is what a weaker model needs and a good oracle is what a stronger model needs, then investing in the oracle is the choice that survives the next model release - which is the same conclusion [[evals-saturate-and-get-replaced]] reaches from the opposite direction.
