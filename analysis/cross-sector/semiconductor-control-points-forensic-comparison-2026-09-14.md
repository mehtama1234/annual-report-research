# Semiconductor control points: architecture, fabrication, inspection, and validation

## Purpose

The semiconductor companies in the archive should not be grouped together
under “AI beneficiaries.” They control different steps, sell to different
decision makers, carry different capital burdens, and expose owners to
different forms of cycle and accounting risk.

The useful chain is:

`compute architecture -> lithography -> materials engineering -> inspection and yield -> deposition/etch -> post-fabrication test -> deployable system`

This comparison uses the completed company dossiers for NVIDIA, ASML, KLA,
Applied Materials, Lam Research, and Teradyne. It is a synthesis, not a
replacement for the company-level evidence.

## Control-point map

| Layer | Company | What the customer is buying | What makes the relationship valuable | Main burden |
| --- | --- | --- | --- | --- |
| Architecture and software ecosystem | NVIDIA | Accelerators, systems, networking, CUDA, and a supported platform | Application compatibility, performance, developer adoption, and ecosystem dependence | Product transitions, supply commitments, export rules, hyperscaler concentration, and very high expectations |
| Lithography | ASML | EUV/DUV systems, upgrades, software, and service | A highly qualified integrated system required for advanced patterning | Extreme customer concentration, supplier dependence, €4.7B R&D, export policy, system timing, and fab cycles |
| Inspection and yield control | KLA | Inspection, metrology, process control, and service | The cost of undetected defects and lost yield makes qualified tools difficult to replace | WFE cycles, customer concentration, China/export controls, service infrastructure, and R&D |
| Materials engineering | Applied Materials | Deposition, etch, thermal processing, packaging, and related tools | Multiple qualified process steps and a large installed-base service layer | Fab capex, China, customer concentration, contract liabilities, inventory, R&D, and facility capex |
| Deposition and etch | Lam Research | Deposition, etch, clean, packaging, spares, upgrades, and support | Process complexity and installed chambers create technical and service dependence | WFE cycles, 34% China revenue, four large customers, acceptance timing, inventory, R&D, and facilities |
| Post-fabrication validation | Teradyne | Semiconductor, memory, system, defense, and industrial test | Customers cannot deploy high-value devices without performance and reliability validation | Semiconductor and memory cycles, receivables, customer advances, acquisitions, Robotics, SBC, and valuation |

The control points are related but not interchangeable. Lithography scarcity
does not prove that every deposition tool has the same pricing power. A large
installed base does not prove that support revenue is independent of tool
utilization. A strong test quarter does not prove that test intensity will
offset a memory or compute-capex downturn.

## Who controls the valuable relationship?

### The customer relationship is strongest where qualification and failure cost meet

ASML, KLA, Applied Materials, and Lam are embedded in fab process decisions.
The customer must qualify equipment, recipes, service response, and yield
outcomes. Replacing a tool can require requalification and can create
production risk.

Teradyne is embedded in test programs and deployment readiness. Its switching
cost is meaningful when test coverage, data, reliability, and production
throughput are tied to a customer platform, but the equipment budget can still
be deferred when product launches or capacity plans are delayed.

NVIDIA's relationship is broader. It reaches developers, cloud operators,
system builders, and end customers through architecture and software. That can
create stronger ecosystem effects, but it also concentrates expectations in a
single platform and requires continuing product leadership.

### The cleanest economics are not necessarily at the most essential step

The cleanest economics tend to occur where:

1. customer failure is expensive;
2. the tool is qualified into a production process;
3. switching is difficult;
4. service or upgrades monetize the installed base; and
5. required reinvestment grows more slowly than customer value.

ASML has the strongest scarcity claim, but also the largest customer and
geopolitical concentration. KLA has a narrow process-control position and
strong service economics, but remains tied to fab budgets. Applied and Lam
cover more process steps and therefore have broad exposure, but they carry
more product, inventory, facility, and China complexity. Teradyne benefits from
validation necessity but has a less pure segment mix and lower current cash
scale. NVIDIA captures more value when platform demand is strong, but its
valuation and customer/supply concentration are more demanding.

## Cash conversion and earnings quality comparison

| Company | Latest annual cash screen | Main cash-quality test | Main financial-engineering test |
| --- | --- | --- | --- |
| ASML | 2025 cash after capex and intangibles about €11.027B | 2024 and 2025 cash benefited from customer advances, supplier timing, and strong system demand; test backlog conversion and acceptance | Backlog is not revenue; customer advances, system timing, export licenses, and service mix must be traced |
| KLA | FY2026 OCF less capex about $3.767B | Test receivables, inventory, deferred revenue, service utilization, warranty, and R&D | Test whether margin and service growth are structural or peak-cycle mix and absorption |
| Applied Materials | FY2025 OCF less capex about $5.698B | Test contract-liability conversion, inventory, facility capex, and point-in-time system revenue | Test whether advance billings, acceptance, customer concentration, and SBC overstate owner cash |
| Lam Research | FY2026 OCF less capital/investing cash use about $4.935B | OCF declined from 2025 while profit and revenue rose; test deferred profit, receivables, and acceptance | Test Japan-held inventory, deferred revenue, customer advances, China, and buyback dilution |
| Teradyne | FY2025 FCF about $450M | Test the $306M receivable use, $53M customer-advance source, and segment cash conversion | Test acquisitions, affiliate earnings, Robotics mix, SBC, and debt-funded capital returns |
| NVIDIA | Company-specific cash screen in its dossier | Test supply commitments, receivables, inventory, customer concentration, and product transition | Test whether platform growth and buybacks remain owner cash after supply and R&D commitments |

NVIDIA’s Q2 fiscal 2027 filing makes the last row more demanding. Six-month
operating cash was `$74.421B`, but receivables rose to `$63.059B`, inventory to
`$31.575B`, and the company used `$39.044B` for share repurchases. It also
reported `$36B` of six-year AI-cloud service commitments and up to `$3.5B` of
land, power, and shell guarantees. The platform is producing exceptional cash,
but it is also taking on more of the infrastructure coordination previously
carried by customers and cloud operators. NVIDIA therefore remains the
strongest architecture-and-software control point in this set while having a
larger non-capex commitment perimeter than the annual cash screen suggests.

The common error is to treat positive operating cash flow as unrestricted
owner cash. Each company must fund some combination of process R&D, customer
qualification, service infrastructure, inventory, manufacturing capacity,
software, supplier commitments, acquisitions, or product transitions.

## Macro and liquidity lens

The semiconductor chain is a liquidity-sensitive system even when the
technology trend is durable.

- Higher rates and weaker customer balance sheets can delay fabs, memory
  expansions, product launches, and test capacity.
- AI demand can increase process intensity while total semiconductor spending
  still cycles through inventory corrections.
- Export controls can alter the addressable market, product mix, service
  rights, customer location, and supplier economics.
- Advanced packaging, HBM, gate-all-around logic, and three-dimensional memory
  can raise tool content, but the customer must still pay for the transition.
- The suppliers with the strongest control points may still experience large
  order and cash fluctuations because a small number of customers determine
  industry capacity.

The correct macro question is not “Will AI continue?” It is:

`What portion of AI-related semiconductor spending survives a liquidity, inventory, customer-capex, and export-policy normalization, and which supplier keeps the resulting owner cash?`

## Valuation expectations

The valuation register shows a common pattern: the market values the control
points well above recent normalized cash screens.

| Company | Base normalized cash case | Base implied equity value | Market snapshot | Interpretation |
| --- | ---: | ---: | ---: | --- |
| ASML | €11.0B at 38x | about $418B | about $632.6B | Requires long-duration EUV growth, high margins, and successful service and export-policy management |
| KLA | $3.8B at 45x | $171B | about $238.4B | Requires strong process-control cash through a down-cycle |
| Applied Materials | $5.8B at 30x | $174B | about $343.2B | Requires cash well above the fiscal 2025 screen or a longer growth runway |
| Lam Research | $5.0B at 60x | $300B | about $350.5B | Requires process-intensity growth and support durability despite China and customer risk |
| Teradyne | $500M at 40x | $20B | about $53.8B | Requires a large increase from 2025 cash and a high multiple despite test cyclicality |

These are scenario screens, not price targets. The comparison shows where the
market is asking the most from the evidence. Scarcity can justify a premium;
it does not justify ignoring the reinvestment and cycle denominator.

## Who carries the burden?

| Burden | Most exposed companies | What to measure |
| --- | --- | --- |
| Fab-capex and WFE cycle | KLA, Applied, Lam, ASML | Orders, systems revenue, customer capex, backlog conversion, and service utilization |
| Extreme customer concentration | ASML, KLA, Lam, NVIDIA | Largest-customer share, pricing, receivables, order timing, and customer project concentration |
| China and export policy | Applied, Lam, ASML, KLA, NVIDIA | Revenue by geography, licenses, product restrictions, service rights, cancellations, and domestic competition |
| R&D and technology leadership | ASML, KLA, Applied, Lam, NVIDIA | R&D intensity, product roadmap, qualification wins, productivity, and return on incremental R&D |
| Working-capital and acceptance timing | Applied, Lam, Teradyne, ASML | Receivables, inventory, contract/deferred revenue, advances, acceptance, and supplier terms |
| Segment and acquisition complexity | Teradyne, Applied, NVIDIA | Organic growth, segment margins, acquisition cash, amortization, affiliate income, and integration cost |
| AI-cloud financing and utilization commitments | NVIDIA | Six-year service commitments, partner liquidity, utilization, revenue-share terms, land/power guarantees, and impairment or inventory exposure |
| Per-share capital allocation | All six | SBC, diluted shares, buybacks, dividends, debt, and repurchase price |

## Filing tests that can change the conclusion

The next filings should be read as a connected experiment:

1. If customer capex slows, do service and support revenues hold, or do they
   fall with utilization and tool retirements?
2. Do backlog and customer advances convert into collected cash and gross profit
   without rising inventory, receivables, or acceptance delays?
3. Does process complexity increase tool content enough to offset lower unit
   volumes or memory corrections?
4. Does China revenue decline gradually and get replaced by allied-region
   demand, or does policy create a permanent product and service loss?
5. Do R&D and facilities produce measurable productivity, qualification, share,
   or installed-base gains?
6. Do buybacks reduce diluted shares after SBC, or mainly return cash while
   preserving a similar per-share claim?
7. Do Teradyne's Product Test and Robotics segments diversify cash, or does
   Semiconductor Test remain the sole source of the valuation narrative?
8. Does NVIDIA's platform remain the demand sponsor for the rest of the chain,
   or does spending broaden while supplier economics compress?
9. Do the AI-cloud commitments create incremental, cash-paying demand, or do
   they shift utilization and financing risk onto NVIDIA?

## Current synthesis

The completed evidence supports a differentiated conclusion:

- The semiconductor chain contains several real control points, not one AI
  trade.
- ASML has the strongest scarcity but also the highest concentration and
  valuation expectations.
- KLA appears to have one of the cleaner process-control economics, but still
  depends on fab spending and export policy.
- Applied Materials and Lam have broader process exposure and meaningful
  service layers, but carry more inventory, facility, acceptance, and China
  burden.
- Teradyne shows that validation is valuable, but the company-level cash stream
  is less pure because of Robotics, Product Test, acquisitions, and a lower
  normalized cash base.
- NVIDIA captures the architecture and ecosystem layer, but its owner economics
  must now be tested against supply commitments, customer concentration,
  product transitions, AI-cloud utilization, guarantees, and valuation.

The strongest thesis is therefore not “buy semiconductor beneficiaries.” It is:

`identify the qualified control point, subtract the capital and liquidity burden, then test whether the market price requires a cash stream that the filings have not yet demonstrated.`

## Company dossiers

- [NVIDIA](../deep-company-pages/nvidia-corporation.md)
- [ASML](../deep-company-pages/asml-holding-nv.md)
- [KLA](../deep-company-pages/kla-corporation.md)
- [Applied Materials](../deep-company-pages/applied-materials-inc.md)
- [Lam Research](../deep-company-pages/lam-research-corporation.md)
- [Teradyne](../deep-company-pages/teradyne-inc.md)
- [Software, process control, and physical compute first-principles essay](../first-principles/software-process-control-and-physical-compute.md)
