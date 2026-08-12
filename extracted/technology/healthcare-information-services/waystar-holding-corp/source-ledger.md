# Source Ledger

Date baseline: 2026-08-12

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
| WAY-T1 | Waystar investor-relations overview | 2026-08-12 | Official IR page | Confirms company identity, mission, and IR hub | `[Disclosed]` | [investor-relations-overview.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/healthcare-information-services/waystar-holding-corp/investor-relations-overview.html) |
| WAY-T2 | Waystar SEC filings page | 2026-08-12 | Official IR page | Confirms the official annual and quarterly filing chain | `[Disclosed]` | [sec-filings-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/healthcare-information-services/waystar-holding-corp/sec-filings-page.html) |
| WAY-T3 | Waystar `2025` Form 10-K | 2026-02-17 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/healthcare-information-services/waystar-holding-corp/2025-10k.html) |
| WAY-T4 | Waystar `Q4 2025` official results page | 2026-08-12 | Official IR page | Confirms official fourth-quarter and full-year `2025` results | `[Disclosed]` | [2025-q4-results-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/healthcare-information-services/waystar-holding-corp/2025-q4-results-page.html) |
| WAY-T5 | Waystar `Q4 2025` 8-K | 2026-02-17 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/healthcare-information-services/waystar-holding-corp/2025-q4-8k.html) |
| WAY-T6 | Waystar `Q1 2026` official results page | 2026-08-12 | Official IR page | Confirms official first-quarter `2026` results | `[Disclosed]` | [2026-q1-results-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/healthcare-information-services/waystar-holding-corp/2026-q1-results-page.html) |
| WAY-T7 | Waystar `Q1 2026` 8-K | 2026-04-29 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/healthcare-information-services/waystar-holding-corp/2026-q1-8k.html) |
| WAY-T8 | Waystar `Q1 2026` 10-Q | 2026-04-29 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/healthcare-information-services/waystar-holding-corp/2026-q1-10q.html) |
| WAY-T9 | Waystar `Q2 2026` official results page | 2026-08-12 | Official IR page | Confirms official second-quarter `2026` results | `[Disclosed]` | [2026-q2-results-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/healthcare-information-services/waystar-holding-corp/2026-q2-results-page.html) |
| WAY-T10 | Waystar `Q2 2026` 8-K | 2026-07-29 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/healthcare-information-services/waystar-holding-corp/2026-q2-8k.html) |
| WAY-T11 | Waystar `Q2 2026` 10-Q | 2026-07-29 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/healthcare-information-services/waystar-holding-corp/2026-q2-10q.html) |

## Reconciliation notes

- No usable AnnualReports company page surfaced during the `2026-08-12` check, so taxonomy and authority were taken from the company's official description and SEC chain instead.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - company IR and SEC for the authoritative annual and quarter chain
  - no usable AnnualReports company page was available to serve as taxonomy confirmation
- The verified chain is strong on official URLs and SEC filings:
  - official investor-relations and filings pages
  - official results pages for `Q4 2025`, `Q1 2026`, and `Q2 2026`
  - SEC annual filing, `8-K` wrappers, and both in-scope `10-Q` filings
- The packet is now `proven` because this workspace preserves a rebuilt local raw-artifact chain spanning the official IR hub, in-scope results pages, and the SEC annual-plus-quarter filing set.

## Missing evidence

- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
