export const meta = {
  name: 'gr0wthpilot-tournament',
  description: 'Gr0wthPilot phase 1: blind positioning and name tournament, scored by judges with differing published rubrics',
  phases: [
    { title: 'Pitch', detail: 'at least four pitchers, blind to each other' },
    { title: 'Judge', detail: 'at least three judges, each with its own published rubric' },
    { title: 'Scorecard', detail: 'every pitch ranked, with margins and the losers kept' },
  ],
}

// args: {
//   package, product, skill,
//   incumbent_name: the Product's current name or null (incumbency is not a score),
//   pitchers: [{ id, stance }]   at least 4; one stance argues against the brief's riskiest lead,
//   judges: [{ id, rubric }]     at least 3; rubric is the relative path of its published rubric file
// }
const A = args || {}
if (!A.package || (A.pitchers || []).length < 4 || (A.judges || []).length < 3) {
  throw new Error('tournament.js needs args.package, at least 4 pitchers, and at least 3 judges')
}
const P = A.package
const T = `${P}/02-brand/tournament`
const RULES = `
Rules: write only inside ${P}, with absolute paths, never starting a shell command with cd.
Creative work (names, positioning, hero messages) is invented freely; any fact you use (a competitor detail, a number, a quote) must already be in the package's research with its URL, or you fetch it and record it in ${P}/sources.d/tournament.md as \`- URL - fetched YYYY-MM-DDTHH:MMZ - what it supports\`.
Never claim a name is cleared: trademark and store-name clearance are UNVERIFIED and are the Founder's next action.
Never ask anyone anything. No em dashes. One sentence per line in Markdown.
`
const PITCH = {
  type: 'object',
  properties: { file: { type: 'string' }, name: { type: 'string' }, hero: { type: 'string' }, one_line: { type: 'string' } },
  required: ['file', 'name', 'hero', 'one_line'],
}
const SCORES = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    scores: {
      type: 'array',
      items: {
        type: 'object',
        properties: { pitch: { type: 'string' }, total: { type: 'number' }, rank: { type: 'integer' }, why: { type: 'string' } },
        required: ['pitch', 'total', 'rank', 'why'],
      },
    },
    name_verdict: { type: 'string' },
  },
  required: ['file', 'scores', 'name_verdict'],
}

phase('Pitch')
const pitches = (await parallel(
  A.pitchers.map((p, i) => () =>
    agent(
      `You are pitcher ${p.id} in Gr0wthPilot's blind tournament for ${A.product}. You have not seen any other pitch and must not look for one in ${T}.
Your stance: ${p.stance}
Read ${P}/01-research/product-facts-brief.md and the research in ${P}/01-research/, and use the methods in ${A.skill}/marketingskills/marketing-psychology/SKILL.md, ${A.skill}/marketingskills/offers/SKILL.md, and ${A.skill}/marketingskills/marketing-ideas/SKILL.md.
Pitch a complete positioning: the name (stress-test ${A.incumbent_name || 'the current working name'} and keep it or beat it; incumbency earns nothing), the category frame, the ideal customer in their own words, the hero message, three supporting messages, the enemy (what the customer is fighting, never the customer), and why this wins against the named competitors.
Write it to ${T}/pitch-${i + 1}.md, starting with "# Pitch ${i + 1}" and never naming yourself.
${RULES}`,
      { label: `pitch:${p.id}`, phase: 'Pitch', schema: PITCH },
    ),
  ),
)).filter(Boolean)
if (pitches.length < 4) throw new Error(`only ${pitches.length} pitches came back; rerun the tournament`)

phase('Judge')
const verdicts = (await parallel(
  A.judges.map(j => () =>
    agent(
      `You are the ${j.id} judge in Gr0wthPilot's tournament for ${A.product}.
Apply only your published rubric, ${P}/${j.rubric}, to every pitch file in ${T} (pitch-1.md to pitch-${pitches.length}.md). Score each criterion, total it, rank every pitch, and say in one paragraph why each loser lost.
Give your own verdict on the name: confirm the incumbent, pick a challenger, or reject all names, with the reason.
Write your report to ${T}/judge-${j.id}.md.
${RULES}`,
      { label: `judge:${j.id}`, phase: 'Judge', schema: SCORES },
    ),
  ),
)).filter(Boolean)
if (verdicts.length < 3) throw new Error(`only ${verdicts.length} judges came back; rerun the judges`)

phase('Scorecard')
const card = await agent(
  `Write Gr0wthPilot's tournament scorecard for ${A.product} to ${T}/scorecard.md from these judge results:
${JSON.stringify(verdicts, null, 1)}
Show a table of every pitch's total from every judge, its rank per judge, and its overall rank; the winning margin over the runner-up on each rubric and overall (label it "margin"); each judge's name verdict; and why each loser lost.
Report honestly: if the winner won narrowly or the judges split, say so; never protect a pitch because a brief favored it.
${RULES}`,
  { label: 'scorecard', phase: 'Scorecard' },
)
return { pitches, verdicts, scorecard: card }
