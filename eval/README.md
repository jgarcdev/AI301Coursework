# Eval set and harness

20 scored issue bundles, 4 unscored calibration bundles from the class
activity, instructor gold labels, and a runnable harness that grades any
rubric against the set.

## The one command

From this directory, with the Claude Code CLI installed (you have it if
you have been building skills):

    python3 run-eval.py --rubric path/to/your-rubric.md

Point `--rubric` at your filled rubric. The shipped template
(`../skill/rubric.md`) is empty on purpose, and the skill
refuses to grade with an empty rubric, so write your checks and verdict
rule first.

Useful flags: `--limit 3` for a quick smoke run, `--only
issue-07,issue-12` to re-grade just the named issues, `--workers N` to
change parallelism (default 5), `--include-calibration` to also grade
the four worksheet issues (they are never scored), `--out results.json`
to keep the full per-check results.

`--only` is the flag for the revise loop: when a full run disagrees on
two issues, re-run only those two while you adjust your rubric (about
$0.20 per issue instead of about $4 for a full run), then confirm with
one full run at the end. Partial runs never print a bar verdict; only a
full 20-issue run can pass.

Every run grades with Sonnet, the course's standard model; there is no
model flag. This keeps every student's run (and the instructor stability
runs that set the bar) on the same grader, and Sonnet is the model your
course credit is budgeted for.

## Saving the run you commit

Add `--save-run eval-run.txt` to your confirming full run and the harness
writes the file for you:

    python3 run-eval.py --rubric path/to/your-rubric.md --save-run eval-run.txt

The file holds the same text you watched on screen, written as UTF-8 on
every platform, under a short header the harness fills in: the pinned
model, the tool it graded, and a fingerprint of each file that went into
the run. That file is what you upload to your course repo.

Partial runs refuse to write it. A `--limit` or `--only` run says so and
leaves the file untouched, so a cheap re-run can never overwrite the full
run you already saved.

Do not hand-edit the file. Where you account for the runs it took to get
there is your write-up in the phase file, not the transcript.

## What the output means

One line per issue while grading, then a table:

    item      gold    verdict  agree  note
    issue-01  accept  accept   yes
    issue-07  reject  accept   NO     graded accept
    ...
    categories: claimed 4/4  clear-accept 8/8  dead-repo 3/3  policy 0/1  scope 4/4
    agreement: 19/20 scored items  (bar: 18/20: below the bar; category floor unmet: no match in policy)

- `gold` is the instructor label from `gold-labels.json`.
- `verdict` is what the skill decided with YOUR rubric.
- The `note` column names the checks your rubric failed the issue on,
  which is where to look when you disagree with a gold label. Names
  tagged `(preferred)` cannot have caused the reject (preferred checks
  never change a verdict); the untagged names are the required
  failures to investigate.
- The `categories` line tallies matches per eval-set composition
  category. Passing needs at least one match in every category (the
  category floor): a rubric that cannot see a whole category, however
  well it does elsewhere, is missing a check the set was built to
  force.
- The agreement line is the score the grading bar reads. The bar:
  agreement of 18 of 20 or better passes (exactly 18 passes), AND the
  category floor holds. The 4 calibration issues are never scored.
  Full bar details, including the human read of your rubric: the
  course portal's Check-In page (`ai301/projects/project_1.md` in this
  repo).

Disagreements are the feedback loop: open the bundle the table names,
reread the evidence, and decide whether your check's threshold or your
check list is what needs to move. Then re-run; retries are unlimited.

## What is in a bundle

Each `issues/*.md` file is self-contained: the issue text, its comment
thread, and a repo-facts block (release recency, commit activity,
maintainer response sample, assignee and linked-PR state, and the
repo's stated contribution policy), all captured on the date stamped
at the top (the contribution-policy lines across all bundles were
verified 2026-08-12). The harness never touches GitHub; the
skill grades the bundle text, so every run sees the same world and your
score cannot drift because a repo woke up.

Every bundle also has a `.json` twin with the same frozen content in
structured form (issue, comments, repo facts as fields). Read whichever
you prefer; they are the same snapshot. `issues_to_json.py` regenerates
the JSON from the markdown.

## Do not grade the live issue

The `source:` line in each bundle names the real issue
(`owner/repo#number`). It is deliberately not a link: the real issue
has kept moving since the capture date, with new comments, new linked
PRs, sometimes a fix already merged. That is exactly why the snapshots
exist. The gold labels describe the snapshot, not today's GitHub. When
the live page and the bundle disagree, the bundle wins.

## Format note

This markdown-plus-manifest layout is the browsable form of the eval-set
format used in production model evals: one record per item with input,
gold label, and metadata (usually JSONL), a judge prompt (here, the
skill plus your rubric), and a scoring script (here, `run_eval.py`).
If you later meet an eval framework at work, you already know the parts.
