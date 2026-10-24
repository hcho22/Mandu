"""Tests for the Workflow scripts' own logic: each script runs under Node with
the Workflow tool's functions (agent, parallel, pipeline, phase, log) stubbed,
and the test checks which agents it starts.

Run from Mandu's root: python3 -m unittest discover -s .claude/skills/gr0wthpilot/tests
"""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

WORKFLOWS = Path(__file__).resolve().parent.parent / "workflows"

# Runs a workflow script the way the Workflow tool does: its body as an async
# function of the tool's globals, its `export const meta` a plain constant.
# Each agent call is answered from REPLIES by the longest label prefix.
HARNESS = r"""
const fs = require('fs')
const [script, argsJson, repliesJson] = process.argv.slice(2)
const replies = JSON.parse(repliesJson)
const labels = []
const agent = async (prompt, opts) => {
  const label = (opts && opts.label) || ''
  labels.push(label)
  const key = Object.keys(replies).filter(k => label.startsWith(k)).sort((a, b) => b.length - a.length)[0]
  return key === undefined ? '' : replies[key]
}
const parallel = async thunks => Promise.all(thunks.map(t => t()))
const pipeline = async (items, ...stages) => Promise.all(items.map(async item => {
  let value = item
  for (const stage of stages) value = await stage(value, item)
  return value
}))
const body = fs.readFileSync(script, 'utf8').replace(/^export const meta/m, 'const meta')
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor
new AsyncFunction('args', 'agent', 'parallel', 'pipeline', 'phase', 'log', body)(
  JSON.parse(argsJson), agent, parallel, pipeline, () => {}, () => {})
  .then(result => console.log(JSON.stringify({ result, labels })))
  .catch(err => { console.error(err.stack); process.exit(1) })
"""


def run_workflow(name, args, replies):
    harness = Path(tempfile.mkdtemp(prefix="gp-wf-")) / "harness.js"
    harness.write_text(HARNESS, encoding="utf-8")
    out = subprocess.run(["node", str(harness), str(WORKFLOWS / name), json.dumps(args), json.dumps(replies)],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, timeout=60)
    if out.returncode != 0:
        raise AssertionError(out.stderr)
    return json.loads(out.stdout)


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class RedTeamTest(unittest.TestCase):
    def test_fix_lanes_follow_deliverable_areas(self):
        pkg = "/Users/founder/Mandu/projects/Testprod/gtm"
        findings = {"findings": [
            {"id": "x-1", "severity": "MUST-FIX", "file": pkg + "/03-site/index.html", "problem": "p"},
            {"id": "x-2", "severity": "SHOULD-FIX", "file": pkg + "/05-social-pmf/angles.md", "problem": "p"},
            {"id": "x-3", "severity": "MUST-FIX", "file": "03-site/index-b.html", "problem": "p"},
            {"id": "x-4", "severity": "OBJECTION", "file": pkg + "/07-thesis/investment-thesis.md", "problem": "p"},
        ]}
        fixed = {"changes": [{"finding": "x-1", "file": "f", "before": "a", "after": "b", "material": True}],
                 "declined": []}
        args = {"package": pkg, "product": "Testprod", "skill": "/skill",
                "personas": [{"id": "p%d" % i, "who": "persona %d" % i, "attack": "attack"} for i in range(4)]}
        out = run_workflow("redteam.js", args, {"redteam:": findings, "fix:": fixed})
        self.assertEqual(sorted(label for label in out["labels"] if label.startswith("fix:")), ["fix:03-site", "fix:05-social-pmf"])
        self.assertEqual(out["result"]["material"], 2)


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class SkepticsTest(unittest.TestCase):
    def test_a_claim_not_every_skeptic_checked_gets_no_verdict(self):
        claims = [{"id": c, "claim": "claim %s" % c, "source": "https://x.example/%s" % c} for c in ("C1", "C2", "C3")]
        replies = {"skeptic:": {"verdict": "STANDS", "reason": "it holds"}, "skeptic:C2:source": None,
                   "skeptic:C3:scope": None}
        out = run_workflow("skeptics.js", {"package": "/p", "product": "Testprod", "claims": claims}, replies)
        self.assertEqual([v["id"] for v in out["result"]["verdicts"]], ["C1"])
        self.assertEqual(out["result"]["missing"], ["C2", "C3"])


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class ResearchTest(unittest.TestCase):
    def test_a_lane_whose_researcher_returned_nothing_is_dropped(self):
        lanes = [{"id": lid, "title": "lane %s" % lid, "task": "research", "outputs": ["01-research/%s.md" % lid]}
                 for lid in ("L1", "L2")]
        replies = {"research:L1": {"files": ["01-research/L1.md"], "claims": [], "gaps": []}, "research:L2": None}
        out = run_workflow("research.js", {"package": "/p", "product": "Testprod", "skill": "/s", "lanes": lanes},
                           replies)
        self.assertEqual([lane["lane"] for lane in out["result"]["lanes"]], ["L1"])
        self.assertEqual(out["result"]["dropped"], ["L2"])


if __name__ == "__main__":
    unittest.main()
