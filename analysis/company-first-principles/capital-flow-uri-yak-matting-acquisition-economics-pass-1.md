# Capital Flow URI Yak/Matting Acquisition Economics Pass 1

## Purpose

This pass upgrades the Surface Protection Mats / Matting thread from category-revenue estimate only to acquisition-economics evidence.

It answers:

`What real numbers did URI disclose when it bought Yak, and what do those numbers tell us about the Matting category?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-matting-acquisition-economics-pass-1.csv`

## Source Boundary

This pass uses:

- URI March `4`, `2024` acquisition announcement for Yak Access
- URI FY `2024` acquisition footnote for Yak purchase accounting
- URI completed prior passes on Specialty category mix and fleet-type revenue estimates

The official web sources are:

- `https://investors.unitedrentals.com/press-releases/press-releases-details/2024/United-Rentals-to-Acquire-Yak-Access-for-1.1-Billion/default.aspx`
- `https://www.sec.gov/Archives/edgar/data/1067701/000106770125000008/R14.htm`

This pass is:

`yak-acquisition-economics-visible`

It is not:

`matting-ROIC-visible`

or:

`ongoing-category-margin-visible`

## Key Yak Numbers

| Metric | Value |
|---|---:|
| Base purchase price | `1.100B USD` |
| Acquisition-date purchase-price fair value | `1.158B USD` |
| Maximum contingent consideration | `50M USD` |
| Estimated contingent consideration in fair value | `41M USD` |
| Yak 2023 adjusted revenue | `353M USD` |
| Yak 2023 adjusted EBITDA | `171M USD` |
| Yak 2023 adjusted EBITDA margin | `48.4%` |
| Yak mat fleet | `~600,000` mats |
| Yak 2024 post-acquisition revenue in URI filing | `322M USD` |
| Pro forma 2024 Yak pre/post-acquisition revenue | `419M USD` |
| Acquired rental-equipment fair value | `127M USD` |
| Acquired customer relationships | `150M USD` |
| Goodwill assigned to Specialty | `828M USD` |

## Derived Operating Scale

| Derived Metric | Value | Boundary |
|---|---:|---|
| 2023 adjusted revenue per mat | `588 USD/mat` | Uses adjusted revenue and approximate mat count. |
| 2023 adjusted EBITDA per mat | `285 USD/mat` | Uses adjusted EBITDA and approximate mat count. |
| Base purchase price per mat | `1,833 USD/mat` | Uses base purchase price, not total fair value. |
| Acquisition fair value per mat | `1,930 USD/mat` | Uses acquisition-date fair value and approximate mat count. |
| Acquired rental-equipment fair value per mat | `212 USD/mat` | Purchase-accounting fair value, not OEC or replacement cost. |
| Goodwill share of acquisition-date fair value | `71.5%` | Goodwill-heavy acquisition; not category ROIC. |
| Net identifiable asset share of acquisition-date fair value | `28.5%` | Purchase-accounting allocation, not operating invested capital. |

## What This Adds

This gives the first real Matting-specific economics:

- Yak was not just a named product category.
- It had `353M USD` of 2023 adjusted revenue.
- It had `171M USD` of 2023 adjusted EBITDA.
- It had roughly `600,000` mats.
- It came with `127M USD` of acquired rental-equipment fair value and `828M USD` of goodwill.
- URI funded the acquisition with `1.100B USD` of senior notes plus ABL drawings.

That supports a much more concrete Matting claim than the prior category-mix pass.

## Why This Still Is Not ROIC

The purchase-accounting numbers are not the same as operating invested capital.

The acquired rental-equipment fair value of `127M USD` is useful, but it is not:

- original equipment cost
- replacement cost
- ongoing maintenance capex
- fleet age
- category utilization
- category gross margin
- category operating income
- category ROIC

The `171M USD` adjusted EBITDA number is pre-acquisition Yak adjusted EBITDA. It does not give ongoing URI Matting margin after integration, depreciation, corporate allocations, synergies, purchase accounting, or growth capex.

## Funding Link

This pass also connects Matting to the capital-flow question:

URI expected to fund the Yak transaction with new debt financing and ABL capacity. The FY `2024` acquisition note says the transaction and related fees were funded through `1.100B USD` of `6 1/8%` senior notes and drawings on URI's senior secured ABL facility.

So the concrete chain is:

`senior notes + ABL drawings -> Yak acquisition -> matting fleet/category adjacency -> utility/midstream/power customer exposure -> Specialty segment`

That is a real capital-flow chain, but it remains acquisition-level rather than ongoing category ROIC.

## Safe Claim

`URI's Yak acquisition makes Matting acquisition economics visible: Yak had 2023 adjusted revenue of 353M USD, adjusted EBITDA of 171M USD, about 600,000 mats, a 1.100B USD base purchase price, 1.158B USD acquisition-date fair value, 127M USD of acquired rental-equipment fair value, and 828M USD of goodwill assigned to Specialty. The deal was funded with senior notes and ABL drawings. This supports a concrete Matting capital-flow and acquisition-economics claim, but it still does not disclose ongoing Matting category margin, OEC, capex, utilization, or ROIC inside URI.`

## Claims Not To Make Yet

Do not say:

- Yak's adjusted EBITDA margin equals ongoing URI Matting margin
- acquired rental-equipment fair value equals OEC
- purchase price per mat equals replacement cost
- goodwill proves poor or good economics by itself
- acquisition adjusted EBITDA proves post-integration ROIC
- Matting explains all Specialty margin compression
- Matting category revenue after 2024 is source-stated
- ABL drawings funded a specific mat purchase schedule or exact Yak source-and-use amount

## Next Concrete Work

The next URI Matting evidence gates are:

1. Find post-acquisition Matting revenue or EBITDA disclosure after FY `2024`.
2. Use `capital-flow-uri-yak-acquisition-funding-chain-pass-1.md` for the instrument-level funding chain.
3. Search for Yak acquisition presentation materials beyond the press release.
4. Look for mat fleet OEC/replacement-cost evidence from industry sources or peers.
5. Track whether Surface Protection Mats share stayed at `4%` or moved after FY `2025`.
6. Connect utility, midstream, power, and renewables customer demand to mat rental utilization without claiming customer-level revenue unless sourced.
