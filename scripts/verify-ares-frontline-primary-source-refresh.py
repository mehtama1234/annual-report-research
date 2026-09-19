#!/usr/bin/env python3
"""Verify the dated Ares/Frontline private-credit source refresh."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "capital-flow-ares-frontline-primary-source-refresh-2026-09-17.md"
TABLE = ANALYSIS / "data" / "capital-flow-ares-frontline-primary-source-refresh-2026-09-17.csv"
ROLLFORWARD = ANALYSIS / "capital-flow-ares-frontline-asif-rollforward-2026-09-18.md"
ROLLFORWARD_TABLE = ANALYSIS / "data" / "capital-flow-ares-frontline-asif-rollforward-2026-09-18.csv"
TRANCHE_BOUNDARY = ANALYSIS / "capital-flow-frontline-tranche-identity-overlap-boundary-2026-09-18.md"
TRANCHE_TABLE = ANALYSIS / "data" / "capital-flow-frontline-tranche-identity-overlap-boundary-2026-09-18.csv"


def main() -> int:
    for path in (REPORT, TABLE, ROLLFORWARD, ROLLFORWARD_TABLE, TRANCHE_BOUNDARY, TRANCHE_TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing Ares/Frontline refresh: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "May 5, 2025",
        "July 31, 2026",
        "SOFR plus `5.00%`",
        "Blackstone Private Credit Fund",
        "Goldman Sachs Private Credit Corp.",
        "Ares Capital Corporation",
        "Ares Strategic Income Fund",
        "Arranger/bookrunner status is a role claim",
        "facility-allocation-and-cash-waterfall-open",
        "frontline-holder-breadth-expanded; tranche-and-facility-identity-open",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: Ares/Frontline refresh marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 14:
        raise SystemExit(f"FAIL: expected 14 Ares/Frontline observations, found {len(rows)}")
    if "$198.675M" not in text or "$54.300M" not in text:
        raise SystemExit("FAIL: selected holder-exposure markers missing")
    rollforward_text = ROLLFORWARD.read_text(encoding="utf-8")
    for marker in ("+$20.0966M", "+$19.7825M", "+$18.2313M", "funding-event-and-borrower-cash-open"):
        if marker not in rollforward_text:
            raise SystemExit(f"FAIL: ASIF roll-forward marker missing: {marker}")
    with ROLLFORWARD_TABLE.open(newline="", encoding="utf-8") as handle:
        rollforward_rows = list(csv.DictReader(handle))
    if len(rollforward_rows) != 3:
        raise SystemExit(f"FAIL: expected 3 ASIF roll-forward observations, found {len(rollforward_rows)}")
    tranche_text = TRANCHE_BOUNDARY.read_text(encoding="utf-8")
    for marker in ("Frontline Road Safety LLC", "Frontline Road Safety Operations, LLC", "03/2031", "03/2032", "$622.8244M", "credit agreement and amendments"):
        if marker not in tranche_text:
            raise SystemExit(f"FAIL: Frontline tranche-boundary marker missing: {marker}")
    with TRANCHE_TABLE.open(newline="", encoding="utf-8") as handle:
        tranche_rows = list(csv.DictReader(handle))
    if len(tranche_rows) != 4:
        raise SystemExit(f"FAIL: expected 4 Frontline tranche identity buckets, found {len(tranche_rows)}")
    print("ares-frontline-primary-source-refresh-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
