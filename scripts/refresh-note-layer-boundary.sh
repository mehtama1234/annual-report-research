#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

report_path="notes/note-layer-boundary-audit-2026-08-11.md"

bash scripts/audit-note-layer-boundary.sh --write-report "$report_path"
bash scripts/audit-note-layer-boundary.sh
bash scripts/verify-insight-system.sh
