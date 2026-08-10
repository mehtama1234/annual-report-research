# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| COST-T1 | AnnualReports.com Costco verification note | 2026-08-09 | Aggregator verification note | Confirms AnnualReports still labeled `2024` as most recent on `2026-08-09` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/discount-variety-stores/costco-wholesale-corp/annualreports-verification.md) |
| COST-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window, plus the live-site challenge constraint | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/discount-variety-stores/costco-wholesale-corp/official-ir-verification.md) |
| COST-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000909832.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/discount-variety-stores/costco-wholesale-corp/submissions-cik0000909832.json) |
| COST-T4 | 2025 annual report PDF | 2026-08-09 collected | Official annual report PDF | Official annual report artifact on disk | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/discount-variety-stores/costco-wholesale-corp/2025-annual-report.pdf) |
| COST-T5 | 2025 Form `10-K` | 2025-10-08 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2025-08-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/discount-variety-stores/costco-wholesale-corp/2025-10k.html) |
| COST-T6 | 2026 Q1 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves first-quarter operating narrative and quarter metrics | `[Disclosed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/discount-variety-stores/costco-wholesale-corp/2026-q1-press-release.html) |
| COST-T7 | 2026 Q1 earnings `8-K` | 2025-12-11 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/discount-variety-stores/costco-wholesale-corp/2026-q1-8k.html) |
| COST-T8 | 2026 Q1 Form `10-Q` | 2025-12-17 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/discount-variety-stores/costco-wholesale-corp/2026-q1-10q.html) |
| COST-T9 | 2026 Q2 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves second-quarter operating narrative and quarter metrics | `[Disclosed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/discount-variety-stores/costco-wholesale-corp/2026-q2-press-release.html) |
| COST-T10 | 2026 Q2 earnings `8-K` | 2026-03-05 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/discount-variety-stores/costco-wholesale-corp/2026-q2-8k.html) |
| COST-T11 | 2026 Q2 Form `10-Q` | 2026-03-11 filed / 2026-08-09 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/discount-variety-stores/costco-wholesale-corp/2026-q2-10q.html) |
| COST-T12 | 2026 Q3 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves third-quarter operating narrative and quarter metrics | `[Disclosed]` | [2026-q3-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/discount-variety-stores/costco-wholesale-corp/2026-q3-press-release.html) |
| COST-T13 | 2026 Q3 earnings `8-K` | 2026-05-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter `2026` results | `[Filed]` | [2026-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/discount-variety-stores/costco-wholesale-corp/2026-q3-8k.html) |
| COST-T14 | 2026 Q3 Form `10-Q` | 2026-06-03 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/discount-variety-stores/costco-wholesale-corp/2026-q3-10q.html) |

## Reconciliation notes

- Costco now has the official annual report PDF on disk plus the core SEC filing chain for the fiscal `2025` annual filing and the last three quarters in scope.
- The live Costco investor-relations HTML pages were current but challenge-gated from this environment, so the packet uses SEC-hosted company exhibits for quarter release text instead of local copies of the live IR pages.
- This is still a solid evidence chain because the company-issued press-release text is preserved in SEC Exhibit `99.1`, and the matching `10-Q` filings are also local.

## Missing evidence

- No standalone transcript artifacts for the `Q1 2026`, `Q2 2026`, or `Q3 2026` earnings calls are saved locally.
- No investor deck or supplementary Exhibit `99.2` files are included in this first Costco packet.
