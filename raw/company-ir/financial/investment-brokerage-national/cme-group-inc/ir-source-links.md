# CME Group IR Source Links

Date verified: 2026-08-08

## Primary IR pages

- Investor relations home: https://www.cmegroup.com/investor-relations.html
- Financial information hub: https://www.cmegroup.com/investor-relations/financial-information.html
- Quarterly statements page: https://www.cmegroup.com/investor-relations/financial-information/quarterly-statements.html
- AnnualReports.com company page: https://www.annualreports.com/Company/cme-group-inc
- Q1 2026 earnings event page: https://investor.cmegroup.com/events/event-details/cme-group-inc-first-quarter-2026-earnings-conference-call
- Q2 2026 earnings event page: https://investor.cmegroup.com/events/event-details/cme-group-inc-second-quarter-2026-earnings-conference-call
- 4Q25 / FY2025 release PDF: https://cmegroupinc.gcs-web.com/node/54901/pdf

## Verified annual-report links

- FY2025 annual report PDF on AnnualReports.com:
  - https://www.annualreports.com/Click/26823
- FY2025 annual report PDF on SEC (`ARS` filing dated 2026-03-23):
  - https://www.sec.gov/Archives/edgar/data/1156375/000162828026020510/ars_2026.pdf

## Verified quarter-material links observed on official pages

- Q1 2026 earnings press release PDF: https://investor.cmegroup.com/static-files/fa9991f8-5049-4205-aac2-4ce5dba85daf
- Q2 2026 earnings press release PDF: https://investor.cmegroup.com/static-files/88654e47-66b8-4a4a-8093-cc60ddeb103e
- Q1 2026 page also lists income statement trends, quarterly commentary, and earnings-call introduction files.
- Q2 2026 page also lists income statement trends, quarterly commentary, and earnings-call introduction files.

## Local collection status

- The SEC filing chain for `2025` annual, `4Q25`, `1Q26`, and `2Q26` is saved locally under `raw/sec/...`.
- Direct shell fetches to several CME IR static-file and event-page endpoints returned incomplete placeholder HTML during this pass, so some official quarter files are URL-verified but not yet saved locally.
- A direct SEC shell fetch for the `2025` annual-report PDF succeeded on `2026-08-09` once the request used a declared research user agent.
- The valid local artifact is now saved as:
  - [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/investment-brokerage-national/cme-group-inc/2025-annual-report.pdf)
