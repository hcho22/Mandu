# Naming availability - raw checks

Run 2026-07-08, from this machine (DNS `dig`, RDAP via rdap.org, `whois`, iTunes Search API via curl).
Guardrail honored: checked availability only; nothing bought or filed.

## Domains

| Domain | Status | Evidence |
|---|---|---|
| fitsnack.com | TAKEN | Resolves to 23.227.38.65 (Shopify IP range), NS googledomains. A storefront, not an app company. |
| fitsnack.app | AVAILABLE | RDAP 404 (unregistered on Google .app registry); no A/NS records. |
| fitsnack.io | AVAILABLE | whois: "Domain not found"; no A/NS records. |
| cairn.com | TAKEN | Resolves; NS dnsimple. |
| cairn.app | TAKEN | RDAP: registered 2018-05-08, clientDeleteProhibited. |
| cairnapp.com | TAKEN | Resolves (GoDaddy NS). |
| getcairn.com | TAKEN | Resolves (Shopify IP). |
| stack.com | TAKEN | AWS NS. |
| stack.app | TAKEN | RDAP: registered 2019-08-02, active. |
| getstack.app | TAKEN | Resolves (Cloudflare). |

## App Store (iTunes Search API, US storefront, 2026-07-08)

- `term=fitsnack`: 0 apps named FitSnack. Top results are unrelated fashion/shopping apps plus one generic home-workout app.
- `term=fit snack`: no collision. Notable adjacent result: **"Asketic Fit: Workout Snacks"** (Health & Fitness) - an app already using "workout snacks" language; flag for competitor research.
- `lookup?bundleId=com.fitsnack.app`: resultCount 0 - the planned bundle ID has no live app.
- `term=cairn`: **"Cairn - Hiking Safety Tracker" (FITCLIMB COM LLC, Health & Fitness, 4.7, 533 ratings)** - a direct name collision INSIDE the Health & Fitness category. Also Cairn University, Cairn games, etc. Cairn is contested.
- `term=stack workout`: extremely crowded field; "Stacked - Workout Tracker" (4.6, 1.7k ratings) and "RepStack" exist. "Stack" as a bare mark in fitness is generic and colliding.

## USPTO (tmsearch.uspto.gov, driven via headless Chrome, 2026-07-08)

Method: the official USPTO Trademark Search SPA (https://tmsearch.uspto.gov/search/search-results), queries typed into the wordmark search box. Control query "peloton" returned 112 results, confirming the harness works. Justia/Trademarkia mirrors are Cloudflare-walled and were not used.

| Query | Key results |
|---|---|
| `fit snack` (6,667 full-text results; relevant top hits) | **FIT SNACK - LIVE REGISTERED**, serial 87315837, Agora Ventures LLC (MA), IC 035: "On-line retail store services featuring subscription boxes" (healthy-snack boxes). Also FIT SNACK serial 90266923 DEAD/ABANDONED (Fit Snack LLC, CO, IC 035); **FITSNACK** (one word) serial 86762926 **DEAD/ABANDONED** (Pervine Foods, FL, IC 005 high-protein nutritional supplements). |
| `CM:cairn AND IC:041` (7 results) | **CAIRN - LIVE REGISTERED bare wordmark**, serial 79380586, The Game Bakers (France), classes **009 (downloadable software)**, 016, 028, 041. Plus CAIRN UNIVERSITY (LIVE, IC 041), CAIRN TRAVELER (LIVE, IC 041), CAIRN COLLECTIVE (DEAD). |
| `stack` in fitness classes | Query did not complete in the SPA session. Assessment relies on the domain + App Store layer plus genericness; see risk notes. Re-verify before any filing. |

### Risk read (inference, not legal advice)

- **FitSnack:** No live mark on the exact one-word FITSNACK; the one-word food mark is dead. But **FIT SNACK is live-registered in IC 035** for healthy-snack subscription boxes, and fitsnack.com is an active snack storefront. An iOS fitness app files in different classes (IC 009/041/042/044), and software vs. snack boxes are arguably unrelated goods, but both live in the broad "wellness" space and the marks are textually identical. MODERATE trademark risk + a real brand-confusion cost ("snack" reads food-first; the .com will never be ours).
- **Cairn:** BLOCKED for practical purposes: a live bare CAIRN registration covering IC 009 downloadable software (a software product could not cleanly register), cairn.app registered since 2018, and "Cairn - Hiking Safety Tracker" already ships in the App Store's Health & Fitness category.
- **Stack:** Not cleanly checkable and does not need to be: bare STACK in fitness is generic-descriptive ("stacking" workouts/habits is category language), every natural domain is taken, and "Stacked - Workout Tracker" already ships. Near-zero defensibility. BLOCKED on distinctiveness grounds.

## Early read (pre-tournament, to be confirmed)

- **FitSnack:** App Store clear, .app/.io available, .com taken by a snack-food storefront (brand-adjacent confusion risk: "snack" reads food-first; USPTO check must look at Class 9/41/42 plus food classes).
- **Cairn:** effectively blocked - same-category App Store collision + all natural domains taken since 2018.
- **Stack:** generic, crowded, all natural domains taken; trademark defensibility near zero in fitness.
