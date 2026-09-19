#!/usr/bin/env python3
"""Verify the insurance statutory named-asset expansion lane and its boundaries."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
NEXT_DIG_MD = ANALYSIS / "capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.md"
NEXT_DIG_CSV = ANALYSIS / "data" / "capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.csv"
APOLLO_ROUTES = ANALYSIS / "combined-investment-research-pilot-03-apollo-named-asset-return-routes.md"
APOLLO_ARISTOTLE = ANALYSIS / "capital-flow-apollo-athene-aristotle-mixed-row-resolution-pass-1.md"
AMAPS = ANALYSIS / "capital-flow-apollo-athene-amaps-named-cash-source-acquisition-pass-1.md"
ACCORDIA = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-pass-1.md"
ACCORDIA_PACKET = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-matched-disposal-owned-interest-proof-packet-pass-1.md"
ACCORDIA_PACKET_DATA = ANALYSIS / "data" / "capital-flow-kkr-global-atlantic-accordia-matched-disposal-owned-interest-proof-packet-pass-1.csv"


def require_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"FAIL: missing insurance lane artifact: {path.relative_to(ROOT)}")


def main() -> int:
    for path in (NEXT_DIG_MD, NEXT_DIG_CSV, APOLLO_ROUTES, APOLLO_ARISTOTLE, AMAPS, ACCORDIA, ACCORDIA_PACKET, ACCORDIA_PACKET_DATA):
        require_file(path)

    next_dig_text = NEXT_DIG_MD.read_text(encoding="utf-8")
    for marker in (
        "insurance statutory named-asset income proof",
        "Why Apollo/Athene Is Still The Prototype",
        "Why KKR / Accordia Is The Best Comparison",
        "Pass / Hold Standard",
        "full named-cash proof",
    ):
        if marker not in next_dig_text:
            raise SystemExit(f"FAIL: insurance next-dig boundary marker missing: {marker}")

    with NEXT_DIG_CSV.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    expected_ids = {f"CFISNAI-{index:03d}" for index in range(1, 9)}
    if {row["route_id"] for row in rows} != expected_ids:
        raise SystemExit("FAIL: insurance next-dig must contain exactly eight route rows")
    if rows[0]["platform_or_route"] != "Apollo Athene":
        raise SystemExit("FAIL: Apollo/Athene must remain the prototype route")
    if rows[1]["platform_or_route"] != "KKR Global Atlantic":
        raise SystemExit("FAIL: KKR/Global Atlantic must remain the comparison route")
    for row in rows[:2]:
        if not row["hold_test"].strip() or not row["pass_test"].strip():
            raise SystemExit(f"FAIL: missing pass/hold control for {row['route_id']}")

    route_text = APOLLO_ROUTES.read_text(encoding="utf-8")
    accordia_text = ACCORDIA.read_text(encoding="utf-8")
    for marker in ("Concord Music Royalties LLC", "AMAPS 1 LLC", "AP Aristotle", "Access waterfall"):
        if marker not in route_text:
            raise SystemExit(f"FAIL: Apollo named-route marker missing: {marker}")
    for marker in ("interest received", "not full named-cash proof", "liability-cost spread"):
        if marker not in accordia_text:
            raise SystemExit(f"FAIL: Accordia proof boundary marker missing: {marker}")
    packet_text = ACCORDIA_PACKET.read_text(encoding="utf-8")
    for marker in ("coordinate-owned-interest-disposal-join-visible", "settlement-and-return-unproven", "Intel Corp", "Orange SA", "custodian/broker settlement"):
        if marker not in packet_text:
            raise SystemExit(f"FAIL: Accordia proof-packet marker missing: {marker}")
    with ACCORDIA_PACKET_DATA.open(newline="", encoding="utf-8") as handle:
        packet_rows = list(csv.DictReader(handle))
    if len(packet_rows) != 3 or {row["packet_id"] for row in packet_rows} != {f"CFKKRGADOP-{index:03d}" for index in range(1, 4)}:
        raise SystemExit("FAIL: Accordia proof packet must contain exactly three joined rows")
    if {row["cusip"] for row in packet_rows} != {"458140-BM-1", "202795-JY-7", "685218-AB-5"}:
        raise SystemExit("FAIL: Accordia proof packet CUSIP set changed unexpectedly")
    for row in packet_rows:
        if row["current_status"] != "coordinate-owned-interest-disposal-join-visible" or not row["what_is_not_proven"].strip():
            raise SystemExit(f"FAIL: Accordia proof packet boundary missing: {row['packet_id']}")

    aristotle_text = APOLLO_ARISTOTLE.read_text(encoding="utf-8")
    amaps_text = AMAPS.read_text(encoding="utf-8")
    if "cash-like consideration candidate" not in aristotle_text:
        raise SystemExit("FAIL: Aristotle cash-like bucket boundary missing")
    if "not full borrower receipt" not in amaps_text and "not full borrower receipt or asset return" not in amaps_text:
        raise SystemExit("FAIL: AMAPS borrower-receipt boundary missing")

    print("Insurance statutory expansion lane verification passed: Apollo/KKR route boundaries checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
