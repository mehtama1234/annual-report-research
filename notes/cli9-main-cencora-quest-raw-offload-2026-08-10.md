# CLI9 Main Cencora / Quest Raw Offload - 2026-08-10

This note records a cleanup offload for Cencora and Quest raw evidence paths that were present in remote `main`.

The extracted research packets stay in git. The raw evidence payload is preserved in Google Drive and removed from the current git tree by the companion cleanup commit.

## Git status before cleanup

- Canonical repo: `/home/manishmehta/ui-projects/annual-report-research`
- Remote main before cleanup note: `88c4afe746f4f3a9ce7d5f07a106c8277a56ae51`
- Cencora / Quest raw paths tracked in `origin/main`: `58`
- Tracked raw payload bytes: `7364970`

Tracked raw families removed from the current tree:

- `raw/annualreports/healthcare/drug-stores/cencora-inc/`
- `raw/company-ir/healthcare/drug-stores/cencora-inc/`
- `raw/sec/healthcare/drug-stores/cencora-inc/`
- `raw/annualreports/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/`
- `raw/company-ir/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/`
- `raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/`

## Google Drive offload

- Drive folder path: `gdrive:annual-report-research/raw-blob-offloads/cli9-main-cencora-quest-raw-offload-2026-08-10`
- Drive folder link: `https://drive.google.com/open?id=1PSNfH2M4hYJEOYh9voNMlPm6_F2iV_qj`
- Tar object: `cli9-main-cencora-quest-raw-offload-2026-08-10.tar`
- Tar Drive ID: `1k0BKcJkIWCRR2lqgO08NxeXtN1QPFIVg`
- Tar size: `7424000` bytes
- Tar SHA256: `354b4dd83c14f0bcd587d973381bba1cc265966231fe320be19f745f5666cf2b`
- Checksum object: `cli9-main-cencora-quest-raw-offload-2026-08-10.tar.sha256`
- Checksum Drive ID: `1gD_2VLf7lmk_Um1W3h24T9xiWXDHe7nz`
- Raw path list object: `raw-paths.txt`
- Raw path list Drive ID: `1U5pM0Q1WtrpfsqZZulsMigho2gSQFIct`

## Restore commands

```bash
rclone copy gdrive:annual-report-research/raw-blob-offloads/cli9-main-cencora-quest-raw-offload-2026-08-10 .
sha256sum -c cli9-main-cencora-quest-raw-offload-2026-08-10.tar.sha256
tar -xf cli9-main-cencora-quest-raw-offload-2026-08-10.tar
```
