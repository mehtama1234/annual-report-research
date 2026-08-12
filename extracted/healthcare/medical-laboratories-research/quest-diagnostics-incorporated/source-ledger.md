# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| DGX-T1 | AnnualReports.com Quest verification note | 2026-08-10 | Aggregator verification note | Confirms `Healthcare / Medical Laboratories & Research` taxonomy and that AnnualReports still lagged at the `2024` package | `[Reported]` | [annualreports-verification.md](/raw/annualreports/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/annualreports-verification.md) |
| DGX-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the archive-confirmation page used for taxonomy and lag verification | `[Reported]` | [company-page.html](/raw/annualreports/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/company-page.html) |
| DGX-T3 | Quest IR source-links note | 2026-08-10 | Official IR verification note | Preserves the official annual-report and quarterly-results source chain, including the Cloudflare caveat on direct shell fetches | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/ir-source-links.md) |
| DGX-T4 | Quest Q4 2025 and full-year 2025 results page | 2026-08-10 collected | Official company results HTML | Preserves the official company-authored Q4 and full-year `2025` result package locally | `[Reported]` | [2025-q4-results.html](/raw/company-ir/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2025-q4-results.html) |
| DGX-T5 | Quest Q1 2026 results page | 2026-08-10 collected | Official company results HTML | Preserves the official company-authored Q1 `2026` result package locally | `[Reported]` | [2026-q1-results.html](/raw/company-ir/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2026-q1-results.html) |
| DGX-T6 | Quest Q2 2026 results page | 2026-08-10 collected | Official company results HTML | Preserves the official company-authored Q2 `2026` result package locally | `[Reported]` | [2026-q2-results.html](/raw/company-ir/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2026-q2-results.html) |
| DGX-T7 | Quest SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms legal identity, ticker, and filing sequence for the annual and quarter chain | `[Filed]` | [CIK0001022079.json](/raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/CIK0001022079.json) |
| DGX-T8 | Quest 2025 Form 10-K | 2026-02-26 | SEC filing HTML | Standalone annual filing for the year ended December 31, 2025 | `[Filed]` | [2025-10k.html](/raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2025-10k.html) |
| DGX-T9 | Quest Q4 2025 earnings filing | 2026-02-10 | SEC current report | Captures fourth-quarter and full-year `2025` results in filed form | `[Filed]` | [2025-q4-8k.html](/raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2025-q4-8k.html) |
| DGX-T10 | Quest Q1 2026 Form 10-Q | 2026-04-22 | SEC filing HTML | Filed quarterly report for March 31, 2026 | `[Filed]` | [2026-q1-10q.html](/raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2026-q1-10q.html) |
| DGX-T11 | Quest Q1 2026 earnings filing | 2026-04-21 | SEC current report | Captures first-quarter `2026` results in filed form | `[Filed]` | [2026-q1-8k.html](/raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2026-q1-8k.html) |
| DGX-T12 | Quest Q2 2026 Form 10-Q | 2026-07-23 | SEC filing HTML | Filed quarterly report for June 30, 2026 | `[Filed]` | [2026-q2-10q.html](/raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2026-q2-10q.html) |
| DGX-T13 | Quest Q2 2026 earnings filing | 2026-07-23 | SEC current report | Captures most recent quarter results in filed form | `[Filed]` | [2026-q2-8k.html](/raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports is used only for lane taxonomy and archive confirmation because it still lagged at the `2024` package on the collection date.
- The official Quest annual-reports page confirmed that the `2025 10-K` was posted, but direct shell fetches of the IR index pages returned Cloudflare challenge HTML.
- The authoritative annual and quarterly evidence is still complete because the quarter result pages were saved from the official company newsroom and the SEC filing chain is fully local.

## Missing evidence

- No standalone annual-report PDF was saved locally in this pass because the official annual-reports index page required browser rendering, but the `2025` annual filing itself is preserved in local SEC HTML form.
- No standalone earnings-call transcript artifact is saved locally in this pass.
