---
type: concept
tags: [agentic-engineering, agents, verification, orchestration, anthropic]
status: developing
source-count: 1
last-updated: 2026-08-01
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
