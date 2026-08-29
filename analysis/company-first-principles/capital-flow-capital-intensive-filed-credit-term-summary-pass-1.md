# Capital Flow Capital-Intensive Filed Credit Term Summary Pass 1

## Purpose

This pass uses already cached filed reports to go one layer deeper than the credit-document locator.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-filed-credit-term-summary-pass-1.csv`

The question is:

`Before we have every credit agreement exhibit, what real term evidence can we still extract from filed 10-Q and 10-K debt notes?`

The answer is useful but bounded. We can extract coupons, maturities, balances, use-of-proceeds language, covenant clues, collateral clues, and a few derived ratios. We still cannot claim full agreement-term proof or project-level source-of-funds proof.

## What Was Added

| Item | Count |
|---|---:|
| Filed credit-term rows | `20` |
| Energy Transfer rows | `4` |
| Cheniere rows | `6` |
| United Rentals rows | `4` |
| Sterling rows | `5` |
| Cross-company governance rows | `1` |

## Theme And Subtheme Interpretation

The broad theme is still:

`capital-intensive real-economy buildout`

This pass sharpens the financing subthemes inside that theme:

| Theme Layer | Subtheme | What It Means | Companies Where It Shows Up |
|---|---|---|---|
| Credit stack visible | Refinancing ladder | New debt is not just abstract balance-sheet capacity; it has coupons, maturities, and use-of-proceeds language. | ET |
| Credit stack visible | Entity debt separation | Debt can be separated by issuer/entity, which matters when assets and cash flows sit in legal subsidiaries. | Cheniere |
| Credit stack visible | Debt-service denominator | Annual reports give a multi-year debt and interest schedule that can later be compared to contract revenue and cash flow. | Cheniere |
| Asset-backed funding | Collateral cushion | Receivables or secured facilities have balances that can be compared to collateral pools or stated facility size. | URI |
| Platform credit reset | Revolver expansion and pricing flexibility | A company can change its capital architecture after scaling, not merely borrow more under the same old structure. | Sterling |
| Governance | Filed-term summary boundary | Filed debt notes improve the evidence, but they do not replace actual credit agreements, borrowing-base certificates, or project waterfalls. | All four |

The evidence ladder is now:

`cash generation -> liquidity/facility capacity -> credit-stack-visible -> source locator -> filed-term-summary -> agreement-term-grade -> borrowing-base/covenant-grade -> project source-of-funds -> physical output and return`

This pass moves the lane to:

`filed-term-summary`

It does not move the lane to:

`agreement-term-grade`

## What We Learned

| Company | Main Financing Subtheme | New Detail From This Pass | What Still Blocks Full Proof |
|---|---|---|---|
| Energy Transfer | Refinancing ladder and covenant clue | ET issued `3.00B USD` of January `2026` senior notes across `2031`, `2036`, and `2056` maturities, redeemed `1.60B USD` of near-term notes, and disclosed a `3.01x` partnership leverage ratio under the Five-Year Credit Facility covenant. | Named-project source-and-use, covenant limit, commercial-paper backstop mechanics, and note indentures. |
| Cheniere | Entity debt and debt-service denominator | SPL, CQP, CCH, and parent debt are separable; FY `2025` filing gives `29.0B USD` of debt plus interest payments due under executed contracts and `290.6B USD` of estimated revenues under executed SPAs. | Entity waterfalls, restricted accounts, SPA-to-debt-service timing, construction accounts, and train-level funding. |
| United Rentals | Asset-backed fleet funding | URI's Q2 debt stack totals `14.230B USD`; AR collateral pool coverage is `125.8%` of AR securitization borrowings; ABL draw intensity is roughly `37.0%` of stated facility size. | Borrowing base, advance rates, fleet collateral, restricted-payment capacity, growth-versus-replacement fleet funding. |
| Sterling | Platform credit reset | Sterling moved from a `450M USD` FY `2025` credit platform to a July `2026` `1.5B USD` revolving platform with July `2031` maturity, `500M USD` incremental base amount, use-of-proceeds language for capex/acquisitions/refinancing, and a `10 bp` SOFR-adjustment elimination. | Full Exhibit `10.1` terms, pricing grid, leverage covenants, collateral definitions, and customer/project funding. |

## Energy Transfer: Refinancing Ladder, Not Yet Project Allocation

ET now has a clearer financing sequence:

| Metric | Value | Why It Matters |
|---|---:|---|
| January `2026` senior notes issued | `3.00B USD` | New long-dated debt was issued in three pieces: `4.55%` due `2031`, `5.35%` due `2036`, and `6.30%` due `2056`. |
| Refinancing use-of-proceeds | filed text | Proceeds were used to refinance existing indebtedness, including commercial paper and Five-Year Credit Facility borrowings. |
| January-February `2026` senior notes redeemed | `1.60B USD` | ET retired `1.00B USD` of January `2026` notes and `600M USD` of May `2027` notes. |
| Partnership leverage ratio under credit-facility covenant | `3.01x` | This is the first numeric covenant clue in the ET credit stack. |
| July `2026` junior subordinated notes | `1.75B USD` | ET added a long-dated subordinated layer due `2057` after Q2 close. |

Simple read:

`ET is refinancing and terming out debt around a large infrastructure platform. The filed reports show the refinancing pipes and one covenant ratio, but they still do not say which pipe funded which named project.`

## Cheniere: Entity Debt Is The Core Subtheme

Cheniere remains the strongest entity-level debt case in the capital-intensive lane.

| Entity / Layer | Filed Detail | Why It Matters |
|---|---|---|
| SPL | `5.027B USD` total SPL Senior Secured Notes at Q2 `2026` | SPL debt should not be blended into a single parent-company number. |
| CQP | `9.550B USD` total CQP Senior Notes at Q2 `2026`, with maturities from `2029` through `2056` | CQP has a visible multi-decade maturity ladder. |
| CCH | `4.930B USD` total debt at Q2 `2026`; CCH Credit Facility was `0` versus `550M USD` at year-end `2025`; CCH Revolving Credit Facility was `65M USD` | CCH moved away from the year-end facility balance while still carrying secured notes. |
| Parent | `4.750B USD` Cheniere parent senior notes at Q2 `2026` | Parent debt is a separate capital layer from project/entity debt. |
| Consolidated annual baseline | `29.0B USD` debt plus interest due under executed contracts; `4.65%` senior-note weighted average contractual rate | Gives a first debt-service denominator. |
| SPA revenue denominator | `290.6B USD` estimated revenues under executed SPAs | Gives a future comparison base, but not a coverage ratio by itself. |

Simple read:

`Cheniere is not just borrowing at the parent and building LNG assets. The debt sits in multiple legal layers, and the annual filing gives a large debt-service schedule and a much larger contract-revenue denominator. The next job is to connect those legal layers to train-level cash waterfalls.`

## United Rentals: Fleet Funding Is Asset-Backed And Covenant-Bound

URI's capital-flow subtheme is not generic infrastructure. It is:

`fleet access funded by cash flow, receivables, secured facilities, term debt, and notes`

| Metric | Value | Calculation / Source |
|---|---:|---|
| Total debt | `14.230B USD` | Q2 `2026` debt table. |
| AR securitization facility balance | `1.414B USD` | Q2 `2026` debt table. |
| AR collateral pool net of reserves and deductions | `1.779B USD` | Q2 `2026` debt note. |
| AR collateral pool / AR borrowings | `125.8%` | `1.779B / 1.414B`. |
| AR excess collateral pool over borrowings | `365M USD` | `1.779B - 1.414B`. |
| ABL balance | `1.666B USD` | Q2 `2026` debt table. |
| Stated ABL facility size | `4.5B USD` | Q2 `2026` debt table. |
| ABL drawn / stated facility size | `37.0%` | `1.666B / 4.5B`. |

The filed 10-K also matters because it says URNA payment capacity is restricted under the ABL facility, term loan facility, and senior note indentures, and substantially all assets are subject to security interests related to existing indebtedness.

Simple read:

`URI is a capital absorber because it has to keep fleet available. The funding stack is partly asset-backed and collateral-bound, so the next proof layer is borrowing-base and fleet-collateral detail, not just more revenue or capex rows.`

## Sterling: The Credit Platform Reset Is A Real Subtheme

Sterling is a different kind of capital-intensive case:

`customer-project execution platform with a larger corporate credit wrapper`

| Metric | Value | Why It Matters |
|---|---:|---|
| FY `2025` pre-reset credit platform | `450M USD` | `300M USD` term loan plus `150M USD` revolver. |
| FY `2025` revolver sublimits | `75M USD` L/C; `15M USD` swing line | Shows the old platform was sized for smaller liquidity needs. |
| Q2 `2026` term loan and total debt | `285.305M USD` total debt | Sterling entered the July reset with no revolver borrowings and a term-loan-led base. |
| July `2026` second amended revolver | `1.5B USD` | A much larger reborrowable platform with July `2031` maturity. |
| Incremental facility base amount | `500M USD` | Up from `400M USD`. |
| SOFR adjustment eliminated | `10 bp` | A pricing improvement clue. |
| Use-of-proceeds language | refinancing, capex, permitted acquisitions, general corporate purposes | Connects the credit reset to the uses that matter for capital-flow research. |

Simple read:

`Sterling scaled the credit wrapper around its backlog and acquisition platform. The filed report shows more size, longer maturity, acquisition/capex use language, and pricing/covenant-flexibility clues. It still does not prove customer-funded project economics or backlog-to-cash conversion by project.`

## Cross-Company Read

| Subtheme | ET | Cheniere | URI | Sterling |
|---|---|---|---|---|
| Refinancing ladder | Strong | Present but entity-specific work remains | Present through debt stack but not the main insight | Present through reset/refinancing language |
| Entity debt separation | Limited at current evidence layer | Strong | Moderate through financing subsidiaries/facilities | Moderate through borrower/guarantor structure still to extract |
| Collateral / borrowing base | Not yet extracted | Not yet extracted | Strongest next path | Still to extract |
| Covenant clue | `3.01x` leverage ratio | covenant compliance in FY filing | restrictions disclosed but no numeric headroom | less restrictive covenants disclosed but no thresholds |
| Project source-of-funds | Still open | Still open | Still open for fleet class and purchase use | Still open for backlog/customer project economics |

## Simple Bottom Line

In simple words:

`We are now past just saying these companies have debt capacity. We can see some terms. ET is refinancing and terming out debt. Cheniere has layered LNG-entity debt and a huge contract-revenue denominator to test later. URI has a collateral-backed fleet funding stack with first collateral and draw ratios. Sterling upgraded its whole credit platform after scaling.`

The important boundary:

`Filed debt-note terms are not the same thing as full credit-agreement terms. They are enough to sharpen the themes and subthemes, but not enough to prove exact project funding or returns.`

## Claim Status

This pass strengthens CTCS-014 again.

Promote only:

`The capital-intensive lane now has filed-term-summary evidence across refinancing ladders, entity debt, collateral clues, covenant clues, debt-service denominators, and credit-platform resets.`

Do not promote:

`The lane has full covenant schedules, borrowing-base proof, collateral reports, rating-agency recovery analysis, agreement waterfalls, project-level source-and-use, or customer-funded backlog proof.`

## Next Pass

The next useful pass is:

`capital-flow-capital-intensive-agreement-term-extraction-pass-1.md`

It should extract:

- ET Five-Year Credit Facility agreement, commercial-paper backstop mechanics, note indentures, and covenant threshold
- Cheniere SPL/CQP/CCH/parent waterfalls, restricted-payment language, construction-account mechanics, and debt-service schedules
- URI ABL and AR securitization advance rates, collateral eligibility, borrowing-base reserves, and fleet collateral links
- Sterling Exhibit `10.1` pricing grid, covenants, guarantors, collateral, incremental facility conditions, and permitted acquisition rules
