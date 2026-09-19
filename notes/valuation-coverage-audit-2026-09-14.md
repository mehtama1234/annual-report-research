# Valuation coverage audit — 2026-09-14

The common deep-dossier register contains 224 source-linked rows. The deep
company archive contains 222 company studies. The difference is not a reason
to assign a common owner-cash multiple to every business: some businesses need
book value, fee layers, property value, or a normalized cash bridge before a
common row would be meaningful. It is also not a reason to imply that every
company has a current valuation screen. This note keeps those two situations
separate.

## 2026-09-15 continuation note

This document remains a September 14 valuation checkpoint. The live archive now
contains 236 company studies. The additional Cigna payer dossier, TJX
off-price dossier, and Astrana healthcare middle-layer dossier are analytically
complete enough for the healthcare comparison, but it is not being added to the
common owner-cash register without a payer-specific capital, claims, reserve,
and per-share cash denominator. Its current valuation questions remain in the
healthcare synthesis and dossier rather than being forced into an industrial
cash screen.

## Packet Inputs Used

- `analysis/valuation/deep-dossier-scenario-inputs-2026-09-13.csv`
- `analysis/deep-company-pages/*.md` for the original 14 unmatched company pages
- the company source ledgers linked from those dossiers
- `scripts/verify-deep-dossier-scenario-register.py`
- `scripts/verify-cross-framework-company-pages.py`

## Current classification

| Company page | Current state | What the page supports | Next valuation test |
| --- | --- | --- | --- |
| [Affirm](../analysis/deep-company-pages/affirm-holdings-inc.md) | Specialized screen present | Separate network/conversion economics from credit, funding, losses, required capital, stock compensation, and dilution; the page now shows a `$400M`/`$1.000B`/`$1.600B` normalized fully diluted operating-earnings screen against a dated `$25.543B` equity value. | Build product- and vintage-level contribution cases after expected loss, funding, servicing, incentives, fraud, capital, warrants, and diluted shares. Do not force it into the common owner-cash register. |
| [Annaly](../analysis/deep-company-pages/annaly-capital-management-inc.md) | Specialized screen present | Book value per share and normalized EAD are the relevant linked denominators; the page has bear/base/bull screens and a dated market snapshot. | Refresh price, book value, EAD, leverage, hedge, repo, and dilution from the next filing. Do not force it into the industrial owner-cash register. |
| [Booking](../analysis/deep-company-pages/booking-holdings-inc.md) | Numerical screen added | FY2025 OCF less PP&E and SBC was about `$8.474B`; the initial common-owner screen uses `$7B`/`$9B`/`$11B` cases against a dated `$135.020B` equity value. | Refresh take rate, supplier funds, marketing, payments, refunds, debt, buybacks, and travel-cycle cash per diluted share. |
| [Domino's](../analysis/deep-company-pages/dominos-pizza-inc.md) | Numerical screen added | FY2025 OCF less PP&E was `$672M`; after `$45M` of SBC, the initial common-owner screen uses `$450M`/`$650M`/`$850M` cases against a dated `$10.711B` equity value. | Refresh transactions, franchisee returns, supply-chain margin, debt, support, dividends, and buybacks. |
| [DoorDash](../analysis/deep-company-pages/doordash-inc.md) | Numerical screen added | FY2025 OCF less PP&E before acquisitions was `$2.174B`; after `$1.051B` of SBC and the `$4.151B` Deliveroo acquisition, the initial common-owner screen uses `$1.000B`/`$3.000B`/`$5.000B` cases against a dated `$89.424B` equity value. | Refresh organic growth, Deliveroo integration, provider cost, insurance, regulation, software, advertising, membership, and dilution. |
| [Huron](../analysis/deep-company-pages/huron-consulting-group-inc.md) | Numerical screen added | FY2025 OCF less PP&E and acquisitions was about `$71M`; after `$47M` of SBC, the initial common-owner screen uses `$25M`/`$60M`/`$100M` cases against a dated `$2.563B` equity value. | Refresh utilization, compensation, collections, working capital, acquisitions, debt service, SBC, and repurchases. |
| [Hyatt](../analysis/deep-company-pages/hyatt-hotels-corporation.md) | Numerical screen added | FY2025 OCF less PP&E was `$159M`; after `$74M` of SBC, the recurring screen uses `$75M`/`$150M`/`$250M` cases against a dated `$15.427B` equity value; `$1.274B` of acquisition cash remains separate. | Refresh base versus incentive fees, owner returns, pipeline conversion, loyalty cost, owned/leased hotels, debt, and dilution. |
| [Korn Ferry](../analysis/deep-company-pages/korn-ferry.md) | Numerical screen added | FY2025 OCF less PP&E and the Trilogy acquisition was about `$257M`; after `$48M` of SBC, the initial screen uses `$150M`/`$220M`/`$300M` cases against a dated `$4.025B` equity value. | Refresh solution mix, utilization, professional compensation, collections, remaining-fee conversion, acquisitions, debt, and diluted cash. |
| [Option Care](../analysis/deep-company-pages/option-care-health-inc.md) | Numerical screen added | FY2025 OCF less PP&E was `$1.068B`; after `$70M` of SBC, the initial common-owner screen uses `$750M`/`$1.000B`/`$1.250B` cases against a dated `$3.682B` equity value. | Refresh therapy mix, drug procurement, nursing labor, receivables, inventory, acquisitions, debt, quality, and the economics of the `$882M` repurchase program. |
| [Planet Fitness](../analysis/deep-company-pages/planet-fitness-inc.md) | Numerical screen added | FY2025 OCF less PP&E was `$255M`; after `$12M` of SBC, the initial common-owner screen uses `$140M`/`$220M`/`$300M` cases against a dated `$3.947B` equity value. | Refresh member retention, club openings, franchisee returns, support, debt, and the gap between repurchases and cash generated. |
| [RH](../analysis/deep-company-pages/rh-inc.md) | Numerical screen added | FY2025 OCF less PP&E was `$252M`; after `$44M` of SBC, the initial common-owner screen uses `$75M`/`$200M`/`$325M` cases against a dated `$2.658B` equity value. | Refresh order conversion, inventory, capex purpose, leases, hospitality cash, and the housing-cycle normalization from the next filing. |
| [Starbucks](../analysis/deep-company-pages/starbucks-corporation.md) | Numerical screen added | FY2025 OCF less PP&E was `$2.442B`; after `$318M` of SBC, the initial common-owner screen uses `$1.200B`/`$2.200B`/`$3.200B` cases against a dated `$113.316B` equity value. | Refresh traffic, ticket, service labor, store repair, capex, leases, stored value, restructuring, China, debt, SBC, and the dividend burden. |
| [Uber](../analysis/deep-company-pages/uber-technologies-inc.md) | Numerical screen added | FY2025 OCF less PP&E and acquisitions was `$8.948B`; after `$1.826B` of SBC, the initial screen uses `$5.000B`/`$7.000B`/`$9.000B` cases against a dated `$148.908B` equity value. | Refresh Mobility and Delivery contribution, membership, incentives, insurance, working capital, regulation, AV partner economics, and diluted cash per share. |
| [Wayfair](../analysis/deep-company-pages/wayfair-inc.md) | Numerical screen added | FY2025 OCF less PP&E was `$464M`; after `$335M` of SBC, the initial common-owner screen uses `$50M`/`$200M`/`$400M` cases against a dated `$13.832B` equity value. | Refresh repeat orders, gross profit, fulfillment, returns, working capital, SBC, leases, and required growth capital from the next filing. |

The security-control cohort is now aligned with the register as well. CrowdStrike
has a dated `$215.934B` equity-value input against `$0.700B / $1.100B / $1.600B`
normalized owner-cash cases at `30x / 45x / 60x`; Palo Alto Networks has a
dated `$264.851B` input against `$2.200B / $3.000B / $4.000B` at `30x / 40x /
50x`; and Zscaler has a dated `$26.448B` input against `$0.500B / $0.800B /
$1.200B` at `30x / 40x / 50x`. Their pages now carry the same screens and
state the remaining renewal, cloud-processing, acquisition, SBC, dilution, and
trust tests. These inputs remain expectations screens, not live quotes or price
targets.

## What “qualitative” means here

“Qualitative” does not mean the company has no valuation reasoning. It means
the page defines the correct denominator and the assumptions that would be
needed, but does not yet provide a synchronized current market input and a
bear/base/bull row in the common register. The page must not be read as a
price target.

“Explicitly unpriced” is stronger: the page itself says that the market input
or cash normalization is not ready. That wording is intentional and should be
preserved until the missing evidence is added.

“Specialized screen present” means a common industrial owner-cash row would be
misleading. Annaly's book value and EAD screen is the current example. The
same rule applies to other capital- or property-specific models when their
denominator is separately documented.

## Reproducibility checks

The classification was produced by comparing the 222 page filenames with the
source-memo paths in
[the deep-dossier scenario register](../analysis/valuation/deep-dossier-scenario-inputs-2026-09-13.csv),
then reading the valuation section of each of the 14 unmatched pages. The
common register now verifies at 224 rows; RH, Wayfair, Starbucks, Option Care,
DoorDash, Domino's, Planet Fitness, Booking, Huron, Hyatt, Korn Ferry, and Uber
were
added only after
their filing chains supplied a cash bridge
and a dated market input. Affirm remains outside the common register because
loan funding and credit cash flows make operating cash a misleading common
denominator. The remaining two exceptions are specialized screens, not padded
with made-up common-register rows.

The next useful work is not to make all 14 look comparable. It is to complete
the highest-value missing bridges in model-specific groups: marketplace and
mobility (Affirm, Booking, DoorDash, Uber, Wayfair), franchise/relationship
platforms (Domino's, Hyatt, Planet Fitness, Starbucks), professional services
(Huron, Korn Ferry), and healthcare (Option Care), while separately refreshing
RH and Annaly with their correct denominators.

## Maintenance checks

```text
python3 scripts/verify-deep-dossier-scenario-register.py
python3 scripts/verify-cross-framework-company-pages.py
bash scripts/verify-insight-system.sh
```

## Skeptical Reader Test

- Can a reader see which pages have a numerical scenario screen and which do
  not?
- Is a specialized denominator kept separate from the common owner-cash
  register?
- Does every unpriced page name the evidence required before a number is
  added?
- Does the note avoid turning a missing market snapshot into a valuation
  conclusion?
