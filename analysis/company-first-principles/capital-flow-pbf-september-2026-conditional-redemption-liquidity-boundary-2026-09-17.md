# PBF September 2026 conditional-redemption liquidity boundary

Research date: `2026-09-17`

## New event

PBF's September 14, 2026 Form 8-K announced an intended `$500M` senior
unsecured exchangeable-note offering and a conditional redemption of the
`$500M` 7.875% senior unsecured notes due 2030. A September 17, 2026 Form 8-K
now confirms that PBF Holding and PBF Finance issued `$550M` of 0%
exchangeable notes due 2032, including the fully exercised `$50M` option, and
received approximately `$533.6M` of net proceeds. The stated uses include
capped-call costs, the full 2030-note redemption, and general corporate
purposes. The 2030 redemption price remains `103.938%` plus accrued and
unpaid interest through the September 24, 2026 redemption date; the financing
leg is completed, but the redemption settlement is still future as of this
research date.

## What this changes

| Field | Observation | Status | Boundary |
|---|---|---|---|
| New financing | `$550M` 0% senior unsecured exchangeable notes due 2032, including the exercised `$50M` option; approximately `$533.6M` net proceeds | issued and proceeds disclosed | Exact capped-call cash cost, final cash allocation, and post-close liquidity remain open |
| Target debt | `$500M` 7.875% senior unsecured notes due 2030 | redemption remains conditional/pending for September 24, 2026 | No final settlement or holder-payment record yet |
| Redemption premium | `103.938%` plus accrued interest | contractual notice term | Does not equal final cash paid until financing and settlement occur |
| Derived redemption cash floor | `$519.690M` for `$500M` principal at `103.938%`, before accrued interest | calculated minimum principal-plus-premium amount | Not final settlement cash; excludes accrued interest, fees, taxes, and any financing shortfall |
| Exchangeable terms | 0% notes with no principal accretion; initial exchange price approximately `$96.80` per share; maximum initial exchange amount up to `7,812,475` shares; capped-call cap price initially `$123.20`; issuers may settle exchange value with cash up to principal and cash/shares above principal | final instrument, settlement-election, and dilution controls visible | Actual exchange, cash/share settlement, capped-call cash cost, and realized dilution remain future/unknown |
| Funding condition | At least `$500M` aggregate gross debt-financing proceeds after the notice | satisfied by the `$550M` issuance | Does not prove the September 24 redemption settlement or available-cash contribution |
| Legal route | PBF Holding and PBF Finance as co-issuers | entity route visible | Does not allocate cash to refinery entities or common-owner residual |

## Named issuer and guarantor perimeter

The September 17 Form 8-K identifies PBF Holding Company LLC and PBF Finance
Corporation as the co-issuers. The initial guarantors are PBF Services Company
LLC, PBF Investments LLC, Delaware City Refining Company LLC, PBF Power
Marketing LLC, Paulsboro Refining Company LLC, Toledo Refining Company LLC,
PBF International Inc., Chalmette Refining, L.L.C., Torrance Refining Company
LLC, PBF Energy Western Region LLC, and Martinez Refining Company LLC. The
filing states that PBF Energy and subsidiaries other than the issuers and
certain subsidiaries are not obligors, while the notes are structurally
subordinated to non-guarantor subsidiary debt and effectively subordinated to
secured debt, including the revolving credit facility.

This narrows the cash-flow perimeter: note proceeds and the intended
redemption are issuer-level flows with a defined guarantor set, not automatic
cash available at each refinery or at PBF Energy Inc. The legal perimeter does
not prove which entity supplied cash for the redemption, the final trustee
payment, intercompany transfers, or common-owner residual.

## QoE and financial-integrity controls

The new issuance is now cash-proceeds evidence at the issuer level, but it
should not be combined with the completed June 2026 2028-note redemption or
the still-future September 24 redemption as if one settlement ledger covered
all events. The analysis must separately reconcile gross proceeds,
discount/fees, undisclosed capped-call cash cost, cash contribution, redemption
premium, accrued interest, debt extinguishment accounting, ABL capacity, and
post-transaction liquidity. Because the notes are structurally subordinated to
non-guarantor subsidiaries, refinery-level cash cannot be inferred from the
issuer proceeds. The exchangeable feature also requires settlement-election,
dilution, and per-share analysis.

This is a liquidity and refinancing boundary, not a manipulation finding.

## Decision

`pbf-2032-exchangeable-financing-issued; 2030-redemption-settlement-open`

The September event upgrades the financing leg from announced to issued, but it
does not provide the September 24 trustee/holder settlement, exact cash
allocation, post-transaction liquidity, refinancing value creation, refinery
owner cash, after-tax NPV, or diluted common-owner return.

## Live SEC recheck — 2026-09-18

The latest checked SEC filing remains the September 17, 2026 Form 8-K. It
confirms approximately `$533.6M` of net proceeds from the `$550M` exchangeable
issuance and states that the proceeds are intended for capped-call costs, the
full 2030-note redemption, and general corporate purposes. It does not report
that the September 24 redemption has settled, the final accrued-interest
amount, the capped-call cash cost, or the post-close liquidity position.

This is a source-freshness confirmation, not a promotion: the status remains
`pbf-2032-exchangeable-financing-issued; 2030-redemption-settlement-open`.
The next source object is a post-September-24 issuer filing, trustee or paying-
agent settlement record, or post-close liquidity disclosure.

The older 2030-note indenture route also identifies the named settlement
counterparties: Wilmington Trust, National Association, as trustee, and
Deutsche Bank Trust Company Americas, as paying agent, registrar, transfer
agent, and authenticating agent. These names sharpen the acquisition path for
the post-redemption settlement request; the historical filing is not itself
evidence that either party has provided the September 2026 payment record.

## September 24 execution checklist

When the redemption date passes, update this route only from a post-event
issuer filing, trustee/paying-agent record, or equivalent controlled source.
Capture the following fields separately from the already completed `$550M`
exchangeable issuance:

| Gate | Required observation | Promotion consequence |
|---|---|---|
| Redemption completion | Issuer confirmation that the 2030 notes were redeemed, with effective date and principal retired | Moves the target debt from conditional to completed; a notice alone is insufficient |
| Trustee/payment | Wilmington Trust or Deutsche Bank settlement amount, payment date, and holder-payment status | Closes the external settlement leg; do not infer it from the redemption formula |
| Accrued interest | Final accrued-interest amount through September 24 and day-count convention | Replaces the `$519.690M` principal-plus-premium floor with an observed or reconciled amount |
| Cash allocation | Issuer/treasury split between `$533.6M` net exchangeable proceeds, capped-call cost, available cash, and general corporate purposes | Separates financing source from cash-on-hand contribution and prevents source/use overclaiming |
| Fees and tax | Capped-call cash cost, issuance costs, extinguishment accounting, and tax treatment | Required for after-tax refinancing-value analysis |
| Post-close liquidity | Cash, revolver balance/availability, ABL or borrowing-base status, and covenant headroom after settlement | Tests whether refinancing improved resilience rather than only retiring a note |
| Exchangeable outcome | Settlement election, capped-call proceeds/cost, shares issued or cash paid, and diluted share count | Closes the common-owner dilution and per-share return leg |
| Operating perimeter | Any intercompany transfer to PBF subsidiaries and refinery-level cash burden | Prevents issuer cash from being assigned automatically to refinery operations or common owners |

The minimum promotion chain is:

```text
2032 exchangeable proceeds
  -> capped-call / available-cash allocation
  -> 2030 trustee payment and accrued interest
  -> post-close debt, liquidity, fees, taxes, and dilution
  -> issuer/refinery cash residual and refinancing-value test
```

Until those joins are observed, retain the current status:
`financing-issued; redemption-settlement-open; refinancing-value-unproven`.

## Source

- [PBF Energy September 14, 2026 Form 8-K](https://www.sec.gov/Archives/edgar/data/1534504/000119312526389847/d179978d8k.htm)
- [PBF Energy September 17, 2026 Form 8-K](https://www.sec.gov/Archives/edgar/data/1534504/000119312526394108/d175053d8k.htm), including the note, guarantee, and capped-call terms
- [PBF 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1534504/000153450424000011/pbf-20231231.htm), identifying the 2030-note trustee and paying agent.

Structured companion: [PBF conditional-redemption table](data/capital-flow-pbf-september-2026-conditional-redemption-liquidity-boundary-2026-09-17.csv).
