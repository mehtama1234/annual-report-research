# Source Ledger

Date baseline: 2026-08-10

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` SEC filing or filing-detail page
- `[Reported]` credible press or transcript provider
- `[Estimated]` derived or analyst estimate
- `[Speculative]` weak or unverified
- `[verify]` found but not yet confirmed directly

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| SON-T1 | AnnualReports.com Sonoco company page | 2026-08-10 | Aggregator page | Confirms `Consumer Goods / Packaging & Containers` classification and confirms AnnualReports was still lagging at `2024` instead of exposing the `2025` annual package | `[Reported]` | [company-page-annualreports.html](/raw/annualreports/consumer-goods/packaging-containers/sonoco-products-co/company-page-annualreports.html) |
| SON-T2 | SEC submissions JSON for Sonoco | 2026-08-10 | SEC index JSON | Confirms CIK, fiscal year-end, and the accession chain for the annual and trailing-quarter filings | `[Filed]` | [sec-submissions.json](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/sec-submissions.json) |
| SON-T3 | Sonoco 2025 Form 10-K HTML | 2026-02-26 | Annual filing HTML | Core annual filing for the year ended `2025-12-31`; anchors the structural packaging-platform description and annual financial results | `[Filed]` | [2025-10k.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/2025-10k.html) |
| SON-T4 | Q4 2025 and full-year 2025 earnings release | 2026-02-16 | Earnings release exhibit | Exact Q4 and full-year `2025` metrics plus initial `2026` guidance and packaging-platform simplification commentary | `[Disclosed]` | [2025-q4-earnings-release.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/2025-q4-earnings-release.html) |
| SON-T5 | Sonoco Q4 2025 earnings 8-K | 2026-02-17 | SEC filing HTML | Filing wrapper proving the earnings-release exhibit for Q4 `2025` and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/2025-q4-8k.html) |
| SON-T6 | Sonoco Q1 2026 earnings 8-K filing-detail page | 2026-04-21 | SEC filing-detail page | Confirms the correct Q1 `2026` earnings-release accession and exhibit path after an initially wrong local 8-K guess | `[Filed]` | [000009176726000019-index.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/000009176726000019-index.html) |
| SON-T7 | Q1 2026 earnings release | 2026-04-21 | Earnings release exhibit | Exact Q1 `2026` metrics, segment commentary, and updated `2026` guidance posture | `[Disclosed]` | [2026-q1-earnings-release.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/2026-q1-earnings-release.html) |
| SON-T8 | Sonoco Q1 2026 10-Q HTML | 2026-04-28 | Quarterly filing HTML | Filed quarter report for the period ended `2026-03-29` | `[Filed]` | [2026-q1-10q.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/2026-q1-10q.html) |
| SON-T9 | Sonoco Q2 2026 earnings 8-K filing-detail page | 2026-07-22 | SEC filing-detail page | Confirms the correct Q2 `2026` earnings-release accession and exhibit path | `[Filed]` | [000009176726000034-index.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/000009176726000034-index.html) |
| SON-T10 | Q2 2026 earnings release | 2026-07-22 | Earnings release exhibit | Exact Q2 `2026` metrics, record operating cash flow, and reaffirmed guidance posture | `[Disclosed]` | [2026-q2-earnings-release.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/2026-q2-earnings-release.html) |
| SON-T11 | Sonoco Q2 2026 10-Q HTML | 2026-07-28 | Quarterly filing HTML | Filed quarter report for the period ended `2026-06-28` | `[Filed]` | [2026-q2-10q.html](/raw/sec/consumer-goods/packaging-containers/sonoco-products-co/2026-q2-10q.html) |

## Reconciliation notes

- The correct trailing-quarter set as of Monday, `2026-08-10`, is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The local file originally saved as `2026-q1-10q.html` was a wrong guessed SEC archive filename and returned an XML `NoSuchKey` response. It has since been replaced with the correct `10-Q` document from accession `0000091767-26-000022`.
- The initially fetched `2026-q1-8k` filing wrapper at accession `0000091767-26-000024` was not the earnings release. The actual Q1 `2026` earnings release is accession `0000091767-26-000019`, confirmed through the filing-detail page.
- AnnualReports is useful here only for taxonomy confirmation and lag verification. The authoritative annual and quarter evidence comes from SEC-hosted filings and earnings-release exhibits.

## Missing evidence

- No standalone official annual-report PDF was collected locally because the saved AnnualReports page still lagged at `2024` and the investor-relations HTML captures were Cloudflare challenge pages rather than usable evidence.
- No standalone official earnings-call transcript artifacts were collected for Q4 `2025`, Q1 `2026`, or Q2 `2026`.
