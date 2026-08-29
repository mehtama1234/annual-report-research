# Capital Flow Collateral Availability Certificate Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-009`.

It asks:

`Can current local evidence prove that reported collateral, borrowing-base capacity, pledged assets, LTV cushion, or credit capacity is legally available and quantified?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-collateral-availability-certificate-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full collateral availability certificate upgrade yet. Matador and Liberty Broadband have partial legal/collateral-mechanics evidence: Matador has an agreement-grade borrowing-base reaffirmation and simple unused elected commitment; Liberty has pledged Charter-share collateral, disclosed collateral value, and LTV-trigger mechanics. United Rentals and KKR/Global Atlantic remain holds because current local evidence shows collateral support or pledged-asset context, not borrowing-base certificates, collateral reports, reserve reports, LTV certificates, or FHLB collateral files.`

## Row Outcomes

| Row | Case | Current Collateral / Availability Evidence | Availability Result | Remaining Gap |
|---|---|---|---|---|
| `CFCACSR-001` | United Rentals fleet | AR collateral-pool coverage above `100%` across extracted periods; Q2 `2026` AR collateral coverage of `125.8%`; ABL draw intensity of `37.0%`; recurring liquidity and fleet/cash-conversion context | Hold with collateral-support context | No ABL borrowing-base certificate, eligible-collateral schedule, advance rates, reserves, L/C treatment, covenant calculation, AR securitization eligibility schedule, or legal availability amount |
| `CFCACSR-002` | KKR / Global Atlantic channel | `9.2B USD` of FHLB funding-agreement pledged assets; `189.204380B USD` insurance investments; `48.754106B USD` mortgage and other loan receivables net; LTV bucket and allowance context | Hold with pledged-asset context | No statutory legal-entity collateral schedule, FHLB collateral file, pledged-asset eligibility, haircut, advance rate, borrowing capacity, legal availability calculation, or liability-cost bridge |
| `CFCACSR-003` | Matador borrowing base | Reserve-based Credit Agreement context; June `2026` borrowing-base reaffirmation; `3.25B USD` borrowing base; `2.75B USD` elected commitments; `939M USD` Credit Agreement borrowings; `53.8M USD` letters of credit; about `1.7572B USD` simple unused elected commitment after LCs; Collateral Coverage Minimum mechanics | Partial borrowing-base and availability proxy | No borrowing-base certificate, reserve report, lender commitment allocation, title/collateral schedule, covenant compliance certificate, availability calculation after reserves, borrowing notices, or asset-area collateral cash support |
| `CFCACSR-004` | Liberty Broadband holdco | `19.1M` Charter shares in collateral accounts; `2.7B USD` disclosed collateral-account value; `864M USD` Margin Loan Facility debt; simple `32.0%` margin-debt/disclosed-collateral ratio; `50%` LTV support trigger; `359M USD` Charter Loan Facility support | Partial pledged-share LTV mechanics proxy | No contractual LTV certificate, collateral haircut, margin-loan agreement definition proof, restricted-cash split, Charter loan full economics, final merger funds-flow, debt-close treatment, or shareholder realization |

## Decision

`collateral-availability-certificate-source-route-hold-with-partials`

`CFRMSWO-009` is executed against the current local source set. It produces two partial collateral/availability rows and two holds:

- Matador: partial borrowing-base and availability proxy.
- Liberty Broadband: partial pledged-share LTV mechanics proxy.
- United Rentals: hold below ABL/AR legal availability proof.
- KKR/Global Atlantic: hold below FHLB/statutory pledged-asset availability proof.

## Safe Claim

`The collateral availability certificate source-route pass confirms that selected rows have collateral, borrowing-base, pledged-asset, or LTV mechanics visible, but the current local evidence does not prove full legal availability, eligible collateral, advance rates, reserve deductions, covenant cushion, FHLB collateral availability, or final collateral-backed payback across the affected rows.`

## Next Work

1. For United Rentals, pull ABL borrowing-base certificates, eligible-collateral schedules, advance rates, reserves, L/C treatment, covenant calculations, and AR securitization eligibility reports.
2. For KKR/Global Atlantic, pull FHLB collateral files, statutory legal-entity pledged-asset schedules, haircut/advance-rate support, funding-agreement liability terms, and Schedule D/BA collateral detail.
3. For Matador, pull borrowing-base redetermination packages, reserve reports, lender commitment schedules, title/collateral schedules, covenant certificates, borrowing notices, and availability calculations after reserves.
4. For Liberty Broadband, pull LTV certificates, margin-loan agreement definitions, collateral haircut schedules, Charter Loan Facility terms, restricted-cash rollforwards, and final merger/debt treatment.
5. Move next to `CFRMSWO-010` retainage, receivable aging, and working-capital collection.
