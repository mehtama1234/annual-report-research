# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| ELF-T1 | AnnualReports.com e.l.f. Beauty verification note | 2026-08-10 | Aggregator verification note | Confirms `Consumer Goods / Personal Products` taxonomy and that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/raw/annualreports/consumer-goods/personal-products/elf-beauty-inc/annualreports-verification.md) |
| ELF-T2 | AnnualReports.com company page snapshot | 2026-08-10 | Aggregator HTML snapshot | Preserves the lagged live discovery page | `[Reported]` | [company-page.html](/raw/annualreports/consumer-goods/personal-products/elf-beauty-inc/company-page.html) |
| ELF-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the annual-report page, events page, and the latest-three-quarter scope | `[Disclosed]` | [official-ir-verification.md](/raw/company-ir/consumer-goods/personal-products/elf-beauty-inc/official-ir-verification.md) |
| ELF-T4 | 2025 annual report PDF | 2026-08-10 collected | Official annual report PDF | Core annual-report artifact from the official company source chain | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/consumer-goods/personal-products/elf-beauty-inc/2025-annual-report.pdf) |
| ELF-T5 | 2025 Form 10-K | 2026-05-21 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for fiscal year ended `2026-03-31` | `[Filed]` | [2025-10k.html](/raw/sec/consumer-goods/personal-products/elf-beauty-inc/2025-10k.html) |
| ELF-T6 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Confirms filer identity and filing sequence | `[Filed]` | [submissions-cik0001600033.json](/raw/sec/consumer-goods/personal-products/elf-beauty-inc/submissions-cik0001600033.json) |
| ELF-T7 | FY2026 Q3 earnings release | 2026-02-04 released / 2026-08-10 collected | Official IR release HTML | Official Q3 FY2026 operating narrative and key metrics | `[Disclosed]` | [2026-fyq3-press-release.html](/raw/company-ir/consumer-goods/personal-products/elf-beauty-inc/2026-fyq3-press-release.html) |
| ELF-T8 | FY2026 Q3 earnings 8-K | 2026-02-04 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for Q3 FY2026 results | `[Filed]` | [2026-fyq3-8k.html](/raw/sec/consumer-goods/personal-products/elf-beauty-inc/2026-fyq3-8k.html) |
| ELF-T9 | FY2026 Q3 Form 10-Q | 2026-02-05 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for quarter ended `2025-12-31` | `[Filed]` | [2026-fyq3-10q.html](/raw/sec/consumer-goods/personal-products/elf-beauty-inc/2026-fyq3-10q.html) |
| ELF-T10 | FY2026 Q4 and full-year results release | 2026-05-20 released / 2026-08-10 collected | Official IR release HTML | Official Q4 FY2026 and full-year FY2026 narrative | `[Disclosed]` | [2026-fyq4-press-release.html](/raw/company-ir/consumer-goods/personal-products/elf-beauty-inc/2026-fyq4-press-release.html) |
| ELF-T11 | FY2026 Q4 earnings 8-K | 2026-05-20 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for Q4 FY2026 and full-year FY2026 results | `[Filed]` | [2026-fyq4-8k.html](/raw/sec/consumer-goods/personal-products/elf-beauty-inc/2026-fyq4-8k.html) |
| ELF-T12 | FY2027 Q1 earnings release exhibit | 2026-08-05 filed / 2026-08-10 collected | SEC exhibit HTML | Exact latest-quarter metrics and updated FY2027 outlook | `[Filed]` | [2027-fyq1-earnings-release-ex99.html](/raw/sec/consumer-goods/personal-products/elf-beauty-inc/2027-fyq1-earnings-release-ex99.html) |
| ELF-T13 | FY2027 Q1 earnings 8-K | 2026-08-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for FY2027 Q1 results | `[Filed]` | [2027-fyq1-8k.html](/raw/sec/consumer-goods/personal-products/elf-beauty-inc/2027-fyq1-8k.html) |
| ELF-T14 | FY2027 Q1 Form 10-Q | 2026-08-06 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2027-fyq1-10q.html](/raw/sec/consumer-goods/personal-products/elf-beauty-inc/2027-fyq1-10q.html) |
| ELF-T15 | FY2027 Q1 presentation | 2026-08-05 collected | Official IR presentation PDF | Latest-quarter management framing preserved directly from the company IR stack | `[Disclosed]` | [2027-fyq1-presentation.pdf](/raw/company-ir/consumer-goods/personal-products/elf-beauty-inc/2027-fyq1-presentation.pdf) |
| ELF-T16 | FY2027 Q1 transcript | 2026-08-05 collected | Official IR transcript PDF | Latest-quarter transcript artifact preserved locally | `[Reported]` | [2027-fyq1-transcript.pdf](/raw/company-ir/consumer-goods/personal-products/elf-beauty-inc/2027-fyq1-transcript.pdf) |

## Reconciliation notes

- e.l.f. Beauty now has a full evidence chain on disk for the `2025` annual-report window and the correct latest three reported quarters in scope as of `2026-08-10`.
- The correct quarter window is `FY2027 Q1`, `FY2026 Q4`, and `FY2026 Q3`.
- `FY2026 Q2` materials exist locally but are outside the latest-three-quarter scope for Monday, August 10, 2026.
- AnnualReports is still useful for taxonomy and identity confirmation, but the page lagged at `2024`, so the current packet depends primarily on official IR and SEC evidence.

## Missing evidence

- No separate official IR HTML result page is saved for FY2027 Q1 because the latest-quarter numerical detail is already preserved in the SEC earnings-release exhibit and the official presentation and transcript PDFs.
