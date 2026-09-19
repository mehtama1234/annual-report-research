#!/usr/bin/env python3
"""Build URI's H1 2026 disclosed cash-to-claims bridge.

The result is a diagnostic cash-use bridge. It is intentionally not labeled
normalized owner cash because replacement/growth, subsidiary transfer, legal
availability, and lifecycle-return allocations remain unresolved.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
OUT = DATA / "capital-flow-uri-h1-2026-cash-claim-bridge-pass-1.csv"
MEMO = ROOT / "analysis/company-first-principles/capital-flow-uri-h1-2026-cash-claim-bridge-pass-1.md"

FIELDS = [
    "bridge_id",
    "period",
    "company",
    "cash_flow_class",
    "line_item",
    "amount_usd_millions",
    "sign",
    "cumulative_after_item_usd_millions",
    "source_artifact",
    "evidence_status",
    "what_is_proven",
    "what_is_not_proven",
    "next_upgrade",
]

ROWS = [
    ("operating", "Operating cash flow", 3305, "reported-operating-cash"),
    ("fleet-reinvestment", "Purchases of rental equipment", -2720, "reported-fleet-investment"),
    ("fleet-recovery", "Proceeds from rental-equipment sales", 680, "reported-resale-recovery"),
    ("non-fleet-reinvestment", "Purchases of non-rental equipment and intangibles", -165, "reported-non-fleet-reinvestment"),
    ("non-fleet-recovery", "Proceeds from non-rental equipment", 26, "reported-non-fleet-recovery"),
    ("acquisition", "Purchases of companies, net of cash acquired", -400, "reported-acquisition-use"),
    ("acquisition", "Contingent consideration paid", -18, "reported-acquisition-claim"),
    ("capital-allocation", "Repurchases including share-settlement taxes", -816, "reported-common-capital-allocation"),
    ("capital-allocation", "Dividends paid", -248, "reported-common-distribution"),
]


def main() -> None:
    cumulative = 0
    output: list[dict[str, str]] = []
    for index, (cash_class, item, amount, status) in enumerate(ROWS, start=1):
        cumulative += amount
        output.append(
            {
                "bridge_id": f"CFURIH1CCB-{index:03d}",
                "period": "H1 2026",
                "company": "United Rentals, Inc.",
                "cash_flow_class": cash_class,
                "line_item": item,
                "amount_usd_millions": str(amount),
                "sign": "source" if amount >= 0 else "use",
                "cumulative_after_item_usd_millions": str(cumulative),
                "source_artifact": "capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md; combined-investment-research-industrial-uptime-uri-fleet-lifecycle-bridge-pass-1-2026-09-17.md",
                "evidence_status": status,
                "what_is_proven": "The H1 2026 filing-backed cash source or use is visible in the consolidated URI cash-flow bridge.",
                "what_is_not_proven": "This line is not allocated to a particular fleet cohort, ABL draw, subsidiary transfer, maintenance/growth bucket, or lifecycle return.",
                "next_upgrade": "Same-period source/use allocation, replacement-versus-growth schedule, legal-entity transfer, and borrowing-base/lifecycle join.",
            }
        )
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    lines = [
        "# United Rentals H1 2026 cash-to-claims bridge — pass 1",
        "",
        "This bridge consolidates disclosed H1 2026 URI cash sources and uses. It is a diagnostic residual, not normalized owner cash.",
        "",
        "| Surface | USD millions |",
        "|---|---:|",
        "| Operating cash flow | 3,305 |",
        "| Less rental-equipment purchases | (2,720) |",
        "| Plus rental-equipment sale proceeds | 680 |",
        "| Less non-rental equipment/intangible purchases | (165) |",
        "| Plus non-rental equipment proceeds | 26 |",
        "| Less acquisitions, net of cash acquired | (400) |",
        "| Less contingent consideration | (18) |",
        "| Less repurchases including share-settlement taxes | (816) |",
        "| Less dividends | (248) |",
        "| Mechanical residual after listed sources/uses | **(356)** |",
        "",
        "## Interpretation",
        "",
        "The negative `$356M` residual is a mechanical result of subtracting the listed uses from reported OCF and adding disclosed disposal proceeds. It is not a loss measure and is not a normalized owner-cash estimate: rental-equipment purchases are not split into maintenance versus growth, disposal proceeds are not recurring cash, and acquisitions/repurchases/dividends are distinct claims.",
        "",
        "URI's operating subsidiaries and debt agreements also restrict transfers to the parent. Therefore consolidated OCF and this residual cannot be treated as freely available common-owner cash without an intercompany-transfer and parent-receipt bridge.",
        "",
        "## Still open",
        "",
        "- replacement versus growth fleet capital;",
        "- fleet-cohort utilization, maintenance, and lifecycle return;",
        "- ABL draw/source-to-purchase allocation and borrowing-base/NOLV/reserve support;",
        "- URNA-to-parent transfer capacity and actual parent receipt; and",
        "- tax, debt-service, dilution, and other senior-claim allocation.",
        "",
        "The machine-readable bridge is [here](data/capital-flow-uri-h1-2026-cash-claim-bridge-pass-1.csv).",
    ]
    MEMO.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote URI H1 2026 cash-claim bridge: 9 rows; mechanical residual=-356 USD millions")


if __name__ == "__main__":
    main()
