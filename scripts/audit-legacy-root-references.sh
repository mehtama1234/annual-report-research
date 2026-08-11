#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
legacy_root="/home/manishmehta/ui-projects/annual-report-research-new-lanes"

all_files="$(mktemp)"
raw_files="$(mktemp)"
trap 'rm -f "$all_files" "$raw_files"' EXIT

rg -l "${legacy_root}" "${repo_root}" --glob '*.md' | sort > "${all_files}" || true
rg -l "${legacy_root}/raw/" "${repo_root}" --glob '*.md' | sort > "${raw_files}" || true

all_count="$(wc -l < "${all_files}" | tr -d ' ')"
raw_count="$(wc -l < "${raw_files}" | tr -d ' ')"
historical_count="$((all_count - raw_count))"

echo "legacy_root=${legacy_root}"
echo "all_markdown_files=${all_count}"
echo "raw_evidence_files=${raw_count}"
echo "historical_or_nonraw_files=${historical_count}"
echo
echo "[historical_or_nonraw]"
comm -23 "${all_files}" "${raw_files}" | sed "s#^${repo_root}/##"
echo
echo "[top_raw_evidence_files]"
rg -n "${legacy_root}/raw/" "${repo_root}" --glob '*.md' \
  | sed -E "s#^${repo_root}/##" \
  | cut -d: -f1 \
  | sort \
  | uniq -c \
  | sort -nr \
  | sed -n '1,40p'
