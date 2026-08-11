# Raw Blob Offload Readme

Date: 2026-08-10

Purpose: preserve the local-only heavy `raw/**` payload outside Git while keeping extracted research, indexes, notes, analysis, and site outputs in remote `main`.

## Packet Inputs Used

- the local raw-delta audit that identified which `raw/**` files were too heavy to keep on remote `main`
- the Google Drive offload location, tar artifact, checksum artifact, and manifest files that preserve recoverability outside Git
- the staged text redaction scan and summary that document the security pass before upload
- the Git-manifest strategy that keeps extracted research, indexes, notes, analysis, and site outputs on `main` while excluding heavy raw payloads
- the repo-offload requirement that another worker should be able to understand what was moved, where it lives, and how it relates to the local commit context

## Scope

- Source repo: `/home/manishmehta/ui-projects/annual-report-research`
- Base remote commit: `738321d8129930e02138cda17c659fbe227b857f`
- Local raw delta commit context: `e5d5efa846beedddd7bfb81341253b4e94f89f0f`
- Raw paths offloaded: `2,172`
- Payload bytes after staged text redaction: `2,386,047,551`
- Drive upload size: `2.228 GiB` / `2,392,504,449` bytes

## Drive Location

- Drive folder path: `gdrive:annual-report-research/raw-blob-offloads/local-main-delta-2026-08-10`
- Tar object: `annual-report-raw-blob-offload-local-main-delta-2026-08-10.tar`
- Tar Drive link: `https://drive.google.com/open?id=1ELztJl2JIwWl24jVkDRnCb-snJBqQTR0`
- Checksum object: `annual-report-raw-blob-offload-local-main-delta-2026-08-10.tar.sha256`
- Checksum Drive link: `https://drive.google.com/open?id=1M-POBbhBvh2IuNO7L1tdMVFQ7T7gGZce`

Tar SHA256:

```text
dead29400e6cd4e5a097b09946638d7d1eec6e50aad3680e79649b18a8ed608c  annual-report-raw-blob-offload-local-main-delta-2026-08-10.tar
```

## Additional CLI9 Healthcare Frontier Offload

- Source repo: `/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers`
- Research snapshot commit with raw payload: `f33ef0de362c99d51ba63e9ce3b3c9ad79598738`
- Raw paths offloaded: `37`
- Drive upload size: `16,005,120` bytes
- Drive folder path: `gdrive:annual-report-research/raw-blob-offloads/cli9-healthcare-delta-2026-08-10`
- Tar object: `annual-report-raw-blob-offload-cli9-healthcare-2026-08-10.tar`
- Tar Drive link: `https://drive.google.com/open?id=10w1-i7gNkhzOPvVdNRm-Bs049tv1Mf0p`
- Checksum object: `annual-report-raw-blob-offload-cli9-healthcare-2026-08-10.tar.sha256`
- Checksum Drive link: `https://drive.google.com/open?id=1imV6nFJMMllg6PksEGB2-1AycdtFp4Cn`

Tar SHA256:

```text
b4e682e6ef38743c738ab3814a7872c30665e9eda44df247f69e7cf08cbee92c  annual-report-raw-blob-offload-cli9-healthcare-2026-08-10.tar
```

This second archive covers the CLI9 healthcare frontier raw source set for:

- `raw/annualreports/healthcare/medical-distribution/`
- `raw/company-ir/healthcare/medical-distribution/`
- `raw/sec/healthcare/medical-distribution/`
- `raw/annualreports/healthcare/medical-laboratories-research/`
- `raw/company-ir/healthcare/medical-laboratories-research/`
- `raw/sec/healthcare/medical-laboratories-research/`

## Repo Manifest Files

- `indexes/raw-blob-offload-manifest-2026-08-10.csv`
- `indexes/raw-blob-offload-summary-2026-08-10.tsv`

The CSV is file-level. Each row records:

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

The `drive_url` points to the Drive tar object plus the internal `payload/...` path.

## Resolving packet evidence links

Many company packets, company profiles, and source ledgers still cite raw evidence by its original `raw/...` identity even though the heavy payload is no longer present in remote `main`.

Use:

```bash
python3 scripts/resolve-offloaded-raw-path.py 'raw/sec/healthcare/medical-distribution/cencora/2026-q2-10q.html'
```

That script reads `indexes/raw-blob-offload-manifest-2026-08-10.csv` and returns the matching `drive_url` plus the key manifest metadata.

For the broader interpretation standard, see:

- `notes/raw-evidence-link-policy-2026-08-11.md`

## Bucket Coverage

The offload covers the local-only raw delta across the heavy buckets called out in the handoff note, including:

- `raw/sec/energy`
- `raw/company-ir/energy`
- `raw/company-ir/basic-materials`
- `raw/sec/basic-materials`
- `raw/company-ir/technology`
- `raw/sec/consumer-goods`
- `raw/company-ir/consumer-goods`
- `raw/company-ir/financial`

## Redaction Audit

The repo working tree was not modified for redaction. Redaction was applied only to the staged upload copy before tar creation.

- Text-like staged files scanned: `1,660`
- Text-like staged files redacted: `13`
- Remaining token-pattern matches in text-like staged files: `0`

The tar includes:

- `redaction-targets.txt`
- `redaction-remaining.txt`
- `raw-delta-paths.txt`
- `raw-blob-offload-manifest-2026-08-10.csv`
- `raw-blob-offload-summary.tsv`

## Git Handling

The heavy raw payload itself remains excluded from remote `main`. This readme, the CSV manifest, and the TSV bucket summary are the lightweight Git pointers for the Drive offload.

Manifest commit: `26dae821618ab0d556dbc364970762480a811086`

## Skeptical Reader Test

- Does this readme identify exactly what was offloaded, where it was uploaded, and which lightweight manifest files remain in Git?
- Can a skeptical reader verify that a redaction pass occurred before the raw tar was uploaded?
- Does the note make the separation between remote `main` and local heavy raw evidence explicit enough for another worker to trust the storage model?
- What missing manifest, checksum, or commit-context detail would make the offload hard to audit?
