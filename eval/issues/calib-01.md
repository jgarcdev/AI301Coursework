# Eval item: calib-01

- source: processing/p5.js#9039
- captured: 2026-08-05
- calibration: true

## Repo facts (captured 2026-08-05)

- repo: processing/p5.js (23844 stars, archived: no)
- description: p5.js is a client-side JS platform that empowers artists, designers, students, and anyone to learn to code and express themselves creatively on the web. It is based on the core principles of Processin
[... truncated, 246 chars total]
- last push to any branch: 2026-08-04
- latest release: v2.3.2 (2026-07-30)
- open issues + PRs: 500
- last 5 default-branch commits:
  - 2026-08-04 by davepagurek: Merge pull request #8955 from Nixxx19/renderer-per-part
  - 2026-08-04 by davepagurek: Remove default export addon
  - 2026-08-04 by davepagurek: Merge branch 'main' into renderer-per-part
  - 2026-08-04 by davepagurek: Merge pull request #8879 from Nixxx19/geometry-part-refactor
  - 2026-08-04 by davepagurek: Merge branch 'main' into geometry-part-refactor
- maintainer first-response sample (5 recently updated issues, days to first owner/member/collaborator comment):
  - #7899 (opened 2025-06-10 by a maintainer): 79.9 days
  - #8940 (opened 2026-06-18 by a maintainer): 4.8 days
  - #9033 (opened 2026-08-03): no maintainer comment in thread
  - #9037 (opened 2026-08-04): 0.2 days
  - #9038 (opened 2026-08-04 by a maintainer): 0.0 days
- contribution policy (CONTRIBUTING.md, section "AI Usage Policy"): fully AI-generated contributions are not accepted; assistive AI use is allowed, and the contributor must understand and take responsibility for every change (details in AI_USAGE_POLICY.md and AGENTS.md)
- this issue: assignees: none; linked PRs: none

## Issue

### [p5.js 2.0+ Bug Report]: min/max function with variable length parametes (#9039)

opened by TakagiHitoshi (NONE) on 2026-08-04, state open, labels: Area:Math, p5.js 2.0+

### Most appropriate sub-area of p5.js?

- [ ] Accessibility
- [ ] Color
- [ ] Core/Environment/Rendering
- [ ] Data
- [ ] DOM
- [ ] Events
- [ ] Image
- [ ] IO
- [x] Math
- [ ] Typography
- [ ] Utilities
- [ ] WebGL
- [ ] WebGPU
- [ ] p5.strands
- [ ] Build process
- [ ] Unit testing
- [ ] Internationalization
- [ ] Friendly errors
- [ ] Other (specify if possible)

### p5.js version

2.3.2

### Web browser and version

chrome 150.0.7871.187

### Operating system

Windows 11

### Steps to reproduce this

This is not an exact bug report, but a request.
min function accepts variable length parameters in p5js v.1, Now it says "Expected at most 2 arguments, but received more in min()." Would be good if compatibility would be maintained.

### Steps:
1. run a code with min(1, 2, 3, 4)
### Snippet:
t=0
draw=_=>{
createCanvas(W=(w=200)*2,W)+colorMode(HSB)+noFill()
for(R=0;R<w;R+=18)for(T=0;T<TAU;T+=.1)
translate(x=R*cos(U=T+t/41)+w,y=R*sin(U)+w),
rotate(t/R+U),
stroke(D=min(x,y,W-x,W-y)*2,w,w,9),
ellipse(0,0,D,D/2),
resetMatrix()
++t}

## Comments (0 total, first 0 shown)

(no comments)
