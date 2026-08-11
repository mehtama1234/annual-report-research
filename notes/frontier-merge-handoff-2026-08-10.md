# Frontier Merge Handoff

Date: 2026-08-10
Repo: `annual-report-research`
Primary repo path: `/home/manishmehta/ui-projects/annual-report-research`
Current branch at handoff: `main`
Current `main` commit at handoff: `4532e6117213dafdb656f40916707d0cc1e014ff`

## Packet Inputs Used

- the observed `main` history and the still-unmerged-by-ancestry frontier branches listed in this handoff
- the prior merge attempt findings about copied content versus preserved ancestry
- the identified blocker conditions, especially path conflicts such as the `Hasbro` split
- the repo rule that branch reconciliation should preserve real evidence state and avoid destructive resets
- the success-condition requirement that a later reconciliation pass should leave clear statements about represented payloads, intentionally unmerged refs, and ancestry status

## Purpose

This note is for the next thread that needs to reconcile the remaining frontier branch lines against `main` without reconstructing the last merge attempt from scratch.

The repo has already absorbed a large amount of frontier work directly onto `main`, but several source branches still show as not merged by ancestry even though some of their content appears to have been copied or replayed onto `main` through direct commits.

## What is already on `main`

Recent `main` history now includes:

- `4532e611` `Add rclone offload supplement for main push`
- `e5d5efa8` `Reconcile remaining index conflicts`
- `ee3ba52f` `Add raw blob offload handoff note`
- `e01474ea` `Merge research outputs from cli4 healthcare branch`
- `d4399b73` `Clean blind-spot and packet conflict repairs`
- `1ab0dc48` `Merge remote-tracking branch 'origin/main'`
- `2b7fc2a0` `Update direct comparison index for Cogent-Lumen memo`
- `7ad210c4` `Bring remaining CLI9 packets and frontier artifacts onto main`
- `520fd012` `Bring media frontier archive work onto main`
- `1e43a006` `Bring remaining frontier worktree changes onto main`
- `32c31e8b` `Merge media and edge infrastructure frontier archive`
- `63f872f3` `Commit remaining frontier note and comparison updates on main`

Earlier already-landed work also includes:

- energy batch on `main`
- blind-spot frontier batch on `main`
- related post-merge notes and conflict-repair commits

## Branches that still show as not merged by ancestry

As of this handoff, these refs are still not merged into `main` according to `git merge-base --is-ancestor <branch> main`:

- `cli4-healthcare-frontier-batch`
- `media-frontier-archive`
- `parallel/new-lanes`
- `parallel/footwear-dept-audit`
- `cli9-remaining-frontiers`

That does **not** mean their content is absent. It means the exact branch tips are not ancestors of `main`.

## Current branch tips observed at handoff

- `main` -> `4532e6117213dafdb656f40916707d0cc1e014ff`
- `cli4-healthcare-frontier-batch` -> `00da1581b5e0ff9bca9eb2db9dcc90aec0352ac7`
- `cli9-remaining-frontiers` -> `46055b6ddfd56fcd4fb1b5b9fc664664928ebf46`
- `media-frontier-archive` -> `9b7b0a327c92050cb222edecee1ca2eb5d24bcf2`
- `parallel/footwear-dept-audit` -> `06199e773b62c69b40d4d01b6e6ebc08f2ddc136`
- `parallel/new-lanes` -> `1620b15395ab64e2daad1ed8692beee206419985`

## What I verified during the merge attempt

1. `main` was moving while I was working.
2. Several direct commits landed on `main` during the process and pulled in frontier content outside a simple branch merge flow.
3. A synthetic merge path using `git merge-tree --write-tree -Xtheirs` could produce clean merge trees for:
   - `parallel/footwear-dept-audit`
   - `media-frontier-archive`
   - `parallel/new-lanes`
   - `cli4-healthcare-frontier-batch`
4. `cli9-remaining-frontiers` remained the unstable branch line.

## The real blocker

`cli9-remaining-frontiers` had path and rename conflicts around `Hasbro` and related moved raw directories.

The important failure pattern was:

- older paths under `raw/.../none/hasbro-inc/`
- newer paths under `raw/.../toys-games-hobbies/hasbro-inc/`
- directory rename ambiguity
- file-location conflicts on SEC artifacts such as:
  - `2025-10k.html`
  - `2025-q4-8k.html`
  - `2026-q1-10q.html`
  - `2026-q1-8k.html`
  - `2026-q2-10q.html`
  - `2026-q2-8k.html`

This is why `cli9-remaining-frontiers` should **not** be force-merged blindly just because most other branches were absorbable.

## Safe interpretation of the current state

- `main` already contains a large amount of the frontier work in content terms.
- branch ancestry is no longer a reliable proxy for whether the research payload is present.
- the remaining job is now a reconciliation problem, not a first-pass merge problem.

## Recommended next actions

1. Treat `main` as the authoritative working branch from `4532e611`.
2. Diff each still-unmerged branch against `main` by path, not just by commit ancestry.
3. For `cli4-healthcare-frontier-batch`, `media-frontier-archive`, `parallel/new-lanes`, and `parallel/footwear-dept-audit`:
   - identify what is actually still missing from `main`
   - cherry-pick or manually copy only the remaining deltas
   - avoid replaying the whole branch if `main` already contains most of the payload
4. For `cli9-remaining-frontiers`:
   - inspect the `Hasbro` raw-path conflict first
   - normalize the intended destination directory
   - then merge or replay the remaining branch content after fixing the path model
5. After reconciliation, re-run:
   - `git merge-base --is-ancestor <branch> main`
   - or explicitly document that branch content was absorbed without preserving ancestry
6. Keep the raw blob offload work separate from branch reconciliation:
   - see `notes/rclone-raw-blob-offload-handoff-2026-08-10.md`

## What not to do

- Do not force-reset active worktrees.
- Do not treat all raw untracked material as disposable.
- Do not assume a branch is unnecessary just because `main` has similarly named files.
- Do not blindly merge `cli9-remaining-frontiers` without resolving the `Hasbro` path split.

## Minimal success condition for the next thread

The next thread should finish with:

- a concrete statement of which branch payloads are now fully represented on `main`
- a list of any remaining intentionally unmerged refs
- a note on whether ancestry was preserved or only content was preserved
- commit hashes for any final reconciliation commits

## Insight-System Maintenance

When you need to confirm that this frontier-merge handoff, the reusable-note boundary, and the broader continuation surfaces still line up before reusing it as a reconciliation reference, use:

- `bash scripts/run-insight-audit-stack.sh`
- `bash scripts/refresh-note-layer-boundary.sh`
- `bash scripts/audit-audit-stack-terminology.sh`
- `bash scripts/audit-maintenance-doc-stack.sh`
- `bash scripts/audit-continuation-mode-links.sh`
- `bash scripts/audit-remaining-brief-links.sh`
- `bash scripts/audit-remaining-stack-links.sh`
- `bash scripts/audit-browser-review-links.sh`
- `bash scripts/verify-insight-system.sh`

## Skeptical Reader Test

- Does this handoff make clear what the next reconciliation thread is trying to prove about branch payloads versus ancestry?
- Can a skeptical reader tell which branches still need attention and what the real blocker was in the prior attempt?
- Does the note protect the next worker from destructive shortcuts like force resets or blind merges?
- What missing branch-state or blocker detail would make the reconciliation plan too weak to trust?
