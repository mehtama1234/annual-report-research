#!/usr/bin/env python3
"""Generate conservative name candidates for blank-CUSIP BA Part 3 rows."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PART1 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv"
PART2 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-parser-pass-1.csv"
PART3 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-blank-cusip-name-candidates-pass-1.csv"
SUMMARY = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-blank-cusip-name-candidates-summary-pass-1.csv"

STOP = {
    "a", "an", "and", "of", "the", "or", "from", "to", "on", "in", "for",
    "llc", "lp", "l", "p", "scsp", "ltd", "limited", "inc", "corp", "co",
    "company", "fund", "junior", "subordinated", "perpet", "perpetual", "note", "notes",
    "wilmington", "de", "cym", "lux", "irl", "nld", "fra", "gbr", "esp", "nld", "aus",
    "berkeley", "ia", "west", "des", "moines", "new", "york", "tax", "free", "exchange",
    "direct", "sale", "over", "counter", "transfer", "schedule", "d", "purchaser", "nature",
}


def tokens(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", text.lower().replace("&", " and "))
    return {word for word in words if len(word) > 2 and word not in STOP and not word.isdigit()}


def read(path: Path) -> list[dict[str, str]]:
    with path.open() as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    part1 = read(PART1)
    part2 = read(PART2)
    part3 = [row for row in read(PART3) if not row["cusip_or_identifier"]]
    candidates = []
    summary: dict[str, int] = {}

    for event_index, event in enumerate(part3, start=1):
        event_tokens = tokens(event["name_or_description_near_row"])
        scored = []
        for source_name, source_rows in (("part1", part1), ("part2", part2)):
            for source in source_rows:
                source_tokens = tokens(source["name_or_description_near_row"])
                overlap = event_tokens & source_tokens
                if len(overlap) < 2:
                    continue
                coverage = len(overlap) / max(1, min(len(event_tokens), len(source_tokens)))
                jaccard = len(overlap) / max(1, len(event_tokens | source_tokens))
                score = (coverage, jaccard, len(overlap))
                scored.append((score, source_name, source, overlap))
        scored.sort(key=lambda item: item[0], reverse=True)
        top = scored[:5]
        if not top:
            status = "no-strong-name-candidate"
        else:
            best = top[0][0]
            tied = [item for item in top if item[0] == best]
            if best[0] >= 0.75 and len(tied) == 1:
                status = "unique-high-coverage-name-candidate"
            elif best[0] >= 0.5:
                status = "ambiguous-or-partial-name-candidate"
            else:
                status = "weak-name-candidate"
        summary[status] = summary.get(status, 0) + 1
        for rank, (score, source_name, source, overlap) in enumerate(top, start=1):
            candidates.append(
                {
                    "candidate_id": f"CFAASBANC-{len(candidates)+1:04d}",
                    "part3_page": event["page"],
                    "part3_source_y": event["source_y"],
                    "part3_name": event["name_or_description_near_row"],
                    "disposal_consideration": event["disposal_consideration"],
                    "part3_row_rank": str(event_index),
                    "candidate_rank": str(rank),
                    "candidate_source": source_name,
                    "candidate_page": source["page"],
                    "candidate_row_id": source["parser_row_id"],
                    "candidate_cusip": source["cusip_or_identifier"],
                    "candidate_name": source["name_or_description_near_row"],
                    "overlap_tokens": ";".join(sorted(overlap)),
                    "coverage_score": f"{score[0]:.4f}",
                    "jaccard_score": f"{score[1]:.4f}",
                    "candidate_status": status,
                    "boundary": "Candidate-only fuzzy name bridge; requires page/row inspection and lot/transaction evidence before continuity promotion.",
                }
            )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fields = list(candidates[0]) if candidates else ["candidate_id"]
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(candidates)
    summary_rows = [{"status": key, "count": str(value), "boundary": "Candidate classification only; no fuzzy match is promoted."} for key, value in sorted(summary.items())]
    with SUMMARY.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]) if summary_rows else ["status"])
        writer.writeheader()
        writer.writerows(summary_rows)
    print(f"blank_part3_events={len(part3)} candidate_rows={len(candidates)}")
    print("status_counts=" + "; ".join(f"{key}:{value}" for key, value in sorted(summary.items())))
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"wrote {SUMMARY.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
