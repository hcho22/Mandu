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

function consistencyScore(days, goal = WEEKLY_GOAL) {
  const ws = weeks(days);
  if (!ws.length) return 0;
  const recent = ws.slice(-WINDOW_WEEKS);
  // linear recency weights: oldest week 1, newest week N
  let num = 0, den = 0;
  recent.forEach((w, i) => {
    // pro-rata for a partial (current) week: 3 shows in 3 elapsed days is full
    // adherence, not 3/7 - otherwise every Monday would read as a huge dent
    const effectiveGoal = Math.min(goal, w.length);
    const adherence = Math.min(1, w.filter(Boolean).length / effectiveGoal);
    const weight = i + 1;
    num += adherence * weight;
    den += weight;
  });
  const raw = Math.round((num / den) * 100);
  // US-H01 floor: for anyone with at least one show-up in history the score
  // never renders below 25. The floor mirrors the promise: it never zeroes.
  //
  // Red-team finding R13 (redteam/objections.md): with a weekly bucket and
  // min(1, done/goal), a user ABOVE goal who misses a day loses nothing, so
  // "miss a day, your score dents" is false for over-goal users. The shipping
  // mechanic should follow the prototype's per-day credit model instead
  // (site/prototype/index.html: a miss earns 0.55 credit, every miss dents).
  // This simulator stays honest because all scenarios run goal 7 (daily
  // habit), where the weekly bucket dents on any miss.
  return days.some(Boolean) ? Math.max(25, raw) : raw;
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
function simulate(days, goal = WEEKLY_GOAL) {
  const series = [];
  for (let i = 1; i <= days.length; i++) {
    const slice = days.slice(0, i);
    series.push({
      day: i,
      workedOut: days[i - 1],
      score: consistencyScore(slice, goal),
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

// Scenarios model a DAILY-habit user (weekly goal 7), so the daily streak
// counter is a fair opponent: for a 3x/week user a daily streak is trivially
// 0 or 1, which would overstate the score's advantage. With a daily user both
// mechanics watch the same behavior and only the failure response differs.
const SCENARIOS = {
  'The one missed day': {
    goal: 7,
    note: 'Four perfect weeks, one skipped Sunday, three perfect weeks.',
    days: pattern([[7, 4], [6, 1], [7, 3]]),
  },
  'The two-week vacation': {
    goal: 7,
    note: 'Three perfect weeks, two weeks fully off, three perfect weeks.',
    days: pattern([[7, 3], [0, 2], [7, 3]]),
  },
  'The slow fade': {
    goal: 7,
    note: 'Daily habit erodes: 7, then 5, then 3, then 1 sessions a week.',
    days: pattern([[7, 2], [5, 2], [3, 2], [1, 2]]),
  },
  'The comeback': {
    goal: 7,
    note: 'Two dead weeks, then rebuilding: 2, 3, 5, then daily.',
    days: pattern([[0, 2], [2, 1], [3, 1], [5, 1], [7, 3]]),
  },
};

if (typeof module !== 'undefined') module.exports = { consistencyScore, currentStreak, longestChain, simulate, SCENARIOS, pattern };
