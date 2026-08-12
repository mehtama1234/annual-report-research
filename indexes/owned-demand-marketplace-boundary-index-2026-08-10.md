# Owned-Demand Marketplace Boundary Index

Date baseline: 2026-08-10

## Scope

This index turns the owned-demand versus marketplace-extended boundary memo into a sortable operating map.

Use it with:

- [owned-demand-marketplace-boundary-index-2026-08-10.csv](/indexes/owned-demand-marketplace-boundary-index-2026-08-10.csv)
- [Owned-Demand Versus Marketplace-Extended Boundary](/extracted/themes/owned-demand-versus-marketplace-extended-boundary-2026-08-10.md)
- [Owned-Demand Channel-Control Index](/indexes/owned-demand-channel-control-index-2026-08-10.md)
- [DTC Versus Channel-Control Crosswalk](/extracted/themes/dtc-vs-channel-control-crosswalk-2026-08-10.md)
- [Warby Parker Versus Nike Versus Ulta Boundary Comparison](/extracted/themes/warby-parker-vs-nike-vs-ulta-boundary-comparison-2026-08-10.md)

The goal is to make this boundary sortable by:

- boundary type
- demand anchor
- what the customer mainly returns for
- what the company mainly controls
- whether marketplace reach assists or replaces owned demand
- best comparison pair

## Boundary map

| Boundary type | Company | Packet | What the customer mainly returns for | What the company mainly controls | Marketplace role | Best comparison pair |
|---|---|---|---|---|---|---|
| True owned-demand system | Levi Strauss & Co. | [company-packet.md](/extracted/consumer-goods/apparel-stores/levi-strauss-co/company-packet.md) | heritage fit and wardrobe authority | brand presentation, pricing, merchandising, and first-party demand | minor or indirect | compare against Gap and against Ulta to separate brand-owned demand from assortment-led interface control |
| True owned-demand system | Crocs, Inc. | [company-packet.md](/extracted/consumer-goods/textile-apparel-footwear-accessories/crocs-inc/company-packet.md) | comfort, ease, and recognizable mass identity | direct brand relationship, merchandising, and customer-file deepening | limited relative to brand core | compare against Deckers and against Amazon to separate owned comfort demand from interface control |
| True owned-demand system | Warby Parker Inc. | [company-packet.md](/extracted/healthcare/medical-instruments-supplies/warby-parker-inc/company-packet.md) | fit, exams, contacts, and direct vision-care relationship | service-linked brand control, customer file, and category extension | minimal relative to direct service relationship | compare against Ulta on service-linked demand that is still brand-owned rather than assortment-owned |
| Hybrid owned-demand with marketplace-assisted reach | YETI Holdings, Inc. | [company-packet.md](/extracted/consumer-goods/sporting-goods/yeti-holdings-inc/company-packet.md) | premium utility, gifting, and direct brand trust | premium hardgoods demand, direct reach, and category authority | assists owned demand through marketplace reach | compare against Ulta and Amazon to separate assisted owned demand from interface-first control |
| Hybrid owned-demand with marketplace-assisted reach | NIKE, Inc. | [company-packet.md](/extracted/retail/apparel-shoe-accessory-stores/nike-inc/company-packet.md) | athletic identity and performance authority | global brand storytelling, direct surfaces, and customer-file depth | channel widener rather than relationship core | compare against Levi and Amazon to separate brand control from interface scale |
| Hybrid owned-demand with marketplace-assisted reach | Deckers Outdoor Corp. | [company-packet.md](/extracted/consumer-goods/textile-apparel-footwear-accessories/deckers-outdoor-corp/company-packet.md) | performance plus comfort attachment | brand mix, product authority, and channel balance | assists product authority rather than replacing it | compare against Crocs and Birkenstock on different owned-demand widening paths |
| Hybrid owned-demand with marketplace-assisted reach | Birkenstock Holding plc | [company-packet.md](/extracted/services/apparel-stores/birkenstock-holding-plc/company-packet.md) | comfort, body alignment, and premium utility | product authority and category control | partner sell-through assists owned demand | compare against Deckers and YETI on utility-led hybrid control |
| Hybrid owned-demand with marketplace-assisted reach | Victoria's Secret & Co. | [company-packet.md](/extracted/consumer-goods/apparel-stores/victorias-secret-co/company-packet.md) | fit, beauty adjacency, and self-presentation | category authority, emotional marketing, and direct surfaces | partner network widens direct demand | compare against Tapestry and Ulta on identity-led demand versus assortment-led interface control |
| Hybrid owned-demand with marketplace-assisted reach | Tapestry, Inc. | [company-packet.md](/extracted/consumer-goods/textile-apparel-clothing/tapestry-inc/company-packet.md) | visible status, handbags, and emotional brand connection | direct brand heat, data, and house-of-brands control | partner distribution widens house-of-brands demand | compare against Victoria's Secret and Amazon on brand heat versus interface utility |
| Marketplace-extended or interface-control system | Ulta Beauty, Inc. | [company-packet.md](/extracted/services/specialty-retail-other/ulta-beauty-inc/company-packet.md) | assortment authority, discovery, replenishment, services, and loyalty | traffic, discovery, services, media, and category interface control | central to the economic model | compare against Warby Parker and YETI to separate service-linked brand demand from assortment-led interface demand |
| Marketplace-extended or interface-control system | Amazon.com, Inc. | [company-packet.md](/extracted/retail/specialty-retail-other/amazoncom-inc/company-packet.md) | search, utility, Prime, fulfillment, and broad account convenience | interface demand, seller services, ads, and ecosystem utility | central to the economic model | compare against Walmart and YETI to separate interface ownership from merchanting or brand-owned demand |
| Marketplace-extended or interface-control system | eBay Inc. | [company-packet.md](/extracted/consumer-goods/internet-service-providers/ebay/company-packet.md) | search, discovery, resale trust, and seller-supply depth | traffic, discovery, trust features, and seller economics | central to the economic model | compare against Etsy and Levi to separate seller-network demand from classic brand-owned demand |

## Highest-confidence uses

- separate true owned-demand systems from assortment-led and interface-led systems
- identify where marketplace reach assists owned demand versus where it becomes the main economic engine
- separate service-linked owned demand, hybrid brand control, and assortment-led interface control on one page
- compare service-linked direct demand against broader discovery and interface control
- tighten the `YETI` versus `Ulta` versus `Amazon` classification problem without reopening the whole DTC crosswalk

## Current best next moves

1. Reuse the direct `Warby Parker` versus `Nike` versus `Ulta` comparison first when the question is whether a company belongs closer to owned service demand, hybrid brand control, or interface-led category control.
2. Reuse this index when deciding whether a new company belongs primarily in the owned-demand lane or the marketplace-extended lane.
3. Add derived columns later for relationship thickness and partner dependence if the mixed cases become more crowded.
4. Use the current set to tighten the `Amazon` versus `Ulta` versus `YETI` comparison before adding another new boundary case.
