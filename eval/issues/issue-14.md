# Eval item: issue-14

- source: LegalQuants/lq-ai#490
- captured: 2026-08-05
- calibration: false

## Repo facts (captured 2026-08-05)

- repo: LegalQuants/lq-ai (113 stars, archived: no)
- description: 
- last push to any branch: 2026-08-05
- latest release: desktop-v0.6.2 (2026-07-04)
- open issues + PRs: 133
- last 5 default-branch commits:
  - 2026-08-05 by SaifAlYounan: Scope autonomous retrieve_chunks to the session owner (AG-01, Refs #288) (#401)
  - 2026-08-05 by sergiomaldo: List KBs by the project_knowledge_bases junction, with backfill (#442)
  - 2026-08-04 by SaifAlYounan: Derive ProviderEgressRefused from LQAIError (typed per CONTRIBUTING) (#488)
  - 2026-08-03 by SaifAlYounan: Guard LLM provider base_url egress at build time (GW-04, Refs #288) (#400)
  - 2026-08-01 by SaifAlYounan: Validate project ownership on chat creation (API-01 IDOR, Refs #288) (#397)
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #489 (opened 2026-08-04): no maintainer comment in thread
- contribution policy (CONTRIBUTING.md): no statement on AI or contribution tooling
- this issue: assignees: none; linked PRs: none

## Issue

### Docs: remove Discord references — the server was never stood up (#490)

opened by houfu (CONTRIBUTOR) on 2026-08-04, state open, labels: documentation, good first issue

## Summary

Our issue templates and contributor docs point people at a Discord server (`discord.gg/lq-ai`) that doesn't exist — it was planned in the original repo-opening checklist but never created. Anyone who clicks the link today hits a dead invite.

The fix is to remove the Discord references and route community conversation to **GitHub Discussions**, which we do keep open for questions from outside the LegalQuants team (and which SECURITY.md and ADR 0022 already rely on).

This is a documentation-only change — no code, no tests, no build step. It's a good first contribution if you'd like to get familiar with our PR process.

## What to change

Six files reference Discord. In each, remove the Discord reference and, where it served as a "where to ask" pointer, point at GitHub Discussions instead:

1. **`.github/ISSUE_TEMPLATE/config.yml`** — delete the `Discord community` contact-link entry (3 lines: `name`, `url`, `about`). Keep the `Security vulnerability` and `GitHub Discussions` entries as they are.

2. **`docs/PRD.md` §7.7 "Project Channels"** (around line 1752) — delete the `**Discord** (LegalQuants-hosted) for synchronous community.` bullet. Leave the Issues, Discussions, and blog bullets.

3. **`README.md` "Project channels"** (around line 482) — same one-bullet deletion; this section mirrors PRD §7.7.

4. **`CONTRIBUTING.md`** — two spots:
   - ~line 354: change "please ping a maintainer in the PR or in `#contributors` on Discord" → "please ping a maintainer in the PR or open a thread in GitHub Discussions."
   - ~line 374: change "**General questions** → GitHub Discussions or `#contributors` on Discord." → "**General questions** → GitHub Discussions."

5. **`skills/CONTRIBUTING.md`** (~line 269): change "GitHub Discussions or `#skill-authors` on Discord" → "GitHub Discussions."

6. **`.github/MAINTAINERS/repo-opening-checklist.md`** — *leave this one alone.* It's a historical one-time checklist, not a live doc; a maintainer will annotate it separately.

Please don't add any other channels while you're in there — internal team channels deliberately aren't listed in public docs.

## Checking your work

- `grep -rni discord` across the repo — excluding `web/` (an upstream fork whose docs we don't edit) and `.github/MAINTAINERS/` — should come back empty after your change.
- SECURITY.md doesn't mention Discord, so it needs no edit — if your grep flags it, look again.

## How to contribute the change (first-timer walkthrough)

1.  Comment in this issue that you'd like to take this.
2. Fork the repo and clone your fork.
3. Create a branch, e.g. `docs/remove-discord-refs`.
4. Make the edits above. No formatter or test suite applies to these files.
5. Commit with a sign-off — this is required, not optional:   ```
   git commit -s -m "Remove Discord references from community docs"
   ```
   The `-s` adds the DCO `Signed-off-by:` trailer; CI rejects commits without it. Use imperative mood in the message ("Remove X", not "Removed X").
5. In the commit body or PR description, add `Closes #<this issue's number>`.
6. Push and open a PR against `main`. In the description, say in a sentence what you changed and paste the (empty) output of the grep check above.
7. A maintainer will review within ~5 business days ([CONTRIBUTING.md](../CONTRIBUTING.md) has the full process).

Questions about any of this? Ask right here in the issue thread — that's what it's for.

## Comments (0 total, first 0 shown)

(no comments)
