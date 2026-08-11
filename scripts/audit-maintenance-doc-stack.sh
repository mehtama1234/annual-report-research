#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import sys

repo = Path.cwd()

full_audit_stack = [
    "bash scripts/run-insight-audit-stack.sh",
    "bash scripts/refresh-note-layer-boundary.sh",
    "bash scripts/audit-audit-stack-terminology.sh",
    "bash scripts/audit-continuation-mode-links.sh",
    "bash scripts/audit-remaining-brief-links.sh",
    "bash scripts/audit-remaining-stack-links.sh",
    "bash scripts/audit-browser-review-links.sh",
    "bash scripts/verify-insight-system.sh",
]
linked_audit_stack = [
    "bash scripts/audit-audit-stack-terminology.sh",
    "bash scripts/audit-continuation-mode-links.sh",
    "bash scripts/audit-remaining-brief-links.sh",
    "bash scripts/audit-remaining-stack-links.sh",
    "bash scripts/audit-browser-review-links.sh",
    "bash scripts/refresh-note-layer-boundary.sh",
]

expected = {
    Path("README.md"): full_audit_stack,
    Path("START-HERE.md"): full_audit_stack,
    Path("notes/insight-note-standardization-cutoff-2026-08-11.md"): [
        "bash scripts/run-insight-audit-stack.sh",
        *linked_audit_stack,
    ],
    Path("notes/insight-artifact-manifest-2026-08-11.md"): [
        "bash scripts/run-insight-audit-stack.sh",
        *linked_audit_stack,
        "bash scripts/verify-insight-system.sh",
    ],
    Path("notes/continuation-mode-alignment-audit-2026-08-11.md"): [
        "bash scripts/audit-audit-stack-terminology.sh",
        "bash scripts/audit-maintenance-doc-stack.sh",
        "bash scripts/audit-continuation-mode-links.sh",
        "bash scripts/audit-remaining-brief-links.sh",
        "bash scripts/audit-remaining-stack-links.sh",
        "bash scripts/audit-browser-review-links.sh",
        "bash scripts/verify-insight-system.sh",
    ],
    Path("notes/insight-extraction-hub-2026-08-11.md"): [
        "bash scripts/run-insight-audit-stack.sh",
        "bash scripts/refresh-note-layer-boundary.sh",
        "bash scripts/audit-audit-stack-terminology.sh",
        "bash scripts/audit-maintenance-doc-stack.sh",
        "bash scripts/audit-continuation-mode-links.sh",
        "bash scripts/audit-remaining-brief-links.sh",
        "bash scripts/audit-remaining-stack-links.sh",
        "bash scripts/audit-browser-review-links.sh",
        "bash scripts/verify-insight-system.sh",
    ],
    Path("notes/end-to-end-insight-operator-and-review-brief-2026-08-11.md"): full_audit_stack,
    Path("notes/remaining-meaty-end-to-end-operator-brief-2026-08-11.md"): full_audit_stack,
    Path("notes/remaining-end-to-end-insight-goal-2026-08-11.md"): full_audit_stack,
    Path("notes/remaining-insight-execution-board-2026-08-11.md"): full_audit_stack,
    Path("notes/master-insight-extraction-goal-2026-08-11.md"): full_audit_stack,
    Path("notes/end-to-end-insight-master-instruction-2026-08-11.md"): full_audit_stack,
    Path("notes/lane-end-to-end-execution-runbook-2026-08-11.md"): full_audit_stack,
    Path("notes/insight-extraction-templates-2026-08-11.md"): full_audit_stack,
    Path("notes/insight-completion-rubric-2026-08-11.md"): full_audit_stack,
    Path("notes/next-steps.md"): full_audit_stack,
    Path("notes/master-operator-brief-2026-08-10.md"): full_audit_stack,
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
