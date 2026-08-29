# Capital Flow AEP/Duke Regulatory Docket Extraction Pass

## Purpose

This page is the first regulatory docket extraction pass for the AEP/Duke power-grid evidence chain.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-aep-duke-regulatory-docket-extraction-pass.csv`

The prior docket queue asked:

`Which parts of the AEP/Duke load, capex, turbine, project, and affordability claims have legal/regulatory permission to become recoverable infrastructure?`

This pass starts answering that with regulator and official-company source evidence.

## Extraction Summary

| Company | Rows | Main Coverage |
|---|---:|---|
| AEP | 4 | AEP Ohio data-center tariff mechanics and I&M expedited generation-resource path |
| Duke | 5 | Anderson County CC docket/approval, Carolinas Resource Plan, DEC/DEP combination queue, and blocked Duke regulatory page note |

Total rows: `9`

## Theme And Subtheme Read

This pass sits under the broader capital-flow theme:

`AI/data-center and electrification demand is turning into utility capital formation when it passes through tariffs, interconnection queues, resource plans, generation approvals, and cost-recovery mechanisms.`

The important point is directional but also testable. We are not treating management commentary as enough. We are asking whether disclosed demand has moved into legal, operational, and financing channels that can cause money to be spent.

### Theme 1: Customer-Backed Large-Load Demand

Subtheme:

`Large-load growth becomes more believable when customers must post fees, sign agreements, accept minimum demand obligations, or reimburse buildout costs.`

Rows:

- `ADRE-001` to `ADRE-003`

AEP Ohio is the clearest example in this pass. The data-center tariff evidence gives us a better filter for separating speculative load inquiries from load that can enter utility planning. The tariff process creates a sequence:

`application -> study fee -> plan of service -> LOA/ESA -> collateral/minimum demand obligations -> PJM forecast -> energization`

That matters because the capital-flow question is not simply `how many GW did management mention?` The better question is:

`How much of the mentioned GW has crossed into a binding customer-obligation process?`

### Theme 2: Regulated Capital Formation

Subtheme:

`Utility capital plans are investable capital-flow evidence only when we can connect them to jurisdictional approval, cost recovery, or prudency review.`

Rows:

- `ADRE-001` to `ADRE-005`
- `ADRE-007` to `ADRE-009`

The regulatory layer is where projected demand can become recoverable infrastructure. AEP Ohio's tariff, I&M's expedited generation-resource path, and Duke's Anderson County approval each move one step beyond earnings-slide rhetoric.

The next denominator is jurisdictional:

`approved capital / pending capital / proposed capital / unsupported management estimate`

This is why the same company-level number can have very different evidence quality by state, operating company, and asset type.

### Theme 3: Generation Procurement As A Capital Sink

Subtheme:

`New load does not become utility investment only through wires. It also creates generation procurement, turbine reservations, acquisitions, and new-build power projects.`

Rows:

- `ADRE-004`
- `ADRE-005`
- `ADRE-006`
- `ADRE-008`

I&M's `318 MW` Big Sandy request is an acquisition-style path. Duke's Anderson County project is a new-build combined-cycle path. Duke's resource-plan filing points to a broader portfolio path across combined-cycle, combustion-turbine, solar, and storage resources.

The analytical split should stay explicit:

| Procurement Type | What It Funds | Evidence Needed |
|---|---|---|
| Acquisition | Existing plant purchase | purchase agreement, regulator approval, closing, rate treatment |
| New-build gas | turbines, EPC, interconnection, plant construction | CPCN/order, project cost, construction timeline, recovery mechanism |
| Renewable/storage buildout | solar, batteries, grid integration | resource-plan approval, RFP/award, interconnection, capex |
| Capacity contract | purchased capacity or PPA | contract term, counterparty, regulator treatment |

### Theme 4: Affordability And Political Constraint

Subtheme:

`The capital-flow path is strongest when companies show not only required spend, but also rate-mitigation tools that make approval politically durable.`

Rows:

- `ADRE-003`
- `ADRE-007`

AEP's tariff mechanics shift some buildout and cancellation risk onto large-load customers. Duke's DEC/DEP combination filing includes an asserted customer-savings rationale. These are not side details. They are part of how capital plans survive regulatory review.

The next analysis should tag every row with:

`who pays first`, `who bears cancellation risk`, `who earns return`, and `what ratepayer protection exists`.

### Theme 5: Jurisdictional Fragmentation

Subtheme:

`Company-level capital-flow claims are only as strong as the weakest state-by-state approval map behind them.`

Rows:

- all rows in this pass

AEP and Duke are multi-jurisdiction systems. A company-level total can combine Ohio tariffs, Indiana acquisition requests, South Carolina generation approvals, North Carolina planning processes, and blocked or still-missing docket records.

This means the correct next unit of analysis is not only company:

`company -> operating company -> jurisdiction -> docket -> asset/load bucket -> status -> dollars/MW -> recovery mechanism`

## Visible Extraction Row Anchors

| Row Range | Company | Focus |
|---|---|---|
| ADRE-001 to ADRE-004 | AEP | AEP Ohio data-center tariff and I&M expedited generation-resource path |
| ADRE-005 to ADRE-009 | Duke | Anderson County CC, Carolinas Resource Plan, DEC/DEP combination, and blocked Duke regulatory page note |

## What Improved

### AEP Ohio Data-Center Tariff

AEP Ohio now has a stronger regulatory-status ladder:

`PUCO adopted settlement -> compliance tariff filed -> tariff effective -> applications/studies -> LOA/ESA -> PJM forecast -> energization`

Important extracted mechanics:

- PUCO adopted AEP Ohio's `2024` Data Center Tariff settlement on July 9, `2025`.
- AEP Ohio filed its compliance tariff on July 11, `2025`.
- The tariff became effective on July 23, `2025`.
- New data-center service requests must use the PowerClerk process.
- Data centers or expansions of `25,000 kW` or greater must pay load-study fees.
- Study fees range from `$10,000` to `$100,000`.
- Customers receive LOA and ESA contracts after load study and plan-of-service work.
- Customers have `60` days to sign LOA and ESA contracts or forfeit their spot.
- LOA cancellation/delay protection requires reimbursement of `100%` of buildout costs if the customer cancels or delays by more than `12` months before target energization.
- Minimum demand, collateral, assignment, behind-the-meter generation, and exit-fee mechanics are defined.

This strengthens the AEP Ohio claim materially. It shows that the regulatory system is trying to make large-load customers carry specific obligations rather than simply putting speculative demand into ordinary utility planning.

### I&M Expedited Generation Resource Path

I&M now has a clearer regulatory path but not final project proof.

Extracted facts:

- I&M says its Expedited Generation Resource Plan was approved by the IURC in January `2026`.
- I&M requested approval to acquire the `318 MW` Big Sandy Peaker Plant.
- The Big Sandy filing is under the approved EGR Plan.
- I&M anticipated an IURC decision in September `2026`.
- I&M says customer benefit would occur by end-`2026` under that timeline.
- I&M says Indiana peak demand is expected to rise from about `2,800 MW` in `2024` to more than `7,000 MW` around `2030`.

This strengthens the AEP/I&M pathway from demand to generation procurement, but the Big Sandy project itself remains pending in this pass.

### Duke Anderson County CC

Duke's Anderson County row is the strongest project-level regulatory extraction so far.

The South Carolina PSC docket page shows:

- docket `2025-250-E`
- opened August 20, `2025`
- status shown as open
- summary: joint application for a Certificate of Environmental Compatibility and Public Convenience and Necessity for a new combined-cycle generating plant in Anderson County
- March 26, `2026` directive for final disposition
- proposed orders granting certificate/application filed March 18, `2026`
- ongoing monitoring reports after approval

Duke's official release adds:

- PSCSC approved the Anderson County project.
- approximate nominal capacity is `1,365 MW`.
- Central Electric Power Cooperative owns `95 MW`.
- North Carolina Electric Membership Corporation owns `100 MW`.
- construction is anticipated to begin in summer `2027`.
- the facility would serve customers by early `2031`.

This strengthens Duke's `7,501 MW` project-table row because at least one named project now has docket and approval trail evidence.

## What Remains Weak

### AEP

Still not fully extracted:

- PUCO Opinion and Order text
- DCT docket number and approved stipulation details
- IURC EGR Plan final order/cause number
- I&M Big Sandy final decision
- PSO, SWEPCO, Appalachian Power, West Virginia, Virginia, Louisiana, Texas, and DOE docket/financing documents

### Duke

Still not fully extracted:

- Anderson County final order attachment and exact conditions
- NCUC Person County and other North Carolina gas project approvals
- Cayuga Indiana CWIP/order proof
- Duke Carolinas Resource Plan docket/order
- DEC/DEP combination final approval documents
- Duke regulatory information page was blocked by `403`, so NCUC/PSC/FERC direct sources are needed

## Claim Upgrade

Before this pass, the docket layer was only a queue.

After this pass, we can say:

`Some AEP and Duke capital-flow claims now have regulatory-source entry points and partial extraction: AEP Ohio has an effective data-center tariff process with customer obligation mechanics, I&M has an approved expedited generation-resource pathway with a pending 318 MW acquisition request, and Duke Anderson County CC has docket/approval evidence for an approximately 1,365 MW combined-cycle plant.`

We still cannot say:

`All AEP and Duke disclosed load and capital-plan rows are approved, recoverable, and in service.`

## Next Extraction Order

1. Pull PUCO DCT Opinion and Order, approved stipulation, and Schedule DCT.
2. Pull IURC EGR Plan order and Big Sandy acquisition cause/order.
3. Pull PSCSC Anderson County final order and monitoring reports.
4. Pull NCUC Carolinas Resource Plan docket and DEC/DEP combination order.
5. Build Duke row-per-project gas generation docket crosswalk.
6. Build AEP row-per-jurisdiction regulatory-progress extraction for PSO, SWEPCO, Appalachian Power, AEP Texas, and DOE loan/grant treatment.

## Bottom Line

The regulatory layer is starting to do real work.

The important simple read:

`AEP and Duke are not just talking about power demand. In several places, the demand is already becoming tariffs, resource-plan proceedings, generation approvals, customer obligations, and monitoring requirements. But every jurisdiction still has to be checked separately before the capital-flow claim can be treated as fully approved and recoverable.`
