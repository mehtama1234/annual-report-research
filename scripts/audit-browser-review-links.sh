#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
import re
import sys

repo = Path.cwd()
verify_path = repo / "scripts" / "verify-insight-system.sh"
site_files = [
    repo / "site" / "index.html",
    repo / "site" / "concrete-insights.html",
]

verify_text = verify_path.read_text()

vars_map = {}
for line in verify_text.splitlines():
    match = re.match(r'([A-Za-z_][A-Za-z0-9_]*)="([^"]+)"', line.strip())
    if match:
        vars_map[match.group(1)] = match.group(2)

required_files = set()
for line in verify_text.splitlines():
    stripped = line.strip().rstrip(",")
    if stripped.startswith('"') and stripped.endswith('"'):
        value = stripped.strip('"')
        if ":" in value:
            continue
        for key, replacement in vars_map.items():
            value = value.replace(f"${key}", replacement)
        if not value.startswith("$"):
            required_files.add(value)

patterns = [
    re.compile(r'viewer\.html\?file=([^"&>]+)'),
]

missing = []
seen = set()

for site_file in site_files:
    text = site_file.read_text()
    for pattern in patterns:
        for match in pattern.finditer(text):
            rel = match.group(1).replace("%20", " ")
            if rel in seen:
                continue
            seen.add(rel)
            if rel not in required_files:
                missing.append((site_file.relative_to(repo), rel))

print("browser-review-link-audit")
print(f"review_pages {len(site_files)}")
print(f"linked_viewer_targets {len(seen)}")
print(f"missing_required_file_coverage {len(missing)}")

if missing:
    for site_file, rel in missing:
        print(f"{site_file} -> {rel}", file=sys.stderr)
    sys.exit(1)

print("browser_review_links_ok")
PY
