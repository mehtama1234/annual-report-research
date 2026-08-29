# Capital Flow KKR Global Atlantic Accordia Schedule D Parser Pass 1

## Purpose

This pass parses Accordia Q4 `2025` Schedule D pages `220-270` into raw CUSIP-level rows.

It asks:

`Can we move from Accordia legal-entity totals and Schedule D samples into a full named security row set for owned, acquired, disposed, and same-year acquisition/disposal securities?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-diagnostic-pass-1.csv`

## Short Answer

`Yes, at raw parser level. The pass creates 1968 CUSIP-level Schedule D rows: 994 owned issuer-credit rows, 92 owned ABS rows, 4 common-stock rows, 493 acquired rows, 275 disposed/redeemed rows, and 110 same-year acquired/disposed rows. This materially upgrades KKR/Global Atlantic from named samples to a full raw named-security universe, but still needs column reconciliation before cash/proceeds/return claims.`

## Parser Coverage

| Metric | Value |
|---|---:|
| Parsed Schedule D rows | 1968 |
| Owned issuer-credit rows | 994 |
| Owned ABS rows | 92 |
| Common-stock rows | 4 |
| Acquired rows | 493 |
| Disposed/redeemed rows | 275 |
| Same-year acquired/disposed rows | 110 |
| Rows with numeric tokens | 1934 |
| Rows with transaction dates | 1968 |
| Full named cash proof upgrades | 0 |

## First Rows

| ID | Schedule | Page | CUSIP | Issuer / Description | Type |
|---|---|---:|---|---|---|
| CFKKRGACEDP-0001 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 912810-RC-4 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0002 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 912810-TB-4 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0003 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 912810-TG-3 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0004 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 912810-TJ-7 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0005 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 912810-TW-8 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0006 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 912828-YB-0 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0007 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 91282C-FF-3 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0008 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 91282C-GM-7 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0009 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 91282C-PN-5 | UNITED STATES TREASURY | us_treasury |
| CFKKRGACEDP-0010 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 268317-AK-0 | ELECTRICITE DE FRANCE SA | utility_or_energy_credit |
| CFKKRGACEDP-0011 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 268317-AL-8 | ELECTRICITE DE FRANCE SA | utility_or_energy_credit |
| CFKKRGACEDP-0012 | Schedule D Part 1 Section 1 issuer-credit obligations owned | 218 | 13063A-7D-0 | CALIFORNIA ST | issuer_credit_or_corporate_bond |

## Proof Effect

This pass moves the KKR/Global Atlantic / Accordia case from compact legal-entity bridge to a raw named-security universe. It now shows the filing can be parsed into exact CUSIPs and issuer names across owned bonds/ABS, acquisitions, disposals/redemptions, and same-year round-trip securities.

## Boundary

This is still not final named cash proof.

The parser preserves raw numeric tokens but does not yet assign every number to final statutory columns such as actual cost, par, fair value, book value, consideration, realized gain/loss, interest income, or interest received. It also does not prove borrower receipt/use, liability-cost spread, funds-withheld waterfall, FHLB economics, collateral certificates, or return.

## Next Action

Run `accordia-schedule-d-column-reconciliation` by schedule part, then reconcile owned rows to the `7.318322163B USD` Schedule D bond base and disposal rows to cash-flow/income/proceeds fields.

## Decision

`kkr-global-atlantic-accordia-schedule-d-parser-raw-named-security-universe-visible-column-reconciliation-next`
