# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| KVUE-T1 | AnnualReports.com Kenvue verification note | 2026-08-10 | Aggregator verification note | Confirms identity, source taxonomy, exchange, employees, headquarters label, and the fact that AnnualReports still lagged at the `2024` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/biotechnology/kenvue/annualreports-verification.md) |
| KVUE-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the live company-page evidence used for taxonomy and annual-package verification | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/biotechnology/kenvue/company-page.html) |
| KVUE-T3 | Kenvue official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official overview, annual-reports page, and quarter-result URLs plus the key scale metrics and trailing-quarter dates | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/biotechnology/kenvue/official-ir-verification.md) |
| KVUE-T4 | SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies legal name, ticker, exchange, SIC description, address, fiscal year-end, and the filing sequence for the annual and trailing-quarter chain | `[Filed]` | [submissions-cik0001944048.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/biotechnology/kenvue/submissions-cik0001944048.json) |
| KVUE-T5 | Kenvue SEC access note | 2026-08-10 | SEC retrieval note | Logs the relevant `10-K`, `8-K`, `10-Q`, and `ARS` identifiers and explains why the direct SEC archive artifacts are not saved locally | `[Filed]` | [sec-access-note.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/biotechnology/kenvue/sec-access-note.md) |

## Reconciliation notes

- Kenvue is preserved under `Technology / Biotechnology` because that is the source taxonomy on AnnualReports.
- The operating reality is much closer to a consumer-health and trusted-routine-use platform than to a technology operating model.
- The local archive therefore keeps the source taxonomy in folders while cross-linking Kenvue into the consumer-interface work as a routine-care and wellness comparison.

## Missing evidence

- No live `2025` annual-report PDF or direct `10-K` HTML artifact is saved locally in this pass because the official IR domain returned Cloudflare challenge pages to shell fetches and the SEC archive returned anti-automation interstitial pages.
- No live Q4 `2025`, Q1 `2026`, or Q2 `2026` official release HTML or PDF artifacts are saved locally for the same reason.
- No standalone earnings-call transcript artifact is saved locally in this pass.
