# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| TMO-T1 | AnnualReports.com Thermo Fisher company-page capture | 2026-08-10 | Aggregator company-page HTML | Confirms AnnualReports taxonomy and `2025` annual-report archive availability | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/company-page.html) |
| TMO-T2 | AnnualReports.com Thermo Fisher verification note | 2026-08-10 | Aggregator verification note | Records the AnnualReports company-page URL for the archive trail | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/annualreports-verification.md) |
| TMO-T3 | Thermo Fisher IR source-links note | 2026-08-09 | Official-source link ledger | Preserves the verified official annual-report and quarterly-results page URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/ir-source-links.md) |
| TMO-T4 | Thermo Fisher 2025 annual report PDF | 2026-08-09 collected | Annual report PDF | Official annual-report artifact for fiscal `2025` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/2025-annual-report.pdf) |
| TMO-T5 | Thermo Fisher 2025 Form 10-K | 2026-02-26 filed / 2026-08-09 collected | SEC filing HTML | Filed annual report for fiscal `2025` | `[Filed]` | [tmo-20251231.htm](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/tmo-20251231.htm) |
| TMO-T6 | Thermo Fisher Q4 2025 earnings 8-K | 2026-01-29 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for late-`2025` earnings results | `[Filed]` | [tmo-20260129.htm](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/tmo-20260129.htm) |
| TMO-T7 | Thermo Fisher Q1 2026 earnings 8-K | 2026-04-23 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for Q1 `2026` earnings results | `[Filed]` | [tmo-20260423.htm](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/tmo-20260423.htm) |
| TMO-T8 | Thermo Fisher Q1 2026 Form 10-Q | 2026-05-01 filed / 2026-08-09 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-28` | `[Filed]` | [tmo-20260328.htm](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/tmo-20260328.htm) |
| TMO-T9 | Thermo Fisher Q2 2026 earnings 8-K | 2026-07-23 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for Q2 `2026` earnings results | `[Filed]` | [tmo-20260723.htm](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/tmo-20260723.htm) |
| TMO-T10 | Thermo Fisher Q2 2026 Form 10-Q | 2026-07-31 filed / 2026-08-09 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-27` | `[Filed]` | [tmo-20260627.htm](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/tmo-20260627.htm) |

## Reconciliation notes

- Thermo Fisher now has a clean annual-plus-quarterly evidence chain on disk for the `2025` annual package and the last three reported quarters as of Monday, `2026-08-10`.
- The annual report PDF is saved locally. The official quarterly result pages were verified and recorded in the IR source-links note, but shell-side download of those IR pages and reconciliation PDFs was not reliable in this pass because of source-side throttling.
- The company materially improves the healthcare sample by adding life-science-tools, scientific workflow, services, and recurring consumables economics.

## Missing evidence

- Local transcript artifacts for the `Q4 2025`, `Q1 2026`, and `Q2 2026` earnings calls.
- Local copies of the official quarterly IR result pages and reconciliation PDFs.
