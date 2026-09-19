# Capital Flow URI ABL Public-Disclosure Proxy Bridge Pass 1

## Purpose

This pass answers the next narrow URI question:

`If the live borrowing-base certificate is not public, what can public Q2 2026 disclosures still tell us without overstating them?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-abl-public-disclosure-proxy-bridge-pass-1.csv`

## Source Boundary

This is not a live borrowing-base certificate.

It uses public disclosures only:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-ex99-earnings-release.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-06-18-ex10-1-receivables-purchase-amendment.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-07-11-tm2520569d1_ex10-1.htm`

## Public Inputs

| Metric | Value | Source |
|---|---:|---|
| Cash and cash equivalents | `112M USD` | Q2 `2026` 10-Q balance sheet. |
| Total liquidity | `2.999B USD` | Q2 `2026` earnings release and 10-Q liquidity language. |
| ABL stated facility size | `4.500B USD` | Q2 `2026` 10-Q debt table. |
| ABL balance | `1.666B USD` | Q2 `2026` 10-Q debt table. |
| AR securitization purchase limit | `1.500B USD` | June `2026` receivables amendment. |
| AR securitization balance | `1.414B USD` | Q2 `2026` 10-Q debt table. |
| AR receivables collateral pool net of reserves/deductions | `1.779B USD` | Q2 `2026` 10-Q debt note. |
| ABL borrowing capacity net of letters of credit | `2.802B USD` | Q2 `2026` 10-Q debt note. |
| AR securitization borrowing capacity | `85M USD` | Q2 `2026` 10-Q debt note. |
| Rental equipment net book value | `17.350B USD` | Q2 `2026` 10-Q balance sheet. |
| OEC | `23.8B USD` | Q2 `2026` earnings release. |
| H1 gross rental capex | `2.931B USD` | Q2 `2026` earnings release. |
| H1 operating cash flow / gross rental capex | `112.8%` | Existing source-backed derived row. |

## Proxy Bridge

| Bridge | Calculation | Result |
|---|---|---:|
| Filed ABL plus AR facility availability | `2.802B + 85M` | `2.887B USD` |
| Reconciliation to total liquidity less cash | `2.999B - 112M` | `2.887B USD` |
| Gross unused ABL stated capacity before constraints | `4.500B - 1.666B` | `2.834B USD` |
| Gross unused AR purchase-limit capacity before constraints | `1.500B - 1.414B` | `86M USD` |
| Gross unused ABL plus AR stated capacity before constraints | `2.834B + 86M` | `2.920B USD` |
| Gap between gross unused stated capacity and implied facility availability | `2.920B - 2.887B` | `33M USD` |
| Facility availability as share of total liquidity | `2.887B / 2.999B` | `96.3%` |
| Cash as share of total liquidity | `112M / 2.999B` | `3.7%` |
| Rental equipment net book value / ABL stated size | `17.350B / 4.500B` | `385.6%` |
| OEC / ABL stated size | `23.8B / 4.500B` | `528.9%` |
| H1 gross rental capex / implied facility availability | `2.931B / 2.887B` | `101.5%` |

## Covenant Status

The Q2 `2026` 10-Q says URI was in compliance with the ABL, AR securitization, term loan, and senior-note covenants.

It also says the ABL fixed-charge coverage covenant applies only if specified availability falls below `10%` of the maximum revolver amount for five consecutive business days, subject to exceptions.

At June `30`, `2026`, specified availability exceeded the required threshold, so the financial covenant was inapplicable.

Using the stated `4.500B USD` facility size, a `10%` orientation threshold is about `450M USD`. That is only an orientation calculation because the agreement uses defined terms.

## What This Adds

This moves the public URI ABL work from:

`certificate-field-map-visible`

to:

`public-facility-availability-visible`

It still does not make URI borrowing-base-grade.

## September 17 public-source recheck

The current SEC Q2 2026 10-Q was rechecked for a populated certificate,
eligibility schedule, NOLV/appraisal, reserve schedule, or lender collateral
report. It repeats the facility-level availability and covenant-status
observations above, but no certificate components or source-to-purchase ledger
were located. The recheck therefore confirms the move-on boundary: Q-13 remains
`evidence-insufficient`, and `2.887B USD` remains a public availability proxy,
not legal Combined Availability or lifecycle-return proof.

The bridge is useful because it constrains the numbers:

- disclosed total liquidity was not mostly cash
- filed facility availability was `2.802B USD` for ABL plus `85M USD` for AR
  securitization, or `2.887B USD` in total
- gross unused stated ABL plus AR capacity was about `2.920B USD`
- the gap is small enough that public disclosures are directionally consistent
- the filing says URI was above the springing-covenant availability threshold

## Safe Claim

`Public Q2 2026 disclosures report 2.802B USD of ABL borrowing capacity net of letters of credit and 85M USD of AR securitization capacity, totaling 2.887B USD. That total reconciles to 2.999B USD of liquidity less 112M USD of cash. It is facility-level availability, not a populated borrowing-base certificate or proof of eligible equipment, NOLV, reserves, or live Combined Availability components.`

## Claims Not To Make Yet

Do not say:

- `2.887B USD` is legal ABL availability
- `2.834B USD` is legal ABL availability
- the borrowing base is known
- eligible rental-equipment NBV or NOLV is known
- reserves are known
- L/C usage is known
- all OEC is eligible collateral
- facilities funded specific fleet purchases

## Next Concrete Work

The next URI evidence gates are:

1. Find rating-agency or lender commentary that cites ABL collateral coverage, utilization, or availability.
2. Find any borrowing-base certificate, collateral report, or availability schedule.
3. Reconcile Q2 `2026` ABL and AR facility availability if later filings split the total liquidity components.
4. Upgrade the new fleet-return/utilization proxy into a true fleet-economics bridge by finding owned-equipment rental revenue, rate/time/mix split, growth-versus-replacement capex, and segment or asset-class OEC.
