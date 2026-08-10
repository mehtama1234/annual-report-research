# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| JWN-T1 | AnnualReports.com Nordstrom verification note | 2026-08-10 | Aggregator verification note | Confirms `Consumer Goods / Department Stores` taxonomy and that AnnualReports still shows `2024` as the last public annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/consumer-goods/department-stores/nordstrom/annualreports-verification.md) |
| JWN-T2 | AnnualReports.com company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves the correct Nordstrom company page and lagging annual-report state | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/consumer-goods/department-stores/nordstrom/company-page.html) |
| JWN-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the final public annual-report artifact, final public Q4 release artifact, and the acquisition stop-point | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/consumer-goods/department-stores/nordstrom/official-ir-verification.md) |
| JWN-T4 | Final public annual report PDF | 2026-08-10 collected | Official annual report PDF | Final public annual-report artifact for fiscal `2024` / year ended `2025-02-01` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/consumer-goods/department-stores/nordstrom/2025-annual-report.pdf) |
| JWN-T5 | Final public Q4 earnings release PDF | 2026-08-10 collected | Official IR release PDF | Final public quarter-results artifact saved locally | `[Disclosed]` | [2025-q4-results-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/consumer-goods/department-stores/nordstrom/2025-q4-results-release.pdf) |
| JWN-T6 | SEC submissions index | 2026-08-10 collected and corrected | SEC submissions JSON | Verifies filer identity and confirms that the public filing chain ends in `2025` before any normal `2026` quarter window exists | `[Filed]` | [submissions-cik0000072333.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/department-stores/nordstrom/submissions-cik0000072333.json) |
| JWN-T7 | Saved local `10-K` file placeholder | preexisting local file | Local HTML artifact with verification issue | Preserved only as a path placeholder; should not be treated as authoritative because earlier SEC access attempts produced blocked-response HTML in this environment | `[verify]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/department-stores/nordstrom/2025-10k.html) |

## Reconciliation notes

- Nordstrom is a terminal public-company case, not an active `2026` trailing-three-quarter coverage target.
- The key fact is structural: the acquisition closed on `2025-05-20`, and Nordstrom common stock ceased trading before the NYSE open on `2025-05-21`.
- AnnualReports taxonomy remains useful, but the archive should not search for nonexistent public `2026` quarter materials after the take-private close.
- The corrected submissions JSON is authoritative for filing identity; older saved SEC HTML in this folder should be treated cautiously because some earlier fetches were blocked by SEC anti-automation controls.

## Missing evidence

- No standalone final public earnings-call transcript is saved locally.
- No cleaned replacement for the local `2025-10k.html` artifact has been saved yet; use the corrected submissions JSON and official annual-report PDF as the stronger evidence chain.
