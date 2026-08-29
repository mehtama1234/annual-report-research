#!/usr/bin/env python3
"""Build lane-specific work queues from the all-company capital-flow triage."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_PRINCIPLES = ROOT / "analysis" / "company-first-principles"
DATA_DIR = FIRST_PRINCIPLES / "data"
TRIAGE_CSV = DATA_DIR / "capital-flow-all-company-triage.csv"
QUEUE_CSV = DATA_DIR / "capital-flow-lane-candidate-queues.csv"
REPORT_MD = FIRST_PRINCIPLES / "capital-flow-lane-candidate-queues.md"


LANE_LIMITS = {
    "private_credit_direct_lending": 10,
    "insurance_and_retirement_capital": 10,
    "power_grid_and_project_finance": 15,
    "debt_refinancing_and_facilities": 10,
    "acquisition_finance": 10,
    "asset_backed_and_securitization": 10,
    "capital_intensity_and_capex": 15,
    "government_and_public_funding": 10,
}


LANE_REQUIREMENTS = {
    "private_credit_direct_lending": "AUM/FPAUM, credit AUM, fundraising, deployment, direct-lending originations, BDC/fund schedules, borrower examples, facility-size proof.",
    "insurance_and_retirement_capital": "Insurance liabilities, invested assets, credit allocation, reinsurance structure, statutory schedules, credit quality, asset-manager linkage.",
    "power_grid_and_project_finance": "Capex plan, rate base, project backlog, customer/load contracts, financing plan, debt/equity issuance, regulatory recovery.",
    "debt_refinancing_and_facilities": "Debt table, credit facility size, maturity ladder, lender/admin agent, pricing, use of proceeds, refinancing or repayment language.",
    "acquisition_finance": "Transaction value, sponsor, financing commitments, credit agreement, merger proxy, use of proceeds, lender group, prior debt treatment.",
    "asset_backed_and_securitization": "Collateral pool, warehouse/securitization size, advance rate, lender or noteholder structure, retained interests, credit losses.",
    "capital_intensity_and_capex": "Capex/backlog, funding mix, operating cash flow, debt issuance, equity issuance, project returns, capacity additions.",
    "government_and_public_funding": "Grant/tax-credit/loan-program amount, program authority, project link, timing, conditions, private co-funding.",
}


LANE_QUESTIONS = {
    "private_credit_direct_lending": "Where does the managed private-credit capital come from, and which operating borrowers receive it?",
    "insurance_and_retirement_capital": "How do insurance or retirement liabilities become credit assets, and what quality/risk sits underneath?",
    "power_grid_and_project_finance": "Which companies are turning electricity/load growth into funded infrastructure buildout?",
    "debt_refinancing_and_facilities": "Where are debt facilities changing the capital stack, maturity wall, or bank/private-credit role?",
    "acquisition_finance": "Which M&A deals require financing proof before we claim capital is flowing into consolidation?",
    "asset_backed_and_securitization": "Where are receivables, leases, collateral pools, or SPVs converting operations into financeable assets?",
    "capital_intensity_and_capex": "Where is the real economy consuming the most capital, and how is that build funded?",
    "government_and_public_funding": "Where is public money lowering private capital cost or directly funding capacity?",
}


def read_triage() -> list[dict[str, str]]:
    with TRIAGE_CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def selected_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_lane: dict[str, list[dict[str, str]]] = defaultdict(list)
    insurance_industries = {"Life Insurance", "Managed Health Care", "Insurance Brokers", "Property Casualty Insurers"}
    for row in rows:
        lane = row["primary_lane"]
        if lane in LANE_LIMITS and int(row["score"]) >= 70:
            if lane == "insurance_and_retirement_capital" and row["industry"] not in insurance_industries:
                continue
            by_lane[lane].append(row)

    selected: list[dict[str, str]] = []
    for lane, limit in LANE_LIMITS.items():
        for lane_rank, row in enumerate(by_lane.get(lane, [])[:limit], start=1):
            selected.append(
                {
                    "lane": lane,
                    "lane_rank": str(lane_rank),
                    "overall_rank": row["rank"],
                    "score": row["score"],
                    "company": row["company"],
                    "sector": row["sector"],
                    "industry": row["industry"],
                    "ticker": row["ticker"],
                    "matched_signal_categories": row["matched_signal_categories"],
                    "hard_number_count": row["hard_number_count"],
                    "dollar_number_count": row["dollar_number_count"],
                    "source_pointer_count": row["source_pointer_count"],
                    "evidence_snippet": row["evidence_snippet"],
                    "packet_path": row["packet_path"],
                    "analysis_path": row["analysis_path"],
                    "proof_numbers_to_extract": LANE_REQUIREMENTS[lane],
                    "lane_question": LANE_QUESTIONS[lane],
                    "recommended_next_step": row["recommended_next_step"],
                    "status": "queued-primary-source-pass",
                }
            )
    return selected


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = [
        "lane",
        "lane_rank",
        "overall_rank",
        "score",
        "company",
        "sector",
        "industry",
        "ticker",
        "matched_signal_categories",
        "hard_number_count",
        "dollar_number_count",
        "source_pointer_count",
        "evidence_snippet",
        "packet_path",
        "analysis_path",
        "proof_numbers_to_extract",
        "lane_question",
        "recommended_next_step",
        "status",
    ]
    with QUEUE_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def md_lane_table(rows: list[dict[str, str]], lane: str) -> str:
    lane_rows = [row for row in rows if row["lane"] == lane]
    if not lane_rows:
        return "_No rows selected in this lane._"
    lines = [
        "| Lane Rank | Overall Rank | Company | Sector | Industry | Score | Evidence Snippet |",
        "|---:|---:|---|---|---|---:|---|",
    ]
    for row in lane_rows:
        snippet = row["evidence_snippet"].replace("|", "/")
        lines.append(
            f"| {row['lane_rank']} | {row['overall_rank']} | {row['company']} | {row['sector']} | "
            f"{row['industry']} | {row['score']} | {snippet} |"
        )
    return "\n".join(lines)


def write_markdown(rows: list[dict[str, str]], all_rows: list[dict[str, str]]) -> None:
    lane_counts = Counter(row["lane"] for row in rows)
    universe_counts = Counter(row["primary_lane"] for row in all_rows)
    sections = []
    for lane in LANE_LIMITS:
        sections.append(
            f"""## {lane.replace('_', ' ').title()}

Question: `{LANE_QUESTIONS[lane]}`

Numbers to extract:

`{LANE_REQUIREMENTS[lane]}`

{md_lane_table(rows, lane)}
"""
        )

    summary_lines = ["| Lane | Universe Rows | Selected Queue Rows |", "|---|---:|---:|"]
    for lane in LANE_LIMITS:
        summary_lines.append(f"| `{lane}` | {universe_counts.get(lane, 0)} | {lane_counts.get(lane, 0)} |")

    content = f"""# Capital Flow Lane Candidate Queues

## Purpose

This converts the all-company triage into lane-specific primary-source work queues.

Machine-readable table:

`analysis/company-first-principles/data/capital-flow-lane-candidate-queues.csv`

## Current Result

| Metric | Value |
|---|---:|
| Source company universe | `{len(all_rows)}` |
| Lane queue rows selected | `{len(rows)}` |
| Lanes with selected rows | `{len(lane_counts)}` |

## Lane Summary

{chr(10).join(summary_lines)}

## What This Means

The private-credit work remains important, but it is only one lane.

The broader map now needs parallel queues for:

- capital-intensive buildout
- power/grid/project finance
- acquisition finance
- refinancing and debt facilities
- insurance/retirement capital
- asset-backed and securitization structures
- government/public funding

Each lane has a different proof package. A private-credit claim needs lender and vehicle evidence. A utility buildout claim needs rate-base, capex, backlog, regulatory recovery, and financing-plan evidence. An acquisition-finance claim needs transaction value, credit agreement, lender group, and use-of-proceeds evidence.

## Lane Queues

{chr(10).join(sections)}

## Current Bottom Line

The next research system should not run one generic extraction across every company.

It should run lane-specific extraction passes against this queue, because each capital-flow mechanism has different proof requirements and different disproof tests.
"""
    REPORT_MD.write_text(content, encoding="utf-8")


def main() -> None:
    all_rows = read_triage()
    rows = selected_rows(all_rows)
    write_csv(rows)
    write_markdown(rows, all_rows)
    print(f"selected={len(rows)} csv={QUEUE_CSV.relative_to(ROOT)} md={REPORT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
