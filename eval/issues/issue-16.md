# Eval item: issue-16

- source: conda/conda#16487
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

### Conda channel notices break json parsing (when stderr and stdout are on the same pipe) (#16487)

opened by Callek (CONTRIBUTOR) on 2026-08-03, state open, labels: type::bug

### Checklist

- [x] I added a descriptive title
- [x] I searched open reports and couldn't find a duplicate

### What happened?

When a channel notice is active for a used channel, but you specify `--json` output. Such as on a `conda create ...` command, you get the channel notice output as raw text on stderr.  where if a user is capturing both stderr and stdout on the same pipe could break json parsing.  But also means that the notices are invisible to the json.

### Conda Info

```shell
active environment : base
    active env location : /Users/callek/miniconda3
            shell level : 3
       user config file : /Users/callek/.condarc
 populated config files : /etc/conda/condarc
                          /Users/callek/miniconda3/.condarc
                          /Users/callek/miniconda3/condarc.d/anaconda-auth.yml
                          /Users/callek/.condarc
          conda version : 26.5.3
    conda-build version : 26.5.0
         python version : 3.13.13.final.0
                 solver : libmamba (default)
       virtual packages : __archspec=1=m4
                          __conda=26.5.3=0
                          __osx=26.5=0
                          __unix=0=0
       base environment : /Users/callek/miniconda3  (writable)
      conda av data dir : /Users/callek/miniconda3/etc/conda
  conda av metadata url : None
           channel URLs : https://repo.anaconda.com/pkgs/main/osx-arm64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-arm64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /Users/callek/miniconda3/pkgs
                          /Users/callek/.conda/pkgs
       envs directories : /Users/callek/miniconda3/envs
                          /Users/callek/.conda/envs
    temporary directory : /var/folders/8b/rfz9vgn576j9c_38v9byy_c40000gp/T
               platform : osx-arm64
             user-agent : conda/26.5.3 requests/2.34.2 CPython/3.13.13 Darwin/25.5.0 OSX/26.5 solver/libmamba conda-libmamba-solver/26.6.0 libmambapy/2.3.2 aau/0.8.1 c/. s/. e/. m/.
                UID:GID : 502:20
             netrc file : None
           offline mode : False
```

### Conda Config

```shell
==> /etc/conda/condarc <==
aggressive_update_packages:
  - anaconda-anon-usage
  - anaconda-ident
  - conda-anaconda-telemetry
anaconda_anon_usage: True
anaconda_heartbeat: True

==> /Users/callek/miniconda3/.condarc <==
channels:
  - defaults

==> /Users/callek/miniconda3/condarc.d/anaconda-auth.yml <==
channel_settings:
  - channel: https://repo.anaconda.cloud/*
    auth: anaconda-auth

==> /Users/callek/.condarc <==
default_activation_env: /Users/callek/miniconda3/envs/default

==> envvars <==
allow_softlinks: False
```

### Conda list

```shell
# packages in environment at /Users/callek/miniconda3:
#
# Name                       Version          Build               Channel
anaconda-anon-usage          0.8.1            pyhb46e38b_100      defaults
anaconda-auth                0.15.1           py313hca03da5_0     defaults
anaconda-cli-base            0.9.1            py313hca03da5_0     defaults
annotated-doc                0.0.4            py313hca03da5_0     defaults
annotated-types              0.6.0            py313hca03da5_1     defaults
anyio                        4.12.1           py313hca03da5_0     defaults
archspec                     0.2.6            py313hca03da5_0     defaults
attrs                        26.1.0           py313h0d18f5d_0     defaults
backports.zstd               1.3.0            py313hb3cf4b8_0     defaults
beautifulsoup4               4.15.0           py313hca03da5_0     defaults
boltons                      25.0.0           py313hca03da5_0     defaults
brotlicffi                   1.2.0.0          py313h50f4ffc_0     defaults
bzip2                        1.0.8            h80987f9_6          defaults
c-ares                       1.34.6           hfe05a68_0          defaults
ca-certificates              2026.5.14        hca03da5_0          defaults
cctools                      1030.6.3         h0aecbd0_1          defaults
certifi                      2026.6.17        py313hca03da5_0     defaults
cffi                         2.0.0            py313h73c2a22_1     defaults
chardet                      5.2.0            py313hca03da5_0     defaults
charset-normalizer           3.4.7            py313hca03da5_0     defaults
click                        8.4.1            py31
[... truncated, 16125 chars total]

## Comments (0 total, first 0 shown)

(no comments)
