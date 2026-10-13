---
type: concept
tags: [ai-career, agent-operations, role, management, craft]
status: developing
source-count: 4
last-updated: 2026-10-02
---

# You Are a Manager of Agents

The role reframe, stated independently by two sources in this batch from opposite ends of a company.

[[ryan-carson]] in [[running-teams-of-ai-agents]]: *no matter what you used to be - IC, people manager, founder, VC, parent, student - you are now a manager of agents, and you should aim to be world-class at it.*
Cody Schneider in [[building-marketing-agents]] calls the marketing version an **"agent jockey"**: someone who takes their existing domain knowledge and encodes it into agent-driven systems rather than executing tasks manually.

## Managing agents makes you *more* technical

This is the counterintuitive part, and Ryan is emphatic about it.
To direct agents well you end up having to understand Postgres, production versus dev environments, migrations, and so on - **and you learn all of it by using the agents.**
He says he is more technical now than at any point in his life.

- The right mental model is **engineering manager**, not "prompt user."
- **"It is a farce that engineering is going away."** Anyone claiming engineers are disappearing or becoming less technical is not doing the work.
- **The carpenter analogy:** if robot carpenters existed, a real carpenter would manage them far better than a non-carpenter, because they know where the cut goes and where the nail goes.
**Domain skill makes you a better manager of agents, not a redundant one.**
- Cody's version from the marketing side: you don't need to be deeply technical to start, but the leverage comes from **domain knowledge encoded into a system**, which is the same claim about where value sits.

## Decision throughput becomes the bottleneck

Once output scales, **you** are the constraint:

- Old cadence: **2-3 high-stakes decisions per day**, communicated in a meeting, executed over two weeks.
- New cadence: **10-20 high-stakes decisions before lunch.**
- Agents are an infinitely scalable team that works very fast, and they will be **blocked by you**. You cannot delegate the decisions yet.
- Be honest about the cost: you will work **more**, not less, and it is tiring.
The muscle analogy - it's a back muscle you never had to exercise before, and it turns out to be the most important one.

**Ryan's system for surviving it:** triage into two buckets (things shipping *today* versus everything else) and **pin** the important threads; write the day's priorities on **paper**, because ~10 of the daily PRs are firefighting and that's exactly what pulls you off what matters; check pinned threads on a **~25 minute cadence**, spaced enough to mentally rest rather than clicking through threads all day.
Mantra: "Slow is smooth, and smooth is fast."

The host's observation, which Ryan accepts: this is not very different from what a well-organized person did *before* AI.
**"It's back to the basics, just in an agent age."**

**A third workload design (2026-10-02).** [[token-maxing-with-agents]] states the same bottleneck in one line - agents are multi-threaded, humans are single-threaded, you are the bottleneck - and answers it by designing work so agents unblock themselves and surface only finished or blocked threads ([[agent-threads-as-inbox]]), rather than by a check-in cadence.

## A dissent worth holding: "I don't feel like a manager"

[[jason-openai-codex]] in [[running-life-on-codex]] is the wiki's first explicit **counter** to this framing.
Asked directly about feeling like a manager of agents, he says he does *not* relate to it: he frames his role as caring about **outcomes and quality** - articulating what he does and does not like ([[taste-as-moat]]) - not about supervising labor or hours.

This is less a factual disagreement than a metaphor clash, and it is genuine:

- Ryan/Cody's "manager of agents" foregrounds **decision throughput and delegation** - the bottleneck is you approving/directing work.
- Jason's "I care about outcomes, not management" foregrounds **taste and specification** - the job is knowing what good is and saying it precisely.
- Both are describing the same day (direct the agents, judge the output, decide what ships); they disagree on which verb names it. [[agent-as-employee]] already flags that the coworker metaphor is "helpful but limiting," and this is that caution landing on the management metaphor specifically.

Recorded as an open perspective split, not resolved. Watch whether later sources cluster on "manager" or on "editor/director-of-taste" language.

## Synthesis

The claim that agent operation makes you more technical is the most useful thing here, and it inverts the anxiety that runs through most career sources.
[[ai-engineer-is-a-builder]] argues the role doesn't require a PhD; this argues the role *actively builds* depth, because directing an agent through a real production problem forces you to understand the problem.

For hcho, whose pivot narrative is "a decade of validation judgment plus AI-native execution," the carpenter analogy is the cleanest one-line articulation of it in the wiki.
It answers the objection the pivot always faces - that domain experience from another field is a sunk cost - by saying the domain skill *is* the management skill.
That belongs in interview prep (`projects/job-search/interview-prep.md`), not duplicated here.

The decision-throughput ceiling is the more actionable half and is under-discussed everywhere else.
It reframes the personal bottleneck from "can I build fast enough" to "can I decide fast enough, all day, without degrading" - and Ryan's answer is unglamorous scheduling discipline, not tooling.
See [[get-out-of-the-loop]] for the opposite pressure: the way to raise the ceiling is to need fewer decisions, not to make them faster.
