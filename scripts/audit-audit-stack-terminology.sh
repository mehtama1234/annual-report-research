#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import re
import sys

repo = Path.cwd()

targets = [
    repo / "README.md",
    repo / "START-HERE.md",
    repo / "notes" / "continuation-mode-alignment-audit-2026-08-11.md",
    repo / "notes" / "insight-note-standardization-cutoff-2026-08-11.md",
    repo / "notes" / "insight-artifact-manifest-2026-08-11.md",
]

forbidden = [
    r"\bbroader insight-system verifier\b",
    r"\bone-command refresh plus verification\b",
    r"\bfull broader insight-system verifier\b",
    r"\brerun both checks\b",
]
pattern = re.compile("|".join(f"(?:{p})" for p in forbidden), re.IGNORECASE)

hits = []
for path in targets:
    text = path.read_text()
    for match in pattern.finditer(text):
        hits.append((path.relative_to(repo).as_posix(), match.group(0)))

print("audit-stack-terminology-audit")
print(f"docs_checked {len(targets)}")
print(f"forbidden_phrase_hits {len(hits)}")

if hits:
    for rel, phrase in hits:
        print(f"{rel} :: {phrase}", file=sys.stderr)
    sys.exit(1)

print("audit_stack_terminology_ok")
PY
