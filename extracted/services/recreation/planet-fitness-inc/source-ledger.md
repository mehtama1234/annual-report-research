# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| PLNT-S1 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Confirms the source mismatch `Consumer Goods / --None--` and the lagged `2024` annual package | `[Reported]` | [annualreports-verification.md](/raw/annualreports/services/recreation/planet-fitness-inc/annualreports-verification.md) |
| PLNT-S2 | AnnualReports company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves the company page showing `Consumer Goods` and `--None--` rather than a usable service taxonomy | `[Reported]` | [company-page.html](/raw/annualreports/services/recreation/planet-fitness-inc/company-page.html) |
| PLNT-S3 | Official IR verification note | 2026-08-10 | Official IR verification note | Records that the official site was challenge-blocked locally but still verifies the `2025` annual and `Q2 2026` results timing | `[Disclosed]` | [official-ir-verification.md](/raw/company-ir/services/recreation/planet-fitness-inc/official-ir-verification.md) |
| PLNT-S4 | Official IR overview shell snapshot | 2026-08-10 collected | Official web HTML snapshot | Preserves the challenge-blocked official-web shell | `[Disclosed]` | [overview.html](/raw/company-ir/services/recreation/planet-fitness-inc/overview.html) |
| PLNT-S5 | Attempted official annual-report file | 2026-08-10 collected | Official web challenge response | Documents that the shell environment could not retrieve the real PDF and instead saved a challenge page | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/services/recreation/planet-fitness-inc/2025-annual-report.pdf) |
| PLNT-S6 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Confirms filer identity, SEC SIC description, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001637207.json](/raw/sec/services/recreation/planet-fitness-inc/submissions-cik0001637207.json) |
| PLNT-S7 | SEC company facts file | 2026-08-10 collected | SEC XBRL facts JSON | Supports revenue, income, and quarter reconciliation | `[Filed]` | [companyfacts-cik0001637207.json](/raw/sec/services/recreation/planet-fitness-inc/companyfacts-cik0001637207.json) |
| PLNT-S8 | Fiscal 2025 Form 10-K | 2026-02-25 filed / 2026-08-10 collected | SEC filing HTML | Provides the full-year operating system and membership-franchise model | `[Filed]` | [2025-10k.html](/raw/sec/services/recreation/planet-fitness-inc/2025-10k.html) |
| PLNT-S9 | Q2 2026 Form 10-Q | 2026-08-06 filed / 2026-08-10 collected | SEC filing HTML | Latest in-scope quarterly filing | `[Filed]` | [2026-q2-10q.html](/raw/sec/services/recreation/planet-fitness-inc/2026-q2-10q.html) |
| PLNT-S10 | Q2 2026 earnings 8-K | 2026-08-06 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the latest results | `[Filed]` | [2026-q2-8k.html](/raw/sec/services/recreation/planet-fitness-inc/2026-q2-8k.html) |
| PLNT-S11 | Q2 2026 earnings release | 2026-08-06 filed / 2026-08-10 collected | SEC-hosted earnings release HTML | Clearest latest-quarter operating narrative and guidance | `[Filed]` | [2026-q2-press-release.html](/raw/sec/services/recreation/planet-fitness-inc/2026-q2-press-release.html) |
| PLNT-S12 | Q1 2026 Form 10-Q | 2026-05-08 filed / 2026-08-10 collected | SEC filing HTML | Prior in-scope quarterly filing | `[Filed]` | [2026-q1-10q.html](/raw/sec/services/recreation/planet-fitness-inc/2026-q1-10q.html) |
| PLNT-S13 | Q1 2026 earnings 8-K | 2026-05-07 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for Q1 `2026` results | `[Filed]` | [2026-q1-8k.html](/raw/sec/services/recreation/planet-fitness-inc/2026-q1-8k.html) |
| PLNT-S14 | Q1 2026 earnings release | 2026-05-07 filed / 2026-08-10 collected | SEC-hosted earnings release HTML | Clearest Q1 `2026` operating narrative and outlook reset | `[Filed]` | [2026-q1-press-release.html](/raw/sec/services/recreation/planet-fitness-inc/2026-q1-press-release.html) |
| PLNT-S15 | Q4 2025 earnings 8-K | 2026-02-24 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for Q4 and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/raw/sec/services/recreation/planet-fitness-inc/2025-q4-8k.html) |
| PLNT-S16 | Q4 2025 earnings release | 2026-02-24 filed / 2026-08-10 collected | SEC-hosted earnings release HTML | Clearest Q4 and full-year `2025` operating narrative and initial `2026` outlook | `[Filed]` | [2025-q4-press-release.html](/raw/sec/services/recreation/planet-fitness-inc/2025-q4-press-release.html) |

## Reconciliation notes

- The archive uses `Services / Recreation` as the analytical placement.
- The saved AnnualReports page instead showed `Consumer Goods / --None--`, which is the taxonomy mismatch this packet is meant to correct.
- The direct official annual-report PDF was not collectible in this shell environment because the saved file is an HTML challenge page rather than a real PDF.
- The fiscal `2025` `10-K` plus the `Q4 2025` through `Q2 2026` SEC-hosted exhibit chain are sufficient for the current packet.

## Missing evidence

- No valid standalone official annual-report PDF is saved locally.
- No standalone latest-quarter transcript artifact is saved locally.
