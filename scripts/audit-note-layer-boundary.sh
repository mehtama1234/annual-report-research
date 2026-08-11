#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

reusable_manifest="indexes/reusable-note-layer-files-2026-08-11.txt"
historical_manifest="indexes/historical-note-exclusion-files-2026-08-11.txt"
historical_category_manifest="indexes/historical-note-exclusion-categories-2026-08-11.tsv"

mapfile -t reusable < <(rg -v '^\s*(#|$)' "$reusable_manifest" | sort)
mapfile -t historical < <(rg -v '^\s*(#|$)' "$historical_manifest" | sort)
mapfile -t notes_files < <(find notes -maxdepth 1 -name '*.md' | sort)
mapfile -t union < <(printf '%s\n' "${reusable[@]}" "${historical[@]}" | sort -u)
mapfile -t historical_categories < <(tail -n +2 "$historical_category_manifest")
historical_with_both_sections=()
mapfile -t historical_category_paths < <(printf '%s\n' "${historical_categories[@]}" | cut -f1 | sort)

for path in "${historical[@]}"; do
  if rg -q '^## Packet Inputs Used' "$path" && rg -q '^## Skeptical Reader Test' "$path"; then
    historical_with_both_sections+=("$path")
  fi
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

printf 'boundary_ok\n'
