# Note Layer Boundary Audit

Date: 2026-08-11
Repo: `annual-report-research`

## Packet Inputs Used

- `indexes/reusable-note-layer-files-2026-08-11.txt`
- `indexes/historical-note-exclusion-files-2026-08-11.txt`
- `indexes/historical-note-exclusion-categories-2026-08-11.tsv`
- the current top-level `notes/*.md` inventory
- the current reusable-note and historical-note boundary rules enforced by `scripts/audit-note-layer-boundary.sh`

## Current Counts

| Metric | Value |
|---|---:|
| Top-level note files | 114 |
| Reusable note files | 51 |
| Historical note files | 63 |
| Manifest union total | 114 |
| Historical handoff files | 49 |
| Historical log files | 7 |
| Historical raw/blob/rclone files | 6 |
| Historical other files | 1 |
| Historical files with both standardized sections | 0 |

## Boundary Status

- reusable and historical manifests together cover every current top-level note file
- the historical category manifest matches the historical exclusion file list
- no historically excluded note currently contains both standardized sections
- the boundary audit completed with `boundary_ok`

## Key Inputs

- [Reusable note manifest](../indexes/reusable-note-layer-files-2026-08-11.txt)
- [Historical note manifest](../indexes/historical-note-exclusion-files-2026-08-11.txt)
- [Historical note categories](../indexes/historical-note-exclusion-categories-2026-08-11.tsv)
- [Cutoff note](insight-note-standardization-cutoff-2026-08-11.md)

## Skeptical Reader Test

- Does this report state the exact current note counts on both sides of the boundary?
- Can a skeptical reader tell whether the manifests fully cover the current top-level note inventory?
- Does the report make historical-note subcategories explicit without relying on filename heuristics alone?
- What future note-layer change would require regenerating this report or moving files between manifests?
