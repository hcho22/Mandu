# Nonzero marketing site + Ready Screen prototype

Everything runs locally with zero build steps and zero network dependencies.

## Run it

Option A (just open it):

    open index.html

Option B (serve it, identical result):

    python3 -m http.server 8080
    # then visit http://localhost:8080

- `index.html` - the marketing site. The phone in the hero is a live iframe of the prototype.
- `prototype/index.html` - the Ready Screen prototype, standalone. It runs the real deterministic
  session engine (`prototype/engine.js`) over the real 42-movement library exported from the
  FitSnack dev repo (`prototype/exercises.js`). Duration chips regenerate the session in under a
  millisecond, swap is deterministic (same pillar + pattern, honest "no alternative" state), the
  demo controls simulate days passing and misses denting the Consistency Score, and Start walks
  the full session player through to the post-session screen.

## Verification

Screenshot-verified on 2026-07-09 at desktop (1440x900) and mobile (390x844) in `screenshots/`:
hero, net (streak-vs-score interactive), science strip, how-it-works, pricing, FAQ, footer CTA,
and the prototype Ready Screen. No horizontal overflow at mobile width; no console errors.
