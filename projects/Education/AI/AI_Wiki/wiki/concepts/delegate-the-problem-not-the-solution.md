---
type: concept
tags: [agentic-engineering, delegation, prompting, judgment, workflow]
status: seed
source-count: 1
last-updated: 2026-10-02
---

# Delegate the Problem, Not the Solution

Hand an agent the problem as you first understand it, early, before you have decided the fix.
Its attempt either solves the problem or tells you the problem is hard enough to deserve your own thinking.
From [[token-maxing-with-agents]].

## Key points

- **Bring the agent in when you start thinking, not after you have decided.** [[theo-t3]] says he changed from involving the agent once he knew what he wanted to involving it as soon as he began considering a problem.
His example: after about three weeks of thinking about one problem, he asked an agent for a stupid-simple solution and got one.
- **Give it the problem, not your solution.** A screenshot plus "fix it" often works, and a prescribed fix constrains the agent to your current idea.
- **The attempt is a difficulty probe.** If the agent fails, you have learned the problem is novel or hard, which is the signal to spend your own attention.
He compares it to managing a team: hand over problems, and dive in yourself only when the first solutions come back wrong.
- **Not "stop thinking."** He is explicit that the point is deciding whether a problem is worth your thought before spending days on it.
His phrase: "Don't outsource thinking, scale it."
- **Ask feasibility first when unsure.** For an uncertain idea he asked how hard it would be, then asked for the build, a PR, and a preview environment in one message.
- **Offer it a fork in the road.** For a confusing settings UI he told the agent to implement directly if confident, otherwise to produce mockups to choose between.

## The low end: offload the silly tasks

The same threshold-lowering applies to trivial work.
His "using tokens poorly" list: understanding a hard-to-parse teammate PR instead of interrupting the author, triaging all open PRs to pick the day's focus, finding an email across five inboxes, collecting scattered records, and sweeping every repository on a machine for abandoned ideas worth reviving.
His test: if nothing you ask an agent feels silly, you are not offloading enough.
Under a subscription these are also how leftover limit gets spent before it resets ([[subscription-vs-api-tokens]]).

## Synthesis

This is a delegation threshold, not a prompting trick.
The wiki's direction pages mostly describe how to specify work once you have decided to delegate it ([[ramble-then-structure]], [[elicitation-over-prompt-engineering]]); this page moves the decision earlier and lower, at both ends.
At the hard end the agent becomes a cheap first attempt that sorts problems into "solved" and "needs a human," and at the trivial end it absorbs chores that were never worth a human context switch.

It sits in productive tension with [[read-what-the-agent-writes]] and [[taste-as-moat]].
Delegating before you think risks never forming the judgment you would have built by thinking, and accepting the agent's first adequate answer can anchor you on it.
The reconciliation is in the probe framing itself: a success should still be read and understood, and a failure is information that buys your attention for the right problem.
What the habit removes is the days spent thinking about problems an agent solves in minutes, not the understanding of the solution.

For hcho the validation analogy is direct: run the cheap test first and let its failure tell you where to spend the expensive investigation.

## Source

- [[token-maxing-with-agents]] - Theo's practice and examples; experience-based, not measured.
