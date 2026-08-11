#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

# Preferred one-command entrypoint for the linked audit stack.
bash scripts/refresh-note-layer-boundary.sh
