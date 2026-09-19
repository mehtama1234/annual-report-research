# MF1 Servicing and Remittance Mechanics Boundary

Research date: `2026-09-17`

## Purpose

This pass tests whether the public MF1 servicing agreement supplies the
mechanics needed to turn a future report into a cash-joinable object:

`borrower payment -> collection account -> servicing deductions -> trustee/payment account -> noteholder or companion-interest remittance`

It is a mechanics boundary, not a cash-receipt observation.

## Public mechanics observed

The locally preserved MF1 servicing-agreement exhibit dated February 5, 2026
names `MF1 2026-FL21 LLC` as issuer and identifies the collateral manager,
servicer, special servicer, advancing agent, trustee, custodian, and note
administrator. The public exhibit also specifies:

| Mechanic | Observed rule | What it enables | What remains missing |
| --- | --- | --- | --- |
| Collection account | The servicer establishes an eligible Collection Account for the issuer's benefit. | A named account endpoint for borrower collections. | Bank statements, balances, and individual borrower receipts. |
| Deposit timing | Properly identified payments and collections received by the servicer are deposited within two business days after receipt. | A falsifiable receipt-to-account timing test. | Actual receipt date, amount, payer, and deposit confirmation. |
| Remittance route | Good and available funds are remitted to the Note Administrator for deposit into the Payment Account on each Remittance Date, subject to specified withdrawals. | A source-to-trustee remittance join. | Payment-account statement, remittance report, and noteholder allocation. |
| Priority deductions | The Collection Account permits specified servicing compensation, special-servicing fees, sub-servicing fees, servicing expenses, and related withdrawals before remittance. | A fee-and-expense waterfall schema. | Period-specific deducted amounts and liability-cost attribution. |
| Partitioned loans | A Partitioned Loan Collection Account may be maintained; amounts allocable to companion interests are treated separately and can be remitted to companion-interest holders. | A legal-perimeter control against combining issuer and companion cash. | Partition register, holder identity, and actual companion remittance. |
| Reporting | The agreement requires servicing/CREFC reports and makes specified reporting available to noteholders. | A concrete report-acquisition route. | The report files and access authorization. |

## Legal-entity and cash boundary

The agreement proves contractual account and remittance mechanics for the
transaction packet. It does not prove that Athene owned any MF1 note or
companion interest, that Apollo-affiliated Atlas entities received cash, that a
borrower paid during a selected period, or that any remittance reached Apollo
common owners. The issuer named in this servicing exhibit is also kept as a
separate legal-entity observation from the MF1 2025-B2 offering wrapper until
the offering, issuer, and candidate-CUSIP crosswalk is independently joined.

## Upgrade test

Q-12 can advance only when a period-matched report or custodian record joins:

1. named legal owner and CUSIP or companion interest;
2. borrower, loan, and collection period;
3. gross principal/interest collections;
4. account deposit and remittance dates;
5. servicing, advancing, trustee, and other deductions;
6. noteholder or companion-interest allocation; and
7. Athene receipt, liability-cost treatment, and Apollo/common-owner waterfall.

The agreement supplies the schema for items 2–6, but none of those values is
observed here.

## CTSLink series-identity control — 2026-09-17

The live CTSLink page currently reachable for the MF1CAP shelf is labeled
`MF1 2026-FL21` and shows August 18, 2026 as the current cycle, September 18,
2026 as the next cycle, and restricted access for the Distribution Date,
Bond-Level, Collateral Summary, Loan Periodic, and Restricted Servicer
reports. This is a useful publication and access-state observation, but it is
not the same label as the statutory candidate `MF1 2025-B2 LLC` / CUSIP
`592918-AA-4`.

The two series must therefore remain separate until an offering/CUSIP/legal-
owner crosswalk joins them. The live `MF1 2026-FL21` report schedule cannot be
used as a 2025-B2 remittance, borrower-cash, or Athene-ownership observation.
See the [live CTSLink series page](https://www.ctslink.com/a/seriesdocs.html?seriesId=2026FL21&shelfId=MF1CAP).

## Decision

`partial-upgrade — MF1 servicing and remittance mechanics visible; cash, Athene ownership, and owner-return joins remain open`

## Primary source

Local source: `raw/primary-sources/capital-flow/mf1/2026-03/mf1-2025-b2-transaction-exhibit.htm`, especially the servicing-account and remittance provisions around lines 2735–2912 and the reporting provisions around lines 4392–4482.
