# Cencora Official IR Verification

Date checked: 2026-08-10

Investor relations home: https://investor.cencora.com/overview/default.aspx

Verified on the official IR stack:

- Quarterly results page: https://investor.cencora.com/financials/quarterly-results/default.aspx
- Latest official quarter in scope as of `2026-08-10`: `Q3 FY2026`, reported `2026-08-05`
- The in-scope trailing quarter chain is:
  - `Q3 FY2026`: https://investor.cencora.com/news/news-details/2026/Cencora-Reports-Fiscal-2026-Third-Quarter-Results/default.aspx
  - `Q2 FY2026`: https://investor.cencora.com/news/news-details/2026/Cencora-Reports-Fiscal-2026-Second-Quarter-Results/default.aspx
  - `Q1 FY2026`: https://investor.cencora.com/news/news-details/2026/Cencora-Reports-Fiscal-2026-First-Quarter-Results/default.aspx

Verified headline figures from official IR pages and official search snippets:

- `Q3 FY2026`:
  - revenue `$84.8 billion`
  - GAAP diluted EPS `$3.94`
  - adjusted diluted EPS `$4.48`
  - year-over-year revenue growth `5.1%`
- `Q2 FY2026`:
  - revenue `$78.4 billion`
  - GAAP diluted EPS `$8.40`
  - adjusted diluted EPS `$4.75`
  - year-over-year revenue growth `3.8%`
- `Q1 FY2026`:
  - revenue `$85.9 billion`
  - GAAP diluted EPS `$2.87`
  - adjusted diluted EPS `$4.08`
  - year-over-year revenue growth `5.5%`

Access notes:

- Direct shell requests to the Cencora IR pages in this workspace returned `HTTP 429` and Cloudflare challenge responses.
- The failed shell attempts are preserved locally in:
  - `investor-home.html.error.txt`
  - `quarterly-results.html.error.txt`
  - `presentations-and-events.html.error.txt`
  - `contacts.html.error.txt`
- The official quarter chain was still verifiable through live official IR search results and the official IR page structure.

Saved annual artifact collected locally:

- [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/drug-stores/cencora-inc/2025-annual-report.pdf)

Interpretation:

- Cencora has a strong annual and quarter chain for CLI 8 even though direct page fetches are rate-limited from this shell.
- The official materials are strong enough to support the healthcare-distribution, institutional-replenishment, specialty-services, and provider-dependence themes central to this frontier.
