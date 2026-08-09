# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| SPOT-T1 | AnnualReports.com Spotify verification note | 2026-08-09 | Aggregator verification note | Confirms Spotify identity and taxonomy while showing AnnualReports.com still lagged the official reporting stack and only exposed the `2024` annual report | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/technology/internet-information-providers/spotify-technology-sa/annualreports-verification.md) |
| SPOT-T2 | Spotify official IR verification note | 2026-08-09 | Official IR verification note | Confirms the `2025` annual reporting year and the latest-quarter update stack on the live investor-relations site | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/technology/internet-information-providers/spotify-technology-sa/official-ir-verification.md) |
| SPOT-T3 | Spotify SEC submissions JSON | 2026-08-09 | SEC index JSON | Verifies legal name, ticker, exchange, SIC description, fiscal year-end, and the relevant `20-F` and `6-K` filing dates and accession numbers | `[Filed]` | [submissions-cik0001639920.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/technology/internet-information-providers/spotify-technology-sa/submissions-cik0001639920.json) |
| SPOT-T4 | Spotify `2025` Form `20-F` | 2026-02-10 | Annual filing HTML | Official annual filing artifact for the year ended `2025-12-31` | `[Filed]` | [2025-20f.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/technology/internet-information-providers/spotify-technology-sa/2025-20f.html) |
| SPOT-T5 | Spotify Q4 `2025` `6-K` | 2026-02-10 | Foreign-issuer current filing | Official SEC wrapper for the Q4 `2025` update | `[Filed]` | [2025-q4-6k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/technology/internet-information-providers/spotify-technology-sa/2025-q4-6k.html) |
| SPOT-T6 | Spotify Q4 `2025` update exhibit `99.1` | 2026-02-10 | Earnings update HTML | Provides year-end quarter metrics, annual run-rate metrics, and management commentary | `[Filed]` | [2025-q4-ex991.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/technology/internet-information-providers/spotify-technology-sa/2025-q4-ex991.html) |
| SPOT-T7 | Spotify Q4 `2025` shareholder deck | 2026-02-10 | Official IR deck PDF | Standalone official update artifact from Spotify's investor CDN | `[Disclosed]` | [2025-q4-shareholder-deck.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/technology/internet-information-providers/spotify-technology-sa/2025-q4-shareholder-deck.pdf) |
| SPOT-T8 | Spotify Q1 `2026` `6-K` | 2026-04-28 | Foreign-issuer current filing | Official SEC wrapper for the Q1 `2026` update | `[Filed]` | [2026-q1-6k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/technology/internet-information-providers/spotify-technology-sa/2026-q1-6k.html) |
| SPOT-T9 | Spotify Q1 `2026` update exhibit `99.1` | 2026-04-28 | Earnings update HTML | Provides first-quarter metrics, profitability, and management commentary | `[Filed]` | [2026-q1-ex991.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/technology/internet-information-providers/spotify-technology-sa/2026-q1-ex991.html) |
| SPOT-T10 | Spotify Q1 `2026` shareholder deck | 2026-04-28 | Official IR deck PDF | Standalone official update artifact from Spotify's investor CDN | `[Disclosed]` | [2026-q1-shareholder-deck.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/technology/internet-information-providers/spotify-technology-sa/2026-q1-shareholder-deck.pdf) |
| SPOT-T11 | Spotify Q2 `2026` `6-K` | 2026-08-04 | Foreign-issuer current filing | Official SEC wrapper for the Q2 `2026` update | `[Filed]` | [2026-q2-6k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/technology/internet-information-providers/spotify-technology-sa/2026-q2-6k.html) |
| SPOT-T12 | Spotify Q2 `2026` update exhibit `99.1` | 2026-08-04 | Earnings update HTML | Provides second-quarter metrics, subscriber milestone, and management commentary | `[Filed]` | [2026-q2-ex991.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/technology/internet-information-providers/spotify-technology-sa/2026-q2-ex991.html) |
| SPOT-T13 | Spotify Q2 `2026` shareholder deck | 2026-08-04 | Official IR deck PDF | Standalone official update artifact from Spotify's investor CDN | `[Disclosed]` | [2026-q2-shareholder-deck.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/technology/internet-information-providers/spotify-technology-sa/2026-q2-shareholder-deck.pdf) |

## Reconciliation notes

- Spotify now has a strong evidence chain for the `2025` annual reporting year and the last three reported quarters in scope:
  - `2025` `20-F`
  - Q4 `2025` update exhibit, `6-K`, and official shareholder deck
  - Q1 `2026` update exhibit, `6-K`, and official shareholder deck
  - Q2 `2026` update exhibit, `6-K`, and official shareholder deck
- SEC filing dates and accession numbers were verified through the official submissions JSON:
  - `2025` `20-F`: filed `2026-02-10`, accession `0001628280-26-006874`
  - Q4 `2025` `6-K`: filed `2026-02-10`, accession `0001140361-26-004482`
  - Q1 `2026` `6-K`: filed `2026-04-28`, accession `0001140361-26-017211`
  - Q2 `2026` `6-K`: filed `2026-08-04`, accession `0001140361-26-031044`

## Missing evidence

- The official `2025` annual-report PDF was referenced by the investor site but its direct CDN filename could not be resolved during this collection pass.
- Ordinary investor-site HTML pages returned `429` rate limiting in the shell environment, so the official IR verification rests on live site inspection plus the successfully downloaded shareholder-update PDFs.
