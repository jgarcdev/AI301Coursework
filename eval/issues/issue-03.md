# Eval item: issue-03

- source: pylint-dev/pylint#9143
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: pylint-dev/pylint (5709 stars, archived: no)
- description: It's not just a linter that annoys you!
- last push to any branch: 2026-08-03
- latest release: v4.0.6 (2026-06-14)
- open issues + PRs: 1078
- last 5 default-branch commits:
  - 2026-08-03 by pre-commit-ci[bot]: [pre-commit.ci] pre-commit autoupdate (#11227)
  - 2026-08-03 by Pierre-Sassoulas: Fix a crash on calls unpacking dicts with non-string keys
  - 2026-08-03 by Pierre-Sassoulas: Ignore primer pragma noise caused by a new message id (#11221)
  - 2026-08-02 by Guflly: Detect repeated attribute chains in comparison-with-itself (#11195)
  - 2026-08-02 by davidpavlovschi: Don't emit useless-parent-delegation for uninspectable C-level parents
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #11229 (opened 2026-08-04): no maintainer comment in thread
  - #11228 (opened 2026-08-04): no maintainer comment in thread
  - #11222 (opened 2026-08-03): no maintainer comment in thread
  - #11175 (opened 2026-07-16): no maintainer comment in thread
  - #11101 (opened 2026-06-11): no maintainer comment in thread
- contribution policy (.github/CONTRIBUTING.md): no statement on AI or contribution tooling; the repo ships AGENTS.md instructions for AI coding agents
- this issue: assignees: none; linked PRs: pylint-dev/pylint#10985 (open); pylint-dev/pylint#10987 (closed); pylint-dev/pylint#11001 (closed); pylint-dev/pylint#11003 (merged); quick123-666/pylint#1 (open); pylint-dev/pylint#11008 (closed)

## Issue

### Add pylint-junit reporter class (#9143)

opened by MarcSkovMadsen (NONE) on 2023-10-12, state open, labels: Enhancement ✨, Help wanted 🙏, Good first issue, Hacktoberfest, Needs PR

### Current problem

I'm a user of pylint. I used to use pylint2junit. I found out it has not been working since pylint 2.15. I then found pylint-junit which seems to fix some issues in pylint2junit. But it also have had issues since pylint 2.15. pylint2junit does not seem maintained. pylint-junit seems more active.

I would really like to continue to use pylint and I need junit reporting for my (Azure DevOps) pipelines.

### Desired solution

Add `pylint-junit` reporter class to `pylint` to make the junit support more robust.

### Additional context

Proposed by @Pierre-Sassoulas in `https://github.com/pylint-dev/pylint/issues/8368#issuecomment-1759674966`

## Comments (2 total, first 2 shown)

### quick123-666 (NONE) on 2026-05-11

Working on this. The plan is to add a `PytestJUnitReporter` class following the existing reporter interface.

For reference, `pylint-junit` (`https://github.com/pylint-dev/pylint-junit`) already implements this and can serve as a reference for the XML structure.

### DanielNoord (COLLABORATOR) on 2026-05-11

@hamza-mobeen Can you comment in this issue so I can assign it to you?

We are **not** looking for any other contributions other than @hamza-mobeen's PR: `https://github.com/pylint-dev/pylint/pull/10985`
