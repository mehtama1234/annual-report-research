#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import re
import sys

repo = Path.cwd()
manifest = repo / "indexes" / "reusable-note-layer-files-2026-08-11.txt"

trigger_patterns = [
    r"first interpretation layer",
    r"blank-slate",
    r"continuation-phase",
    r"continuation mode",
    r"open a lane from zero",
    r"restart the lane from zero",
    r"not .*starting from zero",
    r"not more first-pass",
]
trigger = re.compile("|".join(f"(?:{p})" for p in trigger_patterns), re.IGNORECASE)
required_link = re.compile(
    r"continuation-mode-alignment-audit-2026-08-11\.md|Continuation mode alignment audit",
    re.IGNORECASE,
)

# This handoff uses "first-pass merge problem" in a branch-reconciliation sense,
# not as archive continuation framing.
excluded = {
    Path("notes/frontier-merge-handoff-2026-08-10.md"),
}

files = [
    Path(line.strip())
    for line in manifest.read_text().splitlines()
    if line.strip() and not line.lstrip().startswith("#")
]

flagged = []
for rel in files:
    if rel in excluded:
        continue
    text = (repo / rel).read_text()
    if trigger.search(text) and not required_link.search(text):
        flagged.append(rel)

print("continuation-mode-link-audit")
print(f"reusable_notes_checked {len(files)}")
print(f"excluded_notes {len(excluded)}")
print(f"missing_audit_links {len(flagged)}")

if flagged:
    for rel in flagged:
        print(rel.as_posix(), file=sys.stderr)
    sys.exit(1)

print("continuation_mode_links_ok")
PY
