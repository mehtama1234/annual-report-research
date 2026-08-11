# Repo Coverage Audit

Date baseline: 2026-08-09

## Packet Inputs Used

- the normalized tracker files under `indexes/` that establish company, coverage, and theme counts
- the current repo state on `main` at the audited snapshot and the machine-parseable cleanup done in that pass
- the archive's existing sector briefs, company packets, and theme memos that support the claims about current synthesis depth
- the gap analysis around annual-report coverage and transcript density that determines the next collection priorities
- the repo standard that coverage quality should be judged not only by document presence but also by interpretive usefulness

## Current state

The research workspace is now committed and machine-parseable.

- repo: `annual-report-research`
- branch: `main`
- latest archive snapshot before this audit: `550a53a`

Tracker normalization completed in this pass:

- `indexes/companies.csv`
- `indexes/coverage-tracker.csv`
- `indexes/theme-tracker.csv`

Those files previously contained unescaped commas in company names, linked-company lists, and notes fields. They now parse cleanly as CSV.

## Coverage totals

- companies tracked: `55`
- themes tracked: `17`
- total theme evidence count: `360`

Coverage tracker totals:

- annual reports collected: `54 / 55`
- annual filings collected: `55 / 55`
- latest quarter collected: `55 / 55`
- prior quarter collected: `55 / 55`
- third quarter collected: `55 / 55`
- latest call transcript collected: `13 / 55`

## Sector snapshot

| Sector | Companies | Annual reports | Annual filings | Latest transcripts |
|---|---:|---:|---:|---:|
| Consumer Goods | 6 | 6 | 6 | 1 |
| Financial | 17 | 16 | 17 | 5 |
| Healthcare | 6 | 6 | 6 | 1 |
| Industrial Goods | 8 | 8 | 8 | 0 |
| Services | 5 | 5 | 5 | 0 |
| Technology | 13 | 13 | 13 | 6 |

## Missing annual-report binaries

These are the remaining annual-report gaps in the tracker:

1. Financial / T. Rowe Price Group, Inc.

This is now a single archive-quality tail item, not a broad evidence-chain gap. The SEC filing chain and quarterlies are already present.

## What the archive already says

- Technology is broad enough to support a strong first-pass AI stack and workflow-infrastructure read across platform owners, semiconductors, control layers, cybersecurity, enterprise services, and weaker incumbents.
- Financial is the deepest sector by company count and the best place to study hidden infrastructure economics: scale banks, payments, insurance, public-markets asset management, alternatives, custody, exchanges, and ratings/data.
- Consumer Goods, Healthcare, Industrial Goods, and Services now each have enough breadth for sector-level synthesis, even where transcript depth is still thin.
- Cross-sector work is already substantial enough to support themes around operating infrastructure, trust and automation, regulation, and capital concentration.

## Main weaknesses

1. Transcript coverage is thin.
   Only `13 / 55` companies have the latest transcript saved locally.

2. A small annual-report tail remains.
   Only `1` company still lacks the annual-report binary in the archive.
   The remaining gap is T. Rowe Price, where the official `2025` annual-report PDF is browser-verified but still not retrievable from this machine: standard shell clients stall or fail after connect, an IPv4-only `wget --spider` check timed out waiting for response headers after TLS connect, and a local Playwright / Chromium browser pass on `2026-08-09` returned `403 Access Denied` on both the annual-reports page and the direct asset URL.

3. Services and Industrial Goods are good enough for synthesis but still lighter than Financial and Technology in commentary depth.

4. AnnualReports.com lag remains common.
   Several company pages still show `2024` even where official IR or SEC already provides the correct `2025` annual package.

## Next collection priorities

1. Close the final remaining annual-report gap first.
   That is the cleanest path to a functionally complete `2025` annual archive.

2. Raise transcript density in Financial.
   That sector has the most analytical leverage and still the largest commentary gap.

3. Add transcript depth in Services and Industrial Goods.
   Those sectors now have enough company breadth that management language would materially improve theme quality.

4. Continue turning the sector packets into stronger cross-sector memos.
   The repo already has enough evidence to sharpen industrial, consumer, cultural, and institutional-operating themes without waiting for full transcript completeness.

## Working conclusion

This repo is no longer just a file dump. It is now a structured research archive with clean trackers, near-complete annual and quarterly coverage, and enough sector breadth to support deeper synthesis work. The next phase should focus less on basic collection and more on closing the final annual-report gap and improving transcript-backed interpretation where it matters most.

## Insight-System Maintenance

When you need to confirm that this repo-coverage audit, the tracker layer, and the broader continuation surfaces still line up before relying on its status claims, use:

- `bash scripts/run-insight-audit-stack.sh`
- `bash scripts/refresh-note-layer-boundary.sh`
- `bash scripts/audit-audit-stack-terminology.sh`
- `bash scripts/audit-maintenance-doc-stack.sh`
- `bash scripts/audit-continuation-mode-links.sh`
- `bash scripts/audit-remaining-brief-links.sh`
- `bash scripts/audit-remaining-stack-links.sh`
- `bash scripts/audit-browser-review-links.sh`
- `bash scripts/verify-insight-system.sh`

## Skeptical Reader Test

- Does this audit identify the exact tracker and coverage evidence behind its totals and status claims?
- Can a skeptical reader tell which parts of the repo are strong because of real evidence coverage and which parts are still weak because of transcript or interpretation gaps?
- Does the note separate “documents exist” from “the archive can explain the sector well”?
- What missing tracker evidence or contradictory repo state would weaken the conclusion that the archive has moved past file-dump status?
