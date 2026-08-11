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
| MKL-T1 | AnnualReports verification note for Markel | 2026-08-10 | Aggregator verification note | Confirms `Property & Casualty Insurance` taxonomy and records the lagging `2024` archive state plus older `Markel Corporation` label | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/property-casualty-insurance/markel-group-inc/annualreports-verification.md) |
| MKL-T2 | SEC submissions JSON for Markel | 2026-08-10 | SEC index JSON | Confirms issuer identity, fiscal year-end, and the annual / trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/property-casualty-insurance/markel-group-inc/sec-submissions.json) |
| MKL-T3 | Markel IR source-links note | 2026-08-10 | Official-link verification note | Records official IR entry points and in-scope current-period result-page URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/property-casualty-insurance/markel-group-inc/ir-source-links.md) |
| MKL-T4 | Markel 2025 Form 10-K | 2026-02-20 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/property-casualty-insurance/markel-group-inc/2025-10k.html) |
| MKL-T5 | Markel Q4 2025 earnings 8-K | 2026-02-20 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/property-casualty-insurance/markel-group-inc/2025-q4-8k.html) |
| MKL-T6 | Markel Q1 2026 Form 10-Q | 2026-05-02 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/property-casualty-insurance/markel-group-inc/2026-q1-10q.html) |
| MKL-T7 | Markel Q1 2026 earnings 8-K | 2026-05-20 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/property-casualty-insurance/markel-group-inc/2026-q1-8k.html) |
| MKL-T8 | Markel Q2 2026 Form 10-Q | 2026-08-01 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/property-casualty-insurance/markel-group-inc/2026-q2-10q.html) |
| MKL-T9 | Markel Q2 2026 8-K follow-up filing | 2026-08-07 | SEC filing HTML | Saved local wrapper-style filing associated with second-quarter `2026` results | `[Filed]` | [2026-q2-8k-followup.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/property-casualty-insurance/markel-group-inc/2026-q2-8k-followup.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy confirmation only. As of `2026-08-10`, it still lagged at `2024` and used the older `Markel Corporation` label.
- The correct trailing-quarter set as of `2026-08-10` is `2Q26`, `1Q26`, and `4Q25`.
- The authoritative local evidence chain is SEC-first, with Markel IR result pages preserved as verified official links rather than as locally captured release PDFs.

## Missing evidence

- No local Markel IR HTML or PDF capture of the quarter result pages was preserved in this workspace.
- No local prepared remarks or full earnings-call transcript capture was collected for `4Q25`, `1Q26`, or `2Q26`.
