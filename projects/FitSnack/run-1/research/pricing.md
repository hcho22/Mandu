# FitSnack Pricing: Churn Reconciliation + Price Lock Recommendation

Date: 2026-07-09.
All sources fetched this session; quotes verbatim from fetched pages.
Confidence: HIGH = fetched primary, MEDIUM = fetched secondary citing primary, LOW = snippet only.

## 1. Reconciling the contradictory payer-churn numbers

The three numbers do not contradict each other.
They measure three different things: (a) still-active at month 12, (b) auto-renew switched off during year 1, and (c) actually paid for year 2.

| Number | Source | Scope | What it actually measures |
|---|---|---|---|
| ~72% cancelled in Year 1 | RevenueCat SOSA 2026 summary blog (HIGH) | Cross-category, annual plans | Share of annual subscribers who switched OFF auto-renew during year 1. They keep access until the term ends, so this is not "lost mid-year." Verbatim: "~56% of annual subscribers cancelled in Year 1 in 2025, while this worsened to ~72% in 2026." |
| 44.1% yearly Y1 retention | RevenueCat SOSA 2025 page (HIGH) | Cross-category, yearly plans | Share still retained after one year. Verbatim: "Yearly plans maintain the highest retention rates, but retention has slightly declined from 47.1% in the previous period to 44.1% in this period." The "~50%+ at 12 months for H&F" claim in our corpus is a misattribution: the closest real figure is this cross-category 47.1% prior-period number. No H&F-specific ~50% appears on any page fetched this session. |
| 25% H&F annual first renewal | RevenueCat renewal-rates-by-category blog, SOSA 2026 data (HIGH) | H&F specific, annual plans | Median share of H&F annual subscribers who actually renew (pay) at the first renewal. "Health & Fitness" median annual renewal rate "25%"; cross-category band: "For annual subscriptions, the median first renewal rate ranges from 23%-40% across the top app categories." H&F monthly first renewal: 57%. |
| 33% retention (annual, H&F) | Business of Apps benchmarks page (quote HIGH via curl; metric definition LOW, chart paywalled) | H&F specific, annual plans | Verbatim bullet: "Annual subscriptions to health and fitness apps have a 33% retention rate." The underlying charts ("Health & Fitness App Sub Retention", "Health & Fitness App Renewal Rate") are behind a login, so the exact definition is unverifiable. INFERENCE: it sits inside RevenueCat's 23-40% cross-category first-annual-renewal band, so the most plausible reading is renewal into year 2, slightly above RevenueCat's H&F median of 25%. |

Caution: a secondary source (9to5Mac, MEDIUM) quotes SOSA 2026 as "Yearly plans renew at 83.4% overall."
That figure cannot be a first-renewal rate given the 23-40% median band from RevenueCat's own blog; it likely measures renewal events among subscribers who reach billing with auto-renew still on.
Do not use it for planning.
Two more SOSA 2026 numbers that shape the plan: "the first month accounts for 35% of all annual cancellations" (HIGH), and 95% of cancelled annual subscribers never come back / "annual reactivation sits at just 5%" (MEDIUM, 9to5Mac citing SOSA 2026).

### The one defensible retention sentence

Plan FitSnack's base case on 25-33% of annual subscribers renewing into Year 2 (RevenueCat SOSA 2026 H&F median first annual renewal: 25%; Business of Apps H&F: 33%) and ~57% monthly first renewal, with roughly a third of annual auto-renew shutoffs happening in Month 1; the "72% cancel in Year 1" figure is the same phenomenon measured cross-category as auto-renew shutoff, and the "~50% / 44% retained at 12 months" figures are cross-category still-active metrics from SOSA 2025, so none of the numbers contradict once the metric is named.

## 2. Trial length: keep the 14-day trial, instrument Month 1

H&F trial facts (RevenueCat SOSA 2026 H&F page, HIGH):

- H&F trial-length mix: 29% use trials of 4 days or less (lowest of any category), 54% use 5-9 days, ~11% use 10-16 days, ~6% use 17-32 days.
- H&F median trial-to-paid conversion is 37.7% ("Travel and Health & Fitness lead with the highest median trial-to-paid conversion rates").
- Conversion by trial length (cross-category, not H&F-specific): 4 days or less 25.5%, 5-9 days 37.4%, 10-16 days ~35.4%, 17-32 days "42.5%".

Read on FitSnack's planned 14-day trial:

- A 14-day trial sits in the 10-16 day bucket that only ~11% of H&F apps use; the category norm is 5-9 days (54%).
- Cross-category, 10-16 day trials convert at ~35.4%, roughly on par with 5-9 day trials (37.4%) and far above ultra-short trials (25.5%); 17-32 day trials do best (42.5%).
- INFERENCE: for a discipline/streak app the product needs about two weeks to demonstrate a visible streak, so the 14-day trial is defensible and not a measurable conversion penalty; the real risk is Month 1 auto-renew shutoff (35% of all annual cancellations), so the trial must land a value moment by day 5-7 and a pre-renewal save flow, not just a day-14 paywall.

Recommendation: KEEP the 14-day trial.
Add a day-5/7 milestone moment and a pre-conversion reminder, and treat trial-day-1 to paid-day-30 as the single most instrumented window in the app.

## 3. Price benchmark: the verified annual set

All IAP prices parsed this session from the apps' US App Store pages (HIGH).

| App | Monthly | Annual | Other | Notes |
|---|---|---|---|---|
| Gentler Streak (id 1576857102) | $8.99 | $39.99 | Lifetime $89.99-$179.99, Yearly Family $59.99 | Apple Design Award indie; insight-depth paywall |
| Bare Minimum: Micro Workouts (id 6759055696) | $9.99 | $49.99 | "Annual Special Offer $19.99" intro | Closest concept comp (micro workouts) |
| Wakeout! (id 1242116567) | $12.99 (Full Access) | $69.99 (Full Access; also "Standard Access $59.99", "Yearly subscription $59.99" legacy SKUs) | Family tiers | IAP list does not label periods; $69.99 is the current top annual SKU |
| Seven: 7 Minute Workout (id 650276551) | $9.99 (7 Club) | $79.99 (7 Club Annual) | Legacy "7 Minute Workout" SKUs $39.99-$59.99 | 40M-download incumbent |
| Nike Training Club (id 301521403) | $0 | $0 | No In-App Purchases section on its App Store page | The free substitute; "access industry-leading workout programming and legit coaching for free" |
| Category median (SOSA 2026 H&F, HIGH) | $9.99 | $39.94 | | "Health & Fitness clusters at $39.94 yearly and $9.99 monthly" |
| FitSnack (planned) | $7.99 | $59.99 | | |

Context numbers (SOSA 2026, HIGH): "Health & Fitness leads annual adoption at 68%" of subscriptions sold; H&F yearly realized LTV median $35.64.

### Recommendation: keep $59.99/yr, raise monthly to $9.99

**Annual $59.99: KEEP.**

- It is mid-pack in the verified micro-workout comp set: above Gentler Streak ($39.99) and Bare Minimum ($49.99), below Wakeout ($69.99) and Seven ($79.99).
- It is 1.5x the category median ($39.94), which is defensible only if the depth paywall visibly exceeds Gentler/Bare Minimum (see section 4); the two apps priced above FitSnack both gate their full catalog and personalization.
- With H&F selling 68% annual and yearly realized LTV at $35.64 median, a $59.99 annual with even median-level trial conversion puts FitSnack above category median LTV per payer.

**Monthly $7.99: RAISE to $9.99.**

- Every verified competitor monthly is $8.99-$12.99 and the category median is exactly $9.99; at $7.99 FitSnack would be the cheapest monthly in its set while positioning as premium discipline, which reads as discount, not depth.
- Monthly is the leaky bucket (57% H&F first renewal vs annual's role as the retention plan); its job is to anchor the annual, and $9.99/mo makes $59.99/yr a "save 50%, 6 months free" story versus a weaker 7.5-month math at $7.99.
- INFERENCE: no verified evidence suggests $7.99 vs $9.99 materially changes trial-start rates in this category; the mix is decided at the plan-picker where the annual discount framing dominates.

**Free tier: keep the free core loop forever, and keep it genuinely complete.**
Nike Training Club offers its entire training library for $0, so a crippled free tier loses to a default-installed substitute.
The free loop is the acquisition and habit engine; the paywall must sell depth, not access.

## 4. Paywall-content comparison: what the category actually charges for

| | Seven (7 Club, $9.99/mo / $79.99/yr) | Gentler Streak (Premium, $8.99/mo / $39.99/yr) | NTC ($0) | FitSnack depth paywall (planned) |
|---|---|---|---|---|
| Core workout loop | Free (daily 7-min workouts, habit challenge, achievements) | Free (activity tracking, homepage progress bar, widgets) | Free | Free forever (deterministic 5-60 min engine) |
| Personalized plans / adaptivity | PAID: "Get faster results with personal workout plans adapted to your fitness level" | PAID: "Daily Workout Suggestions" | Free | PAID: daily-adaptive AI Programmer (option C policy re-weighting) |
| Full catalog / variety | PAID: "Access all workouts and over 200 exercises for more varied training" | n/a (tracker, not a catalog app) | Free | PAID: LLM "Variety Language" slice, Strength-Phase catalog (Phase 2) |
| Insights / analytics depth | n/a | PAID: "10-day and 30-day Activity Path", "Full Access to all Wellbeing Metrics", "Full Sleep Analysis", "Full Activity Overview Charts", "Estimate Workouts' Intensity (RPE)" | Partial (basic logging) | PAID candidate: streak analytics, readiness trends |
| Human/coach support | PAID: "Receive exclusive support and guidance from our certified personal trainer" | n/a | Free (content-only) | Not planned for MVP |
| Convenience extras | n/a | PAID: "Add Workout Manually", "Mirror Apple Watch tracking to iPhone" | n/a | Candidate: manual logging, watch mirroring parity |

Pattern (INFERENCE from the verified set): the category never paywalls the core loop; it charges for personalization/plans, catalog variety, and analytics depth.
FitSnack's planned split (free deterministic core loop, paid AI Programmer adaptivity + variety + depth) matches exactly what Seven and Gentler Streak monetize, and Seven proves personalization + full-catalog gating supports a $79.99 annual, giving $59.99 headroom.

## 5. Locked recommendation

1. Annual: $59.99/yr. Keep.
2. Monthly: $9.99/mo. Change from $7.99.
3. Trial: 14 days. Keep, with a day-5/7 value moment and pre-renewal save flow.
4. Free tier: full core loop forever (NTC-proofing).
5. Paywall contents: gate AI Programmer adaptivity, variety/catalog, and analytics depth; never gate the core loop.
6. Retention planning basis: 25-33% of annual payers renew into Year 2; 57% monthly first renewal; 35% of annual cancellations land in Month 1; only ~5% of cancelled annual subscribers ever return.

## Sources

| Source | URL | Fetched | Confidence |
|---|---|---|---|
| RevenueCat, State of Subscription Apps 2026: Health & Fitness | https://www.revenuecat.com/state-of-subscription-apps-2026-health-and-fitness/ | 2026-07-09 | HIGH |
| RevenueCat, Average Subscription Renewal Rates by App Category (SOSA 2026 data, updated 2026-04-24) | https://www.revenuecat.com/blog/growth/average-subscription-renewal-rates-by-app-category/ | 2026-07-09 | HIGH |
| RevenueCat, The State of Subscription Apps in 10 minutes (2026) | https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026/ | 2026-07-09 | HIGH |
| RevenueCat, State of Subscription Apps 2025 | https://www.revenuecat.com/state-of-subscription-apps-2025/ | 2026-07-09 | HIGH |
| Business of Apps, Health & Fitness App Benchmarks | https://www.businessofapps.com/data/health-fitness-app-benchmarks/ | 2026-07-09 (curl; charts paywalled) | HIGH quote / LOW metric definition |
| 9to5Mac on SOSA 2026 reactivation | https://9to5mac.com/2026/05/27/new-report-shows-annual-app-subscribers-rarely-return-after-they-cancel/ | 2026-07-09 | MEDIUM |
| App Store: Gentler Streak (IAP list) | https://apps.apple.com/us/app/gentler-streak-workout-tracker/id1576857102 | 2026-07-09 | HIGH |
| App Store: Bare Minimum Micro Workouts (IAP list) | https://apps.apple.com/us/app/bare-minimum-micro-workouts/id6759055696 | 2026-07-09 | HIGH |
| App Store: Wakeout! (IAP list) | https://apps.apple.com/us/app/wakeout-break-the-sit-habit/id1242116567 | 2026-07-09 | HIGH |
| App Store: Seven 7 Minute Workout (IAP list + description) | https://apps.apple.com/us/app/seven-7-minute-workout/id650276551 | 2026-07-09 | HIGH |
| App Store: Nike Training Club (no IAP section) | https://apps.apple.com/us/app/nike-training-club/id301521403 | 2026-07-09 | HIGH |
| Gentler Streak docs: Premium membership details | https://docs.gentler.app/managing-your-subscription-account/view-your-gentler-streak-premium-membership-details | 2026-07-09 | HIGH |
