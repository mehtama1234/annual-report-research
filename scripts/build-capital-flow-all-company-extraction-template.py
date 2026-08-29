#!/usr/bin/env python3
"""Build the 519-company capital-flow role/wrapper/proof template."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"

TRIAGE = DATA / "capital-flow-all-company-triage.csv"
LANE_QUEUE = DATA / "capital-flow-lane-candidate-queues.csv"
OUTPUT_CSV = DATA / "capital-flow-all-company-extraction-template-pass-1.csv"
OUTPUT_MD = ANALYSIS / "capital-flow-all-company-extraction-template-pass-1.md"

FIELDS = [
    "template_id",
    "source_rank",
    "company",
    "ticker",
    "sector",
    "industry",
    "primary_lane",
    "lane_rank",
    "matched_signal_categories",
    "capital_flow_role",
    "likely_funding_wrapper",
    "source_availability",
    "current_proof_level",
    "denominator_need",
    "next_document",
    "safe_claim",
    "do_not_claim",
    "priority_status",
    "packet_path",
    "analysis_path",
]

ROLE_BY_LANE = {
    "private_credit_direct_lending": "private-credit platform or direct-lending source candidate",
    "insurance_and_retirement_capital": "insurance or retirement-liability capital source candidate",
    "power_grid_and_project_finance": "power, grid, infrastructure, or project-finance demand candidate",
    "debt_refinancing_and_facilities": "refinancing, maturity, facility, or lender-role candidate",
    "acquisition_finance": "acquisition-finance or consolidation candidate",
    "asset_backed_and_securitization": "asset-backed, collateral-pool, receivables, lease, or securitization candidate",
    "capital_intensity_and_capex": "capital-intensive buildout, capex, backlog, or physical-output candidate",
    "government_and_public_funding": "public-funding, grant, tax-credit, or subsidy candidate",
    "low_signal_general_company": "low-signal company retained for universe coverage",
}

WRAPPER_BY_LANE = {
    "private_credit_direct_lending": "manager funds, BDCs, private-credit vehicles, direct-lending programs",
    "insurance_and_retirement_capital": "insurance general accounts, retirement liabilities, reinsurance, affiliated managers",
    "power_grid_and_project_finance": "utility debt/equity, rate-base recovery, project finance, customer contracts, public funding",
    "debt_refinancing_and_facilities": "revolvers, term loans, senior notes, ABL, private placements, amendments",
    "acquisition_finance": "cash, stock, bridge loans, term loans, private credit, bank facilities, assumed debt",
    "asset_backed_and_securitization": "ABL, receivables facilities, securitizations, warehouse lines, collateral SPVs",
    "capital_intensity_and_capex": "operating cash flow, debt, equity, project finance, customer funding, retained earnings",
    "government_and_public_funding": "grants, tax credits, public loans, ratepayer funding, government contracts",
    "low_signal_general_company": "unknown or not yet material",
}

DENOMINATOR_BY_LANE = {
    "private_credit_direct_lending": "private-credit AUM/deployment, BDC schedules, borrower facility sizes, bank-credit lane denominators",
    "insurance_and_retirement_capital": "statutory invested assets, reserves, surplus, NAIC quality, private-credit allocation",
    "power_grid_and_project_finance": "MW/GW load, rate base, capex plan, approved projects, docket status, recovery mechanism",
    "debt_refinancing_and_facilities": "old/new debt, maturity wall, pricing, covenant headroom, lender group, repayment use",
    "acquisition_finance": "transaction value, funding mix, assumed debt, repayment, lender group, use-of-proceeds",
    "asset_backed_and_securitization": "collateral pool, advance rate, availability, loss rate, retained interest, facility size",
    "capital_intensity_and_capex": "capex, backlog, output, utilization, cash conversion, project cost, outside market denominator",
    "government_and_public_funding": "grant amount, tax-credit value, program authority, project cost, private co-funding",
    "low_signal_general_company": "none until stronger signal appears",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def source_availability(row: dict[str, str]) -> str:
    pointers = int(row["source_pointer_count"] or 0)
    if row["analysis_exists"] == "yes" and pointers >= 10:
        return "packet-analysis-and-source-pointers"
    if row["analysis_exists"] == "yes":
        return "packet-and-analysis"
    if pointers >= 10:
        return "packet-and-source-pointers"
    return "packet-only"


def proof_level(row: dict[str, str], lane_rank: str) -> str:
    lane = row["primary_lane"]
    score = int(row["score"] or 0)
    if lane_rank:
        return "lane-queue-candidate"
    if lane == "low_signal_general_company":
        return "radar-only-low-signal"
    if score >= 80:
        return "high-signal-radar"
    return "universe-radar"


def priority_status(row: dict[str, str], lane_rank: str) -> str:
    score = int(row["score"] or 0)
    if lane_rank:
        return "selected-lane-queue"
    if score >= 80:
        return "high-signal-backlog"
    if score >= 60:
        return "monitor"
    return "retain-low-signal"


def next_document(row: dict[str, str]) -> str:
    lane = row["primary_lane"]
    if row["recommended_next_step"]:
        return row["recommended_next_step"]
    if lane == "low_signal_general_company":
        return "Keep in universe; re-score after new filing or packet refresh."
    return f"Pull primary documents for {lane}: {DENOMINATOR_BY_LANE[lane]}."


def safe_claim(row: dict[str, str], level: str) -> str:
    company = row["company"]
    lane = row["primary_lane"]
    role = ROLE_BY_LANE[lane]
    if level == "radar-only-low-signal":
        return f"{company} is retained in the 519-company radar but has no promoted capital-flow claim yet."
    return f"{company} is a {role} based on current packet/radar evidence; promote only after primary-source extraction confirms the lane-specific amounts, actors, periods, and boundaries."


def do_not_claim(row: dict[str, str], level: str) -> str:
    company = row["company"]
    lane = row["primary_lane"]
    if level == "radar-only-low-signal":
        return f"Do not treat {company} as a priority capital-flow case without stronger evidence."
    return f"Do not treat {company}'s {lane} signal as source-to-use-to-output proof until source documents, denominators, and disproof checks are complete."


def build_rows() -> list[dict[str, str]]:
    triage = read_csv(TRIAGE)
    queue = read_csv(LANE_QUEUE)
    lane_rank_by_key = {
        (row["overall_rank"], row["company"], row["lane"]): row["lane_rank"] for row in queue
    }
    rows: list[dict[str, str]] = []
    for index, row in enumerate(triage, start=1):
        lane = row["primary_lane"]
        lane_rank = lane_rank_by_key.get((row["rank"], row["company"], lane), "")
        level = proof_level(row, lane_rank)
        rows.append(
            {
                "template_id": f"ACET-001-{index:03d}",
                "source_rank": row["rank"],
                "company": row["company"],
                "ticker": row["ticker"],
                "sector": row["sector"],
                "industry": row["industry"],
                "primary_lane": lane,
                "lane_rank": lane_rank,
                "matched_signal_categories": row["matched_signal_categories"],
                "capital_flow_role": ROLE_BY_LANE[lane],
                "likely_funding_wrapper": WRAPPER_BY_LANE[lane],
                "source_availability": source_availability(row),
                "current_proof_level": level,
                "denominator_need": DENOMINATOR_BY_LANE[lane],
                "next_document": next_document(row),
                "safe_claim": safe_claim(row, level),
                "do_not_claim": do_not_claim(row, level),
                "priority_status": priority_status(row, lane_rank),
                "packet_path": row["packet_path"],
                "analysis_path": row["analysis_path"],
            }
        )
    return rows


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, str]]) -> None:
    lane_counts = Counter(row["primary_lane"] for row in rows)
    proof_counts = Counter(row["current_proof_level"] for row in rows)
    priority_counts = Counter(row["priority_status"] for row in rows)
    source_counts = Counter(row["source_availability"] for row in rows)

    lines = [
        "# Capital Flow All-Company Extraction Template Pass 1",
        "",
        "## Purpose",
        "",
        "This pass resolves `CFARQ-015`:",
        "",
        "`Can the case-study capital-flow system scale across the full 519-company universe without losing proof discipline?`",
        "",
        "The operating table is:",
        "",
        "`analysis/company-first-principles/data/capital-flow-all-company-extraction-template-pass-1.csv`",
        "",
        "## Short Answer",
        "",
        "Yes, as a template and queue-control system.",
        "",
        "Every company in the `519` company triage now has a row with:",
        "",
        "- lane",
        "- capital-flow role",
        "- likely funding wrapper",
        "- source availability",
        "- current proof level",
        "- denominator need",
        "- next document",
        "- safe claim",
        "- do-not-claim boundary",
        "",
        "This upgrades the research system from case-study evidence to scalable operating model, but it does not mean every company is source-proven.",
        "",
        "## Row Counts",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Template rows | `{len(rows)}` |",
    ]
    for status, count in priority_counts.most_common():
        lines.append(f"| Priority status: `{status}` | `{count}` |")
    lines.extend(["", "## Lane Coverage", "", "| Lane | Rows |", "|---|---:|"])
    for lane, count in lane_counts.most_common():
        lines.append(f"| `{lane}` | `{count}` |")
    lines.extend(["", "## Proof Levels", "", "| Proof Level | Rows |", "|---|---:|"])
    for level, count in proof_counts.most_common():
        lines.append(f"| `{level}` | `{count}` |")
    lines.extend(["", "## Source Availability", "", "| Source Availability | Rows |", "|---|---:|"])
    for status, count in source_counts.most_common():
        lines.append(f"| `{status}` | `{count}` |")
    lines.extend(
        [
            "",
            "## Template Standard",
            "",
            "| Field | Why It Exists |",
            "|---|---|",
            "| `capital_flow_role` | Converts a company from generic sector coverage into a testable capital-flow role. |",
            "| `likely_funding_wrapper` | Names the expected financing container before source extraction. |",
            "| `source_availability` | Separates packet-only rows from rows with analysis and source pointers. |",
            "| `current_proof_level` | Prevents radar rows from being promoted as source-grade evidence. |",
            "| `denominator_need` | Names the outside or internal denominator required before market-scale claims. |",
            "| `next_document` | Turns each company into an actionable source task. |",
            "| `safe_claim` | Gives the strongest currently allowed sentence. |",
            "| `do_not_claim` | Blocks premature source-to-use-to-output language. |",
            "",
            "## Claim Status",
            "",
            "Promote:",
            "",
            "`The 519-company universe now has a role/wrapper/proof extraction template that can route every company into a lane, expected funding wrapper, source-availability status, proof level, denominator need, next-document target, safe claim, and do-not-claim boundary.`",
            "",
            "Do not promote:",
            "",
            "`Every company in the 519-company universe is source-proven or representative of the final thesis.`",
            "",
            "## Queue Decision",
            "",
            "`CFARQ-015` outcome:",
            "",
            "`upgrade-with-boundary - every company now has the required template fields, but most rows remain radar or queue status until primary-source extraction is run.`",
            "",
            "## Next Best Work",
            "",
            "The answer-resolution queue has now been worked through pass 1. The next phase should use this template to run lane-specific extraction batches, starting with the highest-impact unresolved public claims:",
            "",
            "1. insurance statutory quality",
            "2. bank/private-credit lane-share denominator",
            "3. ET/Cheniere named-project source-use-return registry",
            "4. grid/power project status and recovery mechanism",
            "5. all-company role/wrapper/proof refresh after each new source batch",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = build_rows()
    write_csv(rows)
    write_markdown(rows)
    print(f"wrote {len(rows)} rows to {OUTPUT_CSV.relative_to(ROOT)}")
    print(f"wrote report to {OUTPUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
