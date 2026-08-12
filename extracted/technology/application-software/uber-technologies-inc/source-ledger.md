# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| UBER-T1 | AnnualReports.com Uber verification note | 2026-08-10 | Aggregator verification note | Confirms current AnnualReports identity, lagging annual-package status, and the `Technology / Application Software` taxonomy | `[Reported]` | [annualreports-verification.md](/raw/annualreports/technology/application-software/uber-technologies-inc/annualreports-verification.md) |
| UBER-T2 | AnnualReports company page HTML | 2026-08-10 | Aggregator page HTML | Preserves the live company-page evidence used for taxonomy and annual-package verification | `[Reported]` | [company-page.html](/raw/annualreports/technology/application-software/uber-technologies-inc/company-page.html) |
| UBER-T3 | Uber official IR verification note | 2026-08-10 | Official IR verification note | Records the official IR chain and explains the Cloudflare challenge limitation in this shell environment | `[Disclosed]` | [official-ir-verification.md](/raw/company-ir/technology/application-software/uber-technologies-inc/official-ir-verification.md) |
| UBER-T4 | SEC-hosted annual report PDF | 2026-08-10 collected | Annual report PDF | Preserves a durable official annual-report artifact even though the main IR HTML pages were challenge-gated | `[Disclosed]` | [2025-annual-report-sec-ars.pdf](/raw/company-ir/technology/application-software/uber-technologies-inc/2025-annual-report-sec-ars.pdf) |
| UBER-T5 | SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies legal name, ticker, exchange, SIC description, address, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001543151.json](/raw/sec/technology/application-software/uber-technologies-inc/submissions-cik0001543151.json) |
| UBER-T6 | Uber `2025` Form `10-K` | 2026-02-13 filed / 2026-08-10 collected | Annual filing HTML | Core annual filing artifact for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/raw/sec/technology/application-software/uber-technologies-inc/2025-10k.html) |
| UBER-T7 | Uber Q4 `2025` `8-K` | 2026-02-04 filed / 2026-08-10 collected | Current-report HTML | SEC wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/raw/sec/technology/application-software/uber-technologies-inc/2025-q4-8k.html) |
| UBER-T8 | Uber Q4 `2025` `99.1` press release | 2026-02-04 filed / 2026-08-10 collected | Earnings press release HTML | Full year-end results exhibit with trips, MAPCs, gross bookings, revenue, cash flow, and Q1 `2026` outlook | `[Filed]` | [2025-q4-press-release.html](/raw/sec/technology/application-software/uber-technologies-inc/2025-q4-press-release.html) |
| UBER-T9 | Uber Q1 `2026` `10-Q` | 2026-05-06 filed / 2026-08-10 collected | Quarterly filing HTML | Official quarterly filing artifact for the period ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/raw/sec/technology/application-software/uber-technologies-inc/2026-q1-10q.html) |
| UBER-T10 | Uber Q1 `2026` `8-K` | 2026-05-06 filed / 2026-08-10 collected | Current-report HTML | SEC wrapper for the first-quarter results release | `[Filed]` | [2026-q1-8k.html](/raw/sec/technology/application-software/uber-technologies-inc/2026-q1-8k.html) |
| UBER-T11 | Uber Q1 `2026` `99.1` press release | 2026-05-06 filed / 2026-08-10 collected | Earnings press release HTML | First-quarter release with MAPCs, Uber One, gross bookings, revenue, and cash-generation detail | `[Filed]` | [2026-q1-press-release.html](/raw/sec/technology/application-software/uber-technologies-inc/2026-q1-press-release.html) |
| UBER-T12 | Uber Q2 `2026` `10-Q` | 2026-08-05 filed / 2026-08-10 collected | Quarterly filing HTML | Official quarterly filing artifact for the period ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/raw/sec/technology/application-software/uber-technologies-inc/2026-q2-10q.html) |
| UBER-T13 | Uber Q2 `2026` `8-K` | 2026-08-05 filed / 2026-08-10 collected | Current-report HTML | SEC wrapper for the second-quarter results release | `[Filed]` | [2026-q2-8k.html](/raw/sec/technology/application-software/uber-technologies-inc/2026-q2-8k.html) |
| UBER-T14 | Uber Q2 `2026` `99.1` press release | 2026-08-05 filed / 2026-08-10 collected | Earnings press release HTML | Most recent quarter release with scale, profitability, free-cash-flow, and Q3 `2026` outlook detail | `[Filed]` | [2026-q2-press-release.html](/raw/sec/technology/application-software/uber-technologies-inc/2026-q2-press-release.html) |

## Reconciliation notes

- AnnualReports classifies Uber as `Technology / Application Software`, but the actual evidence chain reads more like a mobility, delivery, local-commerce, membership, and coordination platform.
- AnnualReports is also lagging on the annual package here: the live page still shows only `2024`, while the repo has the `2025` `10-K`, the associated year-end `8-K`, and a SEC-hosted annual report PDF.
- The local official IR HTML captures are not usable evidence because they are Cloudflare challenge pages in this environment, so the durable packet is grounded in the SEC chain plus the recorded IR verification note.

## Missing evidence

- No standalone earnings-call transcript artifact is saved locally in this pass.
- No clean locally saved HTML snapshot from the live Uber IR site was collectible from this shell environment beyond challenge pages.
