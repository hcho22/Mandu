---
type: concept
tags: [agent-ops, solo-building, systems, strategy]
status: developing
source-count: 2
last-updated: 2026-10-14
---

# Build the Machine First

The closing thesis of [[one-person-company-with-agents]]: most of the work now is building the *system that does the work*, which inverts old startup advice to skip systems and rush an MVP.

## Key points

- Invest up front in your SDLC, documentation, reference files, crons, and skills; wire them together, and you do "the work of 10 people" - but "the setup is pretty brutal."
- Building the machine yourself means you understand the work, can refine it, and only then augment with more agents or an agent-augmented human.
- **Understand and do every job before you hire to fill it.**
- Corollary: building features is "almost trivial now"; go-to-market (users, revenue, adoption) is the real skill.

## The harness is the leverage (2026-10-14)

[[stop-prompting-design-loops-and-goals]] states the same thesis at the level of a single agent run.
[[john-meta-engineer]] calls the game "building harnesses and environments" so agents do the work consistently, over time, at higher accuracy.
His measure is a ratio he calls "token maxing": as few of your own tokens in as possible, as many tokens of work out.
The example is ChatGPT Deep Research, where one question yields far more output because of the tooling behind the prompt, and his own 22-hour goal, which worked only because the skills, MCPs, deploy access, and context CLI already existed.
"Make me an app" can work, he says, but only because of the pre-work.

His use of "token maxing" differs from [[token-maxing-with-agents]], where Theo means spending the whole flat-rate allowance; the shared assumption is that the human's input is the scarce resource.

## Synthesis

This is the strategic statement of the [[ai-operating-system]] idea at company scale, and it connects to [[self-updating-config]] (the machine that improves itself) and [[everything-is-a-pr]] (the machine's SDLC).
It sits interestingly against [[ship-fast-learn-from-users]]: both invert classic MVP advice, but in opposite directions - Pigford ships the whole product fast and skips systems; Carson builds the system first and ships continuously. The common thread is that AI collapses build cost, so the leverage moves to either speed-to-users or systems-that-scale-you.
For hcho, "build the machine first" is a fair description of what Mandu + AI_Wiki already are.
