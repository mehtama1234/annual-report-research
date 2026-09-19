# URI Q-13 next-source package

Research date: `2026-09-18`

## Purpose

Q-13 tests whether United Rentals' asset-backed funding can be traced from
legal borrowing-base capacity to fleet purchases, collateral support,
repayment, and lifecycle return. The public record currently supports a
facility-level proxy, not a certificate-grade borrowing base or a complete
fleet cash-return bridge.

The machine-readable companion is the [Q-13 source-package CSV](data/capital-flow-uri-q13-next-source-package-2026-09-18.csv).

## Current proven perimeter

- The July 2025 Fifth Amended and Restated Credit Agreement establishes U.S.
  and Canadian borrowing-base formulas, eligible collateral categories,
  reserves, certificate cadence, and agent controls.
- The agreement names a Borrowing Base Certificate as Exhibit A and confirms
  that a May 31, 2025 certificate was delivered as a closing condition.
- Closing Combined Availability had to be at least `$1.000B`, but the filed
  exhibit does not include the populated certificate values.
- URI's Q2 2026 public disclosures report `$2.802B` of ABL capacity net of
  letters of credit and `$85M` of AR-securitization capacity, or `$2.887B` of
  facility-level availability. This reconciles to `$2.999B` total liquidity
  less `$112M` of cash.
- The same Q2 packet reports `$17.350B` rental-equipment net book value,
  `$23.8B` original equipment cost, and `$2.931B` of H1 gross rental capex.

These are legal-term, facility, and operating-scale controls. They do not
prove the live borrowing base, eligible collateral, NOLV, reserves, or a
purchase-level source of funds.

## Ranked acquisition requests

1. **Current quarter-end Borrowing Base Certificate.** Obtain the as-of date,
   U.S. and Canadian eligible equipment and inventory, NBV, NOLV, advance
   rates, reserves, letters of credit, outstandings, Combined Borrowing Base,
   Combined Availability, and Suppressed Availability.
2. **Equipment appraisal/NOLV schedule.** Join the eligible fleet population
   to appraisal dates, orderly liquidation values, exclusions, and advance
   rates.
3. **Reserve and ineligible-collateral schedule.** Reconcile gross collateral
   to net legal availability, including U.S./Canadian splits and agent
   adjustments.
4. **Fleet source-to-purchase ledger.** Match purchase date and fleet cohort
   to operating cash, ABL or AR draws, vendors/sellers, capitalization, later
   sale, and proceeds.
5. **Receivables-facility purchaser report.** Obtain eligible receivables,
   reserves, purchaser balance, availability, collections, dilution, fees,
   and remittance.

## Promotion rule

Q-13 can move beyond `evidence-insufficient` only when the source set joins:

```text
legal facility -> populated availability -> eligible collateral / NOLV / reserves
  -> funded draw -> named fleet purchase -> rental output / sale proceeds
  -> repayment and residual return
```

The `$2.887B` public availability proxy, the `$4.500B` stated ABL size, the
`$1.666B` ABL balance, fleet NBV, OEC, capex, operating cash flow, and covenant
compliance are not substitutes for that chain.

## Stop rule

Do not infer legal availability from stated facility size less reported debt,
assign ABL or AR capacity to specific fleet purchases, or calculate fleet ROIC
without growth-versus-replacement capex and asset-class output. Reopen this
route only for a populated certificate, collateral/appraisal report,
receivables purchaser report, purchase-level funds flow, or lifecycle
repayment/return schedule.

## Decision

`public-facility-availability-proxy-visible; certificate-and-lifecycle-return-unproven`

