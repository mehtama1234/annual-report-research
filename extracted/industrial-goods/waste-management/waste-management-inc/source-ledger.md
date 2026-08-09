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
| WM-T1 | AnnualReports.com Waste Management company page | 2026-08-08 | Aggregator page | Confirms Industrial Goods / Waste Management classification and shows that AnnualReports still lags at the `2024` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/industrial-goods/waste-management/waste-management-inc/company-page-annualreports.html) |
| WM-T2 | SEC submissions JSON for Waste Management | 2026-08-08 | SEC index JSON | Confirms CIK, fiscal year-end, and the filing chain for the annual package plus the trailing three quarters | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/sec-submissions.json) |
| WM-T3 | Waste Management 2025 annual report to shareholders | 2026-03-31 | Annual report PDF | Core annual narrative package for the year ended `2025-12-31` | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/waste-management/waste-management-inc/2025-annual-report-sec-ars.pdf) |
| WM-T4 | Waste Management 2025 Form 10-K | 2026-02-09 | SEC filing HTML | Standalone annual filing covering business mix, Stericycle / Healthcare Solutions integration, risks, and segment framing | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2025-10k.html) |
| WM-T5 | Q4 2025 8-K | 2026-01-28 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2025-q4-8k.html) |
| WM-T6 | Q4 2025 earnings release exhibit | 2026-01-28 | SEC exhibit HTML | Exact Q4 and full-year `2025` metrics, `2026` outlook bridge, and sustainability / Healthcare Solutions update | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2025-q4-earnings-release-sec-ex99.html) |
| WM-T7 | Q1 2026 8-K | 2026-04-28 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2026-q1-8k.html) |
| WM-T8 | Q1 2026 earnings release exhibit | 2026-04-28 | SEC exhibit HTML | Exact Q1 `2026` metrics, free-cash-flow jump, weather and volume commentary, and outlook reaffirmation | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2026-q1-earnings-release-sec-ex99.html) |
| WM-T9 | Q1 2026 Form 10-Q | 2026-04-29 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2026-q1-10q.html) |
| WM-T10 | Q2 2026 8-K | 2026-07-28 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2026-q2-8k.html) |
| WM-T11 | Q2 2026 earnings release exhibit | 2026-07-28 | SEC exhibit HTML | Exact Q2 `2026` metrics, updated `2026` outlook, and margin / project / integration commentary | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2026-q2-earnings-release-sec-ex99.html) |
| WM-T12 | Q2 2026 Form 10-Q | 2026-07-29 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/waste-management/waste-management-inc/2026-q2-10q.html) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports remains useful for classification and archive context, but not for the current annual package. As of `2026-08-08`, its WM page still points to the `2024` annual report and `2024` Form `10-K`.
- The `2025` annual package is therefore anchored to SEC-hosted artifacts: the `10-K` filed on `2026-02-09` and the annual report to shareholders filed on `2026-03-31`.
- The industrial placement matters. WM had partial materials under a Services path earlier, but AnnualReports explicitly classifies the company as `Industrial Goods / Waste Management`, so the active archive should remain under the industrial-goods tree.

## Missing evidence

- No official earnings-call transcript artifacts were collected for Q4 `2025`, Q1 `2026`, or Q2 `2026` in the current workspace.
