# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| TFM-T1 | AnnualReports verification note | 2026-08-10 | Verification note | Confirms that AnnualReports still lagged at `2024` and is being used only for taxonomy and archive confirmation | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/energy/oil-gas-equipment-services/technipfmc-plc/annualreports-verification.md) |
| TFM-T2 | AnnualReports company page capture | 2026-08-10 capture | Aggregator page capture | Preserves the saved page showing lag, ticker, taxonomy, and business description | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/energy/oil-gas-equipment-services/technipfmc-plc/company-page-annualreports.html) |
| TFM-T3 | Official IR verification note | 2026-08-10 | Verification note | Documents that the company-hosted IR routes were Cloudflare-blocked in this environment | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/energy/oil-gas-equipment-services/technipfmc-plc/official-ir-verification.md) |
| TFM-T4 | Company IR blocked route captures | 2026-08-10 captures | Official IR route captures | Preserves evidence that the `2025` results-center and quarter pages were not usable locally | `[Disclosed]` | [results-center-2025.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/energy/oil-gas-equipment-services/technipfmc-plc/results-center-2025.html) |
| TFM-T5 | SEC submissions index | 2026-08-10 capture | SEC JSON index | Preserves the authoritative chronology for the annual and quarter filing chain | `[Filed]` | [submissions-cik0001681459.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/submissions-cik0001681459.json) |
| TFM-T6 | Form `10-K` | 2026-02-19 | SEC filing HTML | Primary annual filing for the year ended `2025-12-31`, including segment structure, `iEPCI`, `Subsea 2.0`, services, backlog, and free-cash-flow framing | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2025-10k.html) |
| TFM-T7 | `Q4 2025` Form `8-K` | 2026-02-19 | SEC filing HTML | Filing wrapper for annual-close results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2025-q4-8k.html) |
| TFM-T8 | `Q4 2025` earnings release exhibit | 2026-02-19 | SEC Exhibit `99.1` HTML | Gives clean quarter and full-year metrics, subsea inbound, backlog, guidance, and shareholder distributions | `[Filed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2025-q4-earnings-release.html) |
| TFM-T9 | `Q1 2026` Form `10-Q` | 2026-04-30 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2026-q1-10q.html) |
| TFM-T10 | `Q1 2026` Form `8-K` | 2026-04-30 | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2026-q1-8k.html) |
| TFM-T11 | `Q1 2026` earnings release exhibit | 2026-04-30 | SEC Exhibit `99.1` HTML | Gives clean quarter metrics, inbound orders, backlog, free cash flow, and shareholder distributions | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2026-q1-earnings-release.html) |
| TFM-T12 | `Q2 2026` Form `10-Q` | 2026-07-30 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2026-q2-10q.html) |
| TFM-T13 | `Q2 2026` Form `8-K` | 2026-07-30 | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2026-q2-8k.html) |
| TFM-T14 | `Q2 2026` earnings release exhibit | 2026-07-30 | SEC Exhibit `99.1` HTML | Gives clean quarter metrics, subsea orders, free cash flow, and shareholder distributions | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-equipment-services/technipfmc-plc/2026-q2-earnings-release.html) |

## Reconciliation notes

- As of `2026-08-10`, the correct trailing-quarter set is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports is useful for taxonomy and archive confirmation only. It still lagged at `2024` for TechnipFMC.
- The official company-hosted IR routes were blocked by Cloudflare in this environment, so the packet is intentionally anchored in the SEC filing and Exhibit `99.1` chain.
- The annual evidence chain is therefore:
  - AnnualReports verification artifact
  - IR block verification note
  - SEC `10-K`
- The quarter evidence chain is therefore:
  - SEC `8-K`
  - SEC Exhibit `99.1`
  - SEC `10-Q`

## Missing evidence

- No clean company-hosted annual-report or quarter-result files were collected because the local IR route captures were Cloudflare block pages.
- No local earnings-call transcript PDFs were collected for the target quarters.
