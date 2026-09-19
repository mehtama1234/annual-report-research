#!/usr/bin/env python3
"""Verify the requirement-level completion audit and its explicit open boundary."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
AUDIT_MD = ANALYSIS / "combined-investment-research-completion-audit.md"
AUDIT_CSV = ANALYSIS / "data" / "combined-investment-research-completion-audit.csv"
QUEUE_CSV = ANALYSIS / "data" / "combined-investment-research-next-evidence-queue.csv"
DELIVERABLE_CSV = ANALYSIS / "data" / "combined-investment-research-deliverable-audit.csv"
SYNTHESIS_MD = ANALYSIS / "combined-investment-research-current-synthesis.md"
GOAL_MD = ANALYSIS / "combined-investment-research-meaty-end-to-end-goal.md"


def resolve(raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else ROOT / path


def main() -> int:
    for path in (AUDIT_MD, AUDIT_CSV, QUEUE_CSV, DELIVERABLE_CSV, SYNTHESIS_MD, GOAL_MD):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing completion-control artifact: {path.relative_to(ROOT)}")

    text = AUDIT_MD.read_text(encoding="utf-8")
    for marker in (
        "The system is not complete.",
        "12 of the 13",
        "CA-06 remains `partial`",
        "Post-pilot expansion status",
        "D-18 through D-98",
        "Latest CA-06 filing evidence",
        "$1.147B",
        "$2.9B",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: completion-audit boundary marker missing: {marker}")

    synthesis = SYNTHESIS_MD.read_text(encoding="utf-8")
    for marker in (
        "### Next-cycle decision surface",
        "Q-11 FPL",
        "Q-12 MF1 / Apollo-Athene",
        "Q-13 URI",
        "Do not call aggregate SPP revenue or utility OCF Distribution Inspection cash",
        "Do not call an Apollo-affiliated wrapper an Athene receipt or common-owner return",
        "Do not call facility capacity or fleet resale recovery a lifecycle return",
    ):
        if marker not in synthesis:
            raise SystemExit(f"FAIL: next-cycle decision-surface marker missing: {marker}")

    goal = GOAL_MD.read_text(encoding="utf-8")
    for marker in (
        "Current execution checkpoint — 2026-09-17 retail handoff",
        "Q-04–Q-06 promotion action\nregister",
        "same-period inventory/payable",
        "no company-disclosed maintenance/replacement split",
        "remains `evidence-insufficient`",
        "no retail proxy is promoted to normalized owner cash",
        "Q-11–Q-13 promotion\naction register",
        "FPL `searched-negative` hold",
        "populated borrowing-base",
    ):
        if marker not in goal:
            raise SystemExit(f"FAIL: meaty-goal checkpoint marker missing: {marker}")

    with AUDIT_CSV.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    expected_ids = {f"CA-{index:02d}" for index in range(1, 14)}
    if {row["audit_id"] for row in rows} != expected_ids:
        raise SystemExit("FAIL: completion audit must contain exactly CA-01 through CA-13")
    status_by_id = {row["audit_id"]: row["status"] for row in rows}
    if status_by_id.get("CA-06") != "partial":
        raise SystemExit("FAIL: CA-06 must remain partial until the normalized denominator is closed")
    if {audit_id for audit_id, status in status_by_id.items() if status != "proven"} != {"CA-06"}:
        raise SystemExit("FAIL: only CA-06 may remain below proven in the current requirement audit")
    for row in rows:
        for field in ("authoritative_evidence", "source_artifact", "remaining_gap", "verification_method"):
            if not row[field].strip():
                raise SystemExit(f"FAIL: completion audit row missing {field}: {row['audit_id']}")
        if not resolve(row["source_artifact"]).exists():
            raise SystemExit(f"FAIL: completion audit source artifact missing: {row['source_artifact']}")

    with QUEUE_CSV.open(newline="", encoding="utf-8") as handle:
        queue_rows = list(csv.DictReader(handle))
    if {row["queue_id"] for row in queue_rows} != {f"Q-{index:02d}" for index in range(1, 14)}:
        raise SystemExit("FAIL: completion audit queue must contain Q-01 through Q-13")

    with DELIVERABLE_CSV.open(newline="", encoding="utf-8") as handle:
        deliverables = list(csv.DictReader(handle))
    if len(deliverables) != 98:
        raise SystemExit(f"FAIL: completion audit expects 98 deliverables, found {len(deliverables)}")

    print("Combined investment completion-audit verification passed: 13 requirements, CA-06 boundary, Q-01 through Q-13, and 98 deliverables checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
