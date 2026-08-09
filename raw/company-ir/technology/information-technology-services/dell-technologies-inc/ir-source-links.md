# Dell Technologies Inc. Investor Relations Source Links

## Official IR entry points

- IR home:
  - https://investors.delltechnologies.com/
- Quarterly results page:
  - https://investors.delltechnologies.com/financial-information/quarterly-results
- SEC filings page:
  - https://investors.delltechnologies.com/financial-information/sec-filings

## In-scope result pages

- FY2025 annual report PDF (`ARS` filing dated 2025-05-16):
  - https://www.sec.gov/Archives/edgar/data/1571996/000119312525121713/d836850dars.pdf

- FY2027 Q1 results reported 2026-05-28:
  - https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-first-quarter-fiscal-2027-financial
- FY2026 Q4 / full-year FY2026 results reported 2026-02-26:
  - https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-fourth-quarter-and-full-year-fiscal-3
- FY2026 Q3 results reported 2025-11-25:
  - https://investors.delltechnologies.com/news-releases/news-release-details/dell-technologies-delivers-third-quarter-fiscal-2026-financial
- FY2025 annual filing page:
  - https://investors.delltechnologies.com/sec-filings/sec-filing/10-k/0001571996-25-000034

## Archive note

- Dell-hosted static-file PDF downloads timed out repeatedly from the shell on 2026-08-09.
- The local archive therefore relies on:
  - verified IR page URLs above, and
  - locally saved SEC filing HTML artifacts under `raw/sec/.../dell-technologies-inc/`
- Direct SEC shell fetches for the `2025` annual-report PDF returned the SEC undeclared-automation block page instead of the PDF.
- The temporary blocked-response file that had been saved locally as `2025-annual-report.pdf` was removed from the workspace on `2026-08-09` because it was not a valid PDF artifact.
