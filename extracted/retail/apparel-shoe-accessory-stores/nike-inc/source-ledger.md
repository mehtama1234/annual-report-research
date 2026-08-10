# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| NKE-T1 | AnnualReports.com Nike verification note | 2026-08-09 | Aggregator verification note | Confirms Nike classification coverage on AnnualReports and notes the unstable direct company page path | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/retail/apparel-shoe-accessory-stores/nike-inc/annualreports-verification.md) |
| NKE-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window, plus the live-site challenge constraint | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/retail/apparel-shoe-accessory-stores/nike-inc/official-ir-verification.md) |
| NKE-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000320187.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/apparel-shoe-accessory-stores/nike-inc/submissions-cik0000320187.json) |
| NKE-T4 | 2026 annual report PDF | 2026-08-09 collected | Official annual report PDF via SEC | Official annual report artifact on disk | `[Disclosed]` | [2026-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/retail/apparel-shoe-accessory-stores/nike-inc/2026-annual-report.pdf) |
| NKE-T5 | 2026 Form `10-K` | 2026-07-15 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2026-05-31` | `[Filed]` | [2026-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/apparel-shoe-accessory-stores/nike-inc/2026-10k.html) |
| NKE-T6 | 2026 Q2 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves second-quarter operating narrative and quarter metrics | `[Disclosed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/retail/apparel-shoe-accessory-stores/nike-inc/2026-q2-press-release.html) |
| NKE-T7 | 2026 Q2 earnings `8-K` | 2025-12-18 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/apparel-shoe-accessory-stores/nike-inc/2026-q2-8k.html) |
| NKE-T8 | 2026 Q2 Form `10-Q` | 2025-12-30 filed / 2026-08-09 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/apparel-shoe-accessory-stores/nike-inc/2026-q2-10q.html) |
| NKE-T9 | 2026 Q3 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves third-quarter operating narrative and quarter metrics | `[Disclosed]` | [2026-q3-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/retail/apparel-shoe-accessory-stores/nike-inc/2026-q3-press-release.html) |
| NKE-T10 | 2026 Q3 earnings `8-K` | 2026-03-31 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter `2026` results | `[Filed]` | [2026-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/apparel-shoe-accessory-stores/nike-inc/2026-q3-8k.html) |
| NKE-T11 | 2026 Q3 Form `10-Q` | 2026-04-01 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/apparel-shoe-accessory-stores/nike-inc/2026-q3-10q.html) |
| NKE-T12 | 2026 Q4 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves fourth-quarter and full-year operating narrative and quarter metrics | `[Disclosed]` | [2026-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/retail/apparel-shoe-accessory-stores/nike-inc/2026-q4-press-release.html) |
| NKE-T13 | 2026 Q4 earnings `8-K` | 2026-06-30 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2026` results | `[Filed]` | [2026-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/apparel-shoe-accessory-stores/nike-inc/2026-q4-8k.html) |

## Reconciliation notes

- Nike now has the official annual report PDF on disk plus the core SEC filing chain for the fiscal `2026` annual filing and the last three quarters in scope.
- The live Nike investor-relations HTML pages were current but challenge-gated from this environment, so the packet uses SEC-hosted company exhibits for quarter release text instead of local copies of the live IR pages.
- This is still a solid evidence chain because the company-issued press-release text is preserved in SEC Exhibit `99.1`, and the matching `10-Q` and `10-K` filings are also local.

## Missing evidence

- No standalone transcript artifacts for the `Q2`, `Q3`, or `Q4 FY2026` earnings calls are saved locally.
- No investor deck or supplementary exhibit files are included in this first Nike packet.
