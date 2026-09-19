# Apollo–Athene Concord exact CUSIP/series identity refresh

Research date: `2026-09-18`

## Result

`exact-public-cusip-series-identity-confirmed; Athene-settlement-and-return-still-open`

Two independent 2025 statutory investment statements identify `20633K-AN-8`
as `TUNES 253 A - ABS`.

More importantly, Athene's own corrected Schedule D row identifies the
instrument as `Concord Music Royalties LLC TUNES 2025-3A A`, with a `6.311%`
coupon and `07/20/2075` maturity. The outside statements are independent CUSIP
corroboration; Athene's row is the authoritative source for the exact class
label, coupon, and maturity in this bridge.

The Arch Mortgage Insurance Company 2025 annual statement, Schedule D Part 1,
shows `20633K-AN-8`, `TUNES 253 A - ABS`, actual cost `$9,999,858`, par
`$10,000,000`, book/adjusted carrying value `$9,999,845`, acquisition
`07/01/2025`, and maturity `10/22/2074`.

The United Guaranty Residential Insurance Company 2025 annual statement,
Schedule D Part 3, independently shows the same CUSIP and description, acquired
`07/01/2025` from Amherst Pierpont Securities, with actual cost `$9,999,858`
and par `$10,000,000`.

This closes the prior exact public CUSIP-to-series ambiguity at the instrument-
family level. KBRA describes Concord's 2025-1, 2025-2, and 2025-3 notes as the
issuer's fourth, fifth, and sixth series and says all series share the same
collateral pool. The statutory statements do not identify the full legal class
suffix, rating class, or Athene's counterparty.

The outside statutory descriptions are abbreviated, and one presents a
different maturity rendering. That formatting difference is not used to
override Athene's own row-level terms.

## Athene-side row being bridged

Athene's local Schedule D parser identifies the same CUSIP as:

- year-end book value: `$215,167,585`;
- same-CUSIP cash-like disposal consideration: `$229,053,398`;
- disposal book value: `$224,990,141`;
- disposal interest/dividends received field: `$4,733,250`; and
- year-end investment income: `$3,313,275`.

These remain statutory row fields. The exact public CUSIP/series join does not
establish that `$229.053398M` was a cash settlement, that it was paid by
Concord or a trustee, or that it reached an Athene bank account.

## Bridge

```text
Athene Schedule D CUSIP 20633K-AN-8
        -> TUNES 253 A - ABS
        -> Concord Music Royalties note family
        -> 2025 Concord issuance/refinancing context
```

This improves the named-asset bridge. It does not equate the Athene row with
the entire Concord 2025 financing, the full `$1.765B` transaction, or any
particular tranche allocation.

## Still missing for the cash loop

1. Athene's trade confirmation, allocation, custodian statement, or settlement
   record for `20633K-AN-8`.
2. Concord trustee or paying-agent remittance for the specific note/class.
3. The exact 2025 note-class and principal amount corresponding to Athene's
   `$229.053398M` disposal consideration.
4. The Series 2022-1 redemption/payoff ledger and variable-funding-note movement.
5. Concord royalty collections and the cash waterfall after senior note service.
6. Athene liability cost, credited-rate, or spread information for an
   asset-level return.

## Safe claim

`Public statutory statements now identify Athene's 20633K-AN-8 candidate as
TUNES 253 A - ABS, a Concord Music Royalties note, with an independent
July-2025 acquisition-side confirmation. Athene reports $229.053398M of
same-CUSIP cash-like consideration, while Concord and KBRA sources provide the
borrower, shared music-copyright collateral, and refinancing context. The
public record still does not prove Athene-specific settlement, trustee
remittance, borrower bank receipt, liability spread, or final return.`

## Sources

- [Arch Mortgage Insurance Company 2025 annual statement](https://s205.q4cdn.com/950744987/files/doc_downloads/Arch-Mortgage-Insurance-Company-Annual-Statement-2025.pdf), Schedule D Part 1 and Part 3.
- [United Guaranty Residential Insurance Company 2025 annual statement](https://s205.q4cdn.com/950744987/files/doc_downloads/United-Guaranty-Residential-Insurance-Company-Annual-Statement-2025.pdf), Schedule D Part 1 and Part 3.
- [KBRA 2025 Concord preliminary ratings release](https://www.kbra.com/publications/ZLhcMNKm/kbra-assigns-preliminary-ratings-to-concord-music-royalties-llc-series-2025-1-series-2025-2-and-series-2025-3?format=web).
- [Concord 2025 transaction announcement](https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/).
