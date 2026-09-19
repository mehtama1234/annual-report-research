# Deep-dossier owner-cash and valuation bridge

Date: 2026-09-13

## What this worksheet is for

This is the current populated valuation register from the deep company
dossiers, covering the current cross-sector company set across industrial, healthcare,
infrastructure, restaurant, property, and financial-platform models. Apollo and
BlackRock remain separately treated financial-intermediation/platform models,
while T. Rowe Price provides the public-markets asset-management contrast case.
It converts reported performance into a valuation-ready evidence register. It
does not produce a target price yet because the archive does not have one
consistent live-price snapshot, normalized share count, or comparable treatment
of insurance and franchise cash across every company.

The governing sequence is:

`reported earnings -> operating cash -> maintenance / required reinvestment -> growth investment -> financing and dilution -> owner cash -> price-implied return`

The central discipline is to avoid calling every dollar left after capex
“free cash flow.” Growth acquisitions, inventory builds, debt-funded buybacks,
insurance liabilities, advertising-fund cash, and stock compensation can all
change what is genuinely available to owners.

## Synchronized market snapshot

The market data below was captured from the finance feed after the September
11, 2026 U.S. session. It is a time-stamped screening input, not a permanent
fact. Market capitalization is the provider's current equity-value field; the
filing diluted weighted-average share count is used as the per-share modeling
denominator, while the provider market capitalization remains the equity-value
cross-check.

| Company | Price | Equity value | Filing diluted shares | Market value / residual after listed uses | Screening residual yield |
|---|---:|---:|---:|---:|---:|
| Aon | $302.69 | $64,745M | 217.1M FY2025 diluted weighted average | 22.9x | 4.36% |
| Intuitive Surgical | $369.15 | $131,897M | 362.7M FY2025 diluted weighted average | 53.3x | 1.88% |
| Vertiv | $257.06 | $100,960M | 390.7M FY2025 diluted weighted average | 142.5x | 0.70% |
| Wingstop | $117.10 | $3,190M | 28.1M FY2025 diluted weighted average | 36.6x | 2.73% |
| WESCO | $356.32 | $17,364.5M | 49.5M FY2025 implied diluted common shares | N/M (negative residual) | -0.06% |
| Quanta | $650.58 | $99,173.8M | 151.3M FY2025 diluted weighted average | N/M (negative post-M&A residual) | -1.70% |
| CME | $275.54 | $99,547.6M | 360.0M FY2025 diluted weighted average | 23.8x | 4.20% |
| BlackRock | $1,079.65 | $161,578.1M | ~149.6M implied from provider equity value / price | Platform-specific; not comparable | Platform-specific |
| T. Rowe Price | $106.29 | $22,673.3M | 220.3M FY2025 diluted weighted average | 10.7x | 9.38% |
| Restaurant Brands International | $76.96 | $35,401.6M | 457.0M FY2025 diluted weighted average | 27.3x | 3.66% |
| Yum! Brands | $140.87 | $38,443.6M | 280.5M FY2025 diluted weighted average | 44.9x | 2.23% |
| CAVA | $55.88 | $6,615.0M | 118.3M FY2025 diluted weighted average | 253.4x | 0.39% |
| McKesson | $881.51 | $105,076.0M | 128.1M FY2025 diluted weighted average | 20.2x | 4.95% |
| Cencora | $321.57 | $62,366.6M | 195.2M FY2025 diluted weighted average | N/M (negative growth residual) | Negative |
| Cardinal Health | $234.57 | $55,358.5M | 242.0M FY2025 diluted weighted average | N/M (negative acquisition residual) | Negative |
| KLA | $180.64 | ~$238,400M price × FY2026 diluted shares | 1,319.6M FY2026 diluted weighted average | ~63.3x cash-after-capex screen | ~1.58% |
| F5 | $411.71 | ~$23,700M price × FY2025 diluted shares | ~57.6M FY2025 shares outstanding | ~32.2x residual after capex/acquisitions | ~3.10% |
| Equinix | $1,037.72 | ~$102,000M price × FY2025 shares | 98.3M shares outstanding at Feb. 10, 2026 | ~28.1x recurring-capex screen | ~3.56% |
| Digital Realty | $188.58 | ~$68,180M price × FY2025 diluted shares/units | ~346.1M FY2025 diluted shares/units | ~26.7x Core FFO screen | ~3.75% |
| Generac | $186.99 | ~$11,151M finance-feed equity value | ~59.3M FY2025 diluted weighted average | ~41.6x cash-after-capex screen | ~2.41% |
| Chipotle Mexican Grill | $36.20 | ~$46,302M finance-feed equity value | ~1,342.6M FY2025 diluted weighted average | ~32.0x cash-after-capex screen | ~3.13% |
| McDonald's | $252.53 | ~$179,574M finance-feed equity value | ~711M FY2025 shares outstanding | ~25.0x parent cash-after-capex screen | ~4.01% |
| NextEra Energy | $82.31 | ~$171,682.5M finance-feed equity value | ~2,085.8M shares outstanding at Q2 2026 | N/M (negative growth-funded residual) | Negative |
| ONEOK | $96.62 | ~$61,063.8M finance-feed equity value | ~631.9M FY2025 diluted shares | ~25.2x pre-dividend residual | ~3.97% |
| Cheniere Energy | $278.34 | ~$58,312.2M finance-feed equity value | 220.3M FY2025 diluted weighted average | ~23.7x post-capex screen | ~4.22% |
| Energy Transfer | $21.55 | ~$74,203.1M finance-feed equity value | Partnership unit denominator; use common-unit and NCI waterfall rather than a corporate diluted-share shortcut | ~19.3x post-capex screen | ~5.18% |
| Exxon Mobil | $165.99 | ~$744,619.1M finance-feed equity value | Use normalized owner cash rather than peak commodity earnings | ~31.5x post-capex screen | ~3.18% |
| ConocoPhillips | $137.35 | ~$166,777.9M finance-feed equity value | Use post-capital-program cash and reserve-replacement normalization | ~23.0x post-capital-program screen | ~4.34% |
| Veralto | $94.10 | ~$23,129.8M finance-feed equity value | Use OCF less PP&E, then test acquisition/R&D/support burden separately | ~22.8x post-capex screen | ~4.39% |
| CECO Environmental | $78.34 | ~$2,736.8M finance-feed equity value | Use GAAP OCF less PP&E; adjusted FCF requires reconciliation | N/M (negative screen) | Negative |
| Motorola Solutions | $466.16 | ~$77,942.0M finance-feed equity value | Use mature OCF less PP&E, then separate acquisition/platform spend | ~30.3x post-capex screen | ~3.30% |
| Cummins | $556.75 | ~$77,109.9M finance-feed equity value | OCF less PP&E and acquisitions; separate truck-cycle, Power Systems, warranty, emissions, and Accelera normalization | ~32.5x post-capex screen | ~3.08% |
| Eaton | $425.37 | ~$165,681.6M finance-feed equity value | OCF less PP&E and acquisitions; separate electrical backlog, unbilled receivables, capacity, acquisition, and separation normalization | ~80.4x post-capex screen | ~1.24% |
| Caterpillar | $818.57 | ~$378,588.6M finance-feed equity value | OCF less PP&E and acquisitions; separate dealer/finance working capital, service, backlog, tariffs, and capital-return normalization | ~42.7x post-capex screen | ~2.34% |
| Constellation Energy | $284.75 | ~$100,889.0M finance-feed equity value | OCF less PP&E and acquisitions; separate hedge, nuclear, Calpine, PPA, debt, decommissioning, and capital-return normalization | ~79.2x post-capex screen | ~1.26% |
| Vistra | $148.38 | ~$50,335.1M finance-feed equity value | OCF less capex including nuclear fuel/LTSA prepayments and Lotus acquisition; separate hedge, fleet, retail, acquisition, ARO, debt, and capital-return normalization | ~282.8x post-capex/acquisition screen | ~0.35% |
| NRG Energy | $113.46 | ~$23,850.5M equity value using official IR close and 210.2M shares | OCF less PP&E capex; separate LS Power/CPower, BYOP, retail, collateral, debt, goodwill, and capital-return normalization | ~31.1x post-capex screen | ~3.21% |
| Alliant Energy | $67.26 | ~$17,548.1M finance-feed equity value | Regulated-utility screen; OCF less construction and productive-asset spending is diagnostic only; separate rate-base recovery, customer funding, affordability, debt, ARO, and dividend coverage | N/M (negative screen) | Negative |
| Applied Industrial Technologies | $323.78 | ~$12,201.3M finance-feed equity value | OCF less PP&E capex and acquisitions; separate technical mix, MRO/project demand, inventory, receivables, acquisition cohorts, debt, SBC, and returns | ~71.0x post-acquisition screen | ~1.41% |
| Freeport-McMoRan | $71.07 | ~$102,554.0M finance-feed equity value | OCF less productive-asset spending; separate copper price, byproducts, Grasberg, reserve replacement, environmental, Indonesia, debt, and dividend normalization | ~91.9x post-investment screen | ~1.09% |
| Air Products and Chemicals | $291.43 | ~$64,930.6M finance-feed equity value | OCF less management capex and acquisitions; show total plant additions, NEOM partner funding, mature-gas cash, project resets, debt, separation, and dividends | N/M (negative screen) | Negative |
| Cameco | $96.68 | ~$42,020.1M finance-feed equity value | Approximate USD conversion of IFRS/CAD OCF less productive-asset spending; separate uranium contract and inventory timing, Fuel Services, Westinghouse equity earnings, sustaining capital, and political risk | ~54.4x converted post-capex screen | ~1.84% |
| Wheaton Precious Metals | $108.00 | ~$69,200.0M finance-feed equity value | OCF less material portfolio investing cash flow; physical capex is not the economic reinvestment measure; separate Antamina debt, operator dependence, metal mix, and deal returns | ~110.5x post-investment screen | ~0.91% |
| Newmont | $126.81 | ~$135,306.3M finance-feed equity value | OCF less productive-asset spending; separate sustaining/growth capital, reserve renewal, reclamation, portfolio sales, debt, and capital returns | ~18.5x post-capital screen | ~5.40% |
| Lundin Gold | ~$67.39 equivalent | ~$16,250.0M approximate USD equity value from C$93 price and ~241M shares | Management FCF; separate Fruta del Norte sustaining and growth capital, Ecuador taxes/profit sharing, FDNS, exploration, concentration, and dividends | ~17.6x FCF screen | ~5.70% |
| Kinross Gold | $29.13 | ~$35,800.8M finance-feed equity value | Management attributable FCF; separate mine costs, sustaining/growth capital, multi-jurisdiction taxes, project renewal, reserves, debt, and buybacks | ~14.5x attributable FCF screen | ~6.91% |
| Bunge Global | $122.41 | ~$23,517.3M finance-feed equity value | OCF less PP&E and Viterra acquisition cash; separate processing/merchandising spreads, inventory, receivables, seasonal debt, mark-to-market, synergies, and returns | N/M (negative acquisition screen) | Negative |
| CF Industries | $133.07 | ~$20,479.5M finance-feed equity value | OCF less PP&E; separate nitrogen price/gas spread, sustaining versus growth capex, outage, Blue Point, environmental, debt, and buyback claims | ~11.4x FY2025 screen | ~8.8% |
| Nutrien | $78.45 | ~$37,809.9M using 481.962M FY2025 year-end shares | Management FCF; separate potash/nitrogen/retail economics, supplier financing, inventory, receivables, mine renewal, lease principal, portfolio exits, and debt | ~19.1x FY2025 FCF | ~5.2% |
| The Mosaic Company | $25.19 | ~$8,007.9M finance-feed equity value | OCF less PP&E; separate phosphate/potash conversion, sulfur and ammonia costs, inventory, Brazil, curtailments, impairments, and capital intensity | N/M (negative FY2025 screen) | Negative |
| FMC | $11.40 | ~$1,427.6M finance-feed equity value | Continuing OCF less PP&E and acquisitions; separate patent transition, factoring, inventory, restructuring, asset sales, and debt | N/M (negative FY2025 screen) | Negative |
| Dow | $29.03 | ~$21,049.7M finance-feed equity value | Continuing OCF less PP&E, gas-field development, and affiliate investments; separate chemical spreads, advance payments, affiliate dividends, restructuring, pensions, environmental claims, and debt | N/M (negative FY2025 screen) | Negative |
| Celanese | $46.09 | ~$5,081.4M finance-feed equity value | Management FCF / OCF less PP&E; separate Engineered Materials, Acetyl Chain, nylon and site actions, working capital, restructuring, debt, goodwill, and dividends | ~6.6x FY2025 FCF | ~15.2% |
| LyondellBasell Industries | $63.69 | ~$20,574.3M finance-feed equity value | OCF less PP&E; separate regional spreads, feedstock, utilization, joint ventures, inventory, cash-improvement actions, European exits, debt, and dividends | ~53.6x FY2025 screen | ~1.9% |
| Westlake | $70.81 | ~$9,099.1M finance-feed equity value | OCF less PP&E; separate HIP and PEM, PVC/chlor-alkali spreads, housing/infrastructure, shutdowns, ACI, environmental claims, debt, and dividends | N/M (negative FY2025 screen) | Negative |
| Franco-Nevada | $266.00 | ~$51,284.5M calculated equity value using 192.8M shares | OCF less property-and-equipment purchases; separate royalty/stream acquisition capital, operator dependence, commodity mix, optionality, and dividends | ~34.4x post-capex screen | ~2.91% |
| United Rentals | $989.12 | ~$61,565.3M finance-feed equity value | 64.6M FY2025 diluted weighted average | ~28.2x management FCF screen | ~3.54% |
| Ecolab | $276.18 | ~$77,938.0M finance-feed equity value | FY2025 diluted-share denominator requires separate filing extraction | ~275.7x post-acquisition screen | ~0.36% |
| Nucor | $259.43 | ~$59,279.8M finance-feed equity value | FY2025 diluted-share denominator requires separate filing extraction | N/M (negative residual) | Negative |
| MasTec | $240.41 | ~$18,961.1M finance-feed equity value | ~84.2M FY2025 diluted shares | ~66.4x cash-after-capex screen | ~1.51% |

### Power-demand and infrastructure valuation screen

The three new cases are intentionally not treated as interchangeable. NextEra's
FY2025 operating cash flow of $12.485B was below its $24.606B total capital-
investment burden, so the residual is a growth-funded measure rather than mature
owner cash. ONEOK produced a positive $2.422B residual after capex and cash
acquisitions, but before dividends, affiliate contributions, and debt service.
MasTec produced approximately $285.7M after capex before separately normalizing
acquisitions, contract assets, and project working capital.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| NextEra Energy | Consolidated OCF less total growth and maintenance investment | $0M at 20x = $0M | $3,000M at 35x = $105,000M | $6,000M at 45x = $270,000M | $171,682.5M | FPL rate recovery, NEER project returns, tax credits, hedge normalization, NCI, debt/equity funding, Dominion execution, and customer affordability |
| ONEOK | OCF less capex and cash acquisitions | $1,800M at 12x = $21,600M | $2,400M at 15x = $36,000M | $3,200M at 18x = $57,600M | $61,063.8M | EnLink/Medallion synergy durability, affiliate distributions, commodity optimization, $34B debt, dividends, and growth capex |
| MasTec | OCF less capex before acquisition and contract-cycle normalization | $150M at 20x = $3,000M | $300M at 30x = $9,000M | $500M at 40x = $20,000M | $18,961.1M | Backlog conversion, contract assets/receivables, acquisition returns, labor, customer concentration, leverage, and project estimates |

### LNG and midstream valuation screen

Cheniere and Energy Transfer require different owner-cash denominators even
though both are energy-infrastructure control points. Cheniere's base case is
lower than its current equity value because the model treats $3.0B as normalized
cash after a conservative capex burden and assigns only a 16x sensitivity while
Stage 3, derivatives, and debt remain unresolved. Energy Transfer's base case
is also below current equity value because $3.5B is a consolidated residual
before the full partnership and minority-interest waterfall, not a clean common-
unit DCF number.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Cheniere Energy | OCF less PP&E, with maintenance/growth and derivative normalization | $2,000M at 12x = $24,000M | $3,000M at 16x = $48,000M | $4,200M at 20x = $84,000M | $58,312.2M | Stage 3 returns, train availability, contracted physical margin, derivative cash-versus-marks, debt, counterparties, and buyback discipline |
| Energy Transfer | Consolidated OCF less productive assets, then allocated through NCI/affiliate claims | $2,000M at 8x = $16,000M | $3,500M at 10x = $35,000M | $5,000M at 12x = $60,000M | $74,203.1M | Growth-capex returns, leverage stabilization, fee-based contract durability, affiliate/NCI claims, distributions, and common-unit attribution |
| United Rentals | Management FCF after fleet and non-fleet investment, acquisitions, and resale/insurance normalization | $1,500M at 18x = $27,000M | $2,200M at 24x = $52,800M | $3,000M at 30x = $90,000M | $61,565.3M | Fleet productivity, utilization, rental rates, resale values, maintenance versus growth capex, acquisitions, debt, restructuring, SBC, and capital returns |

These are deliberately provisional sensitivities, not fair-value claims. The
market-implied hurdle is visible: Cheniere requires either normalized cash above
the base bridge or a higher multiple than the base case; Energy Transfer requires
common-unit cash to be materially higher than the simple consolidated residual,
or it requires a lower risk premium than the balance sheet and partnership
waterfall currently justify.

These are scenario screens, not price targets. NextEra's base case is below the
current equity value because the market is underwriting a long period of regulated
and development compounding beyond the current residual. MasTec's bull case only
approaches the current value after a substantial cash-conversion recovery. ONEOK's
current value is above the base residual screen, which requires durable volume,
integration, and leverage management rather than a one-year optimization gain.

### Field-execution valuation screen

The field-execution operators show why backlog and demand visibility cannot be
valued with one sector multiple. Comfort Systems has unusually strong current
cash conversion but also benefited from advance billings; EMCOR's residual falls
sharply when the UK-sale proceeds are removed and acquisition cash is charged;
Sterling's 2025 acquisition program produced negative residual cash despite strong
reported E-Infrastructure margins.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Comfort Systems USA | OCF less capex, acquisitions, and investment purchases | $450M at 25x = $11,250M | $650M at 35x = $22,750M | $850M at 45x = $38,250M | $59,608.2M | Advance billings, project estimates, labor availability, acquisition returns, contingent consideration, and diluted owner cash |
| EMCOR Group | OCF less capex and acquisitions, excluding UK-sale proceeds | $150M at 25x = $3,750M | $300M at 35x = $10,500M | $500M at 45x = $22,500M | $34,434.8M | Contract-liability release, UK-sale normalization, Miller contribution, electrical-margin repair, backlog conversion, and buybacks |
| Sterling Infrastructure | OCF less capex and acquisitions, including disposal proceeds | $100M at 25x = $2,500M | $250M at 35x = $8,750M | $450M at 45x = $20,250M | $15,915.3M | CEC/E-Infrastructure margin durability, acquisition integration, contract-capital timing, RHB accounting, earn-outs, NCI, and dilution |

These cases are deliberately provisional. They are not price targets and should
not be compared with mature recurring-revenue companies without charging the
full project, acquisition, and working-capital cycle. Comfort's current value is
above the bull screen, EMCOR's is well above the bull screen, and Sterling's sits
between the base and bull screens; each gap is an expectation signal, not a
standalone sell conclusion.

Apollo is intentionally omitted from this residual-yield comparison. The
finance feed showed a $78,706M equity value and a reported P/E of about 46.9x,
but Apollo's earnings denominator combines fee, spread, insurance, principal,
mark, tax, and noncontrolling-interest effects. A P/E comparison would create
false comparability; the Apollo sum-of-the-parts bridge below is the proper
next step. The [Apollo dossier's market-expectations section](../deep-company-pages/apollo-global-management-inc.md)
now compares that dated equity value with the bear, base, and bull SOTP cases,
so the omission from this CSV is a deliberate denominator choice rather than a
missing valuation view.

BlackRock is also kept outside the ordinary residual-yield ranking. Its FY2025
GAAP OCF was $3.927B, but it spent approximately $3.496B on acquisitions,
including Preqin and HPS, while also presenting cash flows excluding CIPs. A
simple OCF-capex-acquisition residual is a useful cash-spend warning, but not a
normalized platform denominator. The separate BlackRock case uses OCF less
capex as a mature-core screen and charges the acquisition program against the
growth-platform thesis.

T. Rowe Price is shown as a clean parent-level asset-management screen. Its
FY2025 parent OCF of $2.490B less capex and other investing activity produced a
$2.127B residual, but the denominator still requires flow, fee-rate, product-
mix, and consolidated-investment-product normalization.

RBI is a specialized franchisor screen: 2025 operating cash flow less PP&E
and acquired franchised restaurants produced a $1.297B residual. It remains
before debt principal, noncontrolling interests, franchisee support/remodel
requirements, and advertising-fund normalization.

The screening yield is calculated as:

`(operating cash flow - listed capex - listed acquisitions / other investing) / provider market capitalization`

It is deliberately labeled “screening.” It is not a free-cash-flow yield
because maintenance versus growth capital, working-capital normalization,
debt service, pensions, insurance capital, SBC, and other owner claims have
not been fully normalized. The different results are nevertheless useful: the
market is currently capitalizing the listed residual at very different prices
before the unresolved burden tests are passed.

## Enterprise-value screen

The balance-sheet adjustment makes the comparison more economically useful, but
it does not solve the normalization problem. This table uses the same market
snapshot and FY2025 balance-sheet fields in the deep memos and underlying
filings. Vertiv's cash and short-term investments are now included from the
2025 filing; its Q2 2026 net-cash position is a different date and is not mixed
into this FY2025 screen.

| Company | Equity value | Debt included | Cash / investments excluded | Approx. enterprise value | EV / residual after listed uses | EV screening yield |
|---|---:|---:|---:|---:|---:|---:|
| Aon | 64,745 | 15,249 | 2,798 | **77,196** | 27.3x | 3.66% |
| Intuitive Surgical | 131,897 | 0 | 5,935 | **125,962** | 50.9x | 1.97% |
| Vertiv | 100,960 | 2,913 | 1,828 | **102,046** | 144.0x | 0.69% |
| Wingstop | 3,190 | ~1,221 | 228.5 | **4,182** | 48.0x | 2.08% |
| WESCO | 17,364.5 | 5,829.4 | 604.8 | **22,589.1** | N/M (negative residual) | -0.05% |
| Quanta | 99,173.8 | 5,994.9 | 439.5 | **104,729.2** | N/M (negative post-M&A residual) | -1.61% |
| CME | 99,547.6 | 3,422.3 | 4,541.9 | **98,428.0** | 23.5x | 4.25% |

BlackRock is excluded from this EV table until corporate cash, debt, CIPs/VIEs,
and sponsored-product balances are normalized on the same basis. Its balance
sheet is not economically comparable to CME's restricted clearing collateral
or an industrial company's gross debt/cash presentation.

T. Rowe Price is also held out of the EV table pending a consistent treatment
of its corporate investments, deferred-compensation hedge assets, restricted
capital, and consolidated investment products.

## Hotel-specific valuation screens

Marriott and Host are not inserted into the ordinary equity-cash ranking
because their denominators represent different control points. The synchronized
September 11, 2026 market snapshot showed Marriott equity value of $87,275.9M
and Host equity value of $15,237.2M.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Marriott | Fee-platform cash after 2025 capital/technology spend and citizenM acquisition | $1,600M at 30x = $48,000M | $2,300M at 38x = $87,400M | $3,000M at 45x = $135,000M | $87,275.9M | Rooms/pipeline conversion, RevPAR, loyalty breakage/redemptions, guarantees, co-brand cash, technology spend, debt, and buybacks |
| Host | OCF less property capex, acquisitions, and investments | $650M at 15x = $9,750M | $800M at 18x = $14,400M | $950M at 20x = $19,000M | $15,237.2M | Normalized NOI, renewal capex, labor/insurance, interest, NAV cap rates, asset sales, debt maturities, and REIT/OP dilution |

These are illustrative screens, not price targets. Marriott's base case assumes
the franchise and loyalty engine converts room growth into cash without a
proportionate increase in loyalty obligations or guarantees. Host's base case
uses a property-owner cash denominator after a $644M 2025 capex burden; an FFO
multiple without that charge would overstate the margin of safety.

## Healthcare reset valuation screen

Baxter requires a recovery model rather than a mature-medtech multiple. The
September 11, 2026 market snapshot showed approximately $12,328.4M of equity
value. Continuing-operations OCF less capex and developed-technology
investment was approximately $429M in 2025.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Baxter | Continuing OCF after capex and developed-technology investment | $250M at 18x = $4,500M | $500M at 25x = $12,500M | $700M at 30x = $21,000M | $12,328.4M | Gross-margin repair, quality/product holds, inventory turns, debt reduction, separation claims, and proof that special items stop recurring |

This is a recovery sensitivity, not a price target. The base case barely
clears current equity value and requires continuing OCF to rise above the 2025
screen while the market grants a recovery multiple. A higher multiple without
evidence of quality and cash repair would be narrative, not valuation.

Stryker requires a platform-medtech screen rather than a mature medtech
multiple. FY2025 OCF was $5.044B, but acquisitions consumed $4.960B and PP&E
capex consumed $761M, leaving a negative $677M OCF-after-acquisitions-and-capex
screen before other investing and financing. The September 11, 2026 market
snapshot showed equity value of approximately $106,366.2M.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Stryker | OCF less acquisitions and PP&E capex | $2,500M at 25x = $62,500M | $4,000M at 30x = $120,000M | $5,500M at 35x = $192,500M | $106,366.2M | Procedure durability, acquisition cohorts, amortization/inventory step-up, stock compensation, cyber/quality burden, and hospital capital budgets |

The screen does not conclude that Stryker destroys value; it shows that the
current price requires acquisition returns and a long competitive-advantage
period. A buyer must verify that robotics, implants, and procedure platforms
produce enough incremental cash to offset the capital deployed to acquire and
support them.

Henry Schein is screened as a provider-workflow distributor rather than a
medtech platform. FY2025 OCF less property capex, capitalized software, and
acquisitions/equity investments was approximately $322M. The September 11,
2026 market snapshot showed equity value of approximately $10,107.5M.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Henry Schein | OCF less property capex, software, and acquisitions | $250M at 20x = $5,000M | $450M at 25x = $11,250M | $700M at 30x = $21,000M | $10,107.5M | Specialty/technology mix, restructuring recurrence, working capital, KKR dilution, debt, cyber, and buyback discipline |

The base screen is near current equity value only if cash conversion improves
from FY2025. The valuation therefore requires the BOLD+1 initiatives to create
cash, not merely adjusted EBITDA or non-GAAP EPS.

## Industrial workflow valuation screen

Fastenal is not treated as a software company merely because Digital Footprint
represented 61.4% of 2025 sales. The relevant denominator is cash after the
physical reinvestment needed to maintain branches, distribution centers,
onsites, vending, trucks, inventory, and technology. 2025 OCF less net capex
was approximately $1,064.8M; the September 11, 2026 market snapshot showed
equity value of approximately $56,731.9M.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Fastenal | OCF less net capex | $850M at 22x = $18,700M | $1,100M at 25x = $27,500M | $1,350M at 28x = $37,800M | $56,731.9M | Large-account gross margin, tariff price/cost, inventory turns, site-level returns, digital adoption versus physical burden, and industrial-cycle durability |

This screen is deliberately conservative about the digital narrative. The
current valuation requires substantially more normalized owner cash, a longer
competitive-advantage period, or a materially higher multiple than the base
case. The upside case must be earned through better incremental site returns
and cash conversion, not simply more FMI/eBusiness penetration.

Ferguson requires a separate broad-line distribution screen because its fiscal
year changed and its acquisition burden is more material. FY2025 OCF less
capex was approximately $1,603M; subtracting the $301M acquisition cash outflow
produces approximately $1,302M before dividends, buybacks, debt service, and
other investing. The September 11, 2026 market snapshot showed equity value of
approximately $43,172.8M.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Ferguson | OCF less capex and acquisitions | $1,000M at 18x = $18,000M | $1,400M at 24x = $33,600M | $1,800M at 28x = $50,400M | $43,172.8M | Repair/non-residential durability, acquisition returns, price timing, working capital, debt, buybacks, and fiscal-period normalization |

The current value sits above the base screen, so the market is underwriting
continued growth, durable share gains, or a longer competitive-advantage period
than the FY2025 cash bridge alone proves. This is not a rejection of the
business; it identifies the precise burden that future filings must overcome.

## Water-infrastructure channel valuation screen

Core & Main is screened separately because its specialized replacement demand
does not eliminate acquisition and ownership-structure claims. Fiscal 2025
audited OCF was $650M; after $46M of capex, $61M of acquisitions, and
approximately $37M of other investing, the residual was approximately $505M.
The prior fiscal year consumed $741M on acquisitions against $621M of OCF,
which keeps the acquisition cadence as the central normalization question. The
September 11, 2026 market snapshot showed equity value of approximately
$7,854.3M.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Core & Main | OCF after capex, acquisitions, and other investing | $200M at 20x = $4,000M | $500M at 25x = $12,500M | $800M at 30x = $24,000M | $7,854.3M | Acquisition/greenfield returns, municipal timing, TRA/NCI claims, inventory rebates/reserves, leverage, and Class A cash conversion |

The screen remains intentionally conservative because one positive
post-acquisition year does not establish a steady-state owner-cash denominator;
the prior-year acquisition-heavy residual
cannot support a conventional free-cash-flow multiple. The base case requires
normalized owner cash to recover while the company continues to fund density
and infrastructure capability. That recovery must be demonstrated in filings,
not inferred from adjusted EBITDA or the secular water narrative.

Grainger is screened separately from project distributors because its
enterprise-procurement relationship and capital-return program deserve a
durability premium, while its LIFO/inflation and segment-mix issues make a
simple peer multiple misleading. FY2025 OCF less capex was approximately
$1,331M; the September 11, 2026 market snapshot showed equity value of about
$60,416M.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Grainger | OCF less supply-chain/technology capex | $1,000M at 25x = $25,000M | $1,400M at 32x = $44,800M | $1,800M at 38x = $68,400M | $60,416M | High-Touch retention, Endless Assortment contribution, LIFO/inflation normalization, inventory/receivables, capex, divestiture recurrence, and buyback discipline |

The current market value is above the base screen and close to the bull screen.
That is consistent with a high-quality franchise, but it leaves little room
for a prolonged working-capital or margin disappointment. The valuation case
needs proof that procurement embeddedness converts into cash returns after the
physical network is maintained.

Vertiv's cash field is now included using the 2025 filing's $1,728.4M cash and
$99.5M short-term investments; the 2025 debt field is the $2,913.0M gross
carrying value before current-portion presentation. The Q2 2026 net-cash
position remains a separate, later-date observation and is not mixed into this
FY2025 screen.

The screen changes the first-pass interpretation. Aon remains the least
expensive on the listed residual, but debt and acquisition normalization are
central to that result. Intuitive remains expensive despite net cash because
the market capitalizes a high-quality installed-base growth and reinvestment
story. Vertiv's price embeds an especially demanding backlog-to-cash and
acquisition-return outcome. Wingstop's debt structure materially reduces the
apparent cash yield of the parent-level franchise model. WESCO is deliberately
shown as N/M because its FY2025 residual after capex and acquisitions was
negative; the negative screen yield is a warning about conversion, not a
meaningful steady-state valuation multiple.

## Market-implied owner-cash hurdles

The table below reverses the valuation question. Instead of guessing a target
price, it asks how much normalized owner cash would be required to support the
current equity value at several illustrative equity-cash multiples.

| Company | Current equity value | Cash multiple 1 | Owner cash required | Cash multiple 2 | Owner cash required | Cash multiple 3 | Owner cash required | Listed residual after uses |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Aon | 64,745 | 20x | 3,237 | 25x | 2,590 | 30x | 2,158 | 2,824 |
| Intuitive Surgical | 131,897 | 35x | 3,768 | 45x | 2,931 | 55x | 2,398 | 2,477 |
| Vertiv | 100,960 | 50x | 2,019 | 75x | 1,346 | 100x | 1,010 | 709 |
| Wingstop | 3,190 | 30x | 106 | 40x | 80 | 50x | 64 | 87 |
| Restaurant Brands International | 35,402 | 25x | 1,416 | 28x | 1,264 | 32x | 1,106 | 1,297 |
| Yum! Brands | 38,444 | 30x | 1,281 | 40x | 961 | 50x | 769 | 857 |
| CAVA | 6,615 | 40x | 165 | 50x | 132 | 60x | 110 | 26 |
| McKesson | 105,076 | 18x | 5,837 | 22x | 4,776 | 26x | 4,041 | 5,202 |
| Cencora | 62,367 | 20x | 3,118 | 25x | 2,495 | 30x | 2,079 | (1,120) |
| Cardinal Health | 55,359 | 18x | 3,076 | 22x | 2,516 | 26x | 2,129 | (3,450) |
| KLA | 238,400 | 35x | 6,811 | 45x | 5,298 | 55x | 4,335 | 3,767 |
| F5 | 23,700 | 30x | 790 | 32x | 741 | 35x | 677 | 735 |
| Equinix | 102,000 | 30x | 3,400 | 35x | 2,914 | 40x | 2,550 | 3,627 recurring-capex screen |
| Digital Realty | 68,180 | 25x | 2,727 | 28x | 2,435 | 32x | 2,131 | 2,558 Core FFO screen |
| Generac | 11,151 | 22x | 507 | 28x | 398 | 34x | 328 | 268 cash-after-capex screen |
| Chipotle Mexican Grill | 46,302 | 25x | 1,852 | 30x | 1,543 | 35x | 1,323 | 1,448 cash-after-capex screen |
| McDonald's | 179,574 | 18x | 9,976 | 21x | 8,551 | 24x | 7,482 | 7,186 parent cash-after-capex screen |
| WESCO | 17,364.5 | 20x | 868 | 25x | 695 | 30x | 579 | (11) |
| Quanta | 99,173.8 | 25x | 3,967 | 35x | 2,834 | 45x | 2,204 | (1,684) |
| BlackRock | 161,578.1 | 30x | 5,386 | 35x | 4,616 | 40x | 4,039 | 3,552 mature-core screen |
| T. Rowe Price | 22,673.3 | 10x | 2,267 | 12x | 1,889 | 15x | 1,511 | 2,127 |

The multiples are illustrative sector-sensitive test points, not claims about
fair value. Their purpose is to expose the burden of the current price:

- Aon needs either more than the listed residual or a high-quality recurring
  cash interpretation of most of it. Debt, pensions, restructuring, and
  acquisition cash determine whether that hurdle is met.
- Intuitive's current value requires sustained cash growth beyond the 2025
  listed residual at moderate-to-high quality multiples, or a premium for
  unusually durable procedure and instrument growth. Inventory, SBC, and
  repurchase requirements are therefore valuation variables, not footnotes.
- Vertiv requires a large increase from the FY2025 residual even at a 100x
  cash multiple. That is consistent with the market pricing a strong backlog
  conversion, margin, and acquisition-return path; it is also why a reversal
  of working-capital support is a central downside test.
- Wingstop's current value is close to 40x the listed residual. The key issue
  is whether the residual understates durable royalty economics or whether
  debt, advertising-fund timing, franchisee support, and buybacks consume the
  difference.
- WESCO's current equity value requires approximately $579M–$868M of normalized
  owner cash at 30x–20x multiples, versus a negative FY2025 residual. Its
  first-half 2026 annualized post-capex cash is roughly $447M before any
  acquisition spend, so the market still requires a conversion and margin
  recovery case rather than merely continued sales growth.
- Quanta's current equity value requires approximately $2.2B–$4.0B of
  normalized owner cash at 45x–25x multiples, versus a negative $1.684B 2025
  residual after capex, acquisitions, and strategic investments. The market is
  therefore capitalizing a future in which backlog growth and acquisition
  spending translate into much higher through-cycle cash.
- CME's current equity value is approximately 23.8x the listed residual, but
  the residual includes collateral-interest economics and excludes the need
  to normalize volume, rates, technology resilience, and stock compensation.
  Restricted performance-bond and guaranty-fund cash is not treated as excess
  corporate cash in the enterprise-value screen.

## Three-scenario normalization framework

The next model should use company-specific normalization rather than one
portfolio-wide haircut. The starting factors below are transparent stress
parameters tied to the evidence in each dossier. They are placeholders for
filing-tested assumptions, not forecasts.

| Company | Bear case focus | Base case focus | Bull case focus | Inputs that must earn the case |
|---|---|---|---|---|
| Aon | 60–70% of listed residual after pensions, restructuring, debt, and weaker organic growth | 75–85% after recurring pensions and normalized acquisition cash | 85–95% with durable organic growth, savings, and disciplined M&A | Retention, price/mix, organic growth exclusions, acquisition cash returns, debt reduction, diluted shares |
| Intuitive Surgical | 60–75% after inventory normalization, SBC, and slower procedures | 80–90% with procedure growth and stable reinvestment | 90–100% if utilization, instruments, services, and capital intensity improve together | Procedures per system, instrument cash per procedure, inventory turns, PP&E, R&D, SBC, repurchases |
| Vertiv | 35–55% after working-capital reversal and weak acquisition contribution | 60–75% after backlog conversion and normal warranty/capacity costs | 80–95% after durable margin, cash conversion, and acquisition returns | Backlog cancellations, gross margin, receivables/inventory, warranty, capex, software, debt, acquired cash flow |
| Wingstop | 40–55% after traffic weakness, debt service, and advertising-fund timing | 60–75% after franchisee health and recurring royalty cash | 80–95% after traffic recovery and self-funded capital returns | Domestic traffic, AUV, franchisee returns, advertising cash, securitized debt, SBC, buyback funding |
| WESCO | $0M after weak turns, project delays, and debt burden | $450M after working-capital normalization and modest margin improvement | $750M after backlog conversion, better turns, and digital payback | Receivable collections, inventory turns, gross margin, supplier terms, digital spend, interest, net debt |

For each case, the worksheet should calculate:

`normalized owner cash = listed residual x evidence-tested conversion factor - recurring cash claims`

`implied equity value = normalized owner cash x selected equity-cash multiple + unrestricted cash - debt and other senior claims`

`implied return = implied equity value / synchronized current equity value - 1`

The model must keep the factor, multiple, and cash claims in separate cells or
fields. A company should not receive a better valuation merely because a
normalization haircut and a higher multiple were chosen together without an
operating reason.

## Materials control-versus-burden valuation screen

Ecolab and Nucor are deliberately not treated as interchangeable materials
companies. Ecolab's $283M FY2025 residual includes a large acquisition program
that may create future service cash; Nucor's $(190)M residual reflects a steel
cycle year in which PP&E spending exceeded OCF. The scenario cases therefore
ask different questions about normalized cash.

| Company | Economic denominator | Bear case | Base case | Bull case | Current equity value | Main expectation burden |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Ecolab | OCF less PP&E and acquisition/affiliate cash | $250M at 25x = $6,250M | $800M at 35x = $28,000M | $1,400M at 45x = $63,000M | $77,938.0M | Ovivo/high-tech acquisition returns, organic pricing, field-service productivity, working capital, debt, SBC, and capital returns |
| Nucor | OCF less PP&E and acquisitions through a steel cycle | $0M at 12x = $0M | $1,500M at 16x = $24,000M | $3,000M at 20x = $60,000M | $59,279.8M | Mid-cycle steel price/volume, EAF utilization, scrap/energy spreads, contract mix, trade policy, project returns, debt, NCI, and capex |

The market is demanding in both cases. Ecolab requires a much higher normalized
cash outcome than FY2025 after acquisitions, while Nucor is priced near the
initial bull screen and therefore needs strong project utilization and
through-cycle cash rather than only a 2026 rebound.

## First-pass filing-tested scenario outputs

The calculations below are recorded in the companion [scenario input
CSV](deep-dossier-scenario-inputs-2026-09-13.csv). The cash cases are anchored
to the reported bridges and the burdens identified in each filing-backed memo;
the multiples are deliberately separate illustrative equity-cash sensitivities.
They are not forecasts or price targets.

Run `python3 scripts/verify-deep-dossier-scenario-register.py` from the
repository root to check the register's schema, source-memo links, scenario
ordering, and cash-times-multiple arithmetic.

| Company | Bear normalized cash | Base normalized cash | Bull normalized cash | Bear implied equity value | Base implied equity value | Bull implied equity value | Current equity value | What the market must prove |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Aon | 2,200 | 2,800 | 3,300 | 39,600 at 18x | 61,600 at 22x | 85,800 at 26x | 64,745 | Recurring brokerage cash can survive debt, pensions, restructuring, and M&A normalization |
| Intuitive Surgical | 1,300 | 1,900 | 2,500 | 39,000 at 30x | 79,800 at 42x | 125,000 at 50x | 131,897 | Procedure, instruments, services, and reinvestment can support cash beyond the FY2025 bridge |
| Vertiv | 400 | 700 | 1,100 | 16,000 at 40x | 49,000 at 70x | 110,000 at 100x | 100,960 | Backlog and the PurgeRite acquisition can produce through-cycle cash after working capital reverses |
| Wingstop | 60 | 85 | 100 | 1,500 at 25x | 2,975 at 35x | 4,500 at 45x | 3,190 | Franchisee economics and traffic can support royalty cash after debt service and capital returns |
| WESCO | 0 | 450 | 750 | 0 at 20x | 11,250 at 25x | 22,500 at 30x | 17,364.5 | Receivable/inventory turns, data-center backlog, margin, and debt reduction can convert sales growth into owner cash |
| Quanta | 1,000 | 1,800 | 2,600 | 35,000 at 35x | 81,000 at 45x | 143,000 at 55x | 99,173.8 | RPO converts at disciplined project margins, M&A returns exceed capital cost, and capex intensity moderates |
| CME | 3,500 | 4,200 | 4,800 | 70,000 at 20x | 96,600 at 23x | 124,800 at 26x | 99,547.6 | Volume and collateral interest normalize without impairing clearing/data growth or resilience spending |
| BlackRock | 3,300 | 4,500 | 5,700 | 99,000 at 30x | 157,500 at 35x | 228,000 at 40x | 161,578.1 | Organic fee-paying AUM, technology margins, HPS/Preqin returns, cash realization, and per-share cash growth must offset fee compression and acquisition burden |
| T. Rowe Price | 1,500 | 2,100 | 2,600 | 15,000 at 10x | 25,200 at 12x | 39,000 at 15x | 22,673.3 | Net-flow repair, fee-rate stabilization, retirement/ETF/alternatives scale, performance, and technology returns must offset legacy outflows |
| KLA | 2,500 | 3,800 | 5,000 | 87,500 at 35x | 171,000 at 45x | 275,000 at 55x | 238,400 | Service pull-through, process-control pricing, and AI/HPC complexity must offset semiconductor-capex cyclicality, R&D, SBC, customer concentration, and debt |
| F5 | 550 | 750 | 950 | 16,500 at 30x | 24,000 at 32x | 33,250 at 35x | 23,700 | Software/subscription and service renewal, AI-security attach, and high gross margins must survive cyber remediation, systems/services burden, CalypsoAI integration, SBC, and cloud-native competition |
| Equinix | 2,500 | 3,500 | 4,500 | 75,000 at 30x | 122,500 at 35x | 180,000 at 40x | 102,000 | MRR and interconnection density must support AFFO and recurring-capex growth after power, rent, expansion capex, debt, leases, JV/VIE claims, SBC, and refinancing |
| Digital Realty | 1,800 | 2,500 | 3,200 | 45,000 at 25x | 70,000 at 28x | 102,400 at 32x | 68,180 | Hyperscale backlog and 10%+ development yields must translate into Core FFO/share after recurring capex, leasing costs, power, debt, JV/private-capital claims, and dilution |
| Generac | 250 | 400 | 550 | 5,500 at 22x | 11,200 at 28x | 18,700 at 34x | 11,151 | C&I and hyperscale backlog must convert into cash after inventory, warranty, legal costs, tariff-refund roll-off, capacity investment, debt, and buybacks |
| Chipotle Mexican Grill | 1,200 | 1,600 | 2,000 | 30,000 at 25x | 48,000 at 30x | 70,000 at 35x | 46,302 | Traffic recovery and Chipotlane-led openings must preserve restaurant margin and unit payback after lease, labor, food, digital, SBC, and buyback claims |
| McDonald's | 6,500 | 7,500 | 8,500 | 117,000 at 18x | 157,500 at 21x | 204,000 at 24x | 179,574 | Franchisee health, rent/royalty collection, traffic recovery, value economics, real-estate reinvestment, debt, and capital returns must sustain parent cash |
| Cheniere Energy | 2,000 | 3,000 | 4,200 | 24,000 at 12x | 48,000 at 16x | 84,000 at 20x | 58,312.2 | Stage 3 and contracted LNG cash must offset derivative, capex, debt, counterparty, and capital-return risk |
| Energy Transfer | 2,000 | 3,500 | 5,000 | 16,000 at 8x | 35,000 at 10x | 60,000 at 12x | 74,203.1 | Corridor growth must produce common-unit cash after productive assets, affiliates, NCI, debt, and distributions |
| United Rentals | 1,500 | 2,200 | 3,000 | 27,000 at 18x | 52,800 at 24x | 90,000 at 30x | 61,565.3 | Fleet productivity and specialty growth must overcome capital intensity, resale-cycle risk, acquisitions, debt, restructuring, SBC, and capital returns |
| Ecolab | 250 | 800 | 1,400 | 6,250 at 25x | 28,000 at 35x | 63,000 at 45x | 77,938.0 | Embedded water/hygiene service must convert acquisition and high-tech investment into recurring cash after field labor, input costs, debt, SBC, and returns |
| Nucor | 0 | 1,500 | 3,000 | 0 at 12x | 24,000 at 16x | 60,000 at 20x | 59,279.8 | Steel pricing, utilization, contract mix, policy, and new-capacity returns must support through-cycle cash after $3.4B capex |
| Arthur J. Gallagher | 1,100 | 1,700 | 2,300 | 26,400 at 24x | 51,000 at 30x | 82,800 at 36x | 61,594.0 | AssuredPartners and future acquisitions must convert into organic fee cash after producer retention, earnouts, integration, debt, dilution, goodwill, and SBC |
| The Sherwin-Williams Company | 1,200 | 1,800 | 2,500 | 30,000 at 25x | 57,600 at 32x | 95,000 at 38x | 79,534.3 | Professional-channel pricing and repaint resilience must convert into owner cash after Suvinil, branch/plant capex, raw materials, working capital, debt, and capital returns |
| S&P Global | 3,000 | 4,000 | 5,000 | 84,000 at 28x | 128,000 at 32x | 180,000 at 36x | 121,364.8 | Ratings, subscriptions, indices, benchmarks, and data must remain trusted and recurring after issuance cycles, acquisitions, dispositions, restructuring, NCI, debt, and buybacks |
| Blackstone | 4,500 | 5,700 | 7,000 | 81,000 at 18x | 114,000 at 20x | 168,000 at 24x | 102,794.8 | FRE deserves recurring value, but performance revenues, realizations, partner/NCI claims, compensation, clawbacks, insurance/private-credit risk, and liquidity must remain explicit |
| Ares Management | 1,400 | 1,800 | 2,300 | 25,200 at 18x | 39,600 at 22x | 59,800 at 26x | 29,790.8 | FRE and fee-paying AUM must convert into common-owner value after company-only acquisition cash, credit losses, acquisition compensation, partner/NCI claims, debt, and liquidity risk |
| KKR | 3,500 | 4,500 | 5,800 | 70,000 at 20x | 103,500 at 23x | 150,800 at 26x | 95,579.4 | FRE, monetization, Global Atlantic insurance spread, wealth, and ABF must convert into common-owner value after insurance capital, credit, partner/NCI, preferred, debt, and liquidity claims |

The current market values are not “targets” in this table. The comparison is a
reverse-valuation test:

- Aon’s base case is near, but below, the synchronized equity value. Its upside
  requires both higher normalized cash and a premium multiple, while its
  downside is exposed to the debt/acquisition structure.
- Intuitive’s bull cash case still sits below current equity value at the
  selected 50x sensitivity. That does not disprove the company; it identifies
  a demanding expectation set around durable growth, margins, and reinvestment.
- Vertiv’s bull case is the only one that clears the current equity value in
  this first pass, and it requires both cash to rise well above FY2025 residual
  and a 100x equity-cash sensitivity. The backlog-to-cash test is therefore
  the central valuation risk.
- Wingstop’s base case is close to current equity value, but the margin of
  safety depends on franchisee health and whether buybacks can be funded after
  debt service rather than through balance-sheet expansion.

BlackRock's range is a platform-specific expectation map: the base case only
approaches the synchronized equity value if the mature core produces about
$4.5B of normalized cash and the market awards a 35x multiple while the newer
platform businesses earn their acquisition cost. The bear case assumes fee
compression, lower market levels, and weaker acquisition conversion; the bull
case requires durable flows and technology/private-markets monetization.

T. Rowe Price's base case modestly exceeds current equity value at a 12x
owner-cash sensitivity, but the evidence burden is flow repair rather than
multiple expansion. If fee rates continue falling, the base cash case must be
reduced even if market-driven AUM remains high.

These outputs should be treated as an expectation map, not as a conclusion on
fair value. The next refresh should change a case only when a filing changes a
cash driver, capital requirement, balance-sheet claim, or evidence grade.

## Why the scenario ranges are provisional but not arbitrary

The companion CSV now records the historical residuals that anchor the cases:

| Company | 2023 residual | 2024 residual | 2025 residual | Filing evidence that limits interpretation |
|---|---:|---:|---:|---|
| Aon | 3,148 | (689) | 2,824 | 2024 acquisition cash was unusually large; 2025 includes a business-sale gain in the cash-flow bridge and requires pension/restructuring/debt normalization |
| Intuitive Surgical | 750 | 1,304 | 2,477 | 2023–24 figures exclude any unlisted other investing in this simplified series; 2025 inventory cash use was 1,063 and SBC was 788 |
| Vertiv | 773 | 1,152 | 709 | 2025 includes 1,185 of acquisitions and 339 of working-capital contribution; cash conversion must be tested after both normalize |
| Wingstop | 70 | 92 | 87 | 2025 OCF declined despite higher operating income; residual precedes 33 of dividends, 222 of buybacks, and debt service, while the ad fund has restricted cash |
| T. Rowe Price | 1,751 | 1,891 | 2,127 | Parent OCF less capex and other investing; consolidated-product flows, fee-rate compression, deferred compensation, and timing effects limit direct comparability |

The historical series does not prove normalized owner cash. It does establish
the range of operating outcomes that the scenario cases must explain. The
evidence grade is therefore:

- **Reported cash bridge: A.** Each starting residual is arithmetically tied
  to the filing-backed company memo.
- **Special-item identification: A-/B+.** Business-sale gains, working-capital
  contributions, acquisition spending, inventory use, and restricted cash are
  disclosed, but not every filing provides a clean recurring/non-recurring
  split.
- **Maintenance-capex estimate: C.** None of these filings cleanly labels every
  dollar of capex as maintenance or growth; the model must not hide this gap.
- **Acquisition return: C.** Purchase prices are visible, but post-close
  standalone cash returns and retention are not yet fully disclosed in the
  archive.
- **Scenario cash range: C+.** The ranges are transparent stress assumptions
  anchored to the history and risks; they become stronger only when the next
  filings provide the missing operating detail.

## Latest-quarter evidence check

The archive also contains a limited 2026 quarterly read-through. It is useful
for changing the direction of the next test, but it is not yet a replacement
for a full quarterly GAAP cash-flow bridge.

| Company | Latest packet evidence | What it confirms | What remains unproven | Scenario effect |
|---|---|---|---|---|
| Aon | 1H26 OCF $986M, capex $140M, acquisition cash $322M, and FCF $846M before acquisitions; 5% organic growth and $50M restructuring savings | Client-demand and margin narrative persisted into 2026 | $1.394B short-term-investment sales, $519M other assets/liabilities movement, pensions, restructuring, and acquisition returns | Supports the base operating case, but the cash-quality grade remains B |
| Intuitive Surgical | 1H26 revenue $5.663B, OCF $1.973B, PP&E $215.9M, and acquisition/IP/other investing $528.2M; inventory used $514.6M and deferred-tax adjustment was $370.3M | Installed-base utilization and recurring-use demand remained strong | Whether deferred-tax and working-capital effects reverse; acquisition contribution, SBC, and repurchase bridge | Supports the revenue/procedure case; normalized per-share owner cash remains unproven |
| Vertiv | 1Q26 OCF about $767M and adjusted FCF about $653M; 2Q26 adjusted FCF about $925M, 22.6% adjusted margin, $5.6B liquidity, and net cash; 2026 capex including software guided to $425M–$525M | FY2025 cash conversion was not an isolated quarter and balance-sheet resilience improved | Full GAAP 2Q cash flow, working-capital reversal, warranty/capacity costs, and acquired-business cash return; whether higher capex is growth or recurring burden | Raises confidence in the bull-side conversion path, but the capex step-up and PurgeRite return hurdle keep the base case unproven |
| Wingstop | Q2 2026 10-Q: 26-week OCF $68.3M versus $31.9M; capex $35.9M; domestic same-store sales down 7.5% in Q2 and 8.1% year to date; long-term debt $1.211B | Unit growth, system sales, and parent revenue remain positive while mature domestic demand is weak | Franchisee cash economics, full ad-fund normalization, and whether 2026 technology capex is maintenance or growth | Narrows neither case: the demand case weakens, while the cash bridge improves but is timing-sensitive |
| WESCO | Q2 2026 10-Q: 1H OCF $275.1M, capex $51.6M, receivables $4.685B, inventory $4.418B, net debt $5.177B; Q2 sales $6.665B and data-center sales about $1.5B | Demand, backlog, and first-half cash improved together | Cash still depended on $726M of accounts-payable funding and $192M of other liabilities; normalized turns, project margins, and digital payback remain unproven | Improves the base case from FY2025, but does not justify a bull multiple until cash conversion persists |

Evidence grades after this check:

- **Vertiv quarterly cash confirmation: B+.** Multiple quarters support the
  cash narrative, but the latest free-cash figure is adjusted and does not
  settle the working-capital or acquisition questions.
- **Aon quarterly operating confirmation: B.** Organic growth and margin are
  supported, while cash quality is only partially observable from the packet.
- **Intuitive quarterly demand confirmation: B.** Procedure and revenue
  evidence support the installed-base thesis, but the valuation denominator is
  still an annual cash bridge.
- **Wingstop quarterly confirmation: B-.** The 2026 10-Q supplies the missing
  cash, debt, unit, AUV, and same-store evidence. It still does not disclose
  franchisee cash returns or make the advertising-fund timing fully recurring,
  so the scenario range should remain wide.
- **WESCO quarterly cash confirmation: B-.** The first-half 10-Q confirms a
  meaningful cash recovery and lower reported leverage, but the balance sheet
  still carries substantial receivables and inventory and the cash-flow bridge
  remains dependent on supplier/customer timing. The scenario range should
  stay wide until a full four-quarter conversion cycle is visible.
- **Quanta quarterly confirmation: B-.** First-half OCF increased sharply and
  DSO improved, but $930M of acquisitions and $451M of capex consumed nearly
  all the operating cash after listed uses. Contract assets, retainage, claims,
  and estimate revisions remain central to the normalized denominator.
- **CME quarterly cash confirmation: B+.** First-half OCF of $2.207B against
  $45.4M of property purchases confirms unusually strong conversion, but the
  denominator still requires collateral-interest and volume-cycle normalization.

## Current conclusion from the hurdle analysis

The market is asking different questions of each business. Aon needs proof
that a substantial residual is recurring after capital structure and
acquisitions. Intuitive needs proof that high-quality growth can compound
without a proportional rise in inventory, SBC, and reinvestment. Vertiv needs
proof that the exceptional cycle converts into through-cycle cash. Wingstop
needs proof that an asset-light parent can return capital without weakening the
franchise system or increasing financing dependence.

This is a more useful starting point than ranking the companies by a single
P/E or headline free-cash-flow yield. It makes the narrative-to-numbers bridge
explicit and gives the next filing a measurable job.

## Populated evidence register

Amounts are in millions of dollars unless noted. “Residual after listed uses”
is a screening bridge, not a final owner-earnings estimate. It is calculated as
operating cash flow less the company-specific investment uses listed in the
deep dossier.

| Company | Reference period | Reported operating cash / comparable earnings | Required or visible investment uses | Residual after listed uses | Quality adjustment before valuation | Evidence grade |
|---|---|---:|---:|---:|---|---|
| Aon | FY2025 | OCF 3,481 | Capex 263; net acquisitions 394 | **2,824** | Exclude business-sale gain from recurring cash analysis; separately test restructuring cash, pensions, debt, fiduciary flows, SBC, and acquisition retention | A — full dossier / 10-K |
| Intuitive Surgical | FY2025 | OCF 3,030.5 | PP&E 539.8; acquisitions/IP/other investing 13.9 | **2,476.8** | Treat instruments/services as recurring-use evidence; test inventory build, usage-based lease timing, SBC of 788.2, and repurchases of 2,295.3 | A — full dossier / 10-K |
| Vertiv | FY2025 | OCF 2,113.8 | Capex 220.0; net acquisitions 1,184.8 | **708.9** | Normalize the 339.3 working-capital contribution; test backlog conversion, warranty, capacity, capitalized software, acquisition returns, and customer concentration | A — full dossier / 10-K |
| Wingstop | FY2025 | OCF 153.1 | PP&E 47.4; acquired restaurants 18.5 | **87.1** | Remove 92.5 investment-sale gain from recurring earnings; reconcile advertising-fund timing, SBC 24.9, debt-funded repurchases of 221.9, dividends of 32.4, and debt service | A — full dossier / 10-K |
| WESCO | FY2025 | OCF 125.0 | Capex 99.8; net acquisitions 36.1 | **(10.9)** | Normalize receivables, inventory, supplier terms, digital-platform costs, interest, debt, SBC 40.5, and project/backlog margins | A- — full dossier / 10-K |
| Quanta | FY2025 | OCF 2,230.0 | Capex 609.2; acquisitions 3,052.1; asset acquisition 103.4; integral investments 148.9 | **(1,683.6)** | Test percentage-of-completion estimates, $983.6M year-end unapproved claims, retainage, labor/fleet capex, contingent consideration, M&A returns, SBC 181.9, and dilution | A- — full dossier / 10-K |
| CME | FY2025 | OCF 4,277.1 | Property purchases 83.5; business-venture investments 11.0 | **4,182.6** | Normalize collateral interest/distributions, volume/rate cycle, technology/regulatory resilience, SBC 94.8, and restricted cash; exclude $1,591.4 business-venture sale proceeds from recurring value | A- — full dossier / 10-K |
| BlackRock | FY2025 | OCF 3,927.0 | Capex 375.0; acquisitions 3,496.0; mature-core screen excludes acquisition spend | **3,552.0 mature-core screen** | Separate CIPs/VIEs, Preqin/HPS acquisition returns, amortization, contingent consideration, SBC 1,307, private marks, and dilution | B — full dossier / 10-K |
| T. Rowe Price | FY2025 | Parent OCF 2,489.5 | Capex 274.2; other investing 88.6; consolidated-product flows excluded | **2,126.7** | Normalize timing, fee compression, investment/product marks, deferred compensation, SBC 216.9, restricted capital, and flow repair | A- — full dossier / 10-K |
| Apollo | Q2 2026 / YTD 2026 | FRE 1,513; SRE 1,596; ANI 2,522 YTD | Insurance assets/liabilities, credit losses, HoldCo financing, NCI, principal investment, and compensation are not captured by a simple industrial OCF bridge | **Not comparable** | Value FRE, SRE, principal income, GAAP income, NCI, marks, tax, insurance capital, and cash separately; do not capitalize all ANI as fee income | A — full dossier / 10-K + supplement |

### What the table actually establishes

- Intuitive has the strongest visible conversion in this tranche, but it also
  has the largest disclosed stock-compensation and repurchase burden relative
  to the simple cash bridge. Its platform economics need a utilization and
  reinvestment model, not a software multiple by analogy.
- Aon has substantial residual cash after capex and acquisitions, but the
  residual still precedes debt, pension, restructuring, and dilution tests.
  Its recurring-growth claim is more credible when organic growth survives
  acquisition normalization and compensation growth.
- Vertiv's 2025 residual is much lower than OCF because the company bought a
  large business. That does not make the acquisition bad; it means the
  valuation must explicitly earn the acquisition return instead of treating
  all 2025 OCF as distributable cash. The working-capital release is another
  reason to stress the bridge.
- Wingstop's parent economics look asset-light until the full system is
  included. The residual after PP&E and restaurant purchases was only $87.1M,
  while repurchases were $221.9M. The valuation must therefore include debt
  service and franchisee health, not only royalty growth.
- Apollo cannot be forced into the same denominator. Its fee-related earnings
  may deserve a recurring framework; spread-related earnings require insurance
  and credit normalization; performance and principal income require a
  realization/mark framework.

## Comparable valuation inputs still required

### Four-lane comparable cash bridge

The first comparable screen should expose where reported operating cash stops
being economically distributable. The figures below are 2025 reported values
from the company dossiers; they are a comparison device, not a claim that the
four businesses share the same accounting denominator.

| Company / economic lane | Operating cash flow | Capex / operating investment | Acquisition or restaurant cash | Residual after listed uses | Quality adjustment still required | What the comparison proves |
|---|---:|---:|---:|---:|---|---|
| [Aon](../deep-company-pages/aon-plc.md) — recurring advisory / brokerage | $3,481M | $263M | $394M | $2,824M | Debt, pension, restructuring, client-collection timing, $432M SBC, and acquisition return | A large residual survives listed uses, but leverage and M&A mean it is not automatically equity owner cash |
| [Intuitive Surgical](../deep-company-pages/intuitive-surgical-inc.md) — installed-base procedure workflow | $1,973M | $539.8M | — | $1,433.9M | $1,063.4M inventory investment, $788.2M SBC, instrument/service reinvestment, and $2,295M repurchases | The installed base creates recurring cash, but working capital and SBC materially change the clean-cash read |
| [Vertiv](../deep-company-pages/vertiv-holdings-co.md) — AI power / thermal integration | $2,113.8M | $220.0M | $1,185M | $708.9M | $339.3M working-capital contribution, PurgeRite integration, warranty/capacity needs, and debt | Backlog visibility is not distributable cash when acquisition and working-capital conversion absorb the cash |
| [Wingstop](../deep-company-pages/wingstop-inc.md) — franchised restaurant royalty system | $153.1M | $47.4M | $18.5M | $87.1M | Franchisee health, $24.9M SBC, $221.9M buybacks, $500M securitized debt, and system-level labor/food burden | Parent asset-lightness is real but incomplete: franchisee economics and debt-funded capital return determine durability |
| [Comfort Systems](../deep-company-pages/comfort-systems-usa-inc.md) — skilled-trades MEP execution | $1,186.4M | $154.9M | $279.6M acquisitions + $64.2M investments | $687.7M | $910.1M increase in billings/deferred revenue, $506.5M retainage, cost-to-cost estimates, $21.8M SBC, and earn-outs | Customer-funded working capital is powerful, but backlog still requires labor, project-estimate, and collection discipline |
| [EMCOR](../deep-company-pages/emcor-group-inc.md) — diversified electrical/mechanical execution | $1,302.1M | $112.8M | $1,022.1M acquisitions, offset by $256.6M UK-sale proceeds | $423.8M | Excluding the sale proceeds, residual is about $167.2M; claims, $944.5M retainage, $1.990B net contract liabilities, and acquisition returns remain material | Scale and RPO diversification do not guarantee clean cash when acquisitions and disposition gains dominate capital allocation |
| [Sterling](../deep-company-pages/sterling-infrastructure-inc.md) — mission-critical site and electrical execution | $440.0M | $77.3M | $482.3M acquisitions, offset by $2.0M disposal proceeds | **$(117.6)M** | CEC's $562M purchase price, $79.5M stock consideration, $80M potential earn-out, joint-venture deconsolidation, layered backlog, and $24.2M SBC | Mission-critical mix and high adjusted margins can coexist with negative residual after the acquisition program |

The ranking is therefore not “highest operating cash wins.” Aon has the
largest residual but also the largest financing and acquisition claims;
Intuitive has the cleanest balance sheet but a meaningful inventory and SBC
owner-claim test; Vertiv has the strongest visible demand signal but the most
obvious conversion and acquisition-return reversal; Wingstop has the smallest
parent residual and the clearest mismatch between reported cash and capital
returned. Comfort Systems shows how customer advances can fund a labor-heavy
operator, EMCOR shows how scale can be offset by acquisition spending and a
disposition gain, and Sterling shows how a concentrated mission-critical mix can
require substantial acquisition capital before owner cash appears. This is the
cross-sector bridge the next filing should update rather than a single
free-cash-flow multiple applied to every company.

The following fields are deliberately blank until sourced for the same date and
definition across the full priority set:

| Input | Why it matters | Required source / test |
|---|---|---|
| Current share price and diluted shares | Converts owner cash and equity value into a market-implied multiple | Same-day market snapshot plus latest filing share count; distinguish basic, diluted, and SBC dilution |
| Net debt and restricted / fiduciary cash | Converts equity value to enterprise value and prevents treating unavailable cash as corporate cash | Latest balance sheet, debt footnote, fiduciary/insurance schedules |
| Maintenance versus growth capex | Determines sustainable owner cash and reinvestment rate | Property and equipment note, management capex description, historical replacement needs |
| Normalized working capital | Prevents one-period releases from inflating cash | Three-to-five-year inventory, receivables, contract assets, payables, and deferred revenue bridge |
| Acquisition economics | Tests whether inorganic growth creates value or only scale and amortization | Purchase price, acquired revenue/EBIT, integration cost, retention, goodwill, and post-close cash returns |
| SBC and repurchase-adjusted share count | Tests whether per-share growth is purchased with dilution or leverage | Equity compensation footnote, diluted share roll-forward, repurchase prices and funding |
| Incremental return on capital | Damodaran bridge from narrative growth to value creation | Incremental NOPAT / incremental invested capital, with working capital and maintenance capital included |
| Macro sensitivity | Alden bridge from rates, liquidity, credit, labor, energy, and capex cycles to cash | Debt maturities, variable-rate exposure, customer/funder concentration, pricing and volume disclosures |

### Market-data provenance and refresh rule

The synchronized snapshot is a dated market-data input from the finance feed,
not a filing fact. On every refresh, record the timestamp, price, equity value,
currency, split status, and the latest filing date. Do not mix this snapshot
with a different day's price or with a basic share count. A valuation output
is not considered reproducible until those fields and the source retrieval
date are stored together.

## Company-specific valuation models

### Aon: fee stream plus capital-allocation normalization

The initial model should start with recurring advisory and brokerage cash, not
reported revenue alone:

`organic revenue x normalized operating margin -> after-tax operating profit -> capex / technology / pensions -> acquisition cash and debt cost -> diluted owner cash`

The 2025 cash bridge is encouraging, but the $1.201B business-sale gain must
not be used to justify a perpetual cash-growth rate. The key Damodaran inputs
are organic growth durability, margin after restructuring savings expire, and
returns on acquired client relationships. The key Alden inputs are commercial
risk pricing, economic activity, rates, and corporate risk budgets. A valuation
should show a base case where 6% organic growth moderates and a downside case
where acquisition activity and debt service consume more of the residual.

### Intuitive Surgical: installed-base cash flow with reinvestment

The model should separate the three engines:

`systems placements -> instruments and accessories utilization -> services / software -> manufacturing and clinical reinvestment`

The 2025 residual of $2.477B is a starting point, not a terminal owner-cash
number. Inventory used $1.063B of cash, PP&E purchases were $539.8M, and SBC
was $788.2M. The valuation must ask whether procedure growth can continue with
lower inventory intensity, what capital is required for Ion and da Vinci
capacity, and how much repurchase spending is needed simply to offset equity
compensation. The major reverse-valuation risk is paying for many years of
procedure growth while assuming current margins and capital intensity remain
unchanged.

### Vertiv: backlog conversion and acquisition return

The model should not capitalize the $15B backlog directly. It should model:

`backlog -> shipments -> gross margin -> working-capital requirement -> warranty / service burden -> capex -> acquisition returns`

The $708.9M 2025 residual is informative because $1.185B of acquisition cash
was spent. The next step is to identify the acquired business's incremental
profit and cash, then calculate an acquisition-adjusted return on invested
capital. The 2025 working-capital contribution of $339.3M also deserves a
reversal stress. If backlog grows while inventory and receivables consume cash,
the market's implied terminal margin is too generous. If conversion remains
strong after the working-capital release reverses, the control-point thesis
gets materially stronger.

### Wingstop: royalty economics constrained by system health

The model must run at two levels:

`franchisee unit economics -> system sales / traffic -> royalty and advertising flows -> parent cash -> debt and capital returns`

Parent residual cash was $87.1M before dividends, buybacks, and debt service,
while buybacks were $221.9M. The 2025 investment-sale gain of $92.5M makes
reported net income especially unsuitable as the base for a valuation multiple.
The critical questions are whether franchisees can fund labor, food, remodels,
and openings; whether domestic traffic recovers; and whether the parent can
return capital without relying on new debt or asset sales.

### Cheniere: export bottleneck with a train-level reinvestment hurdle

The model should separate existing-train owner cash from Stage 3 growth:

`contracted LNG volumes -> train utilization / realized margin -> feed-gas and hedge settlement -> maintenance capex -> growth-train returns -> debt and buybacks`

The FY2025 post-capex residual was $2.461B, while repurchases and dividends
totaled $3.175B. The valuation register therefore uses a $3.0B base case only
as a normalized scenario, not as a claim that the current residual is already
steady-state owner cash. The key reverse-valuation test is whether completed
trains lower capex intensity and produce physical cash after derivative marks
and debt, rather than merely higher adjusted DCF.

### Energy Transfer: corridor cash after the partnership waterfall

Energy Transfer's model is:

`basin and export volumes -> contracted segment margin -> maintenance capex -> growth projects / acquisitions -> interest and debt -> NCI, affiliate, and common-unit distributions`

The FY2025 consolidated residual was $3.846B after productive-asset spending,
but $68.3B of long-term debt and the ownership waterfall prevent assigning that
amount directly to common units. The scenario range is consequently below the
reported adjusted-EBITDA narrative unless project returns and leverage
stabilization are demonstrated. Lake Charles LNG's suspension is a positive
allocation signal, but the replacement projects still need a realized-return
test.

### United Rentals: access economics with a fleet-replacement hurdle

United Rentals' model is:

`fleet density and specialty relevance -> utilization / rental rate -> gross margin -> replacement and growth fleet capex -> through-cycle owner cash`

FY2025 management-defined FCF was $2.181B, but acquisitions consumed $357M,
and repurchases plus dividends totaled $2.433B. The base scenario therefore
requires $2.2B of normalized cash and a 24x sensitivity, while the current
equity value requires either a materially stronger cash outcome or a premium
multiple. The key reverse-valuation test is whether fleet productivity and
resale economics remain strong after project demand normalizes.

### Ecolab: embedded service with acquisition-return proof

Ecolab's model is:

`embedded water / hygiene / compliance workflow -> organic price and service growth -> field productivity -> maintenance capex -> acquisition returns -> owner cash`

FY2025 OCF less PP&E and acquisition/affiliate cash was only $283M, while
buybacks and dividends totaled $1.538B. The $800M base scenario therefore
assumes a recovery from the acquisition-heavy year and requires Ovivo/high-tech
and life-science growth to produce incremental cash. The market's higher value
requires proof that Ecolab is a recurring operating platform rather than a
premium multiple on a capital-intensive roll-up.

### Nucor: steel-cycle cash after the capacity program

Nucor's model is:

`scrap and raw materials -> EAF utilization / realized steel price -> downstream mix -> maintenance and growth capex -> mid-cycle owner cash`

FY2025 OCF less PP&E and acquisitions was $(190)M. The $1.5B base scenario
assumes a normalized recovery but remains far below the $59.3B market value;
the $3.0B bull case only approximately clears it at 20x. The reverse-valuation
test is whether new capacity and value-added products earn through a steel
downcycle, not whether Q2 2026 EBITDA was strong.

### Apollo: sum-of-the-parts with a credit-cycle haircut

Apollo requires a sum-of-the-parts structure:

1. Capitalize normalized FRE using fee growth, fee rates, retention, and
   compensation/reinvestment requirements.
2. Value SRE using normalized spread after credit losses, funding costs,
   duration, policyholder obligations, and required insurance capital.
3. Value performance and principal income on realized, through-cycle cash
   returns, not current marks or management's long-term return assumption.
4. Subtract HoldCo debt, taxes, NCI, preferred claims, and compensation costs.

The Q2 2026 supplement's $1.513B YTD FRE and $1.596B YTD SRE show scale, but
they are not interchangeable. The Q1 2026 GAAP loss of $1.930B attributable to
common stockholders alongside $1.208B ANI is a useful reminder that the
reconciliation is economically important. The next valuation version should
run a credit-loss, spread-compression, and delayed-realization case before
assigning a premium multiple. The [Apollo memo's provisional SOTP sensitivity](../deep-company-pages/apollo-global-management-inc.md)
now makes those separate denominators and the unresolved common-shareholder
claims explicit; it remains outside the ordinary 43-row cash register.

## Next data collection order

1. Refresh the synchronized market-price date and diluted share count across
   the 43-row scenario register.
2. Add net debt, restricted/insurance/fiduciary cash, and debt maturity data.
3. Build three-year normalized working-capital and capex bridges.
4. Add acquisition returns and SBC-adjusted per-share cash.
5. Extend the same fields to the clean-control and contradiction cohorts in the
   cross-sector watchlist.
6. Only then calculate base, bear, and bull implied returns; preserve the
   market-implied growth and margin assumptions rather than burying them in a
   target price.

## Companion evidence

- [Aon full forensic memo](../deep-company-pages/aon-plc.md)
- [Apollo full forensic memo](../deep-company-pages/apollo-global-management-inc.md)
- [Intuitive Surgical full forensic memo](../deep-company-pages/intuitive-surgical-inc.md)
- [Vertiv full forensic memo](../deep-company-pages/vertiv-holdings-co.md)
- [Wingstop full forensic memo](../deep-company-pages/wingstop-inc.md)
- [WESCO full forensic memo](../deep-company-pages/wesco-international-inc.md)
- [Quanta full forensic memo](../deep-company-pages/quanta-services-inc.md)
- [CME full forensic memo](../deep-company-pages/cme-group-inc.md)
- [BlackRock full forensic memo](../deep-company-pages/blackrock-inc.md)
- [T. Rowe Price full forensic memo](../deep-company-pages/t-rowe-price-group-inc.md)
- [Marriott full forensic memo](../deep-company-pages/marriott-international-inc.md)
- [Host Hotels & Resorts full forensic memo](../deep-company-pages/host-hotels-resorts-inc.md)
- [Cheniere full forensic memo](../deep-company-pages/cheniere-energy-inc.md)
- [Energy Transfer full forensic memo](../deep-company-pages/energy-transfer-lp.md)
- [United Rentals full forensic memo](../deep-company-pages/united-rentals-inc.md)
- [Ecolab full forensic memo](../deep-company-pages/ecolab-inc.md)
- [Nucor full forensic memo](../deep-company-pages/nucor-corporation.md)
- [Baxter full forensic memo](../deep-company-pages/baxter-international-inc.md)
- [Fastenal full forensic memo](../deep-company-pages/fastenal-company.md)
- [Ferguson full forensic memo](../deep-company-pages/ferguson-enterprises-inc.md)
- [Grainger full forensic memo](../deep-company-pages/ww-grainger-inc.md)
- [Core & Main full forensic memo](../deep-company-pages/core-main-inc.md)
- [Stryker full forensic memo](../deep-company-pages/stryker-corporation.md)
- [Henry Schein full forensic memo](../deep-company-pages/henry-schein-inc.md)
- [McKesson full forensic memo](../deep-company-pages/mckesson-corporation.md)
- [Cencora full forensic memo](../deep-company-pages/cencora-inc.md)
- [Cardinal Health full forensic memo](../deep-company-pages/cardinal-health-inc.md)
- [KLA full forensic memo](../deep-company-pages/kla-corporation.md)
- [F5 full forensic memo](../deep-company-pages/f5-inc.md)
- [Equinix full forensic memo](../deep-company-pages/equinix-inc.md)
- [Digital Realty full forensic memo](../deep-company-pages/digital-realty-trust-inc.md)
- [Generac full forensic memo](../deep-company-pages/generac-holdings-inc.md)
- [Chipotle full forensic memo](../deep-company-pages/chipotle-mexican-grill.md)
- [McDonald's full forensic memo](../deep-company-pages/mcdonalds-corporation.md)
- [Cross-sector economic-control and forensic watchlist](../cross-sector/cross-sector-economic-control-and-forensic-watchlist-2026-09-13.md)

Filing anchors for the share-count and balance-sheet refresh: [Aon 2025
Form 10-K](https://www.sec.gov/Archives/edgar/data/315293/000162828026008116/aon-20251231.htm),
[Intuitive Surgical 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1035267/000103526726000010/isrg-20251231.htm),
[Vertiv 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm),
and [Wingstop 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1636222/000163622226000008/wing-20251227.htm).

Hotel control-point anchors: [Marriott 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1048286/000104828626000007/mar-20251231.htm)
and [Host Hotels & Resorts 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1070750/000107075026000054/hst-20251231.htm).

The KLA filing anchor is [KLA FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/319201/000031920126000027/klac-20260630.htm).

## Skeptical Reader Test

- Does “residual” subtract the investment required by that company's actual
  operating model?
- Are business-sale gains, working-capital releases, marks, NCI, debt, and SBC
  kept visible?
- Does each valuation model use the right economic denominator rather than
  forcing every company into FCF or ANI?
- Are market price and valuation expectations explicitly sourced rather than
  implied from business quality?
