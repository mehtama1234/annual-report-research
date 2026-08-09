# Source Ledger

Date baseline: 2026-08-08

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` SEC filing or exhibit
- `[Reported]` credible press or transcript provider
- `[Estimated]` derived or analyst estimate
- `[Speculative]` weak or unverified
- `[verify]` found but not yet confirmed directly

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CTAS-T1 | AnnualReports.com Cintas company page | 2026-08-08 | Aggregator page | Confirms the `Services` sector label, the odd `Apparel Stores` industry label, Cincinnati HQ, and that AnnualReports already hosts the `2025` annual package as of `2026-08-08` | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/business-services/cintas-corporation/company-page-annualreports.html) |
| CTAS-T2 | AnnualReports-hosted 2025 annual report PDF | 2026-08-08 | Annual report PDF | Captures the hosted annual report linked from AnnualReports for the fiscal year ended `2025-05-31` | `[Reported]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/business-services/cintas-corporation/2025-annual-report.pdf) |
| CTAS-T3 | SEC-filed 2025 annual report PDF / ARS | 2025-09-16 | Annual report PDF / ARS | Official annual-report artifact for the fiscal year ended `2025-05-31` | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/business-services/cintas-corporation/2025-annual-report-sec-ars.pdf) |
| CTAS-T4 | SEC submissions JSON for Cintas | 2026-08-08 | SEC index JSON | Confirms CIK, ticker, exchange, fiscal year-end, and the correct annual plus trailing-three-quarter filing chronology | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/sec-submissions.json) |
| CTAS-T5 | Cintas 2025 Form 10-K | 2025-07-28 | SEC filing HTML | Filed annual package covering route density, segment structure, operating margins, and cash generation for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/2025-10k.html) |
| CTAS-T6 | FY2026 Q2 8-K | 2025-12-18 | SEC filing HTML | Wrapper filing for fiscal Q2 `2026` earnings release | `[Filed]` | [fy2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-q2-8k.html) |
| CTAS-T7 | FY2026 Q2 earnings release exhibit | 2025-12-18 | SEC exhibit HTML | Exact fiscal Q2 `2026` metrics, margin commentary, and raised annual guidance | `[Filed]` | [fy2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-q2-earnings-release-sec-ex99.html) |
| CTAS-T8 | FY2026 Q2 Form 10-Q | 2026-01-07 | SEC filing HTML | Filed quarterly report for quarter ended `2025-11-30` | `[Filed]` | [fy2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-q2-10q.html) |
| CTAS-T9 | FY2026 Q3 8-K | 2026-03-25 | SEC filing HTML | Correct wrapper filing for fiscal Q3 `2026` earnings release and UniFirst acquisition announcement | `[Filed]` | [fy2026-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-q3-8k.html) |
| CTAS-T10 | FY2026 Q3 earnings release exhibit | 2026-03-25 | SEC exhibit HTML | Exact fiscal Q3 `2026` metrics, raised full-year guidance, and UniFirst commentary | `[Filed]` | [fy2026-q3-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-q3-earnings-release-sec-ex99.html) |
| CTAS-T11 | FY2026 Q3 Form 10-Q | 2026-04-07 | SEC filing HTML | Filed quarterly report for quarter ended `2026-02-28` | `[Filed]` | [fy2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-q3-10q.html) |
| CTAS-T12 | FY2026 Q4 8-K | 2026-07-15 | SEC filing HTML | Wrapper filing for fiscal Q4 `2026` and full-year fiscal `2026` results | `[Filed]` | [fy2026-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-q4-8k.html) |
| CTAS-T13 | FY2026 Q4 / full-year earnings release exhibit | 2026-07-15 | SEC exhibit HTML | Exact fiscal Q4 `2026` metrics, full-year fiscal `2026` metrics, free cash flow, and fiscal `2027` guidance | `[Filed]` | [fy2026-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-q4-earnings-release-sec-ex99.html) |
| CTAS-T14 | Cintas FY2026 Form 10-K | 2026-07-29 | SEC filing HTML | Filed annual package for fiscal `2026`, useful for segment updates, route scale, and the latest operating model framing | `[Filed]` | [fy2026-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/business-services/cintas-corporation/fy2026-10k.html) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-08` is `FY2026 Q4`, `FY2026 Q3`, and `FY2026 Q2`.
- The original saved `FY2026 Q3` earnings wrapper was not the earnings filing. The correct earnings 8-K was filed on `2026-03-25` under accession `0000723254-26-000006`, and the raw files were corrected to use that filing and its `EX-99` exhibit.
- The original saved `FY2026 Q2` and `FY2026 Q3` exhibit files were bad SEC object-key fetches and were replaced with the correct `EX-99` files from the matching accessions.
- AnnualReports' industry label `Apparel Stores` is preserved as a source fact, but the filing evidence shows the company functions as a route-based workplace-services, safety, and facility-services operator.

## Missing evidence

- No official transcript artifact was collected for FY2026 Q2, FY2026 Q3, or FY2026 Q4.
