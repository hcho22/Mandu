---
type: entity
tags: [person, anthropic, claude-code, frontier]
status: established
source-count: 4
last-updated: 2026-10-14
---

# Boris Cherny

**Creator of [[claude-code]]** at [[anthropic]].
Promoted here from "engineer associated with" to creator on the strength of [[building-at-the-frontier]], a live fireside interview recorded the day after Claude Opus 5 shipped - the wiki's first source where he speaks at length rather than being cited by others.

## What shows up in the wiki

**From [[building-at-the-frontier]] (2026-08-01), his own account:**

- [[ablation-driven-development]] - delete the whole system prompt, add back only what repeatedly fails. "An eval measures; an ablation removes things to measure." Asked whether every AI-product builder should do this on every model release: **"100%."**
- [[product-overhang]] - capability nobody has built a product for, and the hobbling that hides it. Includes the [[claude-code]] origin story: strip the scaffolding, give the model the simplest possible harness.
- [[elicitation-over-prompt-engineering]] - the durable skill is a too-hard task plus self-verification. **"Verification is probably the single most important thing that people do not get right."**
- [[long-horizon-agent-runs]] - the Bun Zig-to-Rust rewrite in 11 days (now in production), and an Electron-to-Swift port still running at 15 days.
- [[dynamic-workflows-as-test-time-compute]] - orchestration as a scaling axis; "an algebra for agents," reflecting his functional-programming background.
- [[self-maintaining-codebase]] - 20-30 daily routines maintaining Anthropic's own products, from one-sentence prompts.
- [[evals-saturate-and-get-replaced]] - evals outlive the harness "but not by much"; budget for replacing them.
- [[principles-over-constraints]] - the 80% system-prompt cut, confirmed from the person who ships it.
- [[red-team-your-agent]] - the claim that Opus 5 is not demonstrably prompt-injectable, with his own caveats attached.

**From earlier sources:**

- [[build-for-the-model-of-the-future]] - cited in [[ai-era-50-career-tips]]; now stated in his own words with a procedure attached.
- Named in [[designing-loops-and-workflows]] as the author of **`simplify`**, a repo cleanup tool. (Tool name inferred from an auto-captioned transcript at medium confidence.)
- Credited in [[loops-to-run-your-business]] as one of the people who popularized "loop engineering" on X.
- Cited in [[stop-prompting-design-loops-and-goals]] (2026-10-14) as saying in interviews that he runs loops and that his job is to write loops; the speaker's paraphrase, with the interview not named.

## Positions worth knowing

- **The model is "a living creature."** Each generation has a different personality; you get to know it, then adjust the harness to fit. Traditional engineering - big up-front design, multi-year re-architectures - does not describe this.
- **Being empirical is what separates the best.** Forget past models, forget the CS theory, watch the model attempt the task. The people best at **letting go of their priors** are the ones succeeding.
- **Experienced engineers struggle most**, because over-specifying is what previous systems demanded.
- **On where to learn:** "Maybe don't listen to the LinkedIn influencers. Don't read Twitter." There is no one weird trick.
- **"Coding is solved"** - narrowed by him to the kind of coding he does. Still hard: deep systems codebases, distributed systems, pixel-level UI verification.

## Notes

The wiki's most consequential single voice on [[agentic-engineering]], and the one most likely to invalidate its own earlier pages - his entire method is built on deleting what worked for the last model generation.
Read alongside [[tharic]], the other Anthropic primary source: Tharic describes how to use the orchestration primitives, while Boris argues the frontier is eating them.
