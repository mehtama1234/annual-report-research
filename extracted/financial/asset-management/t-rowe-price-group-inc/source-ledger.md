# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| TROW-T1 | AnnualReports.com T. Rowe Price verification note | 2026-08-09 | Aggregator verification note | Records company metadata and the still-lagged latest annual-report label from AnnualReports | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/financial/asset-management/t-rowe-price-group-inc/annualreports-verification.md) |
| TROW-T2 | T. Rowe Price IR source-links note | 2026-08-09 | Official-source link ledger | Preserves the verified official annual and quarterly IR asset URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/asset-management/t-rowe-price-group-inc/ir-source-links.md) |
| TROW-T3 | T. Rowe Price 2025 Form 10-K | 2026-02-13 filed / 2026-08-08 collected | SEC filing HTML | Filed annual report for `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/t-rowe-price-group-inc/2025-10k.html) |
| TROW-T4 | T. Rowe Price 4Q25 earnings 8-K | 2026-02-04 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for late-2025 earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/t-rowe-price-group-inc/2025-q4-8k.html) |
| TROW-T5 | T. Rowe Price 1Q26 Form 10-Q | 2026-04-30 filed / 2026-08-08 collected | SEC filing HTML | Filed prior quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/t-rowe-price-group-inc/2026-q1-10q.html) |
| TROW-T6 | T. Rowe Price 1Q26 earnings 8-K | 2026-04-30 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for prior quarter release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/t-rowe-price-group-inc/2026-q1-8k.html) |
| TROW-T7 | T. Rowe Price 2Q26 earnings release PDF | 2026-07-31 | Earnings release PDF | Most recent quarter financial release saved locally | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/asset-management/t-rowe-price-group-inc/2026-q2-earnings-release.pdf) |
| TROW-T8 | T. Rowe Price 2Q26 Form 10-Q | 2026-07-31 filed / 2026-08-08 collected | SEC filing HTML | Filed most recent quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/t-rowe-price-group-inc/2026-q2-10q.html) |
| TROW-T9 | T. Rowe Price 2Q26 earnings 8-K | 2026-07-31 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for most recent quarter release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/t-rowe-price-group-inc/2026-q2-8k.html) |

## Reconciliation notes

- T. Rowe Price now has a clean SEC filing chain on disk for the target annual report and the last three quarters.
- AnnualReports still lagged at `2024` on `2026-08-09`, so the official T. Rowe Price IR annual-reports page is the source of truth for the current `2025` annual-report URL.
- The official IR annual-report and transcript URLs were verified and logged, but several `static-files` binary assets did not download cleanly through local machine fetches during this pass.
- Follow-up IPv4-only fetch tests on `2026-08-09` still failed after connection establishment: `wget --spider` timed out waiting for response headers and `curl -I --http1.1` hung without headers or payload.
- An earlier local Playwright / Chromium browser pass on `2026-08-09` hit `403 Access Denied` on both the annual-reports page and the direct annual-report asset URL, and a later fully working local Playwright Chromium runtime still did not produce a usable download event or PDF binary from the direct static-file URL. Together those checks confirm the remaining gap is a machine-local delivery failure rather than a missing source URL. See [browser-runtime-annual-report-attempt-2026-08-09.md](/home/manishmehta/ui-projects/annual-report-research/notes/browser-runtime-annual-report-attempt-2026-08-09.md).
- The one directly saved IR binary artifact in this pass is the `2Q26` earnings release PDF.

## Missing evidence

- A direct saved AnnualReports.com HTML artifact if shell access to `annualreports.com` becomes reliable later.
- A local copy of the official `2025` annual report PDF.
- Local copies of the official `4Q25` and `1Q26` earnings release, supplement, and transcript PDFs.
- Local copies of the official `2Q26` supplement and transcript PDFs.
