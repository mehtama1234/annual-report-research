# Starbucks Corporation Official IR Verification

Date checked: 2026-08-09

Investor relations home:

- https://investor.starbucks.com/ir-home/default.aspx

Verified from Starbucks live investor pages and indexed official results pages:

- Financials pages expose:
  - Annual Reports
  - Quarterly Results and Supplemental Data
  - SEC Filings
- Financial releases pages expose:
  - `Starbucks Reports Q3 Fiscal Year 2026 Results`
  - `Starbucks Reports Q2 Fiscal Year 2026 Results`
  - `Starbucks Reports Q1 Fiscal Year 2026 Results`
  - `Starbucks Reports Q4 and Full Fiscal Year 2025 Results`

Official URLs verified:

- Annual reports page:
  - https://investor.starbucks.com/financials/annual-reports/default.aspx
- Official annual report PDF URL exposed on the SEC filing details page within the IR stack:
  - https://d18rn0p25nwr6d.cloudfront.net/CIK-0000829224/9b249159-6343-4dfb-8b07-8ba6dea60628.pdf
- Quarterly results page:
  - https://investor.starbucks.com/financials/quarterly-results-and-data/default.aspx
- Financial releases index:
  - https://investor.starbucks.com/news/financial-releases/default.aspx
- Q3 2026 results page:
  - https://investor.starbucks.com/news/financial-releases/news-details/2026/Starbucks-Reports-Q3-Fiscal-Year-2026-Results/default.aspx
- Q2 2026 results page:
  - https://investor.starbucks.com/news/financial-releases/news-details/2026/Starbucks-Reports-Q2-Fiscal-Year-2026-Results/default.aspx
- Q1 2026 results page:
  - https://investor.starbucks.com/news/financial-releases/news-details/2026/Starbucks-Reports-Q1-Fiscal-Year-2026-Results/default.aspx
- Q4 / full-year 2025 results page:
  - https://investor.starbucks.com/news/financial-releases/news-details/2025/Starbucks-Reports-Q4-and-Full-Fiscal-Year-2025-Results/default.aspx

Collection note:

- The official URLs above are verified from live investor pages and indexed official results pages.
- Direct shell fetches against the Starbucks IR host returned Cloudflare challenge HTML rather than evidence pages on `2026-08-09`.
- The annual report PDF itself was then collected successfully from the CloudFront document URL exposed by the live Starbucks SEC filing detail page and saved locally as [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/restaurants/starbucks-corporation/2025-annual-report.pdf).
- The Cloudflare challenge files from the main IR host were discarded and are not retained as source artifacts.
- The local evidence chain for this packet now includes both the official annual report PDF and the official SEC filing set for the annual report year and last three fiscal quarters in scope.

Interpretation:

- Starbucks has a current and internally consistent official IR chain for the fiscal `2025` annual package and the last three reported fiscal quarters in scope as of `2026-08-09`.
- The investor-relations stack confirms that the company is reporting through a `Q3 2026`, `Q2 2026`, `Q1 2026` quarterly sequence rather than a calendar-quarter convention.
- This company is directly relevant to the archive because it combines a large-scale consumer routine business, stored-value balances, loyalty mechanics, and a visible management turnaround program under the `Back to Starbucks` strategy.
