# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| EXPE-T1 | AnnualReports.com Expedia verification note | 2026-08-09 | Aggregator verification note | Confirms company identity, HQ, and that AnnualReports still lagged at the `2024` annual package while leaving sector and industry blank | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/transportation-services/expedia-group-inc/annualreports-verification.md) |
| EXPE-T2 | AnnualReports company page HTML | 2026-08-09 | Aggregator page HTML | Preserves the live company-page evidence used for the verification note | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/transportation-services/expedia-group-inc/company-page.html) |
| EXPE-T3 | Expedia official IR verification note | 2026-08-09 | Official IR verification note | Confirms the live annual and trailing-quarter IR chain and the explicit platform, B2B, and advertising framing | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/transportation-services/expedia-group-inc/official-ir-verification.md) |
| EXPE-T4 | SEC submissions JSON | 2026-08-09 collected | SEC index JSON | Verifies legal name, ticker, exchange, SIC description, address, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001324424.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/transportation-services/expedia-group-inc/submissions-cik0001324424.json) |
| EXPE-T5 | Expedia Group `2025` Form `10-K` | 2026-02-13 filed / 2026-08-09 collected | Annual filing HTML | Core annual filing artifact for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/transportation-services/expedia-group-inc/2025-10k.html) |
| EXPE-T6 | Expedia Group Q4 `2025` `8-K` | 2026-02-12 filed / 2026-08-09 collected | Current-report HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/transportation-services/expedia-group-inc/2025-q4-8k.html) |
| EXPE-T7 | Expedia Group Q1 `2026` `10-Q` | 2026-05-08 filed / 2026-08-09 collected | Quarterly filing HTML | Official quarterly filing artifact for the period ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/transportation-services/expedia-group-inc/2026-q1-10q.html) |
| EXPE-T8 | Expedia Group Q1 `2026` `8-K` | 2026-05-07 filed / 2026-08-09 collected | Current-report HTML | SEC wrapper for the first-quarter earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/transportation-services/expedia-group-inc/2026-q1-8k.html) |
| EXPE-T9 | Expedia Group Q2 `2026` `10-Q` | 2026-08-06 filed / 2026-08-09 collected | Quarterly filing HTML | Official quarterly filing artifact for the period ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/transportation-services/expedia-group-inc/2026-q2-10q.html) |
| EXPE-T10 | Expedia Group Q2 `2026` `8-K` | 2026-08-05 filed / 2026-08-09 collected | Current-report HTML | SEC wrapper for the second-quarter earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/transportation-services/expedia-group-inc/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports currently leaves Expedia's sector and industry as `--None--` and only shows the `2024` annual package, so the archive uses the SEC SIC description `Transportation Services` for folder placement.
- The official IR site clearly exposes the current annual and quarterly chain, but direct shell retrieval is rate-limited in this environment.
- The packet therefore uses the official IR verification note for URL confirmation and strategic framing, while relying on the locally saved SEC filings for the durable evidence chain.

## Missing evidence

- No standalone `2025` annual-report PDF is saved locally in this pass.
- No standalone latest-quarter transcript or presentation binary is saved locally even though the official IR event page confirms they exist.
- The live Expedia IR HTML pages were not saved locally because direct shell retrieval frequently returned HTTP `429`.
