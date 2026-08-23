---
type: concept
tags: [agentic-engineering, agent-operations, workflows, orchestration, verification, graph-engineering]
status: seed
source-count: 1
last-updated: 2026-08-05
---

# Graph Engineering

Designing the **work itself** as a graph of jobs (nodes), arrows (transitions), and shared state, instead of running a task inside one long chat.
Named and defined in [[graph-engineering-isenberg]] by [[greg-isenberg]] as the third layer of working with AI:

> Prompt engineering = better questions. Context engineering = better information. **Graph engineering = better design of the work.**

The unit of leverage is not the model call but the shape of the work around it: what runs in parallel, what checks what, where the human approves, and what state each step leaves behind.

## The vocabulary

- **Job** - one step in the workflow (plan, research, critique, merge).
- **Arrow** - what happens next; the dependency between jobs.
- **State** - the shared notes moving through the graph ("what does the system know so far").
- The canonical shape is a **diamond**: one question fans out into parallel jobs, gets checked, and merges back into one answer.

## What it fixes

The default one-chat approach has a single model, in a single pass, decide what matters, do the research, interpret it, write the recommendation, and grade its own confidence, with no checks anywhere.
It *feels* like work was done; nothing was verified.
The graph splits that pass into roles a competent team would have - planner, parallel researchers, a skeptic whose only job is to kill weak findings, a merger, and a human gate - so that **checking is a separate job from producing** ([[self-referential-bias]]).

## Key points

- **Use it when** the work has multiple steps, some can run in parallel, and the output needs checking before it matters (deep research, go-to-market plans, support triage, code review, feedback synthesis, recurring content). **Skip it** for brainstorming ten names or summarizing an email.
- **Smallest graph, not biggest.** More agents is not better; it can mean more noise, several workers confidently repeating the same wrong idea, or more time spent coordinating than thinking. A good graph removes fake waiting, separates workers from checkers, puts the human gate where mistakes are expensive, stops when the answer is good enough, and leaves reusable state.
- **Understand before automating.** "If you automate a workflow you do not understand, you get a mess." Draw the graph before you automate it; the tool comes after the workflow is clear ([[start-as-a-workflow]], [[real-workflow-not-documented]]).
- **The human gate's strictness is priced by blast radius** ([[cost-of-being-wrong]], [[phased-autonomy]]): a private memo gets a light gate; a customer email, a public post, a code deploy, or a refund gets a strict one.
- **Graphs produce memory.** The compounding value is that each run leaves behind notes, evidence, and drafts that make the next run smarter - "the context becomes the moat" ([[ai-operating-system]], [[context-is-king]]).

## Two kinds of graph (do not conflate)

Most confusion about "graph" in AI is that the word names two different things. The source, and this page, are about the second.

| | [[knowledge-graph]] | Agent graph (this page) |
|---|---|---|
| Answers | How **information** connects | How **work** moves |
| Example | customer to company to product to team | planner to researchers to skeptic to merge to human |
| Built from | entities and relationships (GraphRAG) | jobs and arrows |
| Fixes | RAG that can't connect scattered facts | one-chat work with no checks |

The best systems use both; they are complementary, not competing.

## The three build levels

A deliberate ladder, warned against skipping straight to a framework:

1. **Manual** - run each job by hand in its own lane on an Excalidraw / TLDraw board. Do this successfully three times before automating; if the hand-run does not produce better work, automation only produces mediocre work faster.
2. **File-based** - each job writes its own file in a repo ([[claude-code]]): `plan.md`, `customer.md`, `competitors.md`, `review.md`, `recommendation.md`. This is [[agents-as-cron-plus-markdown]] applied to a single task - a reusable paper trail.
3. **Automated** - an orchestration tool runs the graph: LangGraph (checkpoints, persistence, human-in-the-loop), AutoGen / GraphFlow (sequential, parallel, conditional, loops), or n8n / Make.com (graphs that touch Slack, email, CRM).

## Relationship to the wiki's existing vocabulary

Graph engineering is a new *name* for a structure the wiki already holds in pieces, arrived at from the founder/operator side rather than the engineering side:

- The planner/researcher/skeptic/merge structure is [[agent-teams]] (persona panels) plus [[sub-agents]] (parallel fan-out) plus [[one-orchestrator-agent]] (single human interface).
- "Checker is its own job" is [[self-referential-bias]] and [[adversarial-code-review]].
- "Understand the workflow before automating" is [[start-as-a-workflow]] and [[dont-let-ai-be-your-architect]].
- The Level-3 automated version is the [[dynamic-workflows-as-test-time-compute]] fan-out-verify-fan-out pattern.
- Choosing the smallest graph is [[single-call-workflow-or-agent]].

## Synthesis

The useful contribution is not a new technique but a **name for the layer** and a beginner-legible on-ramp to it.
The wiki's engineering sources ([[designing-loops-and-workflows]], [[building-products-with-agents]]) already prescribe splitting doing from verifying and running work in parallel; graph engineering packages that as "draw your work as a team of jobs," which is exactly the framing a non-engineer can act on with a whiteboard and no framework.
That accessibility is the point: it lowers the entry cost of the wiki's most repeated structural lesson.

For hcho the sharpest line is "the same model that writes the answer also grades the answer," in plain operator language, applied not to code review but to **decision research** - which is directly the Purvia buyer-interview and PMF-evidence work.
It also validates the shape of Mandu itself: this assistant is a file-based graph (each job writes a markdown artifact, state persists between runs, a human gate sits before anything irreversible), which is Level 2 of exactly this ladder.
The caution worth importing is "smallest graph that improves quality": the risk in a wiki this fond of orchestration is building a bigger graph than the task earns, and this source is a clean statement of the counter-pressure.
