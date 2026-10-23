# Creator scouting, once and by hand

**robots.txt is binding.** Before reading any page, the agent checks that host's `robots.txt` and never requests a path it disallows, directly or through an archive or mirror.
The agent searches only through a web search engine, and reads only pages `robots.txt` allows; anything disallowed (for example Instagram profiles, and TikTok and YouTube search) hcho reads and copies by hand.

This is how to find smaller creators to vet: accounts of about 5,000 to 10,000 followers already posting about the problem the product solves.
In Mandu it is a one-off search hcho runs by hand in his own session, not a recurring loop.
The agent builds the shortlist only from what was read that way: what hcho copied by hand, and pages `robots.txt` allows.
Ignore the upstream cadence, watchlist state, and cooldown below; there is no schedule, no stored state, and nothing to re-run.

How a search runs here:

1. hcho searches the platforms the package's channel plan uses for small accounts already posting about the problem, and copies what he reads for each candidate (profile, recent posts, and comments) with its address and the date he read it.
2. The agent vets each from that copy, and from pages `robots.txt` allows, with section 1 of `SKILL.md`: the audience-alignment test, the vetting checklist, and the fake-follower check.
3. The agent gives hcho a shortlist with a short note per creator: audience fit, engagement, brand safety, whether they mention the category unprompted, and that early access is a material connection the creator must disclose if they post, so hcho can tell them when he gives access.
   Leave out first-touch drafts: gr0wthlab drafts creator messages, from the creators the package's `06-channels/channel-plan.md` names.
4. hcho decides whether a creator goes into the channel plan, and edits it himself in Mandu.
   Nothing is sent, and no creator is paid or gifted.

## Upstream text

From [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `skills/marketing-loops/references/loop-catalog.md`, lines 402-414, at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b`, MIT License, Copyright (c) 2025 Corey Haines (see `../LICENSE.md`).
Quoted unchanged for reference; the steps above govern where they differ.

> ### The creator-scouting loop
> - **Check cadence**: Monthly
> - **Acts when**: A creator with roughly 5–10K followers posts about your space and fits your audience.
> - **Purpose**: Build relationships with creators before they grow, when they're more reachable and cheaper to work with.
> - **Skills used**: `influencer-marketing`, `social`
> - **Loop body**:
>   1. Search X, Instagram, TikTok, LinkedIn, and YouTube for small accounts already posting about the problem you solve.
>   2. Vet with the influencer-marketing skill's audience-alignment test and fake-follower checks.
>   3. Add qualified creators to a watchlist; draft a first touch (a genuine reply, a product invite) for the best fits.
> - **Self-check**: Is their audience your buyer, or just adjacent? Reach without fit doesn't count.
> - **State / idempotency**: Track every creator scouted, contacted, and declined; never re-pitch inside the cooldown.
> - **Stop / bail-out**: No qualified creators → skip. Human-approve all outreach.
> - **Output**: A creator watchlist with notes and drafted first touches.
