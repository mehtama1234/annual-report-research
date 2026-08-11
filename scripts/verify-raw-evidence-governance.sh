#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

json_report="notes/legacy-root-reference-audit-2026-08-11.json"
audit_note="notes/legacy-root-reference-audit-2026-08-11.md"
policy_note="notes/raw-evidence-link-policy-2026-08-11.md"
offload_readme="notes/raw-blob-offload-readme-2026-08-10.md"
manifest="indexes/raw-blob-offload-manifest-2026-08-10.csv"
top_files_tsv="indexes/legacy-root-raw-reference-top-files-2026-08-11.tsv"
resolver="scripts/resolve-offloaded-raw-path.py"
audit_script="scripts/audit-legacy-root-references.sh"
start_here="START-HERE.md"

required_files=(
  "$json_report"
  "$audit_note"
  "$policy_note"
  "$offload_readme"
  "$manifest"
  "$top_files_tsv"
  "$resolver"
  "$audit_script"
  "$start_here"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "missing required file: $file" >&2
    exit 1
  fi
done

legacy_root="$(python3 - <<'PY'
import json
from pathlib import Path
data = json.loads(Path("notes/legacy-root-reference-audit-2026-08-11.json").read_text())
print(data["legacy_root"])
PY
)"

json_all="$(python3 - <<'PY'
import json
from pathlib import Path
data = json.loads(Path("notes/legacy-root-reference-audit-2026-08-11.json").read_text())
print(data["all_markdown_files"])
PY
)"

json_raw="$(python3 - <<'PY'
import json
from pathlib import Path
data = json.loads(Path("notes/legacy-root-reference-audit-2026-08-11.json").read_text())
print(data["raw_evidence_files"])
PY
)"

json_hist="$(python3 - <<'PY'
import json
from pathlib import Path
data = json.loads(Path("notes/legacy-root-reference-audit-2026-08-11.json").read_text())
print(data["historical_or_nonraw_files"])
PY
)"

live_all="$(rg -l "${legacy_root}" . --glob '*.md' | wc -l | tr -d ' ')"
live_raw="$(rg -l "${legacy_root}/raw/" . --glob '*.md' | wc -l | tr -d ' ')"
live_hist="$((live_all - live_raw))"

if [[ "$json_all" != "$live_all" ]]; then
  echo "all_markdown_files mismatch: json=$json_all live=$live_all" >&2
  exit 1
fi

if [[ "$json_raw" != "$live_raw" ]]; then
  echo "raw_evidence_files mismatch: json=$json_raw live=$live_raw" >&2
  exit 1
fi

if [[ "$json_hist" != "$live_hist" ]]; then
  echo "historical_or_nonraw_files mismatch: json=$json_hist live=$live_hist" >&2
  exit 1
fi

if ! grep -q "count	path" "$top_files_tsv"; then
  echo "top-files TSV missing header" >&2
  exit 1
fi

sample_url="$(python3 "$resolver" --url-only 'raw/sec/healthcare/medical-distribution/cencora/2026-q2-10q.html')"
if [[ "$sample_url" != https://drive.google.com/open?id=* ]]; then
  echo "resolver did not return expected Drive URL" >&2
  exit 1
fi

if ! rg -q "resolve-offloaded-raw-path.py" "$start_here" "$policy_note" "$offload_readme"; then
  echo "resolver guidance missing from operator docs" >&2
  exit 1
fi

if ! rg -q "audit-legacy-root-references.sh" "$start_here" "$audit_note"; then
  echo "audit script guidance missing from operator docs" >&2
  exit 1
fi

echo "raw-evidence-governance-ok"
