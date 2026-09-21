# Eval item: issue-08

- source: zulip/zulip#39794
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
- this issue: assignees: piyushagarwal-55; linked PRs: zulip/zulip#39811 (open)

## Issue

### Migrate compose and message-edit banners to the modern banner component (#39794)

opened by Yogesh-Shivaji365 (COLLABORATOR) on 2026-07-21, state open, labels: help wanted, good first issue, area: message-editing, in progress, area: compose (banners & validation), area: compose

The compose box and message-edit banners still use the legacy `.main-view-banner` markup, instead of the modern banner component
(`web/src/banners.ts`, viewable in the development environment at http://localhost:9991/devtools/banners/).

Because the legacy close button is an `<a role="button" tabindex="0">`, it takes focus on mouse clicks and shows a focus outline. That was worked around in #39759 with a `:focus:not(:focus-visible)` rule and a TODO pointing here; migrating would let us drop the workaround.

Note that the two components use different layout systems (flexbox vs. CSS grid, different padding, line height, and close button size), so this will change how the banners look worth confirming the intended [design](https://chat.zulip.org/#narrow/channel/101-design) before implementing.

## Comments (8 total, first 8 shown)

### piyushagarwal-55 (NONE) on 2026-07-23

Hi, I would like to work on this. Before I start, I want to confirm the approach:

Should this be done incrementally (one banner type at a time), or all at once?
The modern banners.ts component doesn't seem to support some things the legacy compose banners use — like the data-user-id / data-stream-id / data-topic-name attributes and the schedule/onboarding buttons. Should these be added to the banner component, or handled another way?
Could you confirm the intended visual design, since the layout changes from flexbox to CSS grid?
Thanks!

### zulipbot (MEMBER) on 2026-07-23

Hello @zulip/server-compose, @zulip/server-message-view members, this issue was labeled with the "area: message-editing", "area: compose" labels, so you may want to check it out!

<!-- areaLabelAddition -->

### zulipbot (MEMBER) on 2026-07-23

Hello @zulip/server-compose, @zulip/server-message-view members, this issue was labeled with the "area: message-editing", "area: compose" labels, so you may want to check it out!

<!-- areaLabelAddition -->

### amanagr (MEMBER) on 2026-07-24

> Should this be done incrementally (one banner type at a time), or all at once?

Yeah, that sounds fine.

### amanagr (MEMBER) on 2026-07-24

For the other questions, you can open a draft pull request and a design discussion along with it.

### piyushagarwal-55 (NONE) on 2026-07-24

Opened a draft PR (#39811 (`https://github.com/zulip/zulip/pull/39811`)) for the first banner in #39794 (`https://github.com/zulip/zulip/issues/39794`) (topic_missing). Question on the rest: the remaining compose banners need data-user-id/data-stream-id/data-topic-name on the banner root and data-* on action buttons (schedule/onboarding), which the modern component doesn't support yet. Should we extend Banner/ActionButton for data attributes, or rewire the handlers? Starting with the banners that need neither.

### amanagr (MEMBER) on 2026-07-24

I will have spend some time to answer your question, you can do what seems right to you. If you can't determite that you can open a #frontend discussion for it and tag me there.

### zulipbot (MEMBER) on 2026-08-03

@piyushagarwal-55 We noticed that you have not made any updates to this issue or linked PRs for 10 days. Please comment here if you are still actively working on it. Otherwise, we'd appreciate a quick `@zulipbot abandon` comment so that someone else can claim this issue and continue from where you left off.

If we don't hear back, you will be automatically unassigned in 4 days. Thanks!

<!-- inactiveWarning -->
