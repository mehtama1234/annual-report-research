# Source Ledger

Date baseline: 2026-08-08

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CG-T1 | AnnualReports.com Carlyle verification note | 2026-08-08 | Aggregator verification note | Records AnnualReports metadata and confirms the site still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/asset-management/the-carlyle-group-inc/annualreports-verification.md) |
| CG-T2 | Carlyle IR source-links note | 2026-08-08 | Official-source link ledger | Preserves verified annual and quarterly issuer and SEC asset URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/the-carlyle-group-inc/ir-source-links.md) |
| CG-T3 | Carlyle 2025 annual report PDF | 2026-04-23 filed / 2026-08-08 collected | Annual report PDF | Saved official annual report package for `2025` via ARS filing | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/the-carlyle-group-inc/2025-annual-report.pdf) |
| CG-T4 | Carlyle 2025 Form 10-K | 2026-02-27 filed / 2026-08-08 collected | SEC filing HTML | Filed annual report for `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/the-carlyle-group-inc/2025-10k.html) |
| CG-T5 | Carlyle 4Q25 earnings 8-K | 2026-02-26 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for `4Q25` and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/the-carlyle-group-inc/2025-q4-8k.html) |
| CG-T6 | Carlyle 1Q26 Form 10-Q | 2026-05-08 filed / 2026-08-08 collected | SEC filing HTML | Filed prior-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/the-carlyle-group-inc/2026-q1-10q.html) |
| CG-T7 | Carlyle 1Q26 earnings 8-K | 2026-05-07 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for `1Q26` release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/the-carlyle-group-inc/2026-q1-8k.html) |
| CG-T8 | Carlyle 2Q26 earnings 8-K | 2026-08-05 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for `2Q26` release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/the-carlyle-group-inc/2026-q2-8k.html) |

## Reconciliation notes

- Carlyle now has the `2025` annual report PDF plus the `2025` Form `10-K` and the in-scope `4Q25`, `1Q26`, and `2Q26` SEC filing chain on disk.
- Carlyle's rendered IR quarterly-results page verified on `2026-08-08` exposed direct release, supplement, and transcript entries for `4Q25` and `1Q26`, and a direct release plus supplement entry for `2Q26` with no transcript link visible.
- The verified direct IR static-file URLs are preserved in the source-links note even where local command-line download stalled from this environment.

## Missing evidence

- Local copies of Carlyle's verified IR-side release, supplement, and transcript PDFs if a later fetch pass succeeds from this environment.
- A saved `2Q26` transcript artifact if Carlyle posts one later.
