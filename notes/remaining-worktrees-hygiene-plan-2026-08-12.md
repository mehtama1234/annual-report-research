# Remaining Worktrees Hygiene Plan

Date: 2026-08-12

This note is the final hygiene plan for the still-dirty local worktrees attached to `annual-report-research`.

## Current state

- `main` is the authoritative archive branch and is already pushed.
- The concrete packet-side promotions and targeted raw offloads discussed in this session are already settled.
- The remaining worktrees are local hygiene problems, not blockers for archive delivery.

## Worktree 1: `parallel/new-lanes`

- Path: `/home/manishmehta/ui-projects/annual-report-research-new-lanes`
- Branch: `parallel/new-lanes`
- Head: `26cde3a5`
- Dirty count: `13`

### What is in it

Untracked raw-only leftovers:

- savings-loans
- REIT-specialty
- Juniper
- healthcare-information-services
- one UnitedHealth `2026-q2-10q.html`
- two Sysco SEC files

Approximate local size:

- financial savings-loans raw: `58M` combined
- real-estate REIT-specialty raw: `21M+`
- Juniper raw: `18M+`
- healthcare-information-services raw: `6M+`
- Sysco raw: `18M`
- UnitedHealth file: `1.8M`

### Decision

- `Offload or ignore`

### Rule

- Do not merge these into `main`.
- If they matter, bundle them into a future raw-only Drive offload with a pointer note.
- If nobody needs them, leave them local or discard later outside this wrap-up.

## Worktree 2: `parallel/apparel-cluster`

- Path: `/home/manishmehta/ui-projects/annual-report-research-apparel-cluster`
- Branch: `parallel/apparel-cluster`
- Head: `27e6b4d4`
- Dirty count: `425`

### What is in it

Mixed text and raw clutter across:

- basic materials
- healthcare instruments
- services
- technology
- consumer-goods
- indexes
- notes
- raw annualreports verification files

It also contains many untracked sector/company trees and cross-sector writeups, including:

- media frontier files
- basic-materials expansion trees
- packaging and retail extensions
- healthcare instrument and specialized-health trees
- broader industrial and services additions

### Decision

- `Keep for separate triage`

### Rule

- Do not treat this as a single merge candidate.
- Do not offload everything blindly.
- If this branch is revisited, split it into:
  - text packets/syntheses worth comparing to `main`
  - raw evidence worth Drive offload
  - duplicate or branch-behind material to ignore

### Priority

- Lower than `main` integrity and lower than the already-completed targeted offloads.
- This is a future curation pass, not a current blocker.

## Worktree 3: `cli9-remaining-frontiers`

- Path: `/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers`
- Branch: `cli9-remaining-frontiers`
- Head: `f33ef0de`
- Dirty count: `2639`

### What is in it

Large mixed local state across:

- financial raw
- technology raw
- healthcare raw
- consumer-goods raw
- industrial-goods raw
- real-estate raw
- packet edits
- index/planning surfaces

### Decision

- `Closed for healthcare packet promotion`
- `Keep only as a future salvage source`

### Rule

- Do not merge this worktree wholesale.
- The healthcare packet review already concluded that no additional healthcare packet text should be promoted from it.
- Any future value is likely to be:
  - selective raw offload
  - selective blind-spot planning extraction
  - selective packet comparison in non-healthcare lanes

### Existing reference

- [notes/cli9-remaining-frontiers-promotion-ledger-2026-08-12.md](/home/manishmehta/ui-projects/annual-report-research/notes/cli9-remaining-frontiers-promotion-ledger-2026-08-12.md)

## Final keep/offload/ignore summary

### Keep for future triage

- `parallel/apparel-cluster`
- `cli9-remaining-frontiers` as a salvage source only

### Offload if needed

- `parallel/new-lanes` leftover raw-only files
- any future raw subsets extracted deliberately from `parallel/apparel-cluster`
- any future raw subsets extracted deliberately from `cli9-remaining-frontiers`

### Ignore for now

- all remaining dirty worktree state that is not blocking `main`
- duplicate branch-behind packet trees already represented on `main`
- raw delete noise caused by prior offload work

## Operational close

The archive is wrapped enough to stop.

- `main` is the working source of truth
- Drive contains the targeted offloaded evidence bundle already created in this session
- the remaining worktrees are hygiene backlog, not unresolved archive delivery
