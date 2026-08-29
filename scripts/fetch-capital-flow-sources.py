#!/usr/bin/env python3
"""Fetch primary-source documents listed in the capital-flow source manifest."""

from __future__ import annotations

import csv
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "analysis" / "company-first-principles" / "data" / "capital-flow-source-acquisition-manifest.csv"
LOG = ROOT / "analysis" / "company-first-principles" / "data" / "capital-flow-source-download-log.csv"

LOG_FIELDS = [
    "source_id",
    "company",
    "period",
    "document_type",
    "source_url",
    "local_path",
    "bytes",
    "sha256",
    "fetched_at_utc",
    "status",
    "error",
]


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def fetch(url: str) -> bytes:
    request = Request(
        url,
        headers={
            "User-Agent": "annual-report-research/1.0 source verification (contact: local research workspace)",
            "Accept": "*/*",
        },
    )
    with urlopen(request, timeout=60) as response:
        return response.read()


def write_log(rows: list[dict[str, str]]) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=LOG_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv
    source_filter = None
    for arg in argv:
        if arg.startswith("--source-id="):
            source_filter = arg.split("=", 1)[1]

    rows = read_manifest(MANIFEST)
    if source_filter:
        rows = [row for row in rows if row["source_id"] == source_filter]
        if not rows:
            print(f"No manifest row matched --source-id={source_filter}", file=sys.stderr)
            return 2

    log_rows: list[dict[str, str]] = []
    for row in rows:
        local_path = ROOT / row["local_path"]
        log_row = {
            "source_id": row["source_id"],
            "company": row["company"],
            "period": row["period"],
            "document_type": row["document_type"],
            "source_url": row["source_url"],
            "local_path": row["local_path"],
            "bytes": "",
            "sha256": "",
            "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
            "status": "dry-run" if dry_run else "pending",
            "error": "",
        }

        if dry_run:
            print(f"would fetch {row['source_id']} -> {row['local_path']}")
            log_rows.append(log_row)
            continue

        try:
            payload = fetch(row["source_url"])
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(payload)
            log_row["bytes"] = str(len(payload))
            log_row["sha256"] = sha256_bytes(payload)
            log_row["status"] = "fetched"
            print(f"fetched {row['source_id']} ({len(payload)} bytes)")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            if local_path.exists():
                payload = local_path.read_bytes()
                log_row["bytes"] = str(len(payload))
                log_row["sha256"] = sha256_bytes(payload)
                log_row["status"] = "cached-after-fetch-failure"
            else:
                log_row["status"] = "failed"
            log_row["error"] = str(exc)
            print(f"failed {row['source_id']}: {exc}", file=sys.stderr)
        log_rows.append(log_row)

    write_log(log_rows)
    failures = [row for row in log_rows if row["status"] == "failed"]
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
