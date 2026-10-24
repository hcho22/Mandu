# Truth policy: formats the checks read

The Founder's reading of "invent nothing": creative work (names, taglines, visuals, copy, the deliverable nobody expects) is invented freely; facts, numbers, quotes, and competitor details are never invented, each needs a link fetched during the run, and every guess is labeled an assumption with its reasoning.

## sources.md and sources.d/

Each line is one URL:

```
- https://apps.apple.com/us/app/hipstamatic/id342115564 - fetched 2026-10-24T16:05Z - title, price, and rating count of Hipstamatic's US listing
```

The time is the UTC time you fetched it (`date -u +%Y-%m-%dT%H:%MZ`).
Agents write their own fragment, `sources.d/<lane-or-task>.md`; `scripts/merge_sources.py <package>` rebuilds `sources.md` from the fragments, one section per fragment, and the check refuses a fragment line `sources.md` lacks.
A URL counts as fetched in the run only when the guard's WebFetch log shows a 2xx for it, or it appears in last30days output whose SHA-256 the `gp-last30days` wrapper recorded.
WebFetch upgrades http to https and the check compares URLs the same way, without fragments or trailing slashes.

Some URLs in the package are not claims: the Product's own planned site, a schema.org context, an SVG namespace, a font.
Namespace and font hosts are exempt already; list any other prefix in `sources-exempt.md` with the reason:

```
- https://immerse.example/ - the Product's planned site address, used in drafts; not a claim
```

## Source keys

A file that cites one source many times may define it once, as a Markdown reference line, and cite its key:

```
[L]: https://apps.apple.com/us/app/hipstamatic-analog-camera/id1450672436

| Field | Observed | Source |
| --- | --- | --- |
| Rating | 4.6 out of 5, 2.8K ratings | L |

Membership costs $29.99 a year [L].
```

A key counts only in the file that defines it, cited as `[L]` in a line, or as the bare key in a table's Source column; the URL itself still goes in `sources.md`.

## Citing the Product

A fact about the Product cites where you read it in its repository, as `repo:path`, path relative to the repository root:

```
- Each roll holds 24 exposures (repo:Packages/FilmCore/Sources/FilmCore/Roll.swift).
```

## Labels

Put the label in the same line or text block as the claim it qualifies.

- `[ASSUMPTION: why]`: a number or fact you could not source, with the reasoning.
- `[PROJECTION: basis]`: a forecast, with what it rests on.
- `[TARGET]`: a pre-registered threshold the run sets, such as a success signal or a kill line.
- `[PROPOSAL]`: the run's own pick of something the Founder holds, such as a price.
- `[DECIDED BY AGENT]`: a decision the Founder would otherwise have been asked; it also goes in `decisions-log.md`.

A link to a file in `01-research/`, to `sources.md`, or to the claims ledger also counts as a citation, because those files carry the URLs.

## The claims ledger

`08-redteam/claims-ledger.md` holds every load-bearing claim: any fact a positioning line, a price, an Angle, a channel ranking, or a kill criterion rests on.

```
| ID | Claim | Source | Skeptic verdict | Shipped as |
| --- | --- | --- | --- | --- |
| C04 | Hipstamatic charges $29.99 a year in the US | https://apps.apple.com/us/app/hipstamatic/id342115564 | STANDS - the listing shows it today | as stated |
| C09 | Most film photographers shoot fewer than two rolls a month | https://www.reddit.com/r/AnalogCommunity/comments/... | WEAKENED - one thread, not a survey | "Some film photographers say they shoot a roll a month or less" |
| C11 | No competitor develops photos on a delay | https://... | REFUTED - Gudak and Huji both delay | cut |
```

The skeptics write it (`workflows/skeptics.js`); a REFUTED claim is cut everywhere and its "Shipped as" says `cut`; the claim audit refuses a REFUTED claim of six or more words that still appears in a deliverable.

## What the claim audit refuses

`scripts/claim_audit.py` reads every Markdown, HTML, and text file except `sources.md`, the ledger, `run-evidence/`, and the raw last30days output.
It refuses a sentence, table row, or text block holding any of these with no citation and no label:

- a percentage, a price, a multiplier ("3x");
- a count of people, users, downloads, installs, reviews, ratings, followers, customers, or similar;
- a star rating or a ranking ("ranked #3", "#1 in Photo & Video");
- "studies show", "according to", "research shows", "experts say";
- "the only app", "the first app", "no other app", "market leader", "most popular", "fastest-growing";
- a blockquote with no URL in it or on the line after it.

Table cells under a column whose header names a score, weight, signal, kill criterion, target, threshold, floor, budget, goal, margin, rank, day, slot, duration, length, or size are the run's own numbers and are skipped.
