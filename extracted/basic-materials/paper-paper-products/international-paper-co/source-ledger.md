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
| IP-T1 | AnnualReports company page | 2026-08-10 | AnnualReports company page | Confirms `Basic Materials / Paper & Paper Products` taxonomy and proves the aggregator was still lagging at `2024 Annual Report and Form 10K` instead of exposing the current `2025` package | `[Reported]` | [company-page.html](/raw/annualreports/basic-materials/paper-paper-products/international-paper-co/company-page.html) |
| IP-T2 | International Paper annual-report and proxy page | 2026-08-10 | Investor relations page | Confirms the official IR surface already exposed a `2025 Annual Report` entry despite the lagging AnnualReports page | `[Disclosed]` | [annual-report-proxy.html](/raw/company-ir/basic-materials/paper-paper-products/international-paper-co/annual-report-proxy.html) |
| IP-T3 | International Paper 2025 annual report PDF | 2026-03 | Annual report PDF | Official annual-report package saved locally from the IR chain | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/basic-materials/paper-paper-products/international-paper-co/2025-annual-report.pdf) |
| IP-T4 | SEC submissions JSON for International Paper | 2026-08-10 | SEC index JSON | Confirms the filing accession chain for the annual and trailing-quarter materials | `[Filed]` | [sec-submissions.json](/raw/sec/basic-materials/paper-paper-products/international-paper-co/sec-submissions.json) |
| IP-T5 | International Paper 2025 Form 10-K | 2026-02-27 | SEC filing HTML | Core annual SEC filing for the year ended `2025-12-31`; anchors the packaging-solutions reframing and the annual financial base | `[Filed]` | [2025-10k.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2025-10k.html) |
| IP-T6 | Q4 2025 and full-year 2025 earnings release | 2026-01-29 | Earnings release exhibit | Exact Q4 and full-year `2025` metrics, impairment and restructuring detail, and the planned separation framing | `[Disclosed]` | [2025-q4-earnings-release.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2025-q4-earnings-release.html) |
| IP-T7 | International Paper Q4 2025 earnings 8-K | 2026-01-29 | SEC filing HTML | Filing wrapper proving the `Q4 2025` and full-year `2025` earnings-release exhibit | `[Filed]` | [2025-q4-8k.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2025-q4-8k.html) |
| IP-T8 | Q1 2026 earnings release | 2026-04-30 | Earnings release exhibit | Exact `Q1 2026` metrics, box-volume and commercial commentary, sale-proceeds detail, and updated outlook | `[Disclosed]` | [2026-q1-earnings-release.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2026-q1-earnings-release.html) |
| IP-T9 | International Paper Q1 2026 earnings 8-K | 2026-04-30 | SEC filing HTML | Filing wrapper proving the `Q1 2026` earnings-release exhibit | `[Filed]` | [2026-q1-8k.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2026-q1-8k.html) |
| IP-T10 | International Paper Q1 2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Core quarterly SEC filing for the period ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2026-q1-10q.html) |
| IP-T11 | Q2 2026 earnings release | 2026-07-30 | Earnings release exhibit | Exact `Q2 2026` metrics, segment detail, Riverdale conversion commentary, NORPAC acquisition costs, and outlook | `[Disclosed]` | [2026-q2-earnings-release.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2026-q2-earnings-release.html) |
| IP-T12 | International Paper Q2 2026 earnings 8-K | 2026-07-30 | SEC filing HTML | Filing wrapper proving the `Q2 2026` earnings-release exhibit | `[Filed]` | [2026-q2-8k.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2026-q2-8k.html) |
| IP-T13 | International Paper Q2 2026 Form 10-Q | 2026-08-05 | SEC filing HTML | Core quarterly SEC filing for the period ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/raw/sec/basic-materials/paper-paper-products/international-paper-co/2026-q2-10q.html) |

## Reconciliation notes

- The correct trailing-quarter set as of Monday, `2026-08-10`, is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports is useful here for taxonomy confirmation and lag verification, but the authoritative annual evidence comes from the official IR annual-report page and SEC filing chain.
- The official annual-report PDF is saved locally, so this case is stronger than several other lagging-aggregator cases where only the SEC filing could be recovered.
- The quarterly evidence chain is clean: each in-scope quarter now has the earnings-release exhibit and the related SEC filing wrapper saved locally, and the two 2026 quarters also have the filed `10-Q` reports saved locally.

## Missing evidence

- No standalone verbatim earnings-call transcript artifacts were saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
