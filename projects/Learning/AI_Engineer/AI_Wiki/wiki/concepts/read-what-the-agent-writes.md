---
type: concept
tags: [craft, learning, judgment, ai-career, agentic-engineering, failure-modes]
status: seed
source-count: 1
last-updated: 2026-07-28
---

# Read What the Agent Writes

The failure mode and the counter-practice from [[designing-loops-and-workflows]].
The failure mode: users get lazy, stop reading long AI-generated markdown plans, and just tell the agent "just do it."
Both the host and the Anthropic guest confess to it, and Tharic warns it backfires, costing more time and money later than reading would have.

The counter-practice: generate explainers and reports specifically so that you are forced to read them, and treat that reading as the mechanism by which you get more technical.

## Unknown unknowns are the target

The stated goal of "becoming more technical" is not syntax.
It is knowing your **unknown unknowns**: understanding the trade-offs between backend services, between video encoding libraries, between local and remote transcription.
Not memorizing TypeScript specifics.

This is the same target [[planning-is-removing-unknowns]] aims at from the other side.
That page removes unknowns for a specific build; this one removes them from you, permanently, so the next build starts with fewer.

## Key points

- **Push the agent to teach you.** Have it brainstorm the constraints of a system: what is possible, how it currently works, how it could be better.
Tharic stresses "you really do have to push it."
- **Reading is the differentiator, not prompting.**
Generating and actually reading detailed HTML reports is framed as the exception rather than the norm, and as what separates good output from best-in-class output.
Most people prompt and glance at the result without engaging with the reasoning.
- **Make the habit structural.** Add a custom instruction asking the agent to produce an HTML report or explainer for significant tasks, precisely so you are prompted to read and learn from it.
- Citing [[andrej-karpathy]]: **"education should feel like work more than fun."**
Real learning takes deliberate effort; prompting and looking at outputs is not it.

## Synthesis

This is the honest counterweight to [[get-out-of-the-loop]], and the two are easy to mistake for opposites.
Getting out of the loop removes the human from *verifying* the work, which is correct and is what the automated-reviewer family exists to enable.
This page says do not also remove the human from *understanding* the work, because those are different exits and only the first one is safe.
An operator who has stopped reading has no basis for the judgment calls that [[taste-as-moat]] and [[own-the-problem-not-the-code]] say are the last durable human contribution, and the [[cost-of-being-wrong]] is paid by exactly that judgment.

The uncomfortable implication is that the productivity gain and the learning are in tension by default.
Skipping the plan is faster today and makes you less able to catch the agent tomorrow, which is a slow, invisible failure, and the only reliable fix named here is a structural one: instrument the workflow so the reading is unavoidable rather than relying on discipline.

For hcho this is a concrete habit to install in Mandu rather than an abstraction, and it also has a career reading.
If most operators are not reading what their agents produce, then being someone who does is a differentiator in exactly the direction he is already pointed, since catching what the agent got wrong is the entire content of the validation role.
