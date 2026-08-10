# ONE Gas Official IR Verification

- Investor relations root: `https://www.onegas.com/investors/default.aspx`
- Official annual-reports page verified in browser on `2026-08-10`: `https://www.onegas.com/investors/financials-and-filings/annual-reports/default.aspx`
- Official SEC-filings page verified in browser on `2026-08-10`: `https://www.onegas.com/investors/financials-and-filings/sec-filings/default.aspx`
- Official quarterly-results page verified in browser on `2026-08-10`: `https://www.onegas.com/investors/financials-and-filings/quarterly-results/default.aspx`
- Saved local captures of those three pages exist, but they are Cloudflare challenge pages in this environment rather than substantive HTML:
  - `raw/company-ir/utilities/gas-utilities/one-gas-inc/annual-reports.html`
  - `raw/company-ir/utilities/gas-utilities/one-gas-inc/sec-filings.html`
  - `raw/company-ir/utilities/gas-utilities/one-gas-inc/quarterly-results.html`

## Required reported-quarter chain as of 2026-08-10

- Q2 2026 results release verified in browser:
  - URL: `https://www.onegas.com/news/press-release-details/2026/ONE-Gas-Announces-Second-Quarter-2026-Financial-Results-Raises-2026-Adjusted-Earnings-Expectations-to-Upper-Half-of-Financial-Guidance-Ranges/default.aspx`
  - local capture: `raw/company-ir/utilities/gas-utilities/one-gas-inc/2026-q2-release.html` (`Cloudflare challenge page locally; browser verification used for content`)
- Q1 2026 results release verified in browser:
  - URL: `https://www.onegas.com/news/press-release-details/2026/ONE-Gas-Announces-First-Quarter-2026-Financial-Results-Affirms-2026-Financial-Guidance/default.aspx`
  - local capture: `raw/company-ir/utilities/gas-utilities/one-gas-inc/2026-q1-release.html` (`Cloudflare challenge page locally; browser verification used for content`)
- Q4 2025 / FY2025 results release verified in browser:
  - URL: `https://www.onegas.com/news/press-release-details/2026/ONE-Gas-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results-Releases-Non-GAAP-Adjusted-Financial-Guidance/default.aspx`
  - local capture: `raw/company-ir/utilities/gas-utilities/one-gas-inc/2025-q4-release.html` (`Cloudflare challenge page locally; browser verification used for content`)

## Notes

- Browser verification on `2026-08-10` confirmed that the official annual-reports page lists a `2025` annual report.
- Browser verification on `2026-08-10` also confirmed the official Q4 `2025`, Q1 `2026`, and Q2 `2026` release pages and the official guidance page.
- SEC support is used as the local authoritative filing backstop because direct local IR captures were challenge-gated.
