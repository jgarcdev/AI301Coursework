# Eval item: issue-01

- source: conda/conda#16475
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
- this issue: assignees: none; linked PRs: none

## Issue

### Add permanent docs for installing PyPI packages with `conda install` (#16475)

opened by dashagurova (CONTRIBUTOR) on 2026-07-31, state open, labels: type::documentation

### Checklist

- [x] I added a descriptive title
- [x] I searched open reports and couldn't find a duplicate

### What happened?

## Problem
 
The `conda install` workflow for supported PyPI packages is going GA/stable (in September), but the docs do not yet have a permanent home for it.
 
Right now, the workflow mainly lives in `new-features.md`, which is useful for release highlights but not for long term user guidance. Users looking for this later are more likely to find `manage-pkgs.rst`, especially the "Installing non-conda packages" section, which currently still points them toward the older workaround of installing `pip` inside a conda environment and running `pip install` separately.
 
We should add a stable docs location for the GA workflow and update the existing pages that currently mention older or temporary guidance.
 
## Proposed changes
 
### Add a new task page
 
Create a new task page, for example: `Installing PyPI packages with conda`
This should be a standalone page, not a subsection of `manage-pkgs.rst`, because the workflow has its own setup, channel behavior, package selection model, and caveats.
**The page should cover:**
* what the workflow does: install supported PyPI packages with `conda install`, alongside regular conda packages
* what the `conda-pypi` channel is on anaconda.org, provanace, governance (community-led, free)
* required setup: min conda version, adding `conda-pypi` channel, channel priority
* basic usage, including an example that installs conda and PyPI packages together, and how to find what is available before installing (`conda search`, and browsing the channel on anaconda.org)
* environment files: packages currently listed in a `pip:` section of an `environment.yml` can be moved into the regular dependencies list once the channel is added, so the whole environment resolves in one solve
* how packages installed this way behave in normal conda workflows, including `conda list`, export, remove, and environment removal
* troubleshooting or limitations (for example worth saying that this feature is only supported in conda client as right now, with CEP in discussion and then hopefully other ecosystem clients will implement it)

### Update `manage-pkgs.rst`
Update "Installing non-conda packages" so the new page becomes the recommended path for supported PyPI packages. Keep the existing `pip` guidance, but frame it as the fallback for workflows not covered by `conda install` with the `conda-pypi` channel.
 
### Update `pip-interoperability.rst`
This page currently refers to an old deprecated feature and only has minimal current content about conda-pypi. Replace it with a short pointer to the new task page for the current PyPI package installation workflow.
 
### Update `new-features.md`
Keep the feature card short and point users to the new task page.
Move setup steps, examples, warnings, and behavior details out of `new-features.md` and into the permanent docs page. Update the badge if needed for GA.
 
### Consider a global `troubleshooting.rst` entry
Lower priority, but worth naming. Users hitting a broken pip-plus-conda environment might search the global `troubleshooting.rst`. A short entry there pointing to the conda-pypi workflow would catch people who never find the task page.

### Additional Context

## Content notes for the new page
 
The new page should be clear that this is not "pip replacement" documentation. It is the recommended conda CLI workflow for PyPI dependancies. Because pip installing in conda envs is problematic (we can link to a blog post by Mahe for deeper dive on why is problematic)
 
Some general points to include:
* Users can install supported PyPI packages (which is all pure Python wheels) and conda packages together with one `conda install` or `conda create` command.
* Conda channels should stay first in the channel list, with `conda-pypi` added after them.
* Conda should use packages from conda channels where available and reach `conda-pypi` for supported PyPI packages that are otherwise missing.
* On channel priority: keep it brief here and link to `manage-channels.rst` for the mechanics. The point worth making is that this is the one case where mixing channels is safe without strict priority. Strict priority is normally recommended when mixing channels to avoid ABI incompatibility between mismatched compiled binaries, but the `conda-pypi` channel only has pure Python wheels, so that risk does not apply. Flexible priority is fine when pairing it wi
[... truncated, 5615 chars total]

## Comments (0 total, first 0 shown)

(no comments)
