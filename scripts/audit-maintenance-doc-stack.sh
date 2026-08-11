#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import sys

repo = Path.cwd()

full_audit_stack = [
    "bash scripts/refresh-note-layer-boundary.sh",
    "bash scripts/audit-audit-stack-terminology.sh",
    "bash scripts/audit-continuation-mode-links.sh",
    "bash scripts/audit-browser-review-links.sh",
    "bash scripts/verify-insight-system.sh",
]
linked_audit_stack = [
    "bash scripts/audit-audit-stack-terminology.sh",
    "bash scripts/audit-continuation-mode-links.sh",
    "bash scripts/audit-browser-review-links.sh",
    "bash scripts/refresh-note-layer-boundary.sh",
]

expected = {
    Path("README.md"): full_audit_stack,
    Path("START-HERE.md"): full_audit_stack,
    Path("notes/insight-note-standardization-cutoff-2026-08-11.md"): linked_audit_stack,
    Path("notes/insight-artifact-manifest-2026-08-11.md"): [
        *linked_audit_stack,
        "bash scripts/verify-insight-system.sh",
    ],
    Path("notes/continuation-mode-alignment-audit-2026-08-11.md"): [
        "bash scripts/audit-audit-stack-terminology.sh",
        "bash scripts/audit-continuation-mode-links.sh",
        "bash scripts/audit-browser-review-links.sh",
        "bash scripts/verify-insight-system.sh",
    ],
    Path("notes/insight-extraction-hub-2026-08-11.md"): [
        "bash scripts/verify-insight-system.sh",
    ],
}

missing = []
for rel, commands in expected.items():
    text = (repo / rel).read_text()
    for command in commands:
        if command not in text:
            missing.append((rel.as_posix(), command))

print("maintenance-doc-stack-audit")
print(f"docs_checked {len(expected)}")
print(f"missing_command_references {len(missing)}")

if missing:
    for rel, command in missing:
        print(f"{rel} :: {command}", file=sys.stderr)
    sys.exit(1)

print("maintenance_doc_stack_ok")
PY
