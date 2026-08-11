# Main Tracked Raw Offload - 2026-08-10

This note records the comprehensive offload of every `raw/**` file tracked in the current `main` tree after the Cencora / Quest cleanup.

The purpose is to make the current remote `main` tree text-first: extracted packets, indexes, notes, analysis, templates, and other lightweight research artifacts stay in git; raw filing payloads live in Google Drive.

## Git state before cleanup

- Canonical repo: `/home/manishmehta/ui-projects/annual-report-research`
- Base commit before this cleanup: `ff36c5fc911e9a71a7ee2f62f14bfd62084462aa`
- Tracked `raw/**` files: `5449`
- Tracked `raw/**` payload bytes: `6133762130`
- Local raw path list: `/tmp/main-tracked-raw-all-2026-08-10.txt`

## Google Drive offload

- Drive folder path: `gdrive:annual-report-research/raw-blob-offloads/main-tracked-raw-offload-2026-08-10`
- Drive folder link: `https://drive.google.com/open?id=12DymUP2sr-ELrYpx_PNXwFeDvW0IsuRN`
- Local tar: `/home/manishmehta/ui-projects/main-tracked-raw-offload-2026-08-10/main-tracked-raw-offload-2026-08-10.tar`
- Tar SHA256: `4a08b31e7ea8ab96b188bb2a614f54ee94c4097dcfd61c2e9118a27e3fbf1022`
- Uploaded split directory: `/home/manishmehta/ui-projects/main-tracked-raw-offload-2026-08-10-parts7m-1786420142`
- Uploaded part files: `837`
- Uploaded metadata/checksum files: `3`
- Verified Drive file count: `840`
- Verified Drive part payload bytes: `6139156480`
- Verified Drive total bytes including metadata/checksums: `6139751400`

Drive metadata objects:

- `main-tracked-raw-offload-2026-08-10.tar.sha256`: Drive ID `1XRA88i4bO8Yz8X2fhf8ohk4kbL_WX45D`
- `parts.sha256`: Drive ID `1PHs2DsiqXqlAGS3CKWzJHFQh-m_-s1pc`
- `raw-paths.txt`: Drive ID `1Wesfc1i93B84sgdZ9uxuyqMTfQO7IhZV`

Boundary part objects:

- First part, `main-tracked-raw-offload-2026-08-10.tar.part-0000`: Drive ID `18UDyXgYadZL44QR1vOKxD73GLqMjvcEj`
- Last part, `main-tracked-raw-offload-2026-08-10.tar.part-0836`: Drive ID `1RV_L2pFiLNxNjRIaqJtwuRZd-qU3Iotz`

## Restore commands

From a local directory containing the Drive folder contents:

```bash
sha256sum -c parts.sha256
cat main-tracked-raw-offload-2026-08-10.tar.part-* > main-tracked-raw-offload-2026-08-10.tar
sha256sum -c main-tracked-raw-offload-2026-08-10.tar.sha256
tar -tf main-tracked-raw-offload-2026-08-10.tar >/dev/null
```

This archive is the authoritative current-tree raw payload for `main` as of the base commit above. Earlier narrower offload notes remain useful as provenance for specific integration batches, but this note is the broad cleanup checkpoint for the tracked raw tree.
