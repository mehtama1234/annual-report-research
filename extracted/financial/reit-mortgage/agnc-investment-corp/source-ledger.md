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
| AGNC-T1 | AnnualReports.com AGNC company page | 2026-08-12 | Aggregator page | Confirms `REIT - Mortgage Real Estate` taxonomy | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/reit-mortgage/agnc-investment-corp/company-page.html) |
| AGNC-T2 | AGNC official IR verification | 2026-08-12 | Official IR verification note | Confirms the issuer overview and quarterly-results routing for the annual anchor and in-scope quarter chain | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/reit-mortgage/agnc-investment-corp/official-ir-verification.md) |
| AGNC-T3 | AGNC `2025` annual report PDF | 2026-03-06 | Annual report PDF | Annual report package for the year ended `2025-12-31` | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2025-annual-report.pdf) |
| AGNC-T4 | AGNC `2025` Form 10-K | 2026-02-23 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2025-10k.html) |
| AGNC-T5 | AGNC `Q4 2025` earnings release exhibit | 2026-01-26 | SEC exhibit HTML | Exact fourth-quarter and full-year `2025` shareholder-return and spread metrics | `[Filed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2025-q4-press-release.html) |
| AGNC-T6 | AGNC `Q4 2025` 8-K | 2026-01-26 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2025-q4-8k.html) |
| AGNC-T7 | AGNC `Q1 2026` earnings release exhibit | 2026-04-20 | SEC exhibit HTML | Exact first-quarter `2026` book-value, spread-income, and leverage metrics | `[Filed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2026-q1-press-release.html) |
| AGNC-T8 | AGNC `Q1 2026` 8-K | 2026-04-20 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2026-q1-8k.html) |
| AGNC-T9 | AGNC `Q1 2026` 10-Q | 2026-05-04 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2026-q1-10q.html) |
| AGNC-T10 | AGNC `Q2 2026` earnings release exhibit | 2026-07-20 | SEC exhibit HTML | Exact second-quarter `2026` book-value recovery, economic-return, and spread metrics | `[Filed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2026-q2-press-release.html) |
| AGNC-T11 | AGNC `Q2 2026` 8-K | 2026-07-20 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2026-q2-8k.html) |
| AGNC-T12 | AGNC `Q2 2026` 10-Q | 2026-07-31 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/reit-mortgage/agnc-investment-corp/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is now strong enough for local inspection:
  - AnnualReports company page
  - official IR verification note covering the issuer overview and quarterly-results routing
  - annual report PDF and SEC annual filing
  - SEC quarter-release exhibits, `8-K` wrappers, and both in-scope `10-Q` filings
- The remaining limitation is narrow:
  - direct shell retrieval of issuer-hosted IR pages did not yield clean local HTML artifacts in this workspace
  - the official routing and page-level confirmations are preserved in the IR verification note instead
- The packet is now `proven` because this workspace preserves a rebuilt local annual-plus-quarter evidence chain with direct SEC artifacts and a saved official-IR routing record.

## Missing evidence

- No clean local copies of official quarterly presentations or transcript artifacts were rebuilt into this workspace.
- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
