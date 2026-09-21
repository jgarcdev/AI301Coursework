# Eval item: calib-03

- source: httpie/cli#1898
- captured: 2026-08-05
- calibration: true

## Repo facts (captured 2026-08-05)

- repo: httpie/cli (38381 stars, archived: no)
- description: 🥧 HTTPie CLI  — modern, user-friendly command-line HTTP client for the API era. JSON support, colors, sessions, downloads, plugins & more.
- last push to any branch: 2024-12-17
- latest release: 3.2.4 (2024-11-01)
- open issues + PRs: 323
- last 5 default-branch commits:
  - 2024-12-17 by keysmashes: Fix `https` behaviour in fish (#1611)
  - 2024-11-01 by github-actions[bot]: [automated] Update generated content (#1607)
  - 2024-11-01 by jkbrzt: 3.2.4
  - 2024-11-01 by jkbrzt: Update test.yml
  - 2024-11-01 by jkbrzt: Fix/refactor default cert loading
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #1478 (opened 2023-02-09): no maintainer comment in thread
- contribution policy (CONTRIBUTING.md): no statement on AI or contribution tooling
- this issue: assignees: none; linked PRs: httpie/cli#1900 (open); httpie/cli#1903 (open); httpie/cli#1908 (open); httpie/cli#1911 (open); httpie/cli#1916 (open)

## Issue

### Bug: Windows guard in is_available() compares os.system (a function) to 'nt' — always False (#1898)

opened by truongsontung (NONE) on 2026-07-13, state open, labels: none

## Description

In `httpie/output/ui/man_pages.py`, `is_available()` tries to short-circuit on Windows but the check is broken:

`https://github.com/httpie/cli/blob/master/httpie/output/ui/man_pages.py#L21`

```python
def is_available(program: str) -> bool:
    if NO_MAN_PAGES or os.system == 'nt':
        return False
    ...
```

`os.system` is a **built-in function object**, so `os.system == 'nt'` is always `False`. The intended Windows guard never fires. The author almost certainly meant `os.name == 'nt'`.

## Why it is wrong

- `os.system` is `<built-in function system>`; comparing a callable to the string `'nt'` is always `False`.
- The correct, idiomatic Windows check is `os.name == 'nt'` (or `sys.platform == 'win32'`).

## Impact

On Windows the `if NO_MAN_PAGES or os.system == 'nt':` branch is dead code. The function does not short-circuit; instead it falls through to `subprocess.run(['man', '1', program])`. On a typical Windows install `man` is absent, so `FileNotFoundError` is raised and swallowed by the `except Exception: return False`, yielding the same observable result — but only by accident. If a `man` executable happens to be on `PATH` (e.g. Git Bash / WSL), HTTPie will attempt to render man pages on Windows, contrary to the intent of the guard. Also, relying on a swallowed exception for control flow is fragile.

## Reproduction / verification

```python
import os
print(os.system == 'nt')   # -> False (regardless of platform)
print(os.name == 'nt')     # -> True on Windows, 'posix' elsewhere
```

## Suggested fix

```python
import sys
...
def is_available(program: str) -> bool:
    if NO_MAN_PAGES or sys.platform == 'win32':
        return False
    ...
```

(Using `sys.platform == 'win32'` is the most robust Windows detector.)

## Affected version

Current `master` (verified via `git clone --depth 1`).

## Comments (1 total, first 1 shown)

### truongsontung (NONE) on 2026-07-14

Follow-up: confirmed the bug — `os.system` is a built-in function object, so `os.system == 'nt'` is always `False` and the Windows short-circuit never fires (the function instead relies on a swallowed `FileNotFoundError` to return `False` by accident).

The intended guard should be a real platform check, e.g.:

```python
import sys
...
def is_available(program: str) -> bool:
    if NO_MAN_PAGES or sys.platform == 'win32':
        return False
    ...
```

(`sys.platform == 'win32'` is the most robust Windows detector; `os.name == 'nt'` works too.)

Happy to open a PR that (1) swaps the guard for `sys.platform == 'win32'` and (2) adds a regression test asserting `is_available() == (sys.platform == 'win32')` so this can't silently regress again. Just let me know if you'd like me to send it.
