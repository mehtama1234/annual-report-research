# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CMI-T1 | AnnualReports.com Cummins verification note | 2026-08-10 | Aggregator verification note | Confirms Cummins taxonomy and shows AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/annualreports/industrial-goods/farm-construction-machinery/cummins-inc/annualreports-verification.md) |
| CMI-T2 | Cummins AnnualReports company page | 2026-08-10 | Aggregator page capture | Preserves the archive confirmation page | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/annualreports/industrial-goods/farm-construction-machinery/cummins-inc/company-page.html) |
| CMI-T3 | Cummins IR source links note | 2026-08-10 | Official IR link map | Captures the annual and quarterly company-controlled entry points | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/ir-source-links.md) |
| CMI-T4 | Cummins investor home | 2026-08-10 | Official IR page | Confirms the current investor-relations surface | `[Disclosed]` | [investor-home.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/investor-home.html) |
| CMI-T5 | Cummins annual reports page | 2026-08-10 | Official IR page | Confirms the annual-report surface | `[Disclosed]` | [annual-reports.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/annual-reports.html) |
| CMI-T6 | Cummins financial results page | 2026-08-10 | Official IR page | Confirms the quarterly release surface | `[Disclosed]` | [financial-results.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/financial-results.html) |
| CMI-T7 | Cummins 2025 annual report PDF | 2026-02-10 | Annual report PDF | Official annual report artifact | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/2025-annual-report.pdf) |
| CMI-T8 | Cummins 2025 10-K PDF | 2026-02-10 | Annual filing PDF | Official annual filing artifact | `[Disclosed]` | [2025-10k.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/2025-10k.pdf) |
| CMI-T9 | Cummins Q4 2025 earnings release PDF | 2026-02-04 | Earnings release PDF | Preserves the year-end segment and data-center power discussion | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/2025-q4-earnings-release.pdf) |
| CMI-T10 | Cummins Q1 2026 earnings release PDF | 2026-05-05 | Earnings release PDF | Preserves first-quarter demand and Accelera charge discussion | `[Disclosed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/2026-q1-earnings-release.pdf) |
| CMI-T11 | Cummins Q2 2026 earnings release PDF | 2026-08-05 | Earnings release PDF | Preserves latest-quarter record revenue and raised guidance | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/industrial-goods/farm-construction-machinery/cummins-inc/2026-q2-earnings-release.pdf) |
| CMI-T12 | Cummins SEC submissions JSON | 2026-08-10 | SEC index JSON | Verifies legal name, ticker, exchange, fiscal year-end, and the filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/industrial-goods/farm-construction-machinery/cummins-inc/sec-submissions.json) |

## Reconciliation notes

- Cummins' saved evidence chain is local, but it lives in `annual-report-research-cli8-middle-layer-imported-2026-08-10`, not under `annual-report-research/main/raw`.
- The chain is complete for the required window:
  - `2025` annual report PDF and `10-K`
  - Q4 `2025` earnings release
  - Q1 `2026` earnings release and `10-Q`
  - Q2 `2026` earnings release and `10-Q`
- The current saved local proof relies mainly on company-IR PDFs plus the SEC submissions index rather than a fuller SEC HTML and transcript chain.

## Missing evidence

- The raw evidence has not been reintegrated into `annual-report-research/main/raw`; the saved proof currently lives in the imported sibling worktree.
- No local earnings-call transcript was saved for the covered quarters.
