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
| CEMEX-T1 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Confirms archive continuity and authority hierarchy | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/basic-materials/general-building-materials/cemex-sab-de-cv/annualreports-verification.md) |
| CEMEX-T2 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves the annual and quarter document chain and notes the anti-bot limitation on HTML pages | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/cemex-sab-de-cv/ir-source-links.md) |
| CEMEX-T3 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves the authoritative `20-F` and `6-K` accession chain | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/cemex-sab-de-cv/sec-source-links.md) |
| CEMEX-T4 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms filing dates, accession numbers, ticker, and CIK linkage | `[Filed]` | [submissions-cik0001076378.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/cemex-sab-de-cv/submissions-cik0001076378.json) |
| CEMEX-T5 | `2025` audited consolidated financial statements PDF | 2026-08-10 collected | Audited financial statements PDF | Core annual financial source for 2025 revenue, income, cash flow, debt, goodwill, commitments, and segment framing | `[Disclosed]` | [2025-audited-consolidated-financial-statements.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/cemex-sab-de-cv/2025-audited-consolidated-financial-statements.pdf) |
| CEMEX-T6 | `Q4 2025` results PDF | 2026-08-10 collected | Official results PDF | Preserves the year-end operating discussion and 4Q25 metric set | `[Disclosed]` | [2025-q4-results-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/cemex-sab-de-cv/2025-q4-results-report.pdf) |
| CEMEX-T7 | `Q1 2026` results PDF | 2026-08-10 collected | Official results PDF | Preserves first-quarter metric set and management commentary | `[Disclosed]` | [2026-q1-results-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/cemex-sab-de-cv/2026-q1-results-report.pdf) |
| CEMEX-T8 | `Q1 2026` presentation PDF | 2026-08-10 collected | Official presentation PDF | Adds management framing and risk disclosures around the quarter | `[Disclosed]` | [2026-q1-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/cemex-sab-de-cv/2026-q1-presentation.pdf) |
| CEMEX-T9 | `Q2 2026` results PDF | 2026-08-10 collected | Official results PDF | Preserves latest-quarter metrics and commentary on Mexico, EMEA, IIJA, AI-related industrial demand, and cost savings | `[Disclosed]` | [2026-q2-results-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/cemex-sab-de-cv/2026-q2-results-report.pdf) |
| CEMEX-T10 | `Q2 2026` presentation PDF | 2026-08-10 collected | Official presentation PDF | Adds management framing around prices, volumes, and regional conditions | `[Disclosed]` | [2026-q2-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/cemex-sab-de-cv/2026-q2-presentation.pdf) |

## Reconciliation notes

- The correct trailing-quarter set as of 2026-08-10 is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- CEMEX is a foreign private issuer, so the authoritative annual filing is a `20-F` and the in-scope quarter wrappers are `6-K`s rather than `10-K` and `10-Q`.
- Local shell downloads of SEC HTML pages were blocked on 2026-08-10 by SEC automated-tool controls, so the packet uses preserved SEC metadata plus filing URLs for filing authority instead of pretending the blocked HTML stubs are usable evidence.
- Local shell downloads of CEMEX investor HTML pages were also blocked by anti-bot protection, but direct report PDFs remained accessible and were preserved locally.

## Missing evidence

- No separate official earnings-call transcript was collected for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- The full SEC filing HTML bodies were not locally preserved because of rate-limiting, though the accession chain and authoritative URLs were verified and recorded.
