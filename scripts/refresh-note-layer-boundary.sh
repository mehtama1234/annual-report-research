#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

report_path="notes/note-layer-boundary-audit-2026-08-11.md"
json_path="notes/note-layer-boundary-audit-2026-08-11.json"

bash scripts/audit-note-layer-boundary.sh --write-artifacts "$report_path" "$json_path"
bash scripts/audit-note-layer-boundary.sh
bash scripts/audit-audit-stack-terminology.sh
bash scripts/audit-maintenance-doc-stack.sh
bash scripts/audit-continuation-mode-links.sh
bash scripts/audit-browser-review-links.sh
bash scripts/verify-insight-system.sh
