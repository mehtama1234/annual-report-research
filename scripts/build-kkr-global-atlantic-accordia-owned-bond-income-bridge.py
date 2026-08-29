#!/usr/bin/env python3
"""Bridge Accordia coordinate-owned Schedule D bonds to legal-entity income."""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"

OWNED = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-pass-1.csv"
COMPACT = DATA / "capital-flow-kkr-global-atlantic-accordia-compact-extraction-pass-1.csv"

OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-pass-1.csv"
DETAIL_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-detail-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-pass-1.md"

FIELDNAMES = [
    "bridge_row_id",
    "bridge_layer",
    "metric",
    "value",
    "units",
    "proof_use",
    "boundary",
    "next_action",
]

DETAIL_FIELDS = [
    "detail_row_id",
    "coordinate_row_id",
    "schedule_part",
    "page",
    "cusip",
    "cusip_marker_type",
    "book_adjusted_carrying_value",
    "interest_income_due_accrued",
    "interest_received_during_year",
    "payment_due_at_maturity",
    "simple_interest_received_on_book_pct",
    "proof_use",
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


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def money(value: str) -> Decimal:
    value = (value or "").strip()
    if not value:
        return Decimal(0)
    negative = value.startswith("(") and value.endswith(")")
    parsed = Decimal(value.strip("()").replace(",", ""))
    return -parsed if negative else parsed


def fmt_decimal(value: Decimal, places: int = 6) -> str:
    return f"{value:.{places}f}"


def fmt_int(value: Decimal) -> str:
    return str(int(value))


def pct(numerator: Decimal, denominator: Decimal) -> Decimal:
    if not denominator:
        return Decimal(0)
    return numerator / denominator * Decimal(100)


def compact_values() -> dict[str, Decimal]:
    return {row["field"]: money(row["value"]) for row in read_rows(COMPACT)}


def owned_totals(rows: list[dict[str, str]]) -> dict[str, Decimal]:
    return {
        "book": sum(money(row["book_adjusted_carrying_value"]) for row in rows),
        "interest_due_accrued": sum(money(row["interest_income_due_accrued"]) for row in rows),
        "interest_received": sum(money(row["interest_received_during_year"]) for row in rows),
        "payment_due_at_maturity": sum(money(row["payment_due_at_maturity"]) for row in rows),
    }


def filtered(rows: list[dict[str, str]], **criteria: str) -> list[dict[str, str]]:
    out = rows
    for key, value in criteria.items():
        out = [row for row in out if row[key] == value]
    return out


def add_bridge(rows: list[dict[str, str]], layer: str, metric: str, value: str, units: str, proof_use: str, boundary: str, next_action: str) -> None:
    rows.append(
        {
            "bridge_row_id": f"CFKKRGACOBIB-{len(rows)+1:03d}",
            "bridge_layer": layer,
            "metric": metric,
            "value": value,
            "units": units,
            "proof_use": proof_use,
            "boundary": boundary,
            "next_action": next_action,
        }
    )


def build_bridge_rows(owned_rows: list[dict[str, str]], values: dict[str, Decimal]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    totals = owned_totals(owned_rows)
    issuer = owned_totals([r for r in owned_rows if r["schedule_part"].endswith("issuer-credit obligations owned")])
    abs_rows = owned_totals([r for r in owned_rows if r["schedule_part"].endswith("asset-backed securities owned")])
    private = owned_totals(filtered(owned_rows, cusip_marker_type="statutory-private-marker-cusip"))
    standard = owned_totals(filtered(owned_rows, cusip_marker_type="standard-cusip-like"))
    gross_income = values["total_gross_investment_income_collected"]
    net_income = values["summary_net_investment_income"]
    cash_net_income = values["cash_flow_net_investment_income"]
    bond_base = values["bonds_schedule_d_net_admitted_assets"]
    life_reserves = values["aggregate_reserve_for_life_contracts"]
    funds_held = values["funds_held_under_coinsurance"]

    add_bridge(rows, "owned-bond-baseline", "coordinate_owned_bond_book_value", fmt_int(totals["book"]), "USD", "near-reconciled owned Schedule D bond baseline", "book value is not income, proceeds, borrower receipt, or return", "join to income, proceeds, and liability context")
    add_bridge(rows, "owned-bond-baseline", "statutory_bond_net_admitted_assets", fmt_int(bond_base), "USD", "statutory target for owned Schedule D bond base", "summary statutory line is not CUSIP-level income proof", "keep as reconciliation denominator")
    add_bridge(rows, "owned-bond-baseline", "owned_bond_book_variance_vs_statutory_target", fmt_int(totals["book"] - bond_base), "USD", "near-reconciliation residual", "small variance does not prove cash return", "retain tolerance check before downstream joins")
    add_bridge(rows, "income-cash-back", "owned_bond_interest_received_during_year", fmt_int(totals["interest_received"]), "USD", "row-level owned-bond interest received cash-back proxy", "interest received is not borrower receipt/use or net return after liability cost", "rank named rows and join to issuer/wrapper evidence")
    add_bridge(rows, "income-cash-back", "owned_bond_interest_due_accrued", fmt_int(totals["interest_due_accrued"]), "USD", "row-level owned-bond income/accrual context", "due/accrued is not cash received", "separate cash received from accrual field")
    add_bridge(rows, "income-cash-back", "owned_bond_payment_due_at_maturity", fmt_int(totals["payment_due_at_maturity"]), "USD", "contractual maturity endpoint context", "payment due at maturity is not current cash received", "use for maturity/payback route only with disposal or maturity evidence")
    add_bridge(rows, "legal-entity-income", "total_gross_investment_income_collected", fmt_int(gross_income), "USD", "legal-entity gross investment income denominator", "not allocated to each owned bond row", "reconcile owned-bond interest to gross income categories")
    add_bridge(rows, "legal-entity-income", "summary_net_investment_income", fmt_int(net_income), "USD", "legal-entity net investment income bridge", "not asset-level net spread", "join expenses, liability cost, and asset classes")
    add_bridge(rows, "legal-entity-income", "cash_flow_net_investment_income", fmt_int(cash_net_income), "USD", "cash-flow support for net investment income", "not allocated to holdings", "compare with statutory income exhibit")
    add_bridge(rows, "income-coverage", "owned_bond_interest_received_to_gross_income_pct", fmt_decimal(pct(totals["interest_received"], gross_income)), "percent", "shows owned-bond received-interest share of gross investment income", "ratio is category bridge, not issuer-level return", "identify remaining income from mortgage loans, affiliates, other invested assets, and other buckets")
    add_bridge(rows, "income-coverage", "owned_bond_interest_received_to_net_investment_income_pct", fmt_decimal(pct(totals["interest_received"], net_income)), "percent", "shows received-interest scale against net investment income", "ratio does not allocate expenses or liability cost", "build liability spread bridge")
    add_bridge(rows, "income-coverage", "owned_bond_interest_received_to_cash_flow_net_investment_income_pct", fmt_decimal(pct(totals["interest_received"], cash_net_income)), "percent", "compares row-level interest received with cash-flow net investment income", "cash-flow line remains entity-level", "separate collected cash from statutory net income")
    add_bridge(rows, "yield-proxy", "owned_bond_interest_received_on_book_pct", fmt_decimal(pct(totals["interest_received"], totals["book"])), "percent", "simple owned-bond cash-yield proxy", "not IRR, NPV, net spread, or total return", "subtract liability cost and include credit marks before any return claim")
    add_bridge(rows, "yield-proxy", "owned_bond_interest_due_accrued_on_book_pct", fmt_decimal(pct(totals["interest_due_accrued"], totals["book"])), "percent", "simple accrual-yield context", "not cash yield", "compare against received-interest yield and liability cost")
    add_bridge(rows, "schedule-split", "issuer_credit_interest_received", fmt_int(issuer["interest_received"]), "USD", "issuer-credit owned-bond cash-back proxy", "not issuer-level return", "rank named issuer-credit rows")
    add_bridge(rows, "schedule-split", "abs_interest_received", fmt_int(abs_rows["interest_received"]), "USD", "ABS owned-bond cash-back proxy", "not collateral remittance or waterfall proof", "rank ABS rows for trustee/remittance proof")
    add_bridge(rows, "marker-split", "statutory_private_marker_interest_received", fmt_int(private["interest_received"]), "USD", "private-marker row cash-back proxy", "private marker does not identify public borrower receipt/use by itself", "map private-marker CUSIPs to issuer/wrapper documents")
    add_bridge(rows, "marker-split", "standard_cusip_like_interest_received", fmt_int(standard["interest_received"]), "USD", "standard CUSIP row cash-back proxy", "CUSIP visibility does not prove borrower use or waterfall", "map largest standard-CUSIP rows to public issuer evidence")
    add_bridge(rows, "liability-context", "life_reserve_liability", fmt_int(life_reserves), "USD", "insurance liability source-pool context", "not liability-cost spread", "find credited-rate or liability-cost schedule")
    add_bridge(rows, "liability-context", "funds_held_under_coinsurance", fmt_int(funds_held), "USD", "funds-held/coinsurance liability route context", "not treaty waterfall or cash availability", "find funds-held economics and reinsurance treaty support")
    return rows


def build_detail_rows(owned_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    ranked = sorted(owned_rows, key=lambda row: money(row["interest_received_during_year"]), reverse=True)
    out: list[dict[str, str]] = []
    for row in ranked[:40]:
        book = money(row["book_adjusted_carrying_value"])
        interest = money(row["interest_received_during_year"])
        out.append(
            {
                "detail_row_id": f"CFKKRGACOBIBD-{len(out)+1:03d}",
                "coordinate_row_id": row["coordinate_row_id"],
                "schedule_part": row["schedule_part"],
                "page": row["page"],
                "cusip": row["cusip"],
                "cusip_marker_type": row["cusip_marker_type"],
                "book_adjusted_carrying_value": row["book_adjusted_carrying_value"],
                "interest_income_due_accrued": row["interest_income_due_accrued"],
                "interest_received_during_year": row["interest_received_during_year"],
                "payment_due_at_maturity": row["payment_due_at_maturity"],
                "simple_interest_received_on_book_pct": fmt_decimal(pct(interest, book)) if book else "",
                "proof_use": "ranked named owned-bond cash-back proxy row",
                "boundary": "ranked row shows statutory interest received, not borrower receipt/use, remittance waterfall, liability spread, or final return",
                "next_action": "map high-interest CUSIP to issuer/wrapper documents and test income/proceeds continuity",
            }
        )
    return out


def diagnostic_rows(bridge_rows: list[dict[str, str]], detail_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    wanted = {
        row["metric"]: row["value"]
        for row in bridge_rows
    }
    metrics: list[tuple[str, str, str]] = [
        ("bridge_rows", str(len(bridge_rows)), "count"),
        ("detail_rows", str(len(detail_rows)), "count"),
        ("coordinate_owned_bond_book_value", wanted["coordinate_owned_bond_book_value"], "USD"),
        ("owned_bond_interest_received_during_year", wanted["owned_bond_interest_received_during_year"], "USD"),
        ("owned_bond_interest_due_accrued", wanted["owned_bond_interest_due_accrued"], "USD"),
        ("total_gross_investment_income_collected", wanted["total_gross_investment_income_collected"], "USD"),
        ("summary_net_investment_income", wanted["summary_net_investment_income"], "USD"),
        ("cash_flow_net_investment_income", wanted["cash_flow_net_investment_income"], "USD"),
        ("owned_bond_interest_received_to_gross_income_pct", wanted["owned_bond_interest_received_to_gross_income_pct"], "percent"),
        ("owned_bond_interest_received_to_net_investment_income_pct", wanted["owned_bond_interest_received_to_net_investment_income_pct"], "percent"),
        ("owned_bond_interest_received_on_book_pct", wanted["owned_bond_interest_received_on_book_pct"], "percent"),
        ("full_named_cash_proof_upgrades", "0", "count"),
        ("next_parser", "accordia-owned-bond-income-proceeds-cusip-match", "parser"),
    ]
    out: list[dict[str, str]] = []
    for idx, (metric, value, units) in enumerate(metrics, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGACOBIBX-{idx:03d}",
                "metric": metric,
                "value": value,
                "units": units,
                "proof_use": "controls Accordia owned-bond income bridge status",
                "boundary": "Income bridge proves statutory row-level received-interest and legal-entity income context only; it does not prove borrower receipt/use, liability spread, waterfall, collateral certificate, or return.",
                "next_action": "Use ranked rows for CUSIP-level issuer/wrapper mapping and disposal/proceeds continuity tests.",
            }
        )
    return out


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def table(rows: list[dict[str, str]], limit: int = 12) -> str:
    return "\n".join(
        "| {detail_row_id} | {cusip} | {cusip_marker_type} | {book_adjusted_carrying_value} | {interest_received_during_year} | {simple_interest_received_on_book_pct} |".format(**row)
        for row in rows[:limit]
    )


def write_memo(bridge_rows: list[dict[str, str]], detail_rows: list[dict[str, str]], diagnostics: list[dict[str, str]]) -> None:
    metric = {row["metric"]: row["value"] for row in bridge_rows}
    diag = {row["metric"]: row["value"] for row in diagnostics}
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Accordia Owned-Bond Income Bridge Pass 1

## Purpose

This pass joins the near-reconciled Accordia coordinate owned-bond table to legal-entity income and cash-flow context.

It asks:

`Can the KKR/Global Atlantic Accordia statutory prototype move from owned-bond book-value reconciliation to row-level interest-received evidence and legal-entity income context without claiming full borrower cash return?`

The structured bridge table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-pass-1.csv`

The ranked detail table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-detail-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-diagnostic-pass-1.csv`

## Short Answer

`Accordia now has row-level owned-bond cash-back proxy evidence. The coordinate owned-bond base is {metric['coordinate_owned_bond_book_value']} USD. Owned Schedule D bond rows show {metric['owned_bond_interest_received_during_year']} USD of interest received during the year and {metric['owned_bond_interest_due_accrued']} USD of interest due/accrued. Interest received equals {metric['owned_bond_interest_received_to_gross_income_pct']}% of legal-entity gross investment income, {metric['owned_bond_interest_received_to_net_investment_income_pct']}% of summary net investment income, and a simple {metric['owned_bond_interest_received_on_book_pct']}% of coordinate owned-bond book value.`

## Bridge Metrics

| Metric | Value | Units |
|---|---:|---|
| Coordinate owned-bond book value | {metric['coordinate_owned_bond_book_value']} | USD |
| Statutory bond base | {metric['statutory_bond_net_admitted_assets']} | USD |
| Owned-bond interest received | {metric['owned_bond_interest_received_during_year']} | USD |
| Owned-bond interest due/accrued | {metric['owned_bond_interest_due_accrued']} | USD |
| Gross investment income collected | {metric['total_gross_investment_income_collected']} | USD |
| Summary net investment income | {metric['summary_net_investment_income']} | USD |
| Cash-flow net investment income | {metric['cash_flow_net_investment_income']} | USD |
| Interest received / gross income | {metric['owned_bond_interest_received_to_gross_income_pct']} | percent |
| Interest received / net investment income | {metric['owned_bond_interest_received_to_net_investment_income_pct']} | percent |
| Interest received / owned-bond book | {metric['owned_bond_interest_received_on_book_pct']} | percent |
| Private-marker interest received | {metric['statutory_private_marker_interest_received']} | USD |
| ABS interest received | {metric['abs_interest_received']} | USD |

## Top Named Interest-Received Rows

| ID | CUSIP | Marker Type | Book Value | Interest Received | Simple Received/Book % |
|---|---|---|---:|---:|---:|
{table(detail_rows)}

## Proof Effect

This pass moves KKR/Global Atlantic from a destination-only statutory asset map to a cash-back proxy bridge. The owned-bond universe is near-reconciled to the statutory bond base, and the same row set now carries statutory interest received and interest due/accrued fields.

The safe use is:

`Accordia owned Schedule D bonds have near-reconciled book value and row-level statutory interest-received evidence. This supports legal-entity cash-back proxy analysis, not full named borrower return proof.`

## Boundary

This is not full named-cash proof. Interest received in a statutory row does not prove borrower use of proceeds, underlying asset cash receipt, trustee remittance, liability-cost spread, funds-held waterfall, FHLB economics, collateral certificates, IRR, NPV, ROIC, or final return.

## Next Action

Use the top `40` detail rows to build `accordia-owned-bond-income-proceeds-cusip-match`: join selected CUSIPs to disposal/proceeds rows, issuer/wrapper sources, liability-cost context, and controlled-document requests where public proof stops.

## Decision

`kkr-global-atlantic-accordia-owned-bond-income-bridge-visible-cusip-proceeds-match-next`
""",
        encoding="utf-8",
    )


def main() -> None:
    owned_rows = read_rows(OWNED)
    values = compact_values()
    bridge_rows = build_bridge_rows(owned_rows, values)
    detail_rows = build_detail_rows(owned_rows)
    diagnostics = diagnostic_rows(bridge_rows, detail_rows)
    write_csv(OUT, FIELDNAMES, bridge_rows)
    write_csv(DETAIL_OUT, DETAIL_FIELDS, detail_rows)
    write_csv(DIAGNOSTIC_OUT, DIAGNOSTIC_FIELDS, diagnostics)
    write_memo(bridge_rows, detail_rows, diagnostics)
    print(f"wrote {len(bridge_rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(detail_rows)} rows to {DETAIL_OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print(f"wrote memo to {MEMO.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
