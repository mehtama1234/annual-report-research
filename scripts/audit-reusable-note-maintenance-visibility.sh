#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import sys

repo = Path.cwd()
manifest = repo / "indexes/reusable-note-layer-files-2026-08-11.txt"

commands = [
    "bash scripts/run-insight-audit-stack.sh",
    "bash scripts/refresh-note-layer-boundary.sh",
    "bash scripts/audit-audit-stack-terminology.sh",
    "bash scripts/audit-maintenance-doc-stack.sh",
    "bash scripts/audit-continuation-mode-links.sh",
    "bash scripts/audit-remaining-brief-links.sh",
    "bash scripts/audit-remaining-stack-links.sh",
    "bash scripts/audit-browser-review-links.sh",
    "bash scripts/verify-insight-system.sh",
]

files = [
    line.strip()
    for line in manifest.read_text().splitlines()
    if line.strip() and not line.lstrip().startswith("#")
]

missing = []
counts = []
for rel in files:
    path = repo / rel
    text = path.read_text()
    count = sum(command in text for command in commands)
    counts.append((rel, count))
    if count == 0:
        missing.append(rel)

print("reusable-note-maintenance-visibility-audit")
print(f"manifest {manifest.relative_to(repo).as_posix()}")
print(f"notes_checked {len(files)}")
print(f"zero_visibility_notes {len(missing)}")

if counts:
    min_visibility = min(count for _, count in counts)
    print(f"min_command_count {min_visibility}")

if missing:
    for rel in missing:
        print(rel, file=sys.stderr)
    sys.exit(1)

print("reusable_note_maintenance_visibility_ok")
PY
