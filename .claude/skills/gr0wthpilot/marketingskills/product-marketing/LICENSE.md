# License and source

This folder is a modified copy of `skills/product-marketing/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-24 for Gr0wthPilot and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
There is no `MEMORY.md` or `## Memory` section, since Gr0wthPilot's own `MEMORY.md` covers its phase skills.
The changes from upstream are listed under "Changes from upstream" below.

## Upstream license

```
MIT License

Copyright (c) 2025 Corey Haines

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Changes from upstream

In `SKILL.md`:

- Added the "Gr0wthPilot copy: read first" block under the title.
- `description`: cut the 'what have we learned,' and 'log this learning,' triggers (the Learnings section is cut) and the closing clause "it creates `.agents/product-marketing.md` that all other skills reference for product, audience, and positioning context", and added what this copy does in Gr0wthPilot.
- Opening: "The document is stored at `.agents/product-marketing.md`." now reads "The document is the Candidate Package's `01-research/product-facts-brief.md`."
- Step 1: the check for `.agents/product-marketing.md`, `.claude/product-marketing.md`, and the legacy `product-marketing-context.md`, with the offer to move one to the canonical location, now checks only for the Candidate Package's `01-research/product-facts-brief.md`.
- Step 1, "If it exists": "Ask which sections they want to update" now reads "Decide which sections need updating".
- Step 1, "If it doesn't exist": "offer two options" now reads "auto-draft it".
- Step 1, option 1: cut "The user then reviews, corrects, and fills gaps."
- Step 1: cut option 2 ("Start from scratch: Walk through each section conversationally") and "Most users prefer option 1. After presenting the draft, ask: "What needs correcting? What's missing?"".
- Step 2, "If auto-drafting": cut steps 3 and 4 ("Present the draft and ask what needs correcting or is missing" and "Iterate until the user is satisfied").
- Step 2: cut the whole "If starting from scratch" walk-through ("Walk through each section below conversationally" and its four steps).
- Sections to Capture: cut "14. Learnings" ("Start this empty. It fills up as work ships").
- Step 3: "create `.agents/product-marketing.md` with this structure" now reads "create the Candidate Package's `01-research/product-facts-brief.md` with this structure".
- Step 3 document structure: cut the `## Learnings` heading, its "Decisions and tested lessons" line, and its table.
- Step 4: cut "Ask if anything needs adjustment".
- Step 4: "Save to `.agents/product-marketing.md`" now reads "Save to the Candidate Package's `01-research/product-facts-brief.md`".
- Cut "Maintaining Learnings" (the entry format, what earns a place, when to retire an entry, and who writes rows).
- Tips: cut "Ask for examples" and "Validate as you go".

In `references/brand-voice.md`:

- "Build the profile from evidence", step 4: "ask someone who knows the brand which is yours" now reads "ask a fresh agent, given only the profile, which is yours".
- Step 5: "Confirm with the user." now reads "Log the choice.", and "You can infer a draft from samples, but the user decides." now reads "You can infer a draft from samples; log it `[DECIDED BY AGENT]` with the rejected alternative in the Candidate Package's `decisions-log.md`."
- "Personal voice": "for example `.agents/voice/<name>.md`" now reads "for example `01-research/voice-<name>.md` in the Candidate Package".
- "How other skills apply it", when samples conflict: "Raise it with the user, log it in the **Learnings** section of the context file, and update the profile if they agree." now reads "Update the profile, and log the decision `[DECIDED BY AGENT]` with the rejected alternative in the Candidate Package's `decisions-log.md`."
