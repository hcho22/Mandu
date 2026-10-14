---
type: source
title: "Do You Still Read Your Code? Agentic Code Review Strategies"
source-type: tutorial-summary
author: "John Kim (self-described senior staff software engineer at Meta; surname per hcho)"
url: local
date-ingested: 2026-10-14
date-created: unknown
tags: [agentic-engineering, code-review, validation, feature-flags, risk, release]
---

# Agentic Code Review Strategies (John)

A supplied reference summary of an undated YouTube talk by [[john-meta-engineer]], a self-described senior staff software engineer at Meta who runs an AI tech news and tutorials channel on the side.
His answer to "do you still read your code?" is "it depends": review depth is a gradient set by the blast radius of each change.
What makes reading less code safe is the system around the review: gates planned from day one, agent-supplied proof in every PR, static checks for nits, a fresh-context adversarial reviewer, and gated launches.
This is his first source in the wiki; his companion talk on autonomy is [[stop-prompting-design-loops-and-goals]], and [[agentic-coding-workflow-idea-to-review]] merges both with Kun's workflow.

## Key claims

- **Two camps, one gradient.** One camp says reading your code means you are too slow; the other says agents still make dumb mistakes and unreviewed output is slop. His position is that the right amount of review depends on the code being reviewed.
- **Agents belong on the whole path to production:** plan, build, review, launch. Define evaluations and validation criteria ahead of time so the agent and the human have something objective to check against.
- **The codebase is a tree.** Trunk code (entry points such as an `App.js` that wires in the helpers, infrastructure such as image processing and networking, shared state) gets careful reading because a bug there affects the whole app. Leaf code (isolated or fully gated) gets a skim, provided the PR carries proof ([[risk-based-agent-governance]]).
- **Gate everything from day one.** A plain Boolean flag is enough to start; LaunchDarkly is the platform example. Separate leaf work from integration work and give the integration layers their own gates, then let agents make atomic changes ([[feature-gating-from-day-one]]).
- **Demand proof in every PR:** unit tests whose names and asserts can be skimmed, runtime logs, screenshots or video of UI changes, and a stated confidence level for each part of the change. Build the requirement into skills, plus a separate skill against useless tests, because agents can write tests that prove nothing ([[proof-in-the-pr]]).
- **Three safety questions before reading:** what control experience must not change, how bad it could be if the change went wrong, and whether it can be rolled back. A confident yes on the last one is what licenses a skim. "In my opinion, everything should be anchored on safety."
- **Nits are dead.** Style belongs to type checking, linting, and AI reviewers; refactors are cheaper now that validation covers the code.
- **The review-depth knob.** He turns it up for trunk, infrastructure, many-dependency changes, and above all one-way doors. He says he still reads "a lot" of code and probably more than before.
- **Review AI code with an agent that did not write it.** The default reviewers in [[claude-code]] (`/code-review`) and [[codex]] are good enough in his view, but a reviewer that shares the producing context is biased: "The agents will cheat." Give agents a PR template so PRs look alike; his pet peeve is a summary and test plan longer than the diff.
- **Codex on GitHub** can review automatically when a PR opens or when tagged, and costs money. He believes it uses a model trained for review, hedged as "I think."
- **Babysit PRs with a recurring loop.** His example prompt asks an agent to check the PR every hour, fix the reviewer's requests, re-run local and agentic validation, update the PR notes, and resubmit; build it into a skill.
- **Merge-ready is not launch-ready.** Gated and landed work is about 80% done. The last 20% (refactoring, several agents auditing the whole feature for performance, bugs, security, and conformance to spec, and polish such as animations) takes as long as the first 80% and needs human taste ([[merge-ready-vs-launch-ready]]).
- **Launch behind the gate with an A/B test or a canary** even when the user base is too small for statistical power, because a trickle of traffic surfaces bugs, crashes, and alerts early.
- **The position is evolving.** As models improve he expects to read less; "maybe after another few generations of the model" none. Knowing which parts of your codebase are trunk is what makes fast review possible.

## Relationship to the 2026-09-23 review guide

[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] was filed with an unidentified speaker and no inferred identity.
Its claims match this summary point for point: trunk and leaf, the unchanged control experience, gates at integration points, a fresh reviewer, generated tests that prove nothing, merge readiness separated from launch readiness with the 80/20 estimate, and a small rollout treated as a safety check rather than an experiment.
The two files are most likely two derivations of the same talk, so the pair counts as **one voice, not two corroborations**.
What this summary adds is the speaker's identity as he states it, the talk's own order, and its explicit marking of opinion versus rule.
The guide's sample PR template and extra operational advice remain compiler material; this summary confirms that the speaker's own template is not in the transcript.
The match is an inference from content; neither file names the other.

**Speaker identified (2026-10-14).** hcho identified the creator of [[ai-era-50-career-tips]], a Meta staff engineer who teaches Claude Code and Codex and names "agentic validations" and "agentic tooling" as core skills, as John Kim.
This talk's "John," a Meta senior staff engineer with a tutorials channel, is treated as the same person on that identification plus the matching name, employer, channel, and vocabulary; see [[john-meta-engineer]].
The transcript itself still gives only the first name.

## Evidence limits

- The video's real title, URL, publication date, and timestamps are not supplied; the filed title is descriptive.
- The speaker is identified only as "John," and his credentials are self-described.
- The summary is caption-derived. Its Appendix A flags uncertain restorations with `[?]`, including the `/code-review` command name, the "ChatGPT Codex Connector," "goals" for PR babysitting, "agentic garden," the "advance cards" reducer action, and the "AI or Not" demo app.
- AI review being "better than most humans," the 80/20 time split, and "the agents will cheat" are his experience and opinion, with no measurements.
- On-screen examples (tests, the save-card screenshot, the reducer, Codex lint comments) are described only as narrated.
- He links to his own related videos and offers his own PR template; no product is sold in the summary.
- Tool commands are as he named them. A later check of current docs (2026-10-12) is recorded in [[agentic-coding-workflow-idea-to-review]].

## Connections

- [[risk-based-agent-governance]] - the trunk/leaf tree, three safety questions, and review-depth knob, now with a named speaker.
- [[feature-gating-from-day-one]] - gating as a planning decision that buys lighter review later.
- [[proof-in-the-pr]] - evidence replaces line-by-line reading for leaf changes.
- [[fresh-context-review]], [[adversarial-code-review]], and [[self-referential-bias]] - why the producing agent cannot be the reviewer.
- [[merge-ready-vs-launch-ready]] - the 80/20 split and the gated canary.
- [[get-out-of-the-loop]] and [[read-what-the-agent-writes]] - a named practitioner who reads more code than before, not less.
- [[agent-testing-instructions]] - tests count as proof only if they would fail when the requirement breaks.
- [[verification-signal-picks-the-mechanism]] - PR babysitting is a recurring loop, not a goal with an exit check.
- [[claude-code]] and [[codex]] - the two default reviewers he endorses.
- [[agentic-engineering]] - the verification pillar of the area hub.

## Possible project applications

These are Mandu's suggested applications, not claims that the projects already work this way.

- [[projects/RepToday/README|Rep Today]]: an App Store binary cannot be rolled back quickly, so only server-side gates (the Coach endpoint, remote configuration, telemetry) answer "can I roll it back?" with a confident yes. Code compiled into the binary is closer to a one-way door until the next review cycle. The TestFlight cohort is a safety check in his sense, which matches the thesis rule that no rate is judged on fewer than 200 users.
- [[projects/Purvia/README|Purvia]]: the chunk-level ACL predicate inside retrieval is trunk by every one of his tests (shared, consequential, hard to undo once data leaks), so it earns a full human read whatever the eval suite says.
- [[projects/Immerse/README|Immerse]]: the capture path every Camera shares is trunk; a single Camera's look is a leaf only if it is isolated behind its own selection path.

## Source

- Title as supplied: "Do You Still Read Your Code? Agentic Code Review Strategies" (descriptive; the actual video title is not in the transcript).
- Speaker: John, self-described senior staff software engineer at Meta; no surname given.
- URL: not supplied.
- Raw: [[projects/Education/AI/AI_Wiki/raw/agentic-code-review-strategies|Preserved Markdown summary]] (saved verbatim in `raw/`, immutable).
- Original inbox filename: `101226_agentic-code-review-summary.md`; the `101226` prefix is the supply date, not a verified publication date.
- Ingested: 2026-10-14, the first of three sources hcho asked to file in one batch.
