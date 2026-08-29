# Annual Report Company-To-Theme Matrix Pass 1

## Purpose

This pass adds the missing company layer under the theme work.

The theme pages explain the big ideas. This matrix answers the next question:

`Which companies should we read first for each theme, what does each company show, how does the money move, and what proof is still missing?`

The companion table is:

`analysis/company-first-principles/data/annual-report-company-to-theme-matrix-pass-1.csv`

The evidence-depth scorecard for this matrix is:

`/cluster/annual-report-theme-evidence-depth-scorecard-pass-1.md`

## Verdict

`company-to-theme-matrix-ready`

The annual-report project now has `75` company-to-theme rows across `15` themes. Each theme has `5` starting companies. The rows do not claim that every company has complete named-cash proof. They show which companies are useful examples, what each company is actually doing, how it gets paid, what metric to check, and what would disprove the theme claim.

## How To Read This

A theme is not a stock pick. A theme is a repeated pressure in the real economy.

A company belongs in a theme only if it sits on a real path where need turns into money. The useful question is not "is this company exposed to AI, healthcare, housing, or consumers?" The useful question is:

`What need does this company satisfy, who pays it, what proof shows the payment path is real, and what would break the claim?`

That is why the table uses plain fields:

| Field | Meaning |
|---|---|
| theme | The big pattern. |
| subtheme | The smaller mechanism inside the pattern. |
| company | The company to read first. |
| why it belongs | Why this company is relevant to the theme. |
| what it does plain | What the business actually does in ordinary words. |
| how it gets paid | Where cash or revenue comes from. |
| proof metric to check | The evidence that separates a real claim from a story. |
| what would disprove | The event or metric that would make the claim weaker. |

## Theme 1: Power Scarcity

Power scarcity means electricity has become a gate on growth. A company can want more computing, manufacturing, cooling, housing, or logistics capacity, but none of it works without deliverable electricity.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| NextEra Energy / FPL | The clearest local example of utility capital moving toward regulated recovery. | Utility capex -> rate filing -> approved factor or rate -> customer bill -> collected utility cash. |
| Duke Energy | Large regulated utility capex and customer recovery. | Grid and generation spending -> regulated rate base -> customer payments. |
| American Electric Power | Transmission and wires as scarce assets. | Transmission investment -> regulated tariff/recovery -> cash flow. |
| MasTec | Power plans becoming field construction backlog. | Utility/customer project -> contractor work -> progress billing -> cash collection. |
| Sterling Infrastructure | Infrastructure backlog, contract liabilities, and cash conversion. | Project award -> work performed -> cash receipts -> debt capacity and reinvestment. |

The main warning: load growth is not the same thing as profit. The proof has to reach approved recovery, billing determinants, collection, and debt-service coverage.

## Theme 2: Capital Platforms

Capital platforms are money-routing machines. They collect money from pensions, insurers, retirement savers, institutions, wealthy households, ETFs, and credit allocators, then route it into assets and borrowers.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| BlackRock | Public-market access, portfolio workflow, ETFs, and expanding private-market capability. | Saver/institution money -> funds/ETFs/models -> fees and market exposure. |
| Blackstone | Private credit, real estate, infrastructure, insurance-client capital, and deployment scale. | Institutions/insurers/wealth clients -> private funds/SMAs -> assets/borrowers -> fees and realization. |
| Apollo / Athene | Retirement liabilities becoming credit and spread assets. | Retirement/insurance liabilities -> invested assets -> spread income and management fees. |
| KKR / Global Atlantic | Private markets plus affiliated insurance capital. | Insurance and institutional capital -> credit/infrastructure/private assets -> fees, spread, investment income. |
| Brookfield | Hard assets, infrastructure, real estate, credit, and insurance assets. | Investor/insurance capital -> operating assets -> cash yield, fees, carried interest. |

BlackRock source status: `/cluster/annual-report-blackrock-capital-platform-extraction-pass-1.md` upgrades BlackRock to platform-scale source-visible with boundary. It supports BlackRock as the whole-portfolio infrastructure example, but it still does not prove named HPS borrower cash proof.

The main warning: AUM is not proof that money reached a named borrower or asset. Full proof needs legal-entity schedules, asset rows, borrower documents, cash receipts, and return models.

## Theme 3: Industrial Uptime

Industrial uptime means physical work has to keep running. The value is not glamorous. It is the prevention of stoppage: available equipment, parts, tools, inventory, technicians, branches, and project execution.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| United Rentals | Equipment availability and fleet cash yield. | Customer rents equipment -> rental revenue -> fleet utilization -> cash flow. |
| Fastenal | Small parts, onsite supply, vending, and repeat industrial usage. | Customer uses parts -> replenishment sales -> branch/onsite margin. |
| WESCO | Electrical, communications, utility, and automation distribution. | Project demand -> product sale -> working-capital conversion. |
| Grainger | Maintenance, repair, and operating supply at scale. | Facility need -> product purchase -> repeat customer revenue. |
| Applied Industrial Technologies | Technical parts and repair knowledge. | Plant maintenance need -> specialized parts/service -> margin and cash. |

The main warning: sales growth is not enough. The proof must show inventory is turning, receivables are collected, fleet earns above capital cost, and backlog becomes cash.

## Theme 4: Healthcare Access

Healthcare access means medical need has to become actual care. That requires scheduling, staff, authorization, reimbursement, drugs, devices, sites, billing, and trust.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| UnitedHealth Group | Payer, care delivery, data, and pharmacy routing in one system. | Premiums/service fees -> claims/care management -> operating cash. |
| Cigna | Insurance and pharmacy-benefit routing. | Employer/member premiums and pharmacy services -> claims management -> cash flow. |
| DaVita | Repeated chronic care through dialysis sites. | Treatments -> payer reimbursement -> site-level cash. |
| Addus HomeCare | Care shifting into the home. | Billable care hours -> Medicaid/managed-care/private-pay reimbursement. |
| Option Care Health | Complex drug therapy outside hospitals. | Referral -> infusion service and drug dispensing -> payer reimbursement. |

The main warning: revenue does not prove good care. The evidence has to address reimbursement quality, staffing, patient outcomes, collections, and whether the business model improves access or only controls claims.

UnitedHealth source status: `/cluster/annual-report-unitedhealth-healthcare-access-extraction-pass-1.md` upgrades UnitedHealth to source-visible with boundary. It supports UnitedHealth as the healthcare control-plane example, but it still does not prove patient outcomes, fair access, low friction, transparent pharmacy economics, or full payer-to-provider cash collection.

Cigna source status: `/cluster/annual-report-cigna-healthcare-routing-extraction-pass-1.md` upgrades Cigna to source-visible with boundary. It supports Cigna as the benefits and pharmacy-services routing example, but it still does not prove patient affordability, fair access, better outcomes, transparent PBM economics, or full healthcare cash collection.

DaVita source status: `/cluster/annual-report-davita-care-site-extraction-pass-1.md` upgrades DaVita to source-visible with boundary. It supports DaVita as the recurring dialysis treatment-site example, but it still does not prove patient outcomes, affordability, payer-mix durability, risk-contract profitability, or treatment-level cash receipts.

Addus source status: `/cluster/annual-report-addus-home-care-extraction-pass-1.md` upgrades Addus to source-visible with boundary. It supports Addus as the aging-in-place home-care labor and reimbursement example, but it still does not prove patient outcomes, caregiver adequacy, state-rate durability, acquisition returns, or service-line cash collection.

Option Care source status: `/cluster/annual-report-option-care-infusion-extraction-pass-1.md` upgrades Option Care to source-visible with boundary and completes the first-pass healthcare-access company packet. It supports Option Care as the home and alternate-site infusion example, but it still does not prove patient outcomes, therapy-level margin, reimbursement durability, nurse capacity, drug-supply reliability, or working-capital cash conversion.

## Theme 5: Built-Environment Upkeep

Built-environment upkeep means homes, stores, roads, pipes, water systems, and buildings keep aging. The world needs repair and replacement even when new construction slows.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Home Depot | Repair, remodel, contractor demand, and home project spending. | Household/pro purchase -> retail margin -> inventory/cash conversion. |
| Lowe's | Home improvement, appliances, and project retail. | Store/digital sale -> margin -> free cash flow. |
| Core & Main | Waterworks and civic infrastructure replacement. | Municipal/utility project -> distributor sale -> branch cash. |
| Builders FirstSource | Housing materials and value-added components. | Builder demand -> building products -> component and distribution margin. |
| Sherwin-Williams | Repainting, coatings, surface renewal, and contractor accounts. | Paint/coatings sale -> brand/store margin -> working-capital cash. |

Home Depot source status: `/cluster/annual-report-home-depot-built-environment-extraction-pass-1.md` upgrades Home Depot to source-visible with boundary. It supports Home Depot as the housing-upkeep and Pro-trade distribution example: repair, remodel, maintenance, stores, digital channels, SRS/GMS distribution, delivery assets, trade support, and cross-sell all sit in one built-environment system. It does not prove healthy housing demand, recovered large-project demand, SRS/GMS acquisition return, branch-level profitability, or complete repair/remodel cash quality.

Lowe's source status: `/cluster/annual-report-lowes-built-environment-extraction-pass-1.md` upgrades Lowe's to source-visible with boundary. It supports Lowe's as the service-widened home-improvement workflow example: stores, online, home services, loyalty, Pro penetration, branch locations, distribution centers, appliances, repair/remodel, project execution, and acquisition-backed building-products expansion sit in one system. It does not prove healthy housing demand, full Pro-channel profitability, home-services margin, online cash quality, loyalty economics, acquisition return, or project-level cash collection.

Core & Main source status: `/cluster/annual-report-core-main-built-environment-extraction-pass-1.md` upgrades Core & Main to source-visible with boundary. It supports Core & Main as the waterworks, storm-drainage, wastewater, fire-protection, smart-utility, and civic-infrastructure distribution example: municipalities, private water companies, contractors, developers, branch inventory, supplier relationships, project specifications, and field infrastructure work sit in one channel system. It does not prove municipal receipts, funded project conversion, acquisition cash return, branch-level profitability, receivable collection, inventory turns, or complete working-capital cash quality.

Builders FirstSource source status: `/cluster/annual-report-builders-firstsource-built-environment-extraction-pass-1.md` upgrades Builders FirstSource to source-visible with boundary. It supports Builders FirstSource as the professional builder workflow, value-added component, prefabrication, turnkey service, digital workflow, and housing-production efficiency example. It does not prove housing recovery, value-added margin durability, prefabrication adoption, software-like digital economics, customer payment quality, inventory cash conversion, or through-cycle return.

Sherwin-Williams source status: `/cluster/annual-report-sherwin-williams-built-environment-extraction-pass-1.md` upgrades Sherwin-Williams to source-visible with boundary and completes the first-pass built-environment company packet. It supports Sherwin-Williams as the coatings, repaint, surface-renewal, contractor-access, controlled-distribution, raw-material, and pricing-power example. It does not prove housing recovery, contractor-level cash collection, branch-level profitability, price-increase durability, price-versus-volume quality, raw-material pass-through success, receivable quality, or segment-level free-cash-flow conversion.

The main warning: demand language does not prove cash return. The proof has to show branch economics, project funding, inventory turns, acquisition returns, and customer payment.

## Theme 6: Digital Control

Digital control means more online activity creates more need for permission, security, routing, identity, moderation, and workflow.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Cloudflare | Edge network, application security, and traffic control. | Subscription/usage contract -> platform revenue -> cash flow. |
| Akamai | Content delivery, edge security, and traffic routing. | Enterprise/media traffic -> delivery/security fees -> margin. |
| Zscaler | Zero-trust access and identity-based security. | Seat/module subscription -> enterprise expansion -> cash. |
| Fortinet | Hardware plus recurring security services. | Appliance sale -> subscription renewal -> deferred revenue and cash. |
| Roblox | Digital participation, virtual spending, moderation, and creator economy. | User purchase -> deferred revenue/bookings -> platform economics. |

Cloudflare source status: `/cluster/annual-report-cloudflare-digital-control-extraction-pass-1.md` upgrades Cloudflare to source-visible with boundary. It supports Cloudflare as the protected-edge, application-security, Zero Trust, developer-runtime, AI Gateway, and machine-traffic governance example. It does not prove durable GAAP profitability, retention quality, infrastructure-cost discipline, AI-agent monetization, or clean software-like free-cash-flow conversion.

Akamai source status: `/cluster/annual-report-akamai-digital-control-extraction-pass-1.md` upgrades Akamai to source-visible with boundary. It supports Akamai as the delivery-to-security and distributed-cloud transition example: mature internet delivery, application protection, API security, segmentation, CIS contracts, and AI-linked infrastructure commitments. It does not prove the legacy delivery drag is solved, CIS contracts become high-return cash, or AI infrastructure demand automatically creates durable operating leverage.

Zscaler source status: `/cluster/annual-report-zscaler-digital-control-extraction-pass-1.md` upgrades Zscaler to source-visible with boundary. It supports Zscaler as the Zero Trust access, AI-security, and enterprise policy-control example: users, devices, workloads, apps, data flows, and AI agents all need permission rules. It does not prove permanent platform control, GAAP profitability, acquisition integration success, AI-agent monetization, or immunity from bundled security competition.

Fortinet source status: `/cluster/annual-report-fortinet-digital-control-extraction-pass-1.md` upgrades Fortinet to source-visible with boundary. It supports Fortinet as the hardware-attached security-control example: firewalls, branch enforcement, service subscriptions, SASE, OT security, FortiGuard AI Services, billings, deferred revenue, and free cash flow. It does not prove permanent product-cycle strength, channel immunity, SASE dominance, AI-security monetization, renewal durability, or full product-level cash quality.

Roblox source status: `/cluster/annual-report-roblox-digital-control-extraction-pass-1.md` upgrades Roblox to source-visible with boundary. It supports Roblox as the governed digital-participation example: users, creators, virtual currency, discovery, communication, safety, age policy, developer payouts, bookings, and cash flow sit inside one digital-world system. It does not prove clean cash conversion, durable monetization per hour, solved moderation risk, creator health, safety outcomes, or frictionless expansion from youth gaming into broad social infrastructure.

The main warning: users, traffic, or ARR do not automatically prove durable value. The proof needs retention, cash conversion, gross margin, infrastructure cost, and product-level profitability.

## Theme 7: Value Retail

Value retail means households are trying to reduce regret. They want a basket that feels acceptable: low price, trusted product, convenient store, return policy, membership value, or discounted brand.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Costco | Membership-supported bulk value and trust. | Member fee plus merchandise sales -> renewal and cash flow. |
| Walmart | Basket consolidation across grocery, general merchandise, pharmacy, ads, and e-commerce. | Store/digital basket -> scale margin and service revenue. |
| Target | Middle-income pressure and discretionary sensitivity. | Store basket -> margin, markdown risk, and cash conversion. |
| Dollar General | Lower-income and rural budget pressure. | Small basket repeat trips -> consumables margin. |
| Burlington | Off-price discretionary shopping. | Discounted inventory buy -> retail sale -> merchandise margin. |

Costco source status: `/cluster/annual-report-costco-value-retail-extraction-pass-1.md` upgrades Costco to source-visible with boundary. It supports Costco as the paid-access trusted-value example, but it still does not prove full consumer health or unlimited membership pricing power.

Walmart source status: `/cluster/annual-report-walmart-value-retail-extraction-pass-1.md` upgrades Walmart to source-visible with boundary. It supports Walmart as the basket-consolidation and retail-ecosystem example, but it still does not prove full consumer health or eCommerce cash quality.

Target source status: `/cluster/annual-report-target-discretionary-stress-extraction-pass-1.md` upgrades Target to source-visible with boundary. It supports Target as the pressured-middle repair case, but it still does not prove middle-income consumer health or durable second-layer cash quality.

Dollar General source status: `/cluster/annual-report-dollar-general-value-retail-extraction-pass-1.md` upgrades Dollar General to source-visible with boundary. It supports Dollar General as the neighborhood replenishment and proximity-value example, but it still does not prove lower-income consumer health or durable low-ticket cash quality.

Burlington source status: `/cluster/annual-report-burlington-off-price-value-extraction-pass-1.md` upgrades Burlington to source-visible with boundary. It supports Burlington as the off-price bargain-discovery and status-preservation example, but it still does not prove durable discretionary health or full inventory-to-cash quality.

The main warning: low price can still be a bad business if shrink, wages, freight, markdowns, or inventory destroy margin.

## Theme 8: Services And Cultural Consumption

Services show what people still pay for after basic goods: time, convenience, travel, habit, entertainment, relief, status, and connection.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Marriott | Travel demand through brands and franchise fees. | Hotel owner/customer activity -> franchise and management fees. |
| Booking Holdings | Travel demand through digital marketplace control. | Booking volume -> commission/take rate -> cash flow. |
| McDonald's | Convenience, low-ticket routine, and franchising. | Customer meal -> franchise royalty/rent and store sales. |
| Starbucks | Daily habit, loyalty, and small personal reward. | Beverage transaction -> store margin and loyalty reuse. |
| MGM Resorts | Experience spending, gaming, events, and lodging. | Guest trip -> room, gaming, food, entertainment revenue. |

The main warning: service revenue does not automatically mean the consumer is healthy. Credit usage, discounting, traffic, and margin tell whether demand is durable.

## Theme 9: Consumer Goods And Household Identity

Consumer goods show how households defend routines and identity. Cleaning, oral care, beauty, snacks, drinks, toys, and small indulgences can be psychologically important even when budgets are pressured.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Procter & Gamble | Daily household trust and repeated product use. | Repeat purchase -> pricing/mix -> branded cash flow. |
| Colgate-Palmolive | Oral care and global personal-care habits. | Daily-use products -> market share and margin. |
| Estee Lauder | Prestige beauty, gifting, travel retail, and identity. | Brand sale -> channel margin and inventory conversion. |
| Coca-Cola | Low-ticket beverage habit and distribution. | Concentrate/finished product sale -> bottler and brand economics. |
| Hasbro | Toys, games, licensing, and family spending. | Retail/ licensing sale -> entertainment-linked cash. |

The main warning: brand strength has to show up in volume, price/mix, shelf position, repeat purchase, and cash, not only in advertising language.

## Theme 10: Basic Materials And Input Scarcity

Every abstract growth story eventually needs physical inputs. Copper, steel, aggregates, fertilizer, chemicals, lumber, and energy materials have to be found, processed, transported, financed, and sold.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Freeport-McMoRan | Copper as a constraint for electrification and infrastructure. | Mine output -> realized price -> cash cost margin. |
| Nucor | Steel supply behind construction and manufacturing. | Steel shipment -> metal spread -> cash flow. |
| Steel Dynamics | Capex-to-output and steel-cycle economics. | New capacity -> shipments -> margin and cash. |
| Vulcan Materials | Local quarry scarcity and aggregates pricing. | Tons shipped -> local price -> unit margin. |
| CF Industries | Fertilizer and food-input economics. | Nitrogen product sale -> gas-cost advantage -> cash flow. |

The main warning: input scarcity does not always mean producer profits. New supply, demand cycles, commodity prices, and cost inflation can erase the thesis.

## Theme 11: Real Estate And Scarce Locations

Real estate matters when the location itself is hard to replace. The scarce thing may be tower height, warehouse proximity, data-center interconnection, senior-housing beds, or a tenant-specific store site.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| American Tower | Wireless equipment needs physical tower locations. | Carrier lease -> rent escalator -> AFFO. |
| Prologis | Logistics locations near consumers and supply chains. | Warehouse lease -> rent growth and development gains. |
| Equinix | Data-center interconnection and power-constrained campuses. | Colocation/interconnection fee -> recurring cash. |
| Welltower | Senior housing and healthcare real estate. | Resident/operator revenue -> rent or NOI -> AFFO. |
| Realty Income | Ordinary tenant locations converted into monthly rent. | Tenant sale capacity -> rent collection -> AFFO. |

The main warning: property ownership alone is not enough. The tenant must be able to pay, debt must be manageable, and location scarcity must survive new supply.

## Theme 12: Broad Technology Beyond Internet Software

Technology is not only consumer apps. It includes chips, networking, cloud, security, storage, devices, enterprise workflow, telecom, and services.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Microsoft | Cloud, enterprise software, security, AI infrastructure, and workflow. | Subscription/usage/license -> margin and free cash flow. |
| NVIDIA | AI demand becoming chips, systems, and networking. | Accelerator/system sale -> data-center revenue and margin. |
| Broadcom | Custom silicon plus infrastructure software. | Chip and software contracts -> margin and cash. |
| Cisco | Enterprise networking and security equipment. | Product sale plus subscriptions/support -> cash flow. |
| ServiceNow | Enterprise workflow control. | Subscription expansion -> RPO and free cash flow. |

The main warning: AI exposure is not proof of value. The proof is whether capex turns into paid usage, renewal, margin, and cash after competition and customer concentration.

## Theme 13: Healthcare Tools And Medical Infrastructure

Healthcare also depends on tools: devices, diagnostics, labs, hospitals, distribution, supplies, inventory, and procedures.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Abbott | Devices, diagnostics, nutrition, and medical products. | Product sale -> procedure/test/use volume -> cash. |
| Thermo Fisher | Life-science tools and bioproduction inputs. | Instrument/consumable/service sale -> lab and pharma demand. |
| HCA Healthcare | Hospitals as staffed care sites and reimbursement systems. | Patient service -> payer reimbursement -> cash collection. |
| McKesson | Drug distribution and working-capital timing. | Wholesale drug flow -> distribution margin and cash conversion. |
| Stryker | Implants, surgical equipment, and procedure-linked demand. | Device sale -> hospital/procedure volume -> margin. |

The main warning: more care volume can still be a weak business if reimbursement, labor, bad debt, inventory, or regulation absorbs the economics.

## Theme 14: Energy Affordability And Supply Route

Energy affordability is the route from geology and infrastructure into usable fuel cost. The chain includes production, processing, pipes, storage, refining, export, contracts, debt, and end demand.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| Exxon Mobil | Integrated production, refining, chemicals, and project returns. | Commodity/product sale -> margin -> free cash flow. |
| Energy Transfer | Midstream volumes, contracts, DCF, debt, and growth capex. | Hydrocarbon movement -> tariff/fee -> DCF. |
| ONEOK | NGL/gas infrastructure and counterparties. | Gathering/processing/transport -> fees and EBITDA. |
| Plains All American | Tariffed pipeline route and rate evidence. | Barrel movement -> tariff billing -> segment cash. |
| Cheniere | LNG trains, contracts, debt, and export cash. | Gas purchase/liquefaction -> LNG contract/cargo sale -> cash waterfall. |

The main warning: volume is not the same as durable return. The proof needs contract tenor, tariff billing, throughput, project debt service, and contribution by asset.

## Theme 15: Ordinary Finance

Ordinary finance is how pressure becomes visible in cards, deposits, loans, payments, insurance, brokerage, and risk transfer.

Read first:

| Company | What It Shows | Money Path |
|---|---|---|
| JPMorgan Chase | Deposits, lending, cards, payments, markets, and credit losses. | Deposits and capital -> loans/services -> interest and fees. |
| American Express | Card spending, affluent consumer health, merchant fees, and credit risk. | Card spend -> discount revenue, fees, interest, and repayment. |
| Capital One | Consumer credit, card lending, auto loans, and deposits. | Loan/card balance -> interest/interchange -> credit losses. |
| Progressive | Insurance pricing, claims inflation, and household risk transfer. | Premium -> claims/investment income -> underwriting margin. |
| Visa | Payment network acceptance and transaction routing. | Card transaction -> assessment/processing fee -> cash. |

JPMorgan source status: `/cluster/annual-report-jpmorgan-ordinary-finance-extraction-pass-1.md` upgrades JPMorgan to source-visible with boundary. It supports JPMorgan as the broad ordinary-finance anchor: deposits, assets, lending, cards, payments, markets, capital, consumer-condition language, regulatory-capital framing, and credit-pressure sensing sit in one institution. It does not prove borrower health, loan-level repayment, card credit quality, NIM durability, deposit stickiness, allowance adequacy, segment-level cash quality, or recurring market revenue.

American Express source status: `/cluster/annual-report-amex-ordinary-finance-extraction-pass-1.md` upgrades American Express to source-visible with boundary. It supports American Express as the premium card-spend, merchant-network, membership, fee-paying product, younger-cohort, rewards/data, and credit-tone anchor for ordinary finance. It does not prove repayment quality, net merchant economics, reward-cost durability, benefit-cost control, customer lifetime value, delinquency quality, write-off quality, loan yield, or through-cycle premium-consumer health.

Capital One source status: `/cluster/annual-report-capital-one-ordinary-finance-extraction-pass-1.md` upgrades Capital One to source-visible with boundary. It supports Capital One as the consumer-credit, card-loan, auto-loan, deposit, funding-cost, provision, charge-off, capital, Discover-integration, and payment-network expansion anchor for ordinary finance. It does not prove consumer health, borrower repayment quality, acquisition return, charge-off normalization, reserve adequacy, deposit stickiness, payment-network economics, or loss-adjusted profitability.

The main warning: financial scale is not proof of productive money movement. Credit quality, repayment, funding cost, loss ratio, and customer health decide whether the flow is healthy.

## Cross-Theme Takeaways

1. The same company can belong to more than one economic story, but each row should name the exact mechanism. For example, MasTec belongs to power scarcity when it builds grid projects and to industrial uptime when backlog and field execution are the proof.
2. The strongest broad insight is that modern growth is becoming more physical, more financed, and more permissioned. Demand alone does not matter unless it becomes deliverable capacity, approved spending, billed revenue, collected cash, and adequate return.
3. The capital-platform companies are not just "asset managers." They are routes through which pensions, insurers, retirement savers, institutions, and wealth clients reach private credit, infrastructure, real estate, and other assets.
4. Consumer themes split into different kinds of pressure. Value retail shows budget discipline. Services show time, convenience, and experience. Household brands show defended routine and identity.
5. The proof standard should stay strict. A theme can be useful for writing before it becomes full named-cash proof. A named-cash claim requires receipts, billing, debt waterfalls, legal-entity schedules, collateral files, and return models.

## Safe Use

Use this matrix to decide which companies to open first under each theme and what to look for in their annual reports.

Do not use this matrix as investment advice, a ranking of best stocks, or proof that every listed company has already passed full evidence checks.

## Next Work

The next best expansion is not more high-level themes. It is deeper evidence under selected rows:

1. BlackRock, Blackstone, Apollo/Athene, KKR/Global Atlantic, and Brookfield for capital-source routing.
2. FPL/NextEra, Duke, AEP, MasTec, and Sterling for power-to-bill-to-cash evidence.
3. Costco, Walmart, Target, Dollar General, and Burlington for household budget pressure.
4. UnitedHealth, Cigna, DaVita, Addus, and Option Care for healthcare access and reimbursement reality.
5. Exxon, Energy Transfer, ONEOK, Plains, and Cheniere for route-level energy cash proof.

## Decision Marker

`annual-report-company-to-theme-matrix-pass-1-ready`
