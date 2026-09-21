# Eval item: issue-19

- source: zxcalc/zxlive#517
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: zxcalc/zxlive (101 stars, archived: no)
- description: A graphical tool for the ZX calculus
- last push to any branch: 2026-08-04
- latest release: v1.0.0 (2026-04-29)
- open issues + PRs: 64
- last 5 default-branch commits:
  - 2026-08-04 by RazinShaikh: Edge tool can draw multiple parallel edges at once (#521)
  - 2026-08-04 by RazinShaikh: Merge pull request #554 from zxcalc/fix/package-runtime-assets
  - 2026-08-04 by RazinShaikh: Fix resource packaging for release binaries
  - 2026-08-04 by RazinShaikh: Merge pull request #551 from 96-LB/magic-hopf-fix
  - 2026-08-04 by 96-LB: Update Hopf rule matching for X spiders
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #555 (opened 2026-08-04 by a maintainer): no maintainer comment in thread
  - #462 (opened 2026-03-03 by a maintainer): 25.8 days
  - #507 (opened 2026-05-01): 0.4 days
  - #513 (opened 2026-05-04 by a maintainer): 92.1 days
  - #512 (opened 2026-05-04 by a maintainer): no maintainer comment in thread
- contribution policy (CONTRIBUTING.md): no statement on AI or contribution tooling
- this issue: assignees: none; linked PRs: none

## Issue

### Selecting large subgraphs in proof mode freezes the UI (#517)

opened by RazinShaikh (COLLABORATOR) on 2026-05-08, state open, labels: Type: bug, Category: Proof mode, Priority: High

There are two potential causes which should be fixed:
1. The matchers are slow for certain rewrites (quadratic instead of linear)
2. UI update is waiting for the matching thread to finish

Additional suggestions:
1. We should use multi-processing to use all the cores to match rewrites in parallel
2. Only match rewrites in the categories that are not collapsed. If the category is expanded, we should run matchers for those rewrites
3. Applying the rewrite should also happen in a separate thread

## Comments (0 total, first 0 shown)

(no comments)
