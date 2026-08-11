#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import sys

repo = Path.cwd()

paths = {
    Path("notes/remaining-meaty-end-to-end-operator-brief-2026-08-11.md"): [
        "remaining-end-to-end-insight-goal-2026-08-11",
        "remaining-insight-execution-board-2026-08-11",
    ],
    Path("notes/remaining-end-to-end-insight-goal-2026-08-11.md"): [
        "remaining-meaty-end-to-end-operator-brief-2026-08-11",
        "remaining-insight-execution-board-2026-08-11",
    ],
    Path("notes/remaining-insight-execution-board-2026-08-11.md"): [
        "remaining-meaty-end-to-end-operator-brief-2026-08-11",
        "remaining-end-to-end-insight-goal-2026-08-11",
    ],
}

missing = []
for rel, needles in paths.items():
    text = (repo / rel).read_text()
    for needle in needles:
        if needle not in text:
            missing.append((rel, needle))

print("remaining-stack-link-audit")
print(f"checked_notes {len(paths)}")
print(f"missing_cross_links {len(missing)}")

if missing:
    for rel, needle in missing:
        print(f"{rel.as_posix()} -> {needle}", file=sys.stderr)
    sys.exit(1)

print("remaining_stack_links_ok")
PY
