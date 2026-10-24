export const meta = {
  name: 'gr0wthpilot-critic',
  description: 'Gr0wthPilot: the completeness critic checks a phase against its exit criteria and may send it back',
  phases: [
    { title: 'Critique', detail: 'an exit-criteria auditor and a what-is-missing reader, independently' },
    { title: 'Verdict', detail: 'PASS only when both pass' },
  ],
}

// args: { package, product, phase: '1'..'5', round, criteria: [exit criteria strings from references/phase-gates.md] }
const A = args || {}
if (!A.package || !A.phase || !Array.isArray(A.criteria) || A.criteria.length === 0) {
  throw new Error('critic.js needs args.package, args.phase, and the phase exit criteria')
}
const P = A.package
const round = A.round || 1
const GAPS = {
  type: 'object',
  properties: {
    pass: { type: 'boolean' },
    gaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: { criterion: { type: 'string' }, gap: { type: 'string' }, evidence: { type: 'string' }, send_back: { type: 'string' } },
        required: ['gap', 'send_back'],
      },
    },
  },
  required: ['pass', 'gaps'],
}
const RULES = `You only read the package; write nothing. You have authority to send the phase back: a criterion is met only when a file in the package shows it, not when someone says so. Never ask anyone anything.`
const criteria = A.criteria.map((c, i) => `${i + 1}. ${c}`).join('\n')

phase('Critique')
const lenses = [
  `Exit-criteria auditor: check each criterion below against the files in ${P}, one by one, and open the files that would prove it.`,
  `What-is-missing reader: ignore the checklist's wording and ask what a demanding stranger would find missing or unearned in this phase: a research angle never run, a claim never verified, a source never read, a screen never shown, a deliverable that is a placeholder pretending to be finished, an assumption not labeled.`,
]
const reads = (await parallel(
  lenses.map((lens, i) => () =>
    agent(
      `You are Gr0wthPilot's completeness critic for phase ${A.phase} of ${A.product}'s Candidate Package, round ${round}.
${lens}
Exit criteria for phase ${A.phase}:
${criteria}
${RULES}
Return pass true only if nothing material is missing, and each gap with what must be done to close it.`,
      { label: `critic:${A.phase}:${i === 0 ? 'criteria' : 'missing'}`, phase: 'Critique', schema: GAPS },
    ),
  ),
)).filter(Boolean)
if (reads.length < 2) throw new Error('a critic returned nothing; rerun the critic')
const pass = reads.every(r => r.pass)

phase('Verdict')
await agent(
  `Append a "## Round ${round}" section to ${P}/08-redteam/critic-phase-${A.phase}.md (create it with the title "# Completeness critic, phase ${A.phase}" if needed).
List each gap below with what must be done, then end the section with the line "Verdict: ${pass ? 'PASS' : 'SEND BACK'}".
Write only that file, with an absolute path, never starting a shell command with cd. No em dashes.
Gaps: ${JSON.stringify(reads.flatMap(r => r.gaps), null, 1)}`,
  { label: `critic:${A.phase}:verdict`, phase: 'Verdict' },
)
return { verdict: pass ? 'PASS' : 'SEND BACK', gaps: reads.flatMap(r => r.gaps) }
