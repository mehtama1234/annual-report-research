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
| GWW-T1 | AnnualReports company page | 2026-08-10 collected | Aggregator company page | Confirms archive identity and AnnualReports taxonomy | `[Reported]` | [company-page.html](/raw/annualreports/industrial-goods/industrial-supply/ww-grainger-inc/company-page.html) |
| GWW-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents the archive role and the `2024` lag versus the required `2025` annual window | `[Reported]` | [annualreports-verification.md](/raw/annualreports/industrial-goods/industrial-supply/ww-grainger-inc/annualreports-verification.md) |
| GWW-T3 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves the annual-report and quarter-result navigation chain | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/industrial-goods/industrial-supply/ww-grainger-inc/ir-source-links.md) |
| GWW-T4 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves the authoritative `10-K`, `10-Q`, and `8-K` chain plus the exhibit challenge-page caveat | `[Filed]` | [sec-source-links.md](/raw/sec/industrial-goods/industrial-supply/ww-grainger-inc/sec-source-links.md) |
| GWW-T5 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms filing dates, accession numbers, CIK linkage, and latest-quarter ordering | `[Filed]` | [submissions-cik0000277135.json](/raw/sec/industrial-goods/industrial-supply/ww-grainger-inc/submissions-cik0000277135.json) |
| GWW-T6 | `2025` Form `10-K` | 2026-02-19 filed | Annual filing HTML | Preserves business-model framing, segment mix, geography, cash flow, capital allocation, and full-year financial baseline | `[Filed]` | [2025-10k.html](/raw/sec/industrial-goods/industrial-supply/ww-grainger-inc/2025-10k.html) |
| GWW-T7 | `Q4 2025` results `8-K` | 2026-02-03 filed | Results filing HTML | Filed wrapper for the fourth-quarter and full-year `2025` results release | `[Filed]` | [2025-q4-8k.html](/raw/sec/industrial-goods/industrial-supply/ww-grainger-inc/filings/2025-q4-8k.html) |
| GWW-T8 | `Q4 2025` official results page | 2026-02-03 published | Company-distributed results page | Preserves quarter commentary on tariffs, U.K. exit effects, segment growth, and quarterly cash returns | `[Disclosed]` | [2025-q4-results-prnewswire.html](/raw/company-ir/industrial-goods/industrial-supply/ww-grainger-inc/2025-q4-results-prnewswire.html) |
| GWW-T9 | `Q1 2026` results `8-K` | 2026-05-08 filed | Results filing HTML | Filed wrapper for the first-quarter `2026` release | `[Filed]` | [2026-q1-8k.html](/raw/sec/industrial-goods/industrial-supply/ww-grainger-inc/filings/2026-q1-8k.html) |
| GWW-T10 | `Q1 2026` official results page | 2026-05-07 published | Company-distributed results page | Preserves quarter commentary on volume, price inflation, mix, tariffs, and cash generation | `[Disclosed]` | [2026-q1-results-prnewswire.html](/raw/company-ir/industrial-goods/industrial-supply/ww-grainger-inc/2026-q1-results-prnewswire.html) |
| GWW-T11 | `Q1 2026` Form `10-Q` | 2026-05-07 filed | Quarterly filing HTML | Provides the authoritative first-quarter filing support, financial statements, and segment tables | `[Filed]` | [2026-q1-10q.html](/raw/sec/industrial-goods/industrial-supply/ww-grainger-inc/2026-q1-10q.html) |
| GWW-T12 | `Q2 2026` results `8-K` | 2026-08-04 filed | Results filing HTML | Filed wrapper for the most recent reported quarter as of `2026-08-10` | `[Filed]` | [2026-q2-8k.html](/raw/sec/industrial-goods/industrial-supply/ww-grainger-inc/filings/2026-q2-8k.html) |
| GWW-T13 | `Q2 2026` official results page | 2026-08-04 published | Company-distributed results page | Preserves latest-quarter margin detail, tariff-refund effects, guidance raise, and capital-return cadence | `[Disclosed]` | [2026-q2-results-prnewswire.html](/raw/company-ir/industrial-goods/industrial-supply/ww-grainger-inc/2026-q2-results-prnewswire.html) |
| GWW-T14 | `Q2 2026` Form `10-Q` | 2026-08-04 filed | Quarterly filing HTML | Provides the authoritative latest-quarter filing support, segment results, and cash-flow detail | `[Filed]` | [2026-q2-10q.html](/raw/sec/industrial-goods/industrial-supply/ww-grainger-inc/2026-q2-10q.html) |

## Reconciliation notes

- The correct latest three reported quarters as of Monday, August 10, 2026 are `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports lags the required annual window, so the packet uses the `2025` SEC `10-K` as the authoritative annual baseline.
- The SEC `99.1` exhibit URLs were confirmed from the `8-K` wrappers, but the direct exhibit downloads returned SEC automated-tool challenge pages. The packet therefore relies on the official company-distributed quarter-result pages plus the `10-Q` filings for substantive quarter evidence.
- Grainger’s local lane assignment is `Industrial Supply`, even though AnnualReports currently labels the company `Industrial Equipment Wholesale`.

## Missing evidence

- No standalone earnings-call transcript artifact was saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No separate `2025` IR annual-report PDF artifact was preserved locally from the current IR page output; the annual baseline remains source-complete because the authoritative `10-K` is preserved locally.
