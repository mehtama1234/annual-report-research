# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| EHAB-T1 | AnnualReports.com Enhabit verification note | 2026-08-10 | Aggregator verification note | Confirms the company page and records that AnnualReports lagged at the `2024` package on the collection date | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/healthcare/specialized-health-services/enhabit-inc/annualreports-verification.md) |
| EHAB-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the archive-confirmation page used for taxonomy verification | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/healthcare/specialized-health-services/enhabit-inc/company-page.html) |
| EHAB-T3 | Enhabit IR source-links note | 2026-08-10 | Official IR verification note | Preserves the official quarter-results URL chain and the collection note about IR rate limiting | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/healthcare/specialized-health-services/enhabit-inc/ir-source-links.md) |
| EHAB-T4 | Enhabit SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms legal identity, filing sequence, and that the standalone quarter chain ends with `Q1 2026` before the merger close | `[Filed]` | [submissions.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/submissions.json) |
| EHAB-T5 | Enhabit 2025 Form 10-K | 2026-03-05 | SEC filing HTML | Standalone annual filing for the year ended December 31, 2025 | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/2025-10k.html) |
| EHAB-T6 | Enhabit Q4 2025 earnings filing | 2026-03-04 | SEC current report | Captures fourth-quarter and full-year `2025` results in filed form | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/2025-q4-8k.html) |
| EHAB-T7 | Enhabit Q1 2026 Form 10-Q | 2026-05-07 | SEC filing HTML | Filed quarterly report for March 31, 2026 and the best local artifact for the final standalone quarter | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/2026-q1-10q.html) |
| EHAB-T8 | Enhabit Q1 2026 merger-vote filing | 2026-05-12 | SEC current report | Confirms stockholder approval and intended close on May 15, 2026 | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/2026-q1-8k.html) |
| EHAB-T9 | Enhabit merger agreement announcement | 2026-02-23 | SEC current report | Establishes the Kinderhook transaction, `$13.80` per-share cash consideration, and pending take-private context | `[Filed]` | [2026-02-23-merger-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/2026-02-23-merger-8k.html) |
| EHAB-T10 | Enhabit merger close filing | 2026-05-15 | SEC current report | Confirms merger close, delisting process, and end of the standalone public-company reporting chain | `[Filed]` | [2026-05-15-postclose-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/2026-05-15-postclose-8k.html) |
| EHAB-T11 | Enhabit Q3 2025 Form 10-Q | 2025-11-05 | SEC filing HTML | Filed quarterly report for September 30, 2025 | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/2025-q3-10q.html) |
| EHAB-T12 | Enhabit Q3 2025 earnings filing | 2025-11-05 | SEC current report | Captures third-quarter `2025` results in filed form | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/enhabit-inc/2025-q3-8k.html) |

## Reconciliation notes

- AnnualReports is used for taxonomy and archive confirmation only.
- Company IR is documented for source tracing, but direct automated fetches returned HTTP `429` on `2026-08-10`, so the preserved local evidence chain relies on SEC artifacts.
- The target quarter window is not the standard calendar-year `Q2 2026 / Q1 2026 / Q4 2025` chain because the merger closed on `2026-05-15`; as of `2026-08-10`, the latest three reported standalone quarters are `Q1 2026`, `Q4 2025`, and `Q3 2025`.

## Missing evidence

- No company IR HTML or PDF artifact was saved locally in this pass because of rate limiting on the Enhabit IR site.
- No standalone earnings-call transcript artifact is saved locally in this pass.

