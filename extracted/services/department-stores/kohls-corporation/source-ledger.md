# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| KSS-T1 | AnnualReports.com Kohl's verification note | 2026-08-09 | Aggregator verification note | Confirms sector / industry labeling and that AnnualReports still lagged at the `2024` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/department-stores/kohls-corporation/annualreports-verification.md) |
| KSS-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarter-results URL chain for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/department-stores/kohls-corporation/official-ir-verification.md) |
| KSS-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000885639.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/department-stores/kohls-corporation/submissions-cik0000885639.json) |
| KSS-T4 | Fiscal 2025 annual report PDF | 2026-08-09 collected | Official annual report PDF via SEC | Preserves the shareholder annual report artifact for the year ended `2026-01-31` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/department-stores/kohls-corporation/2025-annual-report.pdf) |
| KSS-T5 | Fiscal 2025 Form `10-K` | 2026-03-19 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2026-01-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/department-stores/kohls-corporation/2025-10k.html) |
| KSS-T6 | Q3 2025 earnings `8-K` | 2025-11-25 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/department-stores/kohls-corporation/2025-q3-8k.html) |
| KSS-T7 | Q3 2025 Form `10-Q` | 2025-12-03 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/department-stores/kohls-corporation/2025-q3-10q.html) |
| KSS-T8 | Q4 2025 earnings `8-K` | 2026-03-10 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/department-stores/kohls-corporation/2025-q4-8k.html) |
| KSS-T9 | Q1 2026 earnings `8-K` | 2026-05-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/department-stores/kohls-corporation/2026-q1-8k.html) |
| KSS-T10 | Q1 2026 Form `10-Q` | 2026-06-04 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/department-stores/kohls-corporation/2026-q1-10q.html) |

## Reconciliation notes

- Kohl's now has the official annual report PDF on disk plus the core SEC filing chain for the annual filing and the last three quarters in scope.
- AnnualReports still lagged at `2024` as of `2026-08-09`, so the packet relies on official IR verification plus the SEC chain for current-year coverage.
- Direct quarter result pages were browser-verifiable but shell-blocked by Cloudflare in this environment. That does not weaken the filing-backed local evidence chain because the key quarter metrics are also preserved through the SEC `8-K` and `10-Q` materials.

## Missing evidence

- No standalone local copies of Kohl's official quarter-result HTML pages are included because direct shell fetches were Cloudflare-challenged.
- No standalone verbatim earnings-call transcript artifacts for the in-scope quarters are saved locally.
