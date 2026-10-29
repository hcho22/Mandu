export const meta = {
  name: 'gr0wthpilot-tournament',
  description: 'Gr0wthPilot phase 1: blind positioning and name tournament, scored by judges with differing published rubrics',
  phases: [
    { title: 'Pitch', detail: 'at least four pitchers, blind to each other' },
    { title: 'Collisions', detail: 'name-only rerun: store, web, and domain evidence for every pitched name' },
    { title: 'Judge', detail: 'at least three judges, each with its own published rubric' },
    { title: 'Scorecard', detail: 'every pitch ranked, with margins and the losers kept' },
  ],
}

// args: {
//   package, product, skill,
//   incumbent_name: the Product's current name or null (incumbency is not a score),
//   pitchers: [{ id, stance }]   at least 4; one stance argues against the brief's riskiest lead,
//   judges: [{ id, rubric }]     at least 3; rubric is the relative path of its published rubric file
//   name_only: optional, for a name-only rerun (the launcher's --rename): {
//     old_name: the name App Store Connect refused,
//     ruled_out: [names], ruled_out_roots: [roots]   from the journal's rename block; old_name is among ruled_out,
//     fixed: relative path of the file quoting the positioning, hero message, and look the rerun keeps,
//     names_per_pitch: names each pitcher ranks (default 3)
//   }
// }
const A = args || {}
if (!A.package || (A.pitchers || []).length < 4 || (A.judges || []).length < 3) {
  throw new Error('tournament.js needs args.package, at least 4 pitchers, and at least 3 judges')
}
const N = A.name_only || null
if (N && (!N.old_name || !N.fixed || !(N.ruled_out || []).length)) {
  throw new Error('a name-only tournament needs name_only.old_name, name_only.ruled_out, and name_only.fixed')
}
const P = A.package
const T = `${P}/02-brand/tournament`
const PER = N ? N.names_per_pitch || 3 : 1
const RULED_OUT = N
  ? `
Ruled out, never pitched, and disqualified if pitched: ${N.ruled_out.join(', ')}${(N.ruled_out_roots || []).length ? `, and every name that contains ${N.ruled_out_roots.map(r => `"${r}"`).join(' or ')} in any case or spacing` : ''}.
App Store Connect refused ${N.old_name}; a name close to it in sound or spelling carries the same risk.
`
  : ''
const FIXED = N
  ? `
This is a name-only rerun: the positioning, the hero message, and the look are fixed, quoted in ${P}/${N.fixed}; they are inputs, never pitched again or changed.
`
  : ''
const RULES = `
Rules: write only inside ${P}, with absolute paths, never starting a shell command with cd.
Creative work (names, positioning, hero messages) is invented freely; any fact you use (a competitor detail, a number, a quote) must already be in the package's research with its URL, or you fetch it and record it in ${P}/sources.d/tournament.md as \`- URL - fetched YYYY-MM-DDTHH:MMZ - what it supports\`.
Never claim a name is cleared: trademark and store-name clearance are UNVERIFIED and are the Founder's next action.
Never ask anyone anything. No em dashes. One sentence per line in Markdown.
${FIXED}${RULED_OUT}`
const PITCH = {
  type: 'object',
  properties: { file: { type: 'string' }, name: { type: 'string' }, hero: { type: 'string' }, one_line: { type: 'string' } },
  required: ['file', 'name', 'hero', 'one_line'],
}
const NAME_PITCH = {
  type: 'object',
  properties: { file: { type: 'string' }, names: { type: 'array', items: { type: 'string' } }, one_line: { type: 'string' } },
  required: ['file', 'names', 'one_line'],
}
const EVIDENCE = {
  type: 'object',
  properties: { file: { type: 'string' }, names: { type: 'array', items: { type: 'string' } } },
  required: ['file', 'names'],
}
const SCORES = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    scores: {
      type: 'array',
      items: {
        type: 'object',
        // pitch: the pitch file, or in a name-only tournament the name
        properties: { pitch: { type: 'string' }, total: { type: 'number' }, rank: { type: 'integer' }, why: { type: 'string' } },
        required: ['pitch', 'total', 'rank', 'why'],
      },
    },
    name_verdict: { type: 'string' },
  },
  required: ['file', 'scores', 'name_verdict'],
}

phase('Pitch')
const pitchTask = (p, i) =>
  N
    ? `Read ${P}/${N.fixed}, ${P}/01-research/product-facts-brief.md, ${P}/01-research/name-collisions.md, and the research in ${P}/01-research/, and use the methods in ${A.skill}/marketingskills/marketing-psychology/SKILL.md and ${A.skill}/marketingskills/marketing-ideas/SKILL.md.
Pitch names only: ${PER} names, ranked, your lead first. For each give the store title it would carry, how it carries the fixed positioning and hero message, what a stranger hears in it, and its weakest point.
Write it to ${T}/pitch-${i + 1}.md, starting with "# Pitch ${i + 1}" and never naming yourself.`
    : `Read ${P}/01-research/product-facts-brief.md and the research in ${P}/01-research/, and use the methods in ${A.skill}/marketingskills/marketing-psychology/SKILL.md, ${A.skill}/marketingskills/offers/SKILL.md, and ${A.skill}/marketingskills/marketing-ideas/SKILL.md.
Pitch a complete positioning: the name (stress-test ${A.incumbent_name || 'the current working name'} and keep it or beat it; incumbency earns nothing), the category frame, the ideal customer in their own words, the hero message, three supporting messages, the enemy (what the customer is fighting, never the customer), and why this wins against the named competitors.
Write it to ${T}/pitch-${i + 1}.md, starting with "# Pitch ${i + 1}" and never naming yourself.`
const pitches = (await parallel(
  A.pitchers.map((p, i) => () =>
    agent(
      `You are pitcher ${p.id} in Gr0wthPilot's blind tournament for ${A.product}. You have not seen any other pitch and must not look for one in ${T}.
Your stance: ${p.stance}
${pitchTask(p, i)}
${RULES}`,
      { label: `pitch:${p.id}`, phase: 'Pitch', schema: N ? NAME_PITCH : PITCH },
    ),
  ),
)).filter(Boolean)
if (pitches.length < 4) throw new Error(`only ${pitches.length} pitches came back; rerun the tournament`)

let collisions = []
if (N) {
  phase('Collisions')
  collisions = (await parallel(
    pitches.map((pitch, i) => () =>
      agent(
        `You check name collisions for Gr0wthPilot's name-only tournament for ${A.product}, the way its research step does (${A.skill}/references/research.md, "Collisions").
For every name in ${pitch.file} (${(pitch.names || []).join(', ')}): what the US App Store shows (WebSearch, then fetch each apps.apple.com listing you cite), what the web shows, and what registry lookups show for its likely domains (RDAP responses, such as https://pubapi.registry.google/rdap/domain/<name>.app and https://rdap.verisign.com/com/v1/domain/<name>.com).
Write ${T}/collisions-${i + 1}.md with a "## <Name>" section per name holding three lines, "- App Store:", "- Web:", and "- Domains:", each citing the URLs it rests on, or saying "none seen" when a search showed nothing (an app a search did not show may still exist), and "Clearance: UNVERIFIED".
Record every URL you cite in ${P}/sources.d/tournament-collisions-${i + 1}.md.
Never say a name is clear or available, and never judge it.
${RULES}`,
        { label: `collisions:${A.pitchers[i].id}`, phase: 'Collisions', schema: EVIDENCE },
      ),
    ),
  )).filter(Boolean)
}

phase('Judge')
const judgeTask = rubric => N
  ? `Apply only your published rubric, ${P}/${rubric}, to every name pitched in ${T} (pitch-1.md to pitch-${pitches.length}.md), with the collision evidence in ${T}/collisions-*.md. A ruled-out name scores zero and is listed as disqualified. Score each criterion per name, total it, rank every name, and say in one line why each lower name lost.
Give your own verdict: your pick, then the fallbacks you would accept in order, with the reason.`
  : `Apply only your published rubric, ${P}/${rubric}, to every pitch file in ${T} (pitch-1.md to pitch-${pitches.length}.md). Score each criterion, total it, rank every pitch, and say in one paragraph why each loser lost.
Give your own verdict on the name: confirm the incumbent, pick a challenger, or reject all names, with the reason.`
const verdicts = (await parallel(
  A.judges.map(j => () =>
    agent(
      `You are the ${j.id} judge in Gr0wthPilot's tournament for ${A.product}.
${judgeTask(j.rubric)}
Write your report to ${T}/judge-${j.id}.md.
${RULES}`,
      { label: `judge:${j.id}`, phase: 'Judge', schema: SCORES },
    ),
  ),
)).filter(Boolean)
if (verdicts.length < 3) throw new Error(`only ${verdicts.length} judges came back; rerun the judges`)

phase('Scorecard')
const card = await agent(
  N
    ? `Write Gr0wthPilot's name-only tournament scorecard for ${A.product} to ${T}/scorecard.md from these judge results:
${JSON.stringify(verdicts, null, 1)}
Show a table of every pitched name's total from every judge, its rank per judge, and its overall rank; the margin between each name and the next on each rubric and overall (label it "margin"); the disqualified names and why; each judge's pick and fallbacks; and why each lower name lost.
Report honestly: if the judges split or the margins are narrow, say so.
${RULES}`
    : `Write Gr0wthPilot's tournament scorecard for ${A.product} to ${T}/scorecard.md from these judge results:
${JSON.stringify(verdicts, null, 1)}
Show a table of every pitch's total from every judge, its rank per judge, and its overall rank; the winning margin over the runner-up on each rubric and overall (label it "margin"); each judge's name verdict; and why each loser lost.
Report honestly: if the winner won narrowly or the judges split, say so; never protect a pitch because a brief favored it.
${RULES}`,
  { label: 'scorecard', phase: 'Scorecard' },
)
return { pitches, collisions, verdicts, scorecard: card }
