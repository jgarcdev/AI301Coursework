# Eval item: calib-02

- source: kubernetes/minikube#23436
- captured: 2026-08-05
- calibration: true

## Repo facts (captured 2026-08-05)

- repo: kubernetes/minikube (32013 stars, archived: no)
- description: Run Kubernetes locally
- last push to any branch: 2026-08-03
- latest release: v1.38.1 (2026-02-19)
- open issues + PRs: 536
- last 5 default-branch commits:
  - 2026-08-03 by kubernetes-prow[bot]: Merge pull request #23409 from a4abdul7/docs-wsl2-access
  - 2026-08-02 by kubernetes-prow[bot]: Merge pull request #23424 from minikube-bot/yearly-leaderboard-fba9401
  - 2026-08-02 by minikube-bot: Update yearly leaderboard
  - 2026-08-01 by kubernetes-prow[bot]: Merge pull request #23408 from minikube-bot/auto_bump_nerdctl_version-09462d6
  - 2026-08-01 by kubernetes-prow[bot]: Merge pull request #23381 from minikube-bot/gendocs
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #23441 (opened 2026-08-04 by a maintainer): no maintainer comment in thread
  - #23442 (opened 2026-08-04 by a maintainer): no maintainer comment in thread
  - #23385 (opened 2026-07-19 by a maintainer): 0.0 days
  - #11409 (opened 2021-05-14 by a maintainer): 124.2 days
  - #23437 (opened 2026-08-04 by a maintainer): no maintainer comment in thread
- contribution policy (CONTRIBUTING.md): no statement on AI or contribution tooling
- this issue: assignees: amh1k; linked PRs: kubernetes/minikube#23440 (open)

## Issue

### nerdctl-bin x86_64 package references wrong version variable (#23436)

opened by nirs (COLLABORATOR) on 2026-08-04, state open, labels: good first issue

## Bug

In `deploy/iso/minikube-iso/arch/x86_64/package/nerdctl-bin/nerdctl-bin.mk`, the `NERDCTL_BIN_SOURCE` line references `NERDCTL_BIN_AARCH64_VERSION` instead of `NERDCTL_BIN_VERSION`:

```makefile
NERDCTL_BIN_VERSION = 2.3.5
...
NERDCTL_BIN_SOURCE = nerdctl-$(NERDCTL_BIN_AARCH64_VERSION)-linux-amd64.tar.gz
```

It should be:

```makefile
NERDCTL_BIN_SOURCE = nerdctl-$(NERDCTL_BIN_VERSION)-linux-amd64.tar.gz
```

## Impact

This currently works by accident because both architectures use the same nerdctl version, so `NERDCTL_BIN_AARCH64_VERSION` resolves correctly when both packages are configured. It would break if the versions ever diverged or if the x86_64 package were built in isolation.

## Fix

Change line 10 of `deploy/iso/minikube-iso/arch/x86_64/package/nerdctl-bin/nerdctl-bin.mk` from:

```makefile
NERDCTL_BIN_SOURCE = nerdctl-$(NERDCTL_BIN_AARCH64_VERSION)-linux-amd64.tar.gz
```

to:

```makefile
NERDCTL_BIN_SOURCE = nerdctl-$(NERDCTL_BIN_VERSION)-linux-amd64.tar.gz
```

## Comments (1 total, first 1 shown)

### amh1k (NONE) on 2026-08-04

/assign
