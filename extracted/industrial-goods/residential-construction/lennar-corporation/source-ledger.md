# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| LEN-T1 | AnnualReports.com Lennar verification note | 2026-08-09 | Aggregator verification note | Confirms sector and industry labeling and that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/industrial-goods/residential-construction/lennar-corporation/annualreports-verification.md) |
| LEN-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarter-results chain for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/official-ir-verification.md) |
| LEN-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, exchange, and filing sequence | `[Filed]` | [submissions-cik0000920760.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/residential-construction/lennar-corporation/submissions-cik0000920760.json) |
| LEN-T4 | 2025 annual report PDF | 2026-08-09 collected | Official annual report PDF | Preserves the annual shareholder artifact for fiscal year ended `2025-11-30` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2025-annual-report.pdf) |
| LEN-T5 | Q4 2025 earnings release page | 2025-12-16 published / 2026-08-09 collected | Official earnings-release HTML | Preserves fiscal `2025` year-end operating language and full-year context | `[Disclosed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2025-q4-earnings-release.html) |
| LEN-T6 | Q4 2025 `10-K` PDF | 2026-08-09 collected | Official filing PDF | Preserves the year-end filing artifact from official IR | `[Filed]` | [2025-q4-10k-ir.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2025-q4-10k-ir.pdf) |
| LEN-T7 | Q4 2025 earnings-call transcript | 2026-08-09 collected | Official transcript PDF | Preserves verbatim management discussion on affordability, incentives, and volume | `[Disclosed]` | [2025-q4-earnings-call-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2025-q4-earnings-call-transcript.pdf) |
| LEN-T8 | Q1 2026 earnings release page | 2026-03-12 published / 2026-08-09 corrected and collected | Official earnings-release HTML | Preserves first-quarter `2026` metrics and the production-first land-light framing | `[Disclosed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2026-q1-earnings-release.html) |
| LEN-T9 | Q1 2026 `10-Q` PDF | 2026-08-09 collected | Official filing PDF | Preserves first-quarter filed financial statements from official IR | `[Filed]` | [2026-q1-10q-ir.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2026-q1-10q-ir.pdf) |
| LEN-T10 | Q1 2026 earnings-call transcript | 2026-08-09 collected | Official transcript PDF | Preserves verbatim management discussion on affordability, consumer sentiment, land-light strategy, and volume | `[Disclosed]` | [2026-q1-earnings-call-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2026-q1-earnings-call-transcript.pdf) |
| LEN-T11 | Q2 2026 earnings release page | 2026-06-11 published / 2026-08-09 collected | Official earnings-release HTML | Preserves second-quarter `2026` metrics, guidance, and operating language | `[Disclosed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2026-q2-earnings-release.html) |
| LEN-T12 | Q2 2026 `10-Q` PDF | 2026-08-09 collected | Official filing PDF | Preserves second-quarter filed financial statements from official IR | `[Filed]` | [2026-q2-10q-ir.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2026-q2-10q-ir.pdf) |
| LEN-T13 | Q2 2026 earnings-call transcript | 2026-08-09 collected | Official transcript PDF | Preserves verbatim management discussion on incentives, asset-light execution, and moderated delivery outlook | `[Disclosed]` | [2026-q2-earnings-call-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/residential-construction/lennar-corporation/2026-q2-earnings-call-transcript.pdf) |

## Reconciliation notes

- Lennar now has the official `2025` annual report PDF on disk plus the official IR-hosted filing PDFs and transcripts for the last three reported quarters in scope.
- The local quarter set uses `Q2 2026`, `Q1 2026`, and `Q4 2025` because those were the last three reported quarters available as of `2026-08-09`.
- AnnualReports.com still lagged at `2024`, so the official investor-relations site is the source of truth for the current annual package.
- SEC submissions JSON was collected cleanly, but direct SEC archive HTML fetches returned SEC anti-bot pages in this environment and are not used as trusted evidence for this packet.

## Missing evidence

- No raw AnnualReports HTML snapshot is saved locally because the packet relies on a verification note rather than a scraped copy of the company page.
- The local `raw/sec/.../*.html` Lennar files are not treated as valid filing bodies because they reflect SEC bot-protection responses rather than usable filing content.
