# Source Ledger

Date baseline: 2026-08-08

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| SPGI-T1 | AnnualReports.com S&P Global verification note | 2026-08-08 | Aggregator verification note | Records company metadata and the lagging AnnualReports annual-report label | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/investment-brokerage-national/sp-global-inc/annualreports-verification.md) |
| SPGI-T2 | S&P Global IR source-links note | 2026-08-08 | Official-source link ledger | Preserves verified official annual and quarterly IR URLs plus official overview metrics | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/investment-brokerage-national/sp-global-inc/ir-source-links.md) |
| SPGI-T3 | S&P Global 2025 Form 10-K | 2026-02-11 filed / 2026-08-08 collected | SEC filing HTML | Filed annual report for `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/investment-brokerage-national/sp-global-inc/2025-10k.html) |
| SPGI-T4 | S&P Global 4Q25 earnings 8-K | 2026-02-10 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for late-2025 earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/investment-brokerage-national/sp-global-inc/2025-q4-8k.html) |
| SPGI-T5 | S&P Global 1Q26 Form 10-Q | 2026-04-28 filed / 2026-08-08 collected | SEC filing HTML | Filed prior quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/investment-brokerage-national/sp-global-inc/2026-q1-10q.html) |
| SPGI-T6 | S&P Global 1Q26 earnings 8-K | 2026-04-28 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for prior quarter release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/investment-brokerage-national/sp-global-inc/2026-q1-8k.html) |
| SPGI-T7 | S&P Global 2Q26 Form 10-Q | 2026-07-28 filed / 2026-08-08 collected | SEC filing HTML | Filed most recent quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/investment-brokerage-national/sp-global-inc/2026-q2-10q.html) |
| SPGI-T8 | S&P Global 2Q26 earnings 8-K | 2026-07-28 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for most recent quarter release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/investment-brokerage-national/sp-global-inc/2026-q2-8k.html) |
| SPGI-T9 | S&P Global 2025 annual report PDF | 2026-08-08 collected | Official annual report PDF | Official designed annual-report package saved locally | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/investment-brokerage-national/sp-global-inc/2025-annual-report.pdf) |

## Reconciliation notes

- S&P Global now has a full SEC filing chain on disk for the target annual report and the last three quarters.
- The official `2025` annual report PDF is now saved locally.
- Official S&P Global IR release pages and overview pages were verified on the web, but direct shell fetches to those pages and to guessed static-file URLs ran into Cloudflare challenge pages.
- The locally saved placeholder HTML and PDF files from those blocked fetches are not treated as evidence in the extracted summaries.

## Missing evidence

- A direct saved AnnualReports.com HTML artifact if shell access to `annualreports.com` becomes reliable later.
- Local copies of the official `4Q25`, `1Q26`, and `2Q26` earnings-release PDFs and supplemental slide decks if a later fetch pass succeeds.
- Local transcript artifacts if S&P Global posts or preserves them publicly in a later archive pass.
