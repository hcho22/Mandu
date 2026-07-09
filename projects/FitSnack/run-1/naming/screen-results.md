# FitSnack Naming Screen: Raw Results

Date: 2026-07-09.
Screener: automated (dig, RDAP via rdap.org, iTunes Search API, country=us, limit=8).
Input list had duplicates (Kept x2, Steady x2); each name was checked once.

Pass rule: (.app OR .io unregistered) AND no same-name app in Health & Fitness AND no famous same-name app overall.

## Method notes

- `dig +short NAME.app A` and `NS`, `dig +short NAME.io NS`, `dig +short getNAME.com NS`.
- NS records present = registered.
- Ambiguous or timed-out cases confirmed with `curl -sL -o /dev/null -w "%{http_code}" https://rdap.org/domain/DOMAIN` (200 = registered, 404 = unregistered).
- Local resolver timed out repeatedly on keel.app, tend.app, and getkept.com; RDAP was used as the authority for those.
- nonzero.io returned NS records from dig (n0ns.org/net/com, a .io zone artifact) but RDAP returned 404, so it is treated as unregistered.

## Domain results

| Name | .app A | .app NS | .app RDAP | .io NS | .io RDAP | get*.com NS | Domain verdict |
|---|---|---|---|---|---|---|---|
| Kept | 164.90.207.94 | name.com NS | - | googledomains NS | - | dig timeout, RDAP 200 (registered) | Both taken |
| Steady | 172.67.180.107, 104.21.18.54 | cloudflare NS | - | dreamhost NS | - | hover NS | Both taken |
| Anyway | 165.22.123.139 | helloserver.win NS | - | cloudflare NS | - | namebright NS | Both taken |
| Keel | dig timeout | dig timeout | 200 (registered) | cloudflare NS | - | cloudflare NS | Both taken |
| Sturdy | empty | cloudflare NS | 200 (registered) | 1and1 NS | - | cloudflare NS | Both taken |
| Attend | 217.70.184.38 | gandi NS | - | park.io + awsdns NS | - | afternic NS | Both taken |
| Mettle | 76.223.54.146, 13.248.169.48 | afternic NS (parked/for sale) | - | cloudflare NS | - | namebright NS | Both taken |
| Ajar | 15.197.148.33, 3.33.130.190 | domaincontrol NS | - | awsdns NS | - | cloudflare NS | Both taken |
| Sliver | empty | googledomains NS | 200 (registered) | afternic NS (parked) | - | domaincontrol NS | Both taken |
| Threshold | empty | awsdns NS | 200 (registered) | domaincontrol NS | - | cloudflare NS | Both taken |
| Bout | 165.22.123.139 | helloserver.win NS | - | afternic NS (parked) | - | tld-ns NS | Both taken |
| Tend | dig timeout | empty (timeout suspected) | 200 (registered) | digitalocean NS | - | namebright NS | Both taken |
| Kata | empty | googledomains NS | 200 (registered) | afternic NS (parked) | - | namebright NS | Both taken |
| Breather | 76.223.54.146, 13.248.169.48 | dan.com NS (parked/for sale) | - | spaceship NS | - | domaincontrol NS | Both taken |
| Ember | 162.255.119.161 | registrar-servers NS | - | afternic NS (parked) | - | namebright NS | Both taken |
| Nonzero | 13.248.169.48, 76.223.54.146 | dan.com NS (parked/for sale) | 200 (registered) | n0ns.* NS (zone artifact) | 404 (UNREGISTERED) | empty; RDAP 404 (UNREGISTERED) | nonzero.io AVAILABLE, getnonzero.com AVAILABLE |
| Leeway | 13.248.169.48, 76.223.54.146 | dan.com NS (parked/for sale) | - | googledomains NS | - | awsdns NS | Both taken |
| Still | empty | googledomains NS | 200 (registered) | awsdns NS | - | afternic NS | Both taken |
| Reed | 15.197.148.33, 3.33.130.190 | domaincontrol NS | - | cloudflare NS | - | namebright NS | Both taken |

## App Store results (iTunes Search API, top 8, US)

| Name | Same-name Health & Fitness collision | Other notable hits |
|---|---|---|
| Kept | YES: "The Kept App with Chris Powell" (Triaxiom, LLC) | Kept (Finance, Bank of Ayudhya), Kept: AI Photo Journal, Kept Notes, Kept: Budget Tracker |
| Steady | YES: "Steady: Fear of Flying" (Nordic Social Media AB) | Steady App (Magazines, Steady Media GmbH); Steady the income app is well known |
| Anyway | No exact-name hit | Anyways (Navigation), Anywayanyday (Travel), Drive ANYWAY (Travel) |
| Keel | No same-name H&F | Keel: Your Focus Anchor (Productivity), News Radio 710 KEEL |
| Sturdy | YES: "Sturdy: Women's Fitness" (Sturdy Fitness, LLC) and "Sturdy: GLP-1 Tracker" | Sturdy Savings Mobile Banking |
| Attend | Near-name H&F: "Attend Behavior" (Attend Behavior, Inc.) | Attend (Lifestyle), uAttend, AT&T attend, several attendance apps |
| Mettle | YES: "Mettle: Mental Fitness for Men" (Head Shed App Ltd) | Mettle: Shifts Jobs & Hiring; Mettle is also a well-known UK NatWest business-banking app (search surfaced Monzo/Starling/Revolut alongside) |
| Ajar | No same-name H&F | Ajar App (Business); Azar (Social, large app) is a near-homophone |
| Sliver | No same-name hit at all | Only "silver"/"slither" fuzzy matches (slither.io is famous but distinct) |
| Threshold | No same-name H&F | Threshold: Organizing (Utilities), THRESHOLD SPORTS (Sports), Threshold Capture, Threshold Care |
| Bout | YES: "BOUT Boxing" (Alku Technology) and "Bout Fight Club" (Power Zone Management) | The BOUT (Travel); Bolt (huge app) is a near-name |
| Tend | No same-name H&F | Tend Dental (Medical, well-funded US dental brand), Tend Companion App (Business) |
| Kata | YES (near): "Kata Smartwatch" (H&F, OWTEL) | ShotokanKata (Sports), Shotokan JKA kata (Education); kata is a generic martial-arts term |
| Breather | YES: multiple. "Breather Coach" (PN Medical), "Breather Coach: Box Breathing", "Breather - Relax & Focus", "Breath Now: Breather coach" | Breather was also a famous workspace-rental startup |
| Ember | No exact-name H&F in top 8 | Ember - Temperature Control (famous smart-mug brand), Ember Fund, Ember casinos, Ember: Streak & Habit Tracker (Productivity, adjacent) |
| Nonzero | No H&F hit | Only 2 results total: "NonZero" (Productivity, Lewis Lee) is an exact-name but small, non-famous app; "Run Lines With Me" by NONZERO SOLUTIONS LLC |
| Leeway | No H&F hit | Leeway (Finance), LEEWAY_CRM, Leeway: Time Budget Planner (all small) |
| Still | YES: multiple. "Still: Quit Porn, Smoking Now", "Still: Mindful Meditation" (Kenny Tjay), "Still - Meditation Timer & Tracker" | still: journaling & reflection, Still: Bible sleep stories |
| Reed | No same-name H&F | Reed.co.uk Job Search (major UK job board); Reddit dominates fuzzy results |

## Verdict

| Name | Domain criterion | App Store criterion | PASS |
|---|---|---|---|
| Kept | FAIL (.app and .io registered) | FAIL (same-name H&F app) | NO |
| Steady | FAIL | FAIL (same-name H&F app) | NO |
| Anyway | FAIL | OK | NO |
| Keel | FAIL | OK | NO |
| Sturdy | FAIL | FAIL (two same-name H&F apps) | NO |
| Attend | FAIL | Marginal (near-name H&F) | NO |
| Mettle | FAIL | FAIL (same-name H&F app + famous UK banking app) | NO |
| Ajar | FAIL | OK | NO |
| Sliver | FAIL | OK | NO |
| Threshold | FAIL | OK | NO |
| Bout | FAIL | FAIL (same-name H&F apps) | NO |
| Tend | FAIL | OK (Tend Dental is known but different name space) | NO |
| Kata | FAIL | Marginal (Kata Smartwatch in H&F) | NO |
| Breather | FAIL | FAIL (multiple same-name H&F apps) | NO |
| Ember | FAIL | FAIL (famous same-name brand: Ember mug) | NO |
| Nonzero | PASS (nonzero.io unregistered, RDAP 404; getnonzero.com also unregistered, RDAP 404) | PASS (no H&F collision, no famous same-name app; one small same-name Productivity app "NonZero" by Lewis Lee) | YES |
| Leeway | FAIL | OK | NO |
| Still | FAIL | FAIL (multiple same-name H&F apps) | NO |
| Reed | FAIL | Marginal (Reed.co.uk is a major brand) | NO |

Only survivor: **Nonzero** (nonzero.io and getnonzero.com both unregistered; nonzero.app is parked on dan.com and likely buyable).
Caveat: an exact-name "NonZero" Productivity app exists on the App Store (small, single developer); Apple allows duplicate names across developers only if the exact App Store name field is not identical, so the listing name would need a qualifier (e.g., "Nonzero: Daily Workouts").
