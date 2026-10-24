# License and source

This folder is a modified copy of `skills/ai-seo/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-24 for Gr0wthPilot and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
It has no `## Memory` section or `MEMORY.md`, since Gr0wthPilot's own `MEMORY.md` covers its phase skills.
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
- `description`: added what this copy does in Gr0wthPilot ("In Gr0wthPilot this copy reviews the Candidate Package's local landing page for readiness for AI search and writes `03-site/ai-seo-review.md`; it deploys, submits, and signs up for nothing."); no trigger phrases are cut, since no part of the skill is cut.
- "Before Starting": the `.agents/product-marketing.md` check now points at the Candidate Package's product-facts brief, and "read it before asking questions. Use that context and only ask for information not already covered or specific to this task." now says to read it before answering the questions and to answer the rest as the read-first "Never ask anything" rule says.
- "Before Starting": "Gather this context (ask if not provided):" now reads "Gather this context (answer from those sources; never ask):".
- AI Visibility Audit, Step 1: added an "In Gr0wthPilot" note after "then run each several times", pointing to the read-first "No new spending" and "Engine queries" rules.
- Pillar 3: added an "In Gr0wthPilot" note after the "Actions" list (Wikipedia, Reddit, roundups, third-party profiles, YouTube, podcasts, Quora), pointing to the read-first "Publish nothing" rule.
- "Monitoring AI Visibility": added an "In Gr0wthPilot" note at the head of the section ("Log it in a spreadsheet and track month-over-month"), pointing to the read-first "The Candidate Package is the only context" rule.

In `references/agent-readiness.md`:

- Added an "In Gr0wthPilot" note after "Run one before and after any agent-readiness work" (both scoring tools need a live domain), pointing to the read-first "The page is local" rule.

In `references/ai-attribution.md`:

- Added an "In Gr0wthPilot" note at the head of "Setup" ("Fix referral capture", "Ask people", "Join to outcomes in the CRM"), pointing to the read-first "Publish nothing" rule.

In `references/answer-accuracy.md`:

- Added an "In Gr0wthPilot" note at the head of "Fix the source first", making step 3 ("Fix your profiles") and step 4 ("Send the publisher the correct fact and a source") drafts for the Founder, pointing to the read-first "Publish nothing" rule.

In `references/okf.md`:

- Added an "In Gr0wthPilot" note at the head of "How to ship one": a bundle is built only by hand (option 3), and the web tool ("paste a URL or sitemap"), the plugin install, and "Hosting & discovery" are for the Founder after Handoff, pointing to the read-first "Publish nothing" rule.

In `references/platform-ranking-factors.md`:

- Added an "In Gr0wthPilot" note after Copilot's "What to focus on" list, making "Submit your site to Bing Webmaster Tools" and "Use IndexNow protocol" steps for the Founder, pointing to the read-first "Publish nothing" rule.

In `references/positioning-and-consensus.md`:

- Added an "In Gr0wthPilot" note at the end of "Make Every Profile Say the Same Thing" ("Fill in free profiles fully", "an afternoon of edits across profiles"), pointing to the read-first "Publish nothing" rule.
- Added an "In Gr0wthPilot" note after the "Managing the "Cons" Others Write" bullets ("ask the publisher to use a different con"), pointing to the read-first "Publish nothing" rule.

In `references/youtube-ai-citations.md`:

- Added an "In Gr0wthPilot" note at the head of "The anatomy" ("Upload cleaned captions", "pin a comment"), pointing to the read-first "Publish nothing" rule.
