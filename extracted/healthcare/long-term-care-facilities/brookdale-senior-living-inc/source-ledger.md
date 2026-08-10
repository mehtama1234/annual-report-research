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
| BKD-T1 | AnnualReports.com Brookdale metadata verification | 2026-08-09 | Aggregator page | Confirms `Healthcare` / `Long-Term Care Facilities` classification and that the `2025` annual package is current on AnnualReports | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/healthcare/long-term-care-facilities/brookdale-senior-living-inc/annualreports-verification.md) |
| BKD-T2 | Official Brookdale IR verification | 2026-08-09 | IR verification note | Confirms the official IR chain and the crucial as-of-date nuance that Q2 `2026` is not yet reported on `2026-08-09` | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/long-term-care-facilities/brookdale-senior-living-inc/official-ir-verification.md) |
| BKD-T3 | SEC submissions JSON for Brookdale | 2026-08-09 | SEC index JSON | Confirms CIK, ticker, exchange, December fiscal year-end, and the authoritative annual plus trailing-quarter filing chain | `[Filed]` | [submissions-cik0001332349.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/long-term-care-facilities/brookdale-senior-living-inc/submissions-cik0001332349.json) |
| BKD-T4 | Brookdale 2025 annual report to shareholders / ARS | 2026-04-30 | Annual report PDF | Core annual narrative package for the year ended `2025-12-31`, including occupancy, RevPAR, adjusted EBITDA, and strategic framing | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2025-annual-report-sec-ars.pdf) |
| BKD-T5 | Brookdale 2025 Form 10-K | 2026-02-19 | SEC filing HTML | Filed annual package covering senior-living operations, segment mix, and risk factors | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2025-10k.html) |
| BKD-T6 | Q4 2025 8-K | 2026-02-18 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2025-q4-8k.html) |
| BKD-T7 | Q3 2025 8-K | 2025-11-06 | SEC filing HTML | Wrapper filing for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2025-q3-8k.html) |
| BKD-T8 | Q3 2025 10-Q | 2025-11-07 | SEC filing HTML | Filed quarterly report for the quarter ended `2025-09-30` | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2025-q3-10q.html) |
| BKD-T9 | Q1 2026 earnings release | 2026-05-06 | Official IR PDF | Exact first-quarter `2026` occupancy, RevPAR, operating income, and adjusted EBITDA results | `[Disclosed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2026-q1-earnings-release.pdf) |
| BKD-T10 | Q1 2026 financial supplemental | 2026-05-06 | Official IR PDF | Adds resident-fee, same-community, and balance-sheet detail beyond the release headline | `[Disclosed]` | [2026-q1-financial-supplemental.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2026-q1-financial-supplemental.pdf) |
| BKD-T11 | Q1 2026 investor presentation | 2026-05-06 | Official IR PDF | Management framing for the current quarter and occupancy / margin trajectory | `[Disclosed]` | [2026-q1-investor-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2026-q1-investor-presentation.pdf) |
| BKD-T12 | Q1 2026 company-hosted 10-Q PDF | 2026-05-06 | Official IR PDF | Company-hosted filing artifact confirming the same quarter chain visible on IR | `[Disclosed]` | [2026-q1-10q-company-hosted.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2026-q1-10q-company-hosted.pdf) |
| BKD-T13 | Q1 2026 10-Q | 2026-05-07 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/long-term-care-facilities/brookdale-senior-living-inc/2026-q1-10q.html) |

## Reconciliation notes

- Brookdale is a clean example of an off-cycle trailing-quarter window. As of `2026-08-09`, the latest reported quarter is still `Q1 2026` because Q2 `2026` results are scheduled for `2026-08-10` after market close.
- The correct Brookdale quarter set for this packet is therefore `Q1 2026`, `Q4 2025`, and `Q3 2025`.
- The annual chain is strong because both AnnualReports metadata and the SEC annual report plus `10-K` support the `2025` annual package.

## Missing evidence

- No official transcript artifact was collected for Q1 `2026`, Q4 `2025`, or Q3 `2025`.
- No company-hosted Q4 `2025` or Q3 `2025` quarter PDFs were collected locally; the packet relies on the SEC filing chain for those quarters.
