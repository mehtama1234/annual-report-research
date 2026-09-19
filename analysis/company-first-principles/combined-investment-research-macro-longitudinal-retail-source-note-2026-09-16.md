# Longitudinal retail macro bridge source note

Research date: `2026-09-16`

This note extends the retail macro bridge with FY2020–FY2022 observations from
official SEC XBRL company-facts records. The values are reported operating cash
flow less reported payments to acquire property, plant, and equipment. They
are cash-after-property screens, not normalized owner cash.

## Added observations

| Company | Fiscal period | Operating cash flow ($M) | Property/capex ($M) | Cash after property ($M) | SEC company-facts source |
| --- | --- | ---: | ---: | ---: | --- |
| Target | FY2020 | 10,525 | 2,649 | 7,876 | [CIK 0000027419](https://data.sec.gov/api/xbrl/companyfacts/CIK0000027419.json) |
| Target | FY2021 | 8,625 | 3,544 | 5,081 | [CIK 0000027419](https://data.sec.gov/api/xbrl/companyfacts/CIK0000027419.json) |
| Target | FY2022 | 4,018 | 5,528 | -1,510 | [CIK 0000027419](https://data.sec.gov/api/xbrl/companyfacts/CIK0000027419.json) |
| Walmart | FY2021 | 36,074 | 10,264 | 25,810 | [CIK 0000104169](https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json) |
| Walmart | FY2022 | 24,181 | 13,106 | 11,075 | [CIK 0000104169](https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json) |
| Walmart | FY2023 | 28,841 | 16,857 | 11,984 | [CIK 0000104169](https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json) |
| TJX | FY2021 | 4,562 | 568 | 3,994 | [CIK 0000109198](https://data.sec.gov/api/xbrl/companyfacts/CIK0000109198.json) |
| TJX | FY2022 | 3,057 | 1,045 | 2,012 | [CIK 0000109198](https://data.sec.gov/api/xbrl/companyfacts/CIK0000109198.json) |
| TJX | FY2023 | 4,084 | 1,457 | 2,627 | [CIK 0000109198](https://data.sec.gov/api/xbrl/companyfacts/CIK0000109198.json) |

The SEC records use the `NetCashProvidedByUsedInOperatingActivities` and
`PaymentsToAcquirePropertyPlantAndEquipment` USD facts. Fiscal periods are
mapped to the dominant calendar-year macro regime by the existing bridge; the
retail fiscal years do not align perfectly with calendar years.

## Interpretation boundary

The extended panel makes the stress sequence visible: Target's cash-after-
property screen fell to a negative `$1.510B` in FY2022 as capex rose during the
inflation shock; Walmart's screen remained positive but compressed; and TJX's
off-price screen also compressed before recovering. These observations are
consistent with, but do not establish, an affordability or macro causal effect.
Inventory, supplier terms, pandemic distortions, tariffs, maintenance versus
growth capex, leases, taxes, services, dilution, and management actions remain
confounders.

## Safe claim

`The retail cohort now has a 2020–2026 longitudinal cash-after-property panel
with official macro anchors. It provides a stronger regime-consistency and
falsifier surface, but it remains a reported cash screen rather than causal
proof or normalized common-owner cash.`
