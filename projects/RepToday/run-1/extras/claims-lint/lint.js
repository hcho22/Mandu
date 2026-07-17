#!/usr/bin/env node
// Voice-contract lint: machine-checks every user-facing Nonzero asset against
// the brand guidelines (brand/brand-guidelines.md section 6) and the approved
// claims list (thesis/thesis.md section 5). The same idea as an eval gate in
// CI: the voice contract is a spec, so violations should be caught by a
// program, not a proofread.
//
// Usage: node lint.js        (from anywhere; paths resolve relative to run-1)
// Exit code 0 = clean, 1 = violations found.

'use strict';
const fs = require('fs');
const path = require('path');

const RUN1 = path.resolve(__dirname, '..', '..');

// User-facing assets only. Internal docs (research, thesis, gtm, build log)
// legitimately quote banned phrases while discussing them.
const TARGETS = [
  'site/index.html',
  'site/prototype/index.html',
  'videos/launch/frame.html',
  'videos/founder/frame.html',
  'videos/founder-script.md',
  'extras/app-store-listing.md',
  'extras/simulator/index.html',
];

// [name, regex, why]
const RULES = [
  ['em dash', /—/, 'voice contract: plain dashes only'],
  ['exclamation mark', /!/, 'voice contract: full stops do the emphasis'],
  ['emoji', /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{FE0F}]/u, 'voice contract: no emojis'],
  ['AI marketing', /\bAI[- ](powered|coach|driven|fitness)\b|\bpowered by (machine learning|AI)\b|\bmachine[- ]learning\b/i, 'the app is quiet about its intelligence'],
  ['banned outcome claim', /\b(burn(s|ing)? fat|fat[- ]?burn|get shredded|six[- ]pack|summer body|weight[- ]?loss|lose weight|blood pressure|add(s)? years|live longer|longevity)\b/i, 'claims must stay inside the evidence (thesis section 5)'],
  ['strength promise', /\b(builds?|gain) (strength|muscle)\b/i, 'banned for the micro format (BJSM null result)'],
  ['only-app claim', /\bthe only (app|workout app|fitness app)\b/i, 'refuted broad-uniqueness claim (verification.md)'],
  ['wrong name casing', /\bNonZero\b|\bNon-Zero\b|\bNONZERO\b/, 'the name is "Nonzero" (wordmark "nonzero")'],
  ['internal codename', /\bFitSnack\b/, 'engineering codename must not be user-facing'],
  ['marketing fluff', /\b(revolutionary|game[- ]chang(er|ing)|crush your goals|unleash|supercharge|transform your (life|body))\b/i, 'no marketing fluff'],
  ['streak shaming', /\bstreaks are (toxic|bad|broken|evil)\b/i, 'respect the streak-lovers'],
];

// Waivers: honest negation is allowed to NAME a banned claim while refusing
// it. Each waiver is scoped to one file, one rule, and a context regex the
// offending line must also match. Anything else still fails.
const ALLOW = [
  { file: 'site/index.html', rule: 'banned outcome claim', context: /won't claim|will not (claim|promise)/i,
    reason: 'the honesty box names the claims it refuses' },
  { file: 'site/index.html', rule: 'AI marketing', context: /Is this another AI coach\?/i,
    reason: 'FAQ voices the objection in order to answer it' },
  { file: 'videos/founder-script.md', rule: 'AI marketing', context: /no "AI-powered" claims/i,
    reason: 'compliance note quoting the rule itself' },
  { file: 'extras/app-store-listing.md', rule: 'banned outcome claim', context: /We will not promise|No banned claims/i,
    reason: 'honest refusal line + compliance checklist' },
  { file: 'extras/app-store-listing.md', rule: 'AI marketing', context: /No banned claims|no "AI-powered/i,
    reason: 'compliance checklist quoting the rule' },
  { file: 'extras/app-store-listing.md', rule: 'wrong name casing', context: /unrelated "NonZero" productivity app/,
    reason: 'names a third-party app by its own casing' },
];

function waived(rel, rule, line) {
  return ALLOW.some(a => a.file === rel && a.rule === rule && a.context.test(line));
}

// What the linter checks: human-visible text. For HTML that means text outside
// tags with <script>/<style> removed (code legitimately contains "!").
// Removed blocks are replaced with blank lines so line numbers stay true.
function blank(match) { return match.replace(/[^\n]/g, ''); }
function visibleText(file, src) {
  if (!file.endsWith('.html')) return src;
  return src
    .replace(/<script[\s\S]*?<\/script>/gi, blank)
    .replace(/<style[\s\S]*?<\/style>/gi, blank)
    .replace(/<!--[\s\S]*?-->/g, blank)
    .replace(/<[^>]+>/g, ' ');
}

let violations = 0;
for (const rel of TARGETS) {
  const file = path.join(RUN1, rel);
  if (!fs.existsSync(file)) {
    console.log(`MISSING  ${rel}`);
    violations++;
    continue;
  }
  const text = visibleText(rel, fs.readFileSync(file, 'utf8'));
  const lines = text.split('\n');
  const hits = [];
  lines.forEach((line, i) => {
    for (const [name, re, why] of RULES) {
      const m = line.match(re);
      if (m && !waived(rel, name, line)) hits.push({ line: i + 1, name, why, sample: m[0] });
    }
  });
  if (hits.length) {
    violations += hits.length;
    console.log(`FAIL     ${rel}`);
    for (const h of hits) console.log(`         line ${h.line}: [${h.name}] "${h.sample}" (${h.why})`);
  } else {
    console.log(`ok       ${rel}`);
  }
}

console.log(violations ? `\n${violations} violation(s).` : '\nClean: every user-facing asset honors the voice contract and the approved-claims list.');
process.exit(violations ? 1 : 0);
