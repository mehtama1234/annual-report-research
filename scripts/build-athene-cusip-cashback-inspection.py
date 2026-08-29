#!/usr/bin/env python3
"""Rank high-dollar Athene CUSIP cash-back candidates for inspection."""

from __future__ import annotations

import csv
from collections import Counter
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
MATCH = DATA / "capital-flow-apollo-athene-statutory-cusip-cashback-match-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-cashback-high-dollar-inspection-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-cashback-high-dollar-inspection-diagnostic-pass-1.csv"

FIELDNAMES = [
    "inspection_row_id",
    "rank",
    "cusip",
    "identifier_quality",
    "match_status",
    "issuer_or_description_sample",
    "disposal_consideration_usd",
    "year_end_book_value_usd",
    "disposal_book_value_at_disposal_usd",
    "disposal_realized_gain_loss_usd",
    "disposal_interest_or_dividends_received_usd",
    "first_disposal_date",
    "last_disposal_date",
    "top_purchaser_or_disposition_type",
    "economic_disposition_class",
    "router_or_counterparty_signal",
    "candidate_tier",
    "proof_upgrade_test",
    "disproof_or_hold_test",
    "safe_interpretation",
    "boundary",
    "next_action",
]

DIAGNOSTIC_FIELDS = [
    "diagnostic_id",
    "metric",
    "value",
    "units",
    "proof_use",
    "boundary",
    "next_action",
]


def money(value: str) -> Decimal:
    value = (value or "").strip()
    if not value:
        return Decimal(0)
    negative = value.startswith("(") and value.endswith(")")
    cleaned = value.strip("()").replace(",", "")
    try:
        parsed = Decimal(cleaned)
    except Exception:
        return Decimal(0)
    return -parsed if negative else parsed


def fmt(value: Decimal) -> str:
    return f"{value:.6f}"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def disposition_class(label: str) -> str:
    lowered = (label or "").lower()
    if "tax free exchange" in lowered:
        return "tax-free-exchange-hold"
    if "paydown" in lowered:
        return "principal-paydown-cash-candidate"
    if "maturity" in lowered:
        return "maturity-proceeds-cash-candidate"
    if "redemption" in lowered or "call" in lowered:
        return "redemption-or-call-cash-candidate"
    if "security withdraw" in lowered or "withdraw" in lowered:
        return "security-withdrawal-hold"
    if "direct" in lowered or "private" in lowered:
        return "direct-or-private-transfer-hold"
    if not lowered:
        return "unclassified-hold"
    return "market-sale-or-counterparty-cash-candidate"


def router_signal(description: str, label: str) -> str:
    text = f"{description} {label}".lower()
    signals = []
    for name in [
        ("apollo", "Apollo"),
        ("blackstone", "Blackstone"),
        ("blue owl", "Blue Owl"),
        ("ares", "Ares"),
        ("kkr", "KKR"),
        ("goldman", "Goldman Sachs"),
        ("morgan stanley", "Morgan Stanley"),
        ("barclays", "Barclays"),
        ("jpm", "JPMorgan"),
        ("citigroup", "Citigroup"),
        ("bank of america", "Bank of America"),
    ]:
        if name[0] in text:
            signals.append(name[1])
    return "; ".join(signals) if signals else "no-major-router-label-detected"


def candidate_tier(row: dict[str, str], cls: str) -> str:
    if row["match_status"] != "holding-and-disposal-same-cusip-visible":
        return "tier-3-disposal-only-or-no-year-end-holding"
    if cls in {"tax-free-exchange-hold", "security-withdrawal-hold", "direct-or-private-transfer-hold"}:
        return "tier-2-same-cusip-noncash-or-transfer-hold"
    if cls in {
        "principal-paydown-cash-candidate",
        "maturity-proceeds-cash-candidate",
        "redemption-or-call-cash-candidate",
        "market-sale-or-counterparty-cash-candidate",
    }:
        return "tier-1-same-cusip-cash-candidate"
    return "tier-2-same-cusip-classification-hold"


def upgrade_test(row: dict[str, str], cls: str) -> str:
    if row["match_status"] != "holding-and-disposal-same-cusip-visible":
        return "prove full sale/maturity/paydown status or corrected year-end identifier, then reconcile consideration and book/gain/loss fields"
    if cls == "tax-free-exchange-hold":
        return "prove whether exchange generated cash or only replacement security; inspect lot rows and statutory Part 5 treatment"
    if cls == "principal-paydown-cash-candidate":
        return "reconcile paydown consideration to principal reduction, remaining year-end book value, and interest received"
    if cls == "maturity-proceeds-cash-candidate":
        return "reconcile maturity proceeds to prior book value, realized gain/loss, and cash-flow proceeds category"
    if cls == "redemption-or-call-cash-candidate":
        return "reconcile call/redemption price, book-at-disposal, gain/loss, and interest through disposal date"
    return "inspect source rows, counterparty label, numeric columns, and lot-level continuity before promotion"


def hold_test(cls: str) -> str:
    if cls == "tax-free-exchange-hold":
        return "hold if consideration represents exchange accounting rather than spendable cash"
    if cls == "security-withdrawal-hold":
        return "hold if row is withdrawal or transfer without sale/repayment cash"
    if cls == "direct-or-private-transfer-hold":
        return "hold unless direct/private transfer has cash settlement or sale evidence"
    return "hold if parser columns are shifted, duplicate subtotals exist, or proceeds cannot be tied to a real disposition"


def safe_interpretation(row: dict[str, str], cls: str, tier: str) -> str:
    if tier == "tier-1-same-cusip-cash-candidate":
        return "same-CUSIP candidate where Schedule D shows both year-end holding context and cash-like proceeds/disposition evidence"
    if tier == "tier-2-same-cusip-noncash-or-transfer-hold":
        return "same-CUSIP bridge exists, but disposition label may represent exchange, withdrawal, or transfer rather than realized cash"
    if row["match_status"] == "disposal-only-cusip-visible":
        return "named disposal/proceeds row visible, but no year-end holding match in the current Schedule D holdings parser"
    return "high-dollar row requires classification before any cash-back claim"


def main() -> None:
    rows = [
        row
        for row in read_rows(MATCH)
        if row["identifier_quality"] != "placeholder-identifier-hold"
        and money(row["disposal_consideration_usd"]) > 0
    ]
    rows = sorted(rows, key=lambda row: money(row["disposal_consideration_usd"]), reverse=True)[:100]

    output: list[dict[str, str]] = []
    for rank, row in enumerate(rows, start=1):
        cls = disposition_class(row["top_purchaser_or_disposition_type"])
        tier = candidate_tier(row, cls)
        output.append(
            {
                "inspection_row_id": f"CFAASCBCHI-{rank:03d}",
                "rank": str(rank),
                "cusip": row["cusip"],
                "identifier_quality": row["identifier_quality"],
                "match_status": row["match_status"],
                "issuer_or_description_sample": row["issuer_or_description_sample"],
                "disposal_consideration_usd": row["disposal_consideration_usd"],
                "year_end_book_value_usd": row["year_end_book_value_usd"],
                "disposal_book_value_at_disposal_usd": row["disposal_book_value_at_disposal_usd"],
                "disposal_realized_gain_loss_usd": row["disposal_realized_gain_loss_usd"],
                "disposal_interest_or_dividends_received_usd": row["disposal_interest_or_dividends_received_usd"],
                "first_disposal_date": row["first_disposal_date"],
                "last_disposal_date": row["last_disposal_date"],
                "top_purchaser_or_disposition_type": row["top_purchaser_or_disposition_type"],
                "economic_disposition_class": cls,
                "router_or_counterparty_signal": router_signal(
                    row["issuer_or_description_sample"], row["top_purchaser_or_disposition_type"]
                ),
                "candidate_tier": tier,
                "proof_upgrade_test": upgrade_test(row, cls),
                "disproof_or_hold_test": hold_test(cls),
                "safe_interpretation": safe_interpretation(row, cls, tier),
                "boundary": "ranked inspection row; not final lot-level continuity, borrower cash, liability-cost spread, or asset-return proof",
                "next_action": "inspect raw source rows for this CUSIP and reconcile consideration, book value, gain/loss, interest, and disposition economics",
            }
        )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(output)

    tier_counts = Counter(row["candidate_tier"] for row in output)
    class_counts = Counter(row["economic_disposition_class"] for row in output)
    same_cusip_consideration = sum(
        money(row["disposal_consideration_usd"])
        for row in output
        if row["match_status"] == "holding-and-disposal-same-cusip-visible"
    )
    tier1_consideration = sum(
        money(row["disposal_consideration_usd"])
        for row in output
        if row["candidate_tier"] == "tier-1-same-cusip-cash-candidate"
    )
    total_consideration = sum(money(row["disposal_consideration_usd"]) for row in output)
    diagnostics: list[tuple[str, Decimal | str, str]] = [
        ("inspection_rows", Decimal(len(output)), "count"),
        ("total_top100_consideration", total_consideration, "USD"),
        ("same_cusip_top100_consideration", same_cusip_consideration, "USD"),
        ("tier1_same_cusip_cash_candidate_count", Decimal(tier_counts["tier-1-same-cusip-cash-candidate"]), "count"),
        ("tier1_same_cusip_cash_candidate_consideration", tier1_consideration, "USD"),
        ("tier2_same_cusip_noncash_or_transfer_hold_count", Decimal(tier_counts["tier-2-same-cusip-noncash-or-transfer-hold"]), "count"),
        ("tier3_disposal_only_or_no_year_end_holding_count", Decimal(tier_counts["tier-3-disposal-only-or-no-year-end-holding"]), "count"),
    ]
    for cls, count in class_counts.most_common():
        diagnostics.append((f"economic_class_count__{cls}", Decimal(count), "count"))

    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAASCBCHID-{idx:03d}",
                    "metric": metric,
                    "value": fmt(value) if isinstance(value, Decimal) and units == "USD" else str(int(value)),
                    "units": units,
                    "proof_use": "high-dollar CUSIP cash-back candidate ranking and disposition classification",
                    "boundary": "classification is heuristic and supports inspection priority, not final accounting or return proof",
                    "next_action": "inspect source rows for tier-1 candidates first, then decide whether tier-2 rows are noncash exchanges/transfers or real cash settlements",
                }
            )

    print(f"wrote {len(output)} rows to {OUT}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT}")
    print(dict(tier_counts))
    print(dict(class_counts))


if __name__ == "__main__":
    main()

