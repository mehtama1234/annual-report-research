# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BBY-T1 | AnnualReports.com Best Buy verification note | 2026-08-09 | Aggregator verification note | Confirms sector / industry labeling and that AnnualReports lists the latest package as the `2026 Annual Report and Form 10K` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/electronics-stores/best-buy-co-inc/annualreports-verification.md) |
| BBY-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/electronics-stores/best-buy-co-inc/official-ir-verification.md) |
| BBY-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000764478.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/electronics-stores/best-buy-co-inc/submissions-cik0000764478.json) |
| BBY-T4 | Fiscal 2026 annual report PDF | 2026-08-09 collected | Official annual report PDF | Preserves the shareholder annual report artifact for the year ended `2026-01-31` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/electronics-stores/best-buy-co-inc/2025-annual-report.pdf) |
| BBY-T5 | FY26 Form `10-K` | 2026-03-18 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2026-01-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/electronics-stores/best-buy-co-inc/2025-10k.html) |
| BBY-T6 | Q3 FY26 results release | 2025-11-25 published / 2026-08-09 collected | Company results page HTML | Preserves the quarter narrative around positive comps, category strength, Marketplace launch, and Best Buy Health impairments | `[Disclosed]` | [2025-q3-results-release.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/electronics-stores/best-buy-co-inc/2025-q3-results-release.html) |
| BBY-T7 | Q3 FY26 earnings `8-K` | 2025-11-25 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter FY26 results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/electronics-stores/best-buy-co-inc/2025-q3-8k.html) |
| BBY-T8 | Q3 FY26 Form `10-Q` | 2025-12-05 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/electronics-stores/best-buy-co-inc/2025-q3-10q.html) |
| BBY-T9 | Q4 FY26 results release | 2026-03-03 published / 2026-08-09 collected | Company results page HTML | Preserves the full-year FY26 narrative around mixed holiday demand, positive full-year comps, Marketplace scale, and Best Buy Ads growth | `[Disclosed]` | [2025-q4-results-release.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/electronics-stores/best-buy-co-inc/2025-q4-results-release.html) |
| BBY-T10 | Q4 FY26 earnings `8-K` | 2026-03-03 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year FY26 results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/electronics-stores/best-buy-co-inc/2025-q4-8k.html) |
| BBY-T11 | Q1 FY27 results release | 2026-05-28 published / 2026-08-09 collected | Company results page HTML | Preserves the quarter narrative around better-than-expected comps and stronger Marketplace and Ads contribution | `[Disclosed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/electronics-stores/best-buy-co-inc/2026-q1-results-release.html) |
| BBY-T12 | Q1 FY27 earnings `8-K` | 2026-05-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter FY27 results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/electronics-stores/best-buy-co-inc/2026-q1-8k.html) |
| BBY-T13 | Q1 FY27 Form `10-Q` | 2026-06-05 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter FY27 report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/electronics-stores/best-buy-co-inc/2026-q1-10q.html) |

## Reconciliation notes

- Best Buy now has the official annual report PDF on disk plus the core SEC filing chain for the annual filing and the last three quarters in scope.
- The archive labels the annual package as target year `2025` even though Best Buy and AnnualReports present it as the `2026` annual report, because the report covers the year ended `2026-01-31` and sits inside the archive's late-`2025` / `2026` review window.
- Best Buy's own quarter labels are `Q3 FY26`, `Q4 FY26`, and `Q1 FY27`; the archive maps those to the calendar-window sequence `Q3 2025`, `Q4 2025`, and `Q1 2026`.

## Missing evidence

- No standalone verbatim earnings-call transcript artifacts for the in-scope quarters are saved locally.
- No direct local HTML snapshot of the AnnualReports company page is saved; the packet relies on a verification note because live search coverage was enough to confirm the taxonomy and latest hosted annual package.
