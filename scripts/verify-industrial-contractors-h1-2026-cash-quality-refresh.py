#!/usr/bin/env python3
"""Verify H1 2026 contractor cash-quality facts using CY2026Q2 frames."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "comfort-systems-usa-inc": {"ocf": 1_528_254_000, "capex": 288_837_000, "acq": 162_845_000, "capex_tag": "PaymentsToAcquirePropertyPlantAndEquipment"},
    "emcor-group-inc": {"ocf": 289_913_000, "capex": 59_860_000, "acq": 94_953_000, "capex_tag": "PaymentsToAcquireProductiveAssets"},
    "quanta-services-inc": {"ocf": 1_487_188_000, "capex": 451_048_000, "acq": 930_311_000, "capex_tag": "PaymentsToAcquirePropertyPlantAndEquipment"},
}


def frame_value(facts, tag):
    rows = []
    for units in facts["facts"]["us-gaap"][tag]["units"].values():
        rows.extend(
            row for row in units
            if row.get("fy") == 2026
            and row.get("fp") == "Q2"
            and row.get("form") == "10-Q"
            and row.get("start") == "2026-01-01"
            and row.get("end") == "2026-06-30"
        )
    if not rows:
        raise AssertionError(f"missing CY2026Q2 fact: {tag}")
    return rows[-1]["val"]


def main():
    for name, expected in CASES.items():
        base = f"industrial-goods/general-contractors/{name}"
        filing = ROOT / "raw/sec" / base / "2026-q2-10q.html"
        facts = json.loads((ROOT / "raw/sec/companyfacts" / base / "companyfacts.json").read_text())
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing Q2 filing: {filing}")
        tags = {
            "ocf": "NetCashProvidedByUsedInOperatingActivities",
            "capex": expected["capex_tag"],
            "acq": "PaymentsToAcquireBusinessesNetOfCashAcquired",
        }
        actual = {key: frame_value(facts, tag) for key, tag in tags.items()}
        expected = {key: value for key, value in expected.items() if key != "capex_tag"}
        if actual != expected:
            raise AssertionError(f"{name}: expected {expected}, got {actual}")
        print(name, "ok", actual, "ocf_less_capex=", actual["ocf"] - actual["capex"])
    print("industrial-contractors-h1-2026-cash-quality-refresh-ok")


if __name__ == "__main__":
    main()
