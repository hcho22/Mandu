export const meta = {
  name: 'gr0wthpilot-brand-gate',
  description: 'Gr0wthPilot phase 1 gate: a fresh agent given only the brand guidelines makes one new asset; a reviewer judges it on-brand or not',
  phases: [
    { title: 'Fresh agent', detail: 'sees the guidelines and nothing else' },
    { title: 'Review', detail: 'renders the asset, views it, and judges it against the guidelines' },
  ],
}

// args: { package, product, round, guidelines: the full text of 02-brand/brand-guidelines.md, asset: what to make }
const A = args || {}
if (!A.package || !A.guidelines) throw new Error('brand-gate.js needs args.package and args.guidelines (the full text)')
const P = A.package
const round = A.round || 1
const ASSET = {
  type: 'object',
  properties: { html: { type: 'string' }, notes: { type: 'string' } },
  required: ['html', 'notes'],
}

phase('Fresh agent')
// The Plan agent type starts without the project's CLAUDE.md, so the
// guidelines below are the only thing it knows about this brand.
const made = await agent(
  `You are a designer who has never seen this brand. Everything you know about it is the brand guidelines below; read no file and fetch nothing.
Make one new asset: ${A.asset || 'a 1080x1080 social announcement card for the product'}.
Return it as one complete, self-contained HTML document (inline CSS and SVG only, no external files, scripts, or images) that renders the asset at its exact pixel size, plus notes on every choice you made and every place the guidelines left you guessing.
Brand guidelines:
-----
${A.guidelines}
-----`,
  { label: 'fresh-agent', phase: 'Fresh agent', agentType: 'Plan', schema: ASSET },
)
if (!made) throw new Error('the fresh agent returned nothing; rerun the gate')

phase('Review')
const review = await agent(
  `Review Gr0wthPilot's brand gate, round ${round}, for ${A.product}.
1. Write this HTML to ${P}/02-brand/gate-test-asset${round > 1 ? '-r' + round : ''}.html exactly as given.
2. Render it with \`gp-chrome screenshot ${P}/02-brand/gate-test-asset${round > 1 ? '-r' + round : ''}.html ${P}/02-brand/gate-test-asset${round > 1 ? '-r' + round : ''}.png WIDTHxHEIGHT\` (the asset's own size), run on its own as a single command, then view the PNG.
3. Judge it against ${P}/02-brand/brand-guidelines.md: palette, type, logo use, layout, voice, and every do and don't. It is on-brand only if a stranger would take it for the same brand.
4. Append a "## Round ${round}" section to ${P}/02-brand/gate-test-report.md (create the file with a title if needed): what the fresh agent made, what you saw in the render, each mismatch, each gap in the guidelines the fresh agent's notes reveal, and a last line "Verdict: PASS" or "Verdict: FAIL".
A FAIL is an honest result: the guidelines get fixed and the gate runs again.
Write only inside ${P}, with absolute paths, never starting a shell command with cd. No em dashes.
Fresh agent's notes: ${made.notes}
HTML:
${made.html}`,
  { label: 'brand-review', phase: 'Review', schema: { type: 'object', properties: { verdict: { type: 'string', enum: ['PASS', 'FAIL'] }, gaps: { type: 'array', items: { type: 'string' } } }, required: ['verdict', 'gaps'] } },
)
return review
