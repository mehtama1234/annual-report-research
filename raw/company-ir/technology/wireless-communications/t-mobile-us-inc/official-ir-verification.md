# T-Mobile US, Inc. Official IR Verification

Date: 2026-08-10

Official IR surfaces verified:

- annual reports page: `https://investor.t-mobile.com/financials/annual-reports/default.aspx`
- quarterly results index: `https://investor.t-mobile.com/financials/quarterly-results/default.aspx`
- Q2 2026 earnings event page: `https://investor.t-mobile.com/events-and-presentations/events/event-details/2026/T-Mobile-Q2-2026-Earnings-Call-2026-jCV4ySQyqd/default.aspx`
- SEC filings page: `https://investor.t-mobile.com/financials/sec-filings/default.aspx`

Annual-report IR confirmation:

- The saved annual-reports page title is `T-Mobile - Financials - Annual Reports`.
- The saved page header contains `Annual Reports`.
- Search confirmation against the live IR surface on `2026-08-10` established that the page exposed `2025 Annual Report` and `2026 Proxy Statement`.

Quarter-window IR confirmation as of Monday, August 10, 2026:

- The saved quarterly-results page header contains `Latest Quarterly Results`.
- The saved page exposes the official materials structure for `Earnings Release`, `Form 10-Q/10-K`, and `Transcript`.
- Search confirmation against the live IR surface on `2026-08-10` established that the latest reported period shown on the quarterly-results page was `Q2 2026`.
- The official earnings-event page for Q2 `2026` is dated `July 23, 2026`.
- That means T-Mobile had already reported Q2 `2026` by the archive baseline on `2026-08-10`.
- The latest three reported quarters in scope are therefore:
  - Q2 `2026`
  - Q1 `2026`
  - Q4 `2025`

Collection note:

- Local IR HTML captures preserve the official annual and quarterly navigation chain:
  - [annual-reports-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/wireless-communications/t-mobile-us-inc/annual-reports-page.html)
  - [quarterly-results-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/wireless-communications/t-mobile-us-inc/quarterly-results-page.html)
- In this environment, the saved IR HTML is stronger for confirming page identity and materials structure than for preserving every rendered document tile, so the authoritative annual-plus-quarter chain is anchored by the official IR URLs and the underlying SEC filings.

Working conclusion:

- T-Mobile has a clean official IR chain for the `2025` annual package and the in-scope quarter sequence.
- The packet can be treated as complete because the official IR timing chain and the underlying SEC `10-K`, `ARS`, `8-K`, `10-Q`, and `99.1` earnings exhibits are all preserved locally.
