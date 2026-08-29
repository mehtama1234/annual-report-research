# Capital Flow Asset-Backed Finance Ledger Pass 1

## Purpose

This is the first asset-backed finance and securitization extraction pass for the all-company capital-flow program.

The operating table is:

`analysis/company-first-principles/data/capital-flow-asset-backed-finance-ledger-pass-1.csv`

This pass applies a strict rule:

`Receivables and inventory are not asset-backed finance unless a source shows they are pledged, sold, warehoused, securitized, financed, or used inside a credit-risk structure.`

## Current Result

| Metric | Value |
|---|---:|
| Asset-backed finance rows | `14` |
| Companies covered | `10` |
| Filed first-pass rows | `4` |
| Queued collateral-search rows | `10` |
| Next dashboard status target | `collateral-document-grade` |

## Visible Row Anchors

| Row Range | Focus |
|---|---|
| ABF-001 to ABF-002 | Synchrony consumer receivables, funding base, and credit performance |
| ABF-003 to ABF-004 | Pool receivables facility and seasonal working-capital financing |
| ABF-005 to ABF-006 | Arrow receivables/inventory and supplier inventory protections |
| ABF-007 to ABF-008 | Global Industrial receivables, inventory, and tariff/inventory accounting |
| ABF-009 to ABF-014 | MSC, Target, Dollar General, Zebra, Honeywell, and Henry Schein collateral-search rows |

## What This Lane Is Really Testing

The asset-backed lane is not just:

`Companies have receivables and inventory.`

The useful question is:

`When do operating assets become financeable collateral pools?`

That requires evidence such as:

- receivables facility
- securitization trust
- warehouse line
- collateral pledge
- inventory borrowing base
- receivable sale
- retained interest
- credit-loss reserve
- advance rate
- SPV debt
- ABS notes

## Theme And Subtheme Read

### 1. Merchant-Linked Consumer Credit

Rows:

- `ABF-001`
- `ABF-002`

Synchrony is the strongest row in this pass.

The packet gives:

- `102.2B USD` of Q2 `2026` loan receivables
- `49.8B USD` of Q2 `2026` purchase volume
- `81.1B USD` of year-end `2025` Synchrony Bank deposits
- deposits representing `84%` of total funding at year-end `2025`
- full-year net charge-off rate returning to the `5.5%` to `6.0%` long-term target range

The simple claim:

`Synchrony turns merchant-linked consumer purchases into a large receivable and credit-spread system.`

The boundary:

`This is not yet securitization proof.`

We still need ABS trust filings, retained interests, securitized asset balances, charge-off/delinquency tables, and funding footnotes.

### 2. Receivables Facility And Seasonal Working Capital

Rows:

- `ABF-003`
- `ABF-004`

Pool is the strongest nonfinancial row.

The packet gives:

- `300.0M USD` outstanding under the receivables facility at Q1 `2026`
- `315.5M USD` outstanding under the receivables facility at Q2 `2026`
- explicit statement that the receivables facility remained central to seasonal working-capital support

The simple claim:

`Pool shows how seasonal distributor receivables become a working-capital financing instrument.`

The boundary:

`We still need the receivables facility document and footnote details: facility size, eligible receivables, lender/purchaser, advance rate, maturity, pricing, recourse, and collateral terms.`

### 3. Distributor Working-Capital Intensity

Rows:

- `ABF-005`
- `ABF-006`
- `ABF-007`
- `ABF-008`
- `ABF-009`
- `ABF-014`

These rows are useful but weaker.

They show that middle-layer distributors carry large receivables and inventory loads:

- Arrow had about `28.0B USD` of receivables and about `5.94B USD` of inventories at Q2 `2026`.
- Arrow also disclosed supplier protections covering about `56%` of consolidated inventories for price reductions and about `59%` for repurchase arrangements at year-end `2025`.
- Global Industrial had `186.8M USD` of accounts receivable and `163.6M USD` of inventories at Q2 `2026`.
- MSC depends on inventory, receivables, vending, In-Plant locations, and procurement workflow.
- Henry Schein supplies over `1M` customers and ships about `150,000` cartons daily.

The simple claim:

`Distribution companies can be collateral-rich, working-capital-heavy middle layers.`

The boundary:

`Working-capital intensity is not asset-backed finance until a source shows collateralized funding or receivable sale.`

### 4. Retail Inventory And Payables Search

Rows:

- `ABF-010`
- `ABF-011`

Target and Dollar General remain collateral-search candidates, not proof rows.

Target gives:

- Q1 `2026` capex up `31%` to `1.0B USD`
- non-merchandise sales up `24.6%`
- growing marketplace, delivery, and advertising layers

Dollar General gives:

- fiscal `2025` operating cash flow up `21.3%` to `3.6B USD`
- inventory per store down `7.0%`
- `20,893` stores
- consumables at `81.0%` of fiscal `2025` sales

The simple claim:

`Retailers carry large operating assets and payables systems, but the packet layer does not yet prove asset-backed financing.`

The boundary:

`Do not call inventory management securitization.`

### 5. Equipment, Automation, And Industrial Receivables Search

Rows:

- `ABF-012`
- `ABF-013`

Zebra and Honeywell may have customer receivables, leases, financing receivables, or receivable-sale programs in detailed footnotes. The current packet layer does not prove that yet.

The correct current status is:

`queued`

## Claim Upgrade

Before this pass, asset-backed finance was mostly a queue.

After this pass, the safe claim is:

`The asset-backed finance lane has first-pass filed evidence for Synchrony's merchant-linked loan receivables and Pool's receivables facility. It also has collateral-search rows for Arrow, Global Industrial, MSC, Target, Dollar General, Zebra, Honeywell, and Henry Schein. The strongest current capital-flow evidence is not broad securitization proof; it is a narrower finding that consumer receivables and seasonal distributor receivables are already visible financeable assets in the packet layer.`

What we still cannot say:

`The broader distributor and retailer set has securitized, pledged, or warehoused its receivables or inventory.`

## Current Status By Claim Bucket

| Claim | Current Bucket | Why |
|---|---|---|
| Asset-backed lane is worth deep extraction | `filed` | Synchrony and Pool provide true first-pass finance rows; other candidates define the search field. |
| Synchrony consumer receivables are a credit-asset channel | `filed` | Loan receivables, purchase volume, funding base, NIM, CET1, and charge-off range are visible. |
| Pool receivables facility finances seasonal working capital | `filed` | Receivables facility outstanding amounts are visible in Q1/Q2 2026 packet evidence. |
| Arrow and distributors are collateral-rich candidates | `queued` | Receivables/inventory are visible, but financing documents are not. |
| Retail inventory is asset-backed finance | `queued` | Current evidence shows inventory/capex/operating assets, not collateral funding. |
| Broad securitization claim | `queued` | ABS/trust/SPV filings have not been extracted. |

## Next Extraction Order

1. Synchrony 2025 10-K and Q2 `2026` 10-Q funding footnotes, securitization notes, credit-card trust filings, allowance, charge-off, and delinquency tables.
2. Pool Q1/Q2 `2026` receivables-facility footnotes and facility agreement.
3. Arrow 2025 10-K and Q2 `2026` 10-Q receivables, inventory, supplier protections, factoring, and credit-facility collateral language.
4. Global Industrial Q2 `2026` 10-Q debt/receivables/inventory notes and any factoring/supplier-finance disclosures.
5. MSC 2025 10-K debt footnote, revolver terms, receivables aging, and inventory pledge language.
6. Target and Dollar General 10-K credit-facility, supplier-finance, inventory, and payables disclosures.
7. Henry Schein customer-finance/equipment leasing receivable and supplier-finance disclosures.
8. Zebra and Honeywell receivable-sale, lease/customer-finance, or factoring disclosures.

## Bottom Line

The asset-backed lane is now live, but it is more uneven than refinancing or acquisition finance.

The simple read:

`The strongest current evidence is Synchrony's consumer receivables and Pool's receivables facility. The broader distributor and retailer universe is working-capital heavy, but we should not call that asset-backed finance until the filings show collateralized funding, sale, securitization, warehouse, pledge, or credit-risk transfer.`

The next proof step is:

`working-capital row -> financing footnote -> facility/trust/SPV document -> collateral pool -> advance/loss/funding terms -> bounded claim`

