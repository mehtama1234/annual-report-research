#!/usr/bin/env python3
"""Verify cross-framework company analysis page outputs."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_JSON = ROOT / "analysis" / "cross-framework-company-method-registry.json"
REPORT_MD = ROOT / "analysis" / "cross-framework-company-method-report.md"
INDEX_HTML = ROOT / "site" / "cross-framework-companies" / "index.html"
COMPANIES_DIR = ROOT / "site" / "cross-framework-companies" / "companies"
DATA_DIR = ROOT / "site" / "cross-framework-companies" / "data"
COMPANIES_CSV = ROOT / "indexes" / "companies.csv"
DEEP_MEMO_DIR = ROOT / "analysis" / "deep-company-pages"

REQUIRED_COMPANY_SECTIONS = [
    "Annual-Report Starting Point",
    "Analysis Stack",
    "Business Model Read",
    "Annual Report Takeaways",
    "Latest Quarter Chain",
    "Signal Map",
    "Valuation Focus",
    "Damodaran Questions To Answer",
    "Lyn Alden Macro/Liquidity Checks",
    "Other Strategy Checks",
    "Next Evidence Work",
    "Damodaran Routes",
    "Lyn Alden Routes",
    "Other Investor/Strategy Routes",
    "Local Evidence",
    "Thesis Workbench",
]

DEEP_EXEMPLAR_SLUGS = {
    "mcdonalds-corporation",
    "chipotle-mexican-grill",
}

REQUIRED_DEEP_SECTIONS = [
    "Analysis Results",
    "What Must Be True",
    "Evidence Basis",
    "Plain-English Investment Memo",
    "First-Principles Explanation",
    "What The Numbers Mean",
    "Plain-Language Definitions",
    "Approach Used, What It Found, And Why It Matters",
    "Company Conclusion",
    "What The Market Could Be Missing",
    "Framework Lenses",
    "Method Routing",
    "Annual And Quarter Evidence",
    "Business Model Mechanisms",
    "What Would Prove This Wrong",
    "Deep Questions",
    "Next Filing Watchlist",
    "Comparison Bridge",
    "Source Register",
]

BANNED_DEEP_PHRASES = [
    "Investment Posture",
    "Company Thesis",
    "Mispricing",
    "mispricing",
    "cash engine",
    "underwrite",
    "moat",
    "unit economics",
    "posture",
    "thesis works",
    "loyalty causality",
    "behavior test, not an app download statistic",
    "terminal value",
    "intrinsic value",
    "hurdle rate",
    "beta",
    "collect economics",
    "cash return by store cohort",
    "durable habit",
    "value creation",
    "create value",
    "margin bridge",
    "cohort",
    "P&L",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def roster_count() -> int:
    with COMPANIES_CSV.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    slugs = {row["company_slug"] for row in rows}
    detailed_slugs = {
        path.parent.name
        for path in (ROOT / "analysis" / "company-first-principles").glob("*/*/*/company-analysis.json")
    }
    return len(slugs | detailed_slugs)


def roster_row_count() -> int:
    with COMPANIES_CSV.open(newline="", encoding="utf-8") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def main() -> int:
    if not REGISTRY_JSON.exists():
        fail(f"missing {REGISTRY_JSON.relative_to(ROOT)}")
    if not REPORT_MD.exists():
        fail(f"missing {REPORT_MD.relative_to(ROOT)}")
    if not INDEX_HTML.exists():
        fail(f"missing {INDEX_HTML.relative_to(ROOT)}")
    registry = json.loads(REGISTRY_JSON.read_text(encoding="utf-8"))
    report = REPORT_MD.read_text(encoding="utf-8")
    counts = registry["counts"]
    expected_companies = roster_count()
    expected_rows = roster_row_count()
    if counts["source_roster_rows"] != expected_rows:
        fail(f"registry source row count {counts['source_roster_rows']} != roster rows {expected_rows}")
    if counts["companies"] != expected_companies:
        fail(f"registry company count {counts['companies']} != roster count {expected_companies}")
    if counts["company_pages"] != expected_companies:
        fail(f"company page count {counts['company_pages']} != roster count {expected_companies}")
    if counts["company_data_files"] != expected_companies:
        fail(f"company data count {counts['company_data_files']} != roster count {expected_companies}")
    detailed_count = len(
        list((ROOT / "analysis" / "company-first-principles").glob("*/*/*/company-analysis.json"))
    )
    if counts["detailed_first_principles_packets"] != detailed_count:
        fail(
            "registry detailed packet count "
            f"{counts['detailed_first_principles_packets']} != local detailed packets {detailed_count}"
        )
    if counts["damodaran_use_cases"] < 10:
        fail("expected at least 10 Damodaran use cases")
    if counts["lyn_alden_methods"] < 5:
        fail("expected at least 5 Lyn Alden methods")
    if counts["other_framework_methods"] < 5:
        fail("expected at least 5 other framework methods")
    if counts.get("deep_exemplar_pages") != len(DEEP_EXEMPLAR_SLUGS):
        fail("deep exemplar page count must match the McDonald's/Chipotle exemplar pair")
    if counts["detailed_first_principles_pages"] != detailed_count:
        fail("detailed first-principles page count must match local detailed packets")
    if counts["packet_backed_pages"] < 200:
        fail("expected at least 200 packet-backed company pages")
    for required in (
        "Cross-Framework Company Method Report",
        "Status Tiers",
        "Sector Coverage",
        "Release Gate",
        "Damodaran method library",
        "Lyn Alden source",
    ):
        if required not in report:
            fail(f"{REPORT_MD.relative_to(ROOT)} missing {required}")
    damodaran_library = Path(registry["damodaran_method_library"])
    if not damodaran_library.exists():
        fail(f"Damodaran method library dependency missing: {damodaran_library}")
    damodaran = json.loads(damodaran_library.read_text(encoding="utf-8"))
    if damodaran.get("counts", {}).get("methods", 0) < 90:
        fail("Damodaran method library dependency has too few methods")

    for company in registry["companies"]:
        page = ROOT / company["page"]
        if not page.exists():
            fail(f"missing company page {company['page']}")
        data_path = ROOT / company["data"]
        if not data_path.exists():
            fail(f"missing company data file {company['data']}")
        data = json.loads(data_path.read_text(encoding="utf-8"))
        if data["company_slug"] != company["company_slug"]:
            fail(f"{company['data']} slug does not match registry")
        if data["analysis_status"] != company["analysis_status"]:
            fail(f"{company['data']} analysis_status does not match registry")
        if data["page"] != company["page"]:
            fail(f"{company['data']} page does not match registry")
        text = page.read_text(encoding="utf-8")
        if company["company_slug"] in DEEP_EXEMPLAR_SLUGS:
            if not data.get("deep_exemplar"):
                fail(f"{company['company_slug']} data is missing deep_exemplar flag")
            memo_path = DEEP_MEMO_DIR / f"{company['company_slug']}.md"
            if not memo_path.exists():
                fail(f"{company['company_slug']} is missing source memo {memo_path.relative_to(ROOT)}")
            memo_text = memo_path.read_text(encoding="utf-8")
            for required_phrase in (
                "Bottom Line",
                "How To Read The Company",
                "What The FY2025 Numbers Mean",
                "What The Q2 2026 Numbers Mean",
                "What Each Approach Found",
                "Final Interpretation",
            ):
                if required_phrase not in memo_text:
                    fail(f"{memo_path.relative_to(ROOT)} missing {required_phrase}")
            for section in REQUIRED_DEEP_SECTIONS:
                if section not in text:
                    fail(f"{company['page']} missing deep section {section}")
            for phrase in BANNED_DEEP_PHRASES:
                if phrase in text:
                    fail(f"{company['page']} still contains shorthand/jargon phrase {phrase}")
            for required_phrase in (
                "Deep exemplar",
                "Investor Conclusion",
                "Machine-readable JSON",
                "Compare with",
                "First principles",
                "Damodaran",
                "Lyn Alden",
                "What it found:",
                "Why it matters:",
                "Question this approach asks:",
                "Evidence used here:",
                "What would change the answer:",
            ):
                if required_phrase not in text:
                    fail(f"{company['page']} missing deep UX phrase {required_phrase}")
            if company["company_slug"] == "mcdonalds-corporation":
                for required_phrase in ("customer visits", "franchisees", "operating cash flow", "app changes behavior"):
                    if required_phrase not in text:
                        fail(f"{company['page']} missing McDonald's qualitative result phrase {required_phrase}")
            if company["company_slug"] == "chipotle-mexican-grill":
                for required_phrase in ("customer transactions", "restaurant-level margin", "new stores", "store profit"):
                    if required_phrase not in text:
                        fail(f"{company['page']} missing Chipotle qualitative result phrase {required_phrase}")
            if text.count("<tr><td>") < 8:
                fail(f"{company['page']} has too little tabular deep evidence")
        else:
            for section in REQUIRED_COMPANY_SECTIONS:
                if section not in text:
                    fail(f"{company['page']} missing section {section}")
        if company["analysis_status"] not in {
            "detailed-first-principles",
            "packet-backed",
            "roster-workbench",
        }:
            fail(f"{company['company_slug']} has invalid analysis_status")
        if len(company["damodaran_routes"]) < 5:
            fail(f"{company['company_slug']} has too few Damodaran routes")
        if len(company["lyn_alden_routes"]) < 3:
            fail(f"{company['company_slug']} has too few Lyn Alden routes")
        if len(company["other_framework_routes"]) < 3:
            fail(f"{company['company_slug']} has too few other framework routes")
        for route in company["damodaran_routes"]:
            if not route.get("use_case") or not route.get("description") or not route.get("sample_methods"):
                fail(f"{company['company_slug']} has incomplete Damodaran route")
        for route in company["lyn_alden_routes"]:
            if not route.get("id") or not route.get("source") or not route.get("when_to_use"):
                fail(f"{company['company_slug']} has incomplete Lyn Alden route")
        stack = company.get("analysis_stack", {})
        for field in (
            "operating_model_read",
            "annual_report_takeaways",
            "quarterly_takeaways",
            "signal_takeaways",
            "valuation_focus",
            "damodaran_questions",
            "lyn_macro_liquidity_checks",
            "strategy_framework_checks",
            "next_evidence_work",
        ):
            if not stack.get(field):
                fail(f"{company['company_slug']} missing analysis_stack.{field}")
        if len(stack["damodaran_questions"]) < 4:
            fail(f"{company['company_slug']} has too few Damodaran analysis questions")
        if len(stack["lyn_macro_liquidity_checks"]) < 3:
            fail(f"{company['company_slug']} has too few Lyn analysis checks")
        has_packet = any(path.endswith("company-packet.md") for path in company.get("local_artifacts", []))
        if has_packet:
            if company["analysis_status"] not in {"packet-backed", "detailed-first-principles"}:
                fail(f"{company['company_slug']} has packet artifact but wrong analysis status")
            for field in ("annual_report_takeaways", "quarterly_takeaways", "signal_takeaways"):
                if len(stack.get(field, [])) < 3:
                    fail(f"{company['company_slug']} has too little packet-derived {field}")

    print(
        "Cross-framework company pages verification passed:",
        f"{counts['companies']} companies,",
        f"{counts['company_pages']} pages,",
        f"{counts['detailed_first_principles_packets']} detailed packets",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
