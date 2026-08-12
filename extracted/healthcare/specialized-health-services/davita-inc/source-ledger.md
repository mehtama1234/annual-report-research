# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| DVA-T1 | AnnualReports.com DaVita verification note | 2026-08-10 | Aggregator verification note | Confirms `Healthcare / Specialized Health Services` taxonomy and that AnnualReports still lagged at the `2024` package | `[Reported]` | [annualreports-verification.md](/raw/annualreports/healthcare/specialized-health-services/davita-inc/annualreports-verification.md) |
| DVA-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the archive-confirmation page used for taxonomy and lag verification | `[Reported]` | [company-page.html](/raw/annualreports/healthcare/specialized-health-services/davita-inc/company-page.html) |
| DVA-T3 | DaVita IR source-links note | 2026-08-10 | Official IR verification note | Preserves the official annual-report and quarterly-results source chain | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/healthcare/specialized-health-services/davita-inc/ir-source-links.md) |
| DVA-T4 | Annual report and proxy statement page | 2026-08-10 collected | Official IR HTML | Confirms the official `2025` annual report page and the direct annual-report PDF URL | `[Disclosed]` | [annual-report-and-proxy-statement.html](/raw/company-ir/healthcare/specialized-health-services/davita-inc/annual-report-and-proxy-statement.html) |
| DVA-T5 | DaVita Q4 2025 and full-year 2025 results page | 2026-08-10 collected | Official company results HTML | Preserves the official company-authored Q4 and full-year `2025` result package locally | `[Reported]` | [2025-q4-results.html](/raw/company-ir/healthcare/specialized-health-services/davita-inc/2025-q4-results.html) |
| DVA-T6 | DaVita Q1 2026 results page | 2026-08-10 collected | Official company results HTML | Preserves the official company-authored Q1 `2026` result package locally | `[Reported]` | [2026-q1-results.html](/raw/company-ir/healthcare/specialized-health-services/davita-inc/2026-q1-results.html) |
| DVA-T7 | DaVita Q2 2026 results page | 2026-08-10 collected | Official company results HTML | Preserves the official company-authored Q2 `2026` result package locally | `[Reported]` | [2026-q2-results.html](/raw/company-ir/healthcare/specialized-health-services/davita-inc/2026-q2-results.html) |
| DVA-T8 | DaVita SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms legal identity, ticker, and filing sequence for the annual and quarter chain | `[Filed]` | [CIK0000927066.json](/raw/sec/healthcare/specialized-health-services/davita-inc/CIK0000927066.json) |
| DVA-T9 | DaVita 2025 Form 10-K | 2026-02-11 | SEC filing HTML | Standalone annual filing for the year ended December 31, 2025 | `[Filed]` | [2025-10k.html](/raw/sec/healthcare/specialized-health-services/davita-inc/2025-10k.html) |
| DVA-T10 | DaVita Q4 2025 earnings filing | 2026-02-02 | SEC current report | Captures fourth-quarter and full-year `2025` results in filed form | `[Filed]` | [2025-q4-8k.html](/raw/sec/healthcare/specialized-health-services/davita-inc/2025-q4-8k.html) |
| DVA-T11 | DaVita Q1 2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for March 31, 2026 | `[Filed]` | [2026-q1-10q.html](/raw/sec/healthcare/specialized-health-services/davita-inc/2026-q1-10q.html) |
| DVA-T12 | DaVita Q1 2026 earnings filing | 2026-05-05 | SEC current report | Captures first-quarter `2026` results in filed form | `[Filed]` | [2026-q1-8k.html](/raw/sec/healthcare/specialized-health-services/davita-inc/2026-q1-8k.html) |
| DVA-T13 | DaVita Q2 2026 Form 10-Q | 2026-08-04 | SEC filing HTML | Filed quarterly report for June 30, 2026 | `[Filed]` | [2026-q2-10q.html](/raw/sec/healthcare/specialized-health-services/davita-inc/2026-q2-10q.html) |
| DVA-T14 | DaVita Q2 2026 earnings filing | 2026-08-04 | SEC current report | Captures most recent quarter results in filed form | `[Filed]` | [2026-q2-8k.html](/raw/sec/healthcare/specialized-health-services/davita-inc/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports is used only for lane taxonomy and archive confirmation because it still lagged at the `2024` package on the collection date.
- DaVita’s official IR annual-report page and quarter-result pages are saved locally, which makes the evidence chain stronger than a filing-only reconstruction.
- The SEC annual and quarterly filing chain is complete for the target window.

## Missing evidence

- The direct `2025` annual report PDF link is documented from the official annual-report page, but the PDF itself was not saved locally in this pass.
- No standalone earnings-call transcript artifact is saved locally in this pass.
