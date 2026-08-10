## Rclone Raw Blob Offload Handoff

Date: 2026-08-10

Purpose:
- hand this note to the separate CLI thread that is moving oversized raw archives to Google Drive with `rclone`
- preserve the extracted research, indexes, notes, and site work already integrated on local `main`
- reduce the raw binary payload that is blocking or stalling the push to `origin/main`

## Repo State

- repo: `/home/manishmehta/ui-projects/annual-report-research`
- current branch: `main`
- local `main`: `d4399b73352969136da747a2623c25f9f5de64ff`
- remote `origin/main`: `e01474ea345bf8d24c79c1e8ebfd9a4cc4fa1519`
- ahead/behind count from `origin/main...main`: `1 101`
  - interpretation: local `main` is 101 commits ahead and 1 commit behind the remote tracking ref
- worktree status when this note was finalized: dirty
  - there are active extracted/index/note edits in the repo
  - those edits are not the offload target
  - the offload thread should isolate its work to `raw/...` plus a manifest/pointer commit

## Why This Is Needed

GitHub is not obviously blocked by a single `>100 MB` file in the unpushed range, but the repo is carrying too much medium-to-large raw evidence.

Observed local repo size indicators:
- `4748` objects in `origin/main..main`
- `.git` packed object size: about `4.13 GiB`
- loose object size: about `820 MiB`

The likely push blocker is cumulative pack size and raw binary volume, not one illegal blob.

## Highest-Priority Blob Candidates In `origin/main..main`

Largest unpushed blobs found:

1. `53477876` bytes
   `raw/sec/energy/independent-oil-gas/matador-resources-co/2025-annual-report-ars.pdf`
2. `44453030` bytes
   `raw/company-ir/technology/application-software/affirm-holdings-inc/2025-annual-report.pdf`
3. `40854951` bytes
   `raw/annualreports/basic-materials/gold/kinross-gold-corporation/2025-annual-report.pdf`
4. `32323962` bytes
   `raw/company-ir/energy/independent-oil-gas/matador-resources-co/2025-annual-report.pdf`
5. `28452625` bytes
   `raw/company-ir/technology/internet-service-providers/etsy-inc/2026-q1-shareholder-letter.pdf`
6. `24692666` bytes
   `raw/sec/basic-materials/industrial-metals-minerals/rio-tinto-plc/2025-20f.html`
7. `23922637` bytes
   `raw/company-ir/basic-materials/industrial-metals-minerals/hudbay-minerals-inc/2025-annual-report.pdf`
8. `21684061` bytes
   `raw/company-ir/financial/credit-services/synchrony-financial/2025-annual-report.pdf`
9. `21556305` bytes
   `raw/company-ir/technology/internet-service-providers/etsy-inc/2026-q2-shareholder-letter.pdf`
10. `21478259` bytes
    `raw/sec/energy/independent-oil-gas/diamondback-energy-inc/2025-annual-report-ars.pdf`

More large blobs remain below these, but the pattern is clear: `raw/sec`, `raw/company-ir`, and some `raw/annualreports` PDFs and large HTML/TXT captures dominate the payload.

## Heaviest Raw Directory Buckets In `origin/main..main`

Aggregate byte totals by top raw bucket:

1. `539038470`
   `raw/sec/energy`
2. `419811754`
   `raw/company-ir/energy`
3. `357753105`
   `raw/company-ir/basic-materials`
4. `262646670`
   `raw/sec/basic-materials`
5. `217916623`
   `raw/company-ir/technology`
6. `186988567`
   `raw/sec/consumer-goods`
7. `130204229`
   `raw/company-ir/consumer-goods`
8. `53859220`
   `raw/company-ir/industrial-goods`
9. `49882085`
   `raw/company-ir/services`
10. `43909984`
    `raw/annualreports/basic-materials`
11. `37764641`
    `raw/company-ir/financial`
12. `17827971`
    `raw/sec/financial`

If the other thread wants the fastest relief, start with:
- `raw/sec/energy`
- `raw/company-ir/energy`
- `raw/company-ir/basic-materials`
- `raw/sec/basic-materials`
- `raw/company-ir/technology`

## What Must Stay In Git

Do not offload these first-class research outputs:
- `extracted/`
- `indexes/`
- `notes/`
- `analysis/`
- `site/`

Only the heavy raw evidence trees should be moved out:
- `raw/annualreports/...`
- `raw/company-ir/...`
- `raw/sec/...`

Do not touch these even if they mention the same companies:
- company packets
- company profiles
- source ledgers
- sector or lane syntheses
- queue files and coverage indexes
- handoff notes

## Newly Integrated Research That Should Survive The Offload

Recent integrated work on local `main` includes:
- CLI4 healthcare frontier batch
- media frontier archive payload
- blind-spot and hidden-connectivity integration
- Cogent versus Lumen comparison indexing
- CLI9 company packets now present on local `main`
  - `extracted/financial/credit-services/synchrony-financial/`
  - `extracted/financial/credit-services/upstart-holdings-inc/`
  - `extracted/technology/application-software/affirm-holdings-inc/`

The offload thread should preserve those extracted trees while moving the corresponding heavy raw trees out of Git.

## Suggested Offload Procedure

1. Upload the targeted `raw/...` directories or files to Google Drive with `rclone`.
2. Record stable Drive links in a manifest file inside the repo.
3. Remove the uploaded raw files from Git history or from the current commit range, depending on the chosen cleanup approach.
4. Leave lightweight manifest pointers in Git so the evidence chain is still navigable.

## Exact Scope For The Rclone Thread

The other CLI thread should work in this order:

1. inspect the largest unpushed `raw/...` blobs and buckets listed below
2. upload those files or their containing company folders to Drive
3. create a repo manifest commit with Drive URLs and checksums
4. coordinate a history cleanup or commit-range cleanup that drops the uploaded raw payload from the push set
5. merge the manifest-and-pointer work back into `main`

The other thread does not need to re-research the companies.
Its job is transport, pointering, and payload reduction.

## Highest-Value Raw Trees To Offload First

If the other thread wants a deterministic first pass, start here:

1. `raw/sec/energy/`
2. `raw/company-ir/energy/`
3. `raw/company-ir/basic-materials/`
4. `raw/sec/basic-materials/`
5. `raw/company-ir/technology/`
6. `raw/sec/consumer-goods/`
7. `raw/company-ir/consumer-goods/`
8. `raw/company-ir/financial/`

These buckets carry the bulk of the unpushed binary weight and should produce the biggest relief fastest.

## Manifest And Pointer Structure

Recommended repo-resident artifacts after upload:

1. `indexes/raw-blob-offload-manifest-2026-08-10.csv`
2. `notes/raw-blob-offload-readme-2026-08-10.md`
3. optional lightweight per-company pointer files if the thread wants company-local discoverability

Recommended CSV columns:

- `local_path`
- `drive_url`
- `bytes`
- `sha256`
- `source_family`
- `sector`
- `industry`
- `company_slug`
- `as_of_date`
- `offloaded_by_commit`
- `notes`

`source_family` should be one of:
- `annualreports`
- `company-ir`
- `sec`

## Suggested Rclone Layout

If the other thread wants a stable Drive directory layout, use something like:

- `annual-report-research/raw/sec/...`
- `annual-report-research/raw/company-ir/...`
- `annual-report-research/raw/annualreports/...`

That mirrors repo paths and makes the manifest trivial to audit.

## Merge-Back Deliverables

The offload thread should hand back all of the following:

1. the manifest commit hash
2. the exact Drive root or shared folder URL
3. the list of raw paths uploaded
4. the list of raw paths removed from Git payload
5. any history-rewrite command or branch used to strip the payload
6. confirmation that `extracted/`, `indexes/`, and `notes/` were left intact

If it rewrites history, it must also report the new branch head so the integration thread knows what to fast-forward or force-push.

## Suggested Manifest Fields

If the other thread needs a consistent manifest format, use rows like:

- `local_path`
- `drive_url`
- `bytes`
- `sha256` or `md5` if they want verification
- `coverage_lane`
- `notes`

Example rows:

- `raw/sec/energy/independent-oil-gas/matador-resources-co/2025-annual-report-ars.pdf`
- `raw/company-ir/technology/application-software/affirm-holdings-inc/2025-annual-report.pdf`
- `raw/annualreports/basic-materials/gold/kinross-gold-corporation/2025-annual-report.pdf`

## Commands The Other Thread Can Reuse

Largest unpushed blobs:

```bash
repo=/home/manishmehta/ui-projects/annual-report-research
git -C "$repo" rev-list --objects origin/main..main \
| git -C "$repo" cat-file --batch-check='%(objectname) %(objecttype) %(objectsize) %(rest)' \
| awk '$2=="blob"{printf "%s\t%s\n", $3, $4}' \
| sort -nr \
| sed -n '1,40p'
```

Heaviest raw buckets:

```bash
repo=/home/manishmehta/ui-projects/annual-report-research
git -C "$repo" rev-list --objects origin/main..main \
| git -C "$repo" cat-file --batch-check='%(objectname) %(objecttype) %(objectsize) %(rest)' \
| awk '$2=="blob" && $4 ~ /^raw\\// {
    split($4,a,"/");
    key=a[1]"/"a[2]"/"a[3];
    sz[key]+=$3
  }
  END {
    for (k in sz) printf "%d\t%s\n", sz[k], k
  }' \
| sort -nr \
| sed -n '1,30p'
```

## Current Recommendation

The offload thread should treat `raw/...` as the first thing to externalize.
The best practical order is:

1. offload the energy and basic-materials SEC plus IR raw trees
2. offload the heavier technology and consumer raw trees
3. leave extracted research and index interpretation in Git
4. come back with a Drive manifest commit and a lighter `main` push strategy

## Short Message To Forward To The Other CLI Thread

Use `/home/manishmehta/ui-projects/annual-report-research/notes/rclone-raw-blob-offload-handoff-2026-08-10.md`.

You should offload heavy `raw/sec`, `raw/company-ir`, and `raw/annualreports` content to Google Drive with `rclone`, starting with energy, basic materials, technology, and consumer-goods buckets.

Do not touch `extracted/`, `indexes/`, `notes/`, `analysis/`, or `site/`.

Hand back:
- Drive root URL
- manifest commit hash
- list of uploaded paths
- list of payload paths removed from Git
- any rewrite branch or force-push instructions

## Handoff Target

If another CLI thread is doing the upload, point it at:
- this note
- local `main` at `d4399b73352969136da747a2623c25f9f5de64ff`
- remote `origin/main` at `e01474ea345bf8d24c79c1e8ebfd9a4cc4fa1519`

The core job is:
- move heavy `raw/...` evidence out to Drive
- preserve repo-resident extracted synthesis
- return a manifest-and-link structure that lets this repo push cleanly
