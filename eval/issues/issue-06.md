# Eval item: issue-06

- source: Itqan-community/quran-apps-directory#298
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: Itqan-community/quran-apps-directory (37 stars, archived: no)
- description: 
- last push to any branch: 2026-07-31
- latest release: none published
- open issues + PRs: 14
- last 5 default-branch commits:
  - 2026-07-14 by abubakr-itqan: Merge pull request #291 from Itqan-community/feature/staging-to-main-submit-app-button-fix
  - 2026-07-14 by abubakr-itqan: Merge pull request #290 from Itqan-community/feat/submit-app-disabled-button-style
  - 2026-07-14 by abubakr-itqan: Submit App Button - Clarify disabled state styling
  - 2026-07-13 by abubakr-itqan: Merge pull request #289 from Itqan-community/feature/app-submissions-simplification
  - 2026-07-13 by abubakr-itqan: chore: trigger fresh CI checks for compliant branch name
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #297 (opened 2026-08-05 by a maintainer): no maintainer comment in thread
  - #296 (opened 2026-08-05 by a maintainer): no maintainer comment in thread
  - #295 (opened 2026-08-05 by a maintainer): no maintainer comment in thread
  - #294 (opened 2026-08-05 by a maintainer): no maintainer comment in thread
  - #235 (opened 2026-02-25 by a maintainer): 0.0 days
- contribution policy (CONTRIBUTING.md): no statement on AI or contribution tooling
- this issue: assignees: none; linked PRs: none

## Issue

### QAD: Make 'Submit App' visible on desktop + functional on mobile menu (#298)

opened by Amr-Bendary (COLLABORATOR) on 2026-08-05, state open, labels: bug, good first issue, help wanted, easy, high-priority

**Description**

As a desktop user, I want to see a visible 'Submit App' button on the navbar (and as a mobile user, have a functional action in the drawer) so that I can submit a new app for inclusion.

**Problem**

The 'Submit App' button is hidden on desktop viewports and fails to open the submission flow on mobile viewports.

**Acceptance Criteria**

- [ ] 'Submit App' button is visible on desktop viewports in the navbar header.
- [ ] Accessible in the mobile drawer menu and triggers submission modal/route.
- [ ] Works in both Arabic (RTL) and English (LTR).

**Where to start**

- Look at `src/app/components/header/` and `src/app/components/mobile-menu/`.

## Comments (0 total, first 0 shown)

(no comments)
