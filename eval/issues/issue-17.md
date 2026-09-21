# Eval item: issue-17

- source: jarun/googler#428
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: jarun/googler (6206 stars, archived: yes)
- description: :mag: Google from the terminal
- last push to any branch: 2021-11-13
- latest release: v4.3.2 (2021-01-21)
- open issues + PRs: 3
- last 5 default-branch commits:
  - 2021-11-13 by paxri01: Update PROTOCOL_TLS to PROTOCOL_TLS_CLIENT (#426)
  - 2021-10-24 by jarun: Skip failing test as Google News format has changed
  - 2021-10-24 by jarun: Sanitize -N (news) output
  - 2021-09-21 by rfaile313: Fix the --news functionality (#416)
  - 2021-09-19 by jarun: Update FUNDING.yml
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #435 (opened 2022-01-17): no maintainer comment in thread
  - #434 (opened 2022-01-11): no maintainer comment in thread
  - #429 (opened 2021-11-20): 39.2 days
  - #433 (opened 2021-12-28): 1.4 days
  - #432 (opened 2021-12-28): 0.2 days
- contribution policy: no CONTRIBUTING.md in the repo; no stated policy
- this issue: assignees: none; linked PRs: none

## Issue

### Video-specific search not working (#428)

opened by jarun (OWNER) on 2021-11-20, state open, labels: none

Video search has stopped working:

```
$ googler -V hello -d
[DEBUG] googler version 4.3.2
[DEBUG] Python version 3.9.5
[DEBUG] Platform: Linux-5.11.0-40-generic-x86_64-with-glibc2.33
[DEBUG] Connecting to new host www.google.com
[DEBUG] Opened socket to 142.250.67.36:443
[DEBUG] new_connection completed in 0.097s
[DEBUG] Fetching URL /search?ie=UTF-8&oe=UTF-8&q=hello&sei=YnmAPb4tR_qHZ+ZzAXrLvw&tbm=vid
[DEBUG] Cookie: 1P_JAR=2021-11-20-05
[DEBUG] fetch_page completed in 1.333s
[DEBUG] Response body written to '/tmp/googler-response-p0d8r3gp.html'.
[DEBUG] parse completed in 0.098s
No results.
[DEBUG] Fetching https://raw.githubusercontent.com/jarun/googler/master/info.json for project status...
If you believe this is a bug, please review https://git.io/googler-no-results before submitting a bug report.
googler (? for help)
```

Attached the html response. @zmwangx can you please have a look?
Doesn't look like we do anything special in the parser for videos today. So the format might have changed.

googler-response-p0d8r3gp.zip (`https://github.com/jarun/googler/files/7574001/googler-response-p0d8r3gp.zip`)

## Comments (0 total, first 0 shown)

(no comments)
