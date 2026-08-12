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
| KNF-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports company page | Confirms company identity and taxonomy | `[Reported]` | [company-page.html](/raw/annualreports/basic-materials/general-building-materials/knife-river-corporation/company-page.html) |
| KNF-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents the archive role of AnnualReports | `[Reported]` | [annualreports-verification.md](/raw/annualreports/basic-materials/general-building-materials/knife-river-corporation/annualreports-verification.md) |
| KNF-T3 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves the annual-report, quarter-result, presentation, and filing URLs | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/basic-materials/general-building-materials/knife-river-corporation/ir-source-links.md) |
| KNF-T4 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves the authoritative `10-K`, `10-Q`, and `8-K` references | `[Filed]` | [sec-source-links.md](/raw/sec/basic-materials/general-building-materials/knife-river-corporation/sec-source-links.md) |
| KNF-T5 | `2025` annual report PDF | 2026-08-10 collected | Annual report PDF | Provides annual strategy, positioning, and management framing | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/basic-materials/general-building-materials/knife-river-corporation/2025-annual-report.pdf) |
| KNF-T6 | `2025` Form `10-K` HTML | 2026-08-10 collected | Direct SEC annual filing HTML | Provides the authoritative annual filing | `[Filed]` | [2025-10k.html](/raw/sec/basic-materials/general-building-materials/knife-river-corporation/2025-10k.html) |
| KNF-T7 | `Q4 2025` earnings `8-K` HTML | 2026-08-10 collected | Direct SEC current report HTML | Provides fourth-quarter and full-year results and 2026 guide setup | `[Filed]` | [2025-q4-8k.html](/raw/sec/basic-materials/general-building-materials/knife-river-corporation/2025-q4-8k.html) |
| KNF-T8 | `Q4 2025` presentation PDF | 2026-08-10 collected | Investor presentation PDF | Adds backlog, pricing, and acquisition framing | `[Disclosed]` | [2025-q4-presentation.pdf](/raw/company-ir/basic-materials/general-building-materials/knife-river-corporation/2025-q4-presentation.pdf) |
| KNF-T9 | `Q1 2026` earnings `8-K` HTML | 2026-08-10 collected | Direct SEC current report HTML | Provides first-quarter results and management commentary | `[Filed]` | [2026-q1-8k.html](/raw/sec/basic-materials/general-building-materials/knife-river-corporation/2026-q1-8k.html) |
| KNF-T10 | `Q1 2026` Form `10-Q` HTML | 2026-08-10 collected | Direct SEC quarterly filing HTML | Provides the authoritative first-quarter filing | `[Filed]` | [2026-q1-10q.html](/raw/sec/basic-materials/general-building-materials/knife-river-corporation/2026-q1-10q.html) |
| KNF-T11 | `Q1 2026` presentation PDF | 2026-08-10 collected | Investor presentation PDF | Adds segment and seasonal framing for the first quarter | `[Disclosed]` | [2026-q1-presentation.pdf](/raw/company-ir/basic-materials/general-building-materials/knife-river-corporation/2026-q1-presentation.pdf) |
| KNF-T12 | `Q2 2026` earnings `8-K` HTML | 2026-08-10 collected | Direct SEC current report HTML | Provides the latest-quarter results and raised outlook | `[Filed]` | [2026-q2-8k.html](/raw/sec/basic-materials/general-building-materials/knife-river-corporation/2026-q2-8k.html) |
| KNF-T13 | `Q2 2026` Form `10-Q` HTML | 2026-08-10 collected | Direct SEC quarterly filing HTML | Provides the authoritative latest-quarter filing | `[Filed]` | [2026-q2-10q.html](/raw/sec/basic-materials/general-building-materials/knife-river-corporation/2026-q2-10q.html) |
| KNF-T14 | `Q2 2026` presentation PDF | 2026-08-10 collected | Investor presentation PDF | Adds backlog, pricing, leverage, and acquisition-capex framing | `[Disclosed]` | [2026-q2-presentation.pdf](/raw/company-ir/basic-materials/general-building-materials/knife-river-corporation/2026-q2-presentation.pdf) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- Knife River IR news/result pages were Cloudflare-challenged in the current shell environment, so the local quarter evidence stack relies on direct SEC `8-K` earnings filings, direct SEC `10-Q` filings, and locally saved presentation PDFs.
- This is still a source-complete packet for the target window because the company-hosted annual report and local SEC quarter set fully anchor the required annual and quarter evidence.

## Missing evidence

- No standalone earnings-call transcript artifact was saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- Knife River IR results-page HTML files were downloaded during exploration but returned Cloudflare challenge content, so they are not part of the staged evidence set.
