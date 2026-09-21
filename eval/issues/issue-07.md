# Eval item: issue-07

- source: wting/autojump#727
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: wting/autojump (16956 stars, archived: no)
- description: A cd command that learns - easily navigate directories from the command line
- last push to any branch: 2025-02-27
- latest release: none published
- open issues + PRs: 231
- last 5 default-branch commits:
  - 2023-02-01 by Komi7: fix git clone url
  - 2025-02-10 by soerenwolfers: Update README.md
  - 2025-02-10 by soerenwolfers: Update README.md
  - 2025-02-10 by soerenwolfers: Update README.md
  - 2023-08-22 by wting: Merge branch 'wting_default_python3'
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #569 (opened 2019-04-14): no maintainer comment in thread
  - #734 (opened 2026-05-29): no maintainer comment in thread
  - #593 (opened 2019-11-22): no maintainer comment in thread
  - #732 (opened 2026-04-30): no maintainer comment in thread
  - #689 (opened 2023-12-09): no maintainer comment in thread
- contribution policy: no CONTRIBUTING.md in the repo; no stated policy
- this issue: assignees: none; linked PRs: none

## Issue

### Attempting to jump into a directory whose name has underscores triggers an AttributeError (#727)

opened by jpcofr (NONE) on 2026-02-28, state open, labels: none

When attempting to use j to jump to a directory containing multiple underscores (e.g., 000_play__), autojump fails with a Python AttributeError instead of gracefully handling the search or providing a "directory not found" message.

It appears the get_ith_path lambda assumes that last(take(i, iterable)) will always return a valid object, but in this case, it returns None, causing the crash when accessing the .path attribute.

## Steps to Reproduce
Create a directory with multiple underscores: mkdir -p ~/tmp/000_play__

Change into that directory to add it to the autojump database: cd ~/tmp/000_play__

Return to the home directory: cd ~

Attempt to jump using the underscore pattern: j 000_play__


## Actual Behavior / Stack Trace
The command crashes with the following output:

```bash
[~]$ j 000_play__
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/autojump/22.5.3_3/libexec/bin/autojump", line 342, in <module>
    sys.exit(main(parse_arguments()))
             ~~~~^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/autojump/22.5.3_3/libexec/bin/autojump", line 326, in main
    get_ith_path(
    ~~~~~~~~~~~~^
        tab_index,
        ^^^^^^^^^^
        find_matches(entries, [tab_needle]),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^
  File "/opt/homebrew/Cellar/autojump/22.5.3_3/libexec/bin/autojump", line 324, in <lambda>
    get_ith_path = lambda i, iterable: last(take(i, iterable)).path
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'path'
autojump: directory '000_play__' not found
```

This appears to be the same root cause as reported in #669, but specifically triggered by directory names containing underscores during jump attempts.

## Comments (0 total, first 0 shown)

(no comments)
