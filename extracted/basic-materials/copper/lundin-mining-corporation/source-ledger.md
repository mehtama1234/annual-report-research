# Source Ledger

Date baseline: 2026-08-10

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` filing or filing-equivalent reference
- `[Reported]` credible press or transcript provider
- `[Estimated]` derived or analyst estimate
- `[Speculative]` weak or unverified
- `[verify]` found but not yet confirmed directly

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| LUN-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports page | Confirms taxonomy and provides archive confirmation for `Copper` | `[verify]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/copper/lundin-mining-corporation/company-page-annualreports.html) |
| LUN-T2 | Financial reports index | 2026-08-10 collected | Investor-relations page | Official reporting hub listing the `2025` annual package and `2026` quarter PDFs | `[Disclosed]` | [financial-reports-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/financial-reports-page.html) |
| LUN-T3 | Investors overview page | 2026-08-10 collected | Investor-relations page | Secondary official page confirming the current quarter-report links from the investor hub | `[Disclosed]` | [investors-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/investors-page.html) |
| LUN-T4 | 2026 news index page | 2026-08-10 collected | Investor-relations page | Confirms the annual-report publication item exists in the official `2026` news archive | `[Disclosed]` | [news-2026-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/news-2026-page.html) |
| LUN-T5 | 2025 annual-report publication page | 2026-04-28 published, 2026-08-10 collected | Investor-relations page | Official page confirming publication of the `2025` sustainability statement and annual report | `[Disclosed]` | [2025-annual-report-publication-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/2025-annual-report-publication-page.html) |
| LUN-T6 | 2025 Swedish annual report PDF | 2026 published, 2026-08-10 collected | Annual report PDF | Core `2025` annual report package for the company | `[Disclosed]` | [2025-swedish-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/2025-swedish-annual-report.pdf) |
| LUN-T7 | 2025 annual MD&A and financial statements | 2026-02-19 prepared, 2026-08-10 collected | Annual financial-report PDF | Full-year `2025` annual operating, balance-sheet, and mine-level detail; also anchors `Q4 2025` | `[Filed]` | [2025-q4-financial-report.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/2025-q4-financial-report.pdf) |
| LUN-T8 | Q1 2026 results page | 2026-05-01 | Results page | Official quarter page with record revenue, strong prices, and Vicuña and Los Helados project framing | `[Disclosed]` | [q1-2026-results-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/q1-2026-results-page.html) |
| LUN-T9 | Q1 2026 MD&A and financial statements | 2026-05-06 prepared, 2026-08-10 collected | Quarterly financial-report PDF | Full `Q1 2026` financial, production, capex, and net-cash detail | `[Filed]` | [2026-q1-financial-report.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/2026-q1-financial-report.pdf) |
| LUN-T10 | Q2 2026 results page | 2026-07-29 | Results page | Official quarter page with near-record revenue and free cash flow, Caserones and Los Helados acquisition detail, and post-quarter storm commentary | `[Disclosed]` | [q2-2026-results-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/q2-2026-results-page.html) |
| LUN-T11 | Q2 2026 MD&A and financial statements | 2026-08-05 prepared, 2026-08-10 collected | Quarterly financial-report PDF | Full `Q2 2026` financial, production, capex, and post-quarter operational guidance detail | `[Filed]` | [2026-q2-financial-report.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/copper/lundin-mining-corporation/2026-q2-financial-report.pdf) |
| LUN-T12 | Filing note | 2026-08-10 compiled | Filing-chain note | Documents why the packet uses official company reporting rather than a local SEC chain | `[Filed]` | [filing-note.md](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/copper/lundin-mining-corporation/filing-note.md) |

## Reconciliation notes

- The user requirement is `2025` annual reports plus the latest three reported quarters as of `Monday, August 10, 2026`.
- For Lundin Mining, the correct mapping is:
  - latest period: `Q2 2026`
  - period minus 1: `Q1 2026`
  - period minus 2: `Q4 2025`
- The authoritative chain is the official company reporting set. AnnualReports is used for taxonomy confirmation, not as the controlling annual-report source.

## Missing evidence

- No separate local SEC chain was collected for this packet.
- That is intentional rather than a gap because the official Lundin Mining reporting set is complete for the required annual and quarter window.
