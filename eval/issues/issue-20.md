# Eval item: issue-20

- source: excalidraw/excalidraw#11811
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: excalidraw/excalidraw (128988 stars, archived: no)
- description: Virtual whiteboard for sketching hand-drawn like diagrams
- last push to any branch: 2026-08-04
- latest release: v0.18.1 (2026-04-21)
- open issues + PRs: 3289
- last 5 default-branch commits:
  - 2026-08-04 by dwelle: feat(packages/excalidraw): ViewportStatusFrame & factor out user-follow state (#11819)
  - 2026-08-04 by yanrin13: fix(editor): initialize selectedLinearElement after pasting arrows (#11803)
  - 2026-08-04 by dwelle: fix(editor): normalize container + bound text order on restore (#11827)
  - 2026-08-04 by dwelle: fix(editor): include custom tools in pointer capture (#11826)
  - 2026-08-04 by nihaarsirikonda: fix(editor): prevent crash when editing arrow with bound text (#11814)
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #6669 (opened 2023-06-12): no maintainer comment in thread
  - #11817 (opened 2026-08-04): 0.6 days
  - #11770 (opened 2026-07-27): no maintainer comment in thread
  - #4656 (opened 2022-01-28): 0.1 days
  - #11825 (opened 2026-08-04): no maintainer comment in thread
- contribution policy (CONTRIBUTING.md): no statement on AI or contribution tooling
- this issue: assignees: none; linked PRs: none

## Issue

### Add company logo shape to the toolbar (#11811)

opened by cursor[bot] (NONE) on 2026-08-02, state open, labels: none

**Before submitting**

- [x] Have you checked for any open similar issues (`https://github.com/excalidraw/excalidraw/issues`)?
- [ ] Have you checked our roadmap (`https://github.com/orgs/excalidraw/projects/3`) for similar planned features?

**Is your feature request related to a problem? Please describe.**
There’s no quick way to drop our company logo onto a canvas as a first-class shape. Today you have to import an image each time, which is slow and easy to get inconsistent.

**Describe the solution you'd like.**
Add a new toolbar shape that inserts a fixed company logo (SVG/image). Users should be able to place, resize, and move it like other elements, and it should export correctly.

Success looks like: logo tool in the shapes toolbar → place/resize/move like other elements → correct export.

**Describe alternatives you've considered.**
None identified yet (beyond manually inserting an image each time).

**Additional context.**
Out of scope for v1: custom logo upload / branding settings.
Likely surface: `packages/excalidraw` editor (toolbar + element), possibly app wiring in `excalidraw-app` if needed.
Logo asset TBD.

## Comments (0 total, first 0 shown)

(no comments)
