#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import sys

repo = Path.cwd()

paths = [
    Path("README.md"),
    Path("START-HERE.md"),
    Path("notes/insight-extraction-hub-2026-08-11.md"),
    Path("notes/master-operator-brief-2026-08-10.md"),
    Path("site/index.html"),
    Path("site/concrete-insights.html"),
]

needles = {
    "remaining brief": "remaining-meaty-end-to-end-operator-brief-2026-08-11",
    "remaining goal": "remaining-end-to-end-insight-goal-2026-08-11",
    "remaining board": "remaining-insight-execution-board-2026-08-11",
}

flagged = []
for rel in paths:
    text = (repo / rel).read_text()
    missing = [label for label, needle in needles.items() if needle not in text]
    if missing:
        flagged.append((rel, missing))

print("remaining-brief-link-audit")
print(f"checked_surfaces {len(paths)}")
print(f"missing_required_links {len(flagged)}")

if flagged:
    for rel, missing in flagged:
        print(f"{rel.as_posix()} -> {', '.join(missing)}", file=sys.stderr)
    sys.exit(1)

print("remaining_brief_links_ok")
PY
