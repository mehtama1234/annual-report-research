#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import sys

repo = Path.cwd()
manifest = repo / "indexes/historical-note-exclusion-files-2026-08-11.txt"

commands = [
    "bash scripts/run-insight-audit-stack.sh",
    "bash scripts/refresh-note-layer-boundary.sh",
    "bash scripts/audit-audit-stack-terminology.sh",
    "bash scripts/audit-maintenance-doc-stack.sh",
    "bash scripts/audit-reusable-note-maintenance-visibility.sh",
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

leaks = []
for rel in files:
    path = repo / rel
    text = path.read_text()
    matches = [command for command in commands if command in text]
    if matches:
        leaks.append((rel, matches))

print("historical-note-maintenance-isolation-audit")
print(f"manifest {manifest.relative_to(repo).as_posix()}")
print(f"notes_checked {len(files)}")
print(f"historical_notes_with_maintenance_commands {len(leaks)}")

if leaks:
    for rel, matches in leaks:
        print(rel, file=sys.stderr)
        for command in matches:
            print(f"  {command}", file=sys.stderr)
    sys.exit(1)

print("historical_note_maintenance_isolation_ok")
PY
