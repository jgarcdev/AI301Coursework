# Eval item: issue-15

- source: zulip/zulip#19589
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: zulip/zulip (25604 stars, archived: no)
- description: Zulip server and web application. Open-source team chat that helps teams stay productive and focused.
- last push to any branch: 2026-08-04
- latest release: 12.1 (2026-06-26)
- open issues + PRs: 2043
- last 5 default-branch commits:
  - 2026-08-03 by amanagr: tornado: Report errors as JSON instead of rendering portico pages.
  - 2026-08-03 by amanagr: test_tornado: Run the test harness with Tornado's URL configuration.
  - 2026-08-03 by PieterCK: webhook/slack: Handle missing "real_name" field in UserInfo endpoint.
  - 2026-07-29 by sathwikshetty33: webhooks/airbyte: Remove stale STREAM_NAME attribute.
  - 2026-07-14 by sathwikshetty33: webhooks/docs: Advise collecting only necessary fixtures.
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #38839 (opened 2026-04-06 by a maintainer): 91.7 days
  - #39859 (opened 2026-07-31): 2.6 days
- contribution policy (CONTRIBUTING.md, section "AI use policy and guidelines"): AI tools allowed; contributors must personally understand, test, and be able to explain every change; AI-generated PRs that appear untested or not understood are closed without review
- this issue: assignees: none; linked PRs: zulip/zulip#20840 (closed); zulip/zulip#23123 (closed)

## Issue

### Separate `command` and `text` field for slack-compatible outgoing webhook (#19589)

opened by esamson (NONE) on 2021-08-18, state open, labels: help wanted, area: integrations, good first issue

Discussed here: https://chat.zulip.org/#narrow/stream/127-integrations/topic/gitlab.20slash.20commands/near/1247658

Current behavior puts entire message, including bot mention, in the `text` field of the outgoing POST.

POST coming from Slack itself puts the "slash command" in a separate `command` field while their `text` field only contains the message body after the command.

For better compatibility, if message starts with a bot mention then we should separate that out into a `command` field and put the rest of the message in the `text` field.

Perhaps we can also transform the mention (`**@mybot**`) to a slash command (`/mybot`) so it looks like it would coming from Slack.

## Comments (97 total, first 40 shown)

### zulipbot (MEMBER) on 2021-09-03

Hello @zulip/server-integrations members, this issue was labeled with the "area: integrations" label, so you may want to check it out!

<!-- areaLabelAddition -->

### timabbott (MEMBER) on 2021-09-17

@esamson can you provide an example Slack payload or a pointer to the right part of their documentation?  

https://api.slack.com/legacy/custom-integrations/outgoing-webhooks#legacy-info__post-data does not suggest the presence of a `command` field, but that is a legacy API.

### esamson (NONE) on 2021-09-18

Yeah, I haven't been able to find docs but just observed this by testing against Slack itself.

### esamson (NONE) on 2021-09-28

Hi, @timabbott.

Here is a sample capture, pointing a Slack slash command to requestbin and sending the command: `/gitlab test`

https://requestbin.com/r/en843hnins6x/1ylmaovFRI8NFkkNrZA92vtruUi

```
token=A7Fg5BIh4gBu3C8TxCMtIEQr&team_id=T02BB2GRXGD&team_domain=espaleklek&channel_id=D02AZB5N1AB&channel_name=directmessage&user_id=U02B7AS8J30&user_name=edward.samson&command=%2Fgitlab&text=test&is_enterprise_install=false&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT02BB2GRXGD%2F2534343413430%2Fi0r5OBTVGEZE4yfXZ0PaRaq3
```

What's also interesting there is **response_url**, which is where a response is posted in the case of long tasks. But that's another matter.

### madrix01 (COLLABORATOR) on 2021-10-02

@timabbott @eeshangarg can i work on this issue ??

### jsmwoolf (COLLABORATOR) on 2021-10-14

@madrix01 There's a command on [this page](https://zulip.readthedocs.io/en/latest/overview/contributing.html#working-on-an-issue) you can use to pick up the issue.

### eeshangarg (MEMBER) on 2021-10-15

@esamson Thanks for the additional context! When you say "by testing against Slack itself", do you mean you created a "Slack app" and then pointed the endpoint URL to requestbin? Thanks for reporting!

### eeshangarg (MEMBER) on 2021-10-15

@timabbott Looks like the [Enabling interactivity with Slash commands](https://api.slack.com/interactivity/slash-commands) has the updated format for how the slash commands are supposed to be structured.

### esamson (NONE) on 2021-10-16

@eeshangarg Yes, that's what I did. I took the instruction from https://docs.gitlab.com/ee/user/project/integrations/slack_slash_commands.html and pointed to requestbin instead of gitlab.

### eeshangarg (MEMBER) on 2021-10-25

@esamson Awesome, thank you so much!

### LoganNiswander (COLLABORATOR) on 2021-11-17

@zulipbot claim
Would love to work on this as my first open source contribution!

### zulipbot (MEMBER) on 2021-11-17

Welcome to Zulip, @LoganNiswander! We just sent you an invite to collaborate on this repository at `https://github.com/zulip/zulip/invitations.` Please accept this invite in order to claim this issue and begin a fun, rewarding experience contributing to Zulip!

Here's some tips to get you off to a good start:

- Join me on the [Zulip developers' server](https://chat.zulip.org), to get help, chat about this issue, and meet the other developers.
- Unwatch this repository (`https://help.github.com/articles/unwatching-repositories/`), so that you don't get 100 emails a day.

As you work on this issue, you'll also want to refer to the [Zulip code contribution guide](https://zulip.readthedocs.io/en/latest/contributing/index.html), as well as the rest of the developer documentation on that site.

See you on the other side (that is, the pull request side)!

### zulipbot (MEMBER) on 2021-11-27

Hello @LoganNiswander, you have been unassigned from this issue because you have not updated this issue or any referenced pull requests for over 14 days.

You can reclaim this issue or claim any other issue by commenting `@zulipbot claim` on that issue.

Thanks for your contributions, and hope to see you again soon!

### leighadennis (COLLABORATOR) on 2021-12-16

@zulipbot claim

### zulipbot (MEMBER) on 2021-12-16

Hello @leighadennis, it looks like you've currently claimed 1 issue in this repository. We encourage new contributors to focus their efforts on at most 1 issue at a time, so please complete your work on your other claimed issues before trying to claim this issue again.

We look forward to your valuable contributions!

### leighadennis (COLLABORATOR) on 2021-12-16

@zulipbot claim

### zulipbot (MEMBER) on 2021-12-27

Hello @leighadennis, you have been unassigned from this issue because you have not updated this issue or any referenced pull requests for over 14 days.

You can reclaim this issue or claim any other issue by commenting `@zulipbot claim` on that issue.

Thanks for your contributions, and hope to see you again soon!

### blackbird7112 (COLLABORATOR) on 2022-01-16

@zulipbot claim

### zulipbot (MEMBER) on 2022-01-16

Welcome to Zulip, @rohithvarma3000! We just sent you an invite to collaborate on this repository at `https://github.com/zulip/zulip/invitations.` Please accept this invite in order to claim this issue and begin a fun, rewarding experience contributing to Zulip!

Here's some tips to get you off to a good start:

- Join me on the [Zulip developers' server](https://chat.zulip.org), to get help, chat about this issue, and meet the other developers.
- Unwatch this repository (`https://help.github.com/articles/unwatching-repositories/`), so that you don't get 100 emails a day.

As you work on this issue, you'll also want to refer to the [Zulip code contribution guide](https://zulip.readthedocs.io/en/latest/contributing/index.html), as well as the rest of the developer documentation on that site.

See you on the other side (that is, the pull request side)!

### zulipbot (MEMBER) on 2022-01-26

Hello @rohithvarma3000, you have been unassigned from this issue because you have not updated this issue or any referenced pull requests for over 14 days.

You can reclaim this issue or claim any other issue by commenting `@zulipbot claim` on that issue.

Thanks for your contributions, and hope to see you again soon!

### blackbird7112 (COLLABORATOR) on 2022-01-26

I have worked on this issue and I have made a PR. Review is pending

### BrianMcDowell (COLLABORATOR) on 2022-09-27

@zulipbot claim

### zulipbot (MEMBER) on 2022-09-27

Welcome to Zulip, @BrianMcDowell! We just sent you an invite to collaborate on this repository at `https://github.com/zulip/zulip/invitations.` Please accept this invite in order to claim this issue and begin a fun, rewarding experience contributing to Zulip!

Here's some tips to get you off to a good start:

- Join me on the [Zulip developers' server](https://chat.zulip.org), to get help, chat about this issue, and meet the other developers.
- Unwatch this repository (`https://help.github.com/articles/unwatching-repositories/`), so that you don't get 100 emails a day.

As you work on this issue, you'll also want to refer to the [Zulip code contribution guide](https://zulip.readthedocs.io/en/latest/contributing/index.html), as well as the rest of the developer documentation on that site.

See you on the other side (that is, the pull request side)!

### zulipbot (MEMBER) on 2022-10-13

@BrianMcDowell You have been unassigned from this issue because you have not made any updates for over 14 days. Please feel free to reclaim the issue if you decide to pick up again. Thanks!

### sudhanshu154 (COLLABORATOR) on 2022-12-08

@zulipbot claim

### zulipbot (MEMBER) on 2022-12-08

Hello @sudhanshu154, it looks like you've currently claimed 1 issue in this repository. We encourage new contributors to focus their efforts on at most 1 issue at a time, so please complete your work on your other claimed issues before trying to claim this issue again.

We look forward to your valuable contributions!

### sudhanshu154 (COLLABORATOR) on 2022-12-08

@zulipbot claim

### Kaustubhkongile (COLLABORATOR) on 2023-03-29

@zulipbot claim

### zulipbot (MEMBER) on 2023-03-29

Welcome to Zulip, @Kaustubhkongile! We just sent you an invite to collaborate on this repository at `https://github.com/zulip/zulip/invitations.` Please accept this invite in order to claim this issue and begin a fun, rewarding experience contributing to Zulip!

Here's some tips to get you off to a good start:

- Join me on the [Zulip developers' server](https://chat.zulip.org), to get help, chat about this issue, and meet the other developers.
- Unwatch this repository (`https://help.github.com/articles/unwatching-repositories/`), so that you don't get 100 emails a day.

As you work on this issue, you'll also want to refer to the [Zulip code contribution guide](https://zulip.readthedocs.io/en/latest/contributing/index.html), as well as the rest of the developer documentation on that site.

See you on the other side (that is, the pull request side)!

### zulipbot (MEMBER) on 2023-04-08

@Kaustubhkongile You have been unassigned from this issue because you have not made any updates for over 14 days. Please feel free to reclaim the issue if you decide to pick up again. Thanks!

### zulipbot (MEMBER) on 2023-12-12

**ERROR:** Unexpected response from GitHub API.

### ikrambil (COLLABORATOR) on 2023-12-12

@zulipbot claim

### zulipbot (MEMBER) on 2023-12-12

Welcome to Zulip, @ikrambil! We just sent you an invite to collaborate on this repository at `https://github.com/zulip/zulip/invitations.` Please accept this invite in order to claim this issue and begin a fun, rewarding experience contributing to Zulip!

Here's some tips to get you off to a good start:

- Join me on the [Zulip developers' server](https://chat.zulip.org), to get help, chat about this issue, and meet the other developers.
- Unwatch this repository (`https://help.github.com/articles/unwatching-repositories/`), so that you don't get 100 emails a day.

As you work on this issue, you'll also want to refer to the [Zulip code contribution guide](https://zulip.readthedocs.io/en/latest/contributing/index.html), as well as the rest of the developer documentation on that site.

See you on the other side (that is, the pull request side)!

### taeukkang09 (NONE) on 2023-12-12

@zulipbot claim

### zulipbot (MEMBER) on 2023-12-12

@taeukkang09 This issue cannot be claimed, as someone else is already working on it. Please see our [contributor guide](https://zulip.readthedocs.io/en/latest/overview/contributing.html#your-first-codebase-contribution) for advice on finding an issue to work on. Thanks!

### zulipbot (MEMBER) on 2023-12-22

@ikrambil You have been unassigned from this issue because you have not made any updates for over 14 days. Please feel free to reclaim the issue if you decide to pick up again. Thanks!

### SamChen41 (COLLABORATOR) on 2024-01-28

@zulipbot claim

### zulipbot (MEMBER) on 2024-01-28

Welcome to Zulip, @SamchenUF! We just sent you an invite to collaborate on this repository at `https://github.com/zulip/zulip/invitations.` Please accept this invite in order to claim this issue and begin a fun, rewarding experience contributing to Zulip!

Here's some tips to get you off to a good start:

- Join me on the [Zulip developers' server](https://chat.zulip.org), to get help, chat about this issue, and meet the other developers.
- Unwatch this repository (`https://help.github.com/articles/unwatching-repositories/`), so that you don't get 100 emails a day.

As you work on this issue, you'll also want to refer to the [Zulip code contribution guide](https://zulip.readthedocs.io/en/latest/contributing/index.html), as well as the rest of the developer documentation on that site.

See you on the other side (that is, the pull request side)!

### zulipbot (MEMBER) on 2024-02-07

@SamchenUF You have been unassigned from this issue because you have not made any updates for over 14 days. Please feel free to reclaim the issue if you decide to pick up again. Thanks!

### souvik150 (COLLABORATOR) on 2024-02-16

@zulipbot claim
