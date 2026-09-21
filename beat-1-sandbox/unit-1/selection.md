# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

Record of the issue carried into Unit 2, and of the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in
the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the
wrong label is not graded.

---

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/73

**Verdict output**

**The verdict must record `accept` for this issue.** Choose an issue your own skill
accepts. If your skill rejects every candidate you try, that is a signal about your
rubric rather than about the issues: revise it and re-run — retries are unlimited and a
partial re-run costs about $0.20 — or run the skill on different candidates. Output
recording `reject` for the issue you chose earns no credit for this field.

```
{
   "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/73",
   "checks": [
   {"name": "Maintainer activity", "grade": "pass", "evidence": "Human maintainer Aburke225 (COLLABORATOR) authored all of the last 5 main commits, most recent 2026-09-16, 5 days before today"},
   {"name": "Repository in use", "grade": "pass", "evidence": "archived=false and last push to any branch 2026-09-16, within 180 days"},
   {"name": "Newcomer-sized scope", "grade": "pass", "evidence": "One bounded fix — 'Make the two files agree' across README.md and .env.example, 1-2 hours, no comment thread and no core-internals statement"},
   {"name": "Available to claim", "grade": "pass", "evidence": "assignees: none; no linked or cross-referenced PRs in the timeline; 0 comments, so no claim of any kind"},
   {"name": "Contribution policy permits the workflow", "grade": "pass", "evidence": "docs/CONTRIBUTING.md sets CI/test/commit conditions and is silent on AI; no AI_POLICY.md or AI_USAGE_POLICY.md in the repo"},
   {"name": "Maintainer guidance on this issue", "grade": "unclear", "evidence": "COMMENTS_COUNT: 0 — no maintainer clarification or acceptance criterion in the thread"},
   {"name": "Clear acceptance signal", "grade": "pass", "evidence": "Labeled 'good first issue' by Aburke225 on 2026-09-16, alongside bug/docs/tier-1"}
   ],
   "verdict": "accept"
}
```

---

## Eval iterations

Quote source text directly in each field below. Paraphrase does not satisfy them.

**Run history**

Run 0: agreement: 10/13 scored items

**Issue analysis**

```
item      gold    verdict  agree  note
issue-01  accept  reject   NO     failed: Newcomer-sized scope, Maintainer guidance on this issue (preferred)
```

**Check rationale**

> "Newcomer-sized scope | The issue body, issue labels, and full Comments section | The request is one bounded contribution, not a support question or umbrella/tracking issue; the thread has no unresolved design debate; and neither the issue nor a maintainer says that the work requires changes to core internals. A `good first issue` label may support this judgment but does not replace reading the body and thread | required"

This check is written to reject the kinds of issues that look easy but turn into a multi-hour design discussion or a core-internals patch. For a first contribution, the main risk is not coding skill; it is scope drift. The rule therefore insists that the issue be a single bounded task, that the thread not still be debating the design, and that the fix not require parser/engine/core changes. That matches issue #73. It is a small documentation/config-sync fix between `README.md` and `.env.example`, and the issue text makes the change concrete enough that the work is bounded without extra maintainer direction.

**Trade-offs**

This check is intentionally conservative: it will reject a small-looking issue if the thread is still debating the design or if the maintainer hints the fix touches core internals, even when the issue would be manageable in a larger project. I accepted that trade-off because it is a better fit for a first contribution than a permissive rule. In a canary re-run, an issue with a "good first issue" label but an unresolved design debate would fail this gate even if the patch itself looked small, because the rubric explicitly requires a bounded, settled scope.

---

## Selection rationale

Graded on whether all three are answered, in your own words. Not on how good the
reasoning is, and not on length — a short honest answer to each earns the full marks.
This is also the basis for the claim comment you write in Unit 2.

**Selection rationale**

1. This issue fits my interests and time available because it is a narrow, concrete documentation/config consistency fix rather than a feature or architecture task. It is small enough to finish in a short session and still gives a realistic contribution workflow without swallowing a lot of context.
2. The verdict correctly identified the issue as a bounded, low-risk first contribution: there are no comments, no assignee, no open linked PR, and the task is just to make two files agree. I also weighed that the issue was labeled `good first issue`, which matters as a positive signal even though the rubric does not let labels replace the body-and-thread check.
3. The claim difficulty is low: there is no assignee, no existing PR, and no visible activity in the thread, so it is easy to claim without competing with another contributor. The only caution is that the maintainer guidance is absent, so I would still make the fix and mention the expected documentation/config alignment clearly in the PR.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/issue-select/`.
