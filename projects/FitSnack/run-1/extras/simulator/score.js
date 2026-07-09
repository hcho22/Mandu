// The Consistency Score, implemented per PRD v6 US-H01, next to a classic
// streak counter - so the difference between "dents" and "zeroes" is felt,
// not described.
//
// weeklyAdherence(week) = min(1, workoutsCompleted / weeklyGoal)
// score = weightedRollingAverage(weeklyAdherence, recentWeeks) * 100,
//   recent weeks weighted more. weeklyGoal default 3.
// A 5-minute session counts as a full show-up. A single miss dents the score
// but never zeroes it. longestChain is surfaced as pride, never a threat.

'use strict';

const WEEKLY_GOAL = 3;
const WINDOW_WEEKS = 8;

// days: array of booleans (worked out that day), oldest first.
function weeks(days) {
  const out = [];
  for (let i = 0; i < days.length; i += 7) out.push(days.slice(i, i + 7));
  return out;
}

function consistencyScore(days) {
  const ws = weeks(days);
  if (!ws.length) return 0;
  const recent = ws.slice(-WINDOW_WEEKS);
  // linear recency weights: oldest week 1, newest week N
  let num = 0, den = 0;
  recent.forEach((w, i) => {
    const adherence = Math.min(1, w.filter(Boolean).length / WEEKLY_GOAL);
    const weight = i + 1;
    num += adherence * weight;
    den += weight;
  });
  return Math.round((num / den) * 100);
}

function currentStreak(days) {
  let n = 0;
  for (let i = days.length - 1; i >= 0 && days[i]; i--) n++;
  return n;
}

function longestChain(days) {
  let best = 0, cur = 0;
  for (const d of days) { cur = d ? cur + 1 : 0; best = Math.max(best, cur); }
  return best;
}

// Simulate the same person under both mechanics across a day-by-day pattern.
// Returns per-day series for charting.
function simulate(days) {
  const series = [];
  for (let i = 1; i <= days.length; i++) {
    const slice = days.slice(0, i);
    series.push({
      day: i,
      workedOut: days[i - 1],
      score: consistencyScore(slice),
      streak: currentStreak(slice),
      longestChain: longestChain(slice),
    });
  }
  return series;
}

// Canonical demo scenarios (each 8 weeks = 56 days).
function pattern(spec) {
  // spec: array of [timesPerWeek, weeksCount] pairs, sessions spread through the week
  const days = [];
  const slots = { 0: [], 1: [2], 2: [1, 4], 3: [0, 2, 4], 4: [0, 2, 4, 5], 5: [0, 1, 2, 4, 5], 6: [0, 1, 2, 3, 4, 5], 7: [0, 1, 2, 3, 4, 5, 6] };
  for (const [perWeek, count] of spec) {
    for (let w = 0; w < count; w++) {
      const week = new Array(7).fill(false);
      (slots[perWeek] || []).forEach(d => { week[d] = true; });
      days.push(...week);
    }
  }
  return days;
}

const SCENARIOS = {
  'The one missed day': (() => {
    // 3/week solid, then one week with a single miss (2/week), then back
    const d = pattern([[3, 4]]);
    d.push(...pattern([[2, 1]]));
    d.push(...pattern([[3, 3]]));
    return d;
  })(),
  'The two-week vacation': (() => {
    const d = pattern([[3, 3]]);
    d.push(...pattern([[0, 2]]));
    d.push(...pattern([[3, 3]]));
    return d;
  })(),
  'The slow fade': pattern([[3, 2], [2, 2], [1, 2], [0, 2]]),
  'The comeback': pattern([[0, 2], [1, 1], [2, 2], [3, 3]]),
};

if (typeof module !== 'undefined') module.exports = { consistencyScore, currentStreak, longestChain, simulate, SCENARIOS, pattern };
