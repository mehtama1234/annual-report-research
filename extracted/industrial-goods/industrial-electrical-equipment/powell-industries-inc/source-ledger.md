# Source Ledger

Date baseline: 2026-08-09

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
| POWL-T1 | AnnualReports.com Powell company page metadata | 2026-08-09 | Aggregator page | Confirms `Industrial Goods / Industrial Electrical Equipment` classification and that AnnualReports still appeared to lag at `2024` for the hosted annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/industrial-goods/industrial-electrical-equipment/powell-industries-inc/annualreports-verification.md) |
| POWL-T2 | Powell IR source links | 2026-08-09 | Official IR link note | Captures the annual-reports page, quarterly-results page, press-releases page, and in-scope quarterly release URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/industrial-goods/industrial-electrical-equipment/powell-industries-inc/ir-source-links.md) |
| POWL-T3 | Powell 2025 annual report | 2025-11-19 | Annual report PDF | Core shareholder-facing annual narrative for the fiscal year ended `2025-09-30` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2025-annual-report.pdf) |
| POWL-T4 | Powell 2025 Form 10-K | 2025-11-19 | SEC filing HTML | Formal business description, end-market framing, and annual financial detail | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2025-10k.html) |
| POWL-T5 | Q1 FY2026 8-K | 2026-02-03 | SEC filing HTML | Wrapper filing for first-quarter fiscal 2026 results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2026-q1-8k.html) |
| POWL-T6 | Q1 FY2026 earnings release exhibit | 2026-02-03 | SEC exhibit HTML | Exact Q1 FY2026 metrics, new-orders surge, backlog, and first data-center megaproject detail | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2026-q1-earnings-release-sec-ex99.html) |
| POWL-T7 | Q1 FY2026 Form 10-Q | 2026-02-03 | SEC filing HTML | Filed quarterly report for quarter ended `2025-12-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2026-q1-10q.html) |
| POWL-T8 | Q2 FY2026 8-K | 2026-05-04 | SEC filing HTML | Wrapper filing associated with second-quarter fiscal 2026 results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2026-q2-8k.html) |
| POWL-T9 | Q2 FY2026 Form 10-Q | 2026-05-04 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` and the cleanest saved local source for Q2 FY2026 numbers | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2026-q2-10q.html) |
| POWL-T10 | Q3 FY2026 8-K | 2026-08-03 | SEC filing HTML | Wrapper filing for third-quarter fiscal 2026 results | `[Filed]` | [2026-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2026-q3-8k.html) |
| POWL-T11 | Q3 FY2026 earnings release exhibit | 2026-08-03 | SEC exhibit HTML | Exact Q3 FY2026 metrics, record orders, record backlog, and end-market detail spanning data centers, LNG, and petrochemical demand | `[Filed]` | [2026-q3-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2026-q3-earnings-release-sec-ex99.html) |
| POWL-T12 | Q3 FY2026 Form 10-Q | 2026-08-03 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/2026-q3-10q.html) |
| POWL-T13 | SEC submissions JSON | 2026-08-09 | SEC metadata | Confirms CIK `0000080420`, fiscal year-end `0930`, and the in-scope filing chain | `[Filed]` | [submissions-cik0000080420.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/powell-industries-inc/submissions-cik0000080420.json) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-09` is `Q3 FY2026`, `Q2 FY2026`, and `Q1 FY2026` because Powell's fiscal year ends in September.
- AnnualReports is used here for sector and industry taxonomy, but as of `2026-08-09` it still appeared to lag at `2024` for the hosted annual package.
- The local SEC evidence chain is complete for the `2025` annual filing and the `Q1` through `Q3 FY2026` filing set.
- The Q2 FY2026 quarter packet relies on the saved `10-Q` plus the official IR release URL note because the standalone HTML release capture was not saved locally in this pass.

## Missing evidence

- No official earnings-call transcript artifact was collected for Q1 FY2026, Q2 FY2026, or Q3 FY2026.
- No standalone local Q2 FY2026 earnings-release exhibit HTML artifact is saved beyond the wrapper filing, the filed `10-Q`, and the official IR release URL note.
