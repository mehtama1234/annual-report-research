# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| PODD-T1 | AnnualReports.com Insulet verification note | 2026-08-10 | Aggregator verification note | Confirms source taxonomy and that AnnualReports still lagged at the `2024` annual package | `[Reported]` | [annualreports-verification.md](/raw/annualreports/healthcare/medical-instruments-supplies/insulet-corporation/annualreports-verification.md) |
| PODD-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the company-page evidence used for taxonomy and archive confirmation | `[Reported]` | [company-page.html](/raw/annualreports/healthcare/medical-instruments-supplies/insulet-corporation/company-page.html) |
| PODD-T3 | Insulet IR source-links note | 2026-08-10 | Official IR verification note | Preserves official IR entry points and the verified annual and quarterly result URLs | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/healthcare/medical-instruments-supplies/insulet-corporation/ir-source-links.md) |
| PODD-T4 | Insulet SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms legal identity and filing sequence for the annual and quarterly chain | `[Filed]` | [CIK0001145197.json](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/CIK0001145197.json) |
| PODD-T5 | Insulet 2025 Form 10-K | 2026-02-18 | SEC filing HTML | Standalone annual filing for the year ended December 31, 2025 | `[Filed]` | [2025-10k.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2025-10k.html) |
| PODD-T6 | Insulet Q4 2025 earnings filing | 2026-02-18 | SEC current report | Captures fourth-quarter and full-year `2025` results plus initial `2026` guidance | `[Filed]` | [2025-q4-8k.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2025-q4-8k.html) |
| PODD-T7 | Insulet Q4 2025 press release exhibit | 2026-02-18 | SEC exhibit / company press release | Preserves the company-originated Q4 `2025` operating narrative and guidance | `[Filed]` | [2025-q4-exhibit-99-1.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2025-q4-exhibit-99-1.html) |
| PODD-T8 | Insulet Q1 2026 Form 10-Q | 2026-05-06 | SEC filing HTML | Filed quarterly report for March 31, 2026 | `[Filed]` | [2026-q1-10q.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2026-q1-10q.html) |
| PODD-T9 | Insulet Q1 2026 earnings filing | 2026-05-06 | SEC current report | Captures first-quarter `2026` results and updated guidance | `[Filed]` | [2026-q1-8k.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2026-q1-8k.html) |
| PODD-T10 | Insulet Q1 2026 press release exhibit | 2026-05-06 | SEC exhibit / company press release | Preserves the company-originated Q1 `2026` narrative on international rollout, margin expansion, and type 2 closed-loop development | `[Filed]` | [2026-q1-exhibit-99-1.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2026-q1-exhibit-99-1.html) |
| PODD-T11 | Insulet Q2 2026 Form 10-Q | 2026-08-05 | SEC filing HTML | Filed quarterly report for June 30, 2026 | `[Filed]` | [2026-q2-10q.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2026-q2-10q.html) |
| PODD-T12 | Insulet Q2 2026 earnings filing | 2026-08-05 | SEC current report | Captures most recent quarter results and raised guidance | `[Filed]` | [2026-q2-8k.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2026-q2-8k.html) |
| PODD-T13 | Insulet Q2 2026 press release exhibit | 2026-08-05 | SEC exhibit / company press release | Preserves the company-originated Q2 `2026` narrative on ecosystem expansion, whole-person care messaging, and strong adjusted profitability | `[Filed]` | [2026-q2-exhibit-99-1.html](/raw/sec/healthcare/medical-instruments-supplies/insulet-corporation/2026-q2-exhibit-99-1.html) |

## Reconciliation notes

- AnnualReports preserves the correct healthcare taxonomy, but the annual evidence chain itself had to be reconstructed from official IR references and SEC materials because AnnualReports lagged.
- Insulet's IR pages are verified as official entry points, but direct shell collection returned Cloudflare challenge pages rather than the substantive content.
- The SEC annual and quarterly filing chain is complete for the target window, and the company press release exhibits preserve the operating narrative that the IR pages would otherwise provide.

## Missing evidence

- No standalone IR-hosted `2025` annual-report PDF is saved locally in this pass.
- No standalone earnings-call transcript artifact is saved locally in this pass.
