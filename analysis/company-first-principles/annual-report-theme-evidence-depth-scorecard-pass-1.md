# Annual Report Theme Evidence Depth Scorecard Pass 1

## Purpose

This pass answers the practical question after the company-to-theme matrix:

`Which themes are already strongly supported by local evidence, and which themes are still mostly writing candidates that need more company extraction?`

The companion table is:

`analysis/company-first-principles/data/annual-report-theme-evidence-depth-scorecard-pass-1.csv`

The extraction workbench that turns this scorecard into source-pull tasks is:

`/cluster/annual-report-theme-extraction-workbench-pass-1.md`

## Verdict

`theme-evidence-depth-scorecard-ready`

The `75` company rows are useful, but they are not all equally proven. The current evidence split is:

| Claim Status | Rows | Meaning |
|---|---:|---|
| source-visible-with-boundary | 38 | The folder already has local source-visible evidence or a stronger extracted proof packet, but still with limits. |
| theme-candidate | 37 | The company is a good example for the theme, but needs annual-report or filing extraction before strong company-specific claims. |
| queued-theme-candidate | 0 | No company-to-theme matrix row remains explicitly queued after the built-environment Sherwin-Williams pass. |

## Readiness By Theme

| Theme | Source-Visible Rows | Candidate Rows | Queued Rows | Readiness |
|---|---:|---:|---:|---|
| Power scarcity | 4 | 1 | 0 | high-theme-readiness |
| Capital platforms | 5 | 0 | 0 | high-theme-readiness |
| Energy affordability and supply route | 4 | 1 | 0 | high-theme-readiness |
| Industrial uptime | 1 | 4 | 0 | medium-theme-readiness |
| Basic materials and input scarcity | 1 | 4 | 0 | medium-theme-readiness |
| Services and cultural consumption | 0 | 5 | 0 | medium-theme-readiness |
| Consumer goods and household identity | 0 | 5 | 0 | medium-theme-readiness |
| Real estate and scarce locations | 0 | 5 | 0 | medium-theme-readiness |
| Broad technology beyond internet software | 0 | 5 | 0 | medium-theme-readiness |
| Healthcare tools and medical infrastructure | 0 | 5 | 0 | medium-theme-readiness |
| Ordinary finance | 3 | 2 | 0 | medium-theme-readiness-three-anchors-started |
| Healthcare access | 5 | 0 | 0 | high-theme-readiness |
| Built-environment upkeep | 5 | 0 | 0 | high-theme-readiness-first-pass-complete |
| Digital control | 5 | 0 | 0 | high-theme-readiness-first-pass-complete |
| Value retail | 5 | 0 | 0 | high-theme-readiness |

## What This Means In Plain English

The strongest themes right now are not necessarily the most interesting themes. They are the themes where the folder already contains the most concrete source work.

Power scarcity, capital platforms, and energy route evidence are strongest because prior work already chased filings, regulatory dockets, statutory schedules, credit packets, tariffs, backlog, DCF, project/cash-proxy material, and now a bounded BlackRock platform extraction. These themes can carry detailed writing now, as long as the writing preserves the boundary: source-visible evidence is not the same as final named-cash proof.

The middle group is writing-ready but not yet company-proof-rich. Industrial uptime has strong United Rentals work, but Fastenal, WESCO, Grainger, and Applied Industrial need their own extraction. Basic materials has Steel Dynamics, but copper, aggregates, fertilizer, and broader steel examples still need company work. Services, consumer goods, real estate, broad technology, healthcare tools, and ordinary finance are conceptually strong but mostly need annual-report extraction if the final product wants company-level confidence.

The weaker group is not weak as a theme. It is weaker as extracted evidence. Built-environment upkeep now has five source-visible companies and its first-pass packet is complete: Home Depot supports the housing-upkeep and Pro-distribution version of the theme; Lowe's supports the service-widened home-improvement, online, loyalty, home-services, and Pro-workflow version; Core & Main supports the civic waterworks and infrastructure-replacement version; Builders FirstSource supports the professional builder workflow, prefabrication, value-added component, and housing-production efficiency version; and Sherwin-Williams supports the coatings, repaint, contractor-access, surface-renewal, controlled-distribution, and pricing-discipline version. Digital control has moved into first-pass complete status because all five selected companies are now source-visible with boundary: Cloudflare supports the newer edge-control platform version of the theme, Akamai supports the incumbent delivery-to-security and distributed-cloud transition version, Zscaler supports the Zero Trust access-policy version, Fortinet supports the hardware-attached security enforcement version, and Roblox supports the governed digital-participation and virtual-economy version. Healthcare access has now moved into the strongest first-pass group because UnitedHealth, Cigna, DaVita, Addus, and Option Care are all source-visible with boundary: payer control, benefits/pharmacy routing, recurring dialysis care-site delivery, home-care labor/reimbursement, and alternate-site infusion are all represented. Value retail is also first-pass company-proof-rich because Costco, Walmart, Target, Dollar General, and Burlington are all source-visible with boundary.

## What To Do Next

The next work should not be a new theme brainstorm. The next work should be targeted extraction:

1. Finish the high-value evidence lanes first: FPL/NextEra, Duke, AEP, MasTec, Sterling, BlackRock, Blackstone, Apollo/Athene, KKR/Global Atlantic, Brookfield, Energy Transfer, ONEOK, Plains, Cheniere, and Exxon.
2. Build a retail pressure packet: Costco, Walmart, Target, Dollar General, and Burlington. This first-pass packet is now complete; the next move is cash-quality proof across traffic, ticket, inventory, shrink, margin, fulfillment, renewal, and operating cash flow.
3. Move healthcare access from first-pass company coverage to second-pass cash-quality proof across UnitedHealth, Cigna, DaVita, Addus, and Option Care.
4. Move digital control from cash-quality bridge pass 1 to primary cash-quality extraction: Cloudflare, Akamai, Zscaler, Fortinet, and Roblox are now source-visible with boundary, and `/cluster/annual-report-digital-control-cash-quality-bridge-pass-1.md` identifies the exact missing proof fields. Continue broad technology separately with Microsoft, NVIDIA, Broadcom, Cisco, and ServiceNow.
5. Move built-environment upkeep from cash-quality bridge pass 1 to primary cash-quality extraction: Home Depot, Lowe's, Core & Main, Builders FirstSource, and Sherwin-Williams are now source-visible with boundary, and `/cluster/annual-report-built-environment-cash-quality-bridge-pass-1.md` identifies the exact missing proof fields.
6. Continue the ordinary finance packet: JPMorgan, American Express, and Capital One are now source-visible with boundary; Progressive and Visa still need first-pass extraction.

## Safe Use

Use this scorecard to decide where the writing is already strongest and where the next extraction should go.

Do not use this scorecard to claim that all `75` company examples have equal source depth. They do not.

## Decision Marker

`annual-report-theme-evidence-depth-scorecard-pass-1-ready`
