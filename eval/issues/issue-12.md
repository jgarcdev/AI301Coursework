# Eval item: issue-12

- source: bookwyrm-social/bookwyrm#1133
- captured: 2026-08-12
- calibration: false

## Repo facts (captured 2026-08-12)

- repo: bookwyrm-social/bookwyrm (2766 stars, archived: no)
- description: Social reading and reviewing, decentralized with ActivityPub
- last push to any branch: 2026-08-12
- latest release: v0.9.1 (2026-07-20)
- open issues + PRs: 412
- last 5 default-branch commits:
  - 2026-08-12 by Mouse Reeve: Merge pull request #4080 from PatrickChildersIT/cleaner-javascript
  - 2026-08-11 by Patrick Childers: fix inverted hidden logic for interact event
  - 2026-08-10 by Mouse Reeve: Merge pull request #4047 from hughrun/follow-fedi
  - 2026-08-10 by Mouse Reeve: Merge pull request #4083 from PatrickChildersIT/avoid-embedded-style-src
  - 2026-08-08 by Ilkka Ollakka: Merge pull request #4084 from ilkka-ollakka/fix/anubis_post_allow
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #4094 (opened 2026-08-12): 0.3 days
  - #4095 (opened 2026-08-12): no maintainer comment in thread
  - #3638 (opened 2025-07-09): 0.5 days
  - #3581 (opened 2025-05-20): 447.5 days
  - #4093 (opened 2026-08-10 by a maintainer): no maintainer comment in thread
- contribution policy (CONTRIBUTING.md -> docs.joinbookwyrm.com/contributing.html, section "Generative AI"): "Meaningful human interaction is the whole point of BookWyrm. We do not accept AI-generated code or documentation. If you are unsure how something in BookWyrm works, please ask for help – we are keen to help other humans to understand and contribute to the project."
- this issue: assignees: none; linked PRs: none

## Issue

### Include in-progress books in the reading-goal progress-bar (#1133)

opened by binyamin (NONE) on 2021-05-24, state open, labels: enhancement, good first issue, UI

> sorry for the messy issue. I'm tired :sweat_smile:

Include in-progress books in the reading-goal progress-bar

For example, if I read 1 out of 10 books, and I'm 20% done with my 2nd book, then the progress bar would be at 12% instead of 10%. It might be nice to have that "in-progress" portion in a different color.

Related to #56.

## Comments (3 total, first 3 shown)

### jrings (NONE) on 2024-09-19

I've started to look at this as it seems to be a good first issue. I got the data broken out for percent finished but not complete; the issue is unless I'm missing something there are no stacked progress bars. So this is what I have so far, but it's not very useful: 
![image](https://github.com/user-attachments/assets/d6587d5d-a683-4002-b3eb-211baba5d577)

I don't know much frontend stuff, is there a way to do a stacked bar?

### mouse-reeve (MEMBER) on 2024-09-19

There isn't a built-in way to do a stacked bar, and I don't think the html `progress` element supports that, unfortunately. You could definitely create one with html and css (we use the bulma css library), as long as it's screen-reader accessible.

### richardelliotweinberg (NONE) on 2025-05-08

Can there be a percentage/progress bar for books you are currently reading. I persentage/progress bar would be great for your years reading goal too.
