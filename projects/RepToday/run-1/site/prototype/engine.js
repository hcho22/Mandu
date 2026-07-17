// Deterministic mini-engine for the Ready Screen prototype.
// A faithful, simplified port of the v6 pipeline shape: shape selection ->
// pillar balance by staleness -> pool filter -> chain selection with a variety
// window -> rep/hold targets -> assembly with timing fit. Deterministic for a
// given (seed, minutes): same inputs always produce the same session, which is
// the point of the demo.

'use strict';

// --- Seeded PRNG (mulberry32) -------------------------------------------------
function rng(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function hashStr(s) {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
  return h >>> 0;
}

// --- Step 1: session shape ----------------------------------------------------
// 5-10 singleFocus, 11-20 blendLight, 21-40 blendFull, 41-60 blendExtended (PRD US-E01)
function selectShape(minutes) {
  const m = Math.min(60, Math.max(5, minutes));
  if (m <= 10) return 'singleFocus';
  if (m <= 20) return 'blendLight';
  if (m <= 40) return 'blendFull';
  return 'blendExtended';
}

// Block plan per shape: [pillar, share-of-session] pairs.
// blendExtended gets a dedicated primal block (PRD US-E02).
// The focus pillar is strength or mobility; primal (3 movements in the
// Discipline-Phase library) enters as a dedicated block in longer shapes,
// mirroring how the real engine folds primal into short sessions.
function blockPlan(shape, focusPillar) {
  const other = focusPillar === 'mobility' ? 'strength' : 'mobility';
  switch (shape) {
    case 'singleFocus': return [[focusPillar, 1.0]];
    case 'blendLight': return [[focusPillar, 0.6], [other, 0.4]];
    case 'blendFull': return [[focusPillar, 0.45], [other, 0.35], ['primal', 0.2]];
    case 'blendExtended': return [['strength', 0.4], ['mobility', 0.3], ['primal', 0.3]];
  }
}

// --- Step 2: pillar balance by staleness --------------------------------------
// history: array of {pillar} for recent sessions, most recent last.
function pickFocusPillar(history, rand) {
  const pillars = ['strength', 'mobility'];
  const staleness = { strength: 3, mobility: 3 };
  history.slice(-6).forEach((h, i) => {
    if (!(h.pillar in staleness)) return;
    // more recent sessions reduce staleness more
    staleness[h.pillar] = Math.max(0, staleness[h.pillar] - (i + 1) * 0.8);
  });
  // deterministic weighted pick by staleness
  const total = pillars.reduce((n, p) => n + staleness[p] + 0.25, 0);
  let roll = rand() * total;
  let pick = 'strength';
  for (const p of pillars) {
    roll -= staleness[p] + 0.25;
    if (roll <= 0) { pick = p; break; }
  }
  // First-Week Contrast (US-G02): never repeat yesterday's pillar back-to-back
  const last = history.length ? history[history.length - 1].pillar : null;
  if (last === pick) pick = pick === 'strength' ? 'mobility' : 'strength';
  return pick;
}

// --- Steps 4-5: pool filter + chain selection with variety window -------------
function pickExercises(pillar, count, opts) {
  const { rand, maxDifficulty, recentIds, used } = opts;
  let pool = EXERCISES.filter(e =>
    e.pillar === pillar &&
    e.difficulty <= maxDifficulty &&
    !used.has(e.id)
  );
  // variety window: avoid movements seen in the last N sessions when possible
  const fresh = pool.filter(e => !recentIds.has(e.id));
  if (fresh.length >= count) pool = fresh;
  // one movement per progression chain where possible (mirrors chain selection)
  const picked = [];
  const chains = new Set();
  const shuffled = pool
    .map(e => ({ e, k: rand() }))
    .sort((a, b) => a.k - b.k)
    .map(x => x.e);
  for (const e of shuffled) {
    if (picked.length >= count) break;
    if (chains.has(e.chain) && shuffled.length - picked.length > count) continue;
    picked.push(e); chains.add(e.chain);
  }
  // backfill if chains constraint starved us
  for (const e of shuffled) {
    if (picked.length >= count) break;
    if (!picked.includes(e)) picked.push(e);
  }
  picked.forEach(e => used.add(e.id));
  return picked;
}

// --- Steps 6-7: targets + assembly with timing fit -----------------------------
const REST_SECONDS = 25;

function prescribe(e, sets) {
  return {
    id: e.id, name: e.name, pillar: e.pillar, pattern: e.pattern,
    difficulty: e.difficulty, isHold: e.isHold,
    sets,
    target: e.isHold ? (e.holdSec + 's hold') : (e.reps + ' reps'),
    secondsPerSet: e.timePerSet,
    totalSeconds: sets * e.timePerSet + (sets - 1) * REST_SECONDS,
  };
}

function generateSession(seedStr, minutes, history) {
  history = history || [];
  const m = Math.min(60, Math.max(5, minutes));
  const rand = rng(hashStr(seedStr + ':' + m));
  const shape = selectShape(m);
  const focus = pickFocusPillar(history, rand);
  const plan = blockPlan(shape, focus);
  const budget = m * 60;
  const maxDifficulty = 3; // capped starting difficulty band, served gentle
  const recentIds = new Set(history.slice(-3).flatMap(h => h.exerciseIds || []));
  const used = new Set();

  const blocks = [];
  for (const [pillar, share] of plan) {
    const blockBudget = budget * share;
    // rough sizing: 2 sets per movement; each slot ~2*timePerSet+rest
    const estSlot = 2 * 40 + REST_SECONDS;
    const count = Math.min(5, Math.max(1, Math.round(blockBudget / estSlot)));
    const picks = pickExercises(pillar, count, { rand, maxDifficulty, recentIds, used });
    if (picks.length) blocks.push({ pillar, exercises: picks.map(e => prescribe(e, 2)) });
  }

  // timing fit: nudge sets up/down until within +/-60s of budget (PRD Step 7)
  const all = () => blocks.flatMap(b => b.exercises);
  const totalSec = () => all().reduce((n, x) => n + x.totalSeconds, 0);
  let guard = 0;
  while (totalSec() > budget + 60 && guard++ < 40) {
    const longest = all().filter(x => x.sets > 1).sort((a, b) => b.totalSeconds - a.totalSeconds)[0];
    if (!longest) break;
    longest.sets -= 1;
    longest.totalSeconds = longest.sets * longest.secondsPerSet + (longest.sets - 1) * REST_SECONDS;
  }
  while (totalSec() < budget - 60 && guard++ < 80) {
    const shortest = all().filter(x => x.sets < 4).sort((a, b) => a.totalSeconds - b.totalSeconds)[0];
    if (!shortest) break;
    shortest.sets += 1;
    shortest.totalSeconds = shortest.sets * shortest.secondsPerSet + (shortest.sets - 1) * REST_SECONDS;
  }

  return {
    shape, focus, minutes: m,
    estimatedMinutes: Math.round(totalSec() / 60),
    blocks,
    varietyLine: varietyLine(focus, history),
    exerciseIds: all().map(x => x.id),
  };
}

// Variety Language template (PRD US-G03): only names a contrast the engine produced.
function varietyLine(focus, history) {
  const label = { strength: 'a strength day', mobility: 'a mobility day', primal: 'a primal movement day' };
  const last = history.length ? history[history.length - 1].pillar : null;
  if (last && last !== focus) return 'Today’s ' + label[focus] + ' – yesterday was ' + last + '.';
  return 'Today’s ' + label[focus] + '.';
}

// Deterministic swap (PRD US-C08): same pillar + pattern, difficulty within 1,
// not already in the session; null when no safe peer exists.
function swapExercise(session, exerciseId) {
  for (const block of session.blocks) {
    const idx = block.exercises.findIndex(x => x.id === exerciseId);
    if (idx < 0) continue;
    const cur = block.exercises[idx];
    const inSession = new Set(session.blocks.flatMap(b => b.exercises.map(x => x.id)));
    const peer = EXERCISES.find(e =>
      e.pillar === cur.pillar && e.pattern === cur.pattern &&
      Math.abs(e.difficulty - cur.difficulty) <= 1 && !inSession.has(e.id)
    );
    if (!peer) return null;
    const swapped = prescribe(peer, cur.sets);
    block.exercises[idx] = swapped;
    session.exerciseIds = session.blocks.flatMap(b => b.exercises.map(x => x.id));
    return swapped;
  }
  return null;
}

if (typeof module !== 'undefined') module.exports = { generateSession, swapExercise, selectShape };
