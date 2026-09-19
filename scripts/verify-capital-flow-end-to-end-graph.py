#!/usr/bin/env python3
"""Verify the seeded capital-flow graph schema and its explicit boundaries."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
GRAPH_MD = ANALYSIS / "capital-flow-end-to-end-graph-pass-1.md"
GRAPH_CSV = ANALYSIS / "data" / "capital-flow-end-to-end-graph-pass-1.csv"

FIELDS = [
    "flow_id",
    "capital_source",
    "router",
    "vehicle_or_instrument",
    "recipient",
    "use_of_funds",
    "asset_or_project",
    "output_metric",
    "cash_metric",
    "proof_level",
    "evidence_page",
    "missing_proof",
    "safe_claim",
]


def main() -> int:
    for path in (GRAPH_MD, GRAPH_CSV):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing graph artifact: {path.relative_to(ROOT)}")

    text = GRAPH_MD.read_text(encoding="utf-8")
    for marker in (
        "source-backed capital-flow rows",
        "cash proxy evidence is not asset-level cash-return proof",
        "No row is asset-level-return-proven",
        "completed-source-use-visible",
        "CFE2EG-011",
        "CFE2EG-017",
        "CFE2EG-018",
        "CFE2EG-019",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: graph boundary marker missing: {marker}")

    with GRAPH_CSV.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise SystemExit("FAIL: capital-flow graph header does not match the required schema")
        rows = list(reader)

    expected_ids = {f"CFE2EG-{index:03d}" for index in range(1, 20)}
    if {row["flow_id"] for row in rows} != expected_ids:
        raise SystemExit("FAIL: graph must contain exactly CFE2EG-001 through CFE2EG-019")

    pbf = next(row for row in rows if row["flow_id"] == "CFE2EG-011")
    if pbf["proof_level"] != "completed-source-use-visible" or "801.6M" not in pbf["cash_metric"]:
        raise SystemExit("FAIL: PBF graph row does not preserve completed source/use evidence")

    ares = next(row for row in rows if row["flow_id"] == "CFE2EG-003")
    if "Frontline" not in ares["recipient"] or "ares-frontline-primary-source-refresh" not in ares["evidence_page"]:
        raise SystemExit("FAIL: Ares graph row does not preserve the dated Frontline evidence route")

    atwell = next(row for row in rows if row["flow_id"] == "CFE2EG-017")
    if "Atwell" not in atwell["recipient"] or "atwell-bofa-advent" not in atwell["evidence_page"]:
        raise SystemExit("FAIL: Atwell graph row does not preserve its separate BofA/Advent route")

    amaps = next(row for row in rows if row["flow_id"] == "CFE2EG-018")
    if "02300A-AA-8" not in amaps["vehicle_or_instrument"] or "AMAPS" not in amaps["recipient"]:
        raise SystemExit("FAIL: AMAPS graph row does not preserve its named CUSIP route")
    if amaps["proof_level"] != "source-use-output-cash-proxy-visible" or "amaps-controlled-document-request-packet" not in amaps["evidence_page"]:
        raise SystemExit("FAIL: AMAPS graph row overclaims or loses its controlled-document route")
    for marker in ("2.544B", "1.9175B", "48.871M", "2025-10-24", "Apollo Capital Markets Partner", "268M", "3.987M"):
        if marker not in amaps["output_metric"]:
            raise SystemExit(f"FAIL: AMAPS graph row lost controlled metric: {marker}")

    ap_grange = next(row for row in rows if row["flow_id"] == "CFE2EG-019")
    if "AP Grange" not in ap_grange["recipient"] or "G2964#-AA-7" not in ap_grange["vehicle_or_instrument"]:
        raise SystemExit("FAIL: AP Grange graph row does not preserve its named instrument route")
    if ap_grange["proof_level"] != "source-use-output-cash-proxy-visible" or "ap-grange-call-statutory-bridge" not in ap_grange["evidence_page"]:
        raise SystemExit("FAIL: AP Grange graph row overclaims or loses its statutory bridge")
    for marker in ("673M", "5.662B", "5.080B", "3.638B", "411.999M", "313313"):
        if marker not in ap_grange["output_metric"]:
            raise SystemExit(f"FAIL: AP Grange graph row lost controlled metric: {marker}")
    ap_grange_missing = ap_grange["missing_proof"].lower()
    for marker in ("call notice", "trustee remittance", "affected tranche", "athene allocation", "owner cash"):
        if marker not in ap_grange_missing:
            raise SystemExit(f"FAIL: AP Grange graph row lost missing-proof boundary: {marker}")

    for row in rows:
        for field in FIELDS:
            if not row[field].strip():
                raise SystemExit(f"FAIL: empty {field}: {row['flow_id']}")
        if "asset-level-return-proven" in row["proof_level"]:
            raise SystemExit(f"FAIL: graph row overclaims asset-level return: {row['flow_id']}")

    print("Capital-flow end-to-end graph verification passed: 19 flows, 13 fields, PBF/Ares/Atwell/AMAPS/AP-Grange routes and non-overclaim boundaries checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
