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
| GVA-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports company page | Confirms company identity and archive taxonomy | `[Reported]` | [company-page.html](/raw/annualreports/industrial-goods/general-contractors/granite-construction-incorporated/company-page.html) |
| GVA-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents archive role and authority hierarchy | `[Reported]` | [annualreports-verification.md](/raw/annualreports/industrial-goods/general-contractors/granite-construction-incorporated/annualreports-verification.md) |
| GVA-T3 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves annual-report and quarterly-results URLs | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/industrial-goods/general-contractors/granite-construction-incorporated/ir-source-links.md) |
| GVA-T4 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves the authoritative `10-K`, `10-Q`, and `8-K` chain | `[Filed]` | [sec-source-links.md](/raw/sec/industrial-goods/general-contractors/granite-construction-incorporated/sec-source-links.md) |
| GVA-T5 | Annual reports page HTML | 2026-08-10 collected | Official archive page HTML | Confirms the official annual-report archive and `2025` report path | `[Disclosed]` | [annual-reports.html](/raw/company-ir/industrial-goods/general-contractors/granite-construction-incorporated/annual-reports.html) |
| GVA-T6 | `2025` annual report PDF | 2026-08-10 collected | Annual report PDF | Provides the annual strategic frame and operating-model context | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/industrial-goods/general-contractors/granite-construction-incorporated/2025-annual-report.pdf) |
| GVA-T7 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms filing dates, accession numbers, and ticker / CIK linkage | `[Filed]` | [submissions-cik0000861459.json](/raw/sec/industrial-goods/general-contractors/granite-construction-incorporated/submissions-cik0000861459.json) |
| GVA-T8 | `2025` Form `10-K` HTML | 2026-02-13 filed | Annual filing HTML | Authoritative annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/raw/sec/industrial-goods/general-contractors/granite-construction-incorporated/2025-10k.html) |
| GVA-T9 | `Q4 2025` official results page | 2026-02-12 | Official results page HTML | Provides year-end revenue, CAP, EBITDA, and guidance framing | `[Disclosed]` | [2025-q4-results-release.html](/raw/company-ir/industrial-goods/general-contractors/granite-construction-incorporated/2025-q4-results-release.html) |
| GVA-T10 | `Q4 2025` earnings release PDF | 2026-08-10 collected | Earnings release PDF | Preserves the year-end release locally | `[Disclosed]` | [2025-q4-earnings-release.pdf](/raw/company-ir/industrial-goods/general-contractors/granite-construction-incorporated/2025-q4-earnings-release.pdf) |
| GVA-T11 | `Q4 2025` Form `8-K` | 2026-02-12 filed | Results filing HTML | Filed earnings-release wrapper for quarter and full year `2025` | `[Filed]` | [2025-q4-8k.html](/raw/sec/industrial-goods/general-contractors/granite-construction-incorporated/2025-q4-8k.html) |
| GVA-T12 | `Q1 2026` official results page | 2026-04-30 | Official results page HTML | Provides first-quarter revenue, CAP, guidance, and acquisition commentary | `[Disclosed]` | [2026-q1-results-release.html](/raw/company-ir/industrial-goods/general-contractors/granite-construction-incorporated/2026-q1-results-release.html) |
| GVA-T13 | `Q1 2026` Form `10-Q` | 2026-04-30 filed | Quarterly filing HTML | Authoritative first-quarter financial statements and discussion | `[Filed]` | [2026-q1-10q.html](/raw/sec/industrial-goods/general-contractors/granite-construction-incorporated/2026-q1-10q.html) |
| GVA-T14 | `Q1 2026` Form `8-K` | 2026-04-30 filed | Results filing HTML | Filed wrapper for the first-quarter earnings release | `[Filed]` | [2026-q1-8k.html](/raw/sec/industrial-goods/general-contractors/granite-construction-incorporated/2026-q1-8k.html) |
| GVA-T15 | `Q2 2026` official results page | 2026-07-30 | Official results page HTML | Provides latest-quarter revenue, CAP, cash flow, guidance, and debt-transaction context | `[Disclosed]` | [2026-q2-results-release.html](/raw/company-ir/industrial-goods/general-contractors/granite-construction-incorporated/2026-q2-results-release.html) |
| GVA-T16 | `Q2 2026` Form `10-Q` | 2026-07-30 filed | Quarterly filing HTML | Authoritative latest-quarter financial statements and discussion | `[Filed]` | [2026-q2-10q.html](/raw/sec/industrial-goods/general-contractors/granite-construction-incorporated/2026-q2-10q.html) |
| GVA-T17 | `Q2 2026` Form `8-K` | 2026-07-30 filed | Results filing HTML | Filed wrapper for the latest-quarter earnings release | `[Filed]` | [2026-q2-8k.html](/raw/sec/industrial-goods/general-contractors/granite-construction-incorporated/2026-q2-8k.html) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- Granite IR and SEC are aligned on the timing and contents of the annual-plus-quarter evidence chain collected here.
- The `Q2 2026` GAAP net loss does not represent an operating collapse. Management attributes it to a non-operating loss tied to convertible-debt transactions, while adjusted earnings, EBITDA, CAP, and operating cash flow improved.

## Missing evidence

- No standalone earnings-call transcript artifact was saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No separate `Q1 2026` or `Q2 2026` investor-presentation PDF was collected during this pass.
