---
type: concept
tags: [evals, verification, agents, llm-as-judge, bias, agentic-engineering]
status: developing
source-count: 3
last-updated: 2026-08-21
---

# Self-Referential Bias

A model that reviews its own output grades it too leniently.
Named as a concept in [[designing-loops-and-workflows]] by a member of Anthropic's [[claude-code]] team: "When a model prefers its own outputs, it's going to be more lenient at verifying it."

## The mitigation

- **Verify with a separate instance,** not the one that produced the work.
- The source's recommended structure is **three distinct roles**: one coordinating, one doing the work, one verifying, each with **different context and different models**.
- A stated side benefit: separating the roles also means each one puts more compute into its own job and is less likely to stop early.
- This is one of the two reasons the source gives for using a workflow over a single skill (the other being context management).

## The same phenomenon, named four ways

This page exists because separate parts of the wiki independently arrived at the same finding from different directions - an eval literature, a code-review product, Anthropic's tooling team, and now a founder-audience explainer.

| Framing | Where | The angle |
|---|---|---|
| **Self-enhancement bias** | [[llm-as-judge]], from [[llm-patterns]] and [[llm-evaluation-guidebook]] | Measured: GPT-4 favors its own outputs by about +10%, Claude-v1 by about +25% self-win rate. Mitigation: do not grade with the model that generated, or use a jury |
| **Fresh-context review** | [[fresh-context-review]], from [[building-products-with-agents]] | A reviewer that watched the work happen already believes it is correct and misses edge cases |
| **Self-referential bias** | [[designing-loops-and-workflows]] | An orchestration constraint: it is why workflows split doing from verifying across separate agents |
| **"The same model writes and grades the answer"** | [[graph-engineering-isenberg]] | The founder/operator statement of it, applied to *decision research* not code: the skeptic must be its own job, "like asking someone to write their own performance review" |

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

## A self-QA pass that actually rejected something ([[one-person-marketing-team]], 2026-08-21)

The wiki's first counter-datum, recorded rather than resolved.

Generating UGC video ads, the agent built its own four-stage pipeline ([[storyboard-before-you-generate]]) whose last stage was a **QA pass on its own output**: it screenshotted each finished clip, reviewed them, and **rejected one** with the note "back panel," apparently a garbled logo or text defect, before reporting the job complete.
Same model, same session, same context, grading its own work - and it caught a real defect.

**The likely reconciliation is defect class, not a hole in the bias.**

A mangled logo panel is an objectively checkable property.
The clip either shows a correct logo or it does not, and no preference is involved, which puts the check much closer to a [[functional-scorers|functional scorer]] than to a judgment call.
The measured self-enhancement effect ([[llm-as-judge]]: roughly +10% to +25% self-win rate) is a *preference* bias - a model favors its own outputs when asked which is better.
It is not a claim that a model cannot see a defect it can literally look at.

Stated as a rule the page did not previously carry:

> **Self-review is plausible for objective defects and unreliable for quality judgments.**
> The bias attaches to "is this good," not to "is this broken."

That refines the existing prescription rather than weakening it.
The three-role separation is still correct wherever the verdict is subjective, which is most of what agents are asked to judge.
Where the check is mechanical, a self-run check is cheap and worth having, and the real risk is different - not leniency but **blind spots**, since a defect the generator cannot perceive it will also not perceive as a reviewer.

Two honest caveats on the evidence.
This is a single uninstrumented anecdote from a tutorial with no measurement, against four independent sources that do measure, so it does not move the page's position.
And there is no way to know how many defective clips the same pass **passed**, which is the number that would actually settle it - a reviewer that catches one obvious flaw and waves through three subtle ones looks exactly like this from the outside.

## Synthesis

This is the single mechanism underneath most of the wiki's verification family, and naming it makes the family legible: [[fresh-context-review]], [[adversarial-code-review]], the [[skill-eval-loop]]'s separate grader, jury methods in [[llm-as-judge]], and the verifier sub-agent in [[verification-signal-picks-the-mechanism]] are all the same countermeasure applied at different layers.
The convergence is worth noting on its own terms: an eval-benchmarking literature, a code-review product, Anthropic's own tooling team, and a founder-audience explainer ([[graph-engineering-isenberg]]) reached the same conclusion without citing each other, which is about as strong as evidence gets in this wiki.

For hcho this is the highest-value import from the source.
It is a first-principles argument, backed by numbers, for exactly the role he is qualified to hold: **the thing that checks the work cannot be the thing that did the work.**
That is the organizing principle of independent validation, and it is now a load-bearing constraint in agent architecture rather than a process preference.
It also flags a real risk in his own setup, where a single agent both builds and self-checks Purvia's eval harness, and argues for a separate verifying model in that loop.
