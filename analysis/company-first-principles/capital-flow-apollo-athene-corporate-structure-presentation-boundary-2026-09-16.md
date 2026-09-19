# Apollo–Athene corporate-structure presentation boundary

Research date: `2026-09-16`

## What the official route adds

Athene's investor-relations homepage identifies an `8/11/2026` “Athene
Corporate Structure Overview August 2026 Update” and exposes an official
summary of its capital and liquidity presentation. The summary reports more
than `$470B` of total assets as of June 30, 2026, `$37B` of regulatory capital,
`$1.4B` of excess equity capital, `$79B` of available liquidity, and `$6.1B`
of total deployable capital. The available-liquidity footnote includes `$9.2B`
of cash and cash equivalents, while the deployable-capital footnote includes
`$2.2B` of untapped leverage capacity and `$2.5B` of available undrawn ACRA
capital.

These are useful Athene-level capital and liquidity observations. They do not
identify an Athene-to-AGM transfer, AGM receiving account, parent-only cash,
intercompany elimination, legal availability for common owners, or the amount
of liquidity attributable to the `$110M` H1 distribution-to-parent observation.
The presentation is therefore `evidence-insufficient` for Q-07 promotion: it
strengthens the entity-capital boundary but does not close the common-owner
cash loop.

## Exact promotion boundary

The presentation summary may be used for Athene capital/liquidity context and
for testing whether consolidated liquidity is being confused with unrestricted
AGM cash. It may not be added to the parent-receipt frontier. Promotion still
requires a dated transfer or parent-only cash-flow/bank record, source-entity
identification, intercompany elimination, restrictions, senior claims, and the
common-owner residual.

## Related May presentation access boundary

The same official homepage exposes an `Asset Portfolio Compendium` and an
`“Affiliated” & “Related Party” Assets` presentation, both dated May 1, 2026.
Their official CloudFront PDF links were located, but automated retrieval
returned HTTP `403`, including a normal browser user-agent header check. No
slide-level holdings, CUSIP, ownership, or cash-flow claim is therefore
promoted from either document. They remain useful named
source routes for the Q-08 asset-wrapper and related-party attribution chase.
The current presentations index also lists an August 24, 2026 `AMAPS Overview`
presentation and an August 13, 2026 `Athene Fixed Income Investor
Presentation`; both linked PDF fetches returned HTTP `403`. They are added as
named Q-08 routes without slide-level promotion.

## Source route and access result

- [Athene investor-relations homepage](https://ir.athene.com/) — official
  summary and link to the August 11, 2026 presentation.
- [Athene presentations index](https://ir.athene.com/presentations) — live
  issuer index listing the August 24 AMAPS, August 13 fixed-income, August 11
  corporate-structure, and May 1 asset presentations.
- [Athene May 1, 2026 Form 8-K](https://ir.athene.com/sec-filings/all-sec-filings/content/0001527469-26-000018/ahl-20260501.htm)
  — issuer filing that announces the May asset presentations.
- [Athene August 11, 2026 Form 8-K](https://ir.athene.com/sec-filings/all-sec-filings/content/0001527469-26-000060/ahl-20260811.htm)
  — dated filing announcing the presentation.
- [Presentation PDF](https://d1io3yog0oux5.cloudfront.net/_c05aa1fc7d481faf308cc0fe1acccf51/athene/db/2271/22559/pdf/Athene%2BCorporate%2BStructure%2BOverview_2026_FINAL.pdf)
  — official linked object; direct automated fetch returned `403`, so the
  homepage summary is kept separate from slide-level proof.
- [Asset Portfolio Compendium](https://d1io3yog0oux5.cloudfront.net/_c05aa1fc7d481faf308cb0fe1acccf51/athene/db/2271/22536/pdf/Athene%2BAsset%2BCompendium%2B-%2BMay%2B2026.pdf)
  — official linked object; direct automated fetch returned `403`.
- [Affiliated & Related Party Assets](https://d1io3yog0oux5.cloudfront.net/_c05aa1fc7d481faf308cb0fe1acccf51/athene/db/2271/22537/pdf/Affiliated%2B%2BRelated%2BParty%2BAssets%2B-%2BMay%2B2026.pdf)
  — official linked object; direct automated fetch returned `403`.
- [AMAPS Overview Presentation — August 2026](https://d1io3yog0oux5.cloudfront.net/_c05aa1fc7d481faf308cb0fe1acccf51/athene/db/2271/22565/pdf/AMAPS%2BOverview%2BPresentation%2B%E2%80%94%2BAugust%2B2026.pdf)
  — official linked object; direct automated fetch returned `403`.
- [Athene Fixed Income Investor Presentation — August 2026](https://d1io3yog0oux5.cloudfront.net/_c05aa1fc7d481faf308cb0fe1acccf51/athene/db/2271/22560/pdf/Q2%2B2026%2BFixed%2BIncome%2BInvestor%2BPresentation_FINAL.pdf)
  — official linked object; direct automated fetch returned `403`.

## September 18, 2026 AMAPS retrieval recheck

The AMAPS deck was rechecked through both issuer-linked CDN paths: Apollo's
investor-relations asset URL and the Athene presentations-index CDN URL. A
direct header request to each official URL again returned HTTP `403` from
CloudFront/S3. This confirms an access boundary across both issuer routes;
it does not prove that the deck is nonexistent or that its contents would
close settlement. Keep the deck as a controlled-copy request and do not make
slide-level claims from the posting notice.

Structured result: [corporate-structure presentation CSV](data/capital-flow-apollo-athene-corporate-structure-presentation-boundary-2026-09-16.csv).
