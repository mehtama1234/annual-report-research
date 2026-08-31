# Source Ledger

Date baseline: 2026-08-30

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| MCD-T1 | Existing company packet | 2026-08-09 | Extracted packet | Summarizes annual and quarter takeaways used as the starting point for the first-principles pass | `[Reported]` | [company-packet.md](company-packet.md) |
| MCD-T2 | SEC submissions index | 2026-08-30 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence, including the `ARS` annual-report artifact | `[Filed]` | [submissions-cik0000063908.json](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/submissions-cik0000063908.json) |
| MCD-T3 | SEC company facts | 2026-08-30 collected | SEC companyfacts JSON | Provides machine-readable revenue, net income, EPS, operating cash flow, capex, dividends, and buybacks used in the investment read | `[Filed]` | [companyfacts-cik0000063908.json](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/companyfacts-cik0000063908.json) |
| MCD-T4 | Annual Report to Security Holders (`ARS`) | 2026-04-07 filed / 2026-08-30 collected | SEC-hosted annual report PDF | Official annual-report artifact for the target `2025` reporting year | `[Filed]` | [2025-annual-report.pdf](/home/mehtama1/git-repo/annual-report-research/raw/company-ir/services/restaurants/mcdonalds-corporation/2025-annual-report.pdf) |
| MCD-T5 | 2025 Form `10-K` | 2026-02-24 filed / 2026-08-30 collected | SEC filing HTML | Annual filing for year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2025-10k.html) |
| MCD-T6 | 2025 Q4 earnings `8-K` | 2026-02-11 filed / 2026-08-30 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2025-q4-8k.html) |
| MCD-T7 | 2025 Q4 earnings release exhibit | 2026-02-11 filed / 2026-08-30 collected | SEC exhibit HTML | Actual fourth-quarter and full-year `2025` investor release text | `[Filed]` | [2025-q4-exhibit991.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2025-q4-exhibit991.html) |
| MCD-T8 | 2026 Q1 earnings `8-K` | 2026-05-07 filed / 2026-08-30 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q1-8k.html) |
| MCD-T9 | 2026 Q1 earnings release exhibit | 2026-05-07 filed / 2026-08-30 collected | SEC exhibit HTML | Actual first-quarter `2026` investor release text | `[Filed]` | [2026-q1-exhibit991.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q1-exhibit991.html) |
| MCD-T10 | 2026 Q2 earnings `8-K` | 2026-08-04 filed / 2026-08-30 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q2-8k.html) |
| MCD-T11 | 2026 Q2 earnings release exhibit | 2026-08-04 filed / 2026-08-30 collected | SEC exhibit HTML | Actual second-quarter `2026` investor release text | `[Filed]` | [2026-q2-exhibit991.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q2-exhibit991.html) |
| MCD-T12 | 2026 Q1 Form `10-Q` | 2026-05-07 filed / 2026-08-30 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q1-10q.html) |
| MCD-T13 | 2026 Q2 Form `10-Q` | 2026-08-07 filed / 2026-08-30 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q2-10q.html) |
| MCD-T14 | McDonald's Digitizing the Arches corporate update | 2025-08-14 published / 2026-08-30 referenced | Corporate technology update | Supports loyalty visit lift, Ready on Arrival, and restaurant technology analysis | `[Disclosed]` | https://corporate.mcdonalds.com/corpmcd/our-stories/article/digitizing-the-arches.html |
| MCD-T15 | McDonald's and Google Cloud partnership update | 2023-12-06 published / 2026-08-30 referenced | Corporate technology update | Supports edge computing, restaurant-local compute, and digital platform analysis | `[Disclosed]` | https://corporate.mcdonalds.com/corpmcd/our-stories/article/mcd-google-cloud-announce-partnership.html |
| MCD-T16 | McDonald's McValue platform update | 2025-01-07 published / 2026-08-30 referenced | Corporate value-platform update | Supports `$5 Meal Deal`, Buy One Add One for `$1`, app offers, and local franchisee deal analysis | `[Disclosed]` | https://corporate.mcdonalds.com/corpmcd/our-stories/article/mcdonalds-launching-mcvalue-platform-inus-restaurants-in2025.html |
| MCD-T17 | National Restaurant News `$5 Meal Deal` operator-check coverage | 2024-07-26 published / 2026-08-30 referenced | Trade press | Supports operator-check detail on more than 200 units per day, double projection, 20%-25% transaction mix, and coupon-stack margin pressure | `[Reported]` | https://www.nrn.com/quick-service/mcdonald-s-franchisees-divided-on-5-meal-deal |
| MCD-T18 | Sherwood Grinch campaign and sock-event coverage | 2026-02-11 published / 2026-08-30 collected | Business press HTML | Supports cultural-drop analysis: biggest reported sales day and about `50M` sock pairs sold globally | `[Reported]` | [2026-grinch-socks-sherwood.html](/home/mehtama1/git-repo/annual-report-research/raw/company-ir/services/restaurants/mcdonalds-corporation/2026-grinch-socks-sherwood.html) |

## Reconciliation notes

- McDonald's now has the core SEC chain on disk for the `2025` annual filing and the last three quarters in scope.
- The annual-report artifact is on disk through the SEC-hosted `ARS` filing.
- Q4 `2025`, Q1 `2026`, and Q2 `2026` investor-release exhibit HTML files are now on disk.
- SEC companyfacts are now on disk and support the first investment-read metrics.
- External corporate and trade sources now support the deeper mechanisms around loyalty visit frequency, `$5 Meal Deal` economics, restaurant edge computing, Ready on Arrival, and the Grinch sock campaign.

## Missing evidence

- A locally saved copy of the official McDonald's `Q2 2026` earnings-release PDF from the corporate host.
- Saved HTML mirrors of the McDonald's financial-information and quarter story pages if the corporate host becomes more cooperative in a later pass.
- Standalone earnings-call transcripts for the covered quarters.
- Direct cohort-level proof that loyalty membership caused higher visit frequency rather than mostly selecting customers who were already frequent.
- Franchisee-level economics after `$5 Meal Deal`, coupon stacking, remodel costs, and restaurant technology investment.
