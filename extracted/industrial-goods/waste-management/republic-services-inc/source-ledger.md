# Source Ledger

Date baseline: 2026-08-10

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
| RSG-T1 | AnnualReports company page | 2026-08-10 | Aggregator page | Confirms `Industrial Goods / Waste Management` classification and proves the aggregator still lagged at `2024 Form 10K, 2023 Annual Report` | `[Reported]` | [company-page.html](/raw/annualreports/industrial-goods/waste-management/republic-services-inc/company-page.html) |
| RSG-T2 | AnnualReports search results page | 2026-08-10 | Aggregator page | Confirms the current company slug mapping to `/Company/republic-services-inc` | `[Reported]` | [search-page.html](/raw/annualreports/industrial-goods/waste-management/republic-services-inc/search-page.html) |
| RSG-T3 | Republic investor overview page | 2026-08-10 | Investor relations page | Confirms the official IR annual-report link and the corporate scale profile with `13 million` customers, `17,000` trucks, and more than `1,000` locations | `[Disclosed]` | [overview.html](/raw/company-ir/industrial-goods/waste-management/republic-services-inc/overview.html) |
| RSG-T4 | Republic 2025 annual report PDF | 2026-03-24 | Annual report PDF | Official annual-report package saved locally from the IR chain | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/industrial-goods/waste-management/republic-services-inc/2025-annual-report.pdf) |
| RSG-T5 | SEC submissions JSON for Republic | 2026-08-10 | SEC index JSON | Confirms CIK, fiscal year-end, and the accession chain for the annual and trailing-quarter materials | `[Filed]` | [sec-submissions.json](/raw/sec/industrial-goods/waste-management/republic-services-inc/sec-submissions.json) |
| RSG-T6 | Republic 2025 Form 10-K | 2026-02-18 | SEC filing HTML | Core annual SEC filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2025-10k.html) |
| RSG-T7 | Q4 2025 earnings 8-K | 2026-02-17 | SEC filing HTML | Filing wrapper proving the Q4 and full-year `2025` earnings release | `[Filed]` | [2025-q4-8k.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2025-q4-8k.html) |
| RSG-T8 | Q4 2025 and full-year 2025 earnings release exhibit | 2026-02-17 | SEC exhibit HTML | Exact Q4 and full-year `2025` metrics plus initial `2026` guidance and route-density operating commentary | `[Filed]` | [2025-q4-earnings-release.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2025-q4-earnings-release.html) |
| RSG-T9 | Q1 2026 earnings 8-K | 2026-05-07 | SEC filing HTML | Filing wrapper proving the Q1 `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2026-q1-8k.html) |
| RSG-T10 | Q1 2026 earnings release exhibit | 2026-05-07 | SEC exhibit HTML | Exact Q1 `2026` metrics, margin expansion, acquisition spend, and cash-flow detail | `[Filed]` | [2026-q1-earnings-release.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2026-q1-earnings-release.html) |
| RSG-T11 | Republic Q1 2026 Form 10-Q | 2026-05-08 | SEC filing HTML | Filed quarterly report for the period ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2026-q1-10q.html) |
| RSG-T12 | Q2 2026 earnings 8-K | 2026-08-06 | SEC filing HTML | Filing wrapper proving the Q2 `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2026-q2-8k.html) |
| RSG-T13 | Q2 2026 earnings release exhibit | 2026-08-06 | SEC exhibit HTML | Exact Q2 `2026` metrics, raised full-year guidance, and route-density pricing commentary | `[Filed]` | [2026-q2-earnings-release.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2026-q2-earnings-release.html) |
| RSG-T14 | Republic Q2 2026 Form 10-Q | 2026-08-07 | SEC filing HTML | Filed quarterly report for the period ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/raw/sec/industrial-goods/waste-management/republic-services-inc/2026-q2-10q.html) |

## Reconciliation notes

- The correct trailing-quarter set as of Monday, `2026-08-10`, is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports remains useful for taxonomy confirmation and lag verification, but not for current annual coverage. As of `2026-08-10`, its Republic page still pointed to `2024 Form 10K, 2023 Annual Report`.
- The authoritative annual evidence therefore comes from the official Republic IR page and PDF plus the SEC `10-K` and filing chain.
- The industrial placement matters. Republic belongs under `Industrial Goods / Waste Management`, which keeps it directly comparable with `Waste Management` and `Clean Harbors` inside the behind-the-shelf lane.

## Missing evidence

- No standalone earnings-call transcript artifacts were saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
