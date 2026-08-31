#!/usr/bin/env python3
"""Verify first-principles company analysis artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_ROOT = ROOT / "analysis" / "company-first-principles"

REQUIRED_MD_SECTIONS = [
    "## Core First-Principles Read",
    "## Evidence Base",
    "## Customer Insight",
    "## Operating Insight",
    "## Investment Read",
    "## Axial Codes",
    "## Finding-To-Insight Map",
    "## What Would Prove This Wrong",
    "## Reflection And Next Questions",
    "## Source Register",
    "## Coverage Gaps",
]

REQUIRED_JSON_FIELDS = [
    "company",
    "ticker",
    "primary_question",
    "core_answer",
    "source_register",
    "external_sources",
    "source_discovery_audit",
    "mechanisms",
    "financial_base",
    "operating_evidence",
    "axial_codes",
    "investment_read",
    "deep_questions",
    "deeper_insights",
    "disconfirming_tests",
    "reflection",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def verify_company(directory: Path) -> list[str]:
    messages: list[str] = []
    md_path = directory / "company-analysis.md"
    json_path = directory / "company-analysis.json"

    if not md_path.exists():
        fail(f"missing {md_path.relative_to(ROOT)}")
    if not json_path.exists():
        fail(f"missing {json_path.relative_to(ROOT)}")

    markdown = md_path.read_text(encoding="utf-8")
    for section in REQUIRED_MD_SECTIONS:
        if section not in markdown:
            fail(f"{md_path.relative_to(ROOT)} missing section {section}")

    data = json.loads(json_path.read_text(encoding="utf-8"))
    for field in REQUIRED_JSON_FIELDS:
        if field not in data:
            fail(f"{json_path.relative_to(ROOT)} missing field {field}")

    if len(data["source_register"]) < 5:
        fail(f"{json_path.relative_to(ROOT)} has too few sources")
    for source in data["source_register"]:
        if not (ROOT / source).exists():
            fail(f"source path does not exist: {source}")
    if len(data["external_sources"]) < 3:
        fail("external_sources needs at least three URLs")
    required_lanes = {
        "filings_and_financials",
        "corporate_product_and_value_pages",
        "corporate_technology_pages",
        "earnings_call_and_management_color",
        "trade_press_and_operator_checks",
        "weird_signal_scan",
        "peer_and_disconfirmation_scan",
    }
    audit_lanes = {entry.get("lane") for entry in data["source_discovery_audit"]}
    missing_lanes = sorted(required_lanes - audit_lanes)
    if missing_lanes:
        fail(f"source_discovery_audit missing lanes: {', '.join(missing_lanes)}")
    for entry in data["source_discovery_audit"]:
        for field in ("lane", "status", "what_it_found"):
            if not entry.get(field):
                fail(f"source discovery audit missing {field}")
    if len(data["mechanisms"]) < 5:
        fail("mechanisms needs at least five entries")
    for mechanism in data["mechanisms"]:
        for field in ("name", "what_happened", "first_principles_read", "what_to_verify_next"):
            if not mechanism.get(field):
                fail(f"mechanism missing {field}")

    if len(data["operating_evidence"]) < 3:
        fail("operating_evidence needs at least three entries")
    for item in data["operating_evidence"]:
        if not item.get("claim") or not item.get("sources"):
            fail("each operating_evidence item needs claim and sources")
        for source in item["sources"]:
            if not (ROOT / source).exists():
                fail(f"operating evidence source path does not exist: {source}")

    if len(data["axial_codes"]) < 5:
        fail("axial_codes needs at least five codes")
    for code in data["axial_codes"]:
        for field in ("code", "definition", "evidence_trigger", "cross_company_use"):
            if not code.get(field):
                fail(f"axial code missing {field}")

    financial = data["financial_base"]
    for field in (
        "fy2025_revenue_usd",
        "fy2025_net_income_usd",
        "fy2025_operating_cash_flow_usd",
        "fy2025_capex_usd",
    ):
        if not isinstance(financial.get(field), (int, float)) or financial[field] <= 0:
            fail(f"financial_base.{field} must be positive")

    reflection = data["reflection"]
    if len(data["deep_questions"]) < 5:
        fail("deep_questions needs at least five questions")
    for question in data["deep_questions"]:
        for field in ("question", "why_it_matters", "evidence_needed_next"):
            if not question.get(field):
                fail(f"deep question missing {field}")
    if len(data["deeper_insights"]) < 5:
        fail("deeper_insights needs at least five insights")
    if len(reflection.get("next_questions", [])) < 3:
        fail("reflection needs at least three next questions")
    if len(reflection.get("new_codes_to_test", [])) < 3:
        fail("reflection needs at least three new codes to test")
    if len(data["disconfirming_tests"]) < 3:
        fail("disconfirming_tests needs at least three tests")

    messages.append(f"OK: {directory.relative_to(ROOT)}")
    return messages


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Company analysis directories. Defaults to every directory with company-analysis.json.",
    )
    args = parser.parse_args()

    directories = args.paths
    if not directories:
        directories = sorted(path.parent for path in ANALYSIS_ROOT.glob("*/*/*/company-analysis.json"))
    if not directories:
        fail("no company-analysis.json files found")

    for directory in directories:
        target = directory if directory.is_absolute() else ROOT / directory
        for message in verify_company(target):
            print(message)
    return 0


if __name__ == "__main__":
    sys.exit(main())
