# License and source

This folder is a modified copy of `skills/social/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
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
- `description`: "creating, scheduling, or optimizing" now reads "creating or optimizing"; cut "or wants to do social listening and engagement triage" and the 'social scheduling,' 'social listening,' 'brand mentions,' 'competitor monitoring,' 'top posts to comment on,' and 'find people asking for,' triggers; "Use this for social content, repurposing, scheduling, video scripts, and listening." now reads "Use this for social content, repurposing, and video scripts."; and added what this copy does in Gr0wthPilot ("In Gr0wthPilot this copy drafts the Launch Set and the Test Kit as local files in the Candidate Package; it never posts, schedules, comments, or sends.").
- "Before Creating Content": the `.agents/product-marketing.md` check now points at the Candidate Package's product-facts brief, and "read it before asking questions. Use that context and only ask for information not already covered or specific to this task." now says to read it before answering the questions and to answer the rest as the read-first "Never ask anything" rule says.
- "Before Creating Content": "Gather this context (ask if not provided):" now reads "Gather this context (answer from those sources; never ask):".
- "Engagement Strategy": added an "In Gr0wthPilot" note at the head of the section (responding, commenting, reposting, and DMs), pointing to the read-first "A calendar, not a queue" rule.
- "Engagement Strategy": cut the "For surfacing *which* posts to comment on" paragraph, which pointed to the left-out `references/listening.md`.
- "Scheduling Best Practices": added an "In Gr0wthPilot" note at the head of the section, pointing to the read-first "A calendar, not a queue" rule.
- Cut "Publishing From Your Agent" (asking the user what they schedule with, then creating and scheduling posts through a scheduling tool's MCP server or API and pulling post-level stats).

In `references/reverse-engineering.md`:

- Step 2, "SCRAPE": added an "In Gr0wthPilot" note after the "Tools" list (Apify, Phantom Buster), pointing to the read-first "No new spending" and "Invent nothing factual" rules.

In `references/`:

- Left out `listening.md` (daily triage of which posts to comment on, pulled from Reddit, Hacker News, Bluesky, and signed-in LinkedIn and X browser sessions, with a source list kept in `.agents/listening-sources.md`) and `listening-sources-template.md` (the template for that source list).
