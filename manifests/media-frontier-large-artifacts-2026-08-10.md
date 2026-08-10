# Media Frontier Large Artifact Manifest

Date: 2026-08-10

Frontier: media, influence, consumer interface, and edge infrastructure

## Git Research Package

- Remote-safe `main` package commit before this manifest: `32c31e8b69c55c84f6726acaa8eb1d7186d71a48`
- Slim archive branch: `media-frontier-archive`
- Slim archive commit: `dbac89d9b85e8f6d1fdb24c2256b388951322e7d`

## Google Drive Artifact Location

- Remote: `gdrive:`
- Folder: `annual-report-research/media-influence-consumer-interface-edge-infrastructure/raw-sec-and-large-artifacts-2026-08-10`
- Verified uploaded objects: `2`
- Verified uploaded size: `4.380 GiB` / `4,702,822,526` bytes

Uploaded objects:

- `annual-report-large-artifacts-media-frontier-2026-08-10.tar`
- `annual-report-large-artifacts-media-frontier-2026-08-10.tar.sha256`

Archive checksum:

```text
1b2634c8bb148c5ab4b82c7bb65835151cce590671cc5d54accfd5b43c0932b4  annual-report-large-artifacts-media-frontier-2026-08-10.tar
```

## Local Staging Source

- Staged folder: `/home/manishmehta/ui-projects/annual-report-large-artifacts-media-frontier-2026-08-10`
- Staged folder size before tar: `4.4G`
- Staged file count before tar: `3,729`
- Tar path: `/home/manishmehta/ui-projects/annual-report-large-artifacts-media-frontier-2026-08-10.tar`
- Tar checksum path: `/home/manishmehta/ui-projects/annual-report-large-artifacts-media-frontier-2026-08-10.tar.sha256`

Included raw roots:

- `raw/sec/`
- `raw/company-ir/`
- `raw/annualreports/`

## Redaction Audit

Before upload, the staged artifact copy was scanned for token-like patterns and redacted in place.

- Redacted files: `53`
- Remaining matches after redaction: `0`
- Local audit files inside the tar:
  - `redaction-targets.txt`
  - `redaction-remaining.txt`

## Notes

The Drive artifact is intentionally stored as a tar archive instead of loose files. A direct file-by-file Drive upload was started, but Drive throughput bottlenecked on thousands of small files. Loose partial objects were removed from the Drive destination, and the verified final destination contains only the tar archive and its checksum file.
