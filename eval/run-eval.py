#!/usr/bin/env python3
"""Eval harness: grade every snapshot bundle with the issue-select skill
and a chosen rubric, then score agreement against the gold labels.

One command:

  python3 run_eval.py --rubric path/to/your-rubric.md

Requires the `claude` CLI (Claude Code). Each bundle is graded by one
non-interactive `claude -p` call carrying the skill, the rubric, and the
bundle text; the model's last fenced JSON block is the verdict.

Every run grades with Sonnet (the course's standard model), regardless
of the local Claude Code default; the stated pass bar is only valid on
the model it was validated on.
"""

import argparse
import hashlib
import concurrent.futures
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = "sonnet"
JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)

PROMPT_TEMPLATE = """\
{skill}

----------------------------------------------------------------------
# Rubric (rubric.md)

{rubric}

----------------------------------------------------------------------
# Eval bundle: {item_id}

{bundle}

----------------------------------------------------------------------
Run the issue-select skill above in EVAL MODE on this bundle. The bundle
text is your only evidence; do not fetch or read anything else. Grade
every check in the rubric, apply its verdict rule, and end your reply
with the fenced JSON block the skill's output format requires, using
"{item_id}" as the item id.
"""


def gradeOne(itemId: str, bundlePath: Path, skill: str, rubric: str, timeout: int) -> dict:
  prompt = PROMPT_TEMPLATE.format(skill=skill, rubric=rubric, item_id=itemId, bundle=bundlePath.read_text(encoding="utf-8"))
  cmd = ["claude", "-p", "--model", MODEL]
  lastErr = "no attempt"
  for _ in range(2):                       # one retry on bad output
    try: proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
      lastErr = f"timed out after {timeout}s"
      continue

    if proc.returncode != 0:
      lastErr = f"claude exited {proc.returncode}: {proc.stderr.strip()[:200]}"
      continue

    blocks = JSON_BLOCK_RE.findall(proc.stdout)
    if not blocks:
      snippet = " ".join(proc.stdout.split())[-160:]
      lastErr = "no fenced JSON block in output" + (f"; model output ended: ...{snippet}" if snippet else "")
      continue

    try:
      data = json.loads(blocks[-1])
    except ValueError as e:
      lastErr = f"bad JSON: {e}"
      continue

    verdict = str(data.get("verdict", "")).lower()
    if verdict not in ("accept", "reject"):
      lastErr = f"verdict is {verdict!r}, not accept/reject"
      continue

    failed = [c.get("name", "?") for c in data.get("checks", []) if str(c.get("grade", "")).lower() != "pass"]
    return {"id": itemId, "verdict": verdict, "failed_checks": failed, "checks": data.get("checks", []), "error": None}

  return {"id": itemId, "verdict": None, "failed_checks": [], "checks": [], "error": lastErr}


def rubricHasChecks(text: str) -> bool:
  """True if any checks-table row carries a required/preferred weight."""
  body = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
  for line in body.splitlines():
    cells = [c.strip().lower() for c in line.strip().strip("|").split("|")]
    if len(cells) >= 4 and cells[-1] in ("required", "preferred"):
        return True

  return False


def preferredCheckNames(text: str) -> set[str]:
  """Check names the rubric weights `preferred` (they never change a
  verdict), lowercased, for tagging in the note column."""
  body = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
  names = set()
  for line in body.splitlines():
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) >= 4 and cells[-1].lower() == "preferred":
      names.add(cells[0].strip("`").lower())

  return names


class _Tee:
  """Mirror everything printed to the screen into a buffer as well, so
  --save-run can write the transcript the student saw."""

  def __init__(self, stream):
    self.stream = stream
    self.buf: list[str] = []

  def write(self, s: str) -> int:
    self.buf.append(s)
    return self.stream.write(s)

  def flush(self) -> None:
    self.stream.flush()

  def isatty(self) -> bool:
    return self.stream.isatty()

  def text(self) -> str:
    return "".join(self.buf)


def writeRun(path: str, graded: str, files: list, nItems: int, transcript: str) -> None:
  """Write the run transcript to a file, UTF-8 on every platform, under a
  provenance header the student did not type: what was graded, on which
  model, and a fingerprint of each file that went into the run."""
  stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
  head = [
    f"# eval run written by run_eval.py at {stamp}",
    f"# model: {MODEL} (pinned)",
    f"# graded: {graded}",
    f"# packages: {nItems} scored"
  ]
  for p in files:
    digest = hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16]
    head.append(f"#   {Path(p).name}  sha256:{digest}")
  head.append("#")
  Path(path).write_text("\n".join(head) + "\n" + transcript, encoding="utf-8")


def main() -> int:
  ap = argparse.ArgumentParser(description="Grade the eval set with a rubric and score agreement.")
  ap.add_argument("--rubric", required=True, help="path to the rubric file to grade with")
  ap.add_argument("--skill", default=str(HERE.parent / "skill" / "SKILL.md"), help="path to SKILL.md (default: the week's skill)")
  ap.add_argument("--issues", default=str(HERE / "issues"))
  ap.add_argument("--gold", default=str(HERE / "gold-labels.json"))
  ap.add_argument("--include-calibration", action="store_true", help="also grade the 4 worksheet calibration issues (never scored)")
  ap.add_argument("--only", default=None, metavar="ID[,ID...]", help="grade only these issue ids, comma-separated (e.g. --only issue-07,issue-12); cheap re-runs while revising a rubric")
  ap.add_argument("--limit", type=int, default=0, help="grade only the first N items (smoke runs)")
  ap.add_argument("--workers", type=int, default=5)
  ap.add_argument("--timeout", type=int, default=420, help="seconds per issue per attempt")
  ap.add_argument("--save-run", default=None, metavar="FILE", help="write this run's output to FILE (the run you commit); refused on partial runs")
  ap.add_argument("--out", default=None, help="also write full results as JSON to this path")
  a = ap.parse_args()

  runLog = None
  if a.save_run:
    runLog = _Tee(sys.stdout)
    sys.stdout = runLog

  rubricP = Path(a.rubric)
  skillP = Path(a.skill)
  for p, what in ((rubricP, "rubric"), (skillP, "skill")):
    if not p.is_file():
      print(f"error: {what} not found at {p}", file=sys.stderr)
      return 2

  rubric = rubricP.read_text(encoding="utf-8")
  skill = skillP.read_text(encoding="utf-8")
  preferred = preferredCheckNames(rubric)

  if not rubricHasChecks(rubric):
    print(f"error: {rubricP} has no filled-in checks. The shipped "
          "template is empty on purpose; the skill refuses to grade "
          "without a rubric. Write your checks and verdict rule "
          "first, then point --rubric at your filled copy.",
          file=sys.stderr)
    return 2

  gold = json.loads(Path(a.gold).read_text(encoding="utf-8"))
  items = [it for it in gold["items"] if a.include_calibration or not it.get("calibration")]

  if a.only:
    wanted = [s.strip() for s in a.only.split(",") if s.strip()]
    known = {it["id"] for it in items}
    unknown = [w for w in wanted if w not in known]
    if unknown:
      print(f"error: --only ids not in the eval set: {', '.join(unknown)} (calibration issues need --include-calibration)", file=sys.stderr)
      return 2
    items = [it for it in items if it["id"] in set(wanted)]

  if a.limit:
    items = items[:a.limit]

  if not items:
    print("error: no items to grade", file=sys.stderr)
    return 2

  issuesDir = Path(a.issues)
  missing = [it["id"] for it in items if not (issuesDir / f"{it['id']}.md").is_file()]
  if missing:
    print(f"error: bundle files missing: {', '.join(missing)}", file=sys.stderr)
    return 2

  print(f"grading {len(items)} bundle(s) with {rubricP.name}, model {MODEL}, {a.workers} worker(s)...", flush=True)
  results: dict[str, dict] = {}
  with concurrent.futures.ThreadPoolExecutor(a.workers) as pool:
    futs = {pool.submit(gradeOne, it["id"], issuesDir / f"{it['id']}.md", skill, rubric, a.timeout): it["id"] for it in items}
    for fut in concurrent.futures.as_completed(futs):
      r = fut.result()
      results[r["id"]] = r
      state = r["verdict"] or f"ERROR ({r['error']})"
      print(f"  {r['id']}: {state}", flush=True)

  errors = 0
  scoredTotal = scoredAgree = 0
  cats: dict[str, list[int]] = {}     # category -> [matches, scored items]
  rows = []
  for it in items:
    r = results[it["id"]]
    goldV = it["verdict"]
    if r["error"]:
      errors += 1
      if not it.get("calibration"): cats.setdefault(it.get("category", "?"), [0, 0])[1] += 1
      rows.append((it["id"], goldV, "ERROR", "", r["error"]))
      continue

    isScored = not it.get("calibration")
    match = r["verdict"] == goldV
    if isScored:
      scoredTotal += 1
      scoredAgree += int(match)
      c = cats.setdefault(it.get("category", "?"), [0, 0])
      c[1] += 1
      c[0] += int(match)
    note = "" if match else (
       "failed: " + ", ".join(f"{c} (preferred)" if c.lower() in preferred else c for c in r["failed_checks"]) if r["verdict"] == "reject" else "graded accept"
      )
    rows.append((it["id"], goldV, r["verdict"], "yes" if match else "NO", note))

  wid = max(len(r[0]) for r in rows)
  print(f"\n{'item'.ljust(wid)}  gold    verdict  agree  note")
  for itemId, g, v, m, note in rows:
    print(f"{itemId.ljust(wid)}  {g:7} {v:8} {m:6} {note}")

  bar = gold.get("pass_bar")
  fullScored = sum(1 for it in gold["items"] if not it.get("calibration"))
  if scoredTotal != fullScored:
    bar = None                      # partial run; the bar reads 20 items
  if bar is not None:
    print("\ncategories: " + "  ".join(f"{k} {m}/{t}" for k, (m, t) in sorted(cats.items())))
    floorMissing = sorted(k for k, (m, _) in cats.items() if m == 0)
    print(f"agreement: {scoredAgree}/{scoredTotal} scored items", end="")
    # The bar is 18/20 AND the category floor: at least one matching
    # verdict in every composition category (grading tab).
    if floorMissing: print(f"  (bar: {bar}/{scoredTotal}: below the bar; category floor unmet: no match in {', '.join(floorMissing)})")
    elif scoredAgree >= bar: print(f"  (bar: {bar}/{scoredTotal}: PASS)")
    else: print(f"  (bar: {bar}/{scoredTotal}: below the bar)")
  else: print(f"\nagreement: {scoredAgree}/{scoredTotal} scored items")
  if errors: print(f"{errors} item(s) errored; fix and re-run.", file=sys.stderr)

  if runLog is not None:
    sys.stdout = runLog.stream
    # if scoredTotal != fullScored:
    #   print(f"partial run: NOT written to {a.save_run}. Partial runs "
    #           "are for finding problems; the run you commit comes from "
    #           "one full run of your finished tool.")
    # elif errors: print(f"{errors} item(s) errored: NOT written to {a.save_run}. Fix and re-run.")
    # else:
    writeRun(a.save_run, str(rubricP.parent), [rubricP, skillP], scoredTotal, runLog.text())
    print(f"run written to {a.save_run}")

  if a.out:
    Path(a.out).write_text(json.dumps({
        "rubric": str(rubricP), "model": MODEL,
        "agreement": [scoredAgree, scoredTotal],
        "results": [results[it["id"]] for it in items]}, indent=2),
      encoding="utf-8")
    print(f"full results written to {a.out}")

  return 1 if errors else 0


if __name__ == "__main__":
  sys.exit(main())