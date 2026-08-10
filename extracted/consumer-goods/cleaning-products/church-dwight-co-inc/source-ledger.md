# Church & Dwight Co. Inc. Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CHD-T1 | AnnualReports.com Church & Dwight verification note | 2026-08-10 | Aggregator verification note | Confirms identity, source taxonomy, exchange, employees, headquarters label, and current `2025` annual-package availability | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/consumer-goods/cleaning-products/church-dwight-co-inc/annualreports-verification.md) |
| CHD-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the live company-page evidence used for taxonomy and annual-package verification | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/consumer-goods/cleaning-products/church-dwight-co-inc/company-page.html) |
| CHD-T3 | AnnualReports-hosted `2025` annual report PDF | 2026-08-10 collected | Aggregator annual report PDF | Preserves the `2025` annual-report artifact saved locally from the AnnualReports click path | `[Reported]` | [2025-annual-report-annualreports.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/consumer-goods/cleaning-products/church-dwight-co-inc/2025-annual-report-annualreports.pdf) |
| CHD-T4 | Church & Dwight official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official overview, annual-reports page, quarter-result URLs, and trailing-quarter metrics and dates | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/cleaning-products/church-dwight-co-inc/official-ir-verification.md) |
| CHD-T5 | SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies legal name, ticker, exchange, SIC description, address, fiscal year-end, and the filing sequence for the annual and trailing-quarter chain | `[Filed]` | [submissions-cik0000313927.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/cleaning-products/church-dwight-co-inc/submissions-cik0000313927.json) |
| CHD-T6 | Church & Dwight SEC access note | 2026-08-10 | SEC retrieval note | Logs the relevant `10-K`, `8-K`, `10-Q`, and `ARS` identifiers and explains why the direct SEC archive artifacts are not saved locally | `[Filed]` | [sec-access-note.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/cleaning-products/church-dwight-co-inc/sec-access-note.md) |

## Reconciliation notes

- Church & Dwight is preserved under `Consumer Goods / Cleaning Products` because that is the source taxonomy on AnnualReports and it also matches the operating reality cleanly.
- The packet relies on the AnnualReports PDF for the machine-local annual-report artifact and on official IR plus SEC submissions verification notes for the quarter and filing chain.
- The local evidence is therefore stronger on annual-package capture than on official filing-binary capture in this pass.

## Missing evidence

- No direct `2025` `10-K`, `ARS`, `Q4 2025`, `Q1 2026`, or `Q2 2026` SEC archive artifacts are saved locally in this pass because the SEC archive returned anti-automation interstitial pages.
- No live official IR result-page HTML or PDF artifacts are saved locally in this pass because the Church & Dwight IR domain returned Cloudflare challenge pages to shell fetches.
- No standalone earnings-call transcript artifact is saved locally in this pass.
