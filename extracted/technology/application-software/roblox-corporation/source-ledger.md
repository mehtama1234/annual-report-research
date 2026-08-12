# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| RBLX-T1 | AnnualReports.com Roblox company page | 2026-08-10 collected | Aggregator page | Confirms archive identity, sector, and industry while documenting the lagged `2024` annual label | `[Reported]` | [company-page.html](/raw/annualreports/technology/application-software/roblox-corporation/company-page.html) |
| RBLX-T2 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Records the latest observed AnnualReports metadata and lag condition | `[Reported]` | [annualreports-verification.md](/raw/annualreports/technology/application-software/roblox-corporation/annualreports-verification.md) |
| RBLX-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Records live annual-report, quarterly-results, events, and overview metadata because the main IR navigation pages were Cloudflare-blocked in direct shell capture | `[Disclosed]` | [official-ir-verification.md](/raw/company-ir/technology/application-software/roblox-corporation/official-ir-verification.md) |
| RBLX-T4 | Saved IR overview HTML | 2026-08-10 collected | Official IR HTML snapshot | Preserves the blocked shell capture and documents the Cloudflare challenge condition | `[Disclosed]` | [overview.html](/raw/company-ir/technology/application-software/roblox-corporation/overview.html) |
| RBLX-T5 | Saved IR annual-reports HTML | 2026-08-10 collected | Official IR HTML snapshot | Preserves the blocked shell capture for the annual-reports page | `[Disclosed]` | [annual-reports.html](/raw/company-ir/technology/application-software/roblox-corporation/annual-reports.html) |
| RBLX-T6 | Saved IR quarterly-results HTML | 2026-08-10 collected | Official IR HTML snapshot | Preserves the blocked shell capture for the quarterly-results page | `[Disclosed]` | [quarterly-results.html](/raw/company-ir/technology/application-software/roblox-corporation/quarterly-results.html) |
| RBLX-T7 | Saved IR SEC-filings HTML | 2026-08-10 collected | Official IR HTML snapshot | Preserves the blocked shell capture for the SEC-filings page | `[Disclosed]` | [sec-filings.html](/raw/company-ir/technology/application-software/roblox-corporation/sec-filings.html) |
| RBLX-T8 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, ticker, SIC description, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001315098.json](/raw/sec/technology/application-software/roblox-corporation/submissions-cik0001315098.json) |
| RBLX-T9 | SEC company facts file | 2026-08-10 collected | SEC XBRL facts JSON | Provides clean revenue, net loss, and operating-cash-flow series | `[Filed]` | [companyfacts-cik0001315098.json](/raw/sec/technology/application-software/roblox-corporation/companyfacts-cik0001315098.json) |
| RBLX-T10 | SEC-hosted `2025` annual report PDF | 2026-04-16 filed / 2026-08-10 collected | SEC annual-report PDF | Preserves the annual-report artifact for the fiscal year ended `2025-12-31` | `[Filed]` | [2025-annual-report.pdf](/raw/sec/technology/application-software/roblox-corporation/2025-annual-report.pdf) |
| RBLX-T11 | `2025` Form `10-K` | 2026-02-11 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/raw/sec/technology/application-software/roblox-corporation/2025-10k.html) |
| RBLX-T12 | `Q4 2025` earnings `8-K` | 2026-02-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/raw/sec/technology/application-software/roblox-corporation/2025-q4-8k.html) |
| RBLX-T13 | `Q4 2025` shareholder letter | 2026-02-05 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the fourth-quarter and full-year `2025` operating narrative and metrics | `[Filed]` | [2025-q4-shareholder-letter.html](/raw/sec/technology/application-software/roblox-corporation/2025-q4-shareholder-letter.html) |
| RBLX-T14 | `Q1 2026` earnings `8-K` | 2026-04-30 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/raw/sec/technology/application-software/roblox-corporation/2026-q1-8k.html) |
| RBLX-T15 | `Q1 2026` shareholder letter | 2026-04-30 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves first-quarter `2026` operating narrative and metrics | `[Filed]` | [2026-q1-shareholder-letter.html](/raw/sec/technology/application-software/roblox-corporation/2026-q1-shareholder-letter.html) |
| RBLX-T16 | `Q1 2026` Form `10-Q` | 2026-04-30 filed / 2026-08-10 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/raw/sec/technology/application-software/roblox-corporation/2026-q1-10q.html) |
| RBLX-T17 | `Q2 2026` earnings `8-K` | 2026-07-30 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/raw/sec/technology/application-software/roblox-corporation/2026-q2-8k.html) |
| RBLX-T18 | `Q2 2026` shareholder letter | 2026-07-30 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the current-quarter operating narrative and metrics | `[Filed]` | [2026-q2-shareholder-letter.html](/raw/sec/technology/application-software/roblox-corporation/2026-q2-shareholder-letter.html) |
| RBLX-T19 | `Q2 2026` Form `10-Q` | 2026-07-30 filed / 2026-08-10 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/raw/sec/technology/application-software/roblox-corporation/2026-q2-10q.html) |

## Reconciliation notes

- Roblox now has the full annual-plus-quarter filing chain on disk for the fiscal `2025` annual package and the last three quarters in scope.
- The `AnnualReports` page remained useful for taxonomy discovery, but as of `2026-08-10` it still lagged at `2024`.
- The official IR navigation pages were visible through search-accessible verification, but the direct shell captures landed on Cloudflare challenge pages. This is why the archive relies on a verification note plus the SEC annual-report artifact and SEC-hosted shareholder letters.
- Roblox should be read as a digital participation and creator-economy platform rather than flattened into a plain software comparison.

## Missing evidence

- No standalone official transcript file is saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No directly downloadable official IR PDFs were collectible in this shell environment because the IR domain returned challenge HTML for the direct artifact URLs tested.
