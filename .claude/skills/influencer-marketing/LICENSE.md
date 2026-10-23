# License and source

This folder is a modified copy of `skills/influencer-marketing/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-23 and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
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

- Added the "Mandu copy: read first" block under the title, and the `## Memory` section at the end.
- `description`: the opening "run influencer, creator, or ambassador partnerships to promote their product" now reads "find and vet creators or influencers to approach about their product"; removed the triggers for the cut parts (deal structuring, sponsorships, newsletters, ambassador and creator programs, UGC, thought-leader ads, gifting and seeding, whitelisting, Telegram ads, influencer pay, the ad-creative and referrals pointers) and the "briefing creators" and "measuring ROI" triggers; added the 'creator scouting' and 'vet a creator' triggers, what this copy is for in Mandu, and that it never fetches a page its `robots.txt` disallows.
- Opening paragraph: removed "and paid posts in Telegram channels", "structure fair deals", and the closing "measure real ROI" clause.
- "Before Starting": the `.agents/product-marketing.md` check now points at the product's Go-To-Market Package, and the budget question ("budget and whether it's cash or product") is removed.
- Added an "In Mandu" note under the untrusted-data line, before the vetting checklist, and after the "Tool Integrations" paragraph, pointing to the read-first rule that each host's `robots.txt` is binding.
- Vetting checklist: "Ask for past campaign results" now reads "Look for past campaign results the creator has published".
- Section 4: "Build the disclosure requirement into the brief and the agreement" now says the shortlist notes the disclosure for each pick, and "Give them what's true and let them speak it in their voice" is removed.
- Cut "The Influencer ↔ Ambassador Spectrum" (paid, affiliate, gifted, and ambassador models, and the UGC, performance-paid, and newsletter-sponsorship paragraphs).
- Cut the Telegram-channels vetting bullet and the Telegram line under "Tool Integrations" (Telegram channel ads are bought placements).
- Cut "3. Structuring the Deal" (compensation, rates, usage rights and whitelisting, exclusivity, the paid agreement); the later sections keep their upstream numbers.
- Cut the "Whitelisting performance" measurement bullet.
- Added an "In Mandu" note at the head of sections 2, 5, and 6 and of the run-of-show "Outreach & Deal", "Execution", and "Post-Campaign" groups, pointing to the read-first rule that this copy drafts no creator messages, outreach, or briefs and measures no results.
- Cut "Ambassador Program Design" (a paid or perks program by its own description).
- Cut the "Not securing usage rights", "Scripting the creator", "No attribution plan", "One-and-done", and "Judging on EMV / reach" common mistakes.
- Run-of-show: cut "Agree deliverables, timeline, and compensation type in writing", "Lock usage rights (paid-ad whitelisting window) and exclusivity terms", and "Decide: one-off, repeat, or move to a retainer / ambassador program"; "Put the disclosure requirement in the agreement" is replaced by a Sourcing item that notes the disclosure for each pick.
- Related skills: cut **referrals** (payout rails), **ad-creative** (paid ads from creator content), **cold-email** (creator outreach), and **attribution** and **ai-seo** (measurement); **customer-research** no longer says "and ground the talking points".

In `references/`:

- Left out `paid-ads-creator-program.md` (performance-paid), `newsletter-sponsorships.md` (newsletter sponsorship), `ugc-creator-program.md` (a paid creator program), and `telegram-channels.md` (buying posts in Telegram channels).
- Added `creator-scouting.md`: the creator-scouting section of `skills/marketing-loops/references/loop-catalog.md` (lines 402-415 at the same commit), quoted unchanged under the `robots.txt` rule and Mandu steps that make it a one-off search hcho runs by hand.
