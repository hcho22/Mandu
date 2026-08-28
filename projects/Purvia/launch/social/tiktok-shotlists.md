# TikTok - shot lists only (per the brief; no video is fabricated)

Three vertical (9:16) concepts, each under 45s, engineer-narrated, screen-first.
All on-screen numbers come from CLAIMS.md rows; captions burned in (sound-off viewers).

## Clip 1 - "The green table that lied" (~40s)

| # | Shot | On-screen | VO |
|---|---|---|---|
| 1 | Screen recording: scroll the Purvia README to "The permissions story, in numbers" | highlight the green 1.000 table | "This table was green for 42 days. It was also wrong." |
| 2 | Zoom: the outage paragraph, dates highlighted 2026-06-19 -> 07-30 | red underline on "a real, measured 0.000" | "The benchmark was actually measuring zero. Every night. With the alarm firing." |
| 3 | Terminal: run `python -m evals.permissions_scale.runner` on an unseeded corpus | DEGENERATE RUN notice output | "Here's the fix: a run that measures nothing now refuses to publish a number." |
| 4 | Editor: `test_degenerate_guard.py` open, CI badge green | caption: "the guard is itself CI-pinned" | "And the guard has its own guard." |
| 5 | End card: card1-failure.png | github.com/hcho22/Purvia | "The whole story is in the README. On purpose." |

## Clip 2 - "Break retrieval, watch CI catch it" (~35s)

| # | Shot | On-screen | VO |
|---|---|---|---|
| 1 | Editor: `backend/chunking.py`, change 500 -> 100, commit, push | one-line diff | "One line. Chunk size 500 to 100." |
| 2 | GitHub PR page: eval workflow running | timer overlay | "The eval runs on the PR head and on main." |
| 3 | The bot comment appears: red deltas | zoom on -0.510 | "Four minutes. Recall at five: minus point five one. Posted by nobody." |
| 4 | End card: card3-regression.png | docs/evals.md §4 | "We keep this PR closed and framed." |

## Clip 3 - "The viewer who sees nothing" (~30s)

| # | Shot | On-screen | VO |
|---|---|---|---|
| 1 | App: two browser profiles side by side, same question in chat | left: owner gets answer with "via owner" badge | "Same question. Two users." |
| 2 | Right profile: no grant - retrieval returns nothing relevant | caption: "ACL checked inside the SQL predicate" | "She was never granted the doc. The vector search never even ranked it." |
| 3 | Share dialog: grant her the document; re-ask | badge flips to "via direct grant" | "Grant it, ask again - and the badge tells you exactly why she can see it now." |
| 4 | End card: card2-security.png | n = 60 x 3 x 3, 16-chunk corpus | "Enforced in the predicate. Measured every night." |

Recording requirements (when the captain shoots): local stack up per README "Local development"; demo corpus seeded; two seeded users; OBS vertical canvas 1080x1920; terminal font >= 18pt for legibility.
