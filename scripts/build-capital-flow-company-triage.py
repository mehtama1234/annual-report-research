#!/usr/bin/env python3
"""Build an all-company capital-flow triage from existing company packets."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTRACTED = ROOT / "extracted"
FIRST_PRINCIPLES = ROOT / "analysis" / "company-first-principles"
DATA_DIR = FIRST_PRINCIPLES / "data"
CSV_OUT = DATA_DIR / "capital-flow-all-company-triage.csv"
MD_OUT = FIRST_PRINCIPLES / "capital-flow-all-company-triage.md"


CATEGORIES: dict[str, dict[str, object]] = {
    "private_credit_direct_lending": {
        "weight": 16,
        "terms": [
            "private credit",
            "direct lending",
            "bdc",
            "business development company",
            "senior secured credit facility",
            "unitranche",
        ],
    },
    "debt_refinancing_and_facilities": {
        "weight": 12,
        "terms": [
            "credit facility",
            "revolving credit",
            "term loan",
            "first-lien",
            "first lien",
            "refinancing",
            "refinanced",
            "debt financing",
            "debt maturity",
            "notes payable",
            "senior notes",
            "unsecured notes",
        ],
    },
    "acquisition_finance": {
        "weight": 10,
        "terms": [
            "acquisition",
            "merger",
            "buyout",
            "sponsor",
            "private equity",
            "take-private",
            "sale completion",
            "strategic investment",
        ],
    },
    "asset_backed_and_securitization": {
        "weight": 11,
        "terms": [
            "asset-backed",
            "securitization",
            "receivables",
            "warehouse",
            "clo",
            "spv",
            "special purpose",
        ],
    },
    "insurance_and_retirement_capital": {
        "weight": 13,
        "terms": [
            "health insurance",
            "insurance underwriting",
            "insurance liabilities",
            "annuity",
            "reinsurance",
            "policy liabilities",
            "retirement services",
            "retirement risk transfer",
            "pension risk transfer",
            "statutory capital",
            "statutory filings",
        ],
    },
    "power_grid_and_project_finance": {
        "weight": 13,
        "terms": [
            "rate base",
            "regulatory capital employed",
            "transmission",
            "renewables",
            "storage",
            "project finance",
            "interconnection",
            "large-load",
            "data center",
            "hyperscaler",
        ],
    },
    "capital_intensity_and_capex": {
        "weight": 8,
        "terms": [
            "capital deployment",
            "capex",
            "capital expenditures",
            "backlog",
            "capacity expansion",
            "infrastructure",
            "construction",
        ],
    },
    "government_and_public_funding": {
        "weight": 7,
        "terms": [
            "grant",
            "tax credit",
            "ira",
            "chips act",
            "department of energy",
            "federal",
            "subsidy",
        ],
    },
}


NUMBER_RE = re.compile(
    r"(?i)(?:\$ ?\d+(?:\.\d+)? ?(?:b|bn|billion|m|mm|million)?|\d+(?:\.\d+)? ?(?:b|bn|billion|m|mm|million|gw|mw|%|x))"
)
TICKER_RE = re.compile(r"^- Ticker:\s*(.+)$", re.MULTILINE)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|\n+-\s+|\n+")


def title_from_slug(slug: str) -> str:
    fixes = {"inc": "Inc.", "corp": "Corp.", "co": "Co.", "plc": "PLC", "ltd": "Ltd.", "nv": "N.V.", "sa": "S.A."}
    return " ".join(fixes.get(part, part.capitalize()) for part in slug.replace("_", "-").split("-"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def count_sources(packet_text: str) -> int:
    return packet_text.count("](")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def term_pattern(term: str) -> re.Pattern[str]:
    parts = [re.escape(part) for part in term.split()]
    body = r"[\s-]+".join(parts)
    return re.compile(rf"(?<![A-Za-z0-9]){body}(?![A-Za-z0-9])", re.IGNORECASE)


TERM_PATTERNS = {term: term_pattern(term) for config in CATEGORIES.values() for term in config["terms"]}


def term_in_text(term: str, text: str) -> bool:
    return bool(TERM_PATTERNS[term].search(text))


def find_snippet(text: str, matched_terms: list[str]) -> str:
    if not matched_terms:
        return ""
    terms = sorted(matched_terms, key=len, reverse=True)
    best = ""
    for sentence in SENTENCE_SPLIT_RE.split(text):
        if any(term in TERM_PATTERNS and term_in_text(term, sentence) for term in terms):
            best = normalize(sentence)
            break
    if len(best) > 260:
        best = best[:257].rstrip() + "..."
    return best


def primary_lane(category_scores: Counter[str]) -> str:
    if not category_scores:
        return "low_signal_general_company"
    return category_scores.most_common(1)[0][0]


def recommended_next_step(lane: str) -> str:
    if lane == "private_credit_direct_lending":
        return "Search SEC holder schedules, credit agreements, rating reports, and lender announcements for borrower-level facility evidence."
    if lane == "debt_refinancing_and_facilities":
        return "Extract debt table, maturity schedule, facility size, lender names, pricing, use of proceeds, and repayment/refinancing language."
    if lane == "acquisition_finance":
        return "Pull merger proxy, closing 8-K, credit agreement exhibits, and rating-agency deal reports."
    if lane == "asset_backed_and_securitization":
        return "Extract collateral, advance rate, warehouse lenders, securitization size, and retained-interest economics."
    if lane == "insurance_and_retirement_capital":
        return "Bridge insurance liabilities to investment assets using annual reports, statutory filings, reinsurance notes, and asset schedules."
    if lane == "power_grid_and_project_finance":
        return "Extract capex plan, rate base, project backlog, financing plan, customer contracts, and regulatory recovery evidence."
    if lane == "capital_intensity_and_capex":
        return "Extract capex/backlog numbers and identify whether funding comes from operating cash flow, debt, equity, project finance, or grants."
    if lane == "government_and_public_funding":
        return "Extract grant, tax-credit, loan-program, and subsidy amounts and tie them to projects or capacity additions."
    return "Keep in the universe, but do not prioritize until stronger capital-flow terms or hard numbers appear."


def score_company(packet_path: Path) -> dict[str, object]:
    rel = packet_path.parent.relative_to(EXTRACTED)
    sector, industry, company_slug = rel.parts
    analysis_path = FIRST_PRINCIPLES / rel / "company-analysis.md"
    packet_text = read(packet_path)
    analysis_text = read(analysis_path)
    text = packet_text + "\n" + analysis_text

    category_scores: Counter[str] = Counter()
    matched_terms: list[str] = []
    for category, config in CATEGORIES.items():
        terms = config["terms"]
        weight = int(config["weight"])
        hits = [term for term in terms if term_in_text(term, text)]
        if hits:
            category_scores[category] = weight + min(len(hits) * 2, 10)
            matched_terms.extend(hits)

    insurance_industries = {"Life Insurance", "Managed Health Care", "Insurance Brokers", "Property Casualty Insurers"}
    if industry.replace("-", " ").title() in insurance_industries:
        category_scores["insurance_and_retirement_capital"] = max(
            category_scores["insurance_and_retirement_capital"],
            int(CATEGORIES["insurance_and_retirement_capital"]["weight"]) + 8,
        )
        matched_terms.append("insurance liabilities")

    numbers = NUMBER_RE.findall(text)
    dollar_numbers = [n for n in numbers if "$" in n or re.search(r"(?i)\b(?:b|bn|billion|m|mm|million)\b", n)]
    hard_number_points = min(len(numbers), 25)
    dollar_points = min(len(dollar_numbers) * 2, 20)
    source_points = min(count_sources(packet_text), 12)
    analysis_points = 5 if analysis_text else 0
    score = sum(category_scores.values()) + hard_number_points + dollar_points + source_points + analysis_points

    ticker_match = TICKER_RE.search(packet_text)
    ticker = ticker_match.group(1).strip() if ticker_match else ""
    lane = primary_lane(category_scores)

    return {
        "rank": 0,
        "score": score,
        "company": title_from_slug(company_slug),
        "sector": sector.replace("-", " ").title(),
        "industry": industry.replace("-", " ").title(),
        "ticker": ticker,
        "analysis_exists": "yes" if analysis_text else "no",
        "primary_lane": lane,
        "matched_signal_categories": "; ".join(name for name, _ in category_scores.most_common()),
        "hard_number_count": len(numbers),
        "dollar_number_count": len(dollar_numbers),
        "source_pointer_count": count_sources(packet_text),
        "evidence_snippet": find_snippet(text, matched_terms),
        "packet_path": str(packet_path.relative_to(ROOT)),
        "analysis_path": str(analysis_path.relative_to(ROOT)) if analysis_text else "",
        "recommended_next_step": recommended_next_step(lane),
    }


def write_csv(rows: list[dict[str, object]]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    fields = [
        "rank",
        "score",
        "company",
        "sector",
        "industry",
        "ticker",
        "analysis_exists",
        "primary_lane",
        "matched_signal_categories",
        "hard_number_count",
        "dollar_number_count",
        "source_pointer_count",
        "evidence_snippet",
        "packet_path",
        "analysis_path",
        "recommended_next_step",
    ]
    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def md_table(rows: list[dict[str, object]], limit: int = 30) -> str:
    lines = ["| Rank | Company | Sector | Industry | Score | Primary Lane | Evidence Snippet |", "|---:|---|---|---|---:|---|---|"]
    for row in rows[:limit]:
        snippet = str(row["evidence_snippet"]).replace("|", "/")
        lines.append(
            f"| {row['rank']} | {row['company']} | {row['sector']} | {row['industry']} | "
            f"{row['score']} | `{row['primary_lane']}` | {snippet} |"
        )
    return "\n".join(lines)


def write_markdown(rows: list[dict[str, object]]) -> None:
    lane_counts = Counter(str(row["primary_lane"]) for row in rows)
    sector_counts = Counter(str(row["sector"]) for row in rows[:100])
    high_signal = [row for row in rows if int(row["score"]) >= 80]
    private_credit = [row for row in rows if row["primary_lane"] == "private_credit_direct_lending"]

    lane_lines = ["| Lane | Companies |", "|---|---:|"]
    for lane, count in lane_counts.most_common():
        lane_lines.append(f"| `{lane}` | {count} |")

    sector_lines = ["| Sector | Top-100 Count |", "|---|---:|"]
    for sector, count in sector_counts.most_common():
        sector_lines.append(f"| {sector} | {count} |")

    content = f"""# Capital Flow All-Company Triage

## Purpose

This is the first broad scan across the full company-packet universe.

The goal is not to deeply analyze every company. The goal is to rank where deeper capital-flow work is likely to pay off.

Machine-readable table:

`analysis/company-first-principles/data/capital-flow-all-company-triage.csv`

## Current Result

| Metric | Value |
|---|---:|
| Company packets scanned | `{len(rows)}` |
| High-signal rows with score >= 80 | `{len(high_signal)}` |
| Private-credit/direct-lending primary-lane rows | `{len(private_credit)}` |
| Companies with existing first-principles analysis | `{sum(1 for row in rows if row['analysis_exists'] == 'yes')}` |

## What We Are Finding

The full universe should be triaged before it is deep-dived.

The strongest next candidates are companies where the packet already contains hard numbers plus capital-flow language: debt facilities, refinancing, acquisition finance, rate base, project backlog, private credit, securitization, insurance liabilities, or government support.

This scan converts the `519` company packets into a ranked work queue. It tells us where to pull annual reports, quarterly reports, credit agreements, rating reports, and source-of-funds documents next.

## Top Ranked Candidates

{md_table(rows, 30)}

## Primary-Lane Distribution

{chr(10).join(lane_lines)}

## Top-100 Sector Mix

{chr(10).join(sector_lines)}

## Method

Each company is scored from its existing `company-packet.md` plus any matching `company-analysis.md`.

The score rewards:

- capital-flow signal categories
- hard numbers
- dollar-denominated numbers
- source pointers
- existing first-principles analysis

The categories are deliberately broad in this first pass:

- `private_credit_direct_lending`
- `debt_refinancing_and_facilities`
- `acquisition_finance`
- `asset_backed_and_securitization`
- `insurance_and_retirement_capital`
- `power_grid_and_project_finance`
- `capital_intensity_and_capex`
- `government_and_public_funding`

## How To Use This

Do not treat the score as a claim.

Treat it as a work allocator:

`high score -> pull primary reports -> extract real numbers -> derive bounded claim -> add disproof test`

The next best use is to take the top `25` to `50` rows, group them by lane, and build lane-specific evidence queues.

## Current Bottom Line

Yes, it makes sense to track this across all companies, but only as triage first.

This file is the bridge from the hand-built private-credit cases into a repeatable all-company capital-flow research system.
"""
    MD_OUT.write_text(content, encoding="utf-8")


def main() -> None:
    packets = sorted(EXTRACTED.glob("*/*/*/company-packet.md"), key=lambda p: str(p).lower())
    rows = [score_company(path) for path in packets]
    rows.sort(key=lambda row: (-int(row["score"]), str(row["sector"]), str(row["industry"]), str(row["company"])))
    for i, row in enumerate(rows, start=1):
        row["rank"] = i
    write_csv(rows)
    write_markdown(rows)
    print(f"scanned={len(rows)} csv={CSV_OUT.relative_to(ROOT)} md={MD_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
