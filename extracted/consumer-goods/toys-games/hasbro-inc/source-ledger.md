# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| HAS-T1 | AnnualReports.com Hasbro verification note | 2026-08-10 | Aggregator verification note | Confirms archive identity and documents that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/raw/annualreports/consumer-goods/toys-games/hasbro-inc/annualreports-verification.md) |
| HAS-T2 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official annual-report and quarterly-results chain for the target window | `[Disclosed]` | [official-ir-verification.md](/raw/company-ir/consumer-goods/toys-games/hasbro-inc/official-ir-verification.md) |
| HAS-T3 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, ticker, SIC description, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000046080.json](/raw/sec/consumer-goods/toys-games/hasbro-inc/submissions-cik0000046080.json) |
| HAS-T4 | Official 2025 annual report PDF | 2026-08-10 collected | Official IR PDF | Preserves the live annual-report artifact for the fiscal year ended `2025-12-28` | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/consumer-goods/toys-games/hasbro-inc/2025-annual-report.pdf) |
| HAS-T5 | 2025 Form `10-K` | 2026-02-25 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for the year ended `2025-12-28` | `[Filed]` | [2025-10k.html](/raw/sec/consumer-goods/toys-games/hasbro-inc/2025-10k.html) |
| HAS-T6 | Q4 and FY 2025 results page | 2026-02-10 published / 2026-08-10 collected | Official company results HTML | Preserves fourth-quarter and full-year `2025` operating narrative and metrics | `[Disclosed]` | [2025-q4-and-fy-results-page.html](/raw/company-ir/consumer-goods/toys-games/hasbro-inc/2025-q4-and-fy-results-page.html) |
| HAS-T7 | Q4 and FY 2025 earnings `8-K` | 2026-02-10 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-and-fy-8k.html](/raw/sec/consumer-goods/toys-games/hasbro-inc/2025-q4-and-fy-8k.html) |
| HAS-T8 | Q1 2026 results page | 2026-05-20 published / 2026-08-10 collected | Official company results HTML | Preserves first-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q1-results-page.html](/raw/company-ir/consumer-goods/toys-games/hasbro-inc/2026-q1-results-page.html) |
| HAS-T9 | Q1 2026 earnings `8-K` | 2026-04-23 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/raw/sec/consumer-goods/toys-games/hasbro-inc/2026-q1-8k.html) |
| HAS-T10 | Q1 2026 Form `10-Q` | 2026-05-13 filed / 2026-08-10 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/raw/sec/consumer-goods/toys-games/hasbro-inc/2026-q1-10q.html) |
| HAS-T11 | Q2 2026 results page | 2026-07-21 published / 2026-08-10 collected | Official company results HTML | Preserves second-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q2-results-page.html](/raw/company-ir/consumer-goods/toys-games/hasbro-inc/2026-q2-results-page.html) |
| HAS-T12 | Q2 2026 earnings `8-K` | 2026-07-27 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/raw/sec/consumer-goods/toys-games/hasbro-inc/2026-q2-8k.html) |
| HAS-T13 | Q2 2026 Form `10-Q` | 2026-07-30 filed / 2026-08-10 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/raw/sec/consumer-goods/toys-games/hasbro-inc/2026-q2-10q.html) |

## Reconciliation notes

- Hasbro now has the full annual-plus-quarter chain on disk for the fiscal `2025` annual package and the last three quarters in scope.
- `AnnualReports` remained useful for taxonomy discovery, but as of `2026-08-10` it still lagged at `2024`.
- The official IR chain was necessary to collect the live `2025 Annual Report` and the quarter-window support materials.
- The company should be read as a play, fandom, and franchise-IP system rather than flattened into a generic toy manufacturer.

## Missing evidence

- No standalone transcript artifacts for `Q4 2025`, `Q1 2026`, or `Q2 2026` are saved locally.
- The packet currently leans most heavily on official IR results pages plus the SEC filing chain; deeper annual-report PDF extraction can still be added later if a more granular annual operating summary is needed.
