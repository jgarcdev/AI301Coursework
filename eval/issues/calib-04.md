# Eval item: calib-04

- source: sharkdp/bat#1341
- captured: 2026-08-05
- calibration: true

## Repo facts (captured 2026-08-05)

- repo: sharkdp/bat (60095 stars, archived: no)
- description: A cat(1) clone with wings.
- last push to any branch: 2026-08-01
- latest release: v0.26.1 (2025-12-02)
- open issues + PRs: 421
- last 5 default-branch commits:
  - 2026-08-01 by auto-merge-dependabot-prs[bot]: Merge pull request #3874 from sharkdp/dependabot/cargo/minus-5.7.2
  - 2026-08-01 by dependabot[bot]: build(deps): bump minus from 5.7.1 to 5.7.2
  - 2026-08-01 by auto-merge-dependabot-prs[bot]: Merge pull request #3869 from sharkdp/dependabot/cargo/gix-0.86.0
  - 2026-08-01 by dependabot[bot]: build(deps): bump gix from 0.85.0 to 0.86.0
  - 2026-08-01 by auto-merge-dependabot-prs[bot]: Merge pull request #3871 from sharkdp/dependabot/cargo/terminal-colorsaurus-1.0.3
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #3371 (opened 2025-08-08): no maintainer comment in thread
  - #3878 (opened 2026-08-03): no maintainer comment in thread
  - #3866 (opened 2026-08-01): no maintainer comment in thread
  - #1948 (opened 2021-11-17): 5.5 days
  - #2455 (opened 2023-01-21): 0.0 days
- contribution policy (CONTRIBUTING.md): no statement on AI or contribution tooling
- this issue: assignees: none; linked PRs: none formally linked (PR #3617 is referenced in the comment thread)

## Issue

### Custom fallback syntax opt-in (#1341)

opened by mckellygit (NONE) on 2020-10-24, state open, labels: feature-request, good first issue

Hi,
Thank you for bat, it is awesome (and so is fd!)
Is there a way to have a fallback syntax ?
I don't want to force a new syntax for known file types, I just want to set it to something reasonable for files that did not match any known type.
thx,
-m

## Comments (23 total, first 22 shown)

### sharkdp (OWNER) on 2020-10-24

Thank you for the feedback.

>  Is there a way to have a fallback syntax ?

There is no way to do this currently (maybe by overwriting the `plaintext` syntax..).

>  I don't want to force a new syntax for known file types, I just want to set it to something reasonable for files that did not match any known type.

What would "something reasonable" be?

### mckellygit (NONE) on 2020-10-24

@sharkdp I agree what makes a good fallback syntax is just my opinion, but it could be set to whatever a user wants, including none.  I prefer some color to none though.  For me, I would probably try bash as a fallback.
I'll look into plaintext.
thx,
-m

### mckellygit (NONE) on 2020-10-24

*I think* I have it working ok (for me) with a hacked sublime bash syntax file added as plaintext.
thx so much,
-m

### sharkdp (OWNER) on 2020-10-25

Glad that worked :+1: 

I am not sure if this is something that should be added in a more official manner. I'm inclined to say no, though. It seems to me that most users would be irritated by the potentially wrong highlighting.

I'm therefore closing the issue for now, but let me know if someone feels otherwise.

### wommel (NONE) on 2021-01-16

I think it would be helpfull to have some basic highlighting for unsupported languages.

Nano in this case (besides some "Nano"  shenanigans) highlights everthing that starts with `#` as a commtent. This is basicaly correct for any kind of text based config file i could find which is neither json nor xml. This is a great help to at least conceive the basic structure of a foreign config file or quickly see the important parts of a known one.

### mmcnl (NONE) on 2022-02-12

@mckellygit do you have your hacked plaintext syntax available somewhere? I'd be interested in trying it out. Thanks!

### mckellygit (NONE) on 2022-02-13

Hi,
I created dir: ~/.config/bat/syntaxes/sublime-plaintext-syntax
 and in this dir, I added this file: plaintext.sublime-syntax
 and in this file I added these lines at the top, after the %YAML 1.2 line:
```
name: Plain Text
scope: source.shell.bash
version: 2

extends: Packages/ShellScript/commands-builtin-shell-bash.sublime-syntax

file_extensions:
  - txt

hidden_file_extensions:
  - .bash_aliases
  - .bash_completions
  - .bash_functions
  - .bash_login
  - .bash_logout
  - .bash_profile
  - .bash_variables
  - .bashrc
  - .profile
  - .textmate_init
  - .zlogin
  - .zlogout
  - .zprofile
  - .zshenv
  - .zshrc
  - PKGBUILD  # https://jlk.fjfi.cvut.cz/arch/manpages/man/PKGBUILD.5
  - ebuild
  - eclass

first_line_match: |-
  (?x:
    \s*\*
  )

```
I forget where I found the original plaintext.sublime-syntax file but I will look again or I can attach mine here.
thx,
-m

### mckellygit (NONE) on 2022-02-13

I think the file was from:
```
https://github.com/sublimehq/Packages/blob/master/ShellScript/Bash.sublime-syntax
```
so I renamed it and editted the first few lines to look like above.

### mmcnl (NONE) on 2022-02-13

awesome, thanks @mckellygit!

### mmcnl (NONE) on 2022-05-06

@sharkdp  I am wondering if you would re-consider adding this feature as an option that requires the user to opt-in. This would be very helpful for me as a sysadmin because I frequently have the same need as mentioned above (`https://github.com/sharkdp/bat/issues/1341#issuecomment-761527586`)
> Nano in this case ... highlights everything that starts with # as a comment. This is basically correct for any kind of text based config file i could find which is neither json nor xml. This is a great help to at least conceive the basic structure of a foreign config file or quickly see the important parts of a known one.

In terms of UX, it could be something like `--fallback-syntax=ini` which would only take effect if the current file doesn't match any other language.

I did investigate the custom plaintext suggested by @mckellygit but that approach doesn't work for arbitrary/unknown file extensi
[... truncated, 954 chars total]

### Enselic (COLLABORATOR) on 2022-05-06

To me this sounds like reasonable opt-in functionality, so if someone comes up with a good solution with a good set of integration tests, I think that is something we could add. Since @sharkdp was not sure if closing was the right move, and since there seems to be more than a one-off interest in something like this, I think we should re-open this one.

### mckellygit (NONE) on 2022-05-06

>> but that approach doesn't work for arbitrary/unknown file extensions.

It does for me.  Not sure if I explained my config correctly, but I do get syntax highlighting on arbitrary and unknown files/extensions.
But of course having a builtin fallback syntax would be awesome.

### mmcnl (NONE) on 2022-05-08

@mckellygit I went back and tried your approach again and was able to get it to work.  🎉  Thanks again for the inspiration and instructions!

In the process, I simplified the syntax definition file to only highlight line comments and ignore all of the other bash syntax rules which, in most cases for me, were not needed (eg in `monit` config files). Most likely someone with actual sublime syntax knowledge could simplify this further.

For anyone following along, the full sequence of steps to set this up is:

1. create a `~/.config/bat/syntaxes/sublime-plaintext-syntax/plaintext.sublime-syntax` file with the content below
2. rebuild the bat cache with `bat cache --build` (I was the missing this step the first time I tried)

```
# ~/.config/bat/syntaxes/sublime-plaintext-syntax/plaintext.sublime-syntax

name: Plain Text
scope: source.shell.bash
version: 2

file_extensions:
  - txt

first_li
[... truncated, 1238 chars total]

### mckellygit (NONE) on 2022-05-08

ok, great.  I am so sorry I forgot to list the bat cache --build step.

### BattleCh1cken (NONE) on 2022-09-29

I'd like to work on this as my first rust contribution, is this still relevant?

### keith-hall (COLLABORATOR) on 2022-09-30

Yep, still relevant :)

### Xavrir (CONTRIBUTOR) on 2026-03-07

I’m working on this and plan to open a PR implementing an opt-in  flag with integration tests.

### Xavrir (CONTRIBUTOR) on 2026-03-07

Correction: implementing opt-in `--fallback-syntax` (fallback-only; does not override `--language`) with integration tests.

### Xavrir (CONTRIBUTOR) on 2026-03-07

Opened PR #3617 implementing  (alias: ) with integration tests and no behavior changes to .

### Xavrir (CONTRIBUTOR) on 2026-03-07

Correction: opened PR #3617 implementing --fallback-syntax (alias: --fallback-language) with integration tests and no behavior changes to --language.

### jgarte (NONE) on 2026-05-29

Hi, is this issue complete?

### mckellygit (NONE) on 2026-06-11

Hi,

I have not tried configuring a fallback syntax and removing my custom plain-text syntax file.
I will do that and report back.
But before I even test - if this means the highlighting of unknown files happens now then I'd say yes this issue is complete.

-m
