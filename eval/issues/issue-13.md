# Eval item: issue-13

- source: kubernetes/minikube#23437
- captured: 2026-08-05
- calibration: false

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
  - #23436 (opened 2026-08-04 by a maintainer): no maintainer comment in thread
- contribution policy (CONTRIBUTING.md): no statement on AI or contribution tooling
- this issue: assignees: none; linked PRs: kubernetes/minikube#23438 (open); kubernetes/minikube#23439 (open)

## Issue

### nerdctl-bin package files use spaces instead of tabs (#23437)

opened by nirs (COLLABORATOR) on 2026-08-04, state open, labels: good first issue

## Bug

The nerdctl-bin Buildroot package files use spaces for indentation where tabs are required by Buildroot/Kconfig/Make conventions.

**Affected files:**
- `deploy/iso/minikube-iso/arch/aarch64/package/nerdctl-bin-aarch64/Config.in` — spaces instead of tabs
- `deploy/iso/minikube-iso/arch/x86_64/package/nerdctl-bin/Config.in` — spaces instead of tabs
- `deploy/iso/minikube-iso/arch/aarch64/package/nerdctl-bin-aarch64/nerdctl-bin.mk` — spaces instead of tabs in `INSTALL_TARGET_CMDS`
- `deploy/iso/minikube-iso/arch/x86_64/package/nerdctl-bin/nerdctl-bin.mk` — spaces instead of tabs in `INSTALL_TARGET_CMDS`

Other packages (e.g. `crictl-bin`, `helm-bin`) correctly use tabs.

## Fix

Replace leading spaces with tabs in all four files listed above.

## Comments (0 total, first 0 shown)

(no comments)
