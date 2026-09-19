# Wheaton–Antamina Q-03 metal-credit receipt boundary

Research date: `2026-09-17`

## Why this update matters

The public record now makes the form of the settlement more precise. The BHP
stream is not expected to produce a physical silver shipment to Wheaton. BHP
states that the stream settles through metal credits with no physical delivery,
and Wheaton's accounting policy says precious-metal credit revenue is recognized
when the credits are sold and control transfers. The decisive receipt object is
therefore a legal-counterparty metal-credit, sale, receivable, and cash trail—
not a warehouse receipt.

This narrows the Q-03 request and prevents a false negative based on looking for
physical delivery. It does not close the BHP-only cash loop.

## Newly bounded primary evidence

| Evidence | Observation | What it proves | What remains open |
|---|---|---|---|
| BHP April 2, 2026 Form 6-K | BHP received `$4.3B` upfront consideration; ongoing transfer payments are `20%` of spot silver delivered; settlement occurs through metal credits with no physical delivery | Legal settlement mechanism, counterparty, effective transaction, and upfront recipient-side cash | BHP-only credited ounces, metal-credit issue date, sale/settlement price, receivable, and Wheaton bank receipt |
| BHP FY2026 Form 20-F | Repeats `$4.3B` streaming proceeds, `33.75%` BHP share subject to `90%` payable factor, `100M`-ounce threshold, post-threshold `22.5%`, and no physical delivery | Annual legal and cash-flow classification; confirms Antamina is not a party to the BHP/Wheaton agreement | Period-specific metal-credit ledger and BHP-to-Wheaton allocation |
| BHP FY2026 Form 20-F cash-flow statement | Reports `$4.300B` of proceeds from the streaming arrangement liability, `$41M` of settlements of that liability, and `$(3.280B)` of net financing cash flows | Exact BHP financing-cash-flow classification for the upfront stream proceeds | Bank-level receipt timing, internal use-of-proceeds allocation, or recurring BHP-PMPA credit collection |
| Wheaton Q2 2026 results exhibit | Wheaton states that it paid BHP `$4.3B` on April 1, 2026; proceeds from the new `$1.5B` term loan, a revolver draw, and cash on hand partially funded the purchase | Upfront closing-funds-flow direction and Wheaton financing perimeter | BHP-specific ongoing credit issuance, credit sale/receivable, metal-credit cash collection, or Antamina-level return allocation |
| Wheaton Q2 2026 filing | Combined Antamina attributable production was `2.319M` ounces and sales were `2.063M`; Q2 payable metal produced but not delivered was `1.412M` in the combined table | Post-close operating and timing surface; first BHP-PMPA deliveries occurred during Q2 | Split between BHP PMPA and legacy Glencore PMPA; invoice, credit sale, price, and cash/receivable |
| Wheaton Q2 2026 segment note | Combined Antamina segment reported Q2 sales of `$150.549M`, operating cash flow of `$122.039M`, and net earnings of `$77.323M`; H1 sales were `$277.563M`, operating cash flow `$222.223M`, and net earnings `$170.901M` | Same-entity period-matched operating and cash surface for the combined Antamina streams | BHP-only allocation, credit-sale proceeds, cash collection, tax, debt interest, or common-owner residual |
| Wheaton Q2 contract table | Combined Antamina entitlement is `67.5%`; BHP and Glencore thresholds are separately described | Two-contract boundary and effective-period context | BHP-only delivered/sold quantity and lot-level attribution |
| Wheaton Q2 financial statements, mineral-stream-interest roll-forward | Combined Antamina stream-interest cost was `$5.201B`, accumulated depletion was `$492.6M`, and carrying amount was `$4.708B` at June 30, 2026 | Same-entity accounting-cost, depletion, and balance-sheet burden anchor for the combined BHP/Glencore stream | BHP-only purchase allocation, fair value, recurring receipt, or asset-level return |
| Wheaton Q2 2026 MD&A cash-burden disclosure | Q2 operating cash flow was `$650M`; H1 operating cash flow was approximately `$1.4B`; management says higher interest expense reflected debt drawn to partially fund the BHP Antamina PMPA | Company-level cash and financing-burden context for the return model | Does not allocate operating cash or interest to the BHP stream, nor prove BHP credit receipt or asset-level return |
| Wheaton February 16, 2026 acquisition announcement | The transaction has a top-level BHP parent guarantee and a BHP holding-company guarantee; parent recourse is capped at the upfront deposit and reduces after certain ounces are received, while holding-company recourse is unlimited | Counterparty-credit support and a recourse boundary around the upfront exposure | A guarantee is not a delivered-ounce schedule, settlement receipt, enforcement event, or liability-adjusted return |

## Contract-economics calculation boundary

The public terms now support one useful derived input, while still stopping
short of a cash return. Before the first threshold, BHP's contractual share is
`33.75%` of Antamina silver and the fixed payable factor is `90%`, implying a
contractual payable entitlement of `30.375%` of mine production before any
additional delivery or sale allocation. After `100M` ounces have been
delivered, the BHP stream steps down to `22.5%`, or `20.25%` after the same
payable factor. These are contractual entitlement calculations, not observed
BHP-only delivered ounces, sales, or cash receipts.

The `67.5%` combined Wheaton Antamina figure is therefore a portfolio aggregation of the BHP and legacy Glencore streams, not a BHP receipt proxy.
The return model may use `30.375%` and `20.25%` as scenario entitlement
parameters, but only a BHP-specific production, credit, sale, and collection
schedule can promote them to realized cash.

## Correct receipt object

The next source request should ask for the following row, not a physical metal
shipment:

`BHP legal seller -> BHP PMPA entitlement -> payable/credited ounces -> credit issue date -> quotation-period price -> sale or receivable -> Wheaton cash account -> 20% ongoing payment -> tax and financing allocation`

Minimum fields:

1. BHP PMPA identifier and legal counterparty;
2. production or recovered-ounce period;
3. BHP share before the `90%` payable factor;
4. payable ounces and metal-credit units issued;
5. credit date and whether credits were sold, held, or netted;
6. quotation-period price and settlement currency;
7. invoice, receivable, and cash-collection date;
8. ongoing payment at `20%` of the applicable spot/received price;
9. distinction from the legacy Glencore stream; and
10. tax, debt-service, and corporate funding allocation used in the return.

## Promotion decision

## 2026-09-18 official-source refresh

The latest official BHP FY2026 operational review and Wheaton Q2 2026 release
were checked against the remaining Q-03 receipt object. Wheaton's release
breaks out `$4.3B` of BHP Antamina within `$4.5B` of Q2 net upfront cash
payments relative to mineral-stream interests, independently confirming the
BHP closing-payment amount and its inclusion in broader stream-interest cash
movement. The same release reports approximately `157,600` GEOs of
produced-but-not-yet-delivered inventory at June 30, but that is a company-wide
GEO measure and does not identify BHP Antamina credits, ounces, price, or
collection.

BHP's July 16, 2026 FY2026 operational review provides Antamina copper and
zinc production and BHP's `33.75%` interest label, but it does not provide a
BHP-specific silver-credit issuance, sale/receivable, bank-receipt, tax, or
facility-allocation schedule. It strengthens the operator-period boundary
without changing the Q-03 promotion grade.

This refresh confirms the stop rule: the next useful source must be a new
BHP-specific settlement, delivery, reserve, lender, or transaction-level
schedule. Another broad search of BHP or Wheaton operating releases would not
close the receipt object.

Q-03 remains `full-return-inputs-incomplete` and `searched-negative` for the
checked public BHP-only receipt perimeter. The update is a mechanism upgrade,
not a cash upgrade:

- **Upgraded:** the search target is now a metal-credit and credit-sale ledger;
  physical delivery is not required.
- **Observed:** BHP's `$4.3B` upfront receipt, Wheaton's April 1 `$4.3B`
  payment and identified funding mix, contract terms, Wheaton's first
  post-close delivery statement, and combined Q2 production/sales/timing data.
- **Not observed:** BHP-only credit units, invoice or receivable, realized
  price, cash collection, and asset-specific financing/tax allocation.
- **Partially upgraded:** the upfront closing-funds-flow direction is now
  filing-backed on both sides, but it is not the same object as the recurring
  BHP-PMPA metal-credit receipt and sale trail.
- **Not permitted:** assigning the combined `2.319M` produced, `2.063M` sold,
  or `1.412M` undelivered payable-metal figure entirely to the BHP PMPA.

## Financial-shenanigans and QoE control

The combined Antamina table is an allocation risk, not evidence of wrongdoing.
The same-period increase in Wheaton's combined share from `33.75%` to `67.5%`
creates a plausible operating explanation for higher production, but it does
not identify the BHP lot. Revenue recognition on precious-metal credits also
means reported stream revenue cannot be treated as collected BHP cash without
the credit-sale and receivable-to-bank reconciliation.

The return model must keep separate:

- BHP's upfront proceeds;
- Wheaton's combined Antamina operating revenue and cash-flow proxy;
- BHP-PMPA metal credits and sale proceeds;
- legacy Glencore stream credits;
- ongoing production payments;
- corporate debt interest and repayment; and
- Antamina-specific tax and common-owner residual.

The Q2 MD&A adds a useful burden control: Wheaton reported `$650M` of Q2
operating cash flow and approximately `$1.4B` for H1, while attributing higher
interest expense in part to debt drawn to partially fund the BHP PMPA. This strengthens
the company-level financing perimeter but cannot be assigned to Antamina or
netted against the BHP stream without an interest, tax, and facility-allocation
schedule.

The segment note adds a useful period-matched control without solving that
allocation problem: Antamina's combined Q2 sales were `$150.549M` with
`$122.039M` of operating cash flow and `$77.323M` of net earnings; H1 sales
were `$277.563M` with `$222.223M` of operating cash flow and `$170.901M` of
net earnings. These figures cover the combined BHP and legacy Glencore streams
and therefore must not be assigned to the BHP PMPA. They are a stronger
company-reported operating surface, not BHP-specific receipt evidence.

The Q2 mineral-stream-interest roll-forward adds a balance-sheet burden anchor:
the combined Antamina stream-interest balance had `$5.201B` of cost,
`$492.6M` of accumulated depletion, and a `$4.708B` carrying amount at June
30, 2026. This is useful for a same-entity accounting and depletion bridge, but
it is not a BHP-only purchase allocation, fair-value mark, credit receipt, or
common-owner return. The model must keep it separate from Wheaton's `$4.3B`
upfront BHP payment and from the combined operating cash surface.

## Sources

- [BHP April 2, 2026 Form 6-K](https://www.sec.gov/Archives/edgar/data/811809/000119312526138837/d21321d6k.htm)
- [BHP FY2026 Form 20-F](https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm)
- [Wheaton Q2 2026 results exhibit](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex991.htm)
- [Wheaton Q2 2026 financial statements](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex993.htm)
- [Wheaton Q2 2026 MD&A](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex992.htm)
- [BHP FY2026 operational review](https://www.sec.gov/Archives/edgar/data/811809/000119312526306705/d212012d6k.htm)
- [Wheaton official Q2 2026 results release](https://www.wheatonpm.com/news/news-details/2026/Wheaton-Precious-Metals-Announces-Second-Quarter-2026-Results-and-Record-Year-to-Date-Production-Revenue-Earnings-and-Cash-Flow/default.aspx)

## 2026-09-18 targeted official-source recheck

A narrow recheck of the current BHP and Wheaton official releases was completed
after the broader source refresh. BHP's April completion release again states
that BHP received the full `$4.3B` upfront consideration and that subsequent
settlement is through metal credits with no physical silver delivery. Wheaton's
Q2 release again identifies the BHP payment inside its `$4.5B` of net upfront
mineral-stream payments and confirms the post-close increase to a combined
`67.5%` Antamina silver entitlement.

Neither official release exposes the missing BHP-PMPA row: credited ounces,
credit issue date, quotation-period price, invoice or receivable, sale date,
Wheaton bank collection, or BHP-specific tax/financing allocation. The Q-03
stop rule therefore remains active. This is a current-source confirmation of
the searched-negative boundary, not a promotion of combined Antamina output or
cash into BHP-specific receipt evidence.

Additional official recheck sources:

- [BHP completion release, April 2, 2026](https://www.bhp.com/es/news/media-centre/releases/2026/04/bhp-completes-silver-streaming-agreement-with-wheaton-precious-metals)
- [Wheaton Q2 2026 results release](https://www.wheatonpm.com/news/news-details/2026/Wheaton-Precious-Metals-Announces-Second-Quarter-2026-Results-and-Record-Year-to-Date-Production-Revenue-Earnings-and-Cash-Flow/default.aspx)

Structured companion: [Q-03 metal-credit receipt table](data/capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.csv).
