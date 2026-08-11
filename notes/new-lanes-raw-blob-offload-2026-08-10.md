# New Lanes Raw Blob Offload - 2026-08-10

This note records the raw-evidence offload for the new-lanes frontier research integration. The research outputs were integrated into git without `raw/**` payloads; the raw blob archive lives in Google Drive.

## Git integration

- Remote repository: `https://github.com/mehtama1234/annual-report-research.git`
- Integrated non-raw commit before this pointer note: `1ffb00e8bb29f2b71611acc4c9e9f39ab3b28bb1`
- Integration commit message: `Integrate new lanes frontier research`
- Source worktree: `/home/manishmehta/ui-projects/annual-report-research-new-lanes`
- Source raw tree: `/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw`
- Raw files in source tree: `4117`
- Source raw size: `4.9G`

## Google Drive offload

- Drive target: `gdrive:annual-report-research/raw-blob-offloads/new-lanes-raw-offload-2026-08-10`
- Drive folder link: `https://drive.google.com/open?id=1vLFP-iVzGUZ0ASFrTBtN6fP-KJeKXez_`
- Full local tar: `/home/manishmehta/ui-projects/new-lanes-raw-offload-2026-08-10.tar`
- Full tar size: `5223016711` bytes
- Full tar SHA256: `85fbc6053aff6e75e5b6a80b6916efb0e129fc94b4b6c42733bab2ffd7d37ace`
- Uploaded split directory: `/home/manishmehta/ui-projects/new-lanes-raw-offload-2026-08-10-parts7m-1786410743`
- Uploaded part files: `713`
- Uploaded checksum files: `2`
- Verified Drive file count: `715`
- Verified Drive part payload bytes: `5227560960`
- Verified Drive total bytes including checksums: `5227641662`

Checksum objects:

- `new-lanes-raw-offload-2026-08-10.tar.sha256`: Drive ID `1z4l2UNCoFPeRaGdlTTkYx286K74HuhcO`
- `parts.sha256`: Drive ID `1PwYs0wXOsc3h1c7waLkUo6Iiv4noky-p`

Boundary object IDs:

- First part, `new-lanes-raw-offload-2026-08-10.tar.part-0000`: Drive ID `1bJhFNC4TKmFIJvtxulTpAfRaySgYgLCu`
- Last part, `new-lanes-raw-offload-2026-08-10.tar.part-0712`: Drive ID `1ZRBAE2H1XVO_VufyfdwVgxQUcbOxIulI`

## Restore commands

From a local directory containing all `new-lanes-raw-offload-2026-08-10.tar.part-*` files and both checksum files:

```bash
sha256sum -c parts.sha256
cat new-lanes-raw-offload-2026-08-10.tar.part-* > new-lanes-raw-offload-2026-08-10.tar
sha256sum -c new-lanes-raw-offload-2026-08-10.tar.sha256
tar -tf new-lanes-raw-offload-2026-08-10.tar >/dev/null
```

The split archive was used because Drive/rclone repeatedly failed to finalize larger single-object uploads. Sub-8 MB split objects finalized successfully and are the authoritative offload payload.
