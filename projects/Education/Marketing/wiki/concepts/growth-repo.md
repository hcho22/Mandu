---
type: concept
tags: [marketing, context, memory, agents, knowledge-management]
status: seed
source-count: 1
last-updated: 2026-10-14
---

# Growth Repo

A repository, or simply a structured folder, that holds a company's marketing memory so every AI tool reads the same context and every week's learning is kept.
From [[projects/Education/Marketing/wiki/sources/becoming-a-marketing-engineer|Becoming a Marketing Engineer]], where it is the first thing a [[marketing-engineer]] builds ("growth OS"); the speaker says a plain folder works for non-technical people.

## The problem it fixes

People ask a chat tool for ten posts, paste one into a doc, and the work disappears.
Next week the AI starts from scratch, without the performance data, the founder's voice, the sales-call objections, or the language that earned replies.
The repo is the difference between "AI helped me make a thing" and "AI is helping the whole company get smarter."

## Suggested layout

| Folder | Contents |
|---|---|
| customer truth | Sales-call notes, support tickets, churn notes, interviews, live product feedback ([[customer-truth-file]]) |
| content engine | Founder voice guide, winning hooks, scripts, notes on what performed ([[content-source-library]]) |
| outbound engine | Ideal customer profile, account research, trigger events, approved angles, a banned-language list |
| creative testing | Ad angles, landing-page tests, hooks, offers, results |
| agents | The job definitions for each AI worker |

The source's minimal version is smaller: a folder with customer truth, founder voice, experiments, and agent jobs (it says five files and names four), plus 20 real customer notes.

## Key points

- **Context files beat a bare prompt.** The upgraded prompt reads the customer truth file, the voice file, and the last five posts that drove qualified replies before drafting; the speaker presents this as the main reason output quality jumps.
- **Corrections go into the repo.** A fake-sounding first line becomes a rule; generic intros get three good and three bad examples; an unsupported claim gets the rule that every insight needs a quote, link, or source.
- **A banned-language list** keeps outbound from sounding "like an overexcited SDR who just discovered personalization."
- **The tools change; the repo and the workflow are what persist.**

## Synthesis

This is [[projects/Education/AI/AI_Wiki/wiki/concepts/own-the-context-layer|Own the context layer]] at company scope: the generation tool is rented, and the folder holding the context, rules, and results is the asset.
It is broader than [[content-source-library]], which holds an author's reusable positions and stories; a growth repo adds customer evidence, outbound targeting, experiment results, and agent definitions.
The correction habit is the same compounding loop AI_Wiki records for agent instruction files ([[projects/Education/AI/AI_Wiki/wiki/concepts/self-updating-config|Self-updating config]]), aimed at marketing output.

Mandu's observation: [[projects/RepToday/README|Rep Today]]'s go-to-market package (`projects/RepToday/gtm/`) already has this shape, from mined pain research and brand rules to a seed angle bank and a creative loop, and it is the context [[projects/gr0wthlab/README|gr0wthlab]] reads.
Its evidence rule is stricter than the source's: every seed angle carries a verbatim quote and a source URL.
Its gap is the one the source's minimal version is designed to close quickly: no result has been recorded, because nothing has been published.

## Source

- [[projects/Education/Marketing/wiki/sources/becoming-a-marketing-engineer|Becoming a Marketing Engineer]] - the growth OS folder, its layout, the prompt upgrade, and correction-as-memory.
