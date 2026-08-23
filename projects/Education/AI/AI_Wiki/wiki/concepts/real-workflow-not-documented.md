---
type: concept
tags: [ai-career, fde, discovery, requirements, deployment]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# The Real Workflow, Not the Documented One

**The process people describe is not the process people run.**
Finding the difference is where most FDE time goes ([[fde-in-30-days]]).

## The worked example

"An email arrives" sounds like a simple trigger. In reality:

- It arrives from **40+ senders**, with no consistent formatting.
- The data comes as a PDF, a screenshot, an Excel spreadsheet, or buried in a forwarded thread.
- Many steps are **exceptions**: "ignore the second attachment," "Sarah already signed off on this one."
- There is **no consistent subject line** to route by.
- **The real logic often lives in one person's head and isn't written down anywhere.**

The same complexity repeats at every downstream step - copying into a spreadsheet brings stale data, manual rekeying, and column drift.

## How to surface it

- **Be on-site.** A full 8-10 hour day surfaces undocumented exceptions and edge cases that a 1-hour interview never will.
The comparison drawn is consultants sitting with miners on-site to observe the real workflow.
- **Ask the reflexive question:** how easy would it be for *you* to write down every exception in your own job?
Vas uses his own time at Meta - his official description ("I code all day") omits meetings, production incidents, and firefighting.
Nobody can enumerate their own exceptions on request, which is why you have to watch.

## What it feeds

Once the real workflow is understood, the decision is: **where does deterministic software live, where does the agent act, where does a human approve, and where does the record get updated?**

The recommended architecture follows directly:
deterministic software handles the majority of steps, LLM calls provide judgment where needed, and **human-in-the-loop approval** sits before the agent proceeds to the back half of the workflow.
Vas "strongly recommends" all his FDEs push for that approval step.

## Synthesis

This is the discovery discipline that makes [[single-call-workflow-or-agent]] answerable.
That page says pick the least-powerful architecture that works - but you cannot pick it until you know what the work actually is, and the documented process systematically understates the mess.
The "only 2-3 of 10 steps genuinely need LLM judgment" figure is what you get *after* this stage, not before it.

The deeper claim is that **the exceptions are the system**.
The happy path is usually simple and usually already automated; the value and the risk both live in the undocumented handling that one person carries in their head.
That is the same observation [[solve-for-the-exceptions]] states as a philosophy, and this page is the method for finding them.

For hcho this is familiar territory under a different name.
Hardware validation is the practice of discovering how a system actually behaves versus how the spec says it behaves, and building the test matrix from that gap.
The transfer is close to exact, and it is a more concrete story than "I have validation experience" - it names a specific, hard, well-paid activity he has already done for a decade.
It also directly informs the Agentic RAG buyer interviews, where the goal is not to hear what buyers say they want but to see what they actually do with permissions and retrieval today.
