# Rubric: is this a good first issue?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever checks
you define here. It ships empty on purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where. Name the source
     (repo-facts block, issue body, comment thread, or the locations in
     references/evidence-guide.md). "The repo" is not a source; "the last
     5 default-branch commit dates" is.
   - Pass condition: a condition someone else could apply and get your
     answer. Prefer thresholds with numbers ("a maintainer commented
     within 30 days") over adjectives ("maintainer is responsive").
   - Weight: `required` (a fail here rejects the issue) or `preferred`
     (never changes the verdict; a nice-to-have that helps rank the
     issues you accept).

2. A verdict rule below the table: how the check grades combine into
   accept or reject, including how `unclear` is treated. The verdict
   space is binary. If you write no rule for `unclear`, the skill treats
   it as fail.

Cover what actually kills first contributions. The lecture named four
families: the maintainer is alive, the repo is in use, the scope fits a
newcomer, and nobody else is already on it. A rubric that ignores a family
will fail eval issues designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Maintainer activity | The "last 5 default-branch commits," "maintainer first-response sample," and issue Comments section in the repo-facts block (eval mode), or the corresponding GitHub commit history and issue comments (live mode) | At least one is true: a human maintainer authored one of the last 5 default-branch commits; the first-response sample contains a maintainer response within 30 days of an issue being opened; or a maintainer commented on this issue within 90 days before capture/current date | required |
| Repository in use | The `archived:` status, "last push to any branch," "latest release," and star count on the repo line or under Repo facts | The repository is not archived, and at least one is true: the last push to any branch was within 180 days; the latest release was within 365 days; or the repository has at least 100 stars | required |
| Newcomer-sized scope | The issue body, issue labels, and full Comments section | The request is one bounded contribution, not a support question or umbrella/tracking issue; the thread has no unresolved design debate; and neither the issue nor a maintainer says that the work requires changes to core internals. A `good first issue` label may support this judgment but does not replace reading the body and thread | required |
| Available to claim | The `this issue: assignees:` and `linked PRs:` entries under Repo facts, plus every comment and label-event line | There is no assignee, no open linked PR, and no explicit active claim in the comments. An unanswered claim within the last 30 days, or a comment saying the claimant is still working, counts as active; a closed unmerged PR is not by itself active | required |
| Contribution policy permits the workflow | The "contribution policy" line under Repo facts, including linked contributor documents, dedicated AI policy files, and PR-template requirements | The policy is silent or permits AI-assisted contributions under conditions such as disclosure, testing, or human review. It fails when it explicitly bans AI-generated or AI-assisted contributions | required |
| Maintainer guidance on this issue | The issue Comments section, including each comment's `author_association` and date | A maintainer has given a concrete clarification, acceptance criterion, reproduction request, or confirmation that the issue is suitable for contribution; otherwise grade `unclear` | preferred |
| Clear acceptance signal | The issue body and label-event lines in the issue snapshot or live issue | The issue has a `good first issue`/`help wanted` label or the body states at least one concrete expected behavior or acceptance criterion; otherwise grade `unclear` | preferred |

## Verdict rule

<!-- State how the grades above combine into accept or reject, and how
unclear is treated. Example shape (write your own): "accept if every
required check passes; preferred checks never change the verdict, they
rank accepted issues; unclear counts as fail." -->
Accept only when every required check passes. Preferred checks never change
the verdict and are used only to rank issues that are accepted. For required
checks, `unclear` counts as fail; for preferred checks, `unclear` is reported
but does not affect the verdict.
