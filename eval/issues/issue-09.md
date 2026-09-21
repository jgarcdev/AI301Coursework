# Eval item: issue-09

- source: conda/conda#7617
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: conda/conda (7481 stars, archived: no)
- description: A system-level, binary package and environment manager running on all major operating systems and platforms.
- last push to any branch: 2026-08-04
- latest release: 26.7.0 (2026-07-31)
- open issues + PRs: 662
- last 5 default-branch commits:
  - 2026-08-04 by codewithdaniel1: docs: add authenticated channels guide (#16483)
  - 2026-08-04 by danyeaw: Recipe: add conda-rattler-solver as a run dependency (#16491)
  - 2026-08-04 by codewithdaniel1: docs: update commands concept page (#16485)
  - 2026-08-04 by codewithdaniel1: docs: update channels concept page (#16484)
  - 2026-08-04 by danyeaw: Docs: Fix plantuml download failures by using conda-forge (#16492)
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #16275 (opened 2026-06-24 by a maintainer): 32.9 days
  - #16493 (opened 2026-08-04): no maintainer comment in thread
  - #16231 (opened 2026-06-15): no maintainer comment in thread
  - #16023 (opened 2026-05-05): no maintainer comment in thread
  - #16026 (opened 2026-05-05): no maintainer comment in thread
- contribution policy (CONTRIBUTING.md, section "Generative AI"): generative AI tools welcome; you are responsible for all contributions and must review and understand AI-generated content before including it in a pull request
- this issue: assignees: none; linked PRs: conda/conda#11627 (closed)

## Issue

### conda config clear option (#7617)

opened by jakirkham (MEMBER) on 2018-08-03, state open, labels: type::feature, source::community, good first issue, stale::recovered, duplicate::primary, backlog

Would be great to have an option for `conda config` to `clear` a list entry of all items. For example, `conda config --clear channels` would change `condarc` like so.

```yaml
...
channels: []
...
```

## Comments (4 total, first 4 shown)

### MesaJonathan (NONE) on 2022-01-20

I'd like to take a swing at this as my first open-source contribution. Does it need to be assigned to me?

### jakirkham (MEMBER) on 2022-01-20

Think you can just give it a try if you are interested. Thanks for looking into it Jonathan 😄

### github-actions[bot] (NONE) on 2023-01-21

Hi there, thank you for your contribution!

This issue has been **automatically marked as stale** because it has not had recent activity. It will be closed automatically if no further activity occurs.

If you would like this issue to remain open please:

  1. Verify that you can still reproduce the issue at hand
  2. Comment that the issue is still reproducible and include:
    - What OS and version you reproduced the issue on
    - What steps you followed to reproduce the issue

**NOTE:** If this issue was closed prematurely, please leave a comment.

Thanks!

### jakirkham (MEMBER) on 2023-01-21

(bump)
