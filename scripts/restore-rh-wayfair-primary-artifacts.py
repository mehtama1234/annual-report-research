#!/usr/bin/env python3
"""Restore the core RH and Wayfair SEC artifacts named in their source ledgers."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "annual-report-research/1.0 source verification (contact: local research workspace)"
RESTORED = ROOT / "notes" / "rh-wayfair-restored-artifacts-2026-09-14.tsv"

TARGETS = [
    ("RH-T10", "RH", "1528849", "2026-04-01", "10-K", "raw/sec/services/home-furnishing-stores/rh/2025-10k.html"),
    ("RH-T11", "RH", "1528849", "2025-12-11", "10-Q", "raw/sec/services/home-furnishing-stores/rh/2025-q3-10q.html"),
    ("RH-T12", "RH", "1528849", "2025-12-11", "8-K", "raw/sec/services/home-furnishing-stores/rh/2025-q3-8k.html"),
    ("RH-T16", "RH", "1528849", "2026-06-11", "10-Q", "raw/sec/services/home-furnishing-stores/rh/2026-q1-10q.html"),
    ("W-T8", "Wayfair", "1616707", "2026-02-19", "10-K", "raw/sec/services/home-furnishing-stores/wayfair-inc/2025-10k.html"),
    ("W-T9", "Wayfair", "1616707", "2026-02-19", "8-K", "raw/sec/services/home-furnishing-stores/wayfair-inc/2025-q4-8k.html"),
    ("W-T11", "Wayfair", "1616707", "2026-04-30", "10-Q", "raw/sec/services/home-furnishing-stores/wayfair-inc/2026-q1-10q.html"),
    ("W-T12", "Wayfair", "1616707", "2026-04-30", "8-K", "raw/sec/services/home-furnishing-stores/wayfair-inc/2026-q1-8k.html"),
    ("W-T14", "Wayfair", "1616707", "2026-08-04", "10-Q", "raw/sec/services/home-furnishing-stores/wayfair-inc/2026-q2-10q.html"),
    ("W-T15", "Wayfair", "1616707", "2026-08-04", "8-K", "raw/sec/services/home-furnishing-stores/wayfair-inc/2026-q2-8k.html"),
    ("W-T17", "Wayfair", "1616707", "2025-10-28", "10-Q", "raw/sec/services/home-furnishing-stores/wayfair-inc/2025-q3-10q.html"),
]


def fetch(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    with urlopen(request, timeout=60) as response:
        return response.read()


def filing_rows(cik: str) -> list[dict[str, str]]:
    payload = json.loads(fetch(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
    rows = payload["filings"]["recent"]
    return [dict(zip(rows, values)) for values in zip(*(rows[key] for key in rows))]


def main() -> int:
    output: list[str] = ["source_id\tcompany\tform\tfiling_date\tsource_url\tlocal_path\tbytes\tsha256\tfetched_at_utc"]
    for source_id, company, cik, filing_date, form, local_name in TARGETS:
        match = next((row for row in filing_rows(cik) if row["form"] == form and row["filingDate"] == filing_date), None)
        if not match:
            raise SystemExit(f"Could not find {source_id}: {company} {form} filed {filing_date}")
        accession = match["accessionNumber"]
        source_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}/{match['primaryDocument']}"
        payload = fetch(source_url)
        local_path = ROOT / local_name
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(payload)
        digest = hashlib.sha256(payload).hexdigest()
        output.append("\t".join([source_id, company, form, filing_date, source_url, local_name, str(len(payload)), digest, datetime.now(timezone.utc).isoformat()]))
        print(f"restored {source_id}: {len(payload)} bytes -> {local_name}")
    RESTORED.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(f"wrote {RESTORED.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
