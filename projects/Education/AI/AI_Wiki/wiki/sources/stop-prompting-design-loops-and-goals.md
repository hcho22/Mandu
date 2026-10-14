---
type: source
title: "Stop Prompting, Start Designing Loops and Goals"
source-type: tutorial-summary
author: "John Kim (self-described senior staff software engineer at Meta; surname per hcho)"
url: local
date-ingested: 2026-10-14
date-created: unknown
tags: [agentic-engineering, loops, goals, long-horizon, harness, attention, exit-criteria]
---

# Stop Prompting, Start Designing Loops and Goals (John)

A supplied reference summary of an undated YouTube talk by [[john-meta-engineer]], his second source in the wiki after [[agentic-code-review-strategies]].
His argument: running several terminals and babysitting each agent ("fix this," "try again") makes **your attention the bottleneck**.
The alternative is to spend effort up front designing loops, goals, and a harness so agents run for hours, validate their own work, and unblock themselves.
He demonstrates with a goal that had been running about 22 hours, rebuilding his YouTube production workflow as a website plus an iOS app, and he is explicit that it works only because the tools, context, and exit criteria were already in place.
He calls the "prompting is dead" headline "a little bit of clickbait": you still prompt, but to set up the system.

## Key claims

- **Attention is the bottleneck.** By his rough estimate most people can actively handle only 2-3 agent instances; agents that run 5-10 minutes at a time keep waiting on you for the next step. "If your terminal looks like a wall of agents across multiple tabs, chances are you're probably doing it wrong" ([[get-out-of-the-loop]]).
- **"Token maxing" as leverage.** Treat tokens as a unit of work: put in as few of your own tokens as possible and get as many out as possible. His example is a harness: ChatGPT Deep Research turns the same question into far more output because of the tooling behind it ([[build-the-machine-first]]). He concedes the term is "kind of a cringe term."
- **Loops and goals.** A loop reruns the same prompt until an end criterion is met, or indefinitely; a goal is, in his words, essentially a loop with a certain interval, and he calls the two "pretty interchangeable" ([[verification-signal-picks-the-mechanism]]).
- **A good goal needs a strong exit criterion** the agent can verify with high confidence: an evaluation, design specs, or tests that must pass.
- **Recurring uses:** babysitting PRs, checking in on work every hour or two, and pulling messages from threads he follows every three hours into a summary ([[heartbeat-automation]]).
- **Plan before the long run.** The demo started with a prompt for a website, a native mobile app, and a CLI interface for agentic use. The agent returned a visual plan, then design screens drawn from his existing internal studio site. He spent about an hour reviewing and judged the plan about 80% there on functionality.
- **The goal itself was plain English:** build out the plan, include validations, push to GitHub at good checkpoints, take "full control," and move old files into an archive workspace instead of deleting them. Success meant the website and the iOS app fully working with every main feature ready for him to test. He admits it sounds like "make me a million dollars, don't make any mistakes" and says it probably will not work if copied as is.
- **Three ingredients made it work** ([[long-horizon-agent-runs]]):
  1. **Agentic tooling:** MCP or CLI access to everything the agent needs, so it does not stop to ask. Vercel was already connected and logged in, with skills.
  2. **Context:** "Brain," his local second-brain CLI over his projects and writing, indexed with a vector database (`brain search OpenAI` returns his work on OpenAI), so agents query context instead of hunting for files ([[ai-operating-system]]).
  3. **Exit criteria:** the design screens, which the agent compares its build against.
- **Self-QA.** The agent drives the iOS simulator and works through edge cases and test cases one by one, using iOS self-validation skills he built and trained it to use.
- **The new bottleneck is review.** Autonomous loops produce hundreds of PRs, which became his biggest constraint; he points to his code-review talk and says to use agents to review agent-produced code ([[agentic-code-review-strategies]]).

## Industry voices he cites

These are his characterizations, not verified quotes.

- **Peter Steinberger**, described as now at OpenAI and the creator of OpenClaw ([[open-claw]]), posted a "monthly reminder" to stop prompting coding agents and design loops that prompt them.
- **[[boris-cherny]]**, creator of [[claude-code]], has said in interviews that he runs loops and that his job is to write loops.

## Evidence limits

- No video title, URL, publication date, or timestamps; the summary itself is dated 2026-10-11, which is when it was generated, not when the talk was recorded.
- Caption-derived, with flagged uncertain restorations (`[?]`), including "loops and goals" versus "loops and graphs," the design tool "Pen (formerly Pencil)," and "Opus 4.8."
- **The 22-hour run is a work in progress, not a result.** At recording he was "not close to done," and no completion, defect count, or quality measure is reported.
- It is a personal side project for him and his internal team, so he was not focused on code quality and reviewed only at a high level; he uses goals and loops at work at a smaller scale.
- The Deep Research comparison is not narrated, and the summary notes he names opposite sides of the screen at different points.
- The 2-3 agent limit is his estimate; credentials and the roles of the people he cites are as stated, not checked.
- The exact loop and goal commands are not visible in the captions. Current Claude Code and Codex behavior is checked in [[agentic-coding-workflow-idea-to-review]].
- Mandu's note on the design tool: Mandu's own tooling includes the Pencil design MCP, whose documents are `.pen` files, which may explain the garbled "Pen, which was actually a Pencil" caption. Whether the product was renamed is unverified.

## Contradictions and term collisions

- **"Loops and goals are interchangeable" versus [[verification-signal-picks-the-mechanism]].** [[tharic]], from the [[claude-code]] team, treats `/loop` and `/goal` as different mechanisms chosen by the shape of the verification signal. John's own use cases split the same way: PR babysitting and three-hourly summaries are interval loops, while the 22-hour build is a goal with an exit check. The interchangeability is his characterization; filed as a disagreement, with the documented behavior recorded by the third source of this batch.
- **"Token maxing" means something different here than in [[token-maxing-with-agents]].** Theo uses it for spending the whole flat-rate allowance; John uses it for the ratio of work out to human input in. Both treat the human's input as the scarce resource, but one maximizes consumption and the other maximizes leverage. The wiki keeps both meanings attributed to their speakers rather than defining a single term.

## Connections

- [[long-horizon-agent-runs]] - a third long run, with a different three-ingredient list from Boris Cherny's.
- [[verification-signal-picks-the-mechanism]] - exit criteria as the deciding input, and the interchangeability disagreement.
- [[get-out-of-the-loop]] - a 2-3 instance attention ceiling, matching Tharic's cut to one active session.
- [[build-the-machine-first]] - the harness, not the prompt, is the leverage.
- [[ai-operating-system]] - a second brain exposed to agents as a queryable CLI.
- [[heartbeat-automation]] - periodic check-ins and thread summaries on a fixed cadence.
- [[credential-vaults]] and [[capabilities-not-instructions]] - pre-authenticated deploy tooling removes roadblocks and also grants authority.
- [[define-the-end-to-end-gate]] - "both apps fully working, every main feature built" is a gate stated up front, though looser than a scenario.
- [[agentic-code-review-strategies]] - the review bottleneck the loops create.
- [[agent-operations]] and [[agentic-engineering]] - the recurring-loop and build-time halves of the same talk.

## Possible project applications

These are Mandu's suggested applications, not claims that the projects already work this way.

- [[projects/Purvia/README|Purvia]]: an exit criterion is only as good as its judge. E7's offline judge has been counting the refusal "I don't have that information." as an answer, so a goal that stopped on "E7 passes" would stop on a false success. Fixing the judge is a precondition for handing that metric to any loop.
- [[projects/Immerse/README|Immerse]]: the per-Camera look boards hcho reviews are reference artifacts of the kind John uses as exit criteria. Whether a build agent can compare its output against them with high confidence, or whether they still need his eye, is untested.
- Mandu itself: agents read Mandu's Markdown directly with file tools. John's Brain is the alternative shape, a query CLI over the second brain; it would matter once the wikis are too large to navigate by index.
- [[projects/RepToday/README|Rep Today]]: simulator self-QA covers the flows a simulator can run; the six release-blocking device checks still unrecorded as of 2026-10-12 (including health data, sync, and telemetry) are the part no simulator loop can close.

## Source

- Title as supplied: "Video Summary: Stop Prompting, Start Designing Loops and Goals" (the summary says the video title and URL are not in the transcript).
- Speaker: John, self-described senior staff software engineer at Meta, with "thousands of hours" on AI coding and agentic workflows by his account; treated as John Kim per hcho's 2026-10-14 identification ([[john-meta-engineer]]). The transcript gives only the first name.
- URL: not supplied.
- Raw: [[projects/Education/AI/AI_Wiki/raw/stop-prompting-design-loops-and-goals|Preserved Markdown summary]] (saved verbatim in `raw/`, immutable).
- Original inbox filename: `101226_stop-prompting-loops-goals-summary.md`.
- Ingested: 2026-10-14, the second of three sources hcho asked to file in one batch.
