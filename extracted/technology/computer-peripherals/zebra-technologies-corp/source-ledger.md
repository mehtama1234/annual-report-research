# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| ZBRA-T1 | AnnualReports.com company page | 2026-08-10 collected | Aggregator page HTML | Preserves the current taxonomy and confirms that AnnualReports still lags at `2024` | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/technology/computer-peripherals/zebra-technologies-corp/company-page.html) |
| ZBRA-T2 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Records the observed `Technology / Computer Peripherals` classification and archive lag | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/technology/computer-peripherals/zebra-technologies-corp/annualreports-verification.md) |
| ZBRA-T3 | Zebra official IR verification note | 2026-08-10 | Official IR verification note | Preserves the official page stack, quarter cutoff logic, and shell-access constraints | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computer-peripherals/zebra-technologies-corp/official-ir-verification.md) |
| ZBRA-T4 | Zebra SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies filer identity and the annual-plus-quarter filing sequence in scope | `[Filed]` | [submissions-cik0000877212.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computer-peripherals/zebra-technologies-corp/submissions-cik0000877212.json) |
| ZBRA-T5 | Zebra `2025` annual report PDF | 2026-04-03 filed / 2026-08-10 collected | SEC `ARS` PDF | Preserves the standalone annual-report artifact for the year ended `2025-12-31` | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computer-peripherals/zebra-technologies-corp/2025-annual-report.pdf) |
| ZBRA-T6 | Zebra `2025` Form `10-K` | 2026-02-12 filed / 2026-08-10 collected | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computer-peripherals/zebra-technologies-corp/2025-10k.html) |
| ZBRA-T7 | Zebra Q4 `2025` / FY `2025` earnings `8-K` | 2026-02-12 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper confirming the year-end results release date and annual-results reporting chain | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computer-peripherals/zebra-technologies-corp/2025-q4-8k.html) |
| ZBRA-T8 | Zebra Q1 `2026` `10-Q` | 2026-05-12 filed / 2026-08-10 collected | SEC filing HTML | First-quarter `2026` filing covering the new segment structure and operating mix | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computer-peripherals/zebra-technologies-corp/2026-q1-10q.html) |
| ZBRA-T9 | Zebra Q1 `2026` earnings `8-K` | 2026-05-12 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computer-peripherals/zebra-technologies-corp/2026-q1-8k.html) |
| ZBRA-T10 | Zebra Q2 `2026` `10-Q` | 2026-08-04 filed / 2026-08-10 collected | SEC filing HTML | Most recent quarter in scope and the best evidence for current frontline-device, automation, and workflow mix | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computer-peripherals/zebra-technologies-corp/2026-q2-10q.html) |
| ZBRA-T11 | Zebra Q2 `2026` earnings `8-K` | 2026-08-04 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computer-peripherals/zebra-technologies-corp/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports is useful here for taxonomy, but it still lagged at `2024` as of `2026-08-10`.
- The required `2025` annual-report window is satisfied through Zebra's official annual-reports page plus the filed `2025` `ARS` PDF and `10-K`.
- The latest three reported periods in scope as of `2026-08-10` are:
  - `Q2 2026`, reported `2026-08-04`
  - `Q1 2026`, reported `2026-05-12`
  - `Q4 2025` / FY `2025`, reported `2026-02-12`
- Zebra's official IR site was rate-limited in direct shell access, so the local raw archive preserves URL-verification notes plus SEC-hosted annual and quarter artifacts rather than locally downloaded official IR HTML pages.

## Missing evidence

- No locally saved official IR HTML pages are preserved because direct shell retrieval returned `429` in this environment.
- No standalone earnings-release exhibit or transcript artifact is saved locally.
