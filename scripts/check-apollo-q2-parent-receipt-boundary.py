#!/usr/bin/env python3
"""Reproduce the Apollo Q2 parent-receipt companyfacts boundary."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FACTS = ROOT / "raw" / "sec" / "companyfacts" / "financial" / "asset-management" / "apollo-global-management-inc" / "companyfacts.json"
ACCESSION = "0001858681-26-000040"
SEARCH_TERMS = ("dividend", "distribution", "intercompany", "affiliate", "receipt")
UPSTREAM_TERMS = ("received", "receipt", "intercompany", "affiliate")


def main() -> int:
    if not FACTS.is_file():
        raise SystemExit(f"FAIL: missing {FACTS.relative_to(ROOT)}")
    data = json.loads(FACTS.read_text(encoding="utf-8"))
    matched: list[tuple[str, str, str, str, int | float | str]] = []
    upstream: list[tuple[str, str, str, str, int | float | str]] = []

    for namespace, facts in data.get("facts", {}).items():
        for tag, fact in facts.items():
            searchable = f"{tag} {fact.get('label', '')}".lower()
            if not any(term in searchable for term in SEARCH_TERMS):
                continue
            for unit, items in fact.get("units", {}).items():
                for item in items:
                    if item.get("accn") != ACCESSION:
                        continue
                    row = (
                        f"{namespace}:{tag}",
                        str(fact.get("label", "")),
                        unit,
                        str(item.get("end", "")),
                        item.get("val", ""),
                    )
                    matched.append(row)
                    if any(term in searchable for term in UPSTREAM_TERMS):
                        upstream.append(row)

    if len(matched) != 29:
        raise SystemExit(f"FAIL: expected 29 accession-filtered dividend/distribution facts, found {len(matched)}")
    if upstream:
        raise SystemExit(f"FAIL: unexpected upstream-receipt candidates: {upstream}")

    print(
        "Apollo Q2 parent-receipt boundary passed: "
        f"accession {ACCESSION}, {len(matched)} dividend-related facts, "
        "0 upstream-receipt/intercompany/affiliate facts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
