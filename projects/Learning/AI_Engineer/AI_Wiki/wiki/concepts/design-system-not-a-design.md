---
type: concept
tags: [agentic-engineering, design, ui, taste]
status: seed
source-count: 1
last-updated: 2026-08-01
---

# Create a Design System, Not a Design

From [[agentic-full-stack-build]]: Kun deliberately had the design agent produce a **design system** rather than a one-off design.

Once the system is established, future components and screens can be built and changed without reinventing every element, and **consistency is guaranteed from that point on**.
It is the difference between one screen and an extensible UI vocabulary.

## What he gave it

- The product name.
- The GitHub repo URL, with a note that the repo contains **no source code** - only a README with the requirements.
- An instruction to figure out the main screens itself.
- **Explicit permission to challenge any prescribed user experience** and use its own judgment.
- The target feel: fun, educational, friendly for kids; good control and transparency for parents.

**Letting the design agent challenge the PRD is what produced usable screens** rather than a literal transcription of his requirements.

## The feedback loop

1. Review the generated system - brand icon, wordmark, palette, neutrals.
2. Flag specific component defects (text not centered) - fixed on the next pass.
3. The main critique came only after clicking through real screens: **"it doesn't feel like a children's app."**
4. Request **app icon options**, choose one, ask for refinement and for **icon images formatted for direct use in an iOS app**.
5. Export the whole thing as a project archive and hand the path to the build agent.

**Caution:** ask explicitly for iOS-formatted icon assets. iOS has specific size and format requirements the design tool won't satisfy by default.

**Model note:** Opus was overloaded so he ran **Sonnet**, and it worked out.
"Sonnet is not going to be able to come up with very, very clever solutions, but here I also don't think the problem is too complex."
See [[model-selection]].

## Synthesis

The generalizable idea is that **a system is a better agent deliverable than an artifact**, for the same reason a skill is a better deliverable than a good session: it constrains everything downstream without further human input.
Asking for a design gets you one screen and a fresh negotiation for every subsequent screen.
Asking for a system gets you a vocabulary that the build agent can extend on its own.

That is the design-side instance of [[build-the-machine-first]], and it is the same shape as [[building-skills]] - encode the judgment once, reuse it, rather than re-supplying taste every time.

The second idea is more surprising and worth holding: **inviting the agent to override the PRD improved the result.**
That runs against the instinct in [[dont-let-ai-be-your-architect]], which reserves architecture and interface for humans.
The reconciliation is probably domain - Kun kept the *system* architecture and cut scope aggressively ([[agent-over-engineering]]) while ceding *visual and interaction* judgment, on a product where he had no strong prior.
Knowing which of those you actually have taste about is the real skill, and [[taste-as-moat]] is the page it connects to.
