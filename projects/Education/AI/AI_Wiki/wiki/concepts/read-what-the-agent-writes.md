---
type: concept
tags: [craft, learning, judgment, ai-career, agentic-engineering, failure-modes]
status: developing
source-count: 4
last-updated: 2026-10-14
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

## The tension: "a lot of us don't review code anymore"

[[running-life-on-codex]] states the opposite practice head-on: [[jason-openai-codex]] (and his host) say, as personal practice, that they no longer review most of the code the agent writes - which is why he does much of his work in ChatGPT Work, where the diffs are hidden.

Read carefully, this is less a contradiction than a relocation of the check:

- This page's warning is about not reading the **plan/reasoning**, which is how you keep the judgment to catch the agent.
- Jason has moved verification off the **diff** and onto an **executable oracle**: [[goal-plan-worklog]] goal files that name a verifiable end-state, computer-use self-checks ("open the app, upload this video, confirm the data comes back"), and separate checker steps. He reads the **worklog**, not every message.
- So both agree the check must exist; they disagree on where it lives - reading the work vs running an oracle against it.

The unresolved edge is real, though: an executable check verifies *correctness*, not *understanding*, and this page's core claim is that understanding is a separate exit you should not take ([[andrej-karpathy]]: "education should feel like work"). An operator who only ever reads a green check, never the reasoning, still erodes the judgment [[taste-as-moat]] depends on. Held as an open tension, filed on both pages.

## A further data point: archived unread (2026-10-02)

[[token-maxing-with-agents]] goes past Jason's position: [[theo-t3]] estimates about half his threads are archived without his reading the agent's final message, and calls watching an agent work one of the worst uses of time.
Like Jason, he relocates the check into conditions stated in the prompt and into automated review, so it is another case of verification moved rather than dropped.
He also says plainly that he wants agents brought in when he starts thinking ([[delegate-the-problem-not-the-solution]]), which is the case this page worries about most: the understanding you skip is the one you would have built.

## The opposite data point: reading more (2026-10-14)

[[agentic-code-review-strategies]] is the first named practitioner in the wiki who reports reading *more* code since agents arrived.
[[john-meta-engineer]] still reads "a lot," turns his review knob up for trunk code and one-way doors, and skims gated leaf work that carries proof.
His reason is volume: one person running several agents produces far more code, and the dangerous fraction of it grows with the total.
He also ties fast review to knowing the codebase, which is this page's thesis from the other side: you can only triage what you understand, and understanding comes from having read it.

## Synthesis

This is the honest counterweight to [[get-out-of-the-loop]], and the two are easy to mistake for opposites.
Getting out of the loop removes the human from *verifying* the work, which is correct and is what the automated-reviewer family exists to enable.
This page says do not also remove the human from *understanding* the work, because those are different exits and only the first one is safe.
An operator who has stopped reading has no basis for the judgment calls that [[taste-as-moat]] and [[own-the-problem-not-the-code]] say are the last durable human contribution, and the [[cost-of-being-wrong]] is paid by exactly that judgment.

The uncomfortable implication is that the productivity gain and the learning are in tension by default.
Skipping the plan is faster today and makes you less able to catch the agent tomorrow, which is a slow, invisible failure, and the only reliable fix named here is a structural one: instrument the workflow so the reading is unavoidable rather than relying on discipline.

For hcho this is a concrete habit to install in Mandu rather than an abstraction, and it also has a career reading.
If most operators are not reading what their agents produce, then being someone who does is a differentiator in exactly the direction he is already pointed, since catching what the agent got wrong is the entire content of the validation role.
