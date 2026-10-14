---
type: concept
tags: [agentic-engineering, agents, verification, orchestration, anthropic]
status: developing
source-count: 2
last-updated: 2026-10-14
---

# Long-Horizon Agent Runs

Agent runs measured in **days and weeks** rather than minutes, documented with two production examples in [[building-at-the-frontier]].

The behavioral change [[boris-cherny]] names as the headline of Claude Opus 5 is **duration**.
The model runs for very long periods without stopping, especially paired with auto mode, and it keeps going because it understands the task needs finishing - not because scaffolding forces it to.

## The two case studies

**Bun, Zig to Rust, 11 days.**
[[claude-code]] runs on Bun, which was written in Zig with manual memory management.
The Bun team had been using Claude to fuzz for memory leaks one case at a time; that was the ceiling.
A team member re-ran a harder standing test with each model generation, and starting with Fable the model could do it.
The setup was **a mature test suite as the verifier**, **one prompt** run as a dynamic workflow, and 11 days of runtime.
The result is **in production** as what Claude Code runs on today.
Not one-shot - there was steering - but previous models could not have done it even with steering.

**Electron to Swift, still running at 15 days.**
Boris bootstrapped the environment conversationally through Claude in Slack (hooking up a macOS runner, granting repo access), then gave the entire prompt: *rewrite the Electron app in Swift; run the Electron app in the macOS VM; screenshot it; compare pixel by pixel against the Swift version; don't stop until you're done.*
Still going at the time of the interview.

## The three ingredients

That is the whole recipe, and it is short:

1. **A hard task.**
2. **A verification loop the model can execute itself** - run it, screenshot it, compare pixel by pixel.
3. **A stopping condition** - "don't stop until you're done."

**"You don't need the fancy stuff."**
Boris names `/go` and `/loop` as helpful but not required.

## Key points

- **Verification is the enabling ingredient, not duration.**
Bun worked because a mature test suite made "did you do the right thing?" answerable automatically.
Pick problems where the oracle already exists, or **build the oracle first**.
- The Electron run has spawned an estimated thousands to tens of thousands of agents via [[dynamic-workflows-as-test-time-compute]].
- Claude decided on its own to **live-blog the run**, creating a Slack channel and posting progress screenshots every few minutes - an unprompted observability behavior.
- Human equivalent for the Bun rewrite, per the panel: over a year with the best engineers.

## A third run, with a different recipe (2026-10-14)

[[stop-prompting-design-loops-and-goals]] adds a smaller and less proven example from outside a frontier lab.
[[john-meta-engineer]] had one goal running about 22 hours at recording, rebuilding his YouTube production workflow as a website plus an iOS app.
It was "not close to done," so this is a run in progress, not a result, and it is a side project where he reviewed only at a high level.
His three ingredients are not Boris's three:

| [[boris-cherny]] ([[building-at-the-frontier]]) | [[john-meta-engineer]] ([[stop-prompting-design-loops-and-goals]]) |
|---|---|
| A hard task | Agentic tooling: MCP or CLI access so the agent never stops to ask (Vercel already logged in, with skills) |
| A verification loop the model can run on itself | Context: a queryable second-brain CLI over his projects and writing |
| A stopping condition | Exit criteria: design screens the agent compares its build against, plus simulator self-QA |

The lists share one item, a target the agent can check itself against, and differ in what each takes for granted.
Boris treats the environment as setup: he hooked up the macOS runner and repo access through Claude in Slack before giving the prompt.
John makes that environment the main work, because a run outside a frontier lab stalls on roadblocks (logins, deploy access, missing context) long before it reaches the model's limits.
His rule is to work out the roadblocks the agent may hit and give it the tools to get past them.
He also writes safety into the goal text rather than the environment (push at checkpoints, archive instead of delete), which is governance by instruction: fine for an internal side project, weaker than a boundary for anything consequential ([[capabilities-not-instructions]]).

## Synthesis

This is the strongest evidence in the wiki for [[product-overhang]] being real and large, and it relocates the bottleneck decisively.
For two years the limiting factor on agent autonomy was assumed to be **context and orchestration**, which is why the wiki accumulated pages on [[context-rot]], [[sub-agents]], and mechanism selection.
Boris's claim is that at the frontier the limiting factor is now **whether the task has a self-executable oracle**, and everything else is scaffolding that the model is outgrowing.

Note the tension this creates with [[verification-signal-picks-the-mechanism]]: Tharic's rule was that the verification signal picks your *orchestration primitive*.
Boris's version is that a good enough verification signal means you may not need a primitive at all.
Both agree the signal is what matters; they disagree on how much machinery it has to be wrapped in.
The reconciliation is probably model tier - the machinery earns its keep below the frontier - but that is inference, not something either source states.

For hcho the practical filter on any ambitious agent task is: **what would the agent check itself against, and can it run that check unattended?**
If the answer is "a human looks at it," the run will be short no matter how good the prompt is.

The third case adds a second question to that filter: **what would stop the agent before it ever gets to check itself?**
A missing login, an unconnected deploy target, or context the agent has to hunt for ends a run as surely as a missing oracle.
The combined recipe is a self-checkable target, the tools to reach it without asking, and the context to aim it.
The run is also only as trustworthy as its check: a design-screen comparison or a test suite that passes on wrong output lets the goal stop on a false success.
