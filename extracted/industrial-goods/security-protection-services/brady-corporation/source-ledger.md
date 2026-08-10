# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BRC-T1 | AnnualReports.com Brady company-page capture | 2026-08-10 | Aggregator company-page HTML | Confirms AnnualReports taxonomy and `2025` archive availability | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/security-protection-services/brady-corporation/company-page.html) |
| BRC-T2 | AnnualReports.com Brady verification note | 2026-08-10 | Aggregator verification note | Records the archive trail and taxonomy check | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/security-protection-services/brady-corporation/annualreports-verification.md) |
| BRC-T3 | Brady IR source-links note | 2026-08-10 | Official-source link ledger | Preserves the verified official IR and release URLs when direct shell retrieval was blocked | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/brady-corporation/ir-source-links.md) |
| BRC-T4 | Brady 2025 annual report PDF | 2026-08-10 collected | Annual report PDF | Local annual-report artifact for fiscal `2025` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/brady-corporation/2025-annual-report.pdf) |
| BRC-T5 | Brady 2025 Form 10-K HTML | 2025-09-04 filed / 2026-08-10 collected | Filed annual report HTML | Filed annual report for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/brady-corporation/2025-10k.html) |
| BRC-T6 | Brady fiscal Q1 2026 results release exhibit | 2025-11-17 filed / 2026-08-10 collected | SEC-hosted earnings release exhibit | Most direct local quarterly release artifact for the quarter ended `2025-10-31` | `[Filed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/brady-corporation/2026-q1-results-release.html) |
| BRC-T7 | Brady fiscal Q1 2026 Form 10-Q HTML | 2025-11-17 filed / 2026-08-10 collected | Filed quarterly report HTML | Filed quarterly report for the quarter ended `2025-10-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/brady-corporation/2026-q1-10q.html) |
| BRC-T8 | Brady fiscal Q2 2026 results release exhibit | 2026-02-19 filed / 2026-08-10 collected | SEC-hosted earnings release exhibit | Most direct local quarterly release artifact for the quarter ended `2026-01-31` | `[Filed]` | [2026-q2-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/brady-corporation/2026-q2-results-release.html) |
| BRC-T9 | Brady fiscal Q2 2026 Form 10-Q HTML | 2026-02-19 filed / 2026-08-10 collected | Filed quarterly report HTML | Filed quarterly report for the quarter ended `2026-01-31` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/brady-corporation/2026-q2-10q.html) |
| BRC-T10 | Brady fiscal Q3 2026 results release exhibit | 2026-05-18 filed / 2026-08-10 collected | SEC-hosted earnings release exhibit | Most direct local quarterly release artifact for the quarter ended `2026-04-30` | `[Filed]` | [2026-q3-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/brady-corporation/2026-q3-results-release.html) |
| BRC-T11 | Brady fiscal Q3 2026 Form 10-Q HTML | 2026-05-18 filed / 2026-08-10 collected | Filed quarterly report HTML | Filed quarterly report for the quarter ended `2026-04-30` | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/brady-corporation/2026-q3-10q.html) |
| BRC-T12 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms SEC company identity and filing chronology for the annual-plus-quarter chain | `[Filed]` | [submissions-cik0000746598.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/brady-corporation/submissions-cik0000746598.json) |

## Reconciliation notes

- Brady now has a clean annual-plus-quarterly evidence chain on disk for the `2025` annual package and the latest three reported quarters as of Monday, `2026-08-10`.
- Direct shell retrieval of Brady IR HTML pages was `403`-blocked in this environment, so the evidence chain intentionally leans on the saved AnnualReports artifacts, the saved AnnualReports annual-report PDF, and the SEC `10-K`, `10-Q`, and `8-K` exhibit chain.
- The official Brady IR release URLs are still preserved in the local source-links note so the authoritative IR trail is not lost even though the HTML pages did not mirror successfully in this shell.

## Missing evidence

- Local transcript artifacts for `Q1 FY2026`, `Q2 FY2026`, and `Q3 FY2026`.
- Saved local mirrors of Brady's official IR HTML pages and presentation files.
