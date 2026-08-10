# Criteo Source Ledger

Ticker: `CRTO`  
CIK: `0001576427`  
Coverage window: `2025` annual report plus latest three reported quarters as of `2026-08-10`

## Source list

| ID | Type | Date | Source | File | Notes |
| --- | --- | --- | --- | --- | --- |
| `CRTO-S1` | AnnualReports company page | `2026-08-10` capture | AnnualReports | `raw/annualreports/services/advertising-agencies/criteo/company-page.html` | Confirms archive presence and taxonomy `Services / Advertising Agencies`. |
| `CRTO-S2` | AnnualReports verification note | `2026-08-10` | Internal verification | `raw/annualreports/services/advertising-agencies/criteo/annualreports-verification.md` | Documents AnnualReports lag and bridge to official `2025` sources. |
| `CRTO-S3` | IR home page | `2026-08-10` capture | Official company IR | `raw/company-ir/services/advertising-agencies/criteo/investor-home.html` | Confirms active investor site and latest-results surfacing. |
| `CRTO-S4` | IR SEC-filings page | `2026-08-10` capture | Official company IR | `raw/company-ir/services/advertising-agencies/criteo/sec-filings.html` | Confirms company-hosted filing chain. |
| `CRTO-S5` | Annual report PDF | `2026-02-26` filing / `2026-08-10` saved | Official company IR | `raw/company-ir/services/advertising-agencies/criteo/2025-annual-report.pdf` | Required `2025` annual report. |
| `CRTO-S6` | Q4 2025 earnings release | `2026-02-11` | Official company IR | `raw/company-ir/services/advertising-agencies/criteo/2025-q4-release.html` | Q4 and FY2025 operating discussion and guidance. |
| `CRTO-S7` | Q1 2026 earnings release | `2026-05-06` | Official company IR | `raw/company-ir/services/advertising-agencies/criteo/2026-q1-release.html` | Q1 2026 operating discussion and guidance. |
| `CRTO-S8` | Q2 2026 earnings release | `2026-08-05` | Official company IR | `raw/company-ir/services/advertising-agencies/criteo/2026-q2-release.html` | Latest reported quarter as of `2026-08-10`. |
| `CRTO-S9` | Official IR verification note | `2026-08-10` | Internal verification | `raw/company-ir/services/advertising-agencies/criteo/official-ir-verification.md` | Maps official annual and quarter chain. |
| `CRTO-S10` | SEC submissions JSON | `2026-08-10` capture | SEC | `raw/sec/services/advertising-agencies/criteo/submissions-cik0001576427.json` | Confirms issuer identity, ticker, and filing chronology. |
| `CRTO-S11` | Annual report filing | `2026-02-26` | SEC | `raw/sec/services/advertising-agencies/criteo/2025-10k.html` | Authoritative filed `10-K`. |
| `CRTO-S12` | Q4 2025 current report | `2026-02-11` | SEC | `raw/sec/services/advertising-agencies/criteo/2025-q4-8k.html` | Filed earnings exhibit support for Q4/FY2025. |
| `CRTO-S13` | Q1 2026 current report | `2026-05-06` | SEC | `raw/sec/services/advertising-agencies/criteo/2026-q1-8k.html` | Filed earnings exhibit support for Q1 2026. |
| `CRTO-S14` | Q1 2026 quarterly report | `2026-05-06` | SEC | `raw/sec/services/advertising-agencies/criteo/2026-q1-10q.html` | Authoritative quarter filing support. |
| `CRTO-S15` | Q2 2026 current report | `2026-08-05` | SEC | `raw/sec/services/advertising-agencies/criteo/2026-q2-8k.html` | Filed earnings exhibit support for Q2 2026. |
| `CRTO-S16` | Q2 2026 quarterly report | `2026-08-05` | SEC | `raw/sec/services/advertising-agencies/criteo/2026-q2-10q.html` | Authoritative latest-quarter filing support. |

## Collection note

- `raw/sec/services/advertising-agencies/criteo/submissions-cik0001619544.json` is a stray wrong-company artifact from an earlier fetch and is not part of the evidence chain.
