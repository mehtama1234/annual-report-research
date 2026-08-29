#!/usr/bin/env python3
"""Build a normalized Ares borrower holder-expansion pass."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis" / "company-first-principles" / "data"
ANALYSIS = ROOT / "analysis" / "company-first-principles"

OUTPUT_CSV = DATA / "capital-flow-ares-borrower-holder-expansion-pass-1.csv"
SAME_PERIOD_OUTPUT_CSV = DATA / "capital-flow-ares-borrower-same-period-exposure-summary-pass-1.csv"
OUTPUT_MD = ANALYSIS / "capital-flow-ares-borrower-holder-expansion-pass-1.md"
MASTER_ROLLUP = DATA / "capital-flow-master-borrower-exposure-table.csv"


FIELDS = [
    "row_id",
    "canonical_borrower",
    "sector_lane",
    "sponsor_or_counterparty",
    "source_artifact",
    "source_row_type",
    "reporting_entity",
    "manager_or_platform",
    "vehicle_taxonomy",
    "capital_channel_group",
    "source_visibility",
    "holder_source_classification_confidence",
    "cik",
    "borrower_or_credit_name",
    "period",
    "loan_type",
    "industry",
    "rate_or_coupon",
    "maturity",
    "funded_or_par_amount_usd_m",
    "fair_value_usd_m",
    "unfunded_commitment_usd_m",
    "transaction_or_bank_denominator_usd_m",
    "source_url",
    "local_path",
    "source_location",
    "row_to_transaction_confidence",
    "facility_size_status",
    "bank_replacement_status",
    "safe_claim",
    "do_not_claim",
    "status",
]

SAME_PERIOD_FIELDS = [
    "summary_id",
    "canonical_borrower",
    "sector_lane",
    "selected_period",
    "selected_period_rank",
    "same_period_rows",
    "same_period_reporting_entities",
    "same_period_capital_channel_groups",
    "same_period_fair_value_usd_m",
    "same_period_unfunded_commitment_usd_m",
    "same_period_transaction_or_bank_denominator_usd_m",
    "excluded_periods",
    "excluded_row_count",
    "master_latest_visible_funded_fair_value_usd_m",
    "master_mixed_quarter_visible_funded_fair_value_usd_m",
    "master_visible_unfunded_commitment_usd_m",
    "same_period_status",
    "what_it_says",
    "what_it_does_not_say",
]


BORROWERS = {
    "AeriTek": {
        "csv": "capital-flow-aeritek-sec-holder-crosswalk.csv",
        "artifact": "capital-flow-aeritek-sec-holder-crosswalk.md",
        "sector": "commercial refrigeration and foodservice equipment",
        "sponsor": "Mill Point / NRAC acquisition context",
        "confidence": "borrower-holder-visible; transaction-use mapping incomplete",
        "facility": "facility-size-missing",
        "bank": "bank-replacement-unproven",
        "safe": "Private credit holder schedules show AeriTek-related debt exposure in commercial refrigeration and foodservice equipment.",
    },
    "Atwell": {
        "csv": "capital-flow-atwell-sec-holder-crosswalk.csv",
        "artifact": "capital-flow-atwell-sec-holder-crosswalk.md",
        "sector": "critical infrastructure and engineering services",
        "sponsor": "Ares/Antares transaction trail; prior Bank of America facility visible",
        "confidence": "borrower-holder-visible; replacement mapping incomplete",
        "facility": "prior-bank-denominator-visible; current-facility-size-missing",
        "bank": "prior-bank-visible-but-takeout-unproven",
        "safe": "Atwell has later SEC holder rows and a known prior bank facility, but bank replacement is not proven.",
    },
    "Frontline Road Safety": {
        "csv": "capital-flow-frontline-sec-holder-crosswalk.csv",
        "artifact": "capital-flow-frontline-sec-holder-crosswalk.md",
        "sector": "roadway safety and infrastructure services",
        "sponsor": "Bain Capital",
        "confidence": "transaction-role-plus-holder-visible; row-to-facility mapping incomplete",
        "facility": "facility-size-missing",
        "bank": "bank-replacement-unproven",
        "safe": "Private credit holder schedules show Frontline Road Safety exposure in infrastructure-adjacent roadway safety services.",
    },
    "MAI Capital": {
        "csv": "capital-flow-mai-sec-holder-crosswalk.csv",
        "artifact": "capital-flow-mai-sec-holder-crosswalk.md",
        "sector": "wealth-management advisory consolidation",
        "sponsor": "New Mountain Capital",
        "confidence": "borrower-holder-visible; acquisition mapping incomplete",
        "facility": "facility-size-missing",
        "bank": "bank-replacement-unproven",
        "safe": "Private credit holder schedules show MAI Capital exposure in wealth-management advisory consolidation.",
    },
    "Precinmac": {
        "csv": "capital-flow-precinmac-sec-holder-crosswalk.csv",
        "artifact": "capital-flow-precinmac-sec-holder-crosswalk.md",
        "sector": "precision manufacturing, aerospace, defense, semiconductor, and power",
        "sponsor": "not fully mapped in current pass",
        "confidence": "borrower-holder-visible; current-period refresh needed",
        "facility": "facility-size-missing",
        "bank": "bank-replacement-unproven",
        "safe": "Private credit holder schedules show Precinmac exposure in precision manufacturing and aerospace/industrial supply chains.",
    },
    "Relation Insurance": {
        "csv": "capital-flow-relation-sec-holder-crosswalk.csv",
        "artifact": "capital-flow-relation-sec-holder-crosswalk.md",
        "sector": "insurance brokerage consolidation",
        "sponsor": "BayPine",
        "confidence": "transaction-role-plus-holder-visible; row-to-facility mapping incomplete",
        "facility": "facility-size-missing",
        "bank": "bank-replacement-unproven",
        "safe": "Private credit transaction-role evidence and holder schedules support Relation Insurance as an insurance-brokerage consolidation borrower.",
    },
    "Sunvair": {
        "csv": "capital-flow-sunvair-sec-holder-crosswalk.csv",
        "artifact": "capital-flow-sunvair-sec-holder-crosswalk.md",
        "sector": "aerospace MRO services",
        "sponsor": "not fully mapped in current pass",
        "confidence": "borrower-holder-visible; financing-document mapping incomplete",
        "facility": "facility-size-missing",
        "bank": "bank-replacement-unproven",
        "safe": "Private credit holder schedules show Sunvair exposure in aerospace MRO services.",
    },
    "Valcourt": {
        "csv": "capital-flow-valcourt-sec-holder-crosswalk.csv",
        "artifact": "capital-flow-valcourt-sec-holder-crosswalk.md",
        "sector": "building maintenance and facility services",
        "sponsor": "Littlejohn operating context; transaction debt mapping incomplete",
        "confidence": "borrower-holder-visible; refinance mapping incomplete",
        "facility": "facility-size-missing",
        "bank": "bank-replacement-unproven",
        "safe": "Private credit holder schedules show Valcourt exposure in building maintenance and facility services.",
    },
}


DO_NOT_CLAIM = (
    "Do not claim total facility size, Ares' exact funded amount, full lender group, "
    "use of proceeds, or bank replacement without a facility document, rating report, "
    "payoff/termination evidence, or equivalent source."
)

ENTITY_ALIASES = {
    "Senior Direct Lending Program LLC / Ares Capital exhibit": "Senior Direct Lending Program LLC",
    "KKR filing vehicles": "KKR FS Income Trust Select",
    "Multiple filing vehicles": "multiple filing vehicles",
    "Multiple sources": "multiple sources",
    "Local SEC corpus": "local SEC corpus",
    "Stone Point / SEC R24 filing source": "Stone Point / SEC R24 filing source",
    "Bain Capital": "Bain Capital",
    "The Sterling Group": "The Sterling Group",
    "Latham & Watkins LLP": "Latham & Watkins LLP",
    "BayPine LP": "BayPine LP",
    "Shell / Pennzoil Quaker State Company": "Shell / Pennzoil Quaker State Company",
    "Jiffy Lube / Shell web page": "Jiffy Lube / Shell web page",
    "Shell USA": "Shell USA",
    "Shell Global": "Shell Global",
}

FALLBACK_TAXONOMY = {
    "multiple filing vehicles": {
        "manager_or_platform": "multiple",
        "vehicle_taxonomy": "rollup / multi-vehicle summary",
        "capital_channel_group": "multi-vehicle summary",
        "public_or_private_visibility": "derived from underlying schedules",
        "confidence": "medium",
    },
    "multiple sources": {
        "manager_or_platform": "multiple",
        "vehicle_taxonomy": "derived transaction-gap summary",
        "capital_channel_group": "derived summary",
        "public_or_private_visibility": "derived from source set",
        "confidence": "medium",
    },
    "local SEC corpus": {
        "manager_or_platform": "SEC corpus search",
        "vehicle_taxonomy": "holder-search result",
        "capital_channel_group": "search status",
        "public_or_private_visibility": "local SEC source corpus",
        "confidence": "medium",
    },
    "Stone Point / SEC R24 filing source": {
        "manager_or_platform": "Stone Point",
        "vehicle_taxonomy": "SEC R24 filing source",
        "capital_channel_group": "private credit / filing-source route evidence",
        "public_or_private_visibility": "SEC filing source",
        "confidence": "low-medium",
    },
    "Bain Capital": {
        "manager_or_platform": "Bain Capital",
        "vehicle_taxonomy": "sponsor transaction source",
        "capital_channel_group": "sponsor transaction context",
        "public_or_private_visibility": "public transaction release",
        "confidence": "high",
    },
    "The Sterling Group": {
        "manager_or_platform": "The Sterling Group",
        "vehicle_taxonomy": "seller transaction source",
        "capital_channel_group": "transaction context",
        "public_or_private_visibility": "public transaction release",
        "confidence": "high",
    },
    "Latham & Watkins LLP": {
        "manager_or_platform": "Latham & Watkins",
        "vehicle_taxonomy": "legal-advisor financing source",
        "capital_channel_group": "financing-source context",
        "public_or_private_visibility": "public legal-advisor note",
        "confidence": "high",
    },
    "BayPine LP": {
        "manager_or_platform": "BayPine",
        "vehicle_taxonomy": "sponsor transaction source",
        "capital_channel_group": "sponsor transaction context",
        "public_or_private_visibility": "public transaction release",
        "confidence": "high",
    },
    "Shell / Pennzoil Quaker State Company": {
        "manager_or_platform": "Shell",
        "vehicle_taxonomy": "seller transaction source",
        "capital_channel_group": "transaction value context",
        "public_or_private_visibility": "public transaction release",
        "confidence": "high",
    },
    "Jiffy Lube / Shell web page": {
        "manager_or_platform": "Shell / Jiffy Lube",
        "vehicle_taxonomy": "seller transaction source",
        "capital_channel_group": "transaction value context",
        "public_or_private_visibility": "public company web page",
        "confidence": "high",
    },
    "Shell USA": {
        "manager_or_platform": "Shell",
        "vehicle_taxonomy": "seller transaction source",
        "capital_channel_group": "transaction context",
        "public_or_private_visibility": "public company web page",
        "confidence": "high",
    },
    "Shell Global": {
        "manager_or_platform": "Shell",
        "vehicle_taxonomy": "seller transaction source",
        "capital_channel_group": "transaction context",
        "public_or_private_visibility": "public company web page",
        "confidence": "high",
    },
}


def value(row: dict[str, str], *keys: str) -> str:
    for key in keys:
        if row.get(key):
            return row[key]
    return ""


def load_vehicle_taxonomy() -> dict[str, dict[str, str]]:
    path = DATA / "capital-flow-vehicle-taxonomy.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["reporting_entity"]: row for row in csv.DictReader(handle)}


def taxonomy_for(entity: str, taxonomy: dict[str, dict[str, str]]) -> dict[str, str]:
    lookup = ENTITY_ALIASES.get(entity, entity)
    row = taxonomy.get(lookup) or FALLBACK_TAXONOMY.get(lookup)
    if row:
        return {
            "manager_or_platform": row.get("manager_or_platform", ""),
            "vehicle_taxonomy": row.get("vehicle_taxonomy", ""),
            "capital_channel_group": row.get("capital_channel_group", ""),
            "source_visibility": row.get("public_or_private_visibility", ""),
            "holder_source_classification_confidence": row.get("confidence", ""),
        }
    return {
        "manager_or_platform": "",
        "vehicle_taxonomy": "unclassified source",
        "capital_channel_group": "unclassified",
        "source_visibility": "",
        "holder_source_classification_confidence": "low",
    }


def read_rows() -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    taxonomy = load_vehicle_taxonomy()
    for borrower, meta in BORROWERS.items():
        path = DATA / meta["csv"]
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                fair_value = value(row, "fair_value_usd_m")
                unfunded = value(row, "unfunded_commitment_usd_m")
                if not fair_value and not unfunded:
                    source_row_type = "holder-locator-row"
                elif unfunded and not fair_value:
                    source_row_type = "unfunded-commitment-row"
                elif fair_value and not unfunded:
                    source_row_type = "funded-holder-row"
                else:
                    source_row_type = "funded-and-unfunded-holder-row"
                normalized.append(
                    {
                        "canonical_borrower": borrower,
                        "sector_lane": meta["sector"],
                        "sponsor_or_counterparty": meta["sponsor"],
                        "source_artifact": meta["artifact"],
                        "source_row_type": source_row_type,
                        "reporting_entity": value(row, "reporting_entity"),
                        **taxonomy_for(value(row, "reporting_entity"), taxonomy),
                        "cik": value(row, "cik"),
                        "borrower_or_credit_name": value(row, "borrower_or_credit_name", "borrower"),
                        "period": value(row, "period"),
                        "loan_type": value(row, "loan_type"),
                        "industry": value(row, "industry"),
                        "rate_or_coupon": value(row, "rate_or_coupon", "rate"),
                        "maturity": value(row, "maturity"),
                        "funded_or_par_amount_usd_m": value(row, "funded_or_par_amount_usd_m", "funded_principal_usd_m"),
                        "fair_value_usd_m": fair_value,
                        "unfunded_commitment_usd_m": unfunded,
                        "transaction_or_bank_denominator_usd_m": "200.0000" if borrower == "Atwell" else "",
                        "source_url": value(row, "source_url"),
                        "local_path": value(row, "local_path"),
                        "source_location": value(row, "source_location"),
                        "row_to_transaction_confidence": meta["confidence"],
                        "facility_size_status": meta["facility"],
                        "bank_replacement_status": meta["bank"],
                        "safe_claim": meta["safe"],
                        "do_not_claim": DO_NOT_CLAIM,
                        "status": "normalized-holder-expansion-row",
                    }
                )

    jiffy_path = DATA / "capital-flow-jiffy-transaction-gap-pass.csv"
    with jiffy_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            normalized.append(
                {
                    "canonical_borrower": "Jiffy Lube / Premium Velocity Auto",
                    "sector_lane": "automotive services franchising",
                    "sponsor_or_counterparty": value(row, "sponsor_or_counterparty"),
                    "source_artifact": "capital-flow-jiffy-transaction-gap-pass.md",
                    "source_row_type": value(row, "evidence_type") or "transaction-context-row",
                    "reporting_entity": value(row, "reporting_entity"),
                    **taxonomy_for(value(row, "reporting_entity"), taxonomy),
                    "cik": "",
                    "borrower_or_credit_name": value(row, "borrower_or_transaction"),
                    "period": value(row, "period"),
                    "loan_type": "",
                    "industry": "",
                    "rate_or_coupon": "",
                    "maturity": "",
                    "funded_or_par_amount_usd_m": "",
                    "fair_value_usd_m": "",
                    "unfunded_commitment_usd_m": "",
                    "transaction_or_bank_denominator_usd_m": value(row, "amount_usd_m"),
                    "source_url": value(row, "source_url"),
                    "local_path": value(row, "local_path"),
                    "source_location": value(row, "source_location"),
                    "row_to_transaction_confidence": "transaction-value-and-financing-role-visible; holder-row-missing",
                    "facility_size_status": "facility-size-missing",
                    "bank_replacement_status": "bank-replacement-unproven",
                    "safe_claim": "Jiffy/PVA has transaction-value and Ares financing-role evidence, but no reliable holder-dollar row has been captured yet.",
                    "do_not_claim": DO_NOT_CLAIM,
                    "status": "normalized-transaction-gap-row",
                }
            )

    seen_denominators: set[tuple[str, str]] = set()
    for row in normalized:
        denominator = row["transaction_or_bank_denominator_usd_m"]
        if not denominator:
            continue
        key = (row["canonical_borrower"], denominator)
        if key in seen_denominators:
            row["transaction_or_bank_denominator_usd_m"] = ""
        else:
            seen_denominators.add(key)

    for index, row in enumerate(normalized, start=1):
        row["row_id"] = f"ARBHE-001-{index:03d}"
    return normalized


def as_float(value: str) -> float:
    if not value:
        return 0.0
    try:
        return float(value)
    except ValueError:
        return 0.0


def period_rank(period: str) -> int:
    text = period.strip()
    match = re.fullmatch(r"Q([1-4])\s+(\d{4})", text, flags=re.IGNORECASE)
    if match:
        return int(match.group(2)) * 10 + int(match.group(1))
    match = re.fullmatch(r"FY(\d{4})(?:\s+comparative)?", text, flags=re.IGNORECASE)
    if match:
        return int(match.group(1)) * 10 + 4
    match = re.fullmatch(r"(\d{4})", text)
    if match:
        return int(match.group(1)) * 10 + 4
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        return int(match.group(1)) * 10
    return 0


def is_actual_period_row(row: dict[str, str]) -> bool:
    if row["period"].lower().startswith("latest visible"):
        return False
    if row["reporting_entity"] in {"KKR filing vehicles", "Multiple filing vehicles", "Multiple sources"}:
        return False
    if row["capital_channel_group"] in {"multi-vehicle summary", "derived summary", "search status"}:
        return False
    if row["source_row_type"] not in {
        "funded-holder-row",
        "funded-and-unfunded-holder-row",
        "unfunded-commitment-row",
    }:
        return False
    return bool(row["fair_value_usd_m"] or row["unfunded_commitment_usd_m"])


def same_period_fair_value(row: dict[str, str]) -> float:
    if "unfunded commitment" in row["loan_type"].lower():
        return 0.0
    return as_float(row["fair_value_usd_m"])


def borrower_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    summary = []
    for borrower in [*BORROWERS.keys(), "Jiffy Lube / Premium Velocity Auto"]:
        group = [row for row in rows if row["canonical_borrower"] == borrower]
        summary.append(
            {
                "borrower": borrower,
                "sector": group[0]["sector_lane"],
                "rows": len(group),
                "funded_rows": sum(1 for row in group if row["fair_value_usd_m"]),
                "commitment_rows": sum(1 for row in group if row["unfunded_commitment_usd_m"]),
                "fair_value": sum(as_float(row["fair_value_usd_m"]) for row in group),
                "unfunded": sum(as_float(row["unfunded_commitment_usd_m"]) for row in group),
                "transaction": max(as_float(row["transaction_or_bank_denominator_usd_m"]) for row in group),
                "gap": group[0]["facility_size_status"],
            }
        )
    return summary


def master_totals() -> dict[str, float]:
    totals = {
        "latest_visible_funded_fair_value_usd_m": 0.0,
        "mixed_quarter_visible_funded_fair_value_usd_m": 0.0,
        "visible_unfunded_commitment_usd_m": 0.0,
        "transaction_or_bank_denominator_usd_m": 0.0,
    }
    with MASTER_ROLLUP.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            for key in totals:
                totals[key] += as_float(row.get(key, ""))
    return totals


def master_by_borrower() -> dict[str, dict[str, str]]:
    with MASTER_ROLLUP.open(newline="", encoding="utf-8") as handle:
        return {row["borrower"]: row for row in csv.DictReader(handle)}


def same_period_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    master = master_by_borrower()
    summaries: list[dict[str, str]] = []
    for index, borrower in enumerate([*BORROWERS.keys(), "Jiffy Lube / Premium Velocity Auto"], start=1):
        group = [row for row in rows if row["canonical_borrower"] == borrower]
        actual_rows = [row for row in group if is_actual_period_row(row)]
        selected_period = ""
        selected_rank = 0
        selected_rows: list[dict[str, str]] = []
        if actual_rows:
            selected_rank = max(period_rank(row["period"]) for row in actual_rows)
            selected_periods = sorted({row["period"] for row in actual_rows if period_rank(row["period"]) == selected_rank})
            selected_period = selected_periods[-1]
            selected_rows = [row for row in actual_rows if row["period"] == selected_period]

        excluded_rows = [row for row in actual_rows if row not in selected_rows]
        master_row = master.get(borrower, {})
        summaries.append(
            {
                "summary_id": f"ARBHSP-001-{index:03d}",
                "canonical_borrower": borrower,
                "sector_lane": group[0]["sector_lane"],
                "selected_period": selected_period or "no holder-dollar period captured",
                "selected_period_rank": str(selected_rank) if selected_rank else "",
                "same_period_rows": str(len(selected_rows)),
                "same_period_reporting_entities": "; ".join(sorted({row["reporting_entity"] for row in selected_rows})),
                "same_period_capital_channel_groups": "; ".join(sorted({row["capital_channel_group"] for row in selected_rows})),
                "same_period_fair_value_usd_m": f"{sum(same_period_fair_value(row) for row in selected_rows):.4f}" if selected_rows else "",
                "same_period_unfunded_commitment_usd_m": f"{sum(as_float(row['unfunded_commitment_usd_m']) for row in selected_rows):.4f}" if selected_rows else "",
                "same_period_transaction_or_bank_denominator_usd_m": f"{max(as_float(row['transaction_or_bank_denominator_usd_m']) for row in group):.4f}" if any(row["transaction_or_bank_denominator_usd_m"] for row in group) else "",
                "excluded_periods": "; ".join(sorted({row["period"] for row in excluded_rows})),
                "excluded_row_count": str(len(excluded_rows)),
                "master_latest_visible_funded_fair_value_usd_m": master_row.get("latest_visible_funded_fair_value_usd_m", ""),
                "master_mixed_quarter_visible_funded_fair_value_usd_m": master_row.get("mixed_quarter_visible_funded_fair_value_usd_m", ""),
                "master_visible_unfunded_commitment_usd_m": master_row.get("visible_unfunded_commitment_usd_m", ""),
                "same_period_status": "same-period-holder-summary-visible" if selected_rows else "transaction-context-only-no-holder-period",
                "what_it_says": "This row selects one actual reporting period for the borrower to avoid mixing Q2, Q1, FY, comparative, and derived latest-visible rows.",
                "what_it_does_not_say": "This is not full facility size, not total borrower debt, not Ares allocation, not bank replacement, and not the broader mixed-quarter reach metric.",
            }
        )
    return summaries


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_same_period_csv(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    summaries = same_period_summary(rows)
    with SAME_PERIOD_OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SAME_PERIOD_FIELDS)
        writer.writeheader()
        writer.writerows(summaries)
    return summaries


def write_markdown(rows: list[dict[str, str]]) -> None:
    summary = borrower_summary(rows)
    same_period = same_period_summary(rows)
    rollup = master_totals()
    total_fair = sum(item["fair_value"] for item in summary)
    total_unfunded = sum(item["unfunded"] for item in summary)
    total_transaction = sum(item["transaction"] for item in summary)
    holder_rows = sum(1 for row in rows if row["source_row_type"] in {"funded-holder-row", "funded-and-unfunded-holder-row"})
    commitment_rows = sum(1 for row in rows if row["source_row_type"] == "unfunded-commitment-row")
    channel_counts = Counter(row["capital_channel_group"] for row in rows)

    lines = [
        "# Capital Flow Ares Borrower Holder Expansion Pass 1",
        "",
        "## Purpose",
        "",
        "This pass normalizes the borrower-level holder work across the Ares selected-borrower lane.",
        "",
        "The operating table is:",
        "",
        "`analysis/company-first-principles/data/capital-flow-ares-borrower-holder-expansion-pass-1.csv`",
        "",
        "It does not replace the individual borrower crosswalks. It turns them into one row-level proof table that preserves holder vehicle, vehicle taxonomy, capital-channel group, period, instrument, funded value, unfunded commitment, transaction context, and claim boundary.",
        "",
        "## Source Set",
        "",
        "The normalized source set covers:",
        "",
        "- AeriTek",
        "- Atwell",
        "- Frontline Road Safety",
        "- MAI Capital",
        "- Precinmac",
        "- Relation Insurance",
        "- Sunvair",
        "- Valcourt",
        "- Jiffy Lube / Premium Velocity Auto",
        "",
        "## Normalized Result",
        "",
        f"The pass emits `{len(rows)}` normalized rows across `{len(channel_counts)}` holder/source channel groups: `{holder_rows}` funded-holder rows, `{commitment_rows}` pure unfunded-commitment rows, plus holder-locator and transaction-gap rows.",
        "",
        "The row-level table preserves every extracted row, including historical, comparative, mixed-quarter, and locator rows. Its row-level sums are useful for audit coverage, not for promoted exposure totals:",
        "",
        "| Metric | Amount | Boundary |",
        "|---|---:|---|",
        f"| Row-level fair-value audit sum | `{total_fair:.4f}M USD` | Mixed periods and comparative rows; do not promote as same-date exposure. |",
        f"| Row-level unfunded-commitment audit sum | `{total_unfunded:.4f}M USD` | Mixed periods and commitment rows; do not add to drawn exposure. |",
        f"| Unique borrower transaction / bank denominator context | `{total_transaction:.4f}M USD` | Atwell prior bank facility plus Jiffy sale value; not facility-size proof for the other borrowers. |",
        "",
        "For promoted borrower-level totals, use the master rollup rather than the row-level audit sum:",
        "",
        "| Master-Rollup Metric | Amount | Boundary |",
        "|---|---:|---|",
        f"| Latest visible funded fair value across holder-dollar cases | `{rollup['latest_visible_funded_fair_value_usd_m']:.4f}M USD` | Deduped by borrower case at the current best visible period. |",
        f"| Mixed-quarter visible funded fair value, including selected extra rows | `{rollup['mixed_quarter_visible_funded_fair_value_usd_m']:.4f}M USD` | Useful for reach, not same-date exposure. |",
        f"| Visible unfunded commitments across cases | `{rollup['visible_unfunded_commitment_usd_m']:.4f}M USD` | Commitments are not drawn debt. |",
        f"| Hard transaction / bank denominator values captured | `{rollup['transaction_or_bank_denominator_usd_m']:.4f}M USD` | Atwell prior bank facility plus Jiffy transaction value. |",
        "",
        "The same-period borrower summary is:",
        "",
        "`analysis/company-first-principles/data/capital-flow-ares-borrower-same-period-exposure-summary-pass-1.csv`",
        "",
        "It selects one actual reporting period per borrower before summing fair value or commitments.",
        "",
        "## Holder-Source Taxonomy",
        "",
        "The taxonomy layer classifies each reporting entity or transaction source before any source-of-capital claim is promoted.",
        "",
        "| Capital Channel Group | Normalized Rows | Boundary |",
        "|---|---:|---|",
    ]

    channel_boundaries = {
        "public BDC": "SEC-reporting BDC holder rows; does not identify ultimate shareholder source.",
        "non-traded BDC / private credit fund": "Private or non-listed credit vehicle visibility; investor channel still needs vehicle documents.",
        "direct lending program / private credit vehicle": "Program-level holder visibility; ownership and capital source still need vehicle notes.",
        "registered credit fund": "Registered fund holder visibility; not whole facility proof.",
        "private credit fund": "Private credit fund holder visibility; investor source still unproven.",
        "middle-market lending fund": "Middle-market fund holder visibility, often historical.",
        "financing arranger role only": "Arranger/bookrunner context; not funded allocation.",
        "sponsor transaction context": "Sponsor transaction source; not lender allocation.",
        "transaction context": "Transaction source context; not holder evidence or facility-size proof.",
        "seller transaction source": "Seller or company transaction source; not holder evidence.",
        "transaction value context": "Transaction value source; not debt facility size unless source says so.",
        "financing-source context": "Legal-advisor financing context; not full lender group.",
        "multi-vehicle summary": "Derived summary row; use underlying rows for holder proof.",
        "derived summary": "Computed gap/status row; not a holder vehicle.",
        "search status": "Search-result status row; not exposure proof.",
        "private credit / filing-source route evidence": "Route evidence with unit/context limits.",
    }
    for channel, count in sorted(channel_counts.items()):
        lines.append(f"| {channel or 'unclassified'} | `{count}` | {channel_boundaries.get(channel, 'Classification needs follow-up documentation.')} |")

    lines.extend(
        [
            "",
            "## Same-Period Borrower Summary",
            "",
            "This table is the conservative current-period control. It deliberately excludes derived `latest visible 2026` rows and older periods when a newer actual reporting period exists.",
            "",
            "| Borrower | Selected Period | Same-Period Rows | Fair Value | Unfunded Commitment | Excluded Periods | Boundary |",
            "|---|---|---:|---:|---:|---|---|",
        ]
    )
    for item in same_period:
        fair = f"`{item['same_period_fair_value_usd_m']}M USD`" if item["same_period_fair_value_usd_m"] else ""
        unfunded = f"`{item['same_period_unfunded_commitment_usd_m']}M USD`" if item["same_period_unfunded_commitment_usd_m"] else ""
        excluded = item["excluded_periods"] or ""
        lines.append(
            f"| {item['canonical_borrower']} | {item['selected_period']} | `{item['same_period_rows']}` | {fair} | {unfunded} | {excluded} | Not full facility size or total debt. |"
        )

    lines.extend(
        [
            "",
            "## Borrower Summary",
            "",
            "| Borrower | Sector Lane | Rows | Funded Rows | Commitment Rows | Fair Value Sum | Unfunded Sum | Transaction / Bank Denominator | Main Boundary |",
            "|---|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for item in summary:
        fair = f"`{item['fair_value']:.4f}M USD`" if item["fair_value"] else ""
        unfunded = f"`{item['unfunded']:.4f}M USD`" if item["unfunded"] else ""
        transaction = f"`{item['transaction']:.4f}M USD`" if item["transaction"] else ""
        lines.append(
            f"| {item['borrower']} | {item['sector']} | `{item['rows']}` | `{item['funded_rows']}` | `{item['commitment_rows']}` | {fair} | {unfunded} | {transaction} | `{item['gap']}` |"
        )

    lines.extend(
        [
            "",
            "## What This Adds",
            "",
            "This is the missing sector-level proof layer between individual borrower pages and the master rollup.",
            "",
            "The new table lets the research ask, row by row:",
            "",
            "- which credit vehicle holds the borrower exposure",
            "- whether the row is funded value, unfunded commitment, locator evidence, or transaction context",
            "- what borrower sector the exposure belongs to",
            "- whether transaction-role evidence is linked or still separate",
            "- whether facility size and bank replacement are proven or still missing",
            "",
            "## Safe Claim",
            "",
            "`The Ares borrower-destination lane now has a normalized holder-expansion table across nine borrower cases. The table preserves row-level holder vehicles, holder-source taxonomy, filing periods, instruments, funded fair values, unfunded commitments, transaction context, and proof boundaries. It supports borrower-destination claims across services, infrastructure-adjacent services, aerospace/industrial supply chains, insurance brokerage, wealth management, and automotive services, but it does not prove total facility size, Ares' exact funded amount, full lender groups, use of proceeds, ultimate capital source, or bank replacement.`",
            "",
            "## Claims Not To Make Yet",
            "",
            "Do not say:",
            "",
            "- the row-level fair-value sum is total private-credit exposure",
            "- visible BDC fair value equals total borrower debt",
            "- unfunded commitments are already drawn debt",
            "- every holder row maps to the named Ares selected-borrower transaction",
            "- private credit replaced banks in these cases unless borrower-specific payoff, termination, amendment, or lender replacement evidence exists",
            "",
            "## Next Concrete Work",
            "",
            "1. Search facility-size and bank-replacement documents for Frontline, Relation, Precinmac, and Valcourt first.",
            "2. Pull vehicle-level annual reports, prospectuses, and funding notes for public BDC and non-traded/private-credit vehicles.",
            "3. Add Q3 2026 schedule refresh checks for Jiffy/PVA and the borrowers with Q2-only evidence.",
            "4. Add a transaction-to-holder confidence upgrade only when a credit agreement, rating report, amendment, or lender allocation source links the rows.",
        ]
    )

    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows = read_rows()
    write_csv(rows)
    same_period = write_same_period_csv(rows)
    write_markdown(rows)
    print(f"wrote {len(rows)} rows to {OUTPUT_CSV.relative_to(ROOT)}")
    print(f"wrote {len(same_period)} rows to {SAME_PERIOD_OUTPUT_CSV.relative_to(ROOT)}")
    print(f"wrote report to {OUTPUT_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
