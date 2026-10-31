# Playbook format

`gt render` turns `playbook.md` (full mode) or `content.md` (content mode) into one self-contained HTML file, and `gt check` reads the same file.
Write the report in this format so both work.

## Markdown that renders

- One `#` title, then `##` sections (they make the contents list) and `###` subsections.
- Paragraphs, `-` and `1.` lists (indent a nested list by two or more spaces), `|` tables with a `|---|` separator row, `>` quotes, `**bold**`, `*italic*`, `` `code` ``, `[text](url)` links, and `![alt](img/... or capture/...)` images.
- One sentence per line; lines in a paragraph join into one paragraph.
- The words SEEN and INFERRED, in capitals, render as labels.
- No em dashes; `gt check` refuses them.

## Directives

- `<!-- gt:growth-chart -->` draws `data/growth.csv` (the ratings total by month) with every move in `data/moves.csv` pinned on it, a hover tooltip, and a table view.
  `<!-- gt:growth-chart key=ratings_per_day -->` draws another column.
- `<!-- gt:contact-sheet channel=youtube -->` lays out the top-quarter and bottom-half posts of `data/youtube-posts.csv` that have an `image`, side by side.
  `<!-- gt:contact-sheet channel=ads source=ads-google metric=days_shown -->` tiers another data file by one of its columns first.
- `<!-- gt:gallery dir=img/appstore limit=10 -->` shows every image in one run folder, in name order.

## Citations

- Every URL in the report must be one this run read (`sources.csv`), one a response the run read named (a value in `data/*.csv`), or one hcho captured (`capture/captures.csv`).
- A line with SEEN carries its source on the same line: a link, or a run file such as `data/stack.csv` or `capture/tiktok/01.png`.
- Cite a Wayback snapshot as `https://web.archive.org/web/<timestamp>/<page>`.

## Required sections, full mode

`## The path`, `## Plays`, `## Things to skip`, `## Timeline`, `## By channel`, `## 14-day plan`, and `## Method notes`, in any order after a short summary.

## Required sections, content mode

One `##` section per channel, `## Across channels`, and `## Method notes`.

## A play

Each play is a `###` heading under `## Plays`, with these lines and a prompt block:

````
### 1. Ready-on-open as the hook

- **Stage:** pre-launch, social PMF test
- **Evidence:** SEEN ... ([source](https://...)); INFERRED ...
- **Effort:** day
- **First result:** 7 days - saves per post
- **Cost:** $0

```prompt
In Mandu, for RepToday: read projects/RepToday/gtm/01-research/product-facts-brief.md, then ...
Write the drafts to projects/RepToday/teardowns/01-ladder_261030/plays/01-ready-on-open/.
Do not post, send, or change the Go-To-Market Package.
```
````

A play that needs money goes under `## Paid plays (not at $0)` in the same format, with its cost on the **Cost:** line.
