# Roku Source Ledger

Ticker: `ROKU`  
CIK: `0001428439`  
Coverage window: `2025` annual report plus latest three reported quarters as of `2026-08-10`

## Source list

| ID | Type | Date | Source | File | Notes |
| --- | --- | --- | --- | --- | --- |
| `ROKU-S1` | AnnualReports company page | `2026-08-10` capture | AnnualReports | `raw/annualreports/services/telecom-services-domestic/roku-inc/company-page.html` | Confirms archive presence, company description, and taxonomy `Services / Telecom Services - Domestic`. |
| `ROKU-S2` | AnnualReports verification note | `2026-08-10` | Internal verification | `raw/annualreports/services/telecom-services-domestic/roku-inc/annualreports-verification.md` | Documents AnnualReports lag at `2024` and frontier relevance. |
| `ROKU-S3` | IR home page | `2026-08-10` capture | Official company IR | `raw/company-ir/services/telecom-services-domestic/roku-inc/investor-home.html` | Confirms active investor site. |
| `ROKU-S4` | Quarterly-results page | `2026-08-10` capture | Official company IR | `raw/company-ir/services/telecom-services-domestic/roku-inc/quarterly-results.html` | Maps the Roku shareholder-letter chain used in the packet. |
| `ROKU-S5` | IR SEC-filings page | `2026-08-10` capture | Official company IR | `raw/company-ir/services/telecom-services-domestic/roku-inc/sec-filings.html` | Confirms company-hosted filing navigation. |
| `ROKU-S6` | Q4 2025 / FY2025 shareholder letter | `2026-02-12` / saved `2026-08-10` | Official company IR | `raw/company-ir/services/telecom-services-domestic/roku-inc/2025-q4-shareholder-letter.pdf` | Official quarterly-results chain support for FY2025 and Q4 2025. |
| `ROKU-S7` | Q1 2026 shareholder letter | `2026-04-30` / saved `2026-08-10` | Official company IR | `raw/company-ir/services/telecom-services-domestic/roku-inc/2026-q1-shareholder-letter.pdf` | Official quarterly-results chain support for Q1 2026. |
| `ROKU-S8` | Q2 2026 shareholder letter | `2026-08-06` / saved `2026-08-10` | Official company IR | `raw/company-ir/services/telecom-services-domestic/roku-inc/2026-q2-shareholder-letter.pdf` | Official latest-quarter support from Roku's image host. |
| `ROKU-S9` | Official IR verification note | `2026-08-10` | Internal verification | `raw/company-ir/services/telecom-services-domestic/roku-inc/official-ir-verification.md` | Maps official quarter chain and IR navigation. |
| `ROKU-S10` | SEC submissions JSON | `2026-08-10` capture | SEC | `raw/sec/services/telecom-services-domestic/roku-inc/submissions-cik0001428439.json` | Confirms issuer identity and filing chronology. |
| `ROKU-S11` | Annual report filing | `2026-02-13` | SEC | `raw/sec/services/telecom-services-domestic/roku-inc/2025-10k.html` | Authoritative filed `10-K` for FY2025. |
| `ROKU-S12` | Q4 2025 current report / shareholder-letter exhibit | `2026-02-12` | SEC | `raw/sec/services/telecom-services-domestic/roku-inc/2025-q4-ex99-1.html` | Filed earnings exhibit support for Q4 2025 and FY2025. |
| `ROKU-S13` | Q1 2026 quarterly report | `2026-05-01` | SEC | `raw/sec/services/telecom-services-domestic/roku-inc/2026-q1-10q.html` | Authoritative quarter filing support. |
| `ROKU-S14` | Q1 2026 current report / shareholder-letter exhibit | `2026-04-30` | SEC | `raw/sec/services/telecom-services-domestic/roku-inc/2026-q1-ex99-1.html` | Filed earnings exhibit support for Q1 2026. |
| `ROKU-S15` | Q2 2026 quarterly report | `2026-08-06` | SEC | `raw/sec/services/telecom-services-domestic/roku-inc/2026-q2-10q.html` | Authoritative latest-quarter filing support. |
| `ROKU-S16` | Q2 2026 current report / shareholder-letter exhibit | `2026-08-06` | SEC | `raw/sec/services/telecom-services-domestic/roku-inc/2026-q2-ex99-1.html` | Filed earnings exhibit support for Q2 2026. |

## Collection note

- An earlier local `2026-q2-ex99-1.html` fetch used a bad SEC object key and returned an XML `NoSuchKey` error. That file was replaced with the correct exhibit from accession `0001628280-26-054321`.
