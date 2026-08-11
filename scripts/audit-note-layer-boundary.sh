#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

report_path=""
json_path=""
if [[ "${1:-}" == "--write-report" ]]; then
  report_path="${2:-}"
  if [[ -z "$report_path" ]]; then
    printf 'usage: %s [--write-report path]\n' "${BASH_SOURCE[0]}" >&2
    exit 1
  fi
fi
if [[ "${1:-}" == "--write-json" ]]; then
  json_path="${2:-}"
  if [[ -z "$json_path" ]]; then
    printf 'usage: %s [--write-json path]\n' "${BASH_SOURCE[0]}" >&2
    exit 1
  fi
fi
if [[ "${1:-}" == "--write-artifacts" ]]; then
  report_path="${2:-}"
  json_path="${3:-}"
  if [[ -z "$report_path" || -z "$json_path" ]]; then
    printf 'usage: %s --write-artifacts report_path json_path\n' "${BASH_SOURCE[0]}" >&2
    exit 1
  fi
fi

reusable_manifest="indexes/reusable-note-layer-files-2026-08-11.txt"
historical_manifest="indexes/historical-note-exclusion-files-2026-08-11.txt"
historical_category_manifest="indexes/historical-note-exclusion-categories-2026-08-11.tsv"
maintenance_commands=(
  "bash scripts/run-insight-audit-stack.sh"
  "bash scripts/refresh-note-layer-boundary.sh"
  "bash scripts/audit-audit-stack-terminology.sh"
  "bash scripts/audit-maintenance-doc-stack.sh"
  "bash scripts/audit-reusable-note-maintenance-visibility.sh"
  "bash scripts/audit-continuation-mode-links.sh"
  "bash scripts/audit-remaining-brief-links.sh"
  "bash scripts/audit-remaining-stack-links.sh"
  "bash scripts/audit-browser-review-links.sh"
  "bash scripts/verify-insight-system.sh"
)

mapfile -t reusable < <(rg -v '^\s*(#|$)' "$reusable_manifest" | sort)
mapfile -t historical < <(rg -v '^\s*(#|$)' "$historical_manifest" | sort)
mapfile -t notes_files < <(find notes -maxdepth 1 -name '*.md' | sort)
mapfile -t union < <(printf '%s\n' "${reusable[@]}" "${historical[@]}" | sort -u)
mapfile -t historical_categories < <(tail -n +2 "$historical_category_manifest")
historical_with_both_sections=()
reusable_without_maintenance_commands=()
historical_with_maintenance_commands=()
mapfile -t historical_category_paths < <(printf '%s\n' "${historical_categories[@]}" | cut -f1 | sort)

for path in "${reusable[@]}"; do
  has_maintenance_command=0
  for command in "${maintenance_commands[@]}"; do
    if rg -qF "$command" "$path"; then
      has_maintenance_command=1
      break
    fi
  done
  if [[ "$has_maintenance_command" -eq 0 ]]; then
    reusable_without_maintenance_commands+=("$path")
  fi
done

for path in "${historical[@]}"; do
  if rg -q '^## Packet Inputs Used' "$path" && rg -q '^## Skeptical Reader Test' "$path"; then
    historical_with_both_sections+=("$path")
  fi
  for command in "${maintenance_commands[@]}"; do
    if rg -qF "$command" "$path"; then
      historical_with_maintenance_commands+=("$path")
      break
    fi
  done
done

printf 'note-layer-boundary-audit\n'
printf 'date %s\n' "2026-08-11"
printf 'notes_total %s\n' "${#notes_files[@]}"
printf 'reusable_total %s\n' "${#reusable[@]}"
printf 'historical_total %s\n' "${#historical[@]}"
printf 'manifest_union_total %s\n' "${#union[@]}"
printf 'historical_handoff %s\n' "$(printf '%s\n' "${historical_categories[@]}" | rg -c $'\thandoff$')"
printf 'historical_log %s\n' "$(printf '%s\n' "${historical_categories[@]}" | rg -c $'\tlog$')"
printf 'historical_raw_blob_rclone %s\n' "$(printf '%s\n' "${historical_categories[@]}" | rg -c $'\traw_blob_rclone$')"
printf 'historical_other %s\n' "$(printf '%s\n' "${historical_categories[@]}" | rg -c $'\tother$')"
printf 'historical_with_both_sections %s\n' "${#historical_with_both_sections[@]}"
printf 'reusable_without_maintenance_commands %s\n' "${#reusable_without_maintenance_commands[@]}"
printf 'historical_with_maintenance_commands %s\n' "${#historical_with_maintenance_commands[@]}"

missing_from_manifests="$(comm -23 <(printf '%s\n' "${notes_files[@]}") <(printf '%s\n' "${union[@]}"))"
stale_manifest_entries="$(comm -13 <(printf '%s\n' "${notes_files[@]}") <(printf '%s\n' "${union[@]}"))"

if [[ -n "$missing_from_manifests" ]]; then
  printf 'missing_from_manifests\n%s\n' "$missing_from_manifests" >&2
  exit 1
fi

if [[ -n "$stale_manifest_entries" ]]; then
  printf 'stale_manifest_entries\n%s\n' "$stale_manifest_entries" >&2
  exit 1
fi

if [[ "${#union[@]}" -ne "${#notes_files[@]}" ]]; then
  printf 'count_mismatch union=%s notes=%s\n' "${#union[@]}" "${#notes_files[@]}" >&2
  exit 1
fi

if [[ "${#historical_category_paths[@]}" -ne "${#historical[@]}" ]]; then
  printf 'historical_category_count_mismatch categories=%s historical=%s\n' "${#historical_category_paths[@]}" "${#historical[@]}" >&2
  exit 1
fi

missing_historical_categories="$(comm -23 <(printf '%s\n' "${historical[@]}") <(printf '%s\n' "${historical_category_paths[@]}"))"
stale_historical_categories="$(comm -13 <(printf '%s\n' "${historical[@]}") <(printf '%s\n' "${historical_category_paths[@]}"))"

if [[ -n "$missing_historical_categories" ]]; then
  printf 'missing_historical_categories\n%s\n' "$missing_historical_categories" >&2
  exit 1
fi

if [[ -n "$stale_historical_categories" ]]; then
  printf 'stale_historical_categories\n%s\n' "$stale_historical_categories" >&2
  exit 1
fi

if printf '%s\n' "${historical_categories[@]}" | cut -f2 | rg -qv '^(handoff|log|raw_blob_rclone|other)$'; then
  printf 'invalid_historical_category_detected\n' >&2
  exit 1
fi

if [[ "${#historical_with_both_sections[@]}" -ne 0 ]]; then
  printf 'historical_notes_with_both_sections\n%s\n' "$(printf '%s\n' "${historical_with_both_sections[@]}")" >&2
  exit 1
fi

if [[ "${#reusable_without_maintenance_commands[@]}" -ne 0 ]]; then
  printf 'reusable_notes_without_maintenance_commands\n%s\n' "$(printf '%s\n' "${reusable_without_maintenance_commands[@]}")" >&2
  exit 1
fi

if [[ "${#historical_with_maintenance_commands[@]}" -ne 0 ]]; then
  printf 'historical_notes_with_maintenance_commands\n%s\n' "$(printf '%s\n' "${historical_with_maintenance_commands[@]}")" >&2
  exit 1
fi

if [[ -n "$report_path" ]]; then
  cat >"$report_path" <<EOF
# Note Layer Boundary Audit

Date: 2026-08-11
Repo: \`annual-report-research\`

## Packet Inputs Used

- \`indexes/reusable-note-layer-files-2026-08-11.txt\`
- \`indexes/historical-note-exclusion-files-2026-08-11.txt\`
- \`indexes/historical-note-exclusion-categories-2026-08-11.tsv\`
- the current top-level \`notes/*.md\` inventory
- the current reusable-note and historical-note boundary rules enforced by \`scripts/audit-note-layer-boundary.sh\`

## Current Counts

| Metric | Value |
|---|---:|
| Top-level note files | ${#notes_files[@]} |
| Reusable note files | ${#reusable[@]} |
| Historical note files | ${#historical[@]} |
| Manifest union total | ${#union[@]} |
| Historical handoff files | $(printf '%s\n' "${historical_categories[@]}" | rg -c $'\thandoff$') |
| Historical log files | $(printf '%s\n' "${historical_categories[@]}" | rg -c $'\tlog$') |
| Historical raw/blob/rclone files | $(printf '%s\n' "${historical_categories[@]}" | rg -c $'\traw_blob_rclone$') |
| Historical other files | $(printf '%s\n' "${historical_categories[@]}" | rg -c $'\tother$') |
| Historical files with both standardized sections | ${#historical_with_both_sections[@]} |
| Reusable files without maintenance-surface commands | ${#reusable_without_maintenance_commands[@]} |
| Historical files with maintenance-surface commands | ${#historical_with_maintenance_commands[@]} |

## Boundary Status

- reusable and historical manifests together cover every current top-level note file
- the historical category manifest matches the historical exclusion file list
- no historically excluded note currently contains both standardized sections
- every reusable note currently exposes at least one maintenance-surface command reference
- no historically excluded note currently carries maintenance-surface command references
- the boundary audit completed with \`boundary_ok\`

## Key Inputs

- [Reusable note manifest](../indexes/reusable-note-layer-files-2026-08-11.txt)
- [Historical note manifest](../indexes/historical-note-exclusion-files-2026-08-11.txt)
- [Historical note categories](../indexes/historical-note-exclusion-categories-2026-08-11.tsv)
- [Cutoff note](insight-note-standardization-cutoff-2026-08-11.md)

## Insight-System Maintenance

When you need to confirm that this boundary audit, the reusable-note manifest, and the broader continuation surfaces still line up before relying on this report, use:

- \`bash scripts/run-insight-audit-stack.sh\`
- \`bash scripts/refresh-note-layer-boundary.sh\`
- \`bash scripts/audit-audit-stack-terminology.sh\`
- \`bash scripts/audit-maintenance-doc-stack.sh\`
- \`bash scripts/audit-reusable-note-maintenance-visibility.sh\`
- \`bash scripts/audit-historical-note-maintenance-isolation.sh\`
- \`bash scripts/audit-continuation-mode-links.sh\`
- \`bash scripts/audit-remaining-brief-links.sh\`
- \`bash scripts/audit-remaining-stack-links.sh\`
- \`bash scripts/audit-browser-review-links.sh\`
- \`bash scripts/verify-insight-system.sh\`

## Skeptical Reader Test

- Does this report state the exact current note counts on both sides of the boundary?
- Can a skeptical reader tell whether the manifests fully cover the current top-level note inventory?
- Does the report make historical-note subcategories explicit without relying on filename heuristics alone?
- What future note-layer change would require regenerating this report or moving files between manifests?
EOF
fi

if [[ -n "$json_path" ]]; then
  cat >"$json_path" <<EOF
{
  "date": "2026-08-11",
  "repo": "annual-report-research",
  "notes_total": ${#notes_files[@]},
  "reusable_total": ${#reusable[@]},
  "historical_total": ${#historical[@]},
  "manifest_union_total": ${#union[@]},
  "historical_counts": {
    "handoff": $(printf '%s\n' "${historical_categories[@]}" | rg -c $'\thandoff$'),
    "log": $(printf '%s\n' "${historical_categories[@]}" | rg -c $'\tlog$'),
    "raw_blob_rclone": $(printf '%s\n' "${historical_categories[@]}" | rg -c $'\traw_blob_rclone$'),
    "other": $(printf '%s\n' "${historical_categories[@]}" | rg -c $'\tother$')
  },
  "historical_with_both_sections": ${#historical_with_both_sections[@]},
  "reusable_without_maintenance_commands": ${#reusable_without_maintenance_commands[@]},
  "historical_with_maintenance_commands": ${#historical_with_maintenance_commands[@]},
  "boundary_ok": true,
  "reusable_manifest": "$reusable_manifest",
  "historical_manifest": "$historical_manifest",
  "historical_category_manifest": "$historical_category_manifest"
}
EOF
fi

printf 'boundary_ok\n'
