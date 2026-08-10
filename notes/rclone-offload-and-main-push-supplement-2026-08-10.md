# Rclone Offload And Main Push Supplement

Date: 2026-08-10

Purpose:
- give the separate `rclone` / remote-push thread the extra context needed to carry my local-only work to remote `main`
- clarify that my latest commits are mostly merge-repair and index-reconciliation work, not a new source of large raw payload
- ensure the offload thread preserves the repaired local `main` state while reducing the raw blob weight enough to push

## Current Repo State

- repo: `/home/manishmehta/ui-projects/annual-report-research`
- branch: `main`
- current local head: `e5d5efa846beedddd7bfb81341253b4e94f89f0f`
- current short head: `e5d5efa8`
- remote tracking ref: `origin/main`
- ahead/behind from `origin/main...main`: `1 103`
  - interpretation: local `main` is `103` commits ahead of `origin/main` and `1` commit behind it
- worktree status at note time: clean

## Commits From My Thread That Must Be Preserved

The key local-only commits from my repair pass are:

1. `d4399b73352969136da747a2623c25f9f5de64ff`
   - message: `Clean blind-spot and packet conflict repairs`
2. `e5d5efa846beedddd7bfb81341253b4e94f89f0f`
   - message: `Reconcile remaining index conflicts`

These commits should make it to the final pushed branch.

## What Those Commits Actually Changed

These commits are mostly lightweight repo-surface repair work:

- cleaned remaining markdown merge conflicts
- reconciled remaining index CSV conflicts
- removed duplicate rows in:
  - `indexes/companies.csv`
  - `indexes/coverage-tracker.csv`
- preserved the fuller blind-spot, packaging, hidden-connectivity, and fandom/play rows where there were competing versions

They are not the main reason the push is heavy.
The push pressure still comes from the same large `raw/...` payload described in:

- [rclone-raw-blob-offload-handoff-2026-08-10.md](/home/manishmehta/ui-projects/annual-report-research/notes/rclone-raw-blob-offload-handoff-2026-08-10.md)

## Important Conclusion

The offload thread should treat my work as:

- `must preserve`
- `low blob impact`
- `already integrated on local main`

So the right operational plan is:

1. start from current local `main`
2. preserve `d4399b73` and `e5d5efa8`
3. offload heavy `raw/...` payloads to Google Drive
4. create the manifest / pointer artifacts
5. perform whatever history cleanup is necessary to reduce push size
6. push the resulting repaired branch to remote `main` or report the exact rewritten branch / force-push instructions

## Blob Reality Check

My repair commits themselves are not the blob issue.
The heavy payload is still dominated by the existing local-only raw range.

Largest raw buckets still visible in `origin/main..main`:

1. `539038470` bytes
   - `raw/sec/energy`
2. `419811754` bytes
   - `raw/company-ir/energy`
3. `357753105` bytes
   - `raw/company-ir/basic-materials`
4. `262646670` bytes
   - `raw/sec/basic-materials`
5. `217916623` bytes
   - `raw/company-ir/technology`
6. `186988567` bytes
   - `raw/sec/consumer-goods`
7. `130204229` bytes
   - `raw/company-ir/consumer-goods`

The offload thread should still prioritize those buckets first.

## Large Raw Files That Intersect Areas I Touched Conceptually

Even though my commits were mostly repair work, the current local-only range also includes raw payload for names that now show up in repaired indexes and syntheses, including:

- `raw/company-ir/consumer-goods/toys-games/mattel-inc/2025-annual-report.pdf`
- `raw/company-ir/basic-materials/specialty-chemicals/ecolab-inc/2025-annual-report.pdf`
- `raw/company-ir/basic-materials/specialty-chemicals/ecolab-inc/2026-q2-earnings-slides.pdf`
- `raw/sec/basic-materials/specialty-chemicals/ecolab-inc/2025-10k.html`
- `raw/company-ir/consumer-goods/packaging-containers/packaging-corporation-of-america/2025-annual-report.pdf`
- `raw/sec/consumer-goods/packaging-containers/packaging-corporation-of-america/2025-10k.html`

That means the offload thread can safely move those raw payloads too, as long as it leaves the repaired extracted and index layers intact.

## What Must Not Be Touched

Do not strip or damage the repaired research surface:

- `extracted/`
- `indexes/`
- `notes/`
- `analysis/`
- `site/`

The thread should offload only heavy `raw/...` payloads and then preserve lightweight manifest or pointer records in Git.

## Suggested Merge-Back Result

The final result handed back by the offload thread should include:

1. pushed branch or explicit force-push target
2. resulting remote-visible commit hash
3. confirmation that both repair commits survived
4. Google Drive root URL
5. manifest commit hash
6. uploaded raw-path list
7. removed raw-path list
8. any history-rewrite instructions if the branch was rewritten before push

## Simple Instruction To The Offload Thread

If the thread wants one sentence:

- preserve local `main` through `e5d5efa8`, offload the heavy `raw/...` buckets already identified in the original handoff note, then push the repaired branch state to remote `main`
