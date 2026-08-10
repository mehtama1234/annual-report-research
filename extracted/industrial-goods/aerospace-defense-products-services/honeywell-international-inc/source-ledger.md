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
| HON-T1 | AnnualReports.com Honeywell company page | 2026-08-08 | Aggregator page | Confirms the legacy Industrial Goods / Aerospace/Defense Products & Services classification and shows that AnnualReports still lags at `2024` for the hosted annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/company-page-annualreports.html) |
| HON-T2 | SEC submissions JSON for Honeywell | 2026-08-08 | SEC index JSON | Confirms CIK, fiscal year-end, and the authoritative filing chain for the annual package and trailing three quarters | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/sec-submissions.json) |
| HON-T3 | Honeywell 2025 annual report to shareowners | 2026-04-10 | Annual report PDF | Core annual narrative covering acceleration, separation, backlog, AI and automation framing, and 2025 results | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2025-annual-report-sec-ars.pdf) |
| HON-T4 | Honeywell 2025 Form 10-K | 2026-02-17 | SEC filing HTML | Standalone annual filing for the year ended `2025-12-31`, including segment realignment and capital-allocation framing | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2025-10k.html) |
| HON-T5 | Q4 2025 8-K | 2026-01-29 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2025-q4-8k.html) |
| HON-T6 | Q4 2025 earnings release | 2026-01-29 | IR earnings release PDF | Exact Q4 and full-year 2025 metrics, 2026 outlook, and accelerated spin timing | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2025-q4-earnings-release.pdf) |
| HON-T7 | Q1 2026 8-K | 2026-04-23 | SEC filing HTML | Wrapper filing for first-quarter 2026 earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2026-q1-8k.html) |
| HON-T8 | Q1 2026 earnings release exhibit | 2026-04-23 | SEC exhibit HTML | Exact Q1 2026 metrics, backlog, 2026 guidance reaffirmation, WWS sale announcement, and June 29 spin timing | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2026-q1-earnings-release-sec-ex99.html) |
| HON-T9 | Q1 2026 Form 10-Q | 2026-04-23 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31`, including segment realignment and held-for-sale disclosures | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2026-q1-10q.html) |
| HON-T10 | Segment-recast 8-K | 2026-04-23 | SEC filing HTML | Explicitly documents the new Process Automation and Technology segment and the recast comparative presentation ahead of the spin | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2026-q1-8k.html) |
| HON-T11 | Q2 2026 8-K | 2026-07-23 | SEC filing HTML | Wrapper filing for second-quarter 2026 results after the Aerospace spin-off | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2026-q2-8k.html) |
| HON-T12 | Q2 2026 earnings release exhibit | 2026-07-23 | SEC exhibit HTML | Exact Q2 2026 consolidated and post-spin Honeywell Technologies metrics, updated guidance, and Catalyst Technologies closing detail | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2026-q2-earnings-release-sec-ex99.html) |
| HON-T13 | Q2 2026 Form 10-Q | 2026-07-23 | SEC filing HTML | Filed quarterly report covering the completed Aerospace spin-off, reverse stock split, held-for-sale businesses, and Honeywell Technologies-only framing | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/aerospace-defense-products-services/honeywell-international-inc/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is useful for folder taxonomy and legacy sector tagging, but it is stale for Honeywell by `2026-08-08`. It still shows a `2024` annual package and legacy aerospace-defense classification while the current filings and investor materials reflect the completed Aerospace spin and the Honeywell Technologies automation identity.
- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- Q4 2025 is represented here by the IR earnings release PDF plus the annual filing chain. Q1 2026 and Q2 2026 are fully covered with SEC `8-K` wrappers, filed earnings-release exhibits, and `10-Q` filings.
- The local folder remains under the original AnnualReports industry path so the archive stays aligned with the initial collection taxonomy even though the business description changed materially after `2026-06-29`.

## Missing evidence

- No official latest-quarter earnings-call transcript was collected for `Q2 2026`.
- No transcript artifacts were collected for Q1 2026 or Q4 2025 during this pass.
