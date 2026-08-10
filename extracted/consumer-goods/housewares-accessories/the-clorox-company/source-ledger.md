# The Clorox Company Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CLX-T1 | AnnualReports.com Clorox verification note | 2026-08-10 | Aggregator verification note | Confirms identity, source taxonomy, exchange, employees, headquarters label, and that AnnualReports still showed only the `2024` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/consumer-goods/housewares-accessories/the-clorox-company/annualreports-verification.md) |
| CLX-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the live company-page evidence used for taxonomy and AnnualReports lag verification | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/consumer-goods/housewares-accessories/the-clorox-company/company-page.html) |
| CLX-T3 | Clorox official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official annual-report page, quarterly-results page, quarter event pages, and locally saved annual-plus-quarter document chain | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/housewares-accessories/the-clorox-company/official-ir-verification.md) |
| CLX-T4 | Official `2025` integrated annual report PDF | 2026-08-10 collected | Official annual report PDF | Main annual artifact for the packet because the official IR site exposed `2025` while AnnualReports still lagged at `2024` | `[Disclosed]` | [2025-annual-report-ir.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/housewares-accessories/the-clorox-company/2025-annual-report-ir.pdf) |
| CLX-T5 | Q2 FY2026 press release and prepared remarks | 2026-08-10 collected | Official quarter materials | Anchors the earliest quarter in scope with direct metrics and management commentary | `[Disclosed]` | [2026-q2-press-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/housewares-accessories/the-clorox-company/2026-q2-press-release.pdf) |
| CLX-T6 | Q3 FY2026 press release and prepared remarks | 2026-08-10 collected | Official quarter materials | Anchors the middle quarter in scope including GOJO closing and slower-than-expected share recovery | `[Disclosed]` | [2026-q3-press-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/housewares-accessories/the-clorox-company/2026-q3-press-release.pdf) |
| CLX-T7 | Q4 FY2026 press release and prepared remarks | 2026-08-10 collected | Official quarter materials | Anchors the latest quarter in scope including FY`2027` framing, GOJO integration, and ERP comparison effects | `[Disclosed]` | [2026-q4-press-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/housewares-accessories/the-clorox-company/2026-q4-press-release.pdf) |
| CLX-T8 | SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies legal name, ticker, exchange, SIC description, fiscal year-end, and the annual plus trailing-quarter filing sequence | `[Filed]` | [submissions-cik0000021076.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/housewares-accessories/the-clorox-company/submissions-cik0000021076.json) |
| CLX-T9 | Clorox SEC access note | 2026-08-10 | SEC retrieval note | Logs the `10-K`, `10-Q`, and `8-K` accessions and explains why the direct SEC archive artifacts are not usable locally | `[Filed]` | [sec-access-note.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/housewares-accessories/the-clorox-company/sec-access-note.md) |

## Reconciliation notes

- Clorox is preserved under `Consumer Goods / Housewares & Accessories` because that is the source taxonomy on AnnualReports, even though the operating reality reads more like a household-cleaning and hygiene platform than a generic housewares name.
- The packet relies on the official IR annual report PDF and official IR quarter PDFs because AnnualReports still lagged at `2024` and direct SEC filing pages were blocked by anti-automation controls in this shell environment.
- The AnnualReports page, the official IR annual-report chain, and the SEC submissions index all reconcile to `The Clorox Company` / `CLOROX CO /DE/`, ticker `CLX`, headquartered in Oakland, California.

## Missing evidence

- No current `2025` AnnualReports-hosted annual report PDF is saved locally because AnnualReports still showed only the `2024` annual package on `2026-08-10`.
- No direct SEC filing HTML or binary artifacts are usable locally in this pass because the SEC archive returned anti-automation denial pages.
- No standalone verbatim earnings-call transcript artifact is saved locally in this pass.
