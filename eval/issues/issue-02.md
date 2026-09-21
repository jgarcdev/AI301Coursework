# Eval item: issue-02

- source: rupa/z#349
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: rupa/z (17036 stars, archived: no)
- description: z - jump around
- last push to any branch: 2024-06-19
- latest release: v1.12 (2023-12-09)
- open issues + PRs: 107
- last 5 default-branch commits:
  - 2023-12-09 by jedahan: Escape calls for sed and awk in case someone aliased them (#264)
  - 2023-12-09 by rupa: avoid issues when `date` has been aliased
  - 2023-12-09 by rupa: avoid issues when `env` has been aliased
  - 2021-05-31 by queensferryme: Skip excluding when `$_Z_EXCLUDE_DIRS` is empty (#302)
  - 2021-05-26 by ericbn: Also don't match the root directory (#216)
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #351 (opened 2026-05-28): no maintainer comment in thread
  - #347 (opened 2026-01-09): no maintainer comment in thread
  - #345 (opened 2025-06-26): no maintainer comment in thread
  - #331 (opened 2024-04-06): no maintainer comment in thread
  - #292 (opened 2020-08-24): no maintainer comment in thread
- contribution policy: no CONTRIBUTING.md in the repo; no stated policy
- this issue: assignees: none; linked PRs: none

## Issue

### z -x does not work correctly on macOS because of BSD sed -i syntax (#349)

opened by sermelipharo (NONE) on 2026-03-11, state open, labels: none

On macOS, `z -x` does not correctly remove the current directory from the data file.

The implementation currently uses:

```sh
sed -i -e "\:^${PWD}|.*:d" "$datafile"
```

This works with GNU `sed`, but fails on macOS because BSD `sed` requires an explicit backup suffix argument for `-i`, even if it is empty:

```sh
sed -i '' -e "\:^${PWD}|.*:d" "$datafile"
```

## Reproduction

Given a `.z` entry like:

```text
/Users/me/project|16|1773233408
```

and with the current directory set to:

```sh
/Users/me/project
```

running:

```sh
z -x
```

does not properly remove the entry on macOS.

## Expected behavior

`z -x` should remove the current directory from the data file on macOS as well as on GNU/Linux.

## Possible fix

Replace:

```sh
sed -i -e "\:^${PWD}|.*:d" "$datafile"
```

with something portable, or detect BSD `sed` and use:

```sh
sed -i '' -e "\:^${PWD}|.*:d" "$datafile"
```

## Additional note

In the current implementation, `z -x` also continues execution and prints the list afterward.
It may be worth clarifying whether that is intended behavior or whether `-x` should return immediately after deletion.

## Comments (2 total, first 2 shown)

### Mopf-gg (NONE) on 2026-03-11

您的邮件已收到。谢谢！

### jghub (NONE) on 2026-06-07

hi, in case you care: my fork of z.sh,  `https://github.com/jghub/ze`, fixes the sed -i issue (including the erroneous drop-through to pattern matching you mention: z -x really should return immediately I agree), but its actual purpose is to
a) improve/alter the frecency algorithm
b) make z only track/score cd navigation
(see also `https://github.com/rupa/z/issues/351`)

the fork seems functional, uses different default naming conventions (z → ze everywhere), different db, and might be used in parallel to legacy z.sh for testing/comparison (the README has a db migration recipe, too). I would hope the two mentioned changes (monitor/track only cd actions and switch from legacy scoring approach to proper exponential moving average scoring) make behaviour overall preferable.
