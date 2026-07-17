# Extras

- `app-store-listing.md` - complete App Store listing copy (name, subtitle, promo text, description, keywords, captions, review notes), every field inside Apple's limits, claims traced.
- `screenshot-mockups/` - the five App Store screenshots as an HTML page (`index.html`) plus the rendered capture (`mockups.png`), captions in the brand's fixed message-architecture order.
- `simulator/` - the streak-vs-score simulator: `score.js` (US-H01 Consistency Score implementation with red-team caveats), `index.html` (interactive: scenarios, editable day grid, chart), `simulator.png` (verified capture).
- `claims-lint/` - the unexpected deliverable: a machine-checkable voice-contract gate. `lint.js` fails any user-facing asset that uses a banned phrase, banned claim, wrong name casing, or the internal codename (honest-negation lines are waived by scoped allowlist); `claims-matrix.md` traces every positive marketing claim to its evidence. Run: `node lint.js`.
