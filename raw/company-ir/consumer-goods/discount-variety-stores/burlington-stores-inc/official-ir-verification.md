# Burlington Stores, Inc. Official IR Verification

Date checked: 2026-08-09

Official investor-relations pages verified:

- Investor landing page: https://www.burlingtoninvestors.com/
- Annual reports page: https://www.burlingtoninvestors.com/financial-information/annual-reports
- Quarterly results page: https://www.burlingtoninvestors.com/financial-information/quarterly-results

Verified annual-report chain:

- `2025` annual reports landing page entry is exposed through the official annual-reports page.
- The local annual-report PDF was collected from the SEC-hosted annual-report-to-security-holders filing because direct shell fetches to the Burlington IR site repeatedly timed out or failed with HTTP transport errors in this environment.

Verified quarter window in scope as of `2026-08-09`:

- `Q1 2026` official result page: https://www.burlingtoninvestors.com/news-releases/news-release-details/burlington-stores-reports-strong-first-quarter-sales-and/
  - headline metrics verified from live search coverage: total sales increased `14%`, comparable store sales increased `6%`, net income was `$115 million`, and diluted EPS was `$1.80`
- `Q4 2025` official result page: https://www.burlingtoninvestors.com/news-releases/news-release-details/burlington-stores-inc-reports-fourth-quarter-and-full-year-2025/
  - headline metrics verified from live search coverage: Q4 total sales grew `11%`, comparable store sales increased `4%`, Q4 net income was `$310 million`, diluted EPS was `$4.84`, FY25 total sales grew `9%`, and FY25 net income was `$610 million`
- `Q3 2025` official result page: https://www.burlingtoninvestors.com/news-releases/news-release-details/burlington-stores-inc-reports-third-quarter-2025-earnings/
  - headline metrics verified from live search coverage: total sales grew `7%`, comparable store sales increased `1%`, net income was `$105 million`, diluted EPS was `$1.63`, and adjusted EPS was `$1.80`

Reproducible collection issue:

- As of `2026-08-09`, direct shell requests to the Burlington IR site repeatedly failed in this environment:
  - plain `curl` returned HTTP/2 stream close errors
  - `curl --http1.1` timed out after connect without returning page content
- Because of that, the archive currently relies on the complete SEC filing chain plus live search-verified official IR URLs and snippets for the quarter-result layer.
