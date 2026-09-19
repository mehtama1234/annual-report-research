# Wheaton–Antamina BHP payment-date reconciliation refresh

Research date: `2026-09-18`

## Result

`two-sided-upfront-close-confirmed; one-day-date-difference-unresolved-at-bank-ledger-level`

The newest official filing route adds a useful date control to the existing
`$4.300B` upfront bridge:

| Side | Source statement | Date | Safe interpretation |
|---|---|---:|---|
| Wheaton buyer | Wheaton's closing exhibit says WPMI made the `$4.3B` upfront payment to BHP under the BHP Antamina PMPA | 2026-04-01 | Buyer-side payment/closing date disclosed |
| BHP seller | BHP's FY2026 Form 20-F says BHP received the `$4.300B` upfront payment | 2026-04-02 | Seller-side reported receipt date disclosed |
| Contract | Both filings identify the same BHP Antamina PMPA, effective April 1, 2026 | 2026-04-01 | Named transaction and effective date align |

The one-day difference may reflect closing versus accounting/receipt-date
convention, but the public filings do not provide the bank value date, wire
confirmation, settlement statement, or funds-flow schedule needed to resolve
that inference. It should therefore remain a date-reconciliation control, not
be promoted to an independently matched bank transfer.

## What this improves

The public evidence now supports a stronger narrow claim:

```text
Wheaton filed buyer-side payment/closing date and amount
  -> BHP filed seller-side receipt date and amount
  -> same named Antamina PMPA and aligned effective date
```

This is stronger than a one-sided announcement and makes the remaining gap
more specific. It does not close:

- bank-account or custodian confirmation;
- exact closing funds-flow allocation between cash, term loan, and revolver;
- BHP-PMPA-only metal-credit quantity, invoice, or quotation-period price;
- delivery-level Wheaton cash or receivable entries;
- BHP tax, debt repayment, or common-owner allocation; or
- a financed IRR/NPV or full owner-return calculation.

The `$41M` of BHP streaming-liability settlements reported in the FY2026
20-F also remains unallocated by ounce, invoice, settlement date, and BHP-only
versus other stream activity.

## Promotion rule

Promote only the narrow status:

`public-upfront-cash-loop-confirmed-with-date-reconciliation-control`

Keep Q-03 below full delivery/return proof until a BHP-PMPA metal-credit
ledger, invoice/settlement statement, bank or custodian record, or legal-entity
use/allocation schedule joins the relevant amount, date, counterparty, and
receipt.

## Sources

- [Wheaton closing exhibit filed with the SEC](https://www.sec.gov/Archives/edgar/data/1323404/000127956926000263/ex991.htm).
- [BHP FY2026 Form 20-F](https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm).
- [BHP February 17, 2026 Form 6-K](https://www.sec.gov/Archives/edgar/data/811809/000119312526052837/d29257d6k.htm), which describes the metal-credit/no-physical-delivery settlement mechanism.
- [Existing upfront-settlement bridge](capital-flow-wheaton-antamina-bhp-upfront-settlement-bridge-2026-09-16.md).

