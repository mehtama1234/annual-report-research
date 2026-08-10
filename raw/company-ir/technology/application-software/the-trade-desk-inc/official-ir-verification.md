# Official IR Verification

Date checked: 2026-08-10

## Official IR URLs

- Investor relations home: `https://investors.thetradedesk.com/`
- Annual reports: `https://investors.thetradedesk.com/financials/annual-reports/default.aspx`
- Quarterly results: `https://investors.thetradedesk.com/financials/quarterly-results/default.aspx`
- SEC filings: `https://investors.thetradedesk.com/financials/sec-filings/default.aspx`

## Local retrieval status

- Saved local captures of the investor-relations navigation pages are Cloudflare challenge pages with the title `Just a moment...`.
- The same challenge affected the saved annual-reports, quarterly-results, and SEC-filings navigation pages.
- Because of that access constraint, the local official IR HTML does not preserve the substantive page content even though the official URLs are known and valid.

## Annual and quarter chain used

- The required `2025` annual-report window is satisfied through the filed `2025` Form `10-K` dated `2026-02-27`, together with the official annual-reports URL above.
- The latest three reported quarters as of Monday, August 10, 2026 are supported by the official quarterly-results and SEC-filings URLs above plus the filed SEC artifacts:
  - `Q2 2026` reported `2026-08-06`
  - `Q1 2026` reported `2026-05-07`
  - `Q4 2025` / FY `2025` reported `2026-02-25`

## Why this still qualifies

- The official company IR chain is known and archived at the URL level.
- The authoritative financial and filing evidence is preserved locally through SEC submissions metadata, the filed `10-K`, filed `10-Q`s, filed `8-K`s, and earnings exhibits.
- That is sufficient to complete a defensible packet even though direct company-hosted IR HTML retrieval was blocked in this environment.
