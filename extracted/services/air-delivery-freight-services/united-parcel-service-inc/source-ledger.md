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
| UPS-T1 | AnnualReports.com UPS company page | 2026-08-08 | Aggregator page | Confirms `Services` / `Air Delivery & Freight Services` classification and shows AnnualReports still lagging at `2024` for the hosted annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/air-delivery-freight-services/united-parcel-service-inc/company-page-annualreports.html) |
| UPS-T2 | SEC submissions JSON for UPS | 2026-08-08 | SEC index JSON | Confirms CIK, filing chronology, and the authoritative annual and trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/sec-submissions.json) |
| UPS-T3 | UPS 2025 annual report PDF | 2026-03-19 | Annual report PDF / ARS | Official annual-report artifact for the year ended `2025-12-31` | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/air-delivery-freight-services/united-parcel-service-inc/2025-annual-report.pdf) |
| UPS-T4 | UPS 2025 Form 10-K | 2026-02-17 | SEC filing HTML | Filed annual package covering revenues, segments, package volume, customer concentration, and transformation disclosures | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2025-10k.html) |
| UPS-T5 | Q4 2025 8-K | 2026-01-27 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2025-q4-8k.html) |
| UPS-T6 | Q4 2025 earnings release exhibit | 2026-01-27 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics, `2026` guidance, and Amazon-glide-down framing | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2025-q4-earnings-release-sec-ex99.html) |
| UPS-T7 | Q1 2026 8-K | 2026-04-28 | SEC filing HTML | Wrapper filing for first-quarter 2026 results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2026-q1-8k.html) |
| UPS-T8 | Q1 2026 earnings release exhibit | 2026-04-28 | SEC exhibit HTML | Exact Q1 2026 metrics and guidance reaffirmation during the transition quarter | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2026-q1-earnings-release-sec-ex99.html) |
| UPS-T9 | Q1 2026 Form 10-Q | 2026-05-06 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2026-q1-10q.html) |
| UPS-T10 | Q2 2026 8-K | 2026-07-28 | SEC filing HTML | Wrapper filing for second-quarter 2026 results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2026-q2-8k.html) |
| UPS-T11 | Q2 2026 earnings release exhibit | 2026-07-28 | SEC exhibit HTML | Exact Q2 2026 metrics, large transformation-charge disclosure, and raised `2026` guidance | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2026-q2-earnings-release-sec-ex99.html) |
| UPS-T12 | Q2 2026 Form 10-Q | 2026-08-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30`, including the post-glide-down operating picture | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/air-delivery-freight-services/united-parcel-service-inc/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for classification and folder taxonomy, but as of `2026-08-08` it still lags at `2024` for the hosted annual package.
- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- UPS provides both an annual-report PDF and the filed `10-K`, which makes the annual evidence chain stronger than a `10-K`-only capture.
- The quarterlies are fully covered with `8-K` wrappers, filed earnings-release exhibits, and filed `10-Q`s.

## Missing evidence

- No official transcript artifact was collected for Q4 2025, Q1 2026, or Q2 2026.
