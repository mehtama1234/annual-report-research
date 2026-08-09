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
| KMB-T1 | AnnualReports.com Kimberly-Clark company page | 2026-08-08 | Aggregator page | Confirms Consumer Goods / Personal Products classification and that AnnualReports now lists the `2025` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/consumer-goods/personal-products/kimberly-clark-corp/company-page-annualreports.html) |
| KMB-T2 | Kimberly-Clark 2025 annual report to security holders | 2026-03-23 | Annual report PDF | Core annual narrative, annual highlights, and management framing | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/consumer-goods/personal-products/kimberly-clark-corp/2025-annual-report-sec-ars.pdf) |
| KMB-T3 | Kimberly-Clark 2025 Form 10-K | 2026-02-12 | SEC filing HTML | Standalone annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/personal-products/kimberly-clark-corp/2025-10k.html) |
| KMB-T4 | Kimberly-Clark Q4 2025 earnings release exhibit | 2026-01-27 | SEC exhibit HTML | Quarter-end and full-year 2025 metrics, margin detail, and 2026 setup | `[Filed]` | [2025-q4-earnings-release-sec-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/personal-products/kimberly-clark-corp/2025-q4-earnings-release-sec-ex99-1.html) |
| KMB-T5 | Kimberly-Clark Q4 2025 pre-recorded management discussion transcript | 2026-01-27 | Filed transcript HTML | Powering Care framing, durable-growth language, and cash-flow / leverage algorithm | `[Filed]` | [2025-q4-pre-recorded-management-discussion-transcript.html](/home/manishmehta/ui-projects/annual-report-research/raw/earnings-calls/consumer-goods/personal-products/kimberly-clark-corp/2025-q4-pre-recorded-management-discussion-transcript.html) |
| KMB-T6 | Kimberly-Clark Q1 2026 earnings release exhibit | 2026-04-28 | SEC exhibit HTML | Exact first-quarter 2026 metrics, organic growth bridge, and guidance reaffirmation | `[Filed]` | [2026-q1-earnings-release-sec-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/personal-products/kimberly-clark-corp/2026-q1-earnings-release-sec-ex99-1.html) |
| KMB-T7 | Kimberly-Clark Q1 2026 Form 10-Q | 2026-04-28 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/personal-products/kimberly-clark-corp/2026-q1-10q.html) |
| KMB-T8 | Kimberly-Clark Q2 2026 earnings release exhibit | 2026-08-04 | SEC exhibit HTML | Exact second-quarter and first-half 2026 metrics, China-disruption disclosure, and updated outlook | `[Filed]` | [2026-q2-earnings-release-sec-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/personal-products/kimberly-clark-corp/2026-q2-earnings-release-sec-ex99-1.html) |
| KMB-T9 | Kimberly-Clark Q2 2026 Form 10-Q | 2026-08-04 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/personal-products/kimberly-clark-corp/2026-q2-10q.html) |

## Reconciliation notes

- Kimberly-Clark now has a complete annual evidence chain for current scope through the `2025` annual report package and standalone `2025` Form `10-K`.
- The trailing-three-quarter scope is fully covered for `Q2 2026`, `Q1 2026`, and `Q4 2025` using SEC filings and exhibits, plus a filed management-discussion transcript for `Q4 2025`.
- AnnualReports is currently useful for both classification and annual-package confirmation here; unlike some peers, the Kimberly-Clark page already lists the `2025` annual report.
- Direct official IR page fetches were partially blocked by Cloudflare during collection, so the cleanest evidence chain for this company is AnnualReports for classification plus SEC-hosted annual and quarterly materials for the underlying facts.

## Missing evidence

- No official latest-quarter earnings-call transcript was collected for `Q2 2026`.
- `raw/company-ir/consumer-goods/personal-products/kimberly-clark-corp/2025-annual-report.pdf` is a failed `404` fetch and should not be used as evidence.
- `raw/company-ir/consumer-goods/personal-products/kimberly-clark-corp/annual-reports-page.html` is a Cloudflare challenge page and should not be used as evidence.
