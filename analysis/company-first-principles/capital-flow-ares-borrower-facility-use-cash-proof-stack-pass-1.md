# Capital Flow Ares Borrower Facility/Use/Cash Proof Stack Pass 1

## Purpose

This page executes end-to-end graph upgrade queue row `CFE2EGUQ-003`.

It asks:

`Can Ares borrower exposure move from named borrower-destination evidence to facility-size, use-of-proceeds, borrower-cash, and bank-role proof?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-ares-borrower-facility-use-cash-proof-stack-pass-1.csv`

The strongest local borrower bridge is:

`/cluster/capital-flow-frontline-facility-use-bridge-pass-1.md`

The upstream normalized Ares borrower table is:

`/cluster/capital-flow-ares-borrower-holder-expansion-pass-1.md`

## Current Answer

`No full upgrade. The best current Ares borrower case is Frontline Road Safety. It passes operating-borrower, sponsor-transaction, Ares arranger-role, holder-dollar, commitment-context, instrument-marker, and same-period-control gates. It fails total facility size, use-of-proceeds, borrower cash generation, lender allocation, and bank-role proof.`

## Why Frontline Is The Test Case

Frontline is stronger than most Ares borrower rows because it combines:

- operating-company context
- Bain sponsor transaction context
- Ares lead-arranger and bookrunner role evidence
- multiple SEC-filed holder rows
- visible Q2 `2026` holder fair value
- separate 2026 unfunded commitment evidence

The clean same-period holder number is:

`132.800M USD FSK + 47.936M USD K-FITS + 17.939M USD GSBD = 198.675M USD`

That is holder fair value, not total Frontline debt.

The mixed-period Ares-managed context is:

`76.6927M USD ASIF Q1 2026 Frontline fair value`

That supports Ares-managed holder visibility, but it should not be added to the Q2 total as same-date exposure.

The visible commitment context is:

`53.688M USD GSPCC Q1 2026 + 0.612M USD GSBD Q2 2026 = 54.300M USD`

That is commitment evidence, not drawn cash.

## Money Movement Chain

| Link | Current Evidence | Status |
|---|---:|---|
| Capital router | Ares | visible |
| Transaction role | Lead arranger and bookrunner for senior secured facility supporting Bain's continued growth plans | visible |
| Borrower destination | Frontline Road Safety Holdings / Frontline Road Safety Operations | visible |
| Operating destination | Roadway safety and pavement-marking services platform | visible |
| Holder-dollar evidence | `198.675M USD` latest Q2 2026 visible funded fair value | visible partial |
| Ares-managed holder context | `76.6927M USD` ASIF Q1 2026 fair value | visible with period boundary |
| Commitment context | `54.300M USD` visible 2026 unfunded commitments | visible but not drawn |
| Instrument markers | First-lien senior secured loans around SOFR plus `4.75%` to `5.00%`, March `2032` maturity cluster | visible |
| Facility size | Not captured | missing |
| Use of proceeds | Continued-growth wording only | partial clue |
| Borrower cash generation | Not captured | missing |
| Bank role | No payoff, termination, amendment, UCC, or prior-bank denominator captured | missing |

## Decision

`ares-borrower-facility-use-cash-proof-stack-executed-local-boundary`

The Ares graph row can now name Frontline as the strongest current borrower-destination proof stack. It cannot be promoted to facility/use/cash realization proof.

## Safe Claim

`Ares borrower evidence reaches named borrower-destination and holder-dollar proof through Frontline Road Safety. Ares has transaction-role evidence for a senior secured facility supporting Bain's continued growth plans, and SEC-filed holder rows show 198.675M USD of latest Q2 2026 visible Frontline fair value plus separate 2026 commitment context. The evidence does not prove total facility size, Ares' funded allocation, full lender group, use of proceeds, borrower cash generation, debt-service coverage, or bank replacement.`

## Next Required Documents

1. Frontline credit agreement or amendment.
2. Rating report or private-credit lender presentation.
3. Lender allocation schedule.
4. Use-of-proceeds or funds-flow support.
5. Borrower revenue, EBITDA, free cash flow, margin, or debt-service evidence.
6. Payoff, termination, UCC, or amendment evidence for bank-role resolution.
