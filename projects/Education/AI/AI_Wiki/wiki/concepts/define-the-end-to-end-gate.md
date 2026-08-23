---
type: concept
tags: [agentic-engineering, testing, verification, scope, e2e]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Define the End-to-End Gate

**State the done condition as a concrete end-to-end scenario, and it will force the plan to expose what's actually missing.**

From [[agentic-full-stack-build]].
Kun's MVP gate was not "the app is built." It was:

> the iOS app running in the **simulator**, signing in with his **real Apple account**, connected to the **real backend on the VPS**.

Framing the test that way **immediately surfaced the remaining gaps** - the app was still on mock data, which no status report had said.

**It converts vague "it's built" reports into a concrete remaining-work list.**

## The reusable prompt

The one he says he reuses constantly:

> *"Try to do some end-to-end testing and figure out what the actual bug is. Don't ask me unless there is something only I can do."*

His reasoning: agents are very capable **as long as they keep trying** - "they just need some encouragement."
The second sentence is doing the real work, since it removes the agent's cheapest escape hatch, which is asking the human.

The actual final run was exactly the gate: sign in with Apple using his real account, add $10 in the parent view, see $10 in the child view, sign out and back in to confirm the data came from the server.

## Why a real gate beats a status report

- "Built" is a claim about **code existing**. The gate is a claim about **the system working**, and only one of those is checkable.
- Every shortcut the agent took - mock data, wrong hostname, missing DNS - is invisible to a status report and fatal to the gate.
- The gate names the **real** dependencies (real Apple ID, real VPS, real HTTPS), so the plan cannot satisfy it with a stub.
- It is stated **before** the work, so it shapes the plan rather than auditing it afterward.

## Synthesis

This is the specific, agent-era version of a rule hcho already holds globally: reproduce and verify in an E2E setting as close to the real user experience as possible.
What this source adds is that the gate is most valuable **as a planning instrument, not a testing instrument**.
Stated up front, it makes the agent's own plan reveal its gaps; stated at the end, it is just a test.

It sits directly alongside [[agent-testing-instructions]], which says agents default to shallow tests unless you write down how you would test it.
This compresses that to a single scenario with real dependencies named, and adds the "don't ask me unless only I can do it" clause that keeps the agent from bailing out mid-loop.

It is also the practical form of what [[elicitation-over-prompt-engineering]] and [[long-horizon-agent-runs]] identify as the binding constraint: a stopping condition the agent can evaluate itself.
"Don't stop until pixel-perfect" and "don't stop until it signs in with my real Apple ID against the real backend" are the same instrument at different scales.

For hcho this is directly applicable to Rep Today's pre-submission work, where "provisioning done" is exactly the kind of vague status that hides missing pieces, and a gate ("a TestFlight build installs on a real device and completes the core loop signed in with a real Apple ID") would surface them.
