# Eval item: issue-18

- source: excalidraw/excalidraw#9656
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
- this issue: assignees: none; linked PRs: excalidraw/excalidraw#9685 (open); excalidraw/excalidraw#10371 (open); excalidraw/excalidraw#11021 (closed); excalidraw/excalidraw#11460 (closed); excalidraw/excalidraw#11656 (open); LennyMalcolm0/excalidraw#314 (open)

## Issue

### Allow to switch into different arrow types when using "Tab" switcher when bound to element/s or text (#9656)

opened by zsviczian (COLLABORATOR) on 2025-06-15, state open, labels: enhancement, good first issue

Is it by design that if either ends of an arrow are bound to an element the "TAB" shape switcher does not work?

## Comments (11 total, first 11 shown)

### Mrazator (MEMBER) on 2025-06-15

It is, when talking about line <-> arrow, but it might change in the future.

The issue is that currently, a line is not bindable to other shapes, so switching into a line would unbind the arrow from other shapes, which would be unexpected in most cases.

Similarly, we don't allow switching to line when arrows have a label.

---

Switching between different arrow types (sharp / curved / angled) should still be possible, unclear why it wasn't added.

### zsviczian (COLLABORATOR) on 2025-06-15

yeah, the line I can understand. I was trying to switch between arrow types, which is possible on the element properties panel. Maybe we could not show the line option if the arrow is bound to an element.

### dwelle (MEMBER) on 2025-06-16

Yep, let's do this (not showing the line option).

### pran01 (NONE) on 2025-06-18

Hey, is anyone working on this, or can i pick this up?

### diljitsgit (NONE) on 2025-06-21

Hey! Sorry for not alerting before working on the issue. This is my first open-source contribution so i just kind of solved it while understanding the codebase. Please tell me if i am doing anything wrong or can improve in any way 😅.

I created the pull request: `https://github.com/excalidraw/excalidraw/pull/9685#issue-3165391309`

And here is a video of the working:

`https://github.com/user-attachments/assets/5a9ce401-1d73-4a01-9f92-233b54bbe470`

### levi42x (NONE) on 2025-08-11

“Hi, I’m interested in working on this issue. Is it still open for contribution?”
or is it solved ?

### vercetti322 (NONE) on 2025-10-08

Hi @dwelle, is this issue still open for contribution?

### magic-peach (NONE) on 2025-10-14

Hey, I’m participating in Hacktoberfest and im new to open source! Can I work on this issue?

### Gotnochill (NONE) on 2025-10-20

Greetings!
Would like to work on this, is this open?

### Abhishek-Jatav (NONE) on 2026-07-06

"I'd like to work on this, could I get it assigned to me?"

### vishnukumar650 (NONE) on 2026-08-02

Hi @excalidraw team! I'd like to take up this issue to enable switching between arrow types using the Tab switcher when bound to elements (excluding the line option).
