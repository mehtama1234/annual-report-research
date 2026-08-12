# Source Ledger

Date baseline: `2026-08-12`

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
| PRU-T1 | AnnualReports.com Prudential company page | 2026-08-12 | Aggregator page | Confirms Financial / Life Insurance taxonomy and shows that the hosted annual package still lagged at `2024` | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/life-insurance/prudential-financial-inc/company-page.html) |
| PRU-T2 | Prudential official IR verification | 2026-08-12 | Official IR verification note | Confirms the annual-report and quarterly-results routing plus issuer results-page coverage | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/life-insurance/prudential-financial-inc/official-ir-verification.md) |
| PRU-T3 | Prudential `2025` Form 10-K | 2026-02-12 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2025-10k.html) |
| PRU-T4 | Prudential `Q4 2025` earnings release exhibit | 2026-02-03 | SEC exhibit HTML | Exact fourth-quarter and full-year `2025` metrics and capital-return framing | `[Filed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2025-q4-press-release.html) |
| PRU-T5 | Prudential `Q4 2025` 8-K | 2026-02-03 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2025-q4-8k.html) |
| PRU-T6 | Prudential `Q1 2026` earnings release exhibit | 2026-05-05 | SEC exhibit HTML | Exact first-quarter `2026` metrics and segment-level operating results | `[Filed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2026-q1-press-release.html) |
| PRU-T7 | Prudential `Q1 2026` 8-K | 2026-05-05 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2026-q1-8k.html) |
| PRU-T8 | Prudential `Q1 2026` 10-Q | 2026-05-06 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2026-q1-10q.html) |
| PRU-T9 | Prudential `Q2 2026` preliminary update | 2026-07-15 | SEC filing HTML | Shows estimated assumption-update impacts ahead of the full quarter closeout | `[Filed]` | [2026-q2-preliminary-update-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2026-q2-preliminary-update-8k.html) |
| PRU-T10 | Prudential `Q2 2026` earnings release exhibit | 2026-08-04 | SEC exhibit HTML | Exact second-quarter `2026` earnings and segment-level operating results | `[Filed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2026-q2-press-release.html) |
| PRU-T11 | Prudential `Q2 2026` 8-K | 2026-08-04 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2026-q2-8k.html) |
| PRU-T12 | Prudential `Q2 2026` quarterly financial supplement | 2026-08-04 | SEC exhibit HTML | Adds segment and capital detail for the second quarter `2026` results set | `[Filed]` | [2026-q2-financial-supplement.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2026-q2-financial-supplement.html) |
| PRU-T13 | Prudential `Q2 2026` 10-Q | 2026-08-05 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/prudential-financial-inc/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation only. As of `2026-08-12`, the hosted annual package still lagged at `2024`.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is now strong enough for local inspection:
  - AnnualReports company page
  - official IR verification note covering the annual-report and quarterly-results routing
  - SEC annual filing
  - SEC quarter-release exhibits, `8-K` wrappers, the `Q2 2026` financial supplement, the `Q2 2026` preliminary update filing, and both in-scope `10-Q` filings
- The remaining limitation is narrow:
  - direct shell retrieval attempts to Prudential investor pages were rate-limited or otherwise did not yield clean local HTML artifacts
  - the official routing and page-level confirmations are preserved in the IR verification note instead
- The packet is now `proven` because this workspace preserves a rebuilt local annual-plus-quarter evidence chain with direct SEC artifacts and a saved official-IR routing record.

## Missing evidence

- No local transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
