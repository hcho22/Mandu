---
type: concept
tags: [evals, verification, agents, llm-as-judge, bias, agentic-engineering]
status: developing
source-count: 1
last-updated: 2026-07-28
---

# Self-Referential Bias

A model that reviews its own output grades it too leniently.
Named as a concept in [[designing-loops-and-workflows]] by a member of Anthropic's [[claude-code]] team: "When a model prefers its own outputs, it's going to be more lenient at verifying it."

## The mitigation

- **Verify with a separate instance,** not the one that produced the work.
- The source's recommended structure is **three distinct roles**: one coordinating, one doing the work, one verifying, each with **different context and different models**.
- A stated side benefit: separating the roles also means each one puts more compute into its own job and is less likely to stop early.
- This is one of the two reasons the source gives for using a workflow over a single skill (the other being context management).

## The same phenomenon, named three ways

This page exists because three parts of the wiki independently arrived at the same finding from different directions.

| Framing | Where | The angle |
|---|---|---|
| **Self-enhancement bias** | [[llm-as-judge]], from [[llm-patterns]] and [[llm-evaluation-guidebook]] | Measured: GPT-4 favors its own outputs by about +10%, Claude-v1 by about +25% self-win rate. Mitigation: do not grade with the model that generated, or use a jury |
| **Fresh-context review** | [[fresh-context-review]], from [[building-products-with-agents]] | A reviewer that watched the work happen already believes it is correct and misses edge cases |
| **Self-referential bias** | this source | An orchestration constraint: it is why workflows split doing from verifying across separate agents |

They are not in conflict.
The eval literature measures it, the code-review literature attributes it to shared context, and this source treats it as a design constraint on agent architecture.
The strongest combined reading is that both variables matter and should be separated together: **different model** defeats the preference effect, **different context** defeats the belief effect.
Tharic's three-role structure is the only prescription in the wiki that varies both at once.

## Key points

- The bias is a property of the grader's identity, not just its information.
Clearing the context window is a partial fix; it removes shared belief but leaves a model still grading its own family of outputs.
- It scales with autonomy.
The longer an agent runs unattended ([[get-out-of-the-loop]]), the more the system leans on self-verification, so the bias matters more precisely where it is hardest to notice.
- A jury of several judges ([[llm-evaluation-guidebook]]) and adversarial review by a different model ([[adversarial-code-review]]) are the two established structural defenses.

## Synthesis

This is the single mechanism underneath most of the wiki's verification family, and naming it makes the family legible: [[fresh-context-review]], [[adversarial-code-review]], the [[skill-eval-loop]]'s separate grader, jury methods in [[llm-as-judge]], and the verifier sub-agent in [[verification-signal-picks-the-mechanism]] are all the same countermeasure applied at different layers.
The convergence is worth noting on its own terms: an eval-benchmarking literature, a code-review product, and Anthropic's own tooling team reached the same conclusion without citing each other, which is about as strong as evidence gets in this wiki.

For hcho this is the highest-value import from the source.
It is a first-principles argument, backed by numbers, for exactly the role he is qualified to hold: **the thing that checks the work cannot be the thing that did the work.**
That is the organizing principle of independent validation, and it is now a load-bearing constraint in agent architecture rather than a process preference.
It also flags a real risk in his own setup, where a single agent both builds and self-checks Purvia's eval harness, and argues for a separate verifying model in that loop.
