# Retail Marketplace Boundary Index

Date baseline: 2026-08-10

## Scope

This index turns the retail-versus-marketplace boundary memo into a sortable operating map.

Use it with:

- [retail-marketplace-boundary-index-2026-08-10.csv](/indexes/retail-marketplace-boundary-index-2026-08-10.csv)
- [Retail Versus Marketplace Boundary](/extracted/themes/retail-versus-marketplace-boundary-2026-08-10.md)
- [Retail Systems Index](/indexes/retail-systems-index-2026-08-10.md)
- [Marketplace Systems Index](/indexes/marketplace-systems-index-2026-08-10.md)

The goal is to make this boundary sortable by:

- boundary type
- customer return anchor
- control center of gravity
- whether the marketplace layer widens or defines the economics
- best comparison pair

## Boundary map

| Boundary type | Company | Packet | What the customer mainly returns for | What the company mainly controls | Marketplace or coordination role | Best comparison pair |
|---|---|---|---|---|---|---|
| Inventory-led retailer with marketplace extension | Walmart Inc. | [company-packet.md](/extracted/services/discount-variety-stores/walmart-inc/company-packet.md) | first-party household basket, value, convenience, and omnichannel utility | merchanting, store network, first-party basket, and mass utility relationship | widens retail through media, membership, and marketplace layers | compare against Amazon and Target |
| Inventory-led retailer with marketplace extension | Target Corp. | [company-packet.md](/extracted/services/discount-variety-stores/target-corp/company-packet.md) | household trips, curated mass retail, same-day utility, and app reinforcement | owned merchanting, store base, same-day utility, and retail relationship | widens retail through Roundel, Target Circle 360, and Target+ | compare against Walmart and Amazon |
| Inventory-led retailer with marketplace extension | Ulta Beauty, Inc. | [company-packet.md](/extracted/services/specialty-retail-other/ulta-beauty-inc/company-packet.md) | beauty replenishment, discovery, services, and loyalty | category environment, loyalty, services, and discovery interface | marketplace assortment and media widen a retailer-controlled category environment | compare against Warby Parker and Amazon |
| Inventory-led retailer with marketplace extension | Best Buy Co., Inc. | [company-packet.md](/extracted/services/electronics-stores/best-buy-co-inc/company-packet.md) | electronics replacement, support, and service interaction | owned category environment, services, and support relationship | marketplace and ads widen a service-stabilized retailer | compare against Target and eBay |
| Utility retailer with major ecosystem widening | Amazon.com, Inc. | [company-packet.md](/extracted/retail/specialty-retail-other/amazoncom-inc/company-packet.md) | utility, search, replenishment, Prime, and account-level convenience | interface demand, fulfillment, seller services, ad inventory, and ecosystem utility | central to the economics rather than merely additive | compare against Walmart and eBay |
| Marketplace retail without owned inventory | eBay Inc. | [company-packet.md](/extracted/consumer-goods/internet-service-providers/ebay/company-packet.md) | search, discovery, resale trust, and category culture | seller supply, traffic, trust features, and listing economics | defines the economics | compare against Etsy and Amazon |
| Marketplace retail without owned inventory | Etsy, Inc. | [company-packet.md](/extracted/technology/internet-service-providers/etsy-inc/company-packet.md) | uniqueness, gifting, self-expression, and creator-led discovery | seller identity, creative supply, discovery, and trust | defines the economics | compare against eBay and Ulta |
| Retailer-enablement coordination layer | Maplebear Inc. dba Instacart | [company-packet.md](/extracted/technology/internet-service-providers/maplebear-inc/company-packet.md) | grocery convenience, basket assembly, and digital grocery habit | retailer enablement, grocery-demand routing, retail media, and store software | defines the economics and sits around retailers rather than replacing them | compare against Kroger and Amazon |
| Local-demand coordination layer | DoorDash, Inc. | [company-packet.md](/extracted/technology/internet-service-providers/doordash/company-packet.md) | convenience, local ordering, fill-in purchasing, and membership habit | merchant density, routing, logistics, memberships, and merchant tooling | defines the economics | compare against Uber and Instacart |
| Local-demand coordination layer | Uber Technologies, Inc. | [company-packet.md](/extracted/technology/application-software/uber-technologies-inc/company-packet.md) | movement, delivery, wallet behavior, and account-level local-demand utility | routing, wallet-like account behavior, supply coordination, and memberships | defines the economics | compare against DoorDash and Amazon |

## Highest-confidence uses

- separate retail-first systems from marketplace-first and coordination-first systems
- identify where marketplace layers are quality markers versus where they are the actual economic engine
- keep `Amazon`, `Walmart`, `Target`, `Ulta`, `Best Buy`, `eBay`, `Etsy`, `Instacart`, `DoorDash`, and `Uber` on one comparable screen
- tighten retail-versus-marketplace assignment without reopening the full retail and marketplace memos

## Current best next moves

1. Reuse this index when deciding whether a new company belongs mainly in the retail lane, the marketplace lane, or both.
2. Add a derived column later for relationship thickness if the mixed cases become more crowded.
3. Use the current set to tighten `Amazon` versus `Walmart` versus `Target` comparison quality before adding another hybrid boundary case.
