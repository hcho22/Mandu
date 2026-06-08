# F2F Crunch-Week Plan (Sun 6/7 to Mon 6/15, 2026)

_Created 2026-06-07. One-week, deadline-specific plan for the Hugging Face "Build Small / Backyard AI" submission. Hard deadline: **2026-06-15**._

## The binding constraint

The roadmap requires **5+ real weeknights of usage**. To log 5 honest dinners before Mon 6/15, the end-to-end loop must be **cookable by Tuesday night (6/9)**. Everything else is sequenced around getting there.

This week, F2F takes precedence (per `context/current-priorities.md` #2): F2F gets the bulk of each day; **evals drops to a light keep-warm touch** and resumes full pace Mon 6/16. Job search is a light touch only; defer the Tier A/B/C scan to after 6/15.

## Day-by-day

| Day | F2F (primary, ~4-5h) | Evals (light, ~45-60m) | Evening |
| --- | --- | --- | --- |
| **Sun 6/8** (today, optional) | Modal account + `modal token new`; deploy a hello-world to confirm GPU access. De-risks Monday. | — | — |
| **Mon 6/8** | **Backend up.** Deploy Modal + vLLM serving Qwen2.5-VL-7B; get `/extract` and `/generate` returning schema-locked guided JSON. No UI yet. | Finish **S1** (15-min Hamel L1/L2/L3 review + the 10-label hands-on) | — |
| **Tue 6/9** | **End-to-end loop.** Wire Gradio to the backend: photo -> extract -> confirm chips -> generate -> recipe cards. Ugly is fine. **Target: cookable tonight.** | S2 (classical metrics) — drop if F2F slips | **Usage night 1** + "I made this" |
| **Wed 6/10** | **Controls + honesty mechanics.** Cuisine / people / time-cap / healthier toggle / picky-kid notes; enforce confirmed-pantry-as-source-of-truth, the "from your fridge / you'll also need" split, estimates. | S3 (splits / leakage) — optional | **Usage night 2** |
| **Thu 6/11** | **Off-Brand UI + logging.** Custom Gradio theme / CSS + HTML recipe cards (the badge); "I made this" persistence to the Modal volume. | hold | **Usage night 3** |
| **Fri 6/12** | **Harden the hosted Space.** Error handling, Space secrets (`F2F_BACKEND_URL`, `F2F_AUTH_TOKEN`), keep-warm, and confirm it works on the live HF Space (not just local). | Light weekly review | **Usage night 4** |
| **Sat 6/13** | **Demo.** Record the demo video; draft the social post. | — | **Usage night 5** (hits the bar) |
| **Sun 6/14** | **Final polish + dry-run submit.** Sync `sdk_version` in the README YAML with `requirements.txt`; verify the Space is live end-to-end. | — | buffer night |
| **Mon 6/15** | **Submit in the morning** — do not wait for the evening. | — | — |

## Daily rhythm

| Block | Focus |
| --- | --- |
| Early (~1h) | Evals keep-warm (droppable on days F2F is at risk) |
| Core (~4-5h) | F2F, per the table |
| ~30-45 min | Job search: light touch only (defer the Tier A/B/C scan to after 6/15) |
| End of day | F2F daily log (`log my F2F progress`) |
| Evening | Cook with F2F + log the night |

## Three things that sink the deadline if ignored

1. **The loop must be cookable by Tue night.** That is what makes 5 honest usage nights possible. If Monday's backend slips, the "real usage" claim is at risk. Critical milestone: "Tuesday dinner from the app," not the UI.
2. **Monday is a model-serving day, not a UI day.** vLLM on Modal (cold starts, GPU availability, guided-decoding config) can eat the whole day. Do not touch Gradio until `/extract` returns valid JSON.
3. **Submit Monday morning.** Hackathon portals and HF Spaces fail at the worst time. Leave the evening of 6/15 as margin, not the work itself.

## After 6/15

- Resume full evals pace (S2-S10) Mon 6/16.
- Resume the Tier A/B/C job-search scan.
- Write up F2F for the portfolio (small-VLM deployment, guided-JSON structured output, honesty mechanics).
