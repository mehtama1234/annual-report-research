## CLI4 Raw Blob Offload Handoff

Date: 2026-08-10

Purpose:
- hand the remaining CLI4 raw evidence payload to the rclone / Google Drive offload thread
- keep the research outputs already pushed to `origin/main`
- avoid pushing the full raw archive history through GitHub regular Git

## Current State

- repo: `/home/manishmehta/ui-projects/annual-report-research`
- source branch with raw payload: `cli4-healthcare-frontier-batch`
- branch tip when scoped: `00da1581b5e0ff9bca9eb2db9dcc90aec0352ac7`
- remote `origin/main` after research-output integration: `e01474ea345bf8d24c79c1e8ebfd9a4cc4fa1519`
- pushed research-output commit: `e01474ea345bf8d24c79c1e8ebfd9a4cc4fa1519`
- pushed paths from CLI4 scope: `extracted/`, `indexes/`, `notes/`
- intentionally excluded from that push: new `raw/...` payloads from `origin/main..cli4-healthcare-frontier-batch`

The useful packets, indexes, and notes are on `origin/main`. The remaining work is only raw evidence transport and pointering.

## Why Offload Is Required

GitHub documents:
- regular GitHub repositories block individual files larger than `100 MiB`
- GitHub enforces a `2 GiB` maximum single push size
- large files should use Git LFS or an external distribution path

The remaining CLI4 raw payload does not appear to have a single `>100 MiB` blob, but it does add about `2.97 GiB` of raw blobs, which is over the single-push limit.

Measured remaining payload in:

```bash
origin/main..cli4-healthcare-frontier-batch
```

- raw blobs: `3,676`
- raw bytes: `3,190,513,606`
- raw MiB: `3,042.7`
- raw GiB: `2.97`
- blobs over `10 MB`: `47`

## Scope For Rclone Thread

Offload only heavy raw evidence trees:
- `raw/sec/...`
- `raw/company-ir/...`
- `raw/annualreports/...`

Do not touch:
- `extracted/`
- `indexes/`
- `notes/`
- `analysis/`
- `site/`

Those repo-resident research outputs are already on `origin/main` and should remain ordinary Git content.

## Highest-Priority Buckets

Bucket totals from `origin/main..cli4-healthcare-frontier-batch`, format: `bytes files path`.

```text
539038470 364 raw/sec/energy
419811754 383 raw/company-ir/energy
357753105 296 raw/company-ir/basic-materials
262646670 254 raw/sec/basic-materials
251955288 290 raw/sec/industrial-goods
239916354 290 raw/sec/services
220839134 250 raw/sec/technology
186988567 195 raw/sec/consumer-goods
161289532 224 raw/company-ir/technology
132238874 162 raw/company-ir/consumer-goods
97606092 169 raw/sec/healthcare
86354713 145 raw/company-ir/industrial-goods
84971240 184 raw/company-ir/services
43906879 48 raw/annualreports/basic-materials
29290870 68 raw/company-ir/healthcare
24413038 7 raw/sec/real-estate
20273793 19 raw/sec/utilities
13010286 80 raw/annualreports/energy
```

Recommended first pass:
1. `raw/sec/energy`
2. `raw/company-ir/energy`
3. `raw/company-ir/basic-materials`
4. `raw/sec/basic-materials`
5. `raw/sec/industrial-goods`
6. `raw/sec/services`
7. `raw/sec/technology`
8. `raw/sec/consumer-goods`

## Largest Remaining Raw Blobs

Format: `bytes path`.

```text
53477876 raw/sec/energy/independent-oil-gas/matador-resources-co/2025-annual-report-ars.pdf
40854951 raw/annualreports/basic-materials/gold/kinross-gold-corporation/2025-annual-report.pdf
38972688 raw/sec/industrial-goods/wholesale-other/pool-corp/2025-annual-report.pdf
38211788 raw/sec/industrial-goods/management-services/korn-ferry/2025-annual-report-ars.pdf
32323962 raw/company-ir/energy/independent-oil-gas/matador-resources-co/2025-annual-report.pdf
28811387 raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2025-annual-report.pdf
28452625 raw/company-ir/technology/internet-service-providers/etsy-inc/2026-q1-shareholder-letter.pdf
24692666 raw/sec/basic-materials/industrial-metals-minerals/rio-tinto-plc/2025-20f.html
23922637 raw/company-ir/basic-materials/industrial-metals-minerals/hudbay-minerals-inc/2025-annual-report.pdf
21556305 raw/company-ir/technology/internet-service-providers/etsy-inc/2026-q2-shareholder-letter.pdf
21478259 raw/sec/energy/independent-oil-gas/diamondback-energy-inc/2025-annual-report-ars.pdf
21330410 raw/company-ir/basic-materials/copper/first-quantum-minerals-ltd/2025-annual-report.pdf
19184290 raw/sec/energy/independent-oil-gas/permian-resources-corporation/2025-annual-report-ars.pdf
18124207 raw/company-ir/basic-materials/copper/first-quantum-minerals-ltd/q1-2026-investor-deck.pdf
17826855 raw/company-ir/energy/oil-gas-refining-marketing/imperial-oil-limited/2025-annual-report.pdf
17791479 raw/company-ir/energy/oil-gas-pipelines/williams-companies-inc/2025-annual-report.pdf
17770303 raw/company-ir/services/lodging/hyatt-hotels-corporation/2025-annual-report.pdf
17562170 raw/company-ir/basic-materials/gold/newmont-corporation/2025-annual-report.pdf
17555179 raw/company-ir/industrial-goods/security-protection-services/the-geo-group/fy2025-annual-report.pdf
17443970 raw/sec/industrial-goods/rental-leasing-services/herc-holdings-inc/2025-annual-report.pdf
```

## Expected Google Drive Layout

Mirror repo paths under one Drive root:

```text
annual-report-research/raw/sec/...
annual-report-research/raw/company-ir/...
annual-report-research/raw/annualreports/...
```

The rclone thread should return the Drive root URL and any share/access notes.

## Manifest Deliverable

Create a manifest commit on top of current `main` after upload. Suggested file:

```text
indexes/cli4-raw-blob-offload-manifest-2026-08-10.csv
```

Recommended columns:
- `local_path`
- `drive_path`
- `drive_url`
- `bytes`
- `sha256`
- `source_family`
- `sector`
- `industry`
- `company_slug`
- `document_name`
- `branch_source`
- `source_commit`
- `notes`

`source_family` should be one of:
- `annualreports`
- `company-ir`
- `sec`

`branch_source` should be `cli4-healthcare-frontier-batch`.

`source_commit` should be `00da1581b5e0ff9bca9eb2db9dcc90aec0352ac7` unless the source branch advances and the rclone thread intentionally resyncs.

## Upload And Removal Expectations

The rclone thread should:
1. upload selected `raw/...` files or whole raw buckets to Drive
2. compute `sha256` for every uploaded file
3. write the manifest rows
4. remove those raw payloads from the Git push path or leave them untracked locally
5. commit only the manifest / pointer files
6. hand back the Drive root URL and manifest commit hash

Do not rewrite or remove already-pushed research outputs.

## Commands To Recompute Scope

Raw payload total:

```bash
repo=/home/manishmehta/ui-projects/annual-report-research
git -C "$repo" rev-list --objects origin/main..cli4-healthcare-frontier-batch \
| git -C "$repo" cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
| awk '$1=="blob" && $4 ~ /^raw\\// {
    sum+=$3; count++; if ($3>10000000) big++
  }
  END {
    printf "raw_blobs=%d raw_bytes=%d raw_mib=%.1f raw_gib=%.2f big_gt_10mb=%d\n",
      count, sum, sum/1024/1024, sum/1024/1024/1024, big
  }'
```

Bucket totals:

```bash
repo=/home/manishmehta/ui-projects/annual-report-research
git -C "$repo" rev-list --objects origin/main..cli4-healthcare-frontier-batch \
| git -C "$repo" cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
| awk '$1=="blob" && $4 ~ /^raw\\// {
    split($4,a,"/");
    key=a[1]"/"a[2]"/"a[3];
    sz[key]+=$3; ct[key]++
  }
  END {
    for (k in sz) printf "%d %d %s\n", sz[k], ct[k], k
  }' \
| sort -nr \
| sed -n '1,40p'
```

Largest raw blobs:

```bash
repo=/home/manishmehta/ui-projects/annual-report-research
git -C "$repo" rev-list --objects origin/main..cli4-healthcare-frontier-batch \
| git -C "$repo" cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \
| awk '$1=="blob" && $4 ~ /^raw\\// {print $3, $4}' \
| sort -nr \
| sed -n '1,40p'
```

## Handback Required

Return:
- Drive root URL
- manifest commit hash
- uploaded path list
- removed payload path list
- any skipped paths and why
- whether the source branch advanced beyond `00da1581`
- whether any history rewrite branch was created

## Short Prompt For The Rclone Thread

Use:

```text
notes/cli4-raw-blob-offload-handoff-2026-08-10.md
```

Offload only the remaining `raw/...` payload from `origin/main..cli4-healthcare-frontier-batch` to Google Drive with `rclone`. The research outputs from this branch were already integrated to `origin/main` in commit `e01474ea345bf8d24c79c1e8ebfd9a4cc4fa1519`, so do not touch `extracted/`, `indexes/`, `notes/`, `analysis/`, or `site/` except to add the offload manifest. Return the Drive root URL, manifest commit hash, uploaded paths, removed payload paths, and any rewrite instructions.
