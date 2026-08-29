# Capital Flow Matador Source-Specific Use Allocation Pass 1

## Purpose

This page executes the first Matador row from the debt/refinancing bridge upgrade queue:

`Can Matador's Q2 2026 borrowing-base bridge be upgraded from source/use/output/cash visibility to source-to-specific-use allocation?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-matador-source-specific-use-allocation-pass-1.csv`

The queue row is:

`/cluster/capital-flow-debt-refinancing-bridge-upgrade-queue-pass-1.md`

The upstream Matador bridge is:

`/cluster/capital-flow-matador-borrowing-base-use-return-bridge-pass-1.md`

## Current Answer

`Matador can be upgraded to aggregate timing source/use reconciliation visible, but not to source-specific allocation. The first-half 2026 cash-flow statement reconciles cleanly: 1.407674B USD of operating cash flow plus 661.672M USD of net financing equals 2.069346B USD, which matches 2.057908B USD of net investing use plus an 11.438M USD cash/restricted-cash increase. The source side includes 541.0M USD of net Credit Agreement borrowings, 28.0M USD of net San Mateo borrowings, and 227.421M USD of net senior-note funding after issuance costs and note purchases. The use side includes 745.343M USD of development capex, 1.228834B USD of oil-and-gas property acquisitions, 37.604M USD for Cardinal, 38.697M USD of midstream capex, 6.200M USD of midstream asset acquisitions, and 2.088M USD of other property/equipment. This proves an aggregate source/use envelope, not draw-by-draw allocation to a specific acquisition, well program, or debt retirement.`

## Reconciliation

| Step | Amount | Meaning |
|---|---:|---|
| Operating cash flow | `1.407674B USD` | Company-level internal cash source. |
| Net financing cash | `661.672M USD` | Aggregate external financing source after draws, repayments, note issuance, note purchase, costs, dividends, buybacks, and distributions. |
| Total visible source envelope | `2.069346B USD` | OCF plus net financing. |
| Net investing use | `2.057908B USD` | Development capex, oil-and-gas acquisitions, Cardinal, midstream capex/assets, other property/equipment, net of asset-sale proceeds. |
| Cash/restricted cash increase | `11.438M USD` | Difference between sources and investing use. |
| Reconciliation result | `2.069346B USD` | Net investing plus cash increase equals OCF plus net financing. |

## What Improved

| Area | Prior Bridge | This Pass |
|---|---|---|
| Source side | Gross Credit Agreement draws, repayments, senior note proceeds, and OCF were visible. | Net source envelope is reconciled: OCF plus net financing equals investing use plus cash increase. |
| Use side | Capex, acquisitions, and note purchases were visible as separate facts. | Use envelope is decomposed and tied to the same-period cash-flow statement. |
| Facility context | Borrowing base and commitment increase were agreement-grade. | Facility headroom is calculated: about `1.7572B USD` simple unused elected commitment after borrowings and letters of credit. |
| Acquisition context | Oil-and-gas property acquisitions were visible. | The largest named use is identified: the May `2026` BLM Acquisition of `5,154` net undeveloped acres for about `1.16B USD`. |

## Decision

`aggregate-timing-source-use-reconciliation-visible`

This is an upgrade from:

`source-use-output-cash-bridge-visible-borrowing-base-level`

It does not reach:

`source-specific-use-allocation-visible`

The pass test from the queue required draws, note proceeds, repayments, capex, and acquisitions to be reconciled by amount and timing. The amount-level reconciliation passes at first-half aggregate level. The timing remains period-level, not transaction-level.

## Remaining Gap

| Gap | Why It Matters | Next Source |
|---|---|---|
| Borrowing notices | Needed to assign individual Credit Agreement draws or repayments to specific dates and uses. | Bank borrowing notices and daily revolver rollforward. |
| BLM Acquisition closing statement | Needed to prove whether the `1.16B USD` cash use came from OCF, revolver draws, note proceeds, or cash balances. | Closing statement and treasury funds-flow. |
| Senior-note use of proceeds | Needed to decide whether the `750M USD` note issuance funded acquisition, revolver repayment, note purchase, or general corporate purposes. | Offering memorandum, 8-K, indenture, and use-of-proceeds language. |
| Note purchase economics | Needed to determine whether the `509.670M USD` note purchase improved debt-service quality. | Tender/redemption terms and extinguishment accounting. |
| Asset contribution | Needed to convert acquisition/capex spend into output and cash return. | Asset-area production, LOE, realized price, EBITDA, OCF, reserves, and well results. |

## Safe Claim

`Matador's first-half 2026 filing now supports aggregate timing source/use reconciliation: 1.407674B USD of operating cash flow plus 661.672M USD of net financing equals 2.069346B USD, matching 2.057908B USD of net investing use plus an 11.438M USD cash/restricted-cash increase. The visible sources include net Credit Agreement borrowings, net San Mateo borrowings, and net senior-note funding; the visible uses include development capex, oil-and-gas property acquisitions, Cardinal, midstream capex, and other property/equipment. This does not prove that any specific borrowing or note proceeds funded a specific acquisition, well program, or debt retirement, and it does not prove asset-level return.`

## Next Work

1. Pull senior-note offering and use-of-proceeds documents.
2. Search for the BLM Acquisition closing statement and payment/funds-flow detail.
3. Find borrowing notices or debt rollforward detail for the main Credit Agreement.
4. Build the note-purchase economics table.
5. Join BLM/acquisition/capex uses to asset-area production and cash contribution.
