---
name: ab-testing
description: When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. Also use when the user mentions "A/B test," "split test," "experiment," "test this change," "variant copy," "multivariate test," "hypothesis," "should I test this," "which version is better," "test two versions," "statistical significance," "how long should I run this test," "growth experiments," "experiment velocity," "experiment backlog," "ICE score," "experimentation program," or "experiment playbook." Use this whenever someone is comparing two approaches and wants to measure which performs better, or when they want to build a systematic experimentation practice. In Gr0wthPilot this copy pre-registers the hook-only A/B pairs of a Candidate Package's Test Kit; it runs no test and reads no results. For tracking implementation, see analytics. For page-level conversion optimization, see cro.
metadata:
  version: 2.0.2
---

# A/B Test Setup

## Gr0wthPilot copy: read first

- **Source:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `skills/ab-testing/` at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b`, MIT License, Copyright (c) 2025 Corey Haines.
  The license and the list of changes from upstream are in this folder's `LICENSE.md`.
- **Called by Gr0wthPilot only.** This copy is a phase skill of Mandu's `gr0wthpilot` skill and sits inside its folder, so no other Mandu session lists it.
- **What this copy is for:** phase 3, "Social", reads it to pre-register the Test Kit's hook-only A/B pairs, each with its hypothesis, its two hooks, and the metric that will call it, in `05-social-pmf/ab-pairs.md`.
- **Never ask anything.** Where this skill says to ask the user or gather context, answer from the Candidate Package first (its `01-research/product-facts-brief.md`), then the Product's own repository (read only) and `projects/<Product>/` in Mandu. Where nothing answers a question, decide, and log the decision `[DECIDED BY AGENT]` with the rejected alternative in the Candidate Package's `decisions-log.md`.
- **The Candidate Package is the only context.** Never read for, create, or update `.agents/product-marketing.md` or any other context or strategy file outside the Candidate Package, and add no Learnings rows or results tables; a Product has no results before its Test Kit runs.
- **Publish nothing.** Every output is a local file in the Candidate Package. Nothing here posts, sends, schedules, submits, uploads, deploys, registers, or signs up for anything, and nothing contacts a real person; the Founder does any of that himself after Handoff.
- **No new spending.** Use a paid tool or API only when its key is already in the Product's `.env`, and never print, copy, or commit a key's value. Without one, build images from HTML and SVG and video with Remotion or ffmpeg.
- **Invent nothing factual.** Names, taglines, visuals, and copy are invented freely; every fact, number, quote, and competitor detail carries a URL fetched during this run and listed in the Candidate Package's `sources.md`, and every guess is labeled `[ASSUMPTION]` with its reasoning.
- **Pre-register, never run.** A run designs the pairs and stops before the Test Kit starts: it posts no leg, reads no results, and fills in no result, decision, or learnings field in `references/test-templates.md`; gr0wthlab's Test Kit runs the pairs after Handoff.
- **No significance claims.** The sample-size, traffic-allocation, and implementation sections assume split web traffic, which the Test Kit's TikTok and YouTube Shorts posts do not have; each pair states how it will be read and that limit, and claims no statistical significance.
- Related skills named below are upstream skills; only the copies in Gr0wthPilot's `marketingskills/` folder and Mandu's installed skills exist here.

You are an expert in experimentation and A/B testing. Your goal is to help design tests that produce statistically valid, actionable results.

## Initial Assessment

**Read the Candidate Package first:**
Read its `01-research/product-facts-brief.md` (see "Gr0wthPilot copy: read first") before gathering anything else. Use that context, and look up only what it does not cover or what is specific to this task, in the sources that block names.

Before designing a test, understand:

1. **Test Context** - What are you trying to improve? What change are you considering?
2. **Current State** - Baseline conversion rate? Current traffic volume?
3. **Constraints** - Technical complexity? Timeline? Tools available?

---

## Core Principles

### 1. Start with a Hypothesis
- Not just "let's see what happens"
- Specific prediction of outcome
- Based on reasoning or data

### 2. Test One Thing
- Single variable per test
- Otherwise you don't know what worked

### 3. Statistical Rigor
- Pre-determine sample size
- Don't peek and stop early
- Commit to the methodology

### 4. Measure What Matters
- Primary metric tied to business value
- Secondary metrics for context
- Guardrail metrics to prevent harm

---

## Hypothesis Framework

### Structure

```
Because [observation/data],
we believe [change]
will cause [expected outcome]
for [audience].
We'll know this is true when [metrics].
```

### Example

**Weak**: "Changing the button color might increase clicks."

**Strong**: "Because users report difficulty finding the CTA (per heatmaps and feedback), we believe making the button larger and using contrasting color will increase CTA clicks by 15%+ for new visitors. We'll measure click-through rate from page view to signup start."

---

## Test Types

| Type | Description | Traffic Needed |
|------|-------------|----------------|
| A/B | Two versions, single change | Moderate |
| A/B/n | Multiple variants | Higher |
| MVT | Multiple changes in combinations | Very high |
| Split URL | Different URLs for variants | Moderate |

---

## Sample Size

### Quick Reference

| Baseline | 10% Lift | 20% Lift | 50% Lift |
|----------|----------|----------|----------|
| 1% | 150k/variant | 39k/variant | 6k/variant |
| 3% | 47k/variant | 12k/variant | 2k/variant |
| 5% | 27k/variant | 7k/variant | 1.2k/variant |
| 10% | 12k/variant | 3k/variant | 550/variant |

**Calculators:**
- [Evan Miller's](https://www.evanmiller.org/ab-testing/sample-size.html)
- [Optimizely's](https://www.optimizely.com/sample-size-calculator/)

**For detailed sample size tables and duration calculations**: See [references/sample-size-guide.md](references/sample-size-guide.md)

---

## Metrics Selection

### Primary Metric
- Single metric that matters most
- Directly tied to hypothesis
- What you'll use to call the test

### Secondary Metrics
- Support primary metric interpretation
- Explain why/how the change worked

### Guardrail Metrics
- Things that shouldn't get worse
- Stop test if significantly negative

### Example: Pricing Page Test
- **Primary**: Plan selection rate
- **Secondary**: Time on page, plan distribution
- **Guardrail**: Support tickets, refund rate

---

## Designing Variants

### What to Vary

| Category | Examples |
|----------|----------|
| Headlines/Copy | Message angle, value prop, specificity, tone |
| Visual Design | Layout, color, images, hierarchy |
| CTA | Button copy, size, placement, number |
| Content | Information included, order, amount, social proof |

### Best Practices
- Single, meaningful change
- Bold enough to make a difference
- True to the hypothesis

---

## Traffic Allocation

| Approach | Split | When to Use |
|----------|-------|-------------|
| Standard | 50/50 | Default for A/B |
| Conservative | 90/10, 80/20 | Limit risk of bad variant |
| Ramping | Start small, increase | Technical risk mitigation |

**Considerations:**
- Consistency: Users see same variant on return
- Balanced exposure across time of day/week

---

## Implementation

### Client-Side
- JavaScript modifies page after load
- Quick to implement, can cause flicker
- Tools: PostHog, Optimizely, VWO

### Server-Side
- Variant determined before render
- No flicker, requires dev work
- Tools: PostHog, LaunchDarkly, Split

---

## Running the Test

### Pre-Launch Checklist
- [ ] Hypothesis documented
- [ ] Primary metric defined
- [ ] Sample size calculated
- [ ] Variants implemented correctly
- [ ] Tracking verified
- [ ] QA completed on all variants

### During the Test

**DO:**
- Monitor for technical issues
- Check segment quality
- Document external factors

**Avoid:**
- Peek at results and stop early
- Make changes to variants
- Add traffic from new sources

### The Peeking Problem
Looking at results before reaching sample size and stopping early leads to false positives and wrong decisions. Pre-commit to sample size and trust the process.

---

## Analyzing Results

### Statistical Significance
- For a pre-specified fixed-horizon test, compare its p-value with the chosen significance level (commonly α = 0.05).
- A p-value describes how incompatible the data are with the null model: the probability, **assuming that model and its assumptions**, of a result at least as extreme as the observed one. It is not the probability that the result is random, that the null is true, or that a variant will win again.
- A 95% confidence interval comes from a procedure with 95% coverage over repeated samples under its assumptions. It is not a 95% posterior probability that this particular interval contains the true effect. Report the interval and effect size alongside the p-value.
- Use the planned analysis and stopping rule. Sequential tests and Bayesian analyses have their own interpretation; do not translate every platform's “confidence” score into a fixed-horizon p-value.

These distinctions follow the [American Statistical Association's p-value statement](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf). Statistical significance alone does not establish business value or justify shipping a variant.

### Analysis Checklist

1. **Reach sample size?** If not, result is preliminary
2. **Statistically significant?** Check confidence intervals
3. **Effect size meaningful?** Compare to MDE, project impact
4. **Secondary metrics consistent?** Support the primary?
5. **Guardrail concerns?** Anything get worse?
6. **Segment differences?** Mobile vs. desktop? New vs. returning?

### Interpreting Results

| Result | Conclusion |
|--------|------------|
| Significant winner | Check effect size, uncertainty and guardrails before implementing |
| Significant loser | Keep control, learn why |
| No significant difference | Report the effect interval: it may still allow meaningful benefit and harm, or may exclude effects worth pursuing. Follow the planned stopping rule; do not extend a finished fixed-horizon test until it becomes significant. Plan a new test if needed. |
| Mixed signals | Check data quality and planned metrics; label unplanned segment findings exploratory and confirm them in a new test |

---

## Documentation

Document every test with:
- Hypothesis
- Variants (with screenshots)
- Results (sample, metrics, significance)
- Decision and learnings

**In Gr0wthPilot:** document the hypothesis and variants in `05-social-pmf/ab-pairs.md`; results, the decision, and learnings come from gr0wthlab's Test Kit after Handoff, never from this run (see "Pre-register, never run" in "Gr0wthPilot copy: read first").

**For templates**: See [references/test-templates.md](references/test-templates.md)

---

## Growth Experimentation Program

Individual tests are valuable. A continuous experimentation program is a compounding asset. This section covers how to run experiments as an ongoing growth engine, not just one-off tests.

### The Experiment Loop

```
1. Generate hypotheses (from data, research, competitors, customer feedback)
2. Prioritize with ICE scoring
3. Design and run the test
4. Analyze results with statistical rigor
5. Promote winners to a playbook
6. Generate new hypotheses from learnings
→ Repeat
```

**In Gr0wthPilot:** a run does steps 1 and 2 and the design half of step 3; running the tests, steps 4 to 6, the playbook, and the cadence below come after Handoff with gr0wthlab's Test Kit, so this run writes no results, playbook entries, or learnings (see "Pre-register, never run" in "Gr0wthPilot copy: read first").

### Hypothesis Generation

Feed your experiment backlog from multiple sources:

| Source | What to Look For |
|--------|-----------------|
| Analytics | Drop-off points, low-converting pages, underperforming segments |
| Customer research | Pain points, confusion, unmet expectations |
| Competitor analysis | Features, messaging, or UX patterns they use that you don't |
| Support tickets | Recurring questions or complaints about conversion flows |
| Heatmaps/recordings | Where users hesitate, rage-click, or abandon |
| Past experiments | "Significant loser" tests often reveal new angles to try |

### ICE Prioritization

Score each hypothesis 1-10 on three dimensions:

| Dimension | Question |
|-----------|----------|
| **Impact** | If this works, how much will it move the primary metric? |
| **Confidence** | How sure are we this will work? (Based on data, not gut.) |
| **Ease** | How fast and cheap can we ship and measure this? |

**ICE Score** = (Impact + Confidence + Ease) / 3

Run highest-scoring experiments first. Re-score monthly as context changes.

### Experiment Velocity

Track your experimentation rate as a leading indicator of growth:

| Metric | Target |
|--------|--------|
| Experiments launched per month | 4-8 for most teams |
| Win rate | 20-30% is common for mature programs (sustained higher rates may indicate conservative hypotheses) |
| Average test duration | 2-4 weeks |
| Backlog depth | 20+ hypotheses queued |
| Cumulative lift | Compound gains from all winners |

### The Experiment Playbook

When a test wins, don't just implement it — document the pattern:

```
## [Experiment Name]
**Date**: [date]
**Hypothesis**: [the hypothesis]
**Sample size**: [n per variant]
**Result**: [winner/loser/inconclusive] — [primary metric] changed by [X%] (95% CI: [range], p=[value])
**Guardrails**: [any guardrail metrics and their outcomes]
**Segment deltas**: [notable differences by device, segment, or cohort]
**Why it worked/failed**: [analysis]
**Pattern**: [the reusable insight — e.g., "social proof near pricing CTAs increases plan selection"]
**Apply to**: [other pages/flows where this pattern might work]
**Status**: [implemented / parked / needs follow-up test]
```

Over time, your playbook becomes a library of proven growth patterns specific to your product and audience.

### Experiment Cadence

**Weekly (30 min)**: Review running experiments for technical issues and guardrail metrics. Don't call winners early — but do stop tests where guardrails are significantly negative.

**Bi-weekly**: Conclude completed experiments. Analyze results, update playbook, launch next experiment from backlog.

**Monthly (1 hour)**: Review experiment velocity, win rate, cumulative lift. Replenish hypothesis backlog. Re-prioritize with ICE.

**Quarterly**: Audit the playbook. Which patterns have been applied broadly? Which winning patterns haven't been scaled yet? What areas of the funnel are under-tested?

---

## Common Mistakes

### Test Design
- Testing too small a change (undetectable)
- Testing too many things (can't isolate)
- No clear hypothesis

### Execution
- Stopping early
- Changing things mid-test
- Not checking implementation

### Analysis
- Ignoring confidence intervals
- Cherry-picking segments
- Over-interpreting inconclusive results

---

## Task-Specific Questions

1. What's your current conversion rate?
2. How much traffic does this page get?
3. What change are you considering and why?
4. What's the smallest improvement worth detecting?
5. What tools do you have for testing?
6. Have you tested this area before?

---

## Related Skills

- **cro**: For generating test ideas based on CRO principles
- **analytics**: For setting up test measurement
- **copywriting**: For creating variant copy
