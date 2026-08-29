# Capital Flow Refinancing Event Ledger Pass 1

## Purpose

This is the first debt/refinancing extraction pass for the all-company capital-flow program.

The operating table is:

`analysis/company-first-principles/data/capital-flow-refinancing-event-ledger-pass-1.csv`

It starts moving the debt/refinancing lane from:

`queued`

to:

`filed first-pass evidence`

The source base is the current company-packet layer, which itself points to annual reports, quarterly reports, 10-Ks, 10-Qs, 8-Ks, releases, MD&A files, and source ledgers. This pass does not claim final credit-agreement proof yet.

## Current Result

| Metric | Value |
|---|---:|
| Refinancing/event rows | `15` |
| Companies covered | `10` |
| Main status bucket | `filed` |
| Source depth | packet-derived, source-pointer-backed |

## Visible Row Anchors

| Row Range | Focus |
|---|---|
| RFL-001 to RFL-002 | PBF debt reduction, ABL exit, note refinancing, insurance-proceeds bridge |
| RFL-003 to RFL-004 | Liberty Broadband margin loan, Charter term loan, exchangeable debenture put |
| RFL-005 to RFL-006 | Devon pre/post-merger debt stack and liquidity |
| RFL-007 to RFL-008 | Matador San Mateo credit facility and acquisition-borrowing repayment |
| RFL-009 to RFL-010 | Coterra acquisition term-loan paydown and CNX convertible/facility cleanup |
| RFL-011 to RFL-012 | Ovintiv asset-sale funded note redemption and NuVista leverage bridge |
| RFL-013 to RFL-015 | Cenovus MEG term-loan repayment, Wheaton Antamina financing, Enhabit facility amendment |

## What This Lane Is Really Testing

The debt/refinancing lane is not only about whether a company has debt.

It asks:

`Where is capital moving risk through time, changing maturity pressure, changing lender or collateral structure, funding acquisitions, repairing balance sheets, or preserving operating control?`

The first-pass rows show four different subthemes.

## Theme And Subtheme Read

### 1. Facility Exit, Repayment, And Balance-Sheet Repair

Rows:

- `RFL-001`
- `RFL-002`
- `RFL-003`
- `RFL-004`
- `RFL-008`
- `RFL-009`
- `RFL-010`
- `RFL-013`
- `RFL-015`

This is the strongest first-pass subtheme.

Examples:

- PBF reduced gross debt by over `1B USD`, exited an ABL facility, and refinanced about `802M USD` of `2028` senior notes.
- Liberty Broadband used a Charter term loan of about `359M USD` to repay part of margin-loan borrowings.
- Coterra reduced acquisition-related term-loan debt before the Devon merger endpoint.
- CNX reduced secured-facility borrowings and cleaned up convertible-note exposure.
- Cenovus repaid the MEG acquisition term loan after strong post-deal cash generation.
- Enhabit amended its credit agreement before the Kinderhook take-private close.

The simple claim:

`Debt events are one of the clearest ways to see capital moving through the system because they leave dates, principal amounts, maturities, instruments, collateral, and repayment language.`

The boundary:

`A packet-level debt event is not yet a full refinancing proof package.`

We still need the actual debt footnotes, credit agreements, indentures, and payoff or assumption language.

### 2. Acquisition Debt And Post-Deal Cleanup

Rows:

- `RFL-005`
- `RFL-009`
- `RFL-012`
- `RFL-013`
- `RFL-014`
- `RFL-015`

This subtheme shows acquisition finance after the deal announcement.

Examples:

- Coterra's Delaware acquisition term-loan balance moved down from an issued `1.0B USD` balance to staged repayments.
- Ovintiv used divestiture proceeds after the NuVista acquisition to redeem notes and restore liquidity.
- Cenovus generated enough cash to repay the MEG acquisition term loan.
- Wheaton used a new `1.5B USD` term loan and revolver draw to fund the BHP Antamina stream.
- Enhabit entered a new credit-agreement structure before the take-private close.

The simple claim:

`Acquisition finance should not stop at transaction value. The better question is how the acquisition debt is funded, refinanced, repaid, or absorbed after close.`

The boundary:

`Transaction value is not the same as debt size, and debt size is not the same as incremental growth capital.`

### 3. Commodity-Cycle Balance Sheets

Rows:

- `RFL-001`
- `RFL-002`
- `RFL-005`
- `RFL-006`
- `RFL-007`
- `RFL-008`
- `RFL-009`
- `RFL-010`
- `RFL-011`
- `RFL-012`
- `RFL-013`

Most of the lane is energy-heavy because energy companies show the capital-cycle logic clearly.

The pattern is:

`cash flow -> asset sales or insurance proceeds -> debt paydown/refinancing -> liquidity restoration -> optionality for acquisitions, capex, dividends, or buybacks`

This matters because the capital-flow question is not only:

`who funded growth?`

It is also:

`who survived the cycle, who repaired the balance sheet, and who gained capacity to fund the next asset?`

### 4. Nontraditional Capital Stacks

Rows:

- `RFL-014`

Wheaton is different from the energy borrowers because it is not funding direct mine ownership. It is funding streaming and royalty rights.

The Antamina row matters because it shows:

`cash on hand + term loan + revolver draw -> production-linked contract right`

That is a capital-flow mechanism, but not the same one as a refinery refinancing, shale borrowing-base facility, or healthcare take-private credit agreement.

## Claim Upgrade

Before this pass, the refinancing lane was mostly a queue.

After this pass, the safer claim is:

`The debt/refinancing lane has first-pass filed evidence across 10 companies. The strongest rows show specific capital-structure events: PBF's ABL exit and senior-note refinancing, Liberty Broadband's debenture-put and margin-loan/Charter-term-loan sequence, Coterra's acquisition term-loan paydown, Ovintiv's asset-sale-funded note redemption, Cenovus's MEG term-loan repayment, Wheaton's Antamina term-loan/revolver financing, and Enhabit's amended credit agreement before take-private close.`

What we still cannot say:

`These rows prove all lender groups, all pricing terms, all collateral movement, all debt extinguishment accounting, or all post-close bank/private-credit roles.`

## Current Status By Claim Bucket

| Claim | Current Bucket | Why |
|---|---|---|
| Debt/refinancing lane is worth deep extraction | `filed` | Packet evidence includes named filings, dates, instruments, and amounts. |
| PBF is a concrete refinancing case | `filed` | ABL exit, gross debt reduction, and senior-note refinancing are visible. |
| Liberty Broadband is a concrete capital-structure case | `filed` | Debenture put, margin-loan proceeds, Charter term loan, and waiver mechanics are visible. |
| Energy balance-sheet repair is a repeated pattern | `filed` | PBF, Devon, Matador, Coterra, CNX, Ovintiv, and Cenovus all show debt/liquidity events. |
| Lender displacement or bank/private-credit role change | `queued` | Credit agreements and lender lists still need extraction. |
| Refinancing economics are fully known | `queued` | Coupons, spreads, maturities, premiums, covenants, and collateral are still mostly missing. |

## Next Extraction Order

1. PBF Q2 `2026` 10-Q debt footnote, 8-K exhibits, ABL termination language, and new senior-note terms.
2. Liberty Broadband Q2 `2026` 10-Q debt footnote, Charter term-loan agreement, margin-loan waiver, and debenture put details.
3. Ovintiv Q2 `2026` 10-Q note-redemption footnote and senior-note indenture.
4. Coterra 2025 10-K and Q1 `2026` 10-Q term-loan repayment trail.
5. Cenovus Q2 `2026` MD&A and MEG financing/repaid term-loan footnote.
6. Wheaton Antamina PMPA, term-loan agreement, and revolver amendment.
7. Enhabit February `2026` amended credit agreement and merger-close debt treatment.
8. CNX convertible-note settlement and secured-facility rollforward.
9. Matador San Mateo credit-facility amendment and borrowing-base terms.
10. Devon post-merger debt rollforward and retired instrument list.

## Bottom Line

The debt/refinancing lane is now live.

The simple read:

`Capital is not only flowing into new assets. It is also moving through old debt stacks: paying down acquisition loans, refinancing senior notes, exiting ABLs, using affiliate term loans, redeeming notes after asset sales, expanding midstream credit facilities, and resetting healthcare-service debt before take-private ownership.`

The next proof step is mechanical:

`packet row -> debt footnote -> credit agreement or indenture -> before/after debt stack -> bounded claim`

