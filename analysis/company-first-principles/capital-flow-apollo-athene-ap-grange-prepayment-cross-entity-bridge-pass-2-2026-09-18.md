# Apollo/Athene AP Grange prepayment cross-entity bridge pass 2

Research date: `2026-09-18`

## New public fact

Apollo's Q2 2026 Form 10-Q says that credit-strategy net flows included
approximately `$5.0B` of redemptions related to the prepayment of AP Grange.
The disclosure appears in Apollo's AUM/net-flow discussion for the six months
ended June 30, 2026. See the [Apollo Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm).

This is materially stronger than an issuer-only call disclosure because it
places the AP Grange event in Apollo's credit-strategy fund-flow perimeter:

`AP Grange prepayment -> approximately $5.0B credit-strategy redemption flow`

## Existing statutory and issuer anchors

Athene's Q2 2026 filing says AP Grange called its outstanding ABS debt and that
Athene recognized a `$673M` GAAP gain. In the filed June 30, 2026
concentration table, AP Grange is no longer listed; the comparative December
31, 2025 table reports `$5.080B`, and the footnote attributes the change to the
Q2 call. The table is a concentration screen, so omission is not proof that
every residual AP Grange position was zero. See the [Athene Q2 2026 filing](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm).

The 2025 Athene statutory statement separately contains:

| Route | Statutory marker | 2025 evidence | Current interpretation |
| --- | --- | --- | --- |
| Schedule D Tranche A | `G2964#-AA-7` | `$3.638B` book; 6.50%; 03/20/2045; `$343.374M` investment income; `$265.774M` interest received | Confirmed instrument identity; call settlement still unallocated |
| Schedule BA Tranche B | `G2964#-AB-5` | `$411.999M` Part 1 book; `$31.662M` investment income; `$313,313` Part 3 consideration; blank disposal nature | Separate route; not the `$5.0B` prepayment proof |

Apollo's transaction summary maps the public AP Grange identifier
`US00187RAA32` / `G2964#AA7` to Athene's statutory-style `G2964#-AA-7` marker.
See the [AP Grange Tranche A instrument crosswalk](capital-flow-apollo-athene-ap-grange-tranche-a-public-instrument-crosswalk-pass-1-2026-09-18.md).

## 2025 disposal-counterparty perimeter

Athene's Schedule D Part 4 parser identifies two 2025 disposals from the
6.50% Tranche A row: `$2.249993M` of consideration on October 30, 2025 to
Apollo Global Securities, LLC, and `$33.489724M` on October 3, 2025 to the
AARe–Sony Life [Block] Trust. The two statutory consideration fields total
`$35.739717M`; they are not added to the `$3.638B` year-end holding or to the
Q2 call figures. The source rows do not establish whether either transaction
was a market sale, a transfer, or a settled cash receipt.

Apollo's 2025 Form 10-K identifies Apollo Global Securities, LLC (AGS) as an
Apollo subsidiary and registered broker-dealer. AGS's 2025 SEC-filed public
financials identify AGS as a Delaware LLC whose direct parent changed to
Apollo Global Securities Intermediate, L.P. effective October 15, 2025; both
AGS and its parent are consolidated subsidiaries of Apollo Global Management,
Inc. See the [Apollo 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000013/apo-20251231.htm)
and [AGS 2025 public financials](https://www.sec.gov/Archives/edgar/data/1487801/000148780126000001/agspubfin.pdf).

This creates a real legal-entity route—Athene asset row to an Apollo-affiliated
broker-dealer—for the `$2.249993M` transaction. It does **not** prove that AGS
was the economic buyer, that AGS retained the security, that the consideration
settled into an Apollo-controlled bank account, or that any amount reached
Apollo parent/common owners. The AARe–Sony Life counterparty remains a
separate non-AGS route and is not folded into Apollo cash.

## AGS financial perimeter — not AP Grange settlement

The AGS 2025 statement of financial condition provides a visible balance-sheet
perimeter as of December 31, 2025: `$455.585M` of cash and cash equivalents,
`$86.276M` of trading securities, `$13.825M` of receivables from related
parties, `$7.640M` of underwriting-fee receivables, `$11.071M` of receivables
from brokers/dealers/clearing agencies, and `$23.206M` of payables to related
parties. The filing says AGS conducts underwriting, private-placement,
asset-backed-security and proprietary securities activities, and that
recognized-but-unreceived underwriting fees sit in the underwriting-fee
receivable line. Those balances make AGS a plausible legal and settlement
perimeter for the named `$2.249993M` consideration, but they do not identify
that transaction within any balance-sheet line.

Apollo's Q2 2026 Form 10-Q separately describes AGS as providing underwriting
commitments for related-party and third-party offerings and discloses an
arrangement in which AGS provides firm bids for certain securities sold to
SSGA-managed funds. These are current role disclosures, not AP Grange-specific
execution records. No reviewed source allocates AGS cash, trading inventory,
related-party receivables, underwriting-fee receivables, or related-party
settlement to the Athene disposal.

Accordingly, the correct interpretation is:

`Athene statutory consideration -> AGS named counterparty -> AGS visible financial perimeter`

with the following links still missing:

`AGS named counterparty -> economic buyer/retained note -> settled funds -> Apollo parent/common-owner cash`

The AGS `$455.585M` cash balance, `$13.825M` related-party receivable, and
`$7.640M` underwriting-fee receivable must not be treated as containing the
`$2.249993M` AP Grange amount absent a transaction-level allocation.

## Independent redemption-date control

Principal Life's March 31, 2026 statutory statement records the same AP Grange
6.50% / 03/20/2045 security under identifier `G2964#-AA-7` with transaction
type `Redemption` and transaction date March 20, 2026. The statement's amount
columns show `860,097`, or `$860.097M` where the filing reports amounts in
thousands. See the [Principal Life March 31, 2026 statutory statement](https://investors.principal.com/static-files/b23ce476-06c4-426b-b523-d355c217d59a).

This is an independent insurer-side redemption marker that narrows the
instrument-family event to a dated Q1/Q2 2026 window and shows that at least
one external holder recorded a redemption. It is not Athene's lot, a trustee
remittance, or a bank receipt, and the reported amount cannot be added to
Athene's `$3.638B` position or Apollo's approximately `$5.0B` fund-flow figure.
The date and amount are therefore retained as a timing/scale control only.

## Second insurer record — identifier corroboration with naming conflict

Brighthouse Life's March 31, 2026 statutory statement also records
`G2964#-AA-7` with a March 20, 2026 redemption date, 100% redemption factor,
6.500% coupon, and 03/20/2045 maturity. Its reported consideration/book-value
amount is `$226.341M`. The row's description, however, labels the issuer
`INTEL CORPORATION`, not AP Grange Holdings LLC. See the [Brighthouse Life
March 31, 2026 statutory statement](https://investor.brighthousefinancial.com/static-files/bbdd6002-5e07-4585-a073-38d3f07a9521).

This is therefore retained as a **same-identifier/date corroboration with an
issuer-name conflict**, not as a second confirmed AP Grange holding. The
conflict may reflect an underlying transaction/issuer-label convention, but
the public record reviewed here does not prove that. It strengthens the March
20 redemption-date control while simultaneously keeping the identifier-to-
legal-issuer join open; it is not added to the `$860.097M` Principal Life
amount, Athene's position, or Apollo's fund-flow figure.

The identifier itself also requires caution. The same Principal Life statement
contains an AP Grange 5.000% / 03/20/2045 row under a visually similar
`G2964*-AA-7` code in a different statutory section. Accordingly,
`G2964#-AA-7`/`G2964*-AA-7` is not treated as a unique security key in this
bridge. The 6.500% route remains supported only by the combined tuple of
issuer description, coupon, maturity, transaction date, and amount, together
with the separate Apollo public-instrument crosswalk. This prevents a
same-prefix statutory code from silently joining different AP Grange notes or
an Intel-labeled row to Athene's 6.50% Tranche A holding.

## What this upgrades

1. **The event is now visible at three levels:** issuer call, Athene gain and
   June 30 concentration-table disappearance, and Apollo credit-strategy
   redemption flow.
2. **The approximate amount is directionally consistent with the issuer
   concentration perimeter:** `$5.0B` is close to, but not identical with,
   Athene's `$5.662B` March 31 concentration. The difference may reflect
   rounding, fair value, scope, timing, or positions outside the relevant
   Apollo-managed strategy; it cannot be silently reconciled.
3. **The next evidence request is narrower:** identify which Apollo-managed
   vehicle redeemed, the prepayment date, the exact called tranche/CUSIP, and
   the Athene custody or cash ledger entry.
4. **The independent redemption marker improves timing control:** Principal
   Life records `G2964#-AA-7` as redeemed on March 20, 2026 for a reported
   `$860.097M` amount, but does not close Athene's settlement or remittance
   route.

## Independent holder roll-forward control

KKR Asset-Based Income Fund's SEC-filed semiannual report for June 30, 2026
does not contain an AP Grange position in its schedule of investments. A
secondary SEC-derived holder comparison reports that the same fund had AP
Grange Holdings LLC at `$21.977M` fair value in its March 31, 2026 report and
that the position was absent at June 30. See the [KKR June 30 SEC shareholder
report](https://www.sec.gov/Archives/edgar/data/1966776/000119312526377504/d385227dncsrs.htm)
and the [SEC-derived holder comparison](https://fontrisalts.com/fund/0001966776).

This independently corroborates a Q2 market-side realization, sale, or
restructuring window for the instrument family. It does not identify the
buyer, redemption mechanics, Athene allocation, or cash path, and the
secondary comparison is not used as primary settlement evidence.

## September 18, 2026 exact-call search recheck

An additional targeted search for an AP Grange call notice, paying-agent
statement, redemption notice, or exact `G2964#-AA-7` settlement returned the
same official SEC objects already in the bridge: Athene's Q2 2026 filing
describes the call and `$673M` gain, while Apollo's Q2 2026 filing describes
approximately `$5.0B` of credit-strategy redemptions related to the
prepayment. No new public call notice, trustee remittance, affected-tranche
allocation, or Athene custody/bank record was located.

The search therefore strengthens freshness of the existing event boundary but
does not change the proof grade. The exact next object remains a dated issuer
call/prepayment notice, trustee or paying-agent remittance, Apollo vehicle
allocation, or Athene custody ledger. The `$5.0B` remains a fund-flow
classification and is not added to Athene collected income or Apollo
common-owner cash.

## What remains unproven

The `$5.0B` Apollo disclosure is an AUM/net-flow classification, not a bank
receipt. It does not identify:

- the legal borrower that paid the prepayment;
- the paying agent, trustee, or settlement date;
- whether the amount is principal, accrued/deferred interest, premium, or a
  gross/rounded fund-flow figure;
- Athene's exact allocation across Tranche A, Tranche B, and any other AP
  Grange positions;
- the amount retained by Athene after fees, taxes, liability costs, or ACRA
  noncontrolling interests; or
- any cash distribution from Athene to Apollo parent.

The `$673M` GAAP gain and `$458M` non-GAAP non-operating gain remain distinct
from the `$5.0B` redemption-flow figure. The latter should not be added to
Athene collected investment income or Apollo owner cash.

## Decision

`ap-grange-instrument-identity-confirmed; issuer-call-and-apollo-prepayment-flow-visible; athene-settlement-and-parent-cash-hold`

The next source object is a dated call/prepayment notice, trustee or paying-
agent remittance, Apollo fund redemption allocation, or Athene custody/ledger
record. A broader search for generic AP Grange terms is lower value until one
of those object types is found.
