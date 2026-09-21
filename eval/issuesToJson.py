#!/usr/bin/env python3
"""Mirror every issues/*.md bundle as issues/*.json.

The markdown bundles are the canonical snapshots (captured on the date
stamped in each file); this script derives a structured JSON view of the
same frozen content so the issues can be read programmatically. It never
touches the network: the live issues have moved on since capture, and
re-fetching would desynchronize the snapshots from the gold labels.

Usage: python3 issues_to_json.py   (from this directory; rewrites *.json)
"""

import json
import re
from pathlib import Path

ISSUES_DIR = Path(__file__).parent / "issues"

META_RE = re.compile(r"^- (source|captured|calibration): (.+)$")
TITLE_RE = re.compile(r"^### (.+) \(#(\d+)\)$")
OPENED_RE = re.compile(r"^opened by (\S+) \((\w+)\) on (\d{4}-\d{2}-\d{2}), "r"state (\w+), labels: (.+)$")
COMMENTS_HDR_RE = re.compile(r"^## Comments \((\d+) total(?:, first (\d+) shown)?\)$")
COMMENT_RE = re.compile(r"^### (\S+) \((\w+)\) on (\d{4}-\d{2}-\d{2})$")
THIS_ISSUE_RE = re.compile(r"^- this issue: assignees: ([^;]+);? ?(?:linked PRs: (.+))?$")


def splitSections(lines):
  """Yield (kind, payload) per structural heading, fence-aware."""
  sections = {"meta": [], "repo_facts": [], "issue": [], "comments": []}
  current = "meta"
  fenced = False
  for line in lines:
    if line.startswith("```"):
      fenced = not fenced
      sections[current].append(line)
      continue
    if line.startswith("## "):
      # A comment can end with a fence GitHub closes implicitly at
      # end-of-comment; a structural heading therefore closes any
      # fence still open rather than being swallowed by it.
      fenced = False
    if not fenced:
      if line.startswith("## Repo facts"):
        current = "repo_facts"
        continue
      if line == "## Issue":
        current = "issue"
        continue
      if COMMENTS_HDR_RE.match(line):
        sections["comments_header"] = line
        current = "comments"
        continue
    sections[current].append(line)

  return sections


def parseComments(lines):
  comments, current, fenced = [], None, False
  for line in lines:
    m = COMMENT_RE.match(line)
    if m:
      # same implicit-close rule as in split_sections: a heading
      # ends any fence the previous comment left open
      fenced = False
    elif line.startswith("```"): fenced = not fenced
    if m:
      current = {
        "author": m.group(1),
        "author_association": m.group(2),
        "date": m.group(3),
        "body_markdown": [],
      }
      comments.append(current)
    elif current is not None: current["body_markdown"].append(line)
  for c in comments: c["body_markdown"] = "\n".join(c["body_markdown"]).strip()

  return comments


def parseBundle(path):
  lines = path.read_text().splitlines()
  out = {"id": path.stem, "calibration": False}

  sections = splitSections(lines)

  for line in sections["meta"]:
    m = META_RE.match(line)
    if m:
      key, val = m.groups()
      out[key] = True if val == "true" else val

  factsRaw = "\n".join(sections["repo_facts"]).strip()
  facts = {"raw_markdown": factsRaw}
  for line in sections["repo_facts"]:
    m = THIS_ISSUE_RE.match(line)
    if m:
      assignees = m.group(1).strip()
      facts["assignees"] = [] if assignees == "none" else assignees.split(", ")
      prs = m.group(2) or ""
      facts["linked_prs"] = [{"ref": r, "state": s} for r, s in re.findall(r"([\w.-]+/[\w.-]+#\d+) \((\w+)\)", prs)]
  out["repo_facts"] = facts

  issue = {}
  bodyStart = 0
  for i, line in enumerate(sections["issue"]):
    m = TITLE_RE.match(line)
    if m and "title" not in issue:
      issue["title"], issue["number"] = m.group(1), int(m.group(2))
      continue
    m = OPENED_RE.match(line)
    if m:
      issue["author"], issue["author_association"] = m.group(1), m.group(2)
      issue["opened"], issue["state"] = m.group(3), m.group(4)
      labels = m.group(5).strip()
      issue["labels"] = [] if labels == "none" else labels.split(", ")
      bodyStart = i + 1
      break
  issue["body_markdown"] = "\n".join(sections["issue"][bodyStart:]).strip()
  out["issue"] = issue

  hdr = sections.get("comments_header")
  if hdr:
    m = COMMENTS_HDR_RE.match(hdr)
    out["comments_total"] = int(m.group(1))
    out["comments"] = parseComments(sections["comments"])
  else:
    out["comments_total"] = 0
    out["comments"] = []

  return out


def main():
  bundles = sorted(ISSUES_DIR.glob("*.md"))
  for path in bundles:
    data = parseBundle(path)
    dest = path.with_suffix(".json")
    dest.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    nShown = len(data["comments"])
    print(f"{dest.name}: #{data['issue'].get('number', '?')} {data['comments_total']} comments ({nShown} captured)")
  print(f"{len(bundles)} bundles mirrored")


if __name__ == "__main__":
  main()