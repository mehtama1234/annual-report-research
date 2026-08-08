# Pilot Companies

Date baseline: 2026-08-08

This is the first seeded company universe for the `2025 annual report` + `2026 / late-2025 quarterly` collection window.

## Pilot set

| Sector | Industry | Company | Ticker | AnnualReports.com | Official IR | Target quarter window | Notes |
|---|---|---|---|---|---|---|---|
| Technology | Consumer Services | Apple Inc. | AAPL | https://www.annualreports.com/Company/apple-inc | https://investor.apple.com/investor-relations/default.aspx | FY2026 Q3 / FY2026 Q2 / FY2026 Q1 | AnnualReports currently shows `2025` annual report and Form `10-K`. |
| Technology | Application Software | Microsoft Corporation | MSFT | https://www.annualreports.com/Company/microsoft-corporation | https://www.microsoft.com/en-us/investor/default | FY2026 Q4 / FY2026 Q3 / FY2026 Q2 | AnnualReports currently shows `2024` annual report; collect `2025` annual from Microsoft IR. |
| Financial | Money Center Banks | JPMorgan Chase & Co. | JPM | https://www.annualreports.com/Company/jpmorgan-chase-co | https://www.jpmorganchase.com/ir | 2Q26 / 1Q26 / 4Q25 | JPM IR directly exposes `2025` annual report, `2Q26` press release, transcript, and `10-Q`. |
| Financial | Money Center Banks | Bank of America Corporation | BAC | https://www.annualreports.com/Company/bank-of-america-corporation | https://investor.bankofamerica.com/ | 2Q26 / 1Q26 / 4Q25 | AnnualReports currently shows `2025` annual report and Form `10-K`. |
| Consumer Goods | Personal Products | Procter & Gamble Co. | PG | https://www.annualreports.com/Company/procter-gamble-co | https://www.pginvestor.com/financials/annual-reports/default.aspx | FY2026 Q4 / FY2026 Q3 / FY2026 Q2 | AnnualReports currently shows `2024`; official P&G IR exposes `2025` annual report and Form `10-K`. |
| Consumer Goods | Processed & Packaged Goods | PepsiCo Inc. | PEP | https://www.annualreports.com/Company/pepsico-inc | https://investors.pepsico.com/investors/earnings/index.html | Q2 2026 / Q1 2026 / Q4 2025 | PepsiCo earnings page cleanly exposes the full in-scope quarterly set. |
| Healthcare | Managed Health Care | UnitedHealth Group Incorporated | UNH | https://www.annualreports.com/Company/unitedhealth-group-inc | https://www.unitedhealthgroup.com/investors/financial-reports.html | Q2 2026 / Q1 2026 / Q4 2025 | UnitedHealth IR exposes `2025` annual `10-K` and the in-scope quarterly materials. |
| Healthcare | Drug Manufacturers - General | Pfizer Inc. | PFE | https://www.annualreports.com/Company/pfizer-inc | https://investors.pfizer.com/overview/default.aspx | Q2 2026 / Q1 2026 / Q4 2025 | Pfizer IR and AnnualReports were both verified. |
| Industrial Goods | Construction & Farm Machinery | Caterpillar Inc. | CAT | https://www.annualreports.com/Company/caterpillar-inc | https://www.caterpillar.com/en/investors/reports.html | Q2 2026 / Q1 2026 / Q4 2025 | AnnualReports and Caterpillar IR both expose `2025` annual materials. |
| Industrial Goods | Aerospace/Defense Products & Services | Honeywell International Inc. | HON | https://www.annualreports.com/Company/honeywell-international-inc | https://investor.honeywell.com/investor-relations | Q2 2026 / Q1 2026 / Q4 2025 | AnnualReports currently shows `2024`; use Honeywell IR for `2025` annual and in-scope quarterlies. |

## Source verification notes

- AnnualReports company page verification was done on `2026-08-08`.
- Official investor-relations page verification was done on `2026-08-08`.
- Several AnnualReports pages lag the newest annual report year; where that happened, the official investor-relations page is the source of truth for `2025` annual materials.

## Next collection pass

For each company:

1. Save the AnnualReports.com company page or relevant annual-report links into `raw/annualreports/...`
2. Save the official `2025` annual report and annual filing into `raw/company-ir/...` and `raw/sec/...`
3. Save the three in-scope quarterlies into `raw/company-ir/...`, `raw/sec/...`, and `raw/earnings-calls/...`
4. Fill the matching files under `extracted/...`
