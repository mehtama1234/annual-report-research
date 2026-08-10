## Local-Only Research Delta Handoff

Date: 2026-08-10

Purpose:
- document the remaining non-raw research work that is still stranded on the local backup branch
- separate this from the completed raw-to-Drive offload
- give the next CLI thread an exact merge target so the remaining research can land on remote `main`

## Current State

- repo: `/home/manishmehta/ui-projects/annual-report-research`
- clean local `main`: `ebb571c1d1f62bbd75f587ed983e922c9a8ad14c`
- backup branch with local-only work: `backup/raw-heavy-local-main-2026-08-10`
- backup branch head: `70cc9921e157939a449efb0d835402079b823ad2`
- raw offload manifest commit already on remote `main`: `26dae821618ab0d556dbc364970762480a811086`

Important distinction:
- raw evidence payload has already been moved to Google Drive and pointered on remote `main`
- substantial research, extracted synthesis, themes, indexes, and notes are still only on the backup branch

## What Is Already Done

- `raw/**` upload and pointer workflow is complete
- remote `main` is pushable and contains `0 raw/**` files in the pushed delta
- Drive tar and checksum links already exist

This handoff is only about the remaining research delta.

## What Is Still Local-Only

The diff from `main...backup/raw-heavy-local-main-2026-08-10` still contains non-raw work in these areas:

### Extracted Company Work

- updated basic materials packets, profiles, and ledgers for:
  - `alcoa-corporation`
  - `freeport-mcmoran-inc`
  - `nucor-corporation`
  - `reliance-steel-aluminum-co`
- added full extracted packets, profiles, and ledgers for:
  - `synchrony-financial`
  - `upstart-holdings-inc`
  - `affirm-holdings-inc`
- updated:
  - `extracted/industrial-goods/building-materials-wholesale/core-main-inc/company-packet.md`

### Theme And Interpretation Work

- updated cross-company theme files under `extracted/themes/`, including:
  - taxonomy blind spots
  - behind-the-shelf consumer infrastructure systems
  - consumer cultural pattern map
  - DTC versus channel control
  - hidden connectivity and access layer systems
  - loyalty, wallet, and membership systems
  - platform and ecosystem mapping
  - relationship-system migration paths
  - retail-system crosswalk
  - thick-versus-thin relationship systems
- added:
  - `extracted/themes/waste-management-vs-republic-vs-clean-harbors-vs-casella-boundary-comparison-2026-08-10.md`

### Index And Coverage Work

- updated queue, coverage, and blind-spot tracking files under `indexes/`
- updated:
  - `indexes/companies.csv`
  - `indexes/sectors.csv`
  - `indexes/coverage-tracker.csv`
  - direct comparison indexes
  - hidden connectivity indexes
  - consumer interface indexes
  - annualreports noncovered indexes

### Notes And Handoffs

- updated multiple blind-spot status and audit notes
- added:
  - `notes/cli4-raw-blob-offload-handoff-2026-08-10.md`
  - `notes/frontier-merge-handoff-2026-08-10.md`
  - `notes/rclone-offload-and-main-push-supplement-2026-08-10.md`
  - `notes/rclone-raw-blob-offload-handoff-2026-08-10.md`
- added:
  - `manifests/media-frontier-large-artifacts-2026-08-10.md`

## Commit Stack Still Missing From Remote Main

The backup branch contains a long local-only stack. The most relevant commits include:

- `99a94328` `Add frontier merge handoff note`
- `4532e611` `Add rclone offload supplement for main push`
- `e5d5efa8` `Reconcile remaining index conflicts`
- `ee3ba52f` `Add raw blob offload handoff note`
- `d4399b73` `Clean blind-spot and packet conflict repairs`
- `2b7fc2a0` `Update direct comparison index for Cogent-Lumen memo`
- `7ad210c4` `Bring remaining CLI9 packets and frontier artifacts onto main`
- `520fd012` `Bring media frontier archive work onto main`
- `1e43a006` `Bring remaining frontier worktree changes onto main`
- `63f872f3` `Commit remaining frontier note and comparison updates on main`
- `24b961e9` `Bring CLI4 healthcare frontier batch onto main`
- `5f413eee` `Add blind-spot frontier research batch`

The branch also contains a much larger historical packet stack that includes many energy and basic-materials packet commits.

## Recommended Integration Target

The next CLI thread should move the remaining non-raw research onto remote `main`.

Default recommendation:
- keep raw payload externalized on Drive
- keep remote `main` as the canonical clean branch
- replay or cherry-pick only the non-raw research changes from the backup branch

## Safest Integration Approaches

### Option 1: Selective Cherry-Pick

Use this if the next thread wants to preserve commit structure where possible.

Recommended first picks:

1. `24b961e9`
2. `63f872f3`
3. `1e43a006`
4. `520fd012`
5. `7ad210c4`
6. `2b7fc2a0`
7. `d4399b73`
8. `ee3ba52f`
9. `4532e611`
10. `99a94328`

Expect conflicts in:
- `indexes/companies.csv`
- `indexes/sectors.csv`
- `indexes/coverage-tracker.csv`
- other evolving queue and audit files

### Option 2: Replay Only The Non-Raw Diff

Use this if the next thread wants faster completion and does not need to preserve the old local commit structure.

Suggested flow:

1. check out a new integration branch from remote `main`
2. copy or apply only the non-`raw/` diff from `backup/raw-heavy-local-main-2026-08-10`
3. verify no `raw/**` files enter the commit
4. commit the remaining extracted, theme, index, note, and manifest changes as one or a few clean commits
5. push and merge

This is likely the fastest route.

## Commands The Next Thread Can Reuse

List remaining non-raw files:

```bash
repo=/home/manishmehta/ui-projects/annual-report-research
git -C "$repo" diff --name-status main...backup/raw-heavy-local-main-2026-08-10 \
| awk '$2 !~ /^raw\\// {print}'
```

List local-only commits:

```bash
repo=/home/manishmehta/ui-projects/annual-report-research
git -C "$repo" log --oneline --left-right --cherry-pick main...backup/raw-heavy-local-main-2026-08-10 \
| awk '/^>/{print}'
```

Verify a candidate commit contains no raw payload before pushing:

```bash
repo=/home/manishmehta/ui-projects/annual-report-research
git -C "$repo" diff --name-only origin/main..HEAD | rg '^raw/'
```

## What Should Go To Main Versus Drive

Should go to remote `main`:
- `extracted/**`
- `indexes/**`
- `notes/**`
- `manifests/**`
- any cross-company interpretation or company packet markdown

Should stay externalized on Drive:
- heavy `raw/**` binaries and archive captures already offloaded

Do not solve this by uploading extracted research to Drive.
That would break the repo's usable research layer.

## Deliverable For The Next CLI Thread

The next thread should come back with:

1. commit hash or hashes that bring the remaining non-raw research onto `main`
2. confirmation that no `raw/**` files were reintroduced
3. a short list of any files intentionally left local-only
4. conflict notes if any shared indexes required manual reconciliation

## Short Forward Message

Use `/home/manishmehta/ui-projects/annual-report-research/notes/local-only-research-delta-handoff-2026-08-10.md`.

Raw payload is already offloaded.
Your job is to move the remaining non-raw research delta from `backup/raw-heavy-local-main-2026-08-10` onto clean `main` without reintroducing `raw/**`.
