#!/usr/bin/env python3
"""Build Accordia owned-bond income to acquisition/disposal CUSIP match worklist."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"

DETAIL = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-detail-pass-1.csv"
PARSER = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.csv"
COORDINATE = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-pass-1.csv"

OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-pass-1.csv"
EVENT_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-event-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-pass-1.md"

MATCH_FIELDS = [
    "match_row_id",
    "detail_row_id",
    "coordinate_row_id",
    "rank",
    "cusip",
    "cusip_marker_type",
    "issuer_or_description",
    "owned_page",
    "owned_parser_row_id",
    "book_adjusted_carrying_value",
    "interest_received_during_year",
    "interest_income_due_accrued",
    "payment_due_at_maturity",
    "same_cusip_acquired_rows",
    "same_cusip_disposed_rows",
    "same_cusip_acquired_and_disposed_rows",
    "same_cusip_event_rows",
    "same_cusip_event_pages",
    "same_cusip_event_money_tokens",
    "largest_event_money_token",
    "event_money_token_sum",
    "continuity_status",
    "cash_proof_status",
    "proof_use",
    "boundary",
    "next_action",
]

EVENT_FIELDS = [
    "event_row_id",
    "match_row_id",
    "detail_row_id",
    "cusip",
    "event_type",
    "parser_row_id",
    "schedule_part",
    "page",
    "issuer_or_description",
    "transaction_date_1",
    "transaction_date_2",
    "money_token_count",
    "money_tokens_first_12",
    "raw_text",
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


def fmt(value: Decimal) -> str:
    return str(int(value)) if value == value.to_integral() else f"{value:.6f}"


def money_tokens(row: dict[str, str]) -> list[Decimal]:
    raw = row.get("money_tokens_first_12", "")
    return [money(token.strip()) for token in raw.split(";") if token.strip()]


def event_type(schedule_part: str) -> str:
    lowered = schedule_part.lower()
    if "part 3" in lowered:
        return "same-cusip-acquired-during-year"
    if "part 4" in lowered:
        return "same-cusip-sold-redeemed-disposed-during-year"
    if "part 5" in lowered:
        return "same-cusip-acquired-and-fully-disposed-during-year"
    return "same-cusip-other-parser-row"


def continuity_status(acquired: int, disposed: int, acquired_disposed: int) -> str:
    if disposed and acquired:
        return "owned-interest-plus-acquisition-and-disposal-same-cusip-visible"
    if disposed:
        return "owned-interest-plus-disposal-same-cusip-visible"
    if acquired:
        return "owned-interest-plus-acquisition-same-cusip-visible"
    if acquired_disposed:
        return "owned-interest-plus-same-year-acquired-disposed-cusip-visible"
    return "owned-interest-only-no-current-proceeds-event"


def cash_proof_status(status: str) -> str:
    if "disposal" in status:
        return "proceeds-candidate-raw-token-hold"
    if "acquisition" in status:
        return "same-year-purchase-context-visible-no-proceeds"
    return "interest-received-only-no-proceeds-match"


def proof_use(status: str) -> str:
    if "disposal" in status:
        return "ranked same-CUSIP disposal/proceeds continuity candidate"
    if "acquisition" in status:
        return "ranked same-CUSIP acquisition context for owned interest row"
    return "ranked interest-received row without current-year acquisition/disposal match"


def boundary(status: str) -> str:
    if "disposal" in status:
        return "same CUSIP appears in owned-interest and disposal sections, but raw disposal tokens are not reconciled to consideration, book value, gain/loss, proceeds, or cash settlement"
    if "acquisition" in status:
        return "same CUSIP appears in owned-interest and acquisition sections, but acquisition tokens do not prove use of proceeds, borrower receipt, or later cash return"
    return "owned row has statutory interest received, but no same-CUSIP current-year acquisition/disposal event in the raw parser"


def next_action(status: str) -> str:
    if "disposal" in status:
        return "run coordinate column extraction on the matching disposal page and reconcile consideration, book value, gain/loss, and interest/dividend fields"
    if "acquisition" in status:
        return "inspect acquisition page columns and issuer documents to test purchase route, wrapper, and borrower/use context"
    return "map issuer/wrapper documents and carry row into later-period proceeds or liability-spread matching"


def uniq(values: list[str]) -> str:
    out: list[str] = []
    for value in values:
        if value and value not in out:
            out.append(value)
    return "; ".join(out)


def build() -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    detail_rows = read_rows(DETAIL)
    parser_rows = read_rows(PARSER)
    coordinate_rows = read_rows(COORDINATE)

    parser_by_id = {row["parser_row_id"]: row for row in parser_rows}
    coordinate_by_id = {row["coordinate_row_id"]: row for row in coordinate_rows}
    parser_by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in parser_rows:
        parser_by_cusip[row["cusip"]].append(row)

    matches: list[dict[str, str]] = []
    events: list[dict[str, str]] = []

    for rank, row in enumerate(detail_rows, start=1):
        coordinate = coordinate_by_id[row["coordinate_row_id"]]
        owned_parser = parser_by_id.get(coordinate["parser_row_id"], {})
        event_rows = [
            event
            for event in parser_by_cusip[row["cusip"]]
            if "owned" not in event["schedule_part"].lower()
        ]
        acquired = sum(1 for event in event_rows if "Part 3" in event["schedule_part"])
        disposed = sum(1 for event in event_rows if "Part 4" in event["schedule_part"])
        acquired_disposed = sum(1 for event in event_rows if "Part 5" in event["schedule_part"])
        status = continuity_status(acquired, disposed, acquired_disposed)
        tokens = [token for event in event_rows for token in money_tokens(event)]
        largest = max(tokens, key=lambda value: abs(value)) if tokens else Decimal(0)
        token_sum = sum(tokens, Decimal(0))
        match_id = f"CFKKRGACOBIPCM-{rank:03d}"

        matches.append(
            {
                "match_row_id": match_id,
                "detail_row_id": row["detail_row_id"],
                "coordinate_row_id": row["coordinate_row_id"],
                "rank": str(rank),
                "cusip": row["cusip"],
                "cusip_marker_type": row["cusip_marker_type"],
                "issuer_or_description": owned_parser.get("issuer_or_description", ""),
                "owned_page": row["page"],
                "owned_parser_row_id": coordinate["parser_row_id"],
                "book_adjusted_carrying_value": row["book_adjusted_carrying_value"],
                "interest_received_during_year": row["interest_received_during_year"],
                "interest_income_due_accrued": row["interest_income_due_accrued"],
                "payment_due_at_maturity": row["payment_due_at_maturity"],
                "same_cusip_acquired_rows": str(acquired),
                "same_cusip_disposed_rows": str(disposed),
                "same_cusip_acquired_and_disposed_rows": str(acquired_disposed),
                "same_cusip_event_rows": str(len(event_rows)),
                "same_cusip_event_pages": uniq([event["page"] for event in event_rows]),
                "same_cusip_event_money_tokens": str(sum(len(money_tokens(event)) for event in event_rows)),
                "largest_event_money_token": fmt(largest),
                "event_money_token_sum": fmt(token_sum),
                "continuity_status": status,
                "cash_proof_status": cash_proof_status(status),
                "proof_use": proof_use(status),
                "boundary": boundary(status),
                "next_action": next_action(status),
            }
        )

        for event in event_rows:
            event_status = event_type(event["schedule_part"])
            events.append(
                {
                    "event_row_id": f"CFKKRGACOBIPCE-{len(events)+1:03d}",
                    "match_row_id": match_id,
                    "detail_row_id": row["detail_row_id"],
                    "cusip": row["cusip"],
                    "event_type": event_status,
                    "parser_row_id": event["parser_row_id"],
                    "schedule_part": event["schedule_part"],
                    "page": event["page"],
                    "issuer_or_description": event["issuer_or_description"],
                    "transaction_date_1": event["transaction_date_1"],
                    "transaction_date_2": event["transaction_date_2"],
                    "money_token_count": event["money_token_count"],
                    "money_tokens_first_12": event["money_tokens_first_12"],
                    "raw_text": event["raw_text"],
                    "proof_use": "raw same-CUSIP event row for top owned-bond income/proceeds matching",
                    "boundary": "event row preserves raw parser tokens only; columns are not reconciled to final consideration, proceeds, gain/loss, interest, or settlement cash",
                    "next_action": "perform page-coordinate column extraction for event row before any proceeds or gain/loss claim",
                }
            )

    diagnostics = diagnostic_rows(matches, events)
    return matches, events, diagnostics


def diagnostic_rows(matches: list[dict[str, str]], events: list[dict[str, str]]) -> list[dict[str, str]]:
    status_counts = Counter(row["continuity_status"] for row in matches)
    proof_counts = Counter(row["cash_proof_status"] for row in matches)
    event_type_counts = Counter(row["event_type"] for row in events)
    interest_with_event = sum(money(row["interest_received_during_year"]) for row in matches if int(row["same_cusip_event_rows"]))
    interest_total = sum(money(row["interest_received_during_year"]) for row in matches)
    disposal_candidate_interest = sum(money(row["interest_received_during_year"]) for row in matches if int(row["same_cusip_disposed_rows"]))
    rows = [
        ("match_rows", str(len(matches)), "count"),
        ("event_rows", str(len(events)), "count"),
        ("top_detail_rows_covered", str(len(matches)), "count"),
        ("rows_with_same_cusip_event", str(sum(1 for row in matches if int(row["same_cusip_event_rows"]))), "count"),
        ("rows_with_same_cusip_acquisition", str(sum(1 for row in matches if int(row["same_cusip_acquired_rows"]))), "count"),
        ("rows_with_same_cusip_disposal", str(sum(1 for row in matches if int(row["same_cusip_disposed_rows"]))), "count"),
        ("rows_with_same_year_acquired_disposed", str(sum(1 for row in matches if int(row["same_cusip_acquired_and_disposed_rows"]))), "count"),
        ("interest_received_on_top_40_rows", fmt(interest_total), "USD"),
        ("interest_received_on_rows_with_any_event", fmt(interest_with_event), "USD"),
        ("interest_received_on_disposal_candidate_rows", fmt(disposal_candidate_interest), "USD"),
        ("raw_event_money_token_sum", fmt(sum(money(row["event_money_token_sum"]) for row in matches)), "USD-token-sum"),
        ("raw_event_largest_abs_token", fmt(max((abs(money(row["largest_event_money_token"])) for row in matches), default=Decimal(0))), "USD-token"),
        ("status_owned_interest_plus_acquisition", str(status_counts["owned-interest-plus-acquisition-same-cusip-visible"]), "count"),
        ("status_owned_interest_plus_disposal", str(status_counts["owned-interest-plus-disposal-same-cusip-visible"]), "count"),
        ("status_owned_interest_only", str(status_counts["owned-interest-only-no-current-proceeds-event"]), "count"),
        ("cash_status_proceeds_candidate_raw_token_hold", str(proof_counts["proceeds-candidate-raw-token-hold"]), "count"),
        ("cash_status_purchase_context_no_proceeds", str(proof_counts["same-year-purchase-context-visible-no-proceeds"]), "count"),
        ("event_type_acquired", str(event_type_counts["same-cusip-acquired-during-year"]), "count"),
        ("event_type_disposed", str(event_type_counts["same-cusip-sold-redeemed-disposed-during-year"]), "count"),
        ("full_named_cash_proof_upgrades", "0", "count"),
        ("next_parser", "accordia-disposal-coordinate-column-extraction-for-matched-cusips", "parser"),
    ]
    out: list[dict[str, str]] = []
    for idx, (metric, value, units) in enumerate(rows, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGACOBIPCX-{idx:03d}",
                "metric": metric,
                "value": value,
                "units": units,
                "proof_use": "controls Accordia owned-bond income/proceeds CUSIP match status",
                "boundary": "Same-CUSIP matching is continuity worklist evidence only; raw event tokens are not final proceeds, settlement, borrower use, liability spread, waterfall, collateral certificate, or return proof.",
                "next_action": "Run coordinate column extraction on matched disposal/acquisition pages before promoting any proceeds or gain/loss claim.",
            }
        )
    return out


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def top_table(matches: list[dict[str, str]]) -> str:
    lines = []
    for row in matches[:12]:
        lines.append(
            "| {match_row_id} | {cusip} | {issuer_or_description} | {interest_received_during_year} | {same_cusip_event_rows} | {continuity_status} |".format(**row)
        )
    return "\n".join(lines)


def write_memo(matches: list[dict[str, str]], events: list[dict[str, str]], diagnostics: list[dict[str, str]]) -> None:
    diag = {row["metric"]: row["value"] for row in diagnostics}
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Accordia Owned-Bond Income Proceeds CUSIP Match Pass 1

## Purpose

This pass takes the top `40` Accordia owned-bond interest-received rows and tests whether the same CUSIPs also appear in current-year acquisition, sale, redemption, disposal, or acquired-and-fully-disposed sections of the raw Accordia Schedule D parser.

It asks:

`Which high-interest KKR/Global Atlantic Accordia owned-bond rows have same-CUSIP acquisition or disposal continuity, and where does public statutory proof still stop before proceeds are promoted?`

The match table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-pass-1.csv`

The event table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-event-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-diagnostic-pass-1.csv`

## Short Answer

`The top 40 Accordia owned-bond interest-received rows now have a same-CUSIP continuity worklist. Ten rows have same-CUSIP current-year events: seven acquisition-context rows and three disposal/proceeds-candidate rows. The matched-event rows carry {diag['interest_received_on_rows_with_any_event']} USD of owned-bond interest received, including {diag['interest_received_on_disposal_candidate_rows']} USD on disposal-candidate rows. No row is upgraded to full named-cash proof because the acquisition/disposal event rows are still raw-token evidence, not coordinate-reconciled proceeds columns.`

## Diagnostics

| Metric | Value | Units |
|---|---:|---|
| Match rows | {diag['match_rows']} | count |
| Same-CUSIP event rows | {diag['event_rows']} | count |
| Top rows with any event | {diag['rows_with_same_cusip_event']} | count |
| Rows with same-CUSIP acquisition | {diag['rows_with_same_cusip_acquisition']} | count |
| Rows with same-CUSIP disposal | {diag['rows_with_same_cusip_disposal']} | count |
| Interest received on top 40 rows | {diag['interest_received_on_top_40_rows']} | USD |
| Interest received on rows with any event | {diag['interest_received_on_rows_with_any_event']} | USD |
| Interest received on disposal-candidate rows | {diag['interest_received_on_disposal_candidate_rows']} | USD |
| Raw event money-token sum | {diag['raw_event_money_token_sum']} | USD-token-sum |
| Largest raw event token | {diag['raw_event_largest_abs_token']} | USD-token |
| Full named cash proof upgrades | {diag['full_named_cash_proof_upgrades']} | count |

## Top Match Rows

| ID | CUSIP | Issuer/Description | Interest Received | Event Rows | Continuity Status |
|---|---|---|---:|---:|---|
{top_table(matches)}

## Proof Effect

This pass upgrades the next work from a general proceeds search to a named CUSIP worklist. The best immediate targets are the three disposal/proceeds-candidate CUSIPs because they already connect owned interest-received rows to same-CUSIP sale/redeemed/disposed rows in the raw parser.

The safe use is:

`Accordia top interest-received owned-bond rows now have same-CUSIP acquisition/disposal continuity flags. Three rows are disposal/proceeds candidates, but the event rows remain raw-token evidence until coordinate column extraction reconciles consideration, book value, gain/loss, and interest/dividend fields.`

## Boundary

This is not full named-cash proof. Same-CUSIP continuity does not prove lot-level identity, consideration, settlement cash, borrower receipt/use, trustee remittance, liability-cost spread, funds-held waterfall, collateral certificates, IRR, NPV, ROIC, or KKR platform profit.

## Next Action

Run `accordia-disposal-coordinate-column-extraction-for-matched-cusips` on the matched disposal pages, then reconcile event tokens to statutory disposal columns before any proceeds or gain/loss claim.

## Decision

`kkr-global-atlantic-accordia-income-proceeds-cusip-match-visible-disposal-coordinate-extraction-next`
""",
        encoding="utf-8",
    )


def main() -> None:
    matches, events, diagnostics = build()
    write_csv(OUT, MATCH_FIELDS, matches)
    write_csv(EVENT_OUT, EVENT_FIELDS, events)
    write_csv(DIAGNOSTIC_OUT, DIAGNOSTIC_FIELDS, diagnostics)
    write_memo(matches, events, diagnostics)
    print(f"wrote {len(matches)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(events)} rows to {EVENT_OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print(f"wrote memo to {MEMO.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
