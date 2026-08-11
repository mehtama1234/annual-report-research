#!/usr/bin/env python3

import argparse
import csv
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "indexes" / "raw-blob-offload-manifest-2026-08-10.csv"
LEGACY_REPO_ROOTS = (
    "/home/manishmehta/ui-projects/annual-report-research-new-lanes/",
    "/home/manishmehta/ui-projects/annual-report-research/",
)


def normalize_raw_path(value: str) -> str:
    candidate = value.strip()
    for prefix in LEGACY_REPO_ROOTS:
        if candidate.startswith(prefix):
            candidate = candidate[len(prefix) :]
            break
    if candidate.startswith("./"):
        candidate = candidate[2:]
    if candidate.startswith("/"):
        candidate = candidate[1:]
    if not candidate.startswith("raw/"):
        raise ValueError("path must resolve to a raw/... location")
    return candidate


def load_manifest(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows[row["local_path"]] = row
    return rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Resolve an offloaded raw/... path to its Drive pointer and manifest metadata."
    )
    parser.add_argument(
        "path",
        help="A raw/... path, a repo-relative path, or an absolute legacy/current repo raw path.",
    )
    parser.add_argument(
        "--url-only",
        action="store_true",
        help="Print only the Drive URL for shell use.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not MANIFEST_PATH.exists():
        print(f"manifest not found: {MANIFEST_PATH}", file=sys.stderr)
        return 1

    try:
        raw_path = normalize_raw_path(args.path)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    manifest = load_manifest(MANIFEST_PATH)
    row = manifest.get(raw_path)
    if row is None:
        print(f"not found in manifest: {raw_path}", file=sys.stderr)
        return 3

    if args.url_only:
        print(row["drive_url"])
        return 0

    print(f"local_path: {row['local_path']}")
    print(f"drive_url: {row['drive_url']}")
    print(f"bytes: {row['bytes']}")
    print(f"sha256: {row['sha256']}")
    print(f"source_family: {row['source_family']}")
    print(f"sector: {row['sector']}")
    print(f"industry: {row['industry']}")
    print(f"company_slug: {row['company_slug']}")
    print(f"as_of_date: {row['as_of_date']}")
    print(f"offloaded_by_commit: {row['offloaded_by_commit']}")
    print(f"notes: {row['notes']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
