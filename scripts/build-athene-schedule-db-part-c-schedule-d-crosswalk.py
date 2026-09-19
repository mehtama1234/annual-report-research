#!/usr/bin/env python3
"""Crosswalk named Schedule DB Part C cash components to Schedule D CUSIPs."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PART_C = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-db-part-c-ledger-pass-1.csv"
SCHEDULE_D = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-db-part-c-schedule-d-crosswalk-pass-1.csv"

FIELDNAMES = [
    "crosswalk_id",
    "part_c_ledger_id",
    "part_c_source_page",
    "derivative_identifier",
    "derivative_instrument_type",
    "cash_instrument_cusip",
    "cash_instrument_description",
    "schedule_d_match_count",
    "schedule_d_row_id",
    "schedule_d_source_page",
    "schedule_d_issuer_or_description",
    "schedule_d_naic_designation",
    "schedule_d_actual_cost",
    "schedule_d_par_value",
    "schedule_d_fair_value",
    "schedule_d_book_adjusted_carrying_value",
    "schedule_d_interest_income",
    "schedule_d_interest_received_during_year",
    "match_status",
    "what_is_proven",
    "boundary",
    "next_proof",
]


def main() -> None:
    with PART_C.open(newline="", encoding="utf-8") as handle:
        part_c_rows = list(csv.DictReader(handle))
    with SCHEDULE_D.open(newline="", encoding="utf-8") as handle:
        schedule_d_rows = list(csv.DictReader(handle))

    by_cusip: dict[str, list[dict[str, str]]] = {}
    for row in schedule_d_rows:
        by_cusip.setdefault(row["cusip"].strip().upper(), []).append(row)

    output: list[dict[str, str]] = []
    for part_c in part_c_rows:
        cusip = part_c["cash_instrument_cusip"].strip().upper()
        matches = by_cusip.get(cusip, [])
        if not matches:
            continue
        match_status = "exact-cusip-schedule-d-crosswalk"
        if len(matches) > 1:
            match_status = "exact-cusip-multiple-schedule-d-rows"
        for schedule_d in matches:
            output.append(
                {
                    "crosswalk_id": f"CFAASDBCSD-{len(output) + 1:04d}",
                    "part_c_ledger_id": part_c["ledger_id"],
                    "part_c_source_page": part_c["source_page"],
                    "derivative_identifier": part_c["derivative_identifier"],
                    "derivative_instrument_type": part_c["derivative_instrument_type"],
                    "cash_instrument_cusip": cusip,
                    "cash_instrument_description": part_c["cash_instrument_description"],
                    "schedule_d_match_count": str(len(matches)),
                    "schedule_d_row_id": schedule_d["normalized_row_id"],
                    "schedule_d_source_page": schedule_d["page"],
                    "schedule_d_issuer_or_description": schedule_d["issuer_or_description"],
                    "schedule_d_naic_designation": schedule_d["naic_designation"],
                    "schedule_d_actual_cost": schedule_d["actual_cost"],
                    "schedule_d_par_value": schedule_d["par_value"],
                    "schedule_d_fair_value": schedule_d["fair_value"],
                    "schedule_d_book_adjusted_carrying_value": schedule_d["book_adjusted_carrying_value"],
                    "schedule_d_interest_income": schedule_d["interest_income"],
                    "schedule_d_interest_received_during_year": schedule_d["interest_received_during_year"],
                    "match_status": match_status,
                    "what_is_proven": "A Schedule DB Part C cash-instrument CUSIP has an exact identifier match in Athene Schedule D, joining the named replication component to a statutory holding row.",
                    "boundary": "CUSIP identity and Schedule D fields are not proof of Schedule DB settlement, counterparty remittance, liability/product hedge allocation, borrower cash, or Apollo owner cash.",
                    "next_proof": "Reconcile the matched Schedule D lot to Schedule DB component values, custody/counterparty, derivative cash settlement, liability hedge purpose, and investment-income receipt.",
                }
            )

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)
    unique_part_c = len({row["part_c_ledger_id"] for row in output})
    unique_cusips = len({row["cash_instrument_cusip"] for row in output})
    print(f"wrote {len(output)} crosswalk rows; {unique_part_c} Part C rows; {unique_cusips} unique CUSIPs")


if __name__ == "__main__":
    main()
