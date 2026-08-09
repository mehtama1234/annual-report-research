# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BURL-T1 | AnnualReports.com Burlington verification note | 2026-08-09 | Aggregator verification note | Confirms sector / industry labeling and that AnnualReports already exposed the `2025` annual-report year | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/consumer-goods/discount-variety-stores/burlington-stores-inc/annualreports-verification.md) |
| BURL-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the annual-reports page, quarter-result URL chain, and the shell-side fetch failure pattern | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/consumer-goods/discount-variety-stores/burlington-stores-inc/official-ir-verification.md) |
| BURL-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001579298.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/discount-variety-stores/burlington-stores-inc/submissions-cik0001579298.json) |
| BURL-T4 | 2025 annual report PDF | 2026-08-09 collected | SEC annual report PDF | Annual-report-to-security-holders artifact preserved locally | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/consumer-goods/discount-variety-stores/burlington-stores-inc/2025-annual-report.pdf) |
| BURL-T5 | 2025 Form `10-K` | 2026-03-19 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the fiscal year ended `2026-01-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/discount-variety-stores/burlington-stores-inc/2025-10k.html) |
| BURL-T6 | 2025 Q3 earnings `8-K` | 2025-11-25 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/discount-variety-stores/burlington-stores-inc/2025-q3-8k.html) |
| BURL-T7 | 2025 Q3 Form `10-Q` | 2025-11-25 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/discount-variety-stores/burlington-stores-inc/2025-q3-10q.html) |
| BURL-T8 | 2025 Q4 earnings `8-K` | 2026-03-05 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/discount-variety-stores/burlington-stores-inc/2025-q4-8k.html) |
| BURL-T9 | 2026 Q1 earnings `8-K` | 2026-05-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/discount-variety-stores/burlington-stores-inc/2026-q1-8k.html) |
| BURL-T10 | 2026 Q1 Form `10-Q` | 2026-05-28 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/discount-variety-stores/burlington-stores-inc/2026-q1-10q.html) |

## Reconciliation notes

- Burlington now has a full evidence chain on disk for the `2025` annual-report window and the last three reported quarters in scope as of `2026-08-09`.
- The main remaining collection gap is not the SEC chain. It is the official IR binary and page capture layer, because Burlington's investor site repeatedly failed or timed out in this shell environment.
- For now, the archive treats the official IR URLs as verified and the SEC filings as the durable local record of the quarter chain.
