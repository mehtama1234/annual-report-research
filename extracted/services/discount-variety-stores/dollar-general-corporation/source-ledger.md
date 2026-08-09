# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| DG-T1 | AnnualReports.com Dollar General verification note | 2026-08-09 | Aggregator verification note | Confirms company identity, industry placement, and that AnnualReports still lagged at the `2024` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/discount-variety-stores/dollar-general-corporation/annualreports-verification.md) |
| DG-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the live annual-report and quarter-results URL chain even though direct scripted IR HTML capture was blocked | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/discount-variety-stores/dollar-general-corporation/official-ir-verification.md) |
| DG-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity and the `10-K`, `10-Q`, and `8-K` accession sequence | `[Filed]` | [submissions-cik0000029534.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/discount-variety-stores/dollar-general-corporation/submissions-cik0000029534.json) |
| DG-T4 | Form `10-K` for year ended `2026-01-30` | 2026-03-20 filed / 2026-08-09 collected | SEC filing HTML | Core annual filing for the `2025` reporting year in scope | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/discount-variety-stores/dollar-general-corporation/2025-10k.html) |
| DG-T5 | Q3 `2025` earnings `8-K` | 2025-12-04 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/discount-variety-stores/dollar-general-corporation/2025-q3-8k.html) |
| DG-T6 | Q3 `2025` Form `10-Q` | 2025-12-04 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/discount-variety-stores/dollar-general-corporation/2025-q3-10q.html) |
| DG-T7 | Q4 `2025` earnings `8-K` | 2026-03-12 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/discount-variety-stores/dollar-general-corporation/2025-q4-8k.html) |
| DG-T8 | Q1 `2026` earnings `8-K` | 2026-06-02 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/discount-variety-stores/dollar-general-corporation/2026-q1-8k.html) |
| DG-T9 | Q1 `2026` Form `10-Q` | 2026-06-02 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/discount-variety-stores/dollar-general-corporation/2026-q1-10q.html) |

## Reconciliation notes

- AnnualReports.com still lagged at `2024`, so the annual evidence had to be completed from Dollar General's official IR pages and SEC filings.
- Dollar General's live IR pages were readable in the browser tool but not directly collectible via scripted shell fetches in this environment on `2026-08-09`.
- The local archive therefore relies on browser-verified IR URLs plus the saved SEC filing chain instead of raw IR HTML snapshots.

## Missing evidence

- No standalone local annual-report PDF artifact is saved.
- No standalone local IR HTML snapshots of the annual-reports page or press-release pages are saved because scripted capture returned a placeholder shell in this environment.
- No standalone verbatim earnings-call transcript artifacts for the in-scope quarters are saved locally.
