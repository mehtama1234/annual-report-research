#!/usr/bin/env python3
"""Verify the structured artifacts for the combined investment-research pilots."""

from __future__ import annotations

import csv
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT_DIR = ROOT / "analysis" / "company-first-principles"
LEDGER_DIR = PILOT_DIR / "data"

LEDGER_HEADER = [
    "gate_id",
    "stage",
    "question",
    "entity_or_metric",
    "evidence_value",
    "period",
    "source_artifact",
    "current_status",
    "what_is_proven",
    "missing_upgrade",
]

PILOT_LEDGERS = [
    LEDGER_DIR / "combined-investment-research-pilot-01-wheaton-antamina.csv",
    LEDGER_DIR / "combined-investment-research-pilot-02-affordability-value.csv",
    LEDGER_DIR / "combined-investment-research-pilot-03-apollo-athene.csv",
]

WORKBENCH = LEDGER_DIR / "combined-investment-research-pilot-02-retail-valuation-workbench.csv"
ANTAMINA_WORKBENCH = LEDGER_DIR / "combined-investment-research-pilot-01-antamina-scenario-workbench.csv"
APOLLO_WORKBENCH = LEDGER_DIR / "combined-investment-research-pilot-03-apollo-sotp-workbench.csv"
APOLLO_BRIDGE = LEDGER_DIR / "combined-investment-research-pilot-03-apollo-common-owner-bridge.csv"
RETAIL_BRIDGE = LEDGER_DIR / "combined-investment-research-pilot-02-retail-owner-cash-bridge.csv"
RETAIL_BURDEN = LEDGER_DIR / "combined-investment-research-pilot-02-retail-burden-normalization.csv"
RETAIL_CASH_SCREEN = LEDGER_DIR / "combined-investment-research-pilot-02-retail-normalized-cash-screen.csv"
RETAIL_SUPPORT_DEPENDENCY = LEDGER_DIR / "combined-investment-research-pilot-02-retail-cash-quality-support-dependency-2026-09-15.csv"
RETAIL_PER_SHARE = LEDGER_DIR / "combined-investment-research-pilot-02-retail-annual-per-share-cash.csv"
RETAIL_STACKED_RESIDUAL_PER_SHARE = LEDGER_DIR / "combined-investment-research-pilot-02-retail-stacked-residual-per-share-sensitivity-2026-09-16.csv"
RETAIL_ANNUAL_LEASE_TAX_CASH = LEDGER_DIR / "combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.csv"
RETAIL_ANNUAL_COHORT_DENOMINATOR = LEDGER_DIR / "combined-investment-research-pilot-02-retail-annual-cohort-denominator-control-2026-09-17.csv"
RETAIL_ANNUAL_ATTACHED_FRONTIER = LEDGER_DIR / "combined-investment-research-pilot-02-retail-annual-attached-services-cash-frontier-2026-09-17.csv"
RETAIL_ANNUAL_EXPECTATION_SCREEN = LEDGER_DIR / "combined-investment-research-pilot-02-retail-annual-reported-cash-expectation-screen-2026-09-17.csv"
RETAIL_INTERIM_LEASE_TAX_SEARCH = LEDGER_DIR / "combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.csv"
RETAIL_INTERIM_INLINE_XBRL_SEARCH = LEDGER_DIR / "combined-investment-research-pilot-02-retail-interim-inline-xbrl-search-2026-09-18.csv"
QOE_OVERLAY = LEDGER_DIR / "combined-investment-research-quality-of-earnings-financial-shenanigans-overlay-2026-09-16.csv"
QOE_RETAIL_CASH_CONVERSION = LEDGER_DIR / "combined-investment-research-quality-of-earnings-retail-cash-conversion-screen-2026-09-16.csv"
QOE_COMPOSITE_SCHEMA = LEDGER_DIR / "combined-investment-research-quality-of-earnings-composite-input-schema-2026-09-16.csv"
QOE_CURRENT_RETAIL_EARNINGS_CASH = LEDGER_DIR / "combined-investment-research-quality-of-earnings-current-retail-earnings-cash-screen-2026-09-16.csv"
QOE_CURRENT_RETAIL_COMPOSITE_PANEL = LEDGER_DIR / "combined-investment-research-quality-of-earnings-current-retail-composite-input-panel-2026-09-16.csv"
QOE_RETAIL_COMPARABILITY = LEDGER_DIR / "combined-investment-research-quality-of-earnings-retail-comparability-bridge-2026-09-16.csv"
QOE_RETAIL_TREND_DIAGNOSTICS = LEDGER_DIR / "combined-investment-research-quality-of-earnings-retail-trend-diagnostics-2026-09-16.csv"
QOE_RETAIL_TRANSITION_PANEL = LEDGER_DIR / "combined-investment-research-quality-of-earnings-retail-transition-panel-2026-09-16.csv"
QOE_CAPITAL_FLOW_RATIO_PANEL = LEDGER_DIR / "combined-investment-research-quality-of-earnings-capital-flow-ratio-panel-2026-09-16.csv"
QOE_RETAIL_COMPONENT_SCREEN = LEDGER_DIR / "combined-investment-research-quality-of-earnings-retail-component-screen-2026-09-16.csv"
EVIDENCE_CHAIN_HANDOFF_MATRIX = LEDGER_DIR / "combined-investment-research-evidence-chain-handoff-matrix-2026-09-16.csv"
CA06_PROMOTION_MATRIX = LEDGER_DIR / "combined-investment-research-ca06-promotion-matrix-2026-09-16.csv"
VALUATION_PROMOTION_MATRIX = LEDGER_DIR / "combined-investment-research-valuation-promotion-matrix-2026-09-16.csv"
RETAIL_FIXED_EFFECT_DIAGNOSTIC = LEDGER_DIR / "combined-investment-research-through-cycle-retail-fixed-effect-diagnostic-2026-09-16.csv"
APOLLO_RELATED_PARTY = LEDGER_DIR / "combined-investment-research-pilot-03-apollo-related-party-return-bridge.csv"
APOLLO_FEE_ROLLFORWARD = LEDGER_DIR / "capital-flow-apollo-athene-fee-rollforward-boundary-2026-09-15.csv"
APOLLO_NAMED_ROUTES = LEDGER_DIR / "combined-investment-research-pilot-03-apollo-named-asset-return-routes.csv"
APOLLO_STATUTORY_NAMED_ASSET_MAP = LEDGER_DIR / "capital-flow-apollo-athene-statutory-safe-cashlike-issuer-borrower-map-pass-1.csv"
APOLLO_BA_PART1 = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv"
APOLLO_BA_PART2 = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-parser-pass-1.csv"
APOLLO_BA_PART2_RECON = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-reconciliation-pass-1.csv"
APOLLO_BA_PART3 = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv"
APOLLO_BA_PART3_MATCH = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-part3-part1-cusip-match-pass-1.csv"
APOLLO_BA_CONTINUITY = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv"
APOLLO_BA_CONTINUITY_SUMMARY = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-summary-pass-1.csv"
APOLLO_BA_LOT_QUEUE = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-lot-review-queue-pass-1.csv"
APOLLO_BA_SALE_CROSSWALK = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-sale-schedule-d-crosswalk-pass-1.csv"
APOLLO_BA_INCOME_QUEUE = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-part1-income-review-queue-pass-1.csv"
APOLLO_BA_EXACT_LOT_REVIEW = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-ba-exact-lot-page-review-pass-1.csv"
APOLLO_BA_INCOME_RECONCILIATION = LEDGER_DIR / "capital-flow-apollo-athene-statutory-ba-income-category-reconciliation-pass-1.csv"
APOLLO_PAGE18_NII = LEDGER_DIR / "capital-flow-apollo-athene-statutory-page18-net-investment-income-full-table-pass-1.csv"
APOLLO_SCHEDULE_D_INTEREST_REPAIR = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-d-interest-column-repair-pass-1.csv"
APOLLO_PAGE18_SCHEDULE_D_PERIMETER = LEDGER_DIR / "capital-flow-apollo-athene-statutory-page18-schedule-d-perimeter-bridge-pass-2.csv"
APOLLO_SCHEDULE_D_INTEREST_SUBTOTAL = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-d-interest-subtotal-control-pass-1.csv"
APOLLO_INCOME_POPULATION_BOUNDARY = LEDGER_DIR / "capital-flow-apollo-athene-statutory-income-population-boundary-pass-1.csv"
APOLLO_PAGE18_SCHEDULE_D_RECONCILIATION = LEDGER_DIR / "capital-flow-apollo-athene-statutory-page18-schedule-d-income-reconciliation-pass-3.csv"
APOLLO_LEGAL_ENTITY_BRIDGE = LEDGER_DIR / "capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.csv"
APOLLO_LIABILITY_BURDEN = LEDGER_DIR / "capital-flow-apollo-athene-statutory-liability-interest-burden-bridge-pass-1.csv"
APOLLO_LIABILITY_LOB = LEDGER_DIR / "capital-flow-apollo-athene-statutory-liability-interest-by-line-of-business-pass-1.csv"
APOLLO_DERIVATIVE_HEDGE = LEDGER_DIR / "capital-flow-apollo-athene-statutory-derivative-hedge-boundary-pass-1.csv"
APOLLO_SCHEDULE_DB_PART_C = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-db-part-c-ledger-pass-1.csv"
APOLLO_SCHEDULE_DB_PART_C_SCHEDULE_D = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-db-part-c-schedule-d-crosswalk-pass-1.csv"
APOLLO_SCHEDULE_DB_PART_C_NAMED_LOT = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.csv"
APOLLO_SCHEDULE_DB_PART_C_NAMED_LOT_QUEUE = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-acquisition-queue-pass-1.csv"
APOLLO_AP_GRANGE_BRIDGE = PILOT_DIR / "capital-flow-apollo-athene-ap-grange-prepayment-cross-entity-bridge-pass-2-2026-09-18.md"
APOLLO_AP_GRANGE_SEARCH_BOUNDARY = PILOT_DIR / "capital-flow-apollo-athene-ap-grange-call-settlement-search-boundary-pass-3-2026-09-18.md"
APOLLO_AP_GRANGE_CALL_STATUTORY = LEDGER_DIR / "capital-flow-apollo-athene-ap-grange-call-statutory-bridge-pass-1-2026-09-18.csv"
APOLLO_AP_GRANGE_TRANCHE_A_CASH_ACCRUAL = LEDGER_DIR / "capital-flow-apollo-athene-ap-grange-tranche-a-cash-accrual-crosswalk-2026-09-18.csv"
APOLLO_RECEIPT_FRONTIER = LEDGER_DIR / "capital-flow-apollo-athene-parent-receipt-attribution-frontier-2026-09-15.csv"
APOLLO_Q2_RECEIPT_FRONTIER = LEDGER_DIR / "capital-flow-apollo-athene-q2-parent-receipt-attribution-frontier-2026-09-15.csv"
APOLLO_LIQUIDITY_BOUNDARY = LEDGER_DIR / "capital-flow-apollo-athene-q2-policyholder-liquidity-repo-burden-boundary-2026-09-15.csv"
APOLLO_ARI_SELLER_CASH = LEDGER_DIR / "capital-flow-apollo-athene-ari-q2-seller-cash-debt-waterfall-upgrade-2026-09-15.csv"
APOLLO_ARI_CASH_RECONCILIATION = LEDGER_DIR / "capital-flow-apollo-athene-ari-q2-cash-flow-reconciliation-2026-09-15.csv"
APOLLO_ARI_TRANSACTION_TERMS = LEDGER_DIR / "capital-flow-apollo-athene-ari-transaction-terms-boundary-2026-09-16.csv"
APOLLO_ARI_PAYMENT_MECHANICS = LEDGER_DIR / "capital-flow-apollo-athene-ari-closing-payment-mechanics-boundary-2026-09-16.csv"
APOLLO_ARI_POST_CLOSE_SEARCH = LEDGER_DIR / "capital-flow-apollo-athene-ari-post-close-proof-search-boundary-2026-09-16.csv"
APOLLO_ARI_CASH_DELTA = LEDGER_DIR / "capital-flow-apollo-athene-ari-cash-perimeter-delta-boundary-2026-09-16.csv"
APOLLO_ARI_AUM_OUTFLOW = LEDGER_DIR / "capital-flow-apollo-athene-ari-aum-outflow-boundary-2026-09-16.csv"
APOLLO_ARI_PERIMETER_RECONCILIATION = LEDGER_DIR / "capital-flow-apollo-athene-ari-perimeter-reconciliation-2026-09-15.csv"
APOLLO_ARI_LIQUIDATION_DISTRIBUTION = LEDGER_DIR / "capital-flow-apollo-athene-ari-liquidation-distribution-boundary-2026-09-16.csv"
WHEATON_FORWARD_PROFILE = LEDGER_DIR / "capital-flow-wheaton-antamina-investor-day-forward-profile-boundary-2026-09-16.csv"
WHEATON_FORWARD_PROFILE_URL = "https://s203.q4cdn.com/976005377/files/doc_presentations/2026/Sep/16/2026-Corporate-Presentation-September.pdf"
WHEATON_TECK_RESERVE_CROSS_CHECK = LEDGER_DIR / "capital-flow-wheaton-antamina-teck-reserve-cross-check-2026-09-16.csv"
WHEATON_CREDIT_AGREEMENT_BOUNDARY = LEDGER_DIR / "capital-flow-wheaton-antamina-credit-agreement-waterfall-boundary-2026-09-16.csv"
WHEATON_MATURITY_CLIFF = LEDGER_DIR / "capital-flow-wheaton-antamina-term-maturity-cliff-screen-2026-09-16.csv"
WHEATON_MATURITY_BULLET = LEDGER_DIR / "capital-flow-wheaton-antamina-term-maturity-bullet-coverage-screen-2026-09-16.csv"
WHEATON_Q03_RETURN_INPUT_SCHEMA = LEDGER_DIR / "capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.csv"
WHEATON_Q03_METAL_CREDIT_BOUNDARY = LEDGER_DIR / "capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.csv"
WHEATON_BHP_SOURCE_MANIFEST = LEDGER_DIR / "capital-flow-wheaton-antamina-bhp-fy2026-source-manifest-2026-09-16.csv"
WHEATON_BHP_PAYABLE_SILVER = LEDGER_DIR / "capital-flow-wheaton-antamina-bhp-fy2026-payable-silver-quantity-boundary-2026-09-16.csv"
APOLLO_Q2_PARENT_RECEIPT_REFRESH = LEDGER_DIR / "capital-flow-apollo-athene-q2-parent-receipt-refresh-2026-09-16.csv"
APOLLO_2026_CREDIT_AGREEMENT_PURPOSE = LEDGER_DIR / "capital-flow-apollo-athene-2026-credit-agreement-purpose-perimeter-2026-09-17.csv"
APOLLO_INTERCOMPANY_NOTE_LONGITUDINAL = LEDGER_DIR / "capital-flow-apollo-athene-intercompany-note-longitudinal-refresh-2026-09-16.csv"
APOLLO_MF1_GROSS_PROCEEDS_SCREEN = LEDGER_DIR / "capital-flow-apollo-athene-mf1-gross-proceeds-income-denominator-screen-2026-09-17.csv"
APOLLO_MF1_SAME_CUSIP_JOIN = LEDGER_DIR / "capital-flow-apollo-athene-mf1-same-cusip-servicing-join-boundary-2026-09-17.csv"
APOLLO_MF1_REMITTANCE_ACCESS = LEDGER_DIR / "capital-flow-apollo-athene-mf1-remittance-access-boundary-2026-09-16.csv"
APOLLO_ATHENE_CORPORATE_STRUCTURE_BOUNDARY = LEDGER_DIR / "capital-flow-apollo-athene-corporate-structure-presentation-boundary-2026-09-16.csv"
APOLLO_DEBT_SOLUTIONS_CARRY = LEDGER_DIR / "capital-flow-apollo-athene-apollo-debt-solutions-coupon-carry-sensitivity-2026-09-16.csv"
APOLLO_DEBT_SOLUTIONS_ISSUER_BRIDGE = LEDGER_DIR / "capital-flow-apollo-athene-apollo-debt-solutions-issuer-cash-return-bridge-2026-09-16.csv"
APOLLO_DEBT_SOLUTIONS_PAYMENT_BOUNDARY = LEDGER_DIR / "capital-flow-apollo-athene-apollo-debt-solutions-payment-observability-boundary-2026-09-16.csv"
APOLLO_Q07_COMMON_OWNER_INPUT_SCHEMA = LEDGER_DIR / "capital-flow-apollo-athene-q07-common-owner-input-schema-2026-09-16.csv"
RETAIL_OWNER_CASH_INPUT_SCHEMA = LEDGER_DIR / "capital-flow-retail-owner-cash-input-schema-2026-09-16.csv"
CROSS_SECTOR_COMPARISON = LEDGER_DIR / "combined-investment-research-cross-sector-comparison-2026-09-16.csv"
SOURCE_FAMILY_ROUTES = LEDGER_DIR / "combined-investment-research-source-family-routes-2026-09-16.csv"
CAUSAL_TEST_PROTOCOL = LEDGER_DIR / "combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.csv"
MACRO_CURRENT_REGIME_MEMO = PILOT_DIR / "combined-investment-research-macro-current-regime-validation-2026-09-15.md"
REVIEWERS_GUIDE = PILOT_DIR / "combined-investment-research-reviewers-guide.md"
NEXT_CYCLE_EXPANSION = PILOT_DIR / "combined-investment-research-next-cycle-candidate-expansion-2026-09-16.md"
RETAIL_PANEL_DIAGNOSTIC = LEDGER_DIR / "combined-investment-research-through-cycle-retail-panel-diagnostic-2026-09-16.csv"
RETAIL_WITHIN_DIAGNOSTIC = LEDGER_DIR / "combined-investment-research-through-cycle-retail-within-company-diagnostic-2026-09-16.csv"
RETAIL_LAGGED_DIAGNOSTIC = LEDGER_DIR / "combined-investment-research-through-cycle-retail-lagged-diagnostic-2026-09-16.csv"
RETAIL_CAPEX_PUBLIC_REFRESH = LEDGER_DIR / "combined-investment-research-pilot-02-retail-capex-public-source-refresh-2026-09-16.csv"
RETAIL_ATTACHED_SERVICES_PUBLIC_REFRESH = LEDGER_DIR / "combined-investment-research-pilot-02-retail-attached-services-public-source-refresh-2026-09-16.csv"
EXPANSION_LANE_QOE_OVERLAY = LEDGER_DIR / "combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.csv"
EXPANSION_PROMOTION_ACTIONS = LEDGER_DIR / "combined-investment-research-expansion-promotion-action-register-2026-09-17.csv"
INDUSTRIAL_EVIDENCE = LEDGER_DIR / "combined-investment-research-industrial-uptime-evidence-register-2026-09-17.csv"
INDUSTRIAL_PROMOTION_ACTIONS = LEDGER_DIR / "combined-investment-research-industrial-uptime-promotion-action-register-2026-09-17.csv"
INDUSTRIAL_VALUATION = LEDGER_DIR / "combined-investment-research-industrial-uptime-valuation-workbench-2026-09-17.csv"
INDUSTRIAL_BREAKERS = LEDGER_DIR / "combined-investment-research-industrial-uptime-thesis-breaker-register-2026-09-17.csv"
URI_H1_CASH_CLAIM_BRIDGE = LEDGER_DIR / "capital-flow-uri-h1-2026-cash-claim-bridge-pass-1.csv"
APOLLO_SUPPLEMENT_BOUNDARY = LEDGER_DIR / "capital-flow-apollo-q2-financial-supplement-parent-receipt-search-boundary-2026-09-15.csv"
APOLLO_HOLDCO_BOUNDARY = PILOT_DIR / "capital-flow-apollo-q2-holdco-liquidity-intercompany-boundary-2026-09-15.md"
WHEATON_PACKET_BOUNDARY = LEDGER_DIR / "capital-flow-wheaton-antamina-local-packet-settlement-search-boundary-2026-09-15.csv"
WHEATON_FIRST_DELIVERY_BOUNDARY = LEDGER_DIR / "capital-flow-wheaton-antamina-q2-first-delivery-receipt-boundary-2026-09-15.csv"
WHEATON_PRODUCTION_RECEIPT_BRIDGE = LEDGER_DIR / "capital-flow-wheaton-antamina-production-receipt-bridge-pass-1.csv"
WHEATON_POST_Q2_SEARCH_REFRESH = LEDGER_DIR / "capital-flow-wheaton-antamina-post-q2-public-search-refresh-2026-09-16.csv"
WHEATON_AFTER_TAX_FRONTIER = LEDGER_DIR / "capital-flow-wheaton-antamina-after-tax-financed-allocation-frontier-2026-09-15.csv"
WHEATON_RESERVE_CEILING = LEDGER_DIR / "capital-flow-wheaton-antamina-reserve-constrained-delivery-ceiling-2026-09-15.csv"
WHEATON_RESERVE_RECOVERY_FRONTIER = LEDGER_DIR / "capital-flow-wheaton-antamina-reserve-capped-upfront-recovery-frontier-2026-09-15.csv"
TJX_TEMPORARY_SUPPORT = LEDGER_DIR / "combined-investment-research-pilot-02-tjx-h1-temporary-support.csv"
TJX_CAPEX_CLASSIFICATION = PILOT_DIR / "combined-investment-research-pilot-02-retail-capex-classification.md"
RETAIL_KNOWN_GROWTH_FRONTIER = PILOT_DIR / "combined-investment-research-retail-known-growth-floor-frontier-2026-09-18.md"
RETAIL_KNOWN_GROWTH_FRONTIER_DATA = LEDGER_DIR / "combined-investment-research-retail-known-growth-floor-frontier-2026-09-18.csv"
TJX_Q2_CASH_CAPEX_BOUNDARY = LEDGER_DIR / "combined-investment-research-tjx-q2-cash-capex-boundary-2026-09-18.csv"
RETAIL_H1_DENOMINATOR_HANDOFF = LEDGER_DIR / "combined-investment-research-retail-h1-owner-cash-denominator-handoff-2026-09-17.csv"
RETAIL_TEMPORARY_SUPPORT = PILOT_DIR / "combined-investment-research-pilot-02-retail-temporary-support.md"
RETAIL_SUPPLIER_FINANCE = LEDGER_DIR / "combined-investment-research-pilot-02-retail-supplier-finance-boundary.csv"
RETAIL_SUPPLIER_FINANCE_ROLLFORWARD = LEDGER_DIR / "combined-investment-research-pilot-02-retail-supplier-finance-roll-forward-2026-09-16.csv"
RETAIL_SUPPLIER_FINANCE_SETTLEMENT_FRONTIER = LEDGER_DIR / "combined-investment-research-retail-supplier-finance-settlement-frontier-2026-09-18.csv"
RETAIL_ATTACHED_SERVICES = LEDGER_DIR / "combined-investment-research-pilot-02-retail-attached-services-boundary.csv"
RETAIL_ATTACHED_FRONTIER = LEDGER_DIR / "combined-investment-research-pilot-02-retail-attached-services-cash-frontier-2026-09-15.csv"
RETAIL_PROMOTION_ACTIONS = LEDGER_DIR / "combined-investment-research-retail-promotion-action-register-2026-09-17.csv"
FPL_HISTORICAL_RECOVERY_BOUNDARY = LEDGER_DIR / "capital-flow-fpl-sppcrc-historical-recovery-boundary-2026-09-16.csv"
FPL_RATE_CLASS_FACTORS = LEDGER_DIR / "capital-flow-fpl-2026-sppcrc-rate-class-factor-boundary-2026-09-16.csv"
FPL_RATE_CLASS_DETERMINANTS = LEDGER_DIR / "capital-flow-fpl-sppcrc-rate-class-determinant-boundary-2026-09-16.csv"
FPL_BILLING_RECEIPT_CHASE = LEDGER_DIR / "capital-flow-fpl-billing-determinant-category-receipt-proof-chase-pass-1.csv"
FPL_DISTRIBUTION_INSPECTION_REFRESH = PILOT_DIR / "capital-flow-fpl-distribution-inspection-official-psc-source-refresh-2026-09-16.md"
DUKE_ANDERSON_COST_SENSITIVITY = LEDGER_DIR / "capital-flow-duke-anderson-project-cost-attribution-sensitivity-2026-09-17.csv"
DUKE_ANDERSON_APPROVAL_BOUNDARY = LEDGER_DIR / "capital-flow-duke-anderson-county-generation-approval-recovery-boundary-2026-09-16.csv"
URI_REPORTING_REGIME_BOUNDARY = LEDGER_DIR / "capital-flow-uri-abl-borrowing-base-reporting-regime-boundary-2026-09-16.csv"
URI_BORROWING_BASE_CHASE = LEDGER_DIR / "capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.csv"
URI_ABL_PROXY_BRIDGE = LEDGER_DIR / "capital-flow-uri-abl-public-disclosure-proxy-bridge-pass-1.csv"
URI_Q13_NEXT_SOURCE_PACKAGE = LEDGER_DIR / "capital-flow-uri-q13-next-source-package-2026-09-18.csv"
APOLLO_AP_GRANGE_NEXT_SOURCE_PACKAGE = LEDGER_DIR / "capital-flow-apollo-athene-ap-grange-next-source-package-2026-09-18.csv"
WHEATON_Q03_NEXT_SOURCE_PACKAGE = LEDGER_DIR / "capital-flow-wheaton-antamina-q03-next-source-package-2026-09-18.csv"
APOLLO_Q07_NEXT_SOURCE_PACKAGE = LEDGER_DIR / "capital-flow-apollo-athene-q07-next-source-package-2026-09-18.csv"
INSURANCE_Q12_NEXT_SOURCE_PACKAGE = LEDGER_DIR / "capital-flow-insurance-q12-next-source-package-2026-09-18.csv"
WHEATON_FINANCING_CASH_FLOW = LEDGER_DIR / "capital-flow-wheaton-antamina-financing-cash-flow-upgrade-2026-09-15.csv"
RETAIL_ATTACHED_DENOMINATOR_RECONCILIATION = LEDGER_DIR / "combined-investment-research-pilot-02-walmart-attached-income-denominator-reconciliation-2026-09-16.csv"
RETAIL_COHORT_MATRIX = LEDGER_DIR / "combined-investment-research-pilot-02-retail-cohort-operating-matrix.csv"
RETAIL_COMMON_PERIOD_CASH = LEDGER_DIR / "combined-investment-research-pilot-02-retail-common-period-cash-matrix.csv"
RETAIL_COHORT_WORKING_CAPITAL = LEDGER_DIR / "combined-investment-research-pilot-02-retail-cohort-inventory-payable-balance-screen-2026-09-15.csv"
RETAIL_MARGIN_WORKING_CAPITAL = LEDGER_DIR / "combined-investment-research-pilot-02-retail-margin-working-capital-normalization.csv"
RETAIL_MARGIN_SUPPORT_TRANSITION = LEDGER_DIR / "combined-investment-research-pilot-02-retail-margin-support-transition-2026-09-16.csv"
RETAIL_CAPEX_CLASSIFICATION = LEDGER_DIR / "combined-investment-research-pilot-02-retail-capex-classification.csv"
RETAIL_CAPEX_SENSITIVITY = LEDGER_DIR / "combined-investment-research-pilot-02-retail-capex-allocation-sensitivity.csv"
RETAIL_CAPEX_BOUNDARY_OVERLAY = LEDGER_DIR / "combined-investment-research-pilot-02-retail-capex-boundary-overlay-2026-09-15.csv"
RETAIL_POST_FINANCING_RESIDUAL = LEDGER_DIR / "combined-investment-research-pilot-02-retail-post-financing-residual-screen-2026-09-15.csv"
WALMART_CASH_DENOMINATOR = LEDGER_DIR / "combined-investment-research-pilot-02-walmart-h1-owner-cash-denominator-control-2026-09-15.csv"
TARGET_CASH_DENOMINATOR = LEDGER_DIR / "combined-investment-research-pilot-02-target-h1-owner-cash-denominator-control-2026-09-15.csv"
TARGET_GIFT_CARD_BOUNDARY = LEDGER_DIR / "combined-investment-research-pilot-02-target-gift-card-liability-boundary-2026-09-16.csv"
RETAIL_COHORT_CASH_DENOMINATOR = LEDGER_DIR / "combined-investment-research-pilot-02-retail-cohort-owner-cash-denominator-control-2026-09-15.csv"
APOLLO_CREDIT_QUALITY = LEDGER_DIR / "combined-investment-research-pilot-03-apollo-credit-quality-boundary.csv"
APOLLO_Q2_AMAPS_SOURCE = ROOT / "raw" / "primary-sources" / "capital-flow" / "apollo" / "q2-2026" / "athene-q2-2026-10q.html"
APOLLO_Q2_AMAPS_EXPOSURE = LEDGER_DIR / "capital-flow-apollo-athene-q2-amaps-current-exposure-boundary-2026-09-16.csv"
MARKET_SNAPSHOT_2026_09_16 = LEDGER_DIR / "combined-investment-research-market-snapshot-2026-09-16.csv"
MARKET_SNAPSHOT_2026_09_17 = LEDGER_DIR / "combined-investment-research-market-snapshot-2026-09-17.csv"
CONCORD_SOURCE_ACQUISITION = PILOT_DIR / "capital-flow-apollo-athene-concord-public-document-acquisition-attempt-pass-1.md"
CONCORD_SOURCE_ACQUISITION_DATA = LEDGER_DIR / "capital-flow-apollo-athene-concord-public-document-acquisition-attempt-pass-1.csv"
THESIS_BREAKERS = LEDGER_DIR / "combined-investment-research-thesis-breaker-register.csv"
COMPLETION_AUDIT = LEDGER_DIR / "combined-investment-research-completion-audit.csv"
CAP_CASH_RECONCILIATION = LEDGER_DIR / "combined-investment-research-cash-denominator-reconciliation-2026-09-15.csv"
OWNER_CASH_PROMOTION = LEDGER_DIR / "combined-investment-research-owner-cash-promotion-matrix-2026-09-15.csv"
READER_JS = ROOT / "site" / "reader.js"
METHOD_REGISTRY = LEDGER_DIR / "combined-investment-research-method-registry.csv"
INVESTMENTS_BRIDGE = PILOT_DIR / "combined-investment-research-investments-repo-bridge.md"
INVESTMENTS_ARTICLE_HANDOFF = PILOT_DIR / "combined-investment-research-pilot-01-investments-article-handoff.md"
SOCIAL_THEME_MATRIX = ROOT.parent / "social-research" / "analysis" / "social" / "cross-repository-theme-evidence-matrix.md"
IBIS_CROSSWALK = ROOT / "notes" / "ibis-industries-crosswalk.md"
IBIS_HANDOFF = LEDGER_DIR / "combined-investment-research-pilot-02-ibis-industry-handoff.csv"
INC5000_ROOT = ROOT.parent / "inc5000-analysis"
MACRO_LIQUIDITY_MATRIX = PILOT_DIR / "combined-investment-research-macro-liquidity-transmission-matrix.md"
MACRO_LONGITUDINAL_RETAIL = LEDGER_DIR / "combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.csv"
NEXT_EVIDENCE_QUEUE = LEDGER_DIR / "combined-investment-research-next-evidence-queue.csv"
ACTIVE_PACKET_COVERAGE = LEDGER_DIR / "combined-investment-research-active-pilot-packet-coverage-2026-09-15.csv"
WALMART_CALL_UPGRADE = LEDGER_DIR / "combined-investment-research-pilot-02-walmart-q2-management-call-control-point-upgrade-2026-09-15.csv"
TARGET_CALL_UPGRADE = LEDGER_DIR / "combined-investment-research-pilot-02-target-q2-management-call-control-point-upgrade-2026-09-15.csv"
WORKBENCH_HEADER = [
    "company",
    "valuation_denominator",
    "bear_cash_musd",
    "base_cash_musd",
    "bull_cash_musd",
    "bear_multiple",
    "base_multiple",
    "bull_multiple",
    "bear_value_musd",
    "base_value_musd",
    "bull_value_musd",
    "market_snapshot_musd",
    "base_gap_percent",
    "valuation_status",
    "main_expectation_burden",
    "next_upgrade",
]
ANTAMINA_HEADER = [
    "scenario",
    "upfront_payment_musd",
    "annual_bhp_share_production_moz",
    "payable_factor_pct",
    "initial_stream_share_pct",
    "delivered_threshold_moz",
    "life_of_mine_stream_share_pct",
    "spot_price_usd_oz",
    "stream_payment_pct",
    "burden_haircut_pct",
    "modeled_years",
    "initial_share_years",
    "life_of_mine_share_years",
    "discount_rate_pct",
    "annual_initial_cash_musd",
    "annual_life_of_mine_cash_musd",
    "npv_musd",
    "irr_pct",
    "valuation_status",
    "expectation_burden",
    "next_upgrade",
]
APOLLO_HEADER = [
    "case",
    "normalized_fre_busd",
    "fre_multiple",
    "normalized_sre_busd",
    "sre_multiple",
    "principal_performance_value_busd",
    "common_claims_capital_haircut_busd",
    "fre_value_busd",
    "sre_value_busd",
    "illustrative_equity_value_busd",
    "market_snapshot_busd",
    "gap_to_market_pct",
    "valuation_status",
    "main_expectation_burden",
    "next_upgrade",
]
BRIDGE_HEADER = [
    "line_id", "bridge_stage", "metric", "amount_musd", "period",
    "source_artifact", "status", "interpretation", "next_upgrade",
]
RETAIL_BURDEN_HEADER = [
    "company", "period", "operating_lease_liabilities_musd",
    "lease_cash_or_interest_musd", "diluted_shares_millions",
    "share_based_compensation_musd", "repurchases_musd",
    "maintenance_capex_musd", "growth_or_platform_capex_musd",
    "normalization_status", "source_artifact", "next_upgrade",
]
RETAIL_CASH_SCREEN_HEADER = [
    "company", "period", "reported_cash_after_property_musd",
    "known_one_time_or_cash_support_musd", "share_based_compensation_musd",
    "low_screen_cash_musd", "base_screen_cash_musd", "high_screen_cash_musd",
    "screen_status", "source_artifact", "next_upgrade",
]
RETAIL_PER_SHARE_HEADER = [
    "company", "period", "cash_after_property_musd", "diluted_shares_millions",
    "reported_cash_after_property_per_share_usd", "operating_lease_liabilities_musd",
    "per_share_status", "source_artifact", "next_upgrade",
]
RETAIL_STACKED_RESIDUAL_PER_SHARE_HEADER = [
    "company", "period", "diluted_shares_millions",
    "reported_cash_after_property_musd", "stacked_residual_musd",
    "stacked_residual_per_diluted_share_usd", "status", "source_artifact",
    "next_upgrade",
]
RETAIL_ANNUAL_LEASE_TAX_CASH_HEADER = [
    "company", "period", "cash_after_property_musd",
    "operating_lease_cash_paid_musd", "income_taxes_paid_musd",
    "operating_lease_liabilities_musd", "lease_cash_to_cash_after_property_pct",
    "tax_cash_to_cash_after_property_pct", "status", "what_is_proven",
    "what_is_not_proven", "source_artifact", "next_upgrade",
]
RETAIL_ANNUAL_COHORT_DENOMINATOR_HEADER = [
    "company", "fiscal_period", "operating_cash_flow_musd",
    "property_spending_musd", "cash_after_property_musd",
    "diluted_shares_millions", "cash_after_property_per_diluted_share_usd",
    "operating_lease_cash_musd", "income_tax_cash_musd",
    "supplier_finance_begin_musd", "supplier_finance_end_musd",
    "supplier_finance_movement_musd", "status", "source_artifact",
    "next_upgrade",
]
RETAIL_ANNUAL_ATTACHED_FRONTIER_HEADER = [
    "company", "fiscal_period", "reported_attached_service_pool_musd",
    "zero_percent_cash_musd", "twenty_five_percent_cash_musd",
    "fifty_percent_cash_musd", "seventy_five_percent_cash_musd",
    "one_hundred_percent_cash_musd", "status", "source_artifact",
    "next_upgrade",
]
RETAIL_ANNUAL_EXPECTATION_SCREEN_HEADER = [
    "company", "fiscal_period", "market_cap_musd",
    "reported_cash_after_property_musd",
    "market_cap_to_reported_cash_after_property_multiple", "status",
    "source_artifact", "next_upgrade",
]
RETAIL_INTERIM_LEASE_TAX_SEARCH_HEADER = [
    "search_id", "company", "interim_period", "dedicated_cash_lease_line",
    "dedicated_cash_tax_line", "observed_interim_context", "result_class",
    "what_is_proven", "what_is_not_proven", "source_url", "source_artifact",
    "next_upgrade",
]
RETAIL_INTERIM_INLINE_XBRL_SEARCH_HEADER = [
    "tag_search_id", "company", "interim_period", "tag_or_phrase",
    "searched_route", "result_class", "observed_control",
    "what_is_not_proven", "source_url", "source_artifact",
]
APOLLO_DEBT_SOLUTIONS_CARRY_HEADER = [
    "scenario", "consideration_musd", "issue_principal_musd",
    "implied_issue_share_pct", "coupon_pct", "annual_gross_carry_proxy_musd",
    "five_year_gross_carry_proxy_musd", "status", "what_is_proven",
    "what_is_not_proven", "source_artifact", "next_upgrade",
]
APOLLO_DEBT_SOLUTIONS_ISSUER_BRIDGE_HEADER = [
    "observation_id", "period", "metric", "value_musd", "status",
    "what_is_proven", "what_is_not_proven", "source_artifact", "next_upgrade",
]
APOLLO_DEBT_SOLUTIONS_PAYMENT_BOUNDARY_HEADER = [
    "observation_id", "observation_type", "period_or_date",
    "instrument_or_holder", "observed_value", "status", "what_is_proven",
    "what_is_not_proven", "source_artifact", "next_upgrade",
]
APOLLO_RELATED_PARTY_HEADER = [
    "line_id", "entity", "metric", "amount_musd", "period", "flow_direction",
    "return_or_access_status", "source_artifact", "interpretation", "next_upgrade",
]
APOLLO_NAMED_ROUTES_HEADER = [
    "route_id", "asset_or_wrapper", "athene_entity_evidence_musd",
    "athene_book_or_exposure_musd", "public_cash_or_income_signal_musd",
    "public_destination_or_use", "route_status", "source_artifact",
    "what_is_proven", "missing_upgrade",
]
RETAIL_BRIDGE_HEADER = [
    "company", "period", "revenue_musd", "operating_cash_flow_musd",
    "property_spending_musd", "cash_after_property_musd", "inventory_signal",
    "working_capital_signal", "owner_cash_status", "source_artifact",
    "next_upgrade",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def verify_research_csv_shapes() -> None:
    paths = set(LEDGER_DIR.glob("combined-investment-research*.csv"))
    paths.update(LEDGER_DIR.glob("capital-flow-wheaton-antamina-*-2026-09-15.csv"))
    paths.update(LEDGER_DIR.glob("capital-flow-apollo-athene-*-2026-09-15.csv"))
    for path in sorted(paths):
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.reader(handle))
        if not rows:
            fail(f"research CSV is empty: {path.relative_to(ROOT)}")
        expected_width = len(rows[0])
        mismatches = [
            (index, len(row))
            for index, row in enumerate(rows[1:], start=2)
            if len(row) != expected_width
        ]
        if mismatches:
            fail(f"research CSV shape mismatch in {path.relative_to(ROOT)}: {mismatches[:3]}")


def verify_preserved_primary_artifact_signatures() -> None:
    """Reject present-but-invalid primary artifacts such as access-block pages."""
    html_signatures = {
        ROOT / "raw" / "primary-sources" / "capital-flow" / "debt-refinancing" / "wheaton" / "q2-2026" / "wpm-20260630-ex99-2-mda.htm": "The Company received its first deliveries during the second quarter of 2026",
        ROOT / "raw" / "primary-sources" / "capital-flow" / "debt-refinancing" / "wheaton" / "q2-2026" / "wpm-20260630-ex99-3-financial-statements.htm": "Antamina",
        ROOT / "raw" / "primary-sources" / "capital-flow" / "bhp" / "fy2026" / "bhp-fy2026-20f.htm": "silver streaming agreement",
        ROOT / "raw" / "primary-sources" / "capital-flow" / "bhp" / "fy2026" / "bhp-antamina-streaming-6k-2026-02-17.htm": "5.4&nbsp;million ounces of silver",
        PILOT_DIR / "capital-flow-wheaton-antamina-bhp-q4-production-sales-proxy-upgrade-2026-09-15.md": "double-count the ownership share",
    }
    for path, marker in html_signatures.items():
        if not path.exists():
            fail(f"missing preserved primary artifact: {path.relative_to(ROOT)}")
        content = path.read_text(encoding="utf-8", errors="ignore")
        if marker not in content:
            fail(f"primary artifact signature missing from {path.relative_to(ROOT)}: {marker}")
    bhp_local = ROOT / "raw" / "primary-sources" / "capital-flow" / "bhp" / "fy2026" / "bhp-fy2026-20f.htm"
    if "<TYPE>6-K" not in bhp_local.read_text(encoding="utf-8", errors="ignore"):
        fail("preserved BHP FY2026 artifact is no longer identified as Form 6-K")
    bhp_20f = ROOT / "raw" / "primary-sources" / "capital-flow" / "bhp" / "fy2026" / "bhp-fy2026-20f-canonical.htm"
    bhp_20f_text = bhp_20f.read_text(encoding="utf-8", errors="ignore")
    if 'name="dei:DocumentType"' not in bhp_20f_text or ">20-F<" not in bhp_20f_text:
        fail("preserved BHP FY2026 canonical artifact is no longer identified as Form 20-F")
    teck_aif = ROOT / "raw" / "primary-sources" / "capital-flow" / "teck" / "2025" / "teck-2025-aif.htm"
    teck_aif_text = teck_aif.read_text(encoding="utf-8", errors="ignore") if teck_aif.exists() else ""
    for marker in ("Annual Information Form", "For the year ended December 31, 2025", "Antamina", "US$225 million"):
        if marker not in teck_aif_text:
            fail(f"preserved Teck 2025 AIF signature missing: {marker}")
    antamina_report = ROOT / "raw" / "primary-sources" / "capital-flow" / "antamina" / "2025" / "antamina-technical-report-2024.pdf"
    if not antamina_report.exists() or not antamina_report.read_bytes().startswith(b"%PDF"):
        fail("preserved Antamina technical report is missing or is not a PDF")
    athene_statutory = ROOT / "raw" / "primary-sources" / "capital-flow" / "apollo" / "athene" / "statutory" / "2025" / "athene-annuity-and-life-company-2025-statutory-statement.pdf"
    if not athene_statutory.exists() or not athene_statutory.read_bytes().startswith(b"%PDF"):
        fail("preserved Athene statutory statement is missing or is not a PDF")
    credit_agreement = ROOT / "raw" / "primary-sources" / "capital-flow" / "wheaton" / "2026-03" / "non-revolving-term-facility-credit-agreement.htm"
    credit_text = credit_agreement.read_text(encoding="utf-8", errors="ignore") if credit_agreement.exists() else ""
    for marker in ("Wheaton Precious Metals Corp.", "$1,500,000,000", "Antamina Mine Silver Stream Acquisition", "Bank of Montreal", "0.60:1"):
        if marker not in credit_text:
            fail(f"preserved Wheaton credit-agreement signature missing: {marker}")
    ari_agreement = ROOT / "raw" / "primary-sources" / "capital-flow" / "apollo" / "ari" / "2026-01" / "ari-definitive-purchase-agreement-ex21.htm"
    ari_agreement_text = ari_agreement.read_text(encoding="utf-8", errors="ignore") if ari_agreement.exists() else ""
    for marker in ("Closing Date Calculation Notice", "one hundred-twenty", "True-up"):
        if marker not in ari_agreement_text:
            fail(f"preserved ARI definitive agreement signature missing: {marker}")
    ari_summary = ROOT / "raw" / "primary-sources" / "capital-flow" / "apollo" / "ari" / "2026-01" / "ari-transaction-summary-ex991.htm"
    ari_summary_text = ari_summary.read_text(encoding="utf-8", errors="ignore") if ari_summary.exists() else ""
    for marker in ("99.7%", "loan commitments", "financing contingency"):
        if marker not in ari_summary_text:
            fail(f"preserved ARI transaction summary signature missing: {marker}")
    named_issuer_signatures = {
        ROOT / "raw" / "primary-sources" / "capital-flow" / "apollo" / "named-assets" / "2026-05" / "introducing-amaps.html": ("AMAPS", "structured credit", "asset-backed"),
        ROOT / "raw" / "primary-sources" / "capital-flow" / "concord" / "2025-07" / "concord-1-765b-abs-release.html": ("1.765", "senior notes", "catalog"),
        ROOT / "raw" / "primary-sources" / "capital-flow" / "mf1" / "2026-03" / "mf1-2025-b2-transaction-exhibit.htm": ("SERVICING AGREEMENT", "MF1 COLLATERAL", "Collection Account"),
        ROOT / "raw" / "primary-sources" / "capital-flow" / "mf1" / "2025-05" / "mf1-2025-b2-data-file-procedures-ex99-1.htm": ("MF1 2025-B2", "23 collateral interests", "74 related mortgaged properties"),
    }
    for path, markers in named_issuer_signatures.items():
        if not path.exists():
            fail(f"missing preserved named-issuer artifact: {path.relative_to(ROOT)}")
        content = path.read_text(encoding="utf-8", errors="ignore").lower()
        for marker in markers:
            if marker.lower() not in content:
                fail(f"preserved named-issuer signature missing from {path.relative_to(ROOT)}: {marker}")
    named_issuer_manifest = PILOT_DIR / "data" / "capital-flow-apollo-athene-named-issuer-source-acquisition-2026-09-16.csv"
    if not named_issuer_manifest.exists():
        fail(f"missing named-issuer source manifest: {named_issuer_manifest.relative_to(ROOT)}")
    with named_issuer_manifest.open(newline="", encoding="utf-8") as handle:
        manifest_reader = csv.DictReader(handle)
        expected_manifest_header = [
            "source_id", "route", "issuer_or_wrapper", "same_cusip_route",
            "primary_source_url", "local_source_artifact", "source_period",
            "status", "what_is_proven", "missing_upgrade",
        ]
        if manifest_reader.fieldnames != expected_manifest_header:
            fail(f"named-issuer source manifest header mismatch: {manifest_reader.fieldnames}")
        manifest_rows = list(manifest_reader)
    expected_manifest_routes = {
        "NISA-001": ("AMAPS", "02300A-AA-8", "raw/primary-sources/capital-flow/apollo/named-assets/2026-05/introducing-amaps.html"),
        "NISA-002": ("Concord music-rights ABS", "20633K-AN-8", "raw/primary-sources/capital-flow/concord/2025-07/concord-1-765b-abs-release.html"),
        "NISA-003": ("MF1 2026-FL21 servicing packet", "not-joined-to-592918-AA-4", "raw/primary-sources/capital-flow/mf1/2026-03/mf1-2025-b2-transaction-exhibit.htm"),
        "NISA-004": ("MF1 2025-B2 data procedures", "592918-AA-4", "raw/primary-sources/capital-flow/mf1/2025-05/mf1-2025-b2-data-file-procedures-ex99-1.htm"),
    }
    manifest_source_ids = {row["source_id"] for row in manifest_rows}
    if not set(expected_manifest_routes).issubset(manifest_source_ids):
        fail("named-issuer source manifest baseline route removed")
    for source_id, (route, cusip, artifact) in expected_manifest_routes.items():
        row = next(row for row in manifest_rows if row["source_id"] == source_id)
        if row["route"] != route or row["same_cusip_route"] != cusip or row["local_source_artifact"] != artifact:
            fail(f"named-issuer source manifest route changed: {source_id}")
        if row["status"] != "preserved-source-confirmed" or not (ROOT / artifact).exists():
            fail(f"named-issuer source manifest artifact missing or unconfirmed: {source_id}")
    for extra_row in manifest_rows:
        if extra_row["source_id"] in expected_manifest_routes:
            continue
        extra_artifact = extra_row["local_source_artifact"]
        if not extra_artifact or not (ROOT / extra_artifact).exists():
            fail(f"additional named-issuer artifact missing: {extra_row['source_id']}")
        if extra_row["status"] not in {
            "public-source-refresh-partial",
            "public-source-refresh-insufficient",
            "located-access-controlled",
        }:
            fail(f"additional named-issuer status invalid: {extra_row['source_id']}")
    bhp_boundary = PILOT_DIR / "capital-flow-wheaton-antamina-bhp-fy2026-annual-report-boundary-2026-09-16.md"
    boundary_text = bhp_boundary.read_text(encoding="utf-8", errors="ignore")
    if "https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm" not in boundary_text:
        fail("BHP public-filing boundary lost the canonical Form 20-F route")
    if "Form 6-K results artifact" not in boundary_text:
        fail("BHP public-filing boundary lost the local Form 6-K designation")
    apollo_q2 = ROOT / "raw" / "primary-sources" / "capital-flow" / "apollo" / "q2-2026" / "apollo-2026-q2-10q.pdf"
    if not apollo_q2.exists() or b"/Title (10-Q - 08/10/2026" not in apollo_q2.read_bytes():
        fail(f"preserved Apollo Q2 10-Q is missing or has an unexpected PDF signature: {apollo_q2.relative_to(ROOT)}")
    cross_repository_signatures = {
        ROOT.parent / "social-research" / "analysis" / "social" / "cross-repository-theme-evidence-matrix.md": "Cross-Repository Theme Evidence Matrix",
        ROOT.parent / "inc5000-analysis" / "README.md": "Inc. 5000 — Follow the Money",
        ROOT / "notes" / "ibis-industries-crosswalk.md": "Crosswalk",
    }
    for path, marker in cross_repository_signatures.items():
        if not path.exists():
            fail(f"missing cross-repository source-layer artifact: {path}")
        if marker not in path.read_text(encoding="utf-8", errors="ignore"):
            fail(f"cross-repository source-layer signature missing from {path}: {marker}")
    theme_signatures = {
        PILOT_DIR / "../themes/cultural-value-trust-and-automation-initial-theme-memo.md": "# Cultural Value, Trust, And Automation Initial Theme Memo",
        PILOT_DIR / "../themes/graying-market-initial-theme-memo.md": "# Graying Market Initial Theme Memo",
        PILOT_DIR / "../themes/institutional-operating-infrastructure-initial-theme-memo.md": "# Institutional Operating Infrastructure Initial Theme Memo",
        PILOT_DIR / "../themes/recurring-consumer-interfaces-and-membership-systems-initial-theme-memo.md": "# Recurring Consumer Interfaces And Membership Systems Initial Theme Memo",
        PILOT_DIR / "../themes/technology-ai-platform-initial-theme-memo.md": "# Technology AI-Platform Initial Theme Memo",
        PILOT_DIR / "combined-investment-research-force-to-company-atlas-2026-09-15.md": "# Combined investment research force-to-company atlas",
    }
    for path, marker in theme_signatures.items():
        if not path.exists():
            fail(f"missing theme review anchor: {path.relative_to(ROOT)}")
        if marker not in path.read_text(encoding="utf-8", errors="ignore"):
            fail(f"theme review anchor signature missing from {path.relative_to(ROOT)}: {marker}")
    presentation = ROOT / "raw" / "primary-sources" / "capital-flow" / "wheaton" / "2026-09-16" / "wheaton-investor-day-corporate-presentation-september-2026.pdf"
    if not presentation.exists() or presentation.stat().st_size < 100_000:
        fail(f"preserved Investor Day presentation is missing or implausibly small: {presentation.relative_to(ROOT)}")


def verify_antamina_associate_economics() -> None:
    """Keep the BHP Note 29 entity-level Antamina boundary reproducible."""
    artifact = ROOT / "raw" / "primary-sources" / "capital-flow" / "bhp" / "fy2026" / "bhp-fy2026-20f.htm"
    text = artifact.read_text(encoding="utf-8", errors="ignore")
    for marker in ("Antamina", "33.75", "7,473", "3,029", "1,022", "5,531"):
        if marker not in text:
            fail(f"BHP Antamina associate economics marker missing: {marker}")
    path = PILOT_DIR / "data" / "capital-flow-wheaton-antamina-bhp-associate-economics-boundary-2026-09-16.csv"
    if not path.exists():
        fail(f"missing Antamina associate economics CSV: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "evidence_id", "entity", "period", "metric", "basis", "amount_usd_m",
            "source_artifact", "interpretation", "remaining_gap",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Antamina associate economics header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "revenue": "$7473",
        "profit": "$3029",
        "share_of_profit": "$1022",
        "net_assets": "$5531",
        "group_share_net_assets": "$1867",
        "dividends_received": "$895",
    }
    by_metric = {row["metric"]: row for row in rows}
    if set(by_metric) != set(expected):
        fail(f"Antamina associate economics metric set changed: {sorted(by_metric)}")
    for metric, amount in expected.items():
        row = by_metric[metric]
        if row["amount_usd_m"] != amount or row["source_artifact"] != "raw/primary-sources/capital-flow/bhp/fy2026/bhp-fy2026-20f.htm":
            fail(f"Antamina associate economics row changed: {metric}")
        if not row["remaining_gap"].strip():
            fail(f"Antamina associate economics gap missing: {metric}")


def verify_antamina_mine_plan_burden() -> None:
    """Keep the NI 43-101 annual cost schedule and accounting bases controlled."""
    path = PILOT_DIR / "data" / "capital-flow-wheaton-antamina-mine-plan-burden-schedule-2026-09-16.csv"
    if not path.exists():
        fail(f"missing Antamina mine-plan burden CSV: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "evidence_id", "period", "period_status", "operating_cost_real_usd_m",
            "capital_cost_nominal_usd_m", "source_artifact", "interpretation",
            "remaining_gap",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Antamina mine-plan burden header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 13 or rows[-1]["evidence_id"] != "MPB-TOTAL":
        fail("Antamina mine-plan burden must contain 12 annual rows plus a total")
    annual = rows[:-1]
    expected_years = [str(year) for year in range(2025, 2037)]
    if [row["period"] for row in annual] != expected_years:
        fail("Antamina mine-plan burden year sequence changed")
    if annual[-1]["period_status"] != "partial":
        fail("Antamina 2036 mine-plan row must remain marked partial")
    for row in rows:
        if row["source_artifact"] != "raw/primary-sources/capital-flow/antamina/2025/antamina-technical-report-2024.pdf":
            fail(f"Antamina mine-plan source artifact changed: {row['evidence_id']}")
        for field in ("operating_cost_real_usd_m", "capital_cost_nominal_usd_m"):
            try:
                float(row[field])
            except ValueError:
                fail(f"Antamina mine-plan numeric field invalid: {row['evidence_id']} {field}")
    if rows[-1]["operating_cost_real_usd_m"] != "14681" or rows[-1]["capital_cost_nominal_usd_m"] != "4022":
        fail("Antamina mine-plan published totals changed")


def verify_antamina_silver_production_cross_check() -> None:
    """Keep operator and BHP-share silver observations separated by basis."""
    report = ROOT / "raw/primary-sources/capital-flow/antamina/2024/antamina-sustainability-report-2024.pdf"
    if not report.exists() or not report.read_bytes().startswith(b"%PDF"):
        fail("Antamina 2024 sustainability report is missing or is not a PDF")
    path = PILOT_DIR / "data" / "capital-flow-wheaton-antamina-silver-production-basis-cross-check-2026-09-16.csv"
    if not path.exists():
        fail(f"missing Antamina silver-production cross-check CSV: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "evidence_id", "period", "entity_or_source", "metric", "unit", "basis",
            "value", "source_url", "local_source_artifact", "result_class", "remaining_gap",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Antamina silver cross-check header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 5:
        fail("Antamina silver cross-check must contain five observations")
    expected = {
        "SPB-000": ("2023", "360", "raw/primary-sources/capital-flow/antamina/2023/antamina-sustainability-report-2023.pdf"),
        "SPB-004": ("2023", "352", "raw/primary-sources/capital-flow/antamina/2023/antamina-sustainability-report-2023.pdf"),
        "SPB-001": ("2024", "0.35", "raw/primary-sources/capital-flow/antamina/2024/antamina-sustainability-report-2024.pdf"),
        "SPB-002": ("2024", "0.31", "raw/primary-sources/capital-flow/antamina/2024/antamina-sustainability-report-2024.pdf"),
        "SPB-003": ("2025", "5.4", "raw/primary-sources/capital-flow/bhp/fy2026/bhp-antamina-streaming-6k-2026-02-17.htm"),
    }
    for row in rows:
        evidence_id = row["evidence_id"]
        if evidence_id not in expected:
            fail(f"unexpected Antamina silver cross-check row: {evidence_id}")
        period, value, artifact = expected[evidence_id]
        if row["period"] != period or row["value"] != value or row["local_source_artifact"] != artifact:
            fail(f"Antamina silver cross-check row changed: {evidence_id}")
        if row["result_class"] != "evidence-insufficient" or not row["remaining_gap"].strip():
            fail(f"Antamina silver cross-check boundary changed: {evidence_id}")


def verify_antamina_bhp_share_conversion() -> None:
    """Verify the explicit unit/ownership conversion screen without promoting it to receipts."""
    wheaton_profile = ROOT / "raw/primary-sources/capital-flow/wheaton/2026-02/wheaton-antamina-acquisition-ex99-1-2026-02-16.htm"
    wheaton_text = wheaton_profile.read_text(encoding="utf-8", errors="ignore") if wheaton_profile.exists() else ""
    for marker in ("6.0 Moz", "5.4 Moz", "100 million ounces", "$4.3 billion"):
        if marker not in wheaton_text:
            fail(f"Wheaton Antamina profile marker missing: {marker}")
    path = PILOT_DIR / "data" / "capital-flow-wheaton-antamina-bhp-share-conversion-screen-2026-09-16.csv"
    if not path.exists():
        fail(f"missing Antamina BHP-share conversion CSV: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "screen_id", "period", "source_basis", "operator_silver_mt",
            "operator_silver_moz", "ownership_pct", "mechanical_bhp_share_moz",
            "payable_factor_pct", "payable_sensitivity_moz", "source_artifact",
            "classification", "remaining_gap",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Antamina BHP-share conversion header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "BSC-001": ("2023", 360.0, 11.574269, 3.906318, 3.515686, "raw/primary-sources/capital-flow/antamina/2023/antamina-sustainability-report-2023.pdf"),
        "BSC-002": ("2024", 350.0, 11.252761, 3.797807, 3.418026, "raw/primary-sources/capital-flow/antamina/2024/antamina-sustainability-report-2024.pdf"),
    }
    if len(rows) != 5 or {row["screen_id"] for row in rows} != {"BSC-001", "BSC-002", "BSC-003", "BSC-004", "BSC-005"}:
        fail("Antamina BHP-share conversion screen row set changed")
    for row in rows:
        if row["source_artifact"] and not (ROOT / row["source_artifact"]).exists():
            fail(f"Antamina BHP-share conversion source missing: {row['screen_id']}")
        if row["classification"] not in {"mechanical-conversion-screen", "reported-share-plus-payable-sensitivity", "management-production-profile"}:
            fail(f"Antamina BHP-share conversion classification changed: {row['screen_id']}")
        if not row["remaining_gap"].strip():
            fail(f"Antamina BHP-share conversion gap missing: {row['screen_id']}")
    for screen_id, (period, operator_mt, total_moz, bhp_moz, payable_moz, artifact) in expected.items():
        row = next(row for row in rows if row["screen_id"] == screen_id)
        if row["period"] != period or row["source_artifact"] != artifact:
            fail(f"Antamina BHP-share conversion metadata changed: {screen_id}")
        if not math.isclose(float(row["operator_silver_mt"]), operator_mt, abs_tol=0.001):
            fail(f"Antamina BHP-share conversion operator tonnes changed: {screen_id}")
        if not math.isclose(float(row["operator_silver_moz"]), total_moz, abs_tol=0.000001):
            fail(f"Antamina BHP-share conversion total ounces changed: {screen_id}")
        if not math.isclose(float(row["mechanical_bhp_share_moz"]), bhp_moz, abs_tol=0.000001):
            fail(f"Antamina BHP-share conversion BHP ounces changed: {screen_id}")
        if not math.isclose(float(row["payable_sensitivity_moz"]), payable_moz, abs_tol=0.000001):
            fail(f"Antamina BHP-share conversion payable sensitivity changed: {screen_id}")
    direct = next(row for row in rows if row["screen_id"] == "BSC-003")
    if direct["period"] != "2025" or direct["operator_silver_mt"] or direct["operator_silver_moz"] or direct["mechanical_bhp_share_moz"] != "5.4":
        fail("Antamina direct BHP-share observation must remain separate from operator conversion")
    profiles = {row["screen_id"]: row for row in rows if row["screen_id"] in {"BSC-004", "BSC-005"}}
    if profiles["BSC-004"]["mechanical_bhp_share_moz"] != "6.0" or profiles["BSC-005"]["mechanical_bhp_share_moz"] != "5.4":
        fail("Wheaton Antamina production profile values changed")
    for row in profiles.values():
        if row["classification"] != "management-production-profile":
            fail(f"Wheaton profile classification changed: {row['screen_id']}")


def verify_no_withdrawn_antamina_q4_claims() -> None:
    """Keep withdrawn double-counted BHP quantities out of active research surfaces."""
    correction_memo = "capital-flow-wheaton-antamina-bhp-q4-production-sales-proxy-upgrade-2026-09-15.md"
    forbidden_markers = ("0.32076M", "0.28765M")
    for path in sorted(PILOT_DIR.rglob("*")):
        if path.name == correction_memo or path.suffix not in {".md", ".csv"}:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        found = [marker for marker in forbidden_markers if marker in content]
        if found:
            fail(
                f"withdrawn Antamina Q4 quantity claim found in active surface "
                f"{path.relative_to(ROOT)}: {', '.join(found)}"
            )


def verify_wheaton_production_receipt_bridge() -> None:
    """Keep Q2 combined economics and accounting-event boundaries reproducible."""
    source = ROOT / "raw/primary-sources/capital-flow/debt-refinancing/wheaton/q2-2026/wpm-20260630-ex99-3-financial-statements.htm"
    if not source.exists():
        fail(f"missing Wheaton Q2 financial statements: {source.relative_to(ROOT)}")
    source_text = source.read_text(encoding="utf-8", errors="ignore").lower()
    for marker in ("precious metal credit sales", "control of the precious metal is transferred", "150,549", "77,323", "122,039", "4,708,329"):
        if marker.lower() not in source_text:
            fail(f"Wheaton Q2 production-receipt source marker missing: {marker}")
    if not WHEATON_PRODUCTION_RECEIPT_BRIDGE.exists():
        fail(f"missing Wheaton production-receipt bridge: {WHEATON_PRODUCTION_RECEIPT_BRIDGE.relative_to(ROOT)}")
    with WHEATON_PRODUCTION_RECEIPT_BRIDGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "bridge_id", "proof_gate", "source_document", "source_route", "period",
            "current_evidence", "value_or_metric", "current_status", "what_it_proves",
            "what_it_does_not_prove", "next_required_source", "upgrade_test",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton production-receipt bridge header mismatch: {reader.fieldnames}")
        rows = list(reader)
    by_id = {row["bridge_id"]: row for row in rows}
    if len(rows) != 12 or not {"CFWAPRB-011", "CFWAPRB-012"}.issubset(by_id):
        fail("Wheaton production-receipt bridge must contain the two Q2 upgrade rows")
    q2 = by_id["CFWAPRB-011"]
    if q2["period"] != "Q2 2026" or q2["current_status"] != "combined-period-economics-visible":
        fail("Wheaton Q2 combined economics status changed")
    for marker in ("150.549M USD", "77.323M USD", "122.039M USD", "4.708329B USD"):
        if marker not in q2["value_or_metric"]:
            fail(f"Wheaton Q2 economics metric missing: {marker}")
    recognition = by_id["CFWAPRB-012"]
    if recognition["current_status"] != "accounting-event-and-settlement-input-visible":
        fail("Wheaton accounting-event boundary status changed")
    if not all(recognition[field].strip() for field in ("what_it_does_not_prove", "next_required_source", "upgrade_test")):
        fail("Wheaton accounting-event boundary must retain its upgrade controls")


def verify_wheaton_post_q2_search_refresh() -> None:
    """Keep the dated public-perimeter negative result and its source routes controlled."""
    if not WHEATON_POST_Q2_SEARCH_REFRESH.exists():
        fail(f"missing Wheaton post-Q2 search refresh: {WHEATON_POST_Q2_SEARCH_REFRESH.relative_to(ROOT)}")
    with WHEATON_POST_Q2_SEARCH_REFRESH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "refresh_id", "source", "source_url", "period", "fields_searched",
            "result_class", "what_is_proven", "what_is_not_proven", "next_required_source",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton post-Q2 search refresh header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 5 or {row["refresh_id"] for row in rows} != {"WPM-PQ2-001", "WPM-PQ2-002", "WPM-PQ2-003", "WPM-PQ2-004", "WPM-PQ2-005"}:
        fail("Wheaton post-Q2 search refresh row set changed")
    for row in rows:
        if row["result_class"] != "searched-negative":
            fail(f"Wheaton post-Q2 search result classification changed: {row['refresh_id']}")
        if not row["source_url"].startswith("https://") or not row["fields_searched"].strip() or not row["what_is_not_proven"].strip():
            fail(f"Wheaton post-Q2 search boundary is incomplete: {row['refresh_id']}")
    memo = " ".join((PILOT_DIR / "capital-flow-wheaton-antamina-post-q2-public-search-refresh-2026-09-16.md").read_text(encoding="utf-8").split())
    for marker in ("searched-negative", "official routes continue", "private", "BHP-only credited ounce quantity", "live [Wheaton"):
        if marker not in memo:
            fail(f"Wheaton post-Q2 search memo marker missing: {marker}")


def verify_active_packet_coverage() -> None:
    if not ACTIVE_PACKET_COVERAGE.exists():
        fail(f"missing {ACTIVE_PACKET_COVERAGE.relative_to(ROOT)}")
    with ACTIVE_PACKET_COVERAGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "company_or_entity", "packet_exists", "source_ledger_exists", "deep_dossier_exists",
            "annual_filing_present", "three_quarter_window_present", "results_ir_route_present",
            "call_transcript_status", "current_pilot_evidence", "status", "remaining_gap",
        ]
        if reader.fieldnames != expected_header:
            fail(f"active packet coverage header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("active-pilot-packet-with-call-route", PILOT_DIR / "../deep-company-pages/the-tjx-companies-inc.md", ROOT / "extracted/services/apparel-stores/tjx-companies-inc/company-packet.md", ROOT / "extracted/services/apparel-stores/tjx-companies-inc/source-ledger.md"),
        "Target": ("active-pilot-packet-current-filing-added", PILOT_DIR / "../deep-company-pages/target-corporation.md", ROOT / "extracted/services/discount-variety-stores/target-corp/company-packet.md", ROOT / "extracted/services/discount-variety-stores/target-corp/source-ledger.md"),
        "Walmart": ("active-pilot-packet-with-call-route", PILOT_DIR / "../deep-company-pages/walmart-inc.md", ROOT / "extracted/services/discount-variety-stores/walmart-inc/company-packet.md", ROOT / "extracted/services/discount-variety-stores/walmart-inc/source-ledger.md"),
        "Wheaton": ("active-capital-flow-packet-with-receipt-gap", PILOT_DIR / "../deep-company-pages/wheaton-precious-metals-corporation.md", ROOT / "extracted/basic-materials/gold/wheaton-precious-metals-corp/company-packet.md", ROOT / "extracted/basic-materials/gold/wheaton-precious-metals-corp/source-ledger.md"),
        "Apollo": ("active-capital-flow-packet-with-entity-gap", PILOT_DIR / "../deep-company-pages/apollo-global-management-inc.md", ROOT / "extracted/financial/asset-management/apollo-global-management-inc/company-packet.md", ROOT / "extracted/financial/asset-management/apollo-global-management-inc/source-ledger.md"),
        "Athene legal entity": ("legal-entity-subpacket", PILOT_DIR / "capital-flow-apollo-athene-statutory-cash-return-upgrade-2026-09-15.md", None, None),
    }
    if len(rows) != len(expected) or {row["company_or_entity"] for row in rows} != set(expected):
        fail("active packet coverage rows changed unexpectedly")
    for row in rows:
        status, dossier, packet, ledger = expected[row["company_or_entity"]]
        if row["status"] != status:
            fail(f"active packet coverage status changed: {row['company_or_entity']}")
        if row["remaining_gap"].strip() == "":
            fail(f"active packet coverage gap missing: {row['company_or_entity']}")
        if not dossier.exists():
            fail(f"active packet coverage dossier missing: {dossier}")
        if packet is not None and not packet.exists():
            fail(f"active packet coverage packet missing: {packet}")
        if ledger is not None and not ledger.exists():
            fail(f"active packet coverage ledger missing: {ledger}")


def verify_walmart_call_upgrade() -> None:
    if not WALMART_CALL_UPGRADE.exists():
        fail(f"missing {WALMART_CALL_UPGRADE.relative_to(ROOT)}")
    expected_header = [
        "claim_id", "source_period", "topic", "value", "evidence_grade",
        "what_is_proven", "what_is_not_proven", "source_artifact", "next_test",
    ]
    with WALMART_CALL_UPGRADE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Walmart call-upgrade header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {f"WMT-CALL-{index:03d}" for index in range(1, 6)}
    if len(rows) != 5 or {row["claim_id"] for row in rows} != expected_ids:
        fail("Walmart call-upgrade claims changed unexpectedly")
    expected_grades = {
        "WMT-CALL-001": "management-observation",
        "WMT-CALL-002": "filed-and-management-correlated",
        "WMT-CALL-003": "qualified-mechanism",
        "WMT-CALL-004": "filed-and-management-correlated",
        "WMT-CALL-005": "owner-cash-boundary-held",
    }
    for row in rows:
        if row["evidence_grade"] != expected_grades[row["claim_id"]]:
            fail(f"Walmart call-upgrade evidence grade changed: {row['claim_id']}")
        for field in ("what_is_proven", "what_is_not_proven", "next_test"):
            if not row[field].strip():
                fail(f"Walmart call-upgrade row missing {field}: {row['claim_id']}")
        if not resolve_source(WALMART_CALL_UPGRADE, row["source_artifact"]).exists():
            fail(f"Walmart call-upgrade source missing: {row['source_artifact']}")


def verify_target_call_upgrade() -> None:
    if not TARGET_CALL_UPGRADE.exists():
        fail(f"missing {TARGET_CALL_UPGRADE.relative_to(ROOT)}")
    expected_header = [
        "claim_id", "source_period", "topic", "value", "evidence_grade",
        "what_is_proven", "what_is_not_proven", "source_artifact", "next_test",
    ]
    with TARGET_CALL_UPGRADE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Target call-upgrade header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {f"TGT-CALL-{index:03d}" for index in range(1, 6)}
    if len(rows) != 5 or {row["claim_id"] for row in rows} != expected_ids:
        fail("Target call-upgrade claims changed unexpectedly")
    expected_grades = {
        "TGT-CALL-001": "management-and-release-correlated",
        "TGT-CALL-002": "management-and-release-correlated",
        "TGT-CALL-003": "management-and-release-correlated",
        "TGT-CALL-004": "filed-primary",
        "TGT-CALL-005": "management-observation",
    }
    for row in rows:
        if row["evidence_grade"] != expected_grades[row["claim_id"]]:
            fail(f"Target call-upgrade evidence grade changed: {row['claim_id']}")
        for field in ("what_is_proven", "what_is_not_proven", "next_test"):
            if not row[field].strip():
                fail(f"Target call-upgrade row missing {field}: {row['claim_id']}")
        if not resolve_source(TARGET_CALL_UPGRADE, row["source_artifact"]).exists():
            fail(f"Target call-upgrade source missing: {row['source_artifact']}")


def resolve_source(ledger: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute():
        return path
    if raw.startswith("analysis/"):
        return ROOT / path
    if raw.startswith("../"):
        return PILOT_DIR / path
    return ledger.parent / path


def require_source_links(ledger: Path, rows: list[dict[str, str]]) -> None:
    for row_number, row in enumerate(rows, start=2):
        source = row["source_artifact"].strip()
        if not source:
            fail(f"{ledger.name} row {row_number} has no source artifact")
        resolved = resolve_source(ledger, source)
        if not resolved.exists():
            fail(f"{ledger.name} row {row_number} source missing: {source}")
        for field in ("gate_id", "stage", "question", "entity_or_metric", "current_status", "missing_upgrade"):
            if not row[field].strip():
                fail(f"{ledger.name} row {row_number} has empty {field}")


def verify_ledgers() -> int:
    total = 0
    seen_ids: set[str] = set()
    for ledger in PILOT_LEDGERS:
        if not ledger.exists():
            fail(f"missing {ledger.relative_to(ROOT)}")
        with ledger.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != LEDGER_HEADER:
                fail(f"{ledger.name} header mismatch: {reader.fieldnames}")
            rows = list(reader)
        if not rows:
            fail(f"{ledger.name} has no rows")
        require_source_links(ledger, rows)
        for row in rows:
            if row["gate_id"] in seen_ids:
                fail(f"duplicate gate id across pilot ledgers: {row['gate_id']}")
            seen_ids.add(row["gate_id"])
        total += len(rows)
    return total


def verify_reader_gate_count(total: int) -> None:
    if not READER_JS.exists():
        fail(f"missing {READER_JS.relative_to(ROOT)}")
    text = READER_JS.read_text(encoding="utf-8")
    marker = f"<strong>{total} checked evidence gates</strong>"
    if marker not in text:
        fail(f"reader gate-count marker is stale or missing: expected {total}")


def verify_market_snapshot_2026_09_16() -> None:
    if not MARKET_SNAPSHOT_2026_09_16.exists():
        fail(f"missing market snapshot: {MARKET_SNAPSHOT_2026_09_16.relative_to(ROOT)}")
    with MARKET_SNAPSHOT_2026_09_16.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "ticker", "company", "price_usd", "market_cap_musd",
            "observation_date", "source_route", "interpretation",
        ]
        if reader.fieldnames != expected_header:
            fail(f"market snapshot header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": (124.600, 139178.200),
        "TGT": (154.400, 70499.040),
        "WMT": (108.090, 862342.020),
        "APO": (127.000, 77498.166),
        "WPM": (150.020, 68006.478),
    }
    if {row["ticker"] for row in rows} != set(expected) or len(rows) != len(expected):
        fail("market snapshot ticker set changed unexpectedly")
    for row in rows:
        ticker = row["ticker"]
        price, market_cap = expected[ticker]
        expected_route = {
            "TJX": "https://www.nasdaq.com/market-activity/stocks/tjx",
            "TGT": "https://www.nasdaq.com/market-activity/stocks/tgt",
            "WMT": "https://www.nasdaq.com/market-activity/stocks/wmt",
            "APO": "https://www.nasdaq.com/market-activity/stocks/apo",
            "WPM": "https://www.nasdaq.com/market-activity/stocks/wpm",
        }[ticker]
        if row["observation_date"] != "2026-09-16" or "finance-quote-capture" not in row["source_route"] or expected_route not in row["source_route"]:
            fail(f"market snapshot metadata changed: {ticker}")
        if not math.isclose(float(row["price_usd"]), price, rel_tol=0, abs_tol=0.001):
            fail(f"market snapshot price changed: {ticker}")
        if not math.isclose(float(row["market_cap_musd"]), market_cap, rel_tol=0, abs_tol=0.001):
            fail(f"market snapshot market cap changed: {ticker}")
        if not row["interpretation"].strip():
            fail(f"market snapshot interpretation missing: {ticker}")


def verify_market_snapshot_2026_09_17() -> None:
    if not MARKET_SNAPSHOT_2026_09_17.exists():
        fail(f"missing market snapshot: {MARKET_SNAPSHOT_2026_09_17.relative_to(ROOT)}")
    with MARKET_SNAPSHOT_2026_09_17.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "ticker", "company", "observation_date", "price_usd",
            "market_cap_musd", "source_route",
        ]
        if reader.fieldnames != expected_header:
            fail(f"2026-09-17 market snapshot header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": (122.84, 137212.280),
        "TGT": (154.68, 70626.888),
        "WMT": (107.50, 857635.000),
        "APO": (124.53, 75990.918),
        "WPM": (146.73, 66515.068),
    }
    if {row["ticker"] for row in rows} != set(expected) or len(rows) != len(expected):
        fail("2026-09-17 market snapshot ticker set changed unexpectedly")
    for row in rows:
        ticker = row["ticker"]
        price, market_cap = expected[ticker]
        if row["observation_date"] != "2026-09-17" or row["source_route"] != f"nasdaq-{ticker.lower()}":
            fail(f"2026-09-17 market snapshot metadata changed: {ticker}")
        if not math.isclose(float(row["price_usd"]), price, rel_tol=0, abs_tol=0.001):
            fail(f"2026-09-17 market snapshot price changed: {ticker}")
        if not math.isclose(float(row["market_cap_musd"]), market_cap, rel_tol=0, abs_tol=0.001):
            fail(f"2026-09-17 market snapshot market cap changed: {ticker}")


def number(row: dict[str, str], field: str) -> float:
    raw = row[field].strip()
    try:
        value = float(raw)
    except ValueError as exc:
        fail(f"{row.get('company', '<unknown>')} has invalid {field}: {exc}")
    if not math.isfinite(value):
        fail(f"{row.get('company', '<unknown>')} has non-finite {field}")
    return value


def scenario_irr(flows: list[float]) -> float:
    low, high = -0.999, 10.0
    low_value = sum(value / (1 + low) ** period for period, value in enumerate(flows))
    high_value = sum(value / (1 + high) ** period for period, value in enumerate(flows))
    if low_value * high_value > 0:
        fail("Antamina scenario cash flows do not bracket an IRR")
    for _ in range(200):
        rate = (low + high) / 2
        value = sum(cash / (1 + rate) ** period for period, cash in enumerate(flows))
        if value * low_value > 0:
            low = rate
            low_value = value
        else:
            high = rate
    return (low + high) / 2 * 100


def verify_workbench() -> None:
    if not WORKBENCH.exists():
        fail(f"missing {WORKBENCH.relative_to(ROOT)}")
    with WORKBENCH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != WORKBENCH_HEADER:
            fail(f"valuation workbench header mismatch: {reader.fieldnames}")
        rows = list(reader)
    by_company = {row["company"]: row for row in rows}
    if set(by_company) != {"TJX", "Target", "Walmart"}:
        fail(f"valuation workbench companies are {sorted(by_company)}")

    tjx = by_company["TJX"]
    if tjx["valuation_status"] != "not-comparable":
        fail("TJX must remain explicitly not-comparable until its cash bridge is complete")
    if any(tjx[field].strip() for field in ("bear_cash_musd", "base_cash_musd", "bull_cash_musd", "market_snapshot_musd")):
        fail("TJX has valuation numbers despite its not-comparable status")

    for company in ("Target", "Walmart"):
        row = by_company[company]
        cash = [number(row, field) for field in ("bear_cash_musd", "base_cash_musd", "bull_cash_musd")]
        multiples = [number(row, field) for field in ("bear_multiple", "base_multiple", "bull_multiple")]
        implied = [number(row, field) for field in ("bear_value_musd", "base_value_musd", "bull_value_musd")]
        if not (0 <= cash[0] <= cash[1] <= cash[2]):
            fail(f"{company} cash cases are not ordered")
        if not (0 < multiples[0] <= multiples[1] <= multiples[2]):
            fail(f"{company} multiples are not ordered")
        for actual, expected in zip(implied, (cash[i] * multiples[i] for i in range(3))):
            if not math.isclose(actual, expected, rel_tol=0, abs_tol=1.1):
                fail(f"{company} implied value {actual} does not equal cash × multiple {expected}")
        market = number(row, "market_snapshot_musd")
        expected_gap = (implied[1] / market - 1) * 100
        if not math.isclose(number(row, "base_gap_percent"), expected_gap, abs_tol=0.2):
            fail(f"{company} base gap does not match base value and market snapshot")


def verify_antamina_workbench() -> None:
    if not ANTAMINA_WORKBENCH.exists():
        fail(f"missing {ANTAMINA_WORKBENCH.relative_to(ROOT)}")
    with ANTAMINA_WORKBENCH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ANTAMINA_HEADER:
            fail(f"Antamina workbench header mismatch: {reader.fieldnames}")
        rows = list(reader)
    by_scenario = {row["scenario"]: row for row in rows}
    if set(by_scenario) != {"bear", "base", "bull"}:
        fail(f"Antamina scenarios are {sorted(by_scenario)}")
    for scenario, row in by_scenario.items():
        if row["valuation_status"] != "illustrative-screen":
            fail(f"{scenario} Antamina case must remain illustrative-screen")
        for field in (
            "upfront_payment_musd", "annual_bhp_share_production_moz",
            "payable_factor_pct", "spot_price_usd_oz", "stream_payment_pct",
            "burden_haircut_pct", "modeled_years", "initial_share_years",
            "life_of_mine_share_years", "discount_rate_pct",
            "annual_initial_cash_musd", "annual_life_of_mine_cash_musd",
            "npv_musd", "irr_pct",
        ):
            number(row, field)
        if row["upfront_payment_musd"] != "4300":
            fail(f"{scenario} Antamina upfront payment must remain 4300 MUSD")
        if int(float(row["initial_share_years"])) + int(float(row["life_of_mine_share_years"])) != int(float(row["modeled_years"])):
            fail(f"{scenario} Antamina modeled years do not reconcile")
        expected_initial = (
            float(row["annual_bhp_share_production_moz"])
            * float(row["payable_factor_pct"]) / 100
            * float(row["spot_price_usd_oz"])
            * (1 - float(row["stream_payment_pct"]) / 100)
            * (1 - float(row["burden_haircut_pct"]) / 100)
        )
        if not math.isclose(float(row["annual_initial_cash_musd"]), expected_initial, abs_tol=0.01):
            fail(f"{scenario} Antamina initial cash does not reconcile")
        expected_lom = expected_initial * float(row["life_of_mine_stream_share_pct"]) / float(row["initial_stream_share_pct"])
        if not math.isclose(float(row["annual_life_of_mine_cash_musd"]), expected_lom, abs_tol=0.01):
            fail(f"{scenario} Antamina life-of-mine cash does not reconcile")
        initial_years = int(float(row["initial_share_years"]))
        life_years = int(float(row["life_of_mine_share_years"]))
        flows = [-float(row["upfront_payment_musd"])] + [expected_initial] * initial_years + [expected_lom] * life_years
        discount = float(row["discount_rate_pct"]) / 100
        expected_npv = sum(cash / (1 + discount) ** period for period, cash in enumerate(flows))
        expected_irr = scenario_irr(flows)
        if not math.isclose(float(row["npv_musd"]), expected_npv, abs_tol=0.02):
            fail(f"{scenario} Antamina NPV does not reconcile")
        if not math.isclose(float(row["irr_pct"]), expected_irr, abs_tol=0.02):
            fail(f"{scenario} Antamina IRR does not reconcile")


def verify_apollo_workbench() -> None:
    if not APOLLO_WORKBENCH.exists():
        fail(f"missing {APOLLO_WORKBENCH.relative_to(ROOT)}")
    with APOLLO_WORKBENCH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != APOLLO_HEADER:
            fail(f"Apollo workbench header mismatch: {reader.fieldnames}")
        rows = list(reader)
    by_case = {row["case"]: row for row in rows}
    if set(by_case) != {"bear", "base", "bull"}:
        fail(f"Apollo cases are {sorted(by_case)}")
    for case, row in by_case.items():
        if row["valuation_status"] != "illustrative-sotp":
            fail(f"{case} Apollo case must remain illustrative-sotp")
        fields = (
            "normalized_fre_busd", "fre_multiple", "normalized_sre_busd",
            "sre_multiple", "principal_performance_value_busd",
            "common_claims_capital_haircut_busd", "fre_value_busd",
            "sre_value_busd", "illustrative_equity_value_busd",
            "market_snapshot_busd", "gap_to_market_pct",
        )
        for field in fields:
            number(row, field)
        fre_value = float(row["normalized_fre_busd"]) * float(row["fre_multiple"])
        sre_value = float(row["normalized_sre_busd"]) * float(row["sre_multiple"])
        equity = fre_value + sre_value + float(row["principal_performance_value_busd"]) + float(row["common_claims_capital_haircut_busd"])
        if not math.isclose(float(row["fre_value_busd"]), fre_value, abs_tol=0.01):
            fail(f"{case} Apollo FRE value does not reconcile")
        if not math.isclose(float(row["sre_value_busd"]), sre_value, abs_tol=0.01):
            fail(f"{case} Apollo SRE value does not reconcile")
        if not math.isclose(float(row["illustrative_equity_value_busd"]), equity, abs_tol=0.01):
            fail(f"{case} Apollo equity value does not reconcile")
        expected_gap = (equity / float(row["market_snapshot_busd"]) - 1) * 100
        if not math.isclose(float(row["gap_to_market_pct"]), expected_gap, abs_tol=0.1):
            fail(f"{case} Apollo market gap does not reconcile")


def verify_apollo_primary_source_upgrade() -> None:
    ledger = LEDGER_DIR / "combined-investment-research-pilot-03-apollo-athene.csv"
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = {row["gate_id"]: row for row in csv.DictReader(handle)}
    expected = {
        "APO-016": ("21006000000 USD", "primary-source-confirmed"),
        "APO-017": ("20476000000 USD", "primary-source-confirmed"),
        "APO-018": ("1398000000 USD", "primary-source-confirmed"),
        "APO-019": ("452566000000 USD", "primary-source-confirmed"),
        "APO-020": ("4501000000 USD six months", "primary-source-confirmed"),
        "APO-021": ("478000000 USD six months plus 1100000000 USD unrecognized RSU cost", "primary-source-confirmed"),
        "APO-022": ("2000000000 USD net funded commitments financed through revolver and asset-based financing; no Apollo capital funded under commitment", "primary-source-confirmed"),
        "APO-023": ("No amounts outstanding; covenants satisfied", "primary-source-confirmed"),
        "APO-024": ("70616000000 USD or 15.0 percent of total assets", "primary-source-confirmed"),
        "APO-025": ("17931000000 USD in Apollo funds; 13070000000 USD in asset-origination platforms; 4206000000 USD in retirement-services platforms", "primary-source-confirmed"),
        "APO-026": ("3191000000 USD investment and 134000000 USD additional commitment", "primary-source-confirmed"),
        "APO-027": ("785000000 USD including base sub-allocation and performance fees", "primary-source-confirmed"),
        "APO-028": ("1.41 percent versus 1.62 percent prior year", "primary-source-confirmed"),
        "APO-029": ("7800000000 USD net investment earnings and 5700000000 USD cost of funds", "primary-source-confirmed"),
        "APO-030": ("Approximately negative 1000000000 USD", "primary-source-confirmed"),
        "APO-031": ("Underlying asset impairment reduced Atlas valuation in 2026", "primary-source-confirmed"),
    }
    for gate_id, (value, status) in expected.items():
        if gate_id not in rows:
            fail(f"missing Apollo primary-source gate {gate_id}")
        if rows[gate_id]["evidence_value"] != value or rows[gate_id]["current_status"] != status:
            fail(f"Apollo primary-source gate {gate_id} changed unexpectedly")
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = {row["gate_id"]: row for row in csv.DictReader(handle)}
    if rows.get("APO-045", {}).get("evidence_value") != "269.806570M USD interpreted consideration and 4.029889M USD interpreted interest/dividends across two rows; gain or loss remains blank hold":
        fail("Apollo statutory cash-like gate APO-045 changed unexpectedly")
    if rows.get("APO-045", {}).get("current_status") != "statutory-row-fields-confirmed":
        fail("Apollo statutory cash-like gate APO-045 status changed unexpectedly")
    if rows.get("APO-046", {}).get("evidence_value") != "Athene 375M USD common dividends 71M USD preferred dividends 301M USD NCI distributions and 42M USD parent contribution; Apollo 654M USD common dividends 729M USD repurchases and 49M USD preferred dividends; no Apollo-specific upstream receipt joined":
        fail("Apollo upstream dividend boundary gate APO-046 changed unexpectedly")
    if rows.get("APO-046", {}).get("current_status") != "entity-dividend-boundary-confirmed":
        fail("Apollo upstream dividend boundary gate APO-046 status changed unexpectedly")
    if rows.get("APO-047", {}).get("evidence_value") != "12.732699320B USD net investment income; 12.281980822B USD cash-flow net investment income; 13.601183683B USD collected gross investment income; 8.127852536B USD page-18 collected bond income reconstructed from Schedule D Parts 1/4/5 within $2; 6.230478121B USD corrected Schedule D interest received; 54.035221430B USD bond sale maturity or repayment proceeds; 158.619095705B USD parsed Schedule D bond base; 5.890696798B USD contract/deposit liability burden; 6.842002522B USD bounded residual after that burden; 2.482135218B USD gross derivative assets; 52 named Part C CUSIP controls":
        fail("Apollo legal-entity income/cash gate APO-047 changed unexpectedly")
    if rows.get("APO-047", {}).get("current_status") != "legal-entity-income-cash-bridge-visible":
        fail("Apollo legal-entity income/cash gate APO-047 status changed unexpectedly")
    if rows.get("APO-048", {}).get("evidence_value") != "Completed April 24 2026 cash sale to Athene based on 99.7 percent of loan commitments subject to adjustments; approximately 2.2B USD post-sale total assets primarily cash after debt and expenses; approximately 1.4B USD expected net cash and 1.7B USD common equity in proxy":
        fail("Apollo ARI sale cash-use gate APO-048 changed unexpectedly")
    if rows.get("APO-048", {}).get("current_status") != "completed-related-party-sale-and-seller-cash-use-visible":
        fail("Apollo ARI sale cash-use gate APO-048 status changed unexpectedly")
    if rows.get("APO-049", {}).get("evidence_value") != "Proxy representations cover no unapproved collateral release; no cross-default or cross-collateralization; seller ownership free of liens other than permitted liens; and schedules for principal balances unfunded advances and reserve deposits":
        fail("Apollo ARI collateral boundary gate APO-049 changed unexpectedly")
    if rows.get("APO-049", {}).get("current_status") != "collateral-control-boundary-visible":
        fail("Apollo ARI collateral boundary gate APO-049 status changed unexpectedly")


def verify_wheaton_settlement_boundary_upgrade() -> None:
    ledger = LEDGER_DIR / "combined-investment-research-pilot-01-wheaton-antamina.csv"
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = {row["gate_id"]: row for row in csv.DictReader(handle)}
    expected = {
        "WPM-024": ("Purchase and delivery of metal credits to Wheaton; no physical delivery of silver", "primary-source-confirmed"),
        "WPM-025": ("No minimum or fixed delivery requirements under the agreement", "primary-source-confirmed"),
        "WPM-026": ("4273M USD at June 30 2026; upfront payment was 4300M USD", "primary-source-confirmed"),
        "WPM-027": ("4300M USD proceeds and 41M USD settlements of streaming arrangement liability; no ounce or invoice allocation", "settlement-amount-visible"),
        "WPM-028": ("Risked reserves and resources used in estimate and do not currently meet proved criteria", "primary-source-confirmed"),
        "WPM-029": ("Wheaton received first BHP-PMPA deliveries in Q2 2026; combined Antamina silver was 2.319M ounces produced and 2.063M sold", "first-delivery-confirmed"),
        "WPM-030": ("33.75 percent of payable silver until 100 million ounces delivered then 22.5 percent for life of mine; 90.0 percent payable factor and 20.0 percent spot-price payment", "contract-denominator-confirmed"),
        "WPM-031": ("Approximately 6.0M ounces per year BHP incremental first five years and 5.4M first ten years; combined Antamina approximately 12.0M first five years and 10.8M first ten years; declared reserves support mining through approximately 2036", "production-profile-proxy-confirmed"),
        "WPM-032": ("837000 silver-ounce-equivalent GEO increase in Q2 and 1341000 in H1 primarily driven by BHP PMPA; Q2 operating table reports 2319000 attributable silver ounces produced and 2063000 sold", "incremental-production-proxy-confirmed"),
        "WPM-033": ("Antamina OCF proxy 222.223M USD H1; finance costs 32.502M USD H1; income-tax expense 210.876M USD H1; cash 100.192M USD; gross bank debt 1.972B USD including 1.500B USD term loan and 472M USD revolver", "company-burden-context-confirmed"),
        "WPM-034": ("1.500B USD term loan with two-year maturity and no-penalty repayment; RCF 2.500B USD through June 30 2031 plus 500M USD accordion; RCF pricing SOFR plus 1.10% to 2.15%; standby fee 0.1966%; capitalization covenant <= 0.60:1; Bank of Montreal administrative agent; 472M USD reported RCF balance implies 5.192M to 10.148M USD annual spread-only burden before SOFR and fees; credit agreement requires all term-facility proceeds to partially finance the Antamina Mine Silver Stream Acquisition", "financing-terms-boundary-confirmed"),
        "WPM-035": ("Q4 FY2026 (April-June 2026) BHP-interest payable silver produced 1.056M ounces and sold 0.947M ounces; mechanical 90% contract-factor equivalents 0.9504M and 0.8523M ounces; no additional 33.75% multiplication is applied because the BHP table is already reported at BHP interest; compared with Wheaton's same-period combined 2.319M produced and 2.063M sold, the arithmetic differences are 1.3686M and 1.2107M", "counterparty-side-production-sales-proxy"),
        "WPM-048": ("Q2 2026 Wheaton 6-K exhibits and BHP FY2026 Antamina materials searched for invoice settlement metal credit receipt delivered delivery Antamina and PMPA terms; aggregate 41M USD streaming-liability settlements and combined/proxy rows found, but no BHP-only invoice settlement or receipt ledger", "source-search-boundary-confirmed"),
        "WPM-054": ("BHP PMPA: 33.75% until 100 Moz then 22.5% LOM; legacy Glencore PMPA: 33.75% until 140 Moz then 22.5% LOM; Investor Day pages 37, 41, and 47 separately identify the BHP/Glencore routes and show the combined Antamina reserve denominator", "dual-threshold-distinction-confirmed"),
        "WPM-055": ("67.50% attributable interest; $5.200B upfront consideration paid to June 30 2026; 56.718M silver ounces received and sold to date; $1.171862B cash flow generated to date; 1.412M Q2 PBND ounces", "combined-stream-cumulative-cash-back-proxy-confirmed"),
        "WPM-056": ("5.588M ounces of payable silver in concentrate for BHP's 33.75% Antamina interest", "counterparty-annual-production-denominator-confirmed"),
    }
    for gate_id, (value, status) in expected.items():
        if gate_id not in rows:
            fail(f"missing Wheaton settlement-boundary gate {gate_id}")
        if rows[gate_id]["evidence_value"] != value or rows[gate_id]["current_status"] != status:
            fail(f"Wheaton settlement-boundary gate {gate_id} changed unexpectedly")
    structured = LEDGER_DIR / "capital-flow-wheaton-antamina-dual-pmpa-threshold-reconciliation-2026-09-16.csv"
    with structured.open(newline="", encoding="utf-8") as handle:
        structured_rows = {row["gate_id"]: row for row in csv.DictReader(handle)}
    if structured_rows.get("WPM-054", {}).get("evidence_value") != expected["WPM-054"][0]:
        fail("Wheaton WPM-054 structured evidence value is out of sync with the pilot ledger")
    if structured_rows.get("WPM-054", {}).get("current_status") != expected["WPM-054"][1]:
        fail("Wheaton WPM-054 structured status is out of sync with the pilot ledger")
    with WHEATON_Q03_METAL_CREDIT_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        q03_rows = {row["boundary_id"]: row for row in csv.DictReader(handle)}
    q03_row = q03_rows.get("Q03-MCR-011")
    if q03_row is None:
        fail("Wheaton Q-03 exact financing-cash-flow boundary row is missing")
    if q03_row["status"] != "observed" or "$4.300B" not in q03_row["observed_fact"] or "$41M" not in q03_row["observed_fact"] or "$(3.280B)" not in q03_row["observed_fact"]:
        fail("Wheaton Q-03 exact financing-cash-flow boundary changed unexpectedly")
    q03_boundary = q03_row["does_not_prove"].lower()
    if "bank receipt timing" not in q03_boundary or "recurring bhp-pmpa" not in q03_boundary:
        fail("Wheaton Q-03 financing-cash-flow boundary overclaims")
    guarantee_row = q03_rows.get("Q03-MCR-012")
    if guarantee_row is None or guarantee_row["status"] != "observed":
        fail("Wheaton Q-03 counterparty guarantee boundary is missing")
    for marker in ("parent guarantee", "holding-company guarantee", "unlimited"):
        if marker not in guarantee_row["observed_fact"]:
            fail(f"Wheaton Q-03 guarantee marker missing: {marker}")


def verify_wheaton_forward_profile_source_control() -> None:
    with WHEATON_FORWARD_PROFILE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1 or rows[0].get("gate_id") != "WPM-053":
        fail("Wheaton forward-profile artifact must contain exactly WPM-053")
    row = rows[0]
    if row.get("primary_source_url") != WHEATON_FORWARD_PROFILE_URL:
        fail("Wheaton forward-profile primary source URL changed unexpectedly")
    if row.get("current_status") != "forward-profile-confirmed":
        fail("Wheaton forward-profile status changed unexpectedly")
    if "reserve-backed annual delivery curve" not in row.get("missing_upgrade", ""):
        fail("Wheaton forward-profile reserve boundary disappeared")


def verify_wheaton_teck_reserve_cross_check() -> None:
    expected_header = [
        "cross_check_id", "queue_id", "source_route", "period", "observed_value",
        "ownership_or_scope", "what_is_proven", "missing_upgrade", "result_class",
        "primary_source_url", "source_artifact", "local_source_artifact",
    ]
    with WHEATON_TECK_RESERVE_CROSS_CHECK.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Wheaton Teck reserve cross-check header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row.get("cross_check_id") for row in rows] != ["TRC-001", "TRC-002", "TRC-003", "TRC-004", "TRC-005", "TRC-006", "TRC-007", "TRC-008"]:
        fail("Wheaton Teck reserve cross-check rows changed unexpectedly")
    for row in rows:
        if row["result_class"] != "evidence-insufficient":
            fail(f"Wheaton Teck reserve cross-check over-promoted: {row['cross_check_id']}")
        if row["cross_check_id"] not in {"TRC-006", "TRC-007", "TRC-008"} and row["queue_id"] != "Q-02":
            fail(f"Wheaton Teck reserve cross-check queue changed: {row['cross_check_id']}")
        if row["cross_check_id"] in {"TRC-006", "TRC-007"} and row["queue_id"] != "CA-06":
            fail(f"Wheaton Teck burden row must remain on the CA-06 denominator surface: {row['cross_check_id']}")
        if row["cross_check_id"] == "TRC-008" and row["queue_id"] != "Q-02":
            fail("Wheaton Teck scale sensitivity must remain on the Q-02 reserve surface")
        if row["primary_source_url"] not in {
            "https://www.sec.gov/Archives/edgar/data/886986/000088698626000004/teck-20251231xexx991aif.htm",
            "https://minedocs.com/28/Antamina-TR-12312024.pdf",
        }:
            fail(f"Wheaton Teck reserve source changed: {row['cross_check_id']}")
        if "BHP" not in row["missing_upgrade"] or not row["source_artifact"].strip():
            fail(f"Wheaton Teck reserve cross-check boundary incomplete: {row['cross_check_id']}")
        local_source = ROOT / row["local_source_artifact"]
        if not local_source.exists():
            fail(f"Wheaton Teck local source artifact missing: {row['cross_check_id']}")
        expected_local = (
            "raw/primary-sources/capital-flow/antamina/2025/antamina-technical-report-2024.pdf"
            if row["primary_source_url"].endswith("Antamina-TR-12312024.pdf")
            else "raw/primary-sources/capital-flow/teck/2025/teck-2025-aif.htm"
        )
        if row["local_source_artifact"] != expected_local:
            fail(f"Wheaton Teck local source route changed: {row['cross_check_id']}")


def verify_wheaton_credit_agreement_boundary() -> None:
    expected_header = [
        "boundary_id", "queue_id", "source_route", "period", "observed_value",
        "what_is_proven", "missing_upgrade", "result_class", "primary_source_url",
        "source_artifact", "local_source_artifact",
    ]
    with WHEATON_CREDIT_AGREEMENT_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Wheaton credit-agreement boundary header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row.get("boundary_id") for row in rows] != [
        "Q03-CAB-001", "Q03-CAB-002", "Q03-CAB-003", "Q03-CAB-004", "Q03-CAB-005", "Q03-CAB-006",
    ]:
        fail("Wheaton credit-agreement boundary rows changed unexpectedly")
    agreement_url = "https://www.sec.gov/Archives/edgar/data/1323404/000106299326001700/exhibit99-2.htm"
    q2_statements_url = "https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex993.htm"
    for row in rows:
        if row["queue_id"] != "Q-03" or row["result_class"] != "evidence-insufficient":
            fail(f"Wheaton credit-agreement boundary over-promoted: {row['boundary_id']}")
        expected_url = q2_statements_url if row["boundary_id"] == "Q03-CAB-006" else agreement_url
        if row["primary_source_url"] != expected_url or not row["source_artifact"].strip():
            fail(f"Wheaton credit-agreement boundary source incomplete: {row['boundary_id']}")
        if not row["missing_upgrade"].strip():
            fail(f"Wheaton credit-agreement missing upgrade absent: {row['boundary_id']}")
        local_source = ROOT / row["local_source_artifact"]
        if not local_source.exists():
            fail(f"Wheaton credit-agreement local source missing: {row['boundary_id']}")
    single_draw = rows[-2]
    for marker in ("single closing-date drawdown", "actual single draw", "designated payee"):
        if marker not in single_draw["observed_value"]:
            fail(f"Wheaton single-draw control marker missing: {marker}")
    executed_borrowing = rows[-1]
    for marker in ("drew", "$1.500B", "April 1, 2026"):
        if marker not in executed_borrowing["observed_value"]:
            fail(f"Wheaton executed-borrowing control marker missing: {marker}")


def verify_wheaton_maturity_cliff() -> None:
    expected_header = [
        "screen_id", "queue_id", "source_route", "period", "observed_value",
        "derived_metric", "what_is_proven", "missing_upgrade", "result_class",
        "primary_source_url", "source_artifact",
    ]
    with WHEATON_MATURITY_CLIFF.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Wheaton maturity-cliff header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row.get("screen_id") for row in rows] != ["Q03-MC-001", "Q03-MC-002"]:
        fail("Wheaton maturity-cliff rows changed unexpectedly")
    agreement_url = "https://www.sec.gov/Archives/edgar/data/1323404/000106299326001700/exhibit99-2.htm"
    statements_url = "https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex993.htm"
    if rows[0]["primary_source_url"] != agreement_url or rows[1]["primary_source_url"] != statements_url:
        fail("Wheaton maturity-cliff source route changed")
    expected_ratio = 1500 / 1972 * 100
    ratio_text = rows[1]["derived_metric"].split("is ", 1)[1].split("%", 1)[0]
    if abs(float(ratio_text) - expected_ratio) > 0.001:
        fail("Wheaton maturity-cliff ratio arithmetic mismatch")
    for row in rows:
        if row["queue_id"] != "Q-03" or row["result_class"] != "evidence-insufficient":
            fail(f"Wheaton maturity-cliff over-promoted: {row['screen_id']}")
        if not row["missing_upgrade"].strip() or not row["source_artifact"].strip():
            fail(f"Wheaton maturity-cliff boundary incomplete: {row['screen_id']}")


def verify_wheaton_maturity_bullet() -> None:
    expected_header = [
        "allocation_rate", "term_principal_musd", "allocated_bullet_musd",
        "annualized_stream_ocf_proxy_musd", "bullet_to_annualized_ocf_multiple",
        "one_period_proxy_after_bullet_musd", "status", "source_artifact",
        "next_upgrade",
    ]
    with WHEATON_MATURITY_BULLET.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Wheaton maturity-bullet header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_rates = [0, 25, 50, 75, 100]
    if len(rows) != len(expected_rates):
        fail("Wheaton maturity-bullet rows changed unexpectedly")
    principal = 1500.0
    stream_ocf = 444.446
    for row, expected_rate in zip(rows, expected_rates):
        rate = float(row["allocation_rate"].rstrip("%"))
        bullet = float(row["allocated_bullet_musd"])
        reported_ocf = float(row["annualized_stream_ocf_proxy_musd"])
        multiple = float(row["bullet_to_annualized_ocf_multiple"])
        residual = float(row["one_period_proxy_after_bullet_musd"])
        expected_bullet = principal * rate / 100
        expected_multiple = expected_bullet / stream_ocf
        expected_residual = stream_ocf - expected_bullet
        if abs(rate - expected_rate) > 0.001:
            fail(f"Wheaton maturity-bullet allocation changed: {row['allocation_rate']}")
        if abs(bullet - expected_bullet) > 0.001 or abs(reported_ocf - stream_ocf) > 0.001:
            fail(f"Wheaton maturity-bullet amount arithmetic mismatch: {row['allocation_rate']}")
        if abs(multiple - expected_multiple) > 0.001 or abs(residual - expected_residual) > 0.001:
            fail(f"Wheaton maturity-bullet coverage arithmetic mismatch: {row['allocation_rate']}")
        if (
            row["status"] != "illustrative-allocation-frontier"
            or not row["source_artifact"].strip()
            or not row["next_upgrade"].strip()
        ):
            fail(f"Wheaton maturity-bullet boundary incomplete: {row['allocation_rate']}")


def verify_wheaton_bhp_source_manifest() -> None:
    expected_header = [
        "source_id", "document_role", "declared_form", "observed_local_form",
        "canonical_source_url", "local_artifact", "local_status", "allowed_use",
        "excluded_use",
    ]
    with WHEATON_BHP_SOURCE_MANIFEST.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Wheaton BHP source-manifest header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row.get("source_id") for row in rows] != ["BHP-FY26-20F", "BHP-FY26-6K"]:
        fail("Wheaton BHP source-manifest rows changed unexpectedly")
    expected = {
        "BHP-FY26-20F": (
            "Form 20-F", "Form 20-F", "local-preserved",
            "https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm",
        ),
        "BHP-FY26-6K": (
            "Form 6-K", "Form 6-K", "local-preserved",
            "https://www.sec.gov/Archives/edgar/data/811809/000119312526355840/d54971d6k.htm",
        ),
    }
    for row in rows:
        declared, observed, status, url = expected[row["source_id"]]
        if (row["declared_form"], row["observed_local_form"], row["local_status"], row["canonical_source_url"]) != (declared, observed, status, url):
            fail(f"Wheaton BHP source-manifest provenance changed: {row['source_id']}")
        if row["local_artifact"] and not (ROOT / row["local_artifact"]).exists():
            fail(f"Wheaton BHP source-manifest local artifact missing: {row['source_id']}")
        if not row["allowed_use"].strip() or not row["excluded_use"].strip():
            fail(f"Wheaton BHP source-manifest boundary incomplete: {row['source_id']}")


def verify_wheaton_bhp_payable_silver() -> None:
    if not WHEATON_BHP_PAYABLE_SILVER.exists():
        fail(f"missing {WHEATON_BHP_PAYABLE_SILVER.relative_to(ROOT)}")
    with WHEATON_BHP_PAYABLE_SILVER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "observation_id", "period", "metric",
            "reported_bhp_interest_payable_silver_moz", "contract_payable_factor_pct",
            "mechanical_contract_factor_screen_moz", "mechanical_gross_equivalent_moz",
            "status", "what_is_proven",
            "what_is_not_proven", "source_artifact", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"BHP payable-silver header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 1 or rows[0]["observation_id"] != "WPM-060":
        fail("BHP payable-silver boundary must contain WPM-060 only")
    row = rows[0]
    if row["period"] != "FY2026" or row["status"] != "bhp-annual-quantity-calibration-confirmed":
        fail("BHP payable-silver boundary status or period changed unexpectedly")
    source = resolve_source(WHEATON_BHP_PAYABLE_SILVER, row["source_artifact"])
    if not source.exists():
        fail(f"BHP payable-silver source missing: {row['source_artifact']}")
    reported = number(row, "reported_bhp_interest_payable_silver_moz")
    factor = number(row, "contract_payable_factor_pct")
    factor_screen = number(row, "mechanical_contract_factor_screen_moz")
    gross = number(row, "mechanical_gross_equivalent_moz")
    if not math.isclose(reported, 5.588, abs_tol=0.000001):
        fail("BHP payable-silver reported quantity changed unexpectedly")
    if not math.isclose(factor, 90.0, abs_tol=0.000001):
        fail("BHP payable-silver contractual factor changed unexpectedly")
    if not math.isclose(factor_screen, round(reported * (factor / 100), 3), abs_tol=0.000001):
        fail("BHP payable-silver factor screen arithmetic does not reconcile")
    if not math.isclose(gross, round(reported / (factor / 100), 3), abs_tol=0.000001):
        fail("BHP payable-silver gross-equivalent arithmetic does not reconcile")
    for field in ("what_is_proven", "what_is_not_proven", "next_upgrade"):
        if not row[field].strip():
            fail(f"BHP payable-silver boundary field missing: {field}")
    if "not PMPA settlement quantities" not in row["what_is_not_proven"]:
        fail("BHP payable-silver boundary must preserve the settlement limitation")


def verify_wheaton_antamina_source_manifest() -> None:
    path = PILOT_DIR / "data" / "capital-flow-wheaton-antamina-source-manifest-2026-09-16.csv"
    if not path.exists():
        fail(f"missing Wheaton–Antamina source manifest: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "source_id", "document_role", "declared_form", "observed_local_form",
            "canonical_source_url", "local_artifact", "local_status", "allowed_use",
            "excluded_use",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton–Antamina source-manifest header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "WAM-SEC-001": ("Form 6-K", "Form 6-K", "https://www.sec.gov/Archives/edgar/data/811809/000119312526052837/d29257d6k.htm", "raw/primary-sources/capital-flow/bhp/fy2026/bhp-antamina-streaming-6k-2026-02-17.htm"),
        "WAM-SEC-002": ("Exhibit 99.1", "Exhibit 99.1", "https://www.sec.gov/Archives/edgar/data/1323404/000127956926000133/ex991.htm", "raw/primary-sources/capital-flow/wheaton/2026-02/wheaton-antamina-acquisition-ex99-1-2026-02-16.htm"),
    }
    if [row["source_id"] for row in rows] != list(expected):
        fail("Wheaton–Antamina source-manifest rows changed unexpectedly")
    for row in rows:
        declared, observed, url, artifact = expected[row["source_id"]]
        if (row["declared_form"], row["observed_local_form"], row["canonical_source_url"], row["local_artifact"]) != (declared, observed, url, artifact):
            fail(f"Wheaton–Antamina source-manifest provenance changed: {row['source_id']}")
        if row["local_status"] != "local-preserved" or not (ROOT / artifact).exists():
            fail(f"Wheaton–Antamina source-manifest artifact missing: {row['source_id']}")
        if not row["allowed_use"].strip() or not row["excluded_use"].strip():
            fail(f"Wheaton–Antamina source-manifest boundary incomplete: {row['source_id']}")


def verify_apollo_q2_parent_receipt_refresh() -> None:
    with APOLLO_Q2_PARENT_RECEIPT_REFRESH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "refresh_id", "queue_id", "source_route", "period", "observed_value",
            "destination_scope", "result_class", "what_is_proven", "missing_join",
            "primary_source_url", "source_artifact", "local_source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Apollo Q2 parent-receipt refresh header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row.get("refresh_id") for row in rows] != ["APR-001", "APR-002", "APR-003", "APR-004", "APR-005"]:
        fail("Apollo Q2 parent-receipt refresh rows changed unexpectedly")
    expected_urls = {
        "APR-001": "https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm",
        "APR-002": "https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm",
        "APR-003": "https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm",
        "APR-004": "https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm",
        "APR-005": "https://ir.athene.com/",
    }
    for row in rows:
        if row.get("primary_source_url") != expected_urls[row["refresh_id"]]:
            fail(f"Apollo Q2 parent-receipt refresh source changed: {row['refresh_id']}")
        if row.get("result_class") not in {"searched-negative", "evidence-insufficient", "proven-boundary", "source-not-found"}:
            fail(f"Apollo Q2 parent-receipt refresh over-promoted: {row['refresh_id']}")
        if not row.get("missing_join", "").strip():
            fail(f"Apollo Q2 parent-receipt refresh missing join: {row['refresh_id']}")
        local_source = ROOT / row.get("local_source_artifact", "")
        if not local_source.exists():
            fail(f"Apollo Q2 parent-receipt refresh local source missing: {row['refresh_id']}")


def verify_athene_corporate_structure_boundary() -> None:
    with APOLLO_ATHENE_CORPORATE_STRUCTURE_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "boundary_id", "queue_id", "source_route", "period", "observed_value",
            "destination_scope", "result_class", "what_is_proven", "missing_join",
            "primary_source_url", "source_artifact", "local_source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Athene corporate-structure boundary header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row.get("boundary_id") for row in rows] != ["ACSPB-001", "ACSPB-002", "ACSPB-003", "ACSPB-004", "ACSPB-005", "ACSPB-006", "ACSPB-007"]:
        fail("Athene corporate-structure boundary rows changed unexpectedly")
    for row in rows:
        if row.get("queue_id") not in {"Q-07", "Q-08"}:
            fail(f"Athene corporate-structure boundary queue changed: {row.get('boundary_id')}")
        if row.get("result_class") not in {"evidence-insufficient", "source-access-controlled"}:
            fail(f"Athene corporate-structure boundary over-promoted: {row.get('boundary_id')}")
        if not row.get("missing_join", "").strip():
            fail(f"Athene corporate-structure boundary missing join: {row.get('boundary_id')}")
        if not row.get("source_artifact", "").strip() or not resolve_source(APOLLO_ATHENE_CORPORATE_STRUCTURE_BOUNDARY, row["source_artifact"]).exists():
            fail(f"Athene corporate-structure boundary source missing: {row.get('boundary_id')}")
        if not (ROOT / row.get("local_source_artifact", "")).exists():
            fail(f"Athene corporate-structure boundary local artifact missing: {row.get('boundary_id')}")


def verify_cross_sector_comparison() -> None:
    expected_header = [
        "comparison_id", "pilot", "originating_force", "economic_control_point",
        "immediate_payer_or_funding_source", "main_burden_carrier", "owner_cash_question",
        "valuation_object", "current_proof_grade", "decisive_falsifier", "source_artifact",
        "supporting_artifacts",
    ]
    with CROSS_SECTOR_COMPARISON.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"cross-sector comparison header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row.get("comparison_id") for row in rows] != ["CSC-001", "CSC-002", "CSC-003"]:
        fail("cross-sector comparison must contain the three active pilots in order")
    if {row["pilot"] for row in rows} != {"TJX / Target / Walmart", "Wheaton–Antamina", "Apollo–Athene–ARI"}:
        fail("cross-sector comparison pilot set changed unexpectedly")
    required_terms = {
        "CSC-001": ("owner cash", "sales strength", "Qualified cohort signal"),
        "CSC-002": ("delivered metal", "threshold", "return unproven"),
        "CSC-003": ("legal entity", "unrestricted cash", "common cash unproven"),
    }
    for row in rows:
        for term in required_terms[row["comparison_id"]]:
            if term.lower() not in " ".join(row.values()).lower():
                fail(f"cross-sector comparison term missing for {row['comparison_id']}: {term}")
        for artifact in row["supporting_artifacts"].split(";"):
            if not (PILOT_DIR / artifact).exists():
                fail(f"cross-sector supporting artifact missing: {artifact}")


def verify_wheaton_packet_boundary() -> None:
    if not WHEATON_PACKET_BOUNDARY.exists():
        fail(f"missing {WHEATON_PACKET_BOUNDARY.relative_to(ROOT)}")
    with WHEATON_PACKET_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["gate_id", "source_scope", "primary_source_urls", "period", "search_terms", "observed_fields", "current_status", "what_is_proven", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton packet-boundary header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 1 or rows[0]["gate_id"] != "WPM-048":
        fail("Wheaton packet-boundary rows changed")
    row = rows[0]
    if row["current_status"] != "source-search-boundary-confirmed" or "BHP-only" not in row["what_is_proven"]:
        fail("Wheaton packet-boundary status or claim changed")
    expected_urls = (
        "https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm; "
        "https://www.sec.gov/Archives/edgar/data/811809/000119312526138837/d21321d6k.htm; "
        "https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex992.htm; "
        "https://www.bhp.com/news/media-centre/releases/2026/02/bhp-enters-into-a-silver-streaming-agreement; "
        "https://www.sec.gov/Archives/edgar/data/1323404/000127956926000263/ex991.htm; "
        "https://www.sec.gov/Archives/edgar/data/1323404/000119312526212446/d91444dex991.htm; "
        "https://www.wheatonpm.com/portfolio/operating-mines/antamina/default.aspx"
    )
    if "official SEC Q2 2026 MD&A" not in row["source_scope"] or "BHP April 2 2026 Form 6-K" not in row["source_scope"] or "56.718M" not in row["observed_fields"] or row["primary_source_urls"] != expected_urls:
        fail("Wheaton packet-boundary public cross-check is missing")
    for field in ("source_scope", "primary_source_urls", "period", "search_terms", "observed_fields", "what_is_proven", "missing_upgrade"):
        if not row[field].strip():
            fail(f"Wheaton packet-boundary row incomplete: {field}")


def verify_wheaton_first_delivery_boundary() -> None:
    if not WHEATON_FIRST_DELIVERY_BOUNDARY.exists():
        fail(f"missing {WHEATON_FIRST_DELIVERY_BOUNDARY.relative_to(ROOT)}")
    expected_header = [
        "claim_id", "period", "topic", "value", "evidence_grade",
        "what_is_proven", "what_is_not_proven", "source_artifact", "next_test",
    ]
    with WHEATON_FIRST_DELIVERY_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Wheaton first-delivery header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {f"WPM-Q2-DEL-{index:03d}" for index in range(1, 7)}
    if len(rows) != 6 or {row["claim_id"] for row in rows} != expected_ids:
        fail("Wheaton first-delivery claims changed unexpectedly")
    expected_grades = {
        "WPM-Q2-DEL-001": "first-delivery-confirmed",
        "WPM-Q2-DEL-002": "combined-stream-production-visible",
        "WPM-Q2-DEL-003": "settlement-mechanism-confirmed",
        "WPM-Q2-DEL-004": "upfront-proceeds-confirmed",
        "WPM-Q2-DEL-005": "owner-cash-boundary-held",
        "WPM-Q2-DEL-006": "interpretation-boundary-held",
    }
    for row in rows:
        if row["evidence_grade"] != expected_grades[row["claim_id"]]:
            fail(f"Wheaton first-delivery evidence grade changed: {row['claim_id']}")
        for field in ("what_is_proven", "what_is_not_proven", "next_test"):
            if not row[field].strip():
                fail(f"Wheaton first-delivery row missing {field}: {row['claim_id']}")
        if not resolve_source(WHEATON_FIRST_DELIVERY_BOUNDARY, row["source_artifact"]).exists():
            fail(f"Wheaton first-delivery source missing: {row['source_artifact']}")


def verify_wheaton_after_tax_frontier() -> None:
    if not WHEATON_AFTER_TAX_FRONTIER.exists():
        fail(f"missing Wheaton after-tax frontier: {WHEATON_AFTER_TAX_FRONTIER.relative_to(ROOT)}")
    with WHEATON_AFTER_TAX_FRONTIER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "allocation_case", "finance_allocation_pct", "tax_allocation_pct",
            "annualized_stream_ocf_proxy_musd", "annualized_finance_cost_musd",
            "annualized_tax_expense_musd", "after_tax_financed_cash_musd",
            "cash_to_upfront_pct", "simple_payback_years", "status",
            "source_artifact", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton after-tax frontier header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 5:
        fail(f"Wheaton after-tax frontier must contain 5 rows, found {len(rows)}")
    for row in rows:
        for field in expected_header:
            if field != "simple_payback_years" and not row[field].strip():
                fail(f"Wheaton after-tax frontier row incomplete: {field}")
        finance_rate = float(row["finance_allocation_pct"]) / 100
        tax_rate = float(row["tax_allocation_pct"]) / 100
        ocf = float(row["annualized_stream_ocf_proxy_musd"])
        finance = float(row["annualized_finance_cost_musd"])
        tax = float(row["annualized_tax_expense_musd"])
        cash = float(row["after_tax_financed_cash_musd"])
        expected_cash = ocf - finance * finance_rate - tax * tax_rate
        if abs(cash - expected_cash) > 0.001:
            fail(f"Wheaton after-tax frontier arithmetic mismatch: {row}")
        expected_yield = cash / 4300 * 100
        if abs(float(row["cash_to_upfront_pct"]) - expected_yield) > 0.001:
            fail(f"Wheaton after-tax frontier yield mismatch: {row}")


def verify_wheaton_reserve_ceiling() -> None:
    if not WHEATON_RESERVE_CEILING.exists():
        fail(f"missing Wheaton reserve ceiling: {WHEATON_RESERVE_CEILING.relative_to(ROOT)}")
    with WHEATON_RESERVE_CEILING.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "production_proxy_moz_per_year", "payable_factor_pct",
            "payable_production_moz_per_year", "p_and_p_contained_reserve_moz",
            "mechanical_payable_ceiling_moz", "full_years_within_ceiling",
            "partial_next_year", "reserve_duration_years", "initial_threshold_moz",
            "gap_to_initial_threshold_moz", "status", "source_artifact", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton reserve-ceiling header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 3:
        fail(f"Wheaton reserve ceiling must contain 3 rows, found {len(rows)}")
    for row in rows:
        for field in expected_header:
            if not row[field].strip():
                fail(f"Wheaton reserve-ceiling row incomplete: {row}")
        production = float(row["production_proxy_moz_per_year"])
        factor = float(row["payable_factor_pct"]) / 100
        payable = float(row["payable_production_moz_per_year"])
        reserve = float(row["mechanical_payable_ceiling_moz"])
        duration = float(row["reserve_duration_years"])
        gap = float(row["gap_to_initial_threshold_moz"])
        if not math.isclose(payable, production * factor, abs_tol=0.0001):
            fail(f"Wheaton reserve ceiling payable arithmetic failed: {row}")
        if not math.isclose(reserve, 65.7 * factor, abs_tol=0.0001):
            fail(f"Wheaton reserve ceiling quantity changed: {row}")
        if not math.isclose(duration, reserve / payable, abs_tol=0.001):
            fail(f"Wheaton reserve ceiling duration failed: {row}")
        if not math.isclose(gap, 100 - reserve, abs_tol=0.001):
            fail(f"Wheaton reserve ceiling threshold gap failed: {row}")
        if row["status"] != "qualified-mechanical-ceiling":
            fail(f"Wheaton reserve ceiling status changed: {row}")
        if not resolve_source(WHEATON_RESERVE_CEILING, row["source_artifact"]).exists():
            fail(f"Wheaton reserve-ceiling source missing: {row['source_artifact']}")


def verify_wheaton_reserve_recovery_frontier() -> None:
    if not WHEATON_RESERVE_RECOVERY_FRONTIER.exists():
        fail(f"missing Wheaton reserve-recovery frontier: {WHEATON_RESERVE_RECOVERY_FRONTIER.relative_to(ROOT)}")
    with WHEATON_RESERVE_RECOVERY_FRONTIER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "frontier_id", "queue_id", "silver_price_usd_oz", "contained_reserve_moz",
            "payable_factor_pct", "payable_reserve_moz", "stream_payment_pct",
            "cash_before_burden_musd", "burden_haircut_pct", "cash_after_burden_musd",
            "upfront_payment_musd", "after_burden_recovery_pct", "threshold_applied",
            "status", "source_artifact", "missing_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton reserve-recovery header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["frontier_id"] for row in rows] != ["RUF-001", "RUF-002", "RUF-003", "RUF-004"]:
        fail("Wheaton reserve-recovery frontier rows changed unexpectedly")
    expected_price_haircut = {"RUF-001": (35, 20), "RUF-002": (60, 20), "RUF-003": (90, 20), "RUF-004": (90, 0)}
    for row in rows:
        price, haircut = expected_price_haircut[row["frontier_id"]]
        if float(row["silver_price_usd_oz"]) != price or float(row["burden_haircut_pct"]) != haircut:
            fail(f"Wheaton reserve-recovery scenario changed: {row['frontier_id']}")
        payable_reserve = 65.7 * 0.90
        cash_before = payable_reserve * price * (1 - 0.20)
        cash_after = cash_before * (1 - haircut / 100)
        recovery = cash_after / 4300 * 100
        if not math.isclose(float(row["payable_reserve_moz"]), payable_reserve, abs_tol=0.0001):
            fail(f"Wheaton reserve-recovery payable reserve changed: {row['frontier_id']}")
        if not math.isclose(float(row["cash_before_burden_musd"]), cash_before, abs_tol=0.001):
            fail(f"Wheaton reserve-recovery pre-burden arithmetic failed: {row['frontier_id']}")
        if not math.isclose(float(row["cash_after_burden_musd"]), cash_after, abs_tol=0.001):
            fail(f"Wheaton reserve-recovery post-burden arithmetic failed: {row['frontier_id']}")
        if not math.isclose(float(row["after_burden_recovery_pct"]), recovery, abs_tol=0.001):
            fail(f"Wheaton reserve-recovery percentage failed: {row['frontier_id']}")
        if row["status"] != "reserve-capped-frontier" or row["threshold_applied"] != "no-initial-100M-threshold":
            fail(f"Wheaton reserve-recovery status boundary changed: {row['frontier_id']}")
        if "Reserve-backed" not in row["missing_upgrade"]:
            fail(f"Wheaton reserve-recovery upgrade boundary missing: {row['frontier_id']}")


def verify_apollo_common_owner_bridge() -> None:
    if not APOLLO_BRIDGE.exists():
        fail(f"missing {APOLLO_BRIDGE.relative_to(ROOT)}")
    with APOLLO_BRIDGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != BRIDGE_HEADER:
            fail(f"Apollo bridge header mismatch: {reader.fieldnames}")
        rows = list(reader)
    by_id = {row["line_id"]: row for row in rows}
    required = {f"APO-B{index:02d}" for index in range(1, 37)}
    if set(by_id) != required:
        fail(f"Apollo bridge lines are {sorted(by_id)}")
    for row in rows:
        source = resolve_source(APOLLO_BRIDGE, row["source_artifact"])
        if not source.exists():
            fail(f"Apollo bridge source missing: {row['source_artifact']}")
    amount = lambda line: float(by_id[line]["amount_musd"])
    if amount("APO-B04") != amount("APO-B01") + amount("APO-B02") + amount("APO-B03"):
        fail("Apollo bridge earnings layers do not sum")
    if amount("APO-B07") != amount("APO-B04") - amount("APO-B05") - amount("APO-B06"):
        fail("Apollo bridge ANI does not reconcile")
    if amount("APO-B11") != amount("APO-B09") + amount("APO-B10"):
        fail("Apollo bridge capital return does not reconcile")
    if by_id["APO-B15"]["amount_musd"] != "NA":
        fail("Apollo common-owner residual must remain unresolved")
    expected_transfers = {
        "APO-B16": "42",
        "APO-B17": "271",
        "APO-B18": "759",
        "APO-B19": "301",
        "APO-B20": "41617",
        "APO-B21": "14741",
    }
    for line_id, expected in expected_transfers.items():
        if by_id[line_id]["amount_musd"] != expected:
            fail(f"Apollo entity-transfer line {line_id} changed unexpectedly")
    if by_id["APO-B22"]["amount_musd"] != "NA":
        fail("Apollo insurance dividend restriction must remain a boundary")
    expected_athene = {
        "APO-B23": "375",
        "APO-B24": "71",
        "APO-B25": "27801",
        "APO-B26": "23711",
    }
    for line_id, expected in expected_athene.items():
        if by_id[line_id]["amount_musd"] != expected:
            fail(f"Apollo Athene cash line {line_id} changed unexpectedly")
    expected_cash_pools = {"APO-B27": "3415", "APO-B28": "19", "APO-B29": "23540", "APO-B30": "21957", "APO-B31": "1583"}
    for line_id, expected in expected_cash_pools.items():
        if by_id[line_id]["amount_musd"] != expected:
            fail(f"Apollo cash-pool boundary line {line_id} changed unexpectedly")
    if amount("APO-B29") != amount("APO-B30") + amount("APO-B31"):
        fail("Apollo retirement-services cash pool does not reconcile")
    if amount("APO-B35") != amount("APO-B32") + amount("APO-B33"):
        fail("Apollo common cash uses do not reconcile")
    if amount("APO-B36") != amount("APO-B35") + amount("APO-B34"):
        fail("Apollo common plus preferred cash uses do not reconcile")


def verify_retail_owner_cash_bridge() -> None:
    if not RETAIL_BRIDGE.exists():
        fail(f"missing {RETAIL_BRIDGE.relative_to(ROOT)}")
    with RETAIL_BRIDGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_BRIDGE_HEADER:
            fail(f"retail bridge header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 13:
        fail(f"retail bridge must contain 13 rows, found {len(rows)}")
    for row in rows:
        source = resolve_source(RETAIL_BRIDGE, row["source_artifact"])
        if not source.exists():
            fail(f"retail bridge source missing: {row['source_artifact']}")
        for field in ("company", "period", "owner_cash_status", "inventory_signal", "working_capital_signal", "next_upgrade"):
            if not row[field].strip():
                fail(f"retail bridge has empty {field}")
        has_cash_inputs = row["operating_cash_flow_musd"].strip() and row["property_spending_musd"].strip()
        if has_cash_inputs:
            operating = number(row, "operating_cash_flow_musd")
            property_spending = number(row, "property_spending_musd")
            cash_after = number(row, "cash_after_property_musd")
            if not math.isclose(cash_after, operating - property_spending, abs_tol=0.001):
                fail(f"{row['company']} {row['period']} retail cash bridge does not reconcile")
        elif row["cash_after_property_musd"].strip():
            fail(f"{row['company']} {row['period']} has residual cash without both cash inputs")
    tjx = [row for row in rows if row["company"] == "TJX"]
    if len(tjx) != 5:
        fail("retail bridge must contain five TJX periods")
    tjx_by_period = {row["period"]: row for row in tjx}
    for period in ("FY2024", "FY2025", "FY2026"):
        if tjx_by_period[period]["owner_cash_status"] not in {"reported-cash-bridge", "qualified"}:
            fail(f"TJX {period} must contain a filing-backed cash bridge")
    if tjx_by_period["Q1 FY2027"]["owner_cash_status"] != "unresolved":
        fail("TJX Q1 FY2027 must remain unresolved until a quarterly cash bridge is extracted")
    if tjx_by_period["H1 FY2027"]["owner_cash_status"] != "qualified":
        fail("TJX H1 FY2027 must contain the newly extracted cash bridge")
    if not math.isclose(number(tjx_by_period["H1 FY2027"], "cash_after_property_musd"), 2186, abs_tol=0.001):
        fail("TJX H1 FY2027 cash bridge changed unexpectedly")
    target_h1 = next(
        row for row in rows
        if row["company"] == "Target" and row["period"] == "H1 2026"
    )
    if number(target_h1, "revenue_musd") != 51982:
        fail("Target H1 2026 revenue denominator changed unexpectedly")
    target_annual_revenue = {
        row["period"]: number(row, "revenue_musd")
        for row in rows
        if row["company"] == "Target" and row["period"] in {"FY2023", "FY2024", "FY2025"}
    }
    if target_annual_revenue != {"FY2023": 107412, "FY2024": 106566, "FY2025": 104780}:
        fail("Target annual revenue denominators changed unexpectedly")
    expected_revenue = {
        ("TJX", "FY2024"): 54217,
        ("TJX", "FY2025"): 56360,
        ("TJX", "FY2026"): 60372,
        ("Walmart", "FY2024"): 642637,
        ("Walmart", "FY2025"): 674538,
        ("Walmart", "FY2026"): 706413,
        ("Walmart", "H1 FY2027"): 361784,
    }
    for (company, period), revenue in expected_revenue.items():
        row = next(item for item in rows if item["company"] == company and item["period"] == period)
        if number(row, "revenue_musd") != revenue:
            fail(f"{company} {period} revenue denominator changed unexpectedly")


def verify_retail_burden_normalization() -> None:
    if not RETAIL_BURDEN.exists():
        fail(f"missing {RETAIL_BURDEN.relative_to(ROOT)}")
    with RETAIL_BURDEN.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_BURDEN_HEADER:
            fail(f"retail burden header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 4 or {row["company"] for row in rows} != {"TJX", "Target", "Walmart"}:
        fail("retail burden table must contain annual/current rows for the cohort")
    for row in rows:
        source = resolve_source(RETAIL_BURDEN, row["source_artifact"])
        if not source.exists():
            fail(f"retail burden source missing: {row['source_artifact']}")
        for field in ("company", "period", "normalization_status", "next_upgrade"):
            if not row[field].strip():
                fail(f"retail burden has empty {field}")
        for field in ("operating_lease_liabilities_musd", "diluted_shares_millions"):
            number(row, field)
        capex_fields = [row["maintenance_capex_musd"].strip(), row["growth_or_platform_capex_musd"].strip()]
        if all(capex_fields):
            maintenance = number(row, "maintenance_capex_musd")
            growth = number(row, "growth_or_platform_capex_musd")
            if row["company"] == "TJX" and not math.isclose(maintenance + growth, 1957, abs_tol=0.001):
                fail("TJX burden capex categories do not reconcile to FY2026 property additions")
            if row["company"] == "Walmart" and not math.isclose(maintenance + growth, 14181, abs_tol=0.001):
                fail("Walmart burden capex categories do not reconcile to H1 FY2027 capital spending")


def verify_retail_cash_screen() -> None:
    if not RETAIL_CASH_SCREEN.exists():
        fail(f"missing {RETAIL_CASH_SCREEN.relative_to(ROOT)}")
    with RETAIL_CASH_SCREEN.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_CASH_SCREEN_HEADER:
            fail(f"retail cash screen header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 3 or {row["company"] for row in rows} != {"TJX", "Target", "Walmart"}:
        fail("retail cash screen must contain one row for each cohort company")
    for row in rows:
        source = resolve_source(RETAIL_CASH_SCREEN, row["source_artifact"])
        if not source.exists():
            fail(f"retail cash screen source missing: {row['source_artifact']}")
        reported = number(row, "reported_cash_after_property_musd")
        adjustment = number(row, "known_one_time_or_cash_support_musd")
        low = number(row, "low_screen_cash_musd")
        base = number(row, "base_screen_cash_musd")
        high = number(row, "high_screen_cash_musd")
        if not (0 <= low <= base <= high <= reported):
            fail(f"{row['company']} normalized cash screen is not ordered")
        if row["company"] == "TJX":
            sbc = number(row, "share_based_compensation_musd")
            expected = (reported - adjustment - sbc, reported - sbc, reported)
        elif row["company"] == "Target":
            sbc = number(row, "share_based_compensation_musd")
            expected = (reported - adjustment - sbc, reported - 752 - sbc, reported)
        else:
            if row["share_based_compensation_musd"].strip():
                fail("Walmart H1 screen must keep stock compensation unresolved")
            expected = (reported - adjustment, reported, reported)
        for actual, expected_value in zip((low, base, high), expected):
            if not math.isclose(actual, expected_value, abs_tol=0.001):
                fail(f"{row['company']} normalized cash screen does not reconcile")


def verify_retail_support_dependency() -> None:
    if not RETAIL_SUPPORT_DEPENDENCY.exists():
        fail(f"missing retail support-dependency screen: {RETAIL_SUPPORT_DEPENDENCY.relative_to(ROOT)}")
    with RETAIL_SUPPORT_DEPENDENCY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "company", "period", "reported_cash_after_property_musd",
            "conservative_screen_cash_musd", "screen_reduction_musd",
            "reduction_pct_of_reported_cash", "comparability_status",
            "source_artifact", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail support-dependency header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 4:
        fail(f"retail support-dependency screen must contain 4 rows, found {len(rows)}")
    for row in rows:
        for field in expected_header:
            if not row[field].strip():
                fail(f"retail support-dependency row incomplete: {row}")
        reported = number(row, "reported_cash_after_property_musd")
        conservative = number(row, "conservative_screen_cash_musd")
        reduction = number(row, "screen_reduction_musd")
        percentage = number(row, "reduction_pct_of_reported_cash")
        if not math.isclose(reduction, reported - conservative, abs_tol=0.001):
            fail(f"retail support-dependency reduction does not reconcile: {row}")
        if not math.isclose(percentage, reduction / reported * 100, abs_tol=0.001):
            fail(f"retail support-dependency percentage does not reconcile: {row}")
        if not resolve_source(RETAIL_SUPPORT_DEPENDENCY, row["source_artifact"]).exists():
            fail(f"retail support-dependency source missing: {row['source_artifact']}")


def verify_tjx_temporary_support() -> None:
    if not TJX_TEMPORARY_SUPPORT.exists():
        fail(f"missing {TJX_TEMPORARY_SUPPORT.relative_to(ROOT)}")
    with TJX_TEMPORARY_SUPPORT.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["metric", "period", "amount_musd", "classification", "source_artifact", "interpretation", "next_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"TJX temporary-support header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 5:
        fail(f"TJX temporary-support table must contain 5 rows, found {len(rows)}")
    expected = {
        "IEEPA tariff refunds received": "331",
        "Tariff-related incentive and bonus accrual": "112",
        "Net tariff pretax benefit": "219",
        "Credit-card interchange settlement received": "419",
        "Combined temporary cash-support candidate": "750",
    }
    by_metric = {row["metric"]: row for row in rows}
    if set(by_metric) != set(expected):
        fail(f"TJX temporary-support metrics changed: {sorted(by_metric)}")
    for metric, amount in expected.items():
        row = by_metric[metric]
        if row["amount_musd"] != amount:
            fail(f"TJX temporary-support amount changed for {metric}")
        if not row["interpretation"].strip() or not row["next_upgrade"].strip():
            fail(f"TJX temporary-support row incomplete: {metric}")
        if not resolve_source(TJX_TEMPORARY_SUPPORT, row["source_artifact"]).exists():
            fail(f"TJX temporary-support source missing: {row['source_artifact']}")


def verify_retail_temporary_support() -> None:
    if not RETAIL_TEMPORARY_SUPPORT.exists():
        fail(f"missing {RETAIL_TEMPORARY_SUPPORT.relative_to(ROOT)}")
    text = RETAIL_TEMPORARY_SUPPORT.read_text(encoding="utf-8")
    for marker in ("$994M", "$752M", "$2.9B", "$0.981B"):
        if marker not in text:
            fail(f"retail temporary-support memo missing marker {marker}")


def verify_retail_supplier_finance() -> None:
    if not RETAIL_SUPPLIER_FINANCE.exists():
        fail(f"missing {RETAIL_SUPPLIER_FINANCE.relative_to(ROOT)}")
    with RETAIL_SUPPLIER_FINANCE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["company", "period", "supplier_finance_obligation_musd", "accounts_payable_treatment", "source_artifact", "current_status", "what_is_proven", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"retail supplier-finance header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 2 or {row["company"] for row in rows} != {"Target", "Walmart"}:
        fail("retail supplier-finance rows changed unexpectedly")
    expected = {"Target": "3200", "Walmart": "6400"}
    for row in rows:
        if row["supplier_finance_obligation_musd"] != expected[row["company"]]:
            fail(f"supplier-finance amount changed for {row['company']}")
        if row["current_status"] != "boundary-confirmed":
            fail(f"supplier-finance status changed for {row['company']}")
        if not resolve_source(RETAIL_SUPPLIER_FINANCE, row["source_artifact"]).exists():
            fail(f"supplier-finance source missing: {row['source_artifact']}")


def verify_retail_supplier_finance_rollforward() -> None:
    if not RETAIL_SUPPLIER_FINANCE_ROLLFORWARD.exists():
        fail(f"missing {RETAIL_SUPPLIER_FINANCE_ROLLFORWARD.relative_to(ROOT)}")
    with RETAIL_SUPPLIER_FINANCE_ROLLFORWARD.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "rollforward_id", "company", "as_of_date", "period_label",
            "supplier_finance_obligation_musd", "comparison_date",
            "comparison_obligation_musd", "change_musd", "comparison_basis",
            "status", "source_artifact", "remaining_claims",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail supplier-finance roll-forward header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "RSFR-001": ("Target", "2026-08-01", "2026-01-31", 3200, 3000, 200),
        "RSFR-002": ("Target", "2026-08-01", "2025-08-02", 3200, 2900, 300),
        "RSFR-003": ("Walmart", "2026-07-31", "2026-01-31", 6400, 6000, 400),
        "RSFR-004": ("Walmart", "2026-07-31", "2025-07-31", 6400, 5700, 700),
        "RSFR-005": ("Walmart", "2026-01-31", "2025-01-31", 5989, 5725, 264),
        "RSFR-006": ("Target", "2026-01-31", "2025-02-01", 3026, 3666, -640),
    }
    if len(rows) != len(expected) or {row["rollforward_id"] for row in rows} != set(expected):
        fail("retail supplier-finance roll-forward rows changed unexpectedly")
    for row in rows:
        company, as_of_date, comparison_date, current, comparison, change = expected[row["rollforward_id"]]
        if (row["company"], row["as_of_date"], row["comparison_date"]) != (company, as_of_date, comparison_date):
            fail(f"retail supplier-finance roll-forward dates changed: {row['rollforward_id']}")
        if int(row["supplier_finance_obligation_musd"]) != current or int(row["comparison_obligation_musd"]) != comparison:
            fail(f"retail supplier-finance roll-forward amounts changed: {row['rollforward_id']}")
        if int(row["change_musd"]) != current - comparison:
            fail(f"retail supplier-finance roll-forward arithmetic failed: {row['rollforward_id']}")
        if row["status"] not in {"dated-supplier-finance-movement-visible", "annual-settlement-flow-visible"}:
            fail(f"retail supplier-finance roll-forward status changed: {row['rollforward_id']}")
        if not row["remaining_claims"].strip() or not resolve_source(RETAIL_SUPPLIER_FINANCE_ROLLFORWARD, row["source_artifact"]).exists():
            fail(f"retail supplier-finance roll-forward source or boundary missing: {row['rollforward_id']}")
    memo = (PILOT_DIR / "combined-investment-research-pilot-02-retail-supplier-finance-roll-forward-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("dated comparative movement surface", "$3.2B", "$6.4B", "not a settlement ledger", "must not be added to or subtracted from operating cash flow", "$40.062B", "$12.066B", "settlement-flow observation"):
        if marker not in memo:
            fail(f"retail supplier-finance roll-forward boundary marker missing: {marker}")


def verify_retail_supplier_finance_settlement_frontier() -> None:
    if not RETAIL_SUPPLIER_FINANCE_SETTLEMENT_FRONTIER.exists():
        fail(f"missing {RETAIL_SUPPLIER_FINANCE_SETTLEMENT_FRONTIER.relative_to(ROOT)}")
    with RETAIL_SUPPLIER_FINANCE_SETTLEMENT_FRONTIER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "control_id", "company", "period", "source_route", "observed_fact",
            "what_is_proven", "what_is_not_proven", "result_class",
            "primary_source_url", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail supplier-finance settlement frontier header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "RSF-SET-001": ("Target", "H1 2026", "$3.2B", "historically been lower"),
        "RSF-SET-002": ("Walmart", "H1 FY2027", "$6.4B", "invoice due date"),
    }
    if [row.get("control_id") for row in rows] != list(expected):
        fail("retail supplier-finance settlement frontier rows changed unexpectedly")
    for row in rows:
        company, period, amount_marker, fact_marker = expected[row["control_id"]]
        if (row["company"], row["period"]) != (company, period):
            fail(f"retail supplier-finance settlement frontier identity changed: {row['control_id']}")
        if row["result_class"] != "settlement-unproven" or amount_marker not in row["observed_fact"] or fact_marker not in row["observed_fact"]:
            fail(f"retail supplier-finance settlement frontier boundary changed: {row['control_id']}")
        if not row["what_is_not_proven"].strip() or not row["source_artifact"].strip():
            fail(f"retail supplier-finance settlement frontier missing boundary: {row['control_id']}")
        if not resolve_source(RETAIL_SUPPLIER_FINANCE_SETTLEMENT_FRONTIER, row["source_artifact"]).exists():
            fail(f"retail supplier-finance settlement frontier source missing: {row['source_artifact']}")


def verify_uri_q13_next_source_package() -> None:
    if not URI_Q13_NEXT_SOURCE_PACKAGE.exists():
        fail(f"missing {URI_Q13_NEXT_SOURCE_PACKAGE.relative_to(ROOT)}")
    with URI_Q13_NEXT_SOURCE_PACKAGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "request_id", "queue_id", "priority", "source_object", "minimum_fields",
            "promotion_join", "current_public_status", "result_class", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"URI Q-13 source-package header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = [
        "URI-Q13-REQ-001", "URI-Q13-REQ-002", "URI-Q13-REQ-003",
        "URI-Q13-REQ-004", "URI-Q13-REQ-005",
    ]
    if [row.get("request_id") for row in rows] != expected_ids:
        fail("URI Q-13 source-package rows changed unexpectedly")
    for expected_priority, row in enumerate(rows, start=1):
        if row["queue_id"] != "Q-13" or int(row["priority"]) != expected_priority or row["result_class"] != "source-required":
            fail(f"URI Q-13 source-package routing changed: {row['request_id']}")
        if not row["minimum_fields"].strip() or not row["promotion_join"].strip():
            fail(f"URI Q-13 source-package fields incomplete: {row['request_id']}")
        if not resolve_source(URI_Q13_NEXT_SOURCE_PACKAGE, row["source_artifact"]).exists():
            fail(f"URI Q-13 source-package artifact missing: {row['source_artifact']}")


def verify_apollo_ap_grange_next_source_package() -> None:
    if not APOLLO_AP_GRANGE_NEXT_SOURCE_PACKAGE.exists():
        fail(f"missing AP Grange next-source package: {APOLLO_AP_GRANGE_NEXT_SOURCE_PACKAGE.relative_to(ROOT)}")
    with APOLLO_AP_GRANGE_NEXT_SOURCE_PACKAGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "request_id", "queue_id", "priority", "source_object", "minimum_fields",
            "promotion_join", "current_public_status", "result_class", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"AP Grange source-package header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = [
        "APG-SET-REQ-001", "APG-SET-REQ-002", "APG-SET-REQ-003",
        "APG-SET-REQ-004", "APG-SET-REQ-005",
    ]
    if [row.get("request_id") for row in rows] != expected_ids:
        fail("AP Grange source-package rows changed unexpectedly")
    for expected_priority, row in enumerate(rows, start=1):
        if row["queue_id"] != "Q-08" or int(row["priority"]) != expected_priority:
            fail(f"AP Grange source-package routing changed: {row['request_id']}")
        if row["result_class"] != "source-required" or row["current_public_status"] != "settlement-unproven":
            fail(f"AP Grange source-package status changed: {row['request_id']}")
        if not row["minimum_fields"].strip() or not row["promotion_join"].strip():
            fail(f"AP Grange source-package fields incomplete: {row['request_id']}")
        if not resolve_source(APOLLO_AP_GRANGE_NEXT_SOURCE_PACKAGE, row["source_artifact"]).exists():
            fail(f"AP Grange source-package artifact missing: {row['source_artifact']}")


def verify_wheaton_q03_next_source_package() -> None:
    if not WHEATON_Q03_NEXT_SOURCE_PACKAGE.exists():
        fail(f"missing Wheaton Q-03 next-source package: {WHEATON_Q03_NEXT_SOURCE_PACKAGE.relative_to(ROOT)}")
    with WHEATON_Q03_NEXT_SOURCE_PACKAGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "request_id", "queue_id", "priority", "source_object", "minimum_fields",
            "promotion_join", "current_public_status", "result_class", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton Q-03 source-package header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = [
        "WPM-Q03-REQ-001", "WPM-Q03-REQ-002", "WPM-Q03-REQ-003",
        "WPM-Q03-REQ-004", "WPM-Q03-REQ-005",
    ]
    if [row.get("request_id") for row in rows] != expected_ids:
        fail("Wheaton Q-03 source-package rows changed unexpectedly")
    for expected_priority, row in enumerate(rows, start=1):
        if row["queue_id"] != "Q-03" or int(row["priority"]) != expected_priority:
            fail(f"Wheaton Q-03 source-package routing changed: {row['request_id']}")
        if row["result_class"] != "source-required" or row["current_public_status"] != "return-unproven":
            fail(f"Wheaton Q-03 source-package status changed: {row['request_id']}")
        if not row["minimum_fields"].strip() or not row["promotion_join"].strip():
            fail(f"Wheaton Q-03 source-package fields incomplete: {row['request_id']}")
        if not resolve_source(WHEATON_Q03_NEXT_SOURCE_PACKAGE, row["source_artifact"]).exists():
            fail(f"Wheaton Q-03 source-package artifact missing: {row['source_artifact']}")


def verify_apollo_q07_next_source_package() -> None:
    if not APOLLO_Q07_NEXT_SOURCE_PACKAGE.exists():
        fail(f"missing Apollo Q-07 next-source package: {APOLLO_Q07_NEXT_SOURCE_PACKAGE.relative_to(ROOT)}")
    with APOLLO_Q07_NEXT_SOURCE_PACKAGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "request_id", "queue_id", "priority", "source_object", "minimum_fields",
            "promotion_join", "current_public_status", "result_class", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Apollo Q-07 source-package header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = [
        "APO-Q07-REQ-001", "APO-Q07-REQ-002", "APO-Q07-REQ-003",
        "APO-Q07-REQ-004", "APO-Q07-REQ-005",
    ]
    if [row.get("request_id") for row in rows] != expected_ids:
        fail("Apollo Q-07 source-package rows changed unexpectedly")
    for expected_priority, row in enumerate(rows, start=1):
        if row["queue_id"] != "Q-07" or int(row["priority"]) != expected_priority:
            fail(f"Apollo Q-07 source-package routing changed: {row['request_id']}")
        if row["result_class"] != "source-required" or row["current_public_status"] != "receipt-unproven":
            fail(f"Apollo Q-07 source-package status changed: {row['request_id']}")
        if not row["minimum_fields"].strip() or not row["promotion_join"].strip():
            fail(f"Apollo Q-07 source-package fields incomplete: {row['request_id']}")
        if not resolve_source(APOLLO_Q07_NEXT_SOURCE_PACKAGE, row["source_artifact"]).exists():
            fail(f"Apollo Q-07 source-package artifact missing: {row['source_artifact']}")


def verify_insurance_q12_next_source_package() -> None:
    if not INSURANCE_Q12_NEXT_SOURCE_PACKAGE.exists():
        fail(f"missing insurance Q-12 next-source package: {INSURANCE_Q12_NEXT_SOURCE_PACKAGE.relative_to(ROOT)}")
    with INSURANCE_Q12_NEXT_SOURCE_PACKAGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "request_id", "queue_id", "priority", "source_object", "minimum_fields",
            "promotion_join", "current_public_status", "result_class", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"insurance Q-12 source-package header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = [
        "INS-Q12-REQ-001", "INS-Q12-REQ-002", "INS-Q12-REQ-003",
        "INS-Q12-REQ-004", "INS-Q12-REQ-005", "INS-Q12-REQ-006",
    ]
    if [row.get("request_id") for row in rows] != expected_ids:
        fail("insurance Q-12 source-package rows changed unexpectedly")
    for expected_priority, row in enumerate(rows, start=1):
        if row["queue_id"] != "Q-12" or int(row["priority"]) != expected_priority:
            fail(f"insurance Q-12 source-package routing changed: {row['request_id']}")
        if row["result_class"] != "source-required" or row["current_public_status"] != "return-unproven":
            fail(f"insurance Q-12 source-package status changed: {row['request_id']}")
        if not row["minimum_fields"].strip() or not row["promotion_join"].strip():
            fail(f"insurance Q-12 source-package fields incomplete: {row['request_id']}")
        if not resolve_source(INSURANCE_Q12_NEXT_SOURCE_PACKAGE, row["source_artifact"]).exists():
            fail(f"insurance Q-12 source-package artifact missing: {row['source_artifact']}")


def verify_apollo_ap_grange_tranche_a_cash_accrual() -> None:
    if not APOLLO_AP_GRANGE_TRANCHE_A_CASH_ACCRUAL.exists():
        fail(f"missing {APOLLO_AP_GRANGE_TRANCHE_A_CASH_ACCRUAL.relative_to(ROOT)}")
    with APOLLO_AP_GRANGE_TRANCHE_A_CASH_ACCRUAL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "control_id", "route", "identifier", "period", "observed_fact",
            "what_is_proven", "what_is_not_proven", "result_class", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"AP Grange Tranche A crosswalk header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = ["APG-TA-CA-001", "APG-TA-CA-002", "APG-TA-CA-003", "APG-TA-CA-004"]
    if [row.get("control_id") for row in rows] != expected_ids:
        fail("AP Grange Tranche A crosswalk rows changed unexpectedly")
    markers = {
        "APG-TA-CA-001": ("$343.374413M", "$265.774068M", "6.500%"),
        "APG-TA-CA-002": ("Cayman issuer", "6.500%", "03/20/2045"),
        "APG-TA-CA-003": ("deferred", "90 days", "KEMI"),
        "APG-TA-CA-004": ("$673M", "$5.080B", "June 30"),
    }
    for row in rows:
        if any(marker not in row["observed_fact"] for marker in markers[row["control_id"]]):
            fail(f"AP Grange Tranche A crosswalk marker changed: {row['control_id']}")
        if not row["what_is_not_proven"].strip() or not resolve_source(APOLLO_AP_GRANGE_TRANCHE_A_CASH_ACCRUAL, row["source_artifact"]).exists():
            fail(f"AP Grange Tranche A crosswalk boundary missing: {row['control_id']}")


def verify_tjx_q2_cash_capex_boundary() -> None:
    if not TJX_Q2_CASH_CAPEX_BOUNDARY.exists():
        fail(f"missing {TJX_Q2_CASH_CAPEX_BOUNDARY.relative_to(ROOT)}")
    with TJX_Q2_CASH_CAPEX_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "control_id", "company", "period", "metric", "observed_value",
            "what_is_proven", "what_is_not_proven", "result_class",
            "primary_source_url", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"TJX Q2 cash/capex boundary header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = [
        "TJX-Q2-CCB-001", "TJX-Q2-CCB-002", "TJX-Q2-CCB-003",
        "TJX-Q2-CCB-004", "TJX-Q2-CCB-005",
    ]
    if [row.get("control_id") for row in rows] != expected_ids:
        fail("TJX Q2 cash/capex boundary rows changed unexpectedly")
    markers = {
        "TJX-Q2-CCB-001": "$3.3B",
        "TJX-Q2-CCB-002": "$1.159B",
        "TJX-Q2-CCB-003": "tariff-refund receipt",
        "TJX-Q2-CCB-004": "$1.0B",
        "TJX-Q2-CCB-005": "$2.2B-$2.3B",
    }
    for row in rows:
        if row["company"] != "TJX" or markers[row["control_id"]] not in row["observed_value"]:
            fail(f"TJX Q2 cash/capex boundary marker changed: {row['control_id']}")
        if not row["what_is_not_proven"].strip() or not resolve_source(TJX_Q2_CASH_CAPEX_BOUNDARY, row["source_artifact"]).exists():
            fail(f"TJX Q2 cash/capex boundary source or limitation missing: {row['control_id']}")


def verify_retail_attached_services() -> None:
    if not RETAIL_ATTACHED_SERVICES.exists():
        fail(f"missing {RETAIL_ATTACHED_SERVICES.relative_to(ROOT)}")
    with RETAIL_ATTACHED_SERVICES.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["company", "period", "metric", "amount_musd", "denominator_musd", "primary_source_url", "source_artifact", "status", "what_is_proven", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"retail attached-services header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        ("Target", "Advertising revenue"): "525",
        ("Target", "Credit-card profit sharing"): "269",
        ("Target", "Other revenue"): "347",
        ("Walmart U.S.", "Membership and other income"): "1676",
        ("Walmart International", "Membership and other income"): "851",
        ("Sam's Club U.S.", "Membership and other income"): "1328",
    }
    if len(rows) != len(expected):
        fail("retail attached-services rows changed unexpectedly")
    for row in rows:
        key = (row["company"], row["metric"])
        if key not in expected or row["amount_musd"] != expected[key]:
            fail(f"retail attached-services row changed: {key}")
        expected_url = "https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm" if row["company"] == "Target" else "https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000154/wmt-20260731.htm"
        if row["primary_source_url"] != expected_url:
            fail(f"retail attached-services primary source changed: {key}")
        if row["status"] != "boundary-confirmed":
            fail(f"retail attached-services status changed: {key}")
        if not resolve_source(RETAIL_ATTACHED_SERVICES, row["source_artifact"]).exists():
            fail(f"retail attached-services source missing: {row['source_artifact']}")


def verify_retail_attached_frontier() -> None:
    if not RETAIL_ATTACHED_FRONTIER.exists():
        fail(f"missing {RETAIL_ATTACHED_FRONTIER.relative_to(ROOT)}")
    with RETAIL_ATTACHED_FRONTIER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["company", "period", "attached_service_pool_musd", "conversion_rate_pct", "mechanical_cash_frontier_musd", "denominator_cash_musd", "status", "source_artifact", "interpretation"]
        if reader.fieldnames != expected_header:
            fail(f"retail attached-frontier header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "Target": ("H1 2026", "1141", "4519"),
        "Walmart": ("H1 FY2027", "3855", "19710"),
    }
    if len(rows) != 10:
        fail(f"retail attached-frontier must contain 10 rows, found {len(rows)}")
    for row in rows:
        period, pool, denominator = expected.get(row["company"], (None, None, None))
        if period is None or row["period"] != period or row["attached_service_pool_musd"] != pool or row["denominator_cash_musd"] != denominator:
            fail(f"retail attached-frontier input changed: {row}")
        rate = float(row["conversion_rate_pct"])
        expected_cash = float(pool) * rate / 100
        if not math.isclose(float(row["mechanical_cash_frontier_musd"]), expected_cash, rel_tol=0, abs_tol=0.001):
            fail(f"retail attached-frontier arithmetic failed: {row}")
        if row["status"] != "sensitivity-only":
            fail(f"retail attached-frontier status changed: {row}")
        if not resolve_source(RETAIL_ATTACHED_FRONTIER, row["source_artifact"]).exists():
            fail(f"retail attached-frontier source missing: {row['source_artifact']}")


def verify_retail_attached_denominator_reconciliation() -> None:
    """Keep Walmart consolidated and segment attached-income denominators distinct."""
    if not RETAIL_ATTACHED_DENOMINATOR_RECONCILIATION.exists():
        fail(f"missing Walmart attached-income reconciliation: {RETAIL_ATTACHED_DENOMINATOR_RECONCILIATION.relative_to(ROOT)}")
    with RETAIL_ATTACHED_DENOMINATOR_RECONCILIATION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "reconciliation_id", "denominator_basis", "period", "amount_musd",
            "components_or_formula", "status", "what_is_proven", "what_is_not_proven",
            "next_required_source",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Walmart attached-income reconciliation header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {"WAI-001": ("consolidated", "3904"), "WAI-002": ("segment-subtotal", "3855"), "WAI-003": ("unreconciled-difference", "49")}
    if len(rows) != 3 or {row["reconciliation_id"] for row in rows} != set(expected):
        fail("Walmart attached-income reconciliation row set changed")
    for row in rows:
        basis, amount = expected[row["reconciliation_id"]]
        if row["denominator_basis"] != basis or row["amount_musd"] != amount:
            fail(f"Walmart attached-income denominator changed: {row['reconciliation_id']}")
        if not row["what_is_not_proven"].strip() or not row["next_required_source"].strip():
            fail(f"Walmart attached-income boundary is incomplete: {row['reconciliation_id']}")
    if int(expected["WAI-001"][1]) - int(expected["WAI-002"][1]) != int(expected["WAI-003"][1]):
        fail("Walmart attached-income denominator difference does not reconcile")


def verify_retail_cohort_matrix() -> None:
    if not RETAIL_COHORT_MATRIX.exists():
        fail(f"missing {RETAIL_COHORT_MATRIX.relative_to(ROOT)}")
    with RETAIL_COHORT_MATRIX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["company", "period", "metric", "value", "unit", "source_artifact", "status", "what_is_proven", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"retail cohort matrix header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        ("TJX", "Comparable sales growth"): "6",
        ("TJX", "Revenue"): "14300",
        ("Target", "Comparable sales growth"): "3.8",
        ("Target", "Traffic growth"): "3.6",
        ("Target", "Non-merchandise sales growth"): "20.1",
        ("Walmart U.S.", "Comparable sales growth"): "3.8",
        ("Walmart U.S.", "eCommerce sales"): "56400",
        ("Sam's Club U.S.", "Comparable sales growth"): "7.3",
    }
    if len(rows) != len(expected):
        fail("retail cohort matrix rows changed unexpectedly")
    for row in rows:
        key = (row["company"], row["metric"])
        if key not in expected or row["value"] != expected[key]:
            fail(f"retail cohort matrix row changed: {key}")
        if row["status"] != "primary-source-confirmed":
            fail(f"retail cohort matrix status changed: {key}")
        if not resolve_source(RETAIL_COHORT_MATRIX, row["source_artifact"]).exists():
            fail(f"retail cohort matrix source missing: {row['source_artifact']}")


def verify_retail_common_period_cash() -> None:
    if not RETAIL_COMMON_PERIOD_CASH.exists():
        fail(f"missing {RETAIL_COMMON_PERIOD_CASH.relative_to(ROOT)}")
    with RETAIL_COMMON_PERIOD_CASH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["company", "period", "net_sales_musd", "operating_cash_flow_musd", "property_spending_musd", "cash_after_property_musd", "cash_after_property_pct_sales", "gross_margin_pct", "gross_margin_basis", "temporary_gross_profit_support_musd", "gross_margin_ex_support_pct", "support_basis", "diluted_shares_millions", "mechanical_cash_per_share_usd", "status", "source_artifact", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"retail common-period cash header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("29503", "3345", "1159", "2186", "7.409416", "32.376369", "331", "31.254449", "1.955278"),
        "Target": ("51982", "4519", "2404", "2115", "4.068716", "31.4", "994", "29.479435", "4.636125"),
        "Walmart": ("361784", "19710", "14181", "5529", "1.528260", "24.9", "2900", "24.053579", "0.691828"),
    }
    if len(rows) != 3 or {row["company"] for row in rows} != set(expected):
        fail("retail common-period cash rows changed unexpectedly")
    for row in rows:
        values = expected[row["company"]]
        if tuple(row[field] for field in ("net_sales_musd", "operating_cash_flow_musd", "property_spending_musd", "cash_after_property_musd", "cash_after_property_pct_sales", "gross_margin_pct", "temporary_gross_profit_support_musd", "gross_margin_ex_support_pct", "mechanical_cash_per_share_usd")) != values:
            fail(f"retail common-period cash row changed: {row['company']}")
        if not row["gross_margin_basis"].strip():
            fail(f"retail gross-margin basis missing: {row['company']}")
        if not row["support_basis"].strip():
            fail(f"retail gross-margin support basis missing: {row['company']}")
        sales = number(row, "net_sales_musd")
        cash_after = number(row, "cash_after_property_musd")
        if not math.isclose(cash_after / sales * 100, number(row, "cash_after_property_pct_sales"), abs_tol=0.000001):
            fail(f"retail common-period cash intensity does not reconcile: {row['company']}")
        if row["status"] != "reported-denominator-screen":
            fail(f"retail common-period cash status changed: {row['company']}")
        if not resolve_source(RETAIL_COMMON_PERIOD_CASH, row["source_artifact"]).exists():
            fail(f"retail common-period cash source missing: {row['source_artifact']}")


def verify_retail_margin_working_capital() -> None:
    if not RETAIL_MARGIN_WORKING_CAPITAL.exists():
        fail(f"missing {RETAIL_MARGIN_WORKING_CAPITAL.relative_to(ROOT)}")
    with RETAIL_MARGIN_WORKING_CAPITAL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["company", "period", "operating_cash_flow_musd", "inventory_cash_signal_musd", "accounts_payable_cash_signal_musd", "supplier_finance_obligation_musd", "temporary_support_screen_musd", "gross_margin_pct", "gross_margin_basis", "gross_margin_ex_support_pct", "support_basis", "status", "source_artifact", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"retail margin working-capital header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("3345", "603", "470", "", "750", "32.376369", "31.254449"),
        "Target": ("4519", "", "612", "3200", "1364", "31.4", "29.479435"),
        "Walmart": ("19710", "2660", "1648", "6400", "4548", "24.9", "24.053579"),
    }
    if len(rows) != 3 or {row["company"] for row in rows} != set(expected):
        fail("retail margin working-capital rows changed unexpectedly")
    fields = ("operating_cash_flow_musd", "inventory_cash_signal_musd", "accounts_payable_cash_signal_musd", "supplier_finance_obligation_musd", "temporary_support_screen_musd", "gross_margin_pct", "gross_margin_ex_support_pct")
    for row in rows:
        if tuple(row[field] for field in fields) != expected[row["company"]]:
            fail(f"retail margin working-capital row changed: {row['company']}")
        for field in ("gross_margin_pct", "gross_margin_ex_support_pct"):
            number(row, field)
        for field in ("gross_margin_basis", "support_basis"):
            if not row[field].strip():
                fail(f"retail margin working-capital basis missing: {row['company']}")
        if row["status"] != "normalization-input":
            fail(f"retail margin working-capital status changed: {row['company']}")
        if not resolve_source(RETAIL_MARGIN_WORKING_CAPITAL, row["source_artifact"]).exists():
            fail(f"retail margin working-capital source missing: {row['source_artifact']}")


def verify_retail_capex_classification() -> None:
    if not RETAIL_CAPEX_CLASSIFICATION.exists():
        fail(f"missing {RETAIL_CAPEX_CLASSIFICATION.relative_to(ROOT)}")
    with RETAIL_CAPEX_CLASSIFICATION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["company", "period", "total_capex_musd", "disclosed_category_evidence", "maintenance_split_status", "source_artifact", "what_is_proven", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"retail capex-classification header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 3 or {(row["company"], row["period"]) for row in rows} != {("TJX", "H1 FY2027"), ("Target", "H1 2026"), ("Walmart", "H1 FY2027")}:
        fail("retail capex-classification rows changed unexpectedly")
    expected_totals = {"TJX": "1159", "Target": "2404", "Walmart": "14181"}
    for row in rows:
        if row["total_capex_musd"] != expected_totals[row["company"]]:
            fail(f"retail capex total changed for {row['company']}")
        if row["maintenance_split_status"] not in {"not-quantified", "not-disclosed"}:
            fail(f"retail capex split status overclaims for {row['company']}")
        for field in ("disclosed_category_evidence", "what_is_proven", "missing_upgrade"):
            if not row[field].strip():
                fail(f"retail capex row incomplete for {row['company']}")
        if not resolve_source(RETAIL_CAPEX_CLASSIFICATION, row["source_artifact"]).exists():
            fail(f"retail capex source missing: {row['source_artifact']}")
    memo = TJX_CAPEX_CLASSIFICATION.read_text(encoding="utf-8")
    for marker in ("Q-05 promotion surface", "$6.616B", "annual plan cannot be prorated"):
        if marker not in memo:
            fail(f"retail capex promotion-surface marker missing: {marker}")
    if not RETAIL_KNOWN_GROWTH_FRONTIER.exists():
        fail(f"missing retail known-growth frontier: {RETAIL_KNOWN_GROWTH_FRONTIER.relative_to(ROOT)}")
    growth_memo = RETAIL_KNOWN_GROWTH_FRONTIER.read_text(encoding="utf-8")
    for marker in ("24` year-to-date", "unit-count control", "$2.4B` H1 deployment", "not a dollar maintenance/growth allocation"):
        if marker not in growth_memo:
            fail(f"retail known-growth frontier marker missing: {marker}")
    if not RETAIL_H1_DENOMINATOR_HANDOFF.exists():
        fail(f"missing retail H1 denominator handoff: {RETAIL_H1_DENOMINATOR_HANDOFF.relative_to(ROOT)}")
    with RETAIL_H1_DENOMINATOR_HANDOFF.open(newline="", encoding="utf-8") as handle:
        handoff_rows = {row["company"]: row for row in csv.DictReader(handle)}
    expected_growth_floors = {"TJX": "222", "Target": "0", "Walmart": "1087"}
    if set(handoff_rows) != set(expected_growth_floors):
        fail("retail H1 denominator handoff company set changed unexpectedly")
    for company, growth_floor in expected_growth_floors.items():
        row = handoff_rows[company]
        if row["identified_growth_floor_musd"] != growth_floor:
            fail(f"retail identified growth floor changed for {company}")
        if row["promotion_status"] != "hold":
            fail(f"retail H1 denominator handoff over-promoted {company}")
    if not RETAIL_KNOWN_GROWTH_FRONTIER_DATA.exists():
        fail(f"missing retail known-growth frontier ledger: {RETAIL_KNOWN_GROWTH_FRONTIER_DATA.relative_to(ROOT)}")
    with RETAIL_KNOWN_GROWTH_FRONTIER_DATA.open(newline="", encoding="utf-8") as handle:
        frontier_rows = {row["company"]: row for row in csv.DictReader(handle)}
    expected_frontier = {
        "TJX": (3345, 1159, 2186, 222, 937, 2408),
        "Target": (4519, 2404, 2115, 0, 2404, 2115),
        "Walmart": (19710, 14181, 5529, 1087, 13094, 6616),
    }
    if set(frontier_rows) != set(expected_frontier):
        fail("retail known-growth frontier ledger company set changed unexpectedly")
    frontier_fields = ("operating_cash_musd", "property_spending_musd", "cash_after_property_musd", "disclosed_growth_floor_musd", "unallocated_property_remainder_musd", "optimistic_residual_after_unallocated_musd")
    for company, expected_values in expected_frontier.items():
        row = frontier_rows[company]
        if tuple(int(row[field]) for field in frontier_fields) != expected_values:
            fail(f"retail known-growth frontier arithmetic changed for {company}")
        if row["status"] != "allocation-sensitivity-only":
            fail(f"retail known-growth frontier over-promoted {company}")
        if not resolve_source(RETAIL_KNOWN_GROWTH_FRONTIER_DATA, row["source_artifact"]).exists():
            fail(f"retail known-growth frontier source missing: {row['source_artifact']}")


def verify_retail_promotion_action_register() -> None:
    if not RETAIL_PROMOTION_ACTIONS.exists():
        fail(f"missing retail promotion action register: {RETAIL_PROMOTION_ACTIONS.relative_to(ROOT)}")
    expected_header = [
        "queue_id", "pilot", "current_status", "current_evidence_artifact", "required_source", "period_or_denominator",
        "join_fields", "promotion_test", "blocked_by", "source_artifact",
    ]
    with RETAIL_PROMOTION_ACTIONS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail promotion action header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 3 or {row["queue_id"] for row in rows} != {"Q-04", "Q-05", "Q-06"}:
        fail("retail promotion action register rows changed unexpectedly")
    for row in rows:
        if row["pilot"] != "Retail cohort" or row["current_status"] != "partial":
            fail(f"retail promotion action status changed: {row['queue_id']}")
        for field in expected_header[3:9]:
            if not row[field].strip():
                fail(f"retail promotion action field missing: {row['queue_id']} {field}")
        if not resolve_source(RETAIL_PROMOTION_ACTIONS, row["current_evidence_artifact"]).exists():
            fail(f"retail current evidence source missing: {row['current_evidence_artifact']}")
        if not resolve_source(RETAIL_PROMOTION_ACTIONS, row["source_artifact"]).exists():
            fail(f"retail promotion action source missing: {row['source_artifact']}")
    memo = PILOT_DIR / "combined-investment-research-pilot-02-retail-owner-cash-promotion-rule.md"
    text = memo.read_text(encoding="utf-8")
    for marker in ("Q-04–Q-06 promotion action register", "settlement-date working-capital reconciliation", "maintenance-versus-growth", "service-level collection"):
        if marker not in text:
            fail(f"retail promotion action memo marker missing: {marker}")


def verify_tjx_maintenance_expense_boundary() -> None:
    ledger = PILOT_LEDGERS[1]
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = {row["gate_id"]: row for row in csv.DictReader(handle)}
    row = rows.get("AVP-053")
    if row is None:
        fail("TJX maintenance-expense ledger gate is missing")
    if row["current_status"] != "maintenance-expense-boundary-confirmed":
        fail("TJX maintenance-expense boundary overclaims or changed")
    if row["source_artifact"] != "analysis/company-first-principles/combined-investment-research-pilot-02-retail-capex-classification.md":
        fail("TJX maintenance-expense boundary source changed")
    source = resolve_source(ledger, row["source_artifact"])
    if not source.exists():
        fail("TJX maintenance-expense boundary source is missing")
    text = source.read_text(encoding="utf-8")
    for marker in (
        "maintenance and repairs are charged to",
        "expense as incurred",
        "does not establish that",
        "renovations or improvements are all growth capital",
        "H1 FY2027",
        "maintenance-versus-growth allocation therefore remains unresolved",
    ):
        if marker not in text:
            fail(f"TJX maintenance-expense boundary marker missing: {marker}")


def verify_retail_capex_boundary_overlay() -> None:
    if not RETAIL_CAPEX_BOUNDARY_OVERLAY.exists():
        fail(f"missing {RETAIL_CAPEX_BOUNDARY_OVERLAY.relative_to(ROOT)}")
    with RETAIL_CAPEX_BOUNDARY_OVERLAY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "overlay_id", "company", "period", "operating_cash_flow_musd",
            "total_capex_musd", "identified_growth_capex_musd",
            "implied_maintenance_ceiling_musd", "ocf_less_implied_maintenance_musd",
            "status", "source_artifact", "remaining_claims",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail capex boundary-overlay header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 1:
        fail(f"retail capex boundary overlay must contain 1 row, found {len(rows)}")
    row = rows[0]
    expected = {
        "company": "Walmart", "period": "H1 FY2027",
        "operating_cash_flow_musd": "19710", "total_capex_musd": "14181",
        "identified_growth_capex_musd": "1087", "implied_maintenance_ceiling_musd": "13094",
        "ocf_less_implied_maintenance_musd": "6616",
    }
    for field, value in expected.items():
        if row[field] != value:
            fail(f"retail capex boundary overlay changed: {field}={row[field]}")
    if int(row["implied_maintenance_ceiling_musd"]) != int(row["total_capex_musd"]) - int(row["identified_growth_capex_musd"]):
        fail(f"retail capex boundary maintenance arithmetic failed: {row}")
    if int(row["ocf_less_implied_maintenance_musd"]) != int(row["operating_cash_flow_musd"]) - int(row["implied_maintenance_ceiling_musd"]):
        fail(f"retail capex boundary cash arithmetic failed: {row}")
    if row["status"] != "qualified-classification-boundary":
        fail(f"retail capex boundary status changed: {row}")
    if not resolve_source(RETAIL_CAPEX_BOUNDARY_OVERLAY, row["source_artifact"]).exists():
        fail(f"retail capex boundary source missing: {row['source_artifact']}")


def verify_retail_post_financing_residual() -> None:
    if not RETAIL_POST_FINANCING_RESIDUAL.exists():
        fail(f"missing {RETAIL_POST_FINANCING_RESIDUAL.relative_to(ROOT)}")
    with RETAIL_POST_FINANCING_RESIDUAL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "screen_id", "queue_id", "company", "period", "cash_after_property_musd",
            "support_candidate_musd", "sbc_sensitivity_musd", "debt_principal_repayment_musd",
            "reported_residual_musd", "support_removed_residual_musd", "support_sbc_residual_musd",
            "support_sbc_debt_residual_musd", "status", "source_artifact", "remaining_claims",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail post-financing residual header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("H1 FY2027", "2186", "750", "85", "0", "2186", "1436", "1351", "1351"),
        "Target": ("H1 2026", "2115", "1364", "154", "1070", "2115", "751", "597", "-473"),
        "Walmart": ("H1 FY2027", "5529", "4548", "NA", "2303", "5529", "981", "NA", "-1322"),
    }
    if len(rows) != 3 or {row["company"] for row in rows} != set(expected):
        fail("retail post-financing residual rows changed unexpectedly")
    for row in rows:
        values = expected[row["company"]]
        fields = ("period", "cash_after_property_musd", "support_candidate_musd", "sbc_sensitivity_musd", "debt_principal_repayment_musd", "reported_residual_musd", "support_removed_residual_musd", "support_sbc_residual_musd", "support_sbc_debt_residual_musd")
        if tuple(row[field] for field in fields) != values:
            fail(f"retail post-financing residual changed: {row['company']}")
        cash = int(row["cash_after_property_musd"])
        support = int(row["support_candidate_musd"])
        debt = int(row["debt_principal_repayment_musd"])
        if int(row["reported_residual_musd"]) != cash or int(row["support_removed_residual_musd"]) != cash - support:
            fail(f"retail post-financing reported/support arithmetic failed: {row}")
        if row["sbc_sensitivity_musd"] != "NA":
            sbc = int(row["sbc_sensitivity_musd"])
            if int(row["support_sbc_residual_musd"]) != cash - support - sbc:
                fail(f"retail post-financing SBC arithmetic failed: {row}")
            if int(row["support_sbc_debt_residual_musd"]) != cash - support - sbc - debt:
                fail(f"retail post-financing debt arithmetic failed: {row}")
        elif row["support_sbc_residual_musd"] != "NA":
            fail(f"retail post-financing NA sensitivity changed: {row}")
        if row["status"] != "source-bounded-post-financing-residual":
            fail(f"retail post-financing status changed: {row}")
        if not row["remaining_claims"].strip() or not resolve_source(RETAIL_POST_FINANCING_RESIDUAL, row["source_artifact"]).exists():
            fail(f"retail post-financing row incomplete: {row}")


def verify_walmart_cash_denominator() -> None:
    if not WALMART_CASH_DENOMINATOR.exists():
        fail(f"missing {WALMART_CASH_DENOMINATOR.relative_to(ROOT)}")
    expected_header = [
        "claim_id", "period", "topic", "value", "evidence_grade",
        "what_is_proven", "what_is_not_proven", "source_artifact", "next_test",
    ]
    with WALMART_CASH_DENOMINATOR.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Walmart cash-denominator header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {f"WMT-CASH-{index:03d}" for index in range(1, 10)}
    if len(rows) != 9 or {row["claim_id"] for row in rows} != expected_ids:
        fail("Walmart cash-denominator claims changed unexpectedly")
    expected_grades = {
        "WMT-CASH-001": "filed-and-reconciled",
        "WMT-CASH-002": "category-visible",
        "WMT-CASH-003": "filed-and-reconciled",
        "WMT-CASH-004": "filed-and-reconciled-separate-use",
        "WMT-CASH-005": "filed-and-reconciled",
        "WMT-CASH-006": "owner-cash-boundary-held",
        "WMT-CASH-007": "balance-visible-cash-open",
        "WMT-CASH-008": "provision-visible-cash-paid-open",
        "WMT-CASH-009": "category-visible-historical",
    }
    for row in rows:
        if row["evidence_grade"] != expected_grades[row["claim_id"]]:
            fail(f"Walmart cash-denominator evidence grade changed: {row['claim_id']}")
        for field in ("what_is_proven", "what_is_not_proven", "next_test"):
            if not row[field].strip():
                fail(f"Walmart cash-denominator row missing {field}: {row['claim_id']}")
        if not resolve_source(WALMART_CASH_DENOMINATOR, row["source_artifact"]).exists():
            fail(f"Walmart cash-denominator source missing: {row['source_artifact']}")


def verify_target_cash_denominator() -> None:
    if not TARGET_CASH_DENOMINATOR.exists():
        fail(f"missing {TARGET_CASH_DENOMINATOR.relative_to(ROOT)}")
    expected_header = [
        "claim_id", "period", "topic", "value", "evidence_grade",
        "what_is_proven", "what_is_not_proven", "source_artifact", "next_test",
    ]
    with TARGET_CASH_DENOMINATOR.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Target cash-denominator header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {f"TGT-CASH-{index:03d}" for index in range(1, 9)}
    if len(rows) != 8 or {row["claim_id"] for row in rows} != expected_ids:
        fail("Target cash-denominator claims changed unexpectedly")
    expected_grades = {
        "TGT-CASH-001": "filed-and-reconciled",
        "TGT-CASH-002": "filed-and-reconciled-separate-uses",
        "TGT-CASH-003": "filed-and-reconciled",
        "TGT-CASH-004": "filed-and-reconciled",
        "TGT-CASH-005": "dependency-visible",
        "TGT-CASH-006": "owner-cash-boundary-held",
        "TGT-CASH-007": "balance-and-roic-burden-visible",
        "TGT-CASH-008": "provision-visible-cash-paid-open",
    }
    for row in rows:
        if row["evidence_grade"] != expected_grades[row["claim_id"]]:
            fail(f"Target cash-denominator evidence grade changed: {row['claim_id']}")
        for field in ("what_is_proven", "what_is_not_proven", "next_test"):
            if not row[field].strip():
                fail(f"Target cash-denominator row missing {field}: {row['claim_id']}")
        if not resolve_source(TARGET_CASH_DENOMINATOR, row["source_artifact"]).exists():
            fail(f"Target cash-denominator source missing: {row['source_artifact']}")


def verify_target_gift_card_boundary() -> None:
    if not TARGET_GIFT_CARD_BOUNDARY.exists():
        fail(f"missing Target gift-card boundary: {TARGET_GIFT_CARD_BOUNDARY.relative_to(ROOT)}")
    with TARGET_GIFT_CARD_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "observation_id", "period", "beginning_liability_musd", "issued_musd",
            "revenue_recognized_from_beginning_musd", "ending_liability_musd", "status",
            "what_is_proven", "what_is_not_proven", "source_artifact", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Target gift-card header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 1 or rows[0]["observation_id"] != "TGT-GC-001":
        fail("Target gift-card boundary must contain TGT-GC-001 only")
    row = rows[0]
    expected = {
        "beginning_liability_musd": 1197.0,
        "issued_musd": 376.0,
        "revenue_recognized_from_beginning_musd": 614.0,
        "ending_liability_musd": 959.0,
    }
    if row["status"] != "gift-card-timing-boundary-confirmed":
        fail("Target gift-card boundary is over-promoted")
    for field, value in expected.items():
        if not math.isclose(float(row[field]), value, abs_tol=0.001):
            fail(f"Target gift-card value changed: {field}")
    if not math.isclose(expected["beginning_liability_musd"] + expected["issued_musd"] - expected["revenue_recognized_from_beginning_musd"], expected["ending_liability_musd"], abs_tol=0.001):
        fail("Target gift-card liability roll-forward does not reconcile")
    if not resolve_source(TARGET_GIFT_CARD_BOUNDARY, row["source_artifact"]).exists():
        fail(f"Target gift-card source missing: {row['source_artifact']}")
    for field in ("period", "what_is_proven", "what_is_not_proven", "next_upgrade"):
        if not row[field].strip():
            fail(f"Target gift-card row incomplete: {field}")


def verify_retail_cohort_cash_denominator() -> None:
    if not RETAIL_COHORT_CASH_DENOMINATOR.exists():
        fail(f"missing {RETAIL_COHORT_CASH_DENOMINATOR.relative_to(ROOT)}")
    expected_header = [
        "company", "period", "cash_after_property_musd", "support_candidate_musd",
        "sbc_sensitivity_musd", "debt_principal_repayment_musd",
        "stacked_burden_residual_musd", "denominator_grade", "source_artifact", "next_upgrade",
    ]
    with RETAIL_COHORT_CASH_DENOMINATOR.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail cohort denominator header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("H1 FY2027", 2186, 750, 85, 0, 1351, "source-bounded-residual"),
        "Target": ("H1 2026", 2115, 1364, 154, 1070, -473, "source-bounded-residual"),
        "Walmart": ("H1 FY2027", 5529, 4548, None, 2303, -1322, "source-bounded-residual-sbc-unavailable"),
    }
    if len(rows) != 3 or {row["company"] for row in rows} != set(expected):
        fail("retail cohort denominator rows changed unexpectedly")
    for row in rows:
        period, cash, support, sbc, debt, residual, grade = expected[row["company"]]
        if row["period"] != period or row["denominator_grade"] != grade:
            fail(f"retail cohort denominator status changed: {row}")
        for field, value in (("cash_after_property_musd", cash), ("support_candidate_musd", support), ("debt_principal_repayment_musd", debt), ("stacked_burden_residual_musd", residual)):
            if int(row[field]) != value:
                fail(f"retail cohort denominator value changed: {row}")
        if sbc is None:
            if row["sbc_sensitivity_musd"] != "NA":
                fail(f"retail cohort Walmart SBC boundary changed: {row}")
        elif int(row["sbc_sensitivity_musd"]) != sbc:
            fail(f"retail cohort SBC value changed: {row}")
        if sbc is None:
            if int(row["stacked_burden_residual_musd"]) != cash - support - debt:
                fail(f"retail cohort Walmart residual arithmetic failed: {row}")
        elif int(row["stacked_burden_residual_musd"]) != cash - support - sbc - debt:
            fail(f"retail cohort residual arithmetic failed: {row}")
        if not row["next_upgrade"].strip() or not resolve_source(RETAIL_COHORT_CASH_DENOMINATOR, row["source_artifact"]).exists():
            fail(f"retail cohort denominator row incomplete: {row}")


def verify_retail_capex_sensitivity() -> None:
    if not RETAIL_CAPEX_SENSITIVITY.exists():
        fail(f"missing {RETAIL_CAPEX_SENSITIVITY.relative_to(ROOT)}")
    with RETAIL_CAPEX_SENSITIVITY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "company", "period", "operating_cash_flow_musd",
            "total_property_spending_musd", "zero_percent_maintenance_cash_musd",
            "fifty_percent_maintenance_cash_musd", "one_hundred_percent_maintenance_cash_musd",
            "status", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail capex sensitivity header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("3345", "1159", "3345", "2765.5", "2186"),
        "Target": ("4519", "2404", "4519", "3317", "2115"),
        "Walmart": ("19710", "14181", "19710", "12619.5", "5529"),
    }
    if len(rows) != 3 or {row["company"] for row in rows} != set(expected):
        fail("retail capex sensitivity rows changed unexpectedly")
    fields = (
        "operating_cash_flow_musd", "total_property_spending_musd",
        "zero_percent_maintenance_cash_musd", "fifty_percent_maintenance_cash_musd",
        "one_hundred_percent_maintenance_cash_musd",
    )
    for row in rows:
        if tuple(row[field] for field in fields) != expected[row["company"]]:
            fail(f"retail capex sensitivity changed: {row['company']}")
        if row["status"] != "capex-boundary-screen":
            fail(f"retail capex sensitivity status changed: {row['company']}")
        if not resolve_source(RETAIL_CAPEX_SENSITIVITY, row["source_artifact"]).exists():
            fail(f"retail capex sensitivity source missing: {row['source_artifact']}")


def verify_retail_capex_public_refresh() -> None:
    expected_header = [
        "refresh_id", "queue_id", "company", "period", "observed_capex_or_category",
        "what_is_proven", "missing_upgrade", "result_class", "primary_source_url",
        "source_artifact",
    ]
    with RETAIL_CAPEX_PUBLIC_REFRESH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail capex public-refresh header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = ["RCX-001", "RCX-002", "RCX-003", "RCX-004", "RCX-005", "RCX-006"]
    if [row.get("refresh_id") for row in rows] != expected_ids:
        fail("retail capex public-refresh rows changed unexpectedly")
    expected_urls = {
        "RCX-001": "https://investor.tjx.com/node/21541/html",
        "RCX-002": "https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm",
        "RCX-003": "https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000154/wmt-20260731.htm",
        "RCX-004": "https://corporate.target.com/news-features/article/2026/05/target-store-remodels-new-stores-strategy",
        "RCX-005": "https://stock.walmart.com/_assets/_ef4b3350ef1127ae63b1dd51abb6cf31/walmart/db/950/9988/annual_report/Walmart%2B2026%2BAnnual%2BReport.pdf",
        "RCX-006": "https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm",
    }
    for row in rows:
        if row["result_class"] != "evidence-insufficient":
            fail(f"retail capex public refresh over-promoted: {row['refresh_id']}")
        if row["primary_source_url"] != expected_urls[row["refresh_id"]]:
            fail(f"retail capex public-refresh source changed: {row['refresh_id']}")
        if not row["missing_upgrade"].strip():
            fail(f"retail capex public-refresh missing upgrade: {row['refresh_id']}")
        if not resolve_source(RETAIL_CAPEX_PUBLIC_REFRESH, row["source_artifact"]).exists():
            fail(f"retail capex public-refresh source artifact missing: {row['source_artifact']}")


def verify_retail_attached_services_public_refresh() -> None:
    expected_header = [
        "refresh_id", "queue_id", "company", "period", "observed_service_evidence",
        "what_is_proven", "missing_upgrade", "result_class", "primary_source_url",
        "source_artifact",
    ]
    with RETAIL_ATTACHED_SERVICES_PUBLIC_REFRESH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail attached-services refresh header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = ["RAS-001", "RAS-002", "RAS-003", "RAS-004", "RAS-005"]
    if [row.get("refresh_id") for row in rows] != expected_ids:
        fail("retail attached-services refresh rows changed unexpectedly")
    expected_urls = {
        "RAS-001": "https://corporate.target.com/press/release/2026/08/target-corporation-reports-second-quarter-earnings",
        "RAS-002": "https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000154/wmt-20260731.htm",
        "RAS-003": "https://investor.tjx.com/node/21541/html",
        "RAS-004": "https://corporate.target.com/investors/annual/2025-annual-report/10-k-report/10-k-part-ii/item-8-financial-statements-and-supplementary-data",
        "RAS-005": "https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000055/wmt-20260131.htm",
    }
    for row in rows:
        if row["result_class"] != "evidence-insufficient":
            fail(f"retail attached-services refresh over-promoted: {row['refresh_id']}")
        if row["primary_source_url"] != expected_urls[row["refresh_id"]]:
            fail(f"retail attached-services refresh source changed: {row['refresh_id']}")
        if not row["missing_upgrade"].strip():
            fail(f"retail attached-services refresh missing upgrade: {row['refresh_id']}")
        if not resolve_source(RETAIL_ATTACHED_SERVICES_PUBLIC_REFRESH, row["source_artifact"]).exists():
            fail(f"retail attached-services refresh source artifact missing: {row['source_artifact']}")


def verify_retail_per_share_cash() -> None:
    if not RETAIL_PER_SHARE.exists():
        fail(f"missing {RETAIL_PER_SHARE.relative_to(ROOT)}")
    with RETAIL_PER_SHARE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_PER_SHARE_HEADER:
            fail(f"retail per-share header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 3 or {row["company"] for row in rows} != {"TJX", "Target", "Walmart"}:
        fail("retail per-share table must contain one row for each cohort company")
    for row in rows:
        source = resolve_source(RETAIL_PER_SHARE, row["source_artifact"])
        if not source.exists():
            fail(f"retail per-share source missing: {row['source_artifact']}")
        cash = number(row, "cash_after_property_musd")
        shares = number(row, "diluted_shares_millions")
        lease = number(row, "operating_lease_liabilities_musd")
        per_share = number(row, "reported_cash_after_property_per_share_usd")
        if shares <= 0 or lease < 0:
            fail(f"{row['company']} retail per-share inputs are invalid")
        if not math.isclose(per_share, cash / shares, abs_tol=0.0001):
            fail(f"{row['company']} reported cash per diluted share does not reconcile")


def verify_retail_stacked_residual_per_share() -> None:
    if not RETAIL_STACKED_RESIDUAL_PER_SHARE.exists():
        fail(f"missing {RETAIL_STACKED_RESIDUAL_PER_SHARE.relative_to(ROOT)}")
    with RETAIL_STACKED_RESIDUAL_PER_SHARE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_STACKED_RESIDUAL_PER_SHARE_HEADER:
            fail(f"retail stacked residual per-share header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        ("TJX", "H1 FY2027"): (1118, 2186, 1351),
        ("Target", "H1 2026"): (456.2, 2115, -473),
        ("Walmart", "H1 FY2027"): (7989, 5529, -1322),
    }
    if len(rows) != len(expected) or {(row["company"], row["period"]) for row in rows} != set(expected):
        fail("retail stacked residual per-share table must contain the three expected cohort rows")
    for row in rows:
        key = (row["company"], row["period"])
        if row["status"] != "stress-sensitivity":
            fail(f"{row['company']} {row['period']} stacked residual is over-promoted")
        source = resolve_source(RETAIL_STACKED_RESIDUAL_PER_SHARE, row["source_artifact"])
        if not source.exists():
            fail(f"retail stacked residual source missing: {row['source_artifact']}")
        shares, reported, residual = expected[key]
        if not math.isclose(number(row, "diluted_shares_millions"), shares, abs_tol=0.001):
            fail(f"{row['company']} diluted-share denominator changed unexpectedly")
        if not math.isclose(number(row, "reported_cash_after_property_musd"), reported, abs_tol=0.001):
            fail(f"{row['company']} reported cash-after-property input changed unexpectedly")
        if not math.isclose(number(row, "stacked_residual_musd"), residual, abs_tol=0.001):
            fail(f"{row['company']} stacked residual input changed unexpectedly")
        calculated = residual / shares
        if not math.isclose(number(row, "stacked_residual_per_diluted_share_usd"), calculated, abs_tol=0.000001):
            fail(f"{row['company']} stacked residual per diluted share does not reconcile")


def verify_retail_annual_lease_tax_cash() -> None:
    if not RETAIL_ANNUAL_LEASE_TAX_CASH.exists():
        fail(f"missing {RETAIL_ANNUAL_LEASE_TAX_CASH.relative_to(ROOT)}")
    with RETAIL_ANNUAL_LEASE_TAX_CASH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_ANNUAL_LEASE_TAX_CASH_HEADER:
            fail(f"retail annual lease-tax header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        ("TJX", "FY2026"): (4917, 2214, 1471, 10620),
        ("Target", "FY2025"): (2835, 529, 1091, 3834),
        ("Walmart", "FY2026"): (14923, 2315, 5364, 15572),
    }
    if len(rows) != 3 or {(row["company"], row["period"]) for row in rows} != set(expected):
        fail("retail annual lease-tax table must contain the three expected rows")
    for row in rows:
        key = (row["company"], row["period"])
        if row["status"] != "annual-burden-visible":
            fail(f"retail annual lease-tax row over-promoted: {key}")
        source = resolve_source(RETAIL_ANNUAL_LEASE_TAX_CASH, row["source_artifact"])
        if not source.exists():
            fail(f"retail annual lease-tax source missing: {row['source_artifact']}")
        values = tuple(number(row, field) for field in (
            "cash_after_property_musd", "operating_lease_cash_paid_musd",
            "income_taxes_paid_musd", "operating_lease_liabilities_musd",
        ))
        if values != expected[key]:
            fail(f"retail annual lease-tax values changed unexpectedly: {key}")
        lease_ratio = number(row, "lease_cash_to_cash_after_property_pct")
        tax_ratio = number(row, "tax_cash_to_cash_after_property_pct")
        if not math.isclose(lease_ratio, values[1] / values[0] * 100, abs_tol=0.000001):
            fail(f"retail annual lease-cash ratio does not reconcile: {key}")
        if not math.isclose(tax_ratio, values[2] / values[0] * 100, abs_tol=0.000001):
            fail(f"retail annual tax-cash ratio does not reconcile: {key}")
        for field in ("what_is_proven", "what_is_not_proven", "next_upgrade"):
            if not row[field].strip():
                fail(f"retail annual lease-tax field missing: {key} {field}")
    memo = (PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("$2.214B", "$0.529B", "$2.315B", "$1.471B", "$1.091B", "$5.364B", "45.0%", "38.5%", "not additional deductions"):
        if marker not in memo:
            fail(f"retail annual lease-tax memo marker missing: {marker}")


def verify_retail_annual_cohort_denominator() -> None:
    if not RETAIL_ANNUAL_COHORT_DENOMINATOR.exists():
        fail(f"missing {RETAIL_ANNUAL_COHORT_DENOMINATOR.relative_to(ROOT)}")
    with RETAIL_ANNUAL_COHORT_DENOMINATOR.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_ANNUAL_COHORT_DENOMINATOR_HEADER:
            fail(f"retail annual cohort denominator header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        ("TJX", "FY2026"): (6874, 1957, 4917, 1128, 2214, 1471),
        ("Target", "FY2025"): (6562, 3727, 2835, 455.6, 529, 1091),
        ("Walmart", "FY2026"): (41565, 26642, 14923, 8022, 2315, 5364),
    }
    if len(rows) != 3 or {(row["company"], row["fiscal_period"]) for row in rows} != set(expected):
        fail("retail annual cohort denominator must contain the three expected rows")
    for row in rows:
        key = (row["company"], row["fiscal_period"])
        if row["status"] != "reported-not-normalized":
            fail(f"retail annual cohort denominator over-promoted: {key}")
        source = resolve_source(RETAIL_ANNUAL_COHORT_DENOMINATOR, row["source_artifact"])
        if not source.exists():
            fail(f"retail annual cohort denominator source missing: {row['source_artifact']}")
        ocf, property_spending, cash, shares, lease_cash, tax_cash = expected[key]
        observed = tuple(number(row, field) for field in (
            "operating_cash_flow_musd", "property_spending_musd",
            "cash_after_property_musd", "diluted_shares_millions",
            "operating_lease_cash_musd", "income_tax_cash_musd",
        ))
        if observed != (ocf, property_spending, cash, shares, lease_cash, tax_cash):
            fail(f"retail annual cohort denominator values changed unexpectedly: {key}")
        if cash != ocf - property_spending:
            fail(f"retail annual cohort cash-after-property arithmetic failed: {key}")
        per_share = number(row, "cash_after_property_per_diluted_share_usd")
        if not math.isclose(per_share, cash / shares, abs_tol=0.000001):
            fail(f"retail annual cohort per-share arithmetic failed: {key}")
        begin = row["supplier_finance_begin_musd"]
        end = row["supplier_finance_end_musd"]
        movement = row["supplier_finance_movement_musd"]
        if key == ("TJX", "FY2026"):
            if (begin, end, movement) != ("", "", ""):
                fail("TJX annual supplier-finance boundary changed unexpectedly")
        elif not (begin and end and movement) or not math.isclose(float(movement), float(end) - float(begin), abs_tol=0.001):
            fail(f"annual supplier-finance movement does not reconcile: {key}")
        if not row["next_upgrade"].strip():
            fail(f"retail annual cohort next-upgrade field missing: {key}")
    memo = (PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-cohort-denominator-control-2026-09-17.md").read_text(encoding="utf-8")
    for marker in ("cash-after-property", "reported-not-normalized", "not subtracted a second time", "-640", "+264"):
        if marker not in memo:
            fail(f"retail annual cohort denominator memo marker missing: {marker}")


def verify_retail_annual_attached_frontier() -> None:
    if not RETAIL_ANNUAL_ATTACHED_FRONTIER.exists():
        fail(f"missing {RETAIL_ANNUAL_ATTACHED_FRONTIER.relative_to(ROOT)}")
    with RETAIL_ANNUAL_ATTACHED_FRONTIER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_ANNUAL_ATTACHED_FRONTIER_HEADER:
            fail(f"retail annual attached frontier header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        ("Target", "FY2025"): 2063,
        ("Walmart", "FY2026"): 6750,
    }
    if len(rows) != 2 or {(row["company"], row["fiscal_period"]) for row in rows} != set(expected):
        fail("retail annual attached frontier must contain Target and Walmart annual rows")
    for row in rows:
        key = (row["company"], row["fiscal_period"])
        if row["status"] != "evidence-insufficient":
            fail(f"retail annual attached frontier over-promoted: {key}")
        source = resolve_source(RETAIL_ANNUAL_ATTACHED_FRONTIER, row["source_artifact"])
        if not source.exists():
            fail(f"retail annual attached frontier source missing: {row['source_artifact']}")
        pool = expected[key]
        if number(row, "reported_attached_service_pool_musd") != pool:
            fail(f"retail annual attached pool changed unexpectedly: {key}")
        conversion_fields = (
            "zero_percent_cash_musd", "twenty_five_percent_cash_musd",
            "fifty_percent_cash_musd", "seventy_five_percent_cash_musd",
            "one_hundred_percent_cash_musd",
        )
        expected_values = (0, pool * 0.25, pool * 0.5, pool * 0.75, pool)
        for field, expected_value in zip(conversion_fields, expected_values):
            if not math.isclose(number(row, field), expected_value, abs_tol=0.001):
                fail(f"retail annual attached frontier arithmetic failed: {key} {field}")
        if not row["next_upgrade"].strip():
            fail(f"retail annual attached frontier next-upgrade field missing: {key}")
    memo = (PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-attached-services-cash-frontier-2026-09-17.md").read_text(encoding="utf-8")
    for marker in ("$2.063B", "$6.750B", "Mechanical conversion frontier", "not owner-cash estimates", "evidence-insufficient"):
        if marker not in memo:
            fail(f"retail annual attached frontier memo marker missing: {marker}")


def verify_retail_annual_expectation_screen() -> None:
    if not RETAIL_ANNUAL_EXPECTATION_SCREEN.exists():
        fail(f"missing {RETAIL_ANNUAL_EXPECTATION_SCREEN.relative_to(ROOT)}")
    with RETAIL_ANNUAL_EXPECTATION_SCREEN.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_ANNUAL_EXPECTATION_SCREEN_HEADER:
            fail(f"retail annual expectation header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        ("TJX", "FY2026"): (137212, 4917),
        ("Target", "FY2025"): (70627, 2835),
        ("Walmart", "FY2026"): (857635, 14923),
    }
    if len(rows) != 3 or {(row["company"], row["fiscal_period"]) for row in rows} != set(expected):
        fail("retail annual expectation screen must contain the three expected rows")
    for row in rows:
        key = (row["company"], row["fiscal_period"])
        if row["status"] != "qualified-reported-cash-expectation-screen":
            fail(f"retail annual expectation screen over-promoted: {key}")
        source = resolve_source(RETAIL_ANNUAL_EXPECTATION_SCREEN, row["source_artifact"])
        if not source.exists():
            fail(f"retail annual expectation source missing: {row['source_artifact']}")
        market_cap, cash = expected[key]
        if number(row, "market_cap_musd") != market_cap or number(row, "reported_cash_after_property_musd") != cash:
            fail(f"retail annual expectation inputs changed unexpectedly: {key}")
        multiple = number(row, "market_cap_to_reported_cash_after_property_multiple")
        if not math.isclose(multiple, market_cap / cash, abs_tol=0.000001):
            fail(f"retail annual expectation multiple does not reconcile: {key}")
        if not row["next_upgrade"].strip():
            fail(f"retail annual expectation next-upgrade field missing: {key}")
    memo = (PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-reported-cash-expectation-screen-2026-09-17.md").read_text(encoding="utf-8")
    for marker in ("27.906x", "24.913x", "57.471x", "normalized owner-cash multiple, intrinsic value", "qualified-reported-cash-expectation-screen"):
        if marker not in memo:
            fail(f"retail annual expectation memo marker missing: {marker}")


def verify_retail_interim_lease_tax_search() -> None:
    if not RETAIL_INTERIM_LEASE_TAX_SEARCH.exists():
        fail(f"missing {RETAIL_INTERIM_LEASE_TAX_SEARCH.relative_to(ROOT)}")
    with RETAIL_INTERIM_LEASE_TAX_SEARCH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_INTERIM_LEASE_TAX_SEARCH_HEADER:
            fail(f"retail interim lease-tax header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "RITAX-001": ("TJX", "https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm"),
        "RITAX-002": ("Target", "https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm"),
        "RITAX-003": ("Walmart", "https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm"),
    }
    if [row["search_id"] for row in rows] != list(expected):
        fail("retail interim lease-tax search rows changed unexpectedly")
    for row in rows:
        company, url = expected[row["search_id"]]
        if row["company"] != company or row["source_url"] != url:
            fail(f"retail interim lease-tax source changed: {row['search_id']}")
        if row["search_id"] == "RITAX-001":
            if row["result_class"] != "lease-cash-visible; tax-cash-searched-negative":
                fail(f"retail interim TJX lease-tax status changed: {row['search_id']}")
            if row["dedicated_cash_lease_line"] != "$1.147B operating cash paid" or row["dedicated_cash_tax_line"] != "not located in checked 10-Q HTML":
                fail(f"retail interim TJX payment boundary changed: {row['search_id']}")
        else:
            if row["result_class"] != "searched-negative":
                fail(f"retail interim lease-tax search over-promoted: {row['search_id']}")
            if row["dedicated_cash_lease_line"] != "not located in checked 10-Q HTML or inline-XBRL facts" or row["dedicated_cash_tax_line"] != "not located in checked 10-Q HTML or inline-XBRL facts":
                fail(f"retail interim lease-tax negative boundary changed: {row['search_id']}")
        if not resolve_source(RETAIL_INTERIM_LEASE_TAX_SEARCH, row["source_artifact"]).exists():
            fail(f"retail interim lease-tax source artifact missing: {row['source_artifact']}")
        for field in ("interim_period", "observed_interim_context", "what_is_proven", "what_is_not_proven", "next_upgrade"):
            if not row[field].strip():
                fail(f"retail interim lease-tax field missing: {row['search_id']} {field}")


def verify_retail_interim_inline_xbrl_search() -> None:
    if not RETAIL_INTERIM_INLINE_XBRL_SEARCH.exists():
        fail(f"missing {RETAIL_INTERIM_INLINE_XBRL_SEARCH.relative_to(ROOT)}")
    with RETAIL_INTERIM_INLINE_XBRL_SEARCH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != RETAIL_INTERIM_INLINE_XBRL_SEARCH_HEADER:
            fail(f"retail inline-XBRL header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 4 or [row["tag_search_id"] for row in rows] != [f"RIXBRL-{index:03d}" for index in range(1, 5)]:
        fail("retail inline-XBRL search population changed")
    expected = {
        "RIXBRL-001": ("Target", "PaymentsOfIncomeTaxes"),
        "RIXBRL-002": ("Target", "OperatingLeasePayments"),
        "RIXBRL-003": ("Walmart", "PaymentsOfIncomeTaxes"),
        "RIXBRL-004": ("Walmart", "OperatingLeasePayments"),
    }
    for row in rows:
        company, tag = expected[row["tag_search_id"]]
        if row["company"] != company or row["tag_or_phrase"] != tag or row["result_class"] != "not-located":
            fail(f"retail inline-XBRL result changed: {row['tag_search_id']}")
        if row["searched_route"] != "SEC inline-XBRL HTML" or "cash" not in row["what_is_not_proven"]:
            fail(f"retail inline-XBRL boundary weakened: {row['tag_search_id']}")
        if not resolve_source(RETAIL_INTERIM_INLINE_XBRL_SEARCH, row["source_artifact"]).exists():
            fail(f"retail inline-XBRL source artifact missing: {row['source_artifact']}")


def verify_apollo_debt_solutions_coupon_carry() -> None:
    if not APOLLO_DEBT_SOLUTIONS_CARRY.exists():
        fail(f"missing {APOLLO_DEBT_SOLUTIONS_CARRY.relative_to(ROOT)}")
    with APOLLO_DEBT_SOLUTIONS_CARRY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != APOLLO_DEBT_SOLUTIONS_CARRY_HEADER:
            fail(f"Apollo Debt Solutions carry header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 1:
        fail("Apollo Debt Solutions carry sensitivity must contain one scenario row")
    row = rows[0]
    if row["scenario"] != "par-equivalent-candidate":
        fail("Apollo Debt Solutions carry scenario changed unexpectedly")
    if row["status"] != "illustrative-sensitivity":
        fail("Apollo Debt Solutions carry sensitivity is over-promoted")
    source = resolve_source(APOLLO_DEBT_SOLUTIONS_CARRY, row["source_artifact"])
    if not source.exists():
        fail(f"Apollo Debt Solutions carry source missing: {row['source_artifact']}")
    consideration = number(row, "consideration_musd")
    principal = number(row, "issue_principal_musd")
    share = number(row, "implied_issue_share_pct")
    coupon = number(row, "coupon_pct")
    annual = number(row, "annual_gross_carry_proxy_musd")
    five_year = number(row, "five_year_gross_carry_proxy_musd")
    if not math.isclose(consideration, 215.832, abs_tol=0.000001):
        fail("Apollo Debt Solutions carry consideration changed unexpectedly")
    if not math.isclose(principal, 600.0, abs_tol=0.000001):
        fail("Apollo Debt Solutions carry issue principal changed unexpectedly")
    if not math.isclose(share, consideration / principal * 100, abs_tol=0.0001):
        fail("Apollo Debt Solutions implied issue share does not reconcile")
    if not math.isclose(coupon, 6.7, abs_tol=0.000001):
        fail("Apollo Debt Solutions coupon changed unexpectedly")
    expected_annual = principal * coupon / 100 * share / 100
    if not math.isclose(annual, round(expected_annual, 3), abs_tol=0.000001):
        fail("Apollo Debt Solutions annual carry proxy does not reconcile")
    if not math.isclose(five_year, round(expected_annual * 5, 3), abs_tol=0.000001):
        fail("Apollo Debt Solutions five-year carry proxy does not reconcile")
    for field in ("what_is_proven", "what_is_not_proven", "next_upgrade"):
        if not row[field].strip():
            fail(f"Apollo Debt Solutions carry field missing: {field}")


def verify_apollo_debt_solutions_issuer_bridge() -> None:
    if not APOLLO_DEBT_SOLUTIONS_ISSUER_BRIDGE.exists():
        fail(f"missing {APOLLO_DEBT_SOLUTIONS_ISSUER_BRIDGE.relative_to(ROOT)}")
    with APOLLO_DEBT_SOLUTIONS_ISSUER_BRIDGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != APOLLO_DEBT_SOLUTIONS_ISSUER_BRIDGE_HEADER:
            fail(f"Apollo Debt Solutions issuer bridge header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "ADS-ISSUER-001": 1153.510,
        "ADS-ISSUER-002": 599.045,
        "ADS-ISSUER-003": 323.289,
        "ADS-ISSUER-004": 857.638,
        "ADS-ISSUER-005": 16567.834,
        "ADS-ISSUER-006": 312.890,
        "ADS-ISSUER-007": 398.539,
        "ADS-ISSUER-008": 782.527,
        "ADS-ISSUER-009": 4714.695,
        "ADS-ISSUER-010": 2031.953,
        "ADS-ISSUER-011": 1617.107,
        "ADS-ISSUER-012": 1449.623,
    }
    if [row["observation_id"] for row in rows] != list(expected):
        fail("Apollo Debt Solutions issuer bridge observations changed unexpectedly")
    for row in rows:
        if not math.isclose(number(row, "value_musd"), expected[row["observation_id"]], abs_tol=0.000001):
            fail(f"Apollo Debt Solutions issuer bridge value changed: {row['observation_id']}")
        if row["observation_id"] == "ADS-ISSUER-012" and row["status"] != "financing-reconciliation-gap":
            fail("Apollo Debt Solutions financing residual must remain a reconciliation gap")
        if row["observation_id"] != "ADS-ISSUER-012" and not row["status"].strip():
            fail(f"Apollo Debt Solutions issuer bridge status missing: {row['observation_id']}")
        source = resolve_source(APOLLO_DEBT_SOLUTIONS_ISSUER_BRIDGE, row["source_artifact"])
        if not source.exists():
            fail(f"Apollo Debt Solutions issuer bridge source missing: {row['source_artifact']}")
        for field in ("period", "metric", "what_is_proven", "what_is_not_proven", "next_upgrade"):
            if not row[field].strip():
                fail(f"Apollo Debt Solutions issuer bridge field missing: {row['observation_id']} {field}")
    by_id = {row["observation_id"]: number(row, "value_musd") for row in rows}
    visible_financing = (
        by_id["ADS-ISSUER-008"]
        + by_id["ADS-ISSUER-009"]
        - by_id["ADS-ISSUER-010"]
        - by_id["ADS-ISSUER-007"]
    )
    residual = visible_financing - by_id["ADS-ISSUER-011"]
    if not math.isclose(visible_financing, 3066.730, abs_tol=0.000001):
        fail("Apollo Debt Solutions visible financing subtotal does not reconcile")
    if not math.isclose(residual, by_id["ADS-ISSUER-012"], abs_tol=0.000001):
        fail("Apollo Debt Solutions financing reconciliation residual does not reconcile")


def verify_apollo_debt_solutions_payment_boundary() -> None:
    if not APOLLO_DEBT_SOLUTIONS_PAYMENT_BOUNDARY.exists():
        fail(f"missing {APOLLO_DEBT_SOLUTIONS_PAYMENT_BOUNDARY.relative_to(ROOT)}")
    with APOLLO_DEBT_SOLUTIONS_PAYMENT_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != APOLLO_DEBT_SOLUTIONS_PAYMENT_BOUNDARY_HEADER:
            fail(f"Apollo Debt Solutions payment boundary header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = ["ADS-PAY-001", "ADS-PAY-002", "ADS-PAY-003", "ADS-PAY-004"]
    if [row["observation_id"] for row in rows] != expected_ids:
        fail("Apollo Debt Solutions payment boundary rows changed unexpectedly")
    expected_status = {
        "ADS-PAY-001": "partial-upgrade",
        "ADS-PAY-002": "partial-upgrade",
        "ADS-PAY-003": "evidence-insufficient",
        "ADS-PAY-004": "searched-negative",
    }
    for row in rows:
        if row["status"] != expected_status[row["observation_id"]]:
            fail(f"Apollo Debt Solutions payment boundary status changed: {row['observation_id']}")
        source = resolve_source(APOLLO_DEBT_SOLUTIONS_PAYMENT_BOUNDARY, row["source_artifact"])
        if not source.exists():
            fail(f"Apollo Debt Solutions payment boundary source missing: {row['source_artifact']}")
        for field in ("observation_type", "period_or_date", "instrument_or_holder", "observed_value", "what_is_proven", "what_is_not_proven", "next_upgrade"):
            if not row[field].strip():
                fail(f"Apollo Debt Solutions payment boundary field missing: {row['observation_id']} {field}")
    if "6.700%" not in rows[0]["observed_value"] or "January 29" not in rows[0]["observed_value"] or "July 29" not in rows[0]["observed_value"]:
        fail("Apollo Debt Solutions contractual payment schedule changed unexpectedly")
    if "$600M" not in rows[1]["observed_value"] or "2031" not in rows[1]["observed_value"]:
        fail("Apollo Debt Solutions principal/maturity boundary changed unexpectedly")
    if "No public trustee remittance" not in rows[3]["observed_value"]:
        fail("Apollo Debt Solutions searched-negative boundary changed unexpectedly")


def verify_apollo_related_party_bridge() -> None:
    if not APOLLO_RELATED_PARTY.exists():
        fail(f"missing {APOLLO_RELATED_PARTY.relative_to(ROOT)}")
    with APOLLO_RELATED_PARTY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != APOLLO_RELATED_PARTY_HEADER:
            fail(f"Apollo related-party header mismatch: {reader.fieldnames}")
        rows = list(reader)
    required = {f"APO-R{index:02d}" for index in range(1, 20)}
    by_id = {row["line_id"]: row for row in rows}
    if set(by_id) != required:
        fail(f"Apollo related-party lines are {sorted(by_id)}")
    for row in rows:
        source = resolve_source(APOLLO_RELATED_PARTY, row["source_artifact"])
        if not source.exists():
            fail(f"Apollo related-party source missing: {row['source_artifact']}")
        for field in ("line_id", "entity", "metric", "amount_musd", "period", "flow_direction", "return_or_access_status", "interpretation", "next_upgrade"):
            if not row[field].strip():
                fail(f"Apollo related-party row {row['line_id']} has empty {field}")
    expected = {
        "APO-R01": "70616", "APO-R02": "17931", "APO-R03": "13070",
        "APO-R04": "4206", "APO-R05": "3191", "APO-R06": "134",
        "APO-R07": "785", "APO-R08": "7800", "APO-R09": "5700",
        "APO-R10": "1.41 percent", "APO-R11": "-1000",
        "APO-R12": "375", "APO-R13": "71", "APO-R14": "301", "APO-R15": "NA",
        "APO-R16": "140", "APO-R17": "8700", "APO-R18": "134", "APO-R19": "392",
    }
    for line_id, value in expected.items():
        if by_id[line_id]["amount_musd"] != value:
            fail(f"Apollo related-party line {line_id} changed unexpectedly")


def verify_apollo_fee_rollforward() -> None:
    if not APOLLO_FEE_ROLLFORWARD.exists():
        fail(f"missing {APOLLO_FEE_ROLLFORWARD.relative_to(ROOT)}")
    with APOLLO_FEE_ROLLFORWARD.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "boundary_id", "entity", "opening_payable_musd", "period_expense_musd",
            "ending_payable_musd", "mechanical_implied_settlement_musd", "period",
            "proof_status", "source_artifact", "missing_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Apollo fee rollforward header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if {row["boundary_id"] for row in rows} != {"FEE-RF-01", "FEE-RF-02"}:
        fail("Apollo fee rollforward rows changed unexpectedly")
    for row in rows:
        if not resolve_source(APOLLO_FEE_ROLLFORWARD, row["source_artifact"]).exists():
            fail(f"Apollo fee rollforward source missing: {row['source_artifact']}")
        for field in ("boundary_id", "entity", "period", "proof_status", "source_artifact", "missing_upgrade"):
            if not row[field].strip():
                fail(f"Apollo fee rollforward field missing: {field}")
    management = next(row for row in rows if row["boundary_id"] == "FEE-RF-01")
    if int(management["mechanical_implied_settlement_musd"]) != (
        int(management["opening_payable_musd"])
        + int(management["period_expense_musd"])
        - int(management["ending_payable_musd"])
    ):
        fail("Apollo management-fee rollforward arithmetic failed")
    if management["proof_status"] != "mechanical-rollforward-qualified":
        fail("Apollo management-fee rollforward status overclaims proof")
    contingent = next(row for row in rows if row["boundary_id"] == "FEE-RF-02")
    if contingent["period_expense_musd"] != "NA" or contingent["mechanical_implied_settlement_musd"] != "NA":
        fail("ACRA contingent-fee row must remain non-calculable")


def verify_apollo_named_asset_routes() -> None:
    if not APOLLO_NAMED_ROUTES.exists():
        fail(f"missing {APOLLO_NAMED_ROUTES.relative_to(ROOT)}")
    with APOLLO_NAMED_ROUTES.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != APOLLO_NAMED_ROUTES_HEADER:
            fail(f"Apollo named-route header mismatch: {reader.fieldnames}")
        rows = list(reader)
    required = {"APO-N01", "APO-N02", "APO-N03"}
    by_id = {row["route_id"]: row for row in rows}
    if set(by_id) != required:
        fail(f"Apollo named routes are {sorted(by_id)}")
    for row in rows:
        source = resolve_source(APOLLO_NAMED_ROUTES, row["source_artifact"])
        if not source.exists():
            fail(f"Apollo named-route source missing: {row['source_artifact']}")
        for field in ("route_id", "asset_or_wrapper", "public_destination_or_use", "route_status", "what_is_proven", "missing_upgrade"):
            if not row[field].strip():
                fail(f"Apollo named route {row['route_id']} has empty {field}")
        number(row, "athene_entity_evidence_musd")
        for field in ("athene_book_or_exposure_musd", "public_cash_or_income_signal_musd"):
            if row[field].strip():
                number(row, field)
    if by_id["APO-N01"]["route_status"] != "borrower-wrapper-use-proxy-visible":
        fail("Concord route grade changed unexpectedly")
    if by_id["APO-N02"]["route_status"] != "platform-wrapper-athene-alignment-visible":
        fail("AMAPS route grade changed unexpectedly")
    if by_id["APO-N03"]["route_status"] != "mixed-row-cash-like-candidate":
        fail("AP Aristotle route grade changed unexpectedly")


def verify_apollo_statutory_named_asset_return_boundary() -> None:
    """Keep statutory named-asset observations below settled-return promotion."""
    if not APOLLO_STATUTORY_NAMED_ASSET_MAP.exists():
        fail(f"missing Apollo statutory named-asset map: {APOLLO_STATUTORY_NAMED_ASSET_MAP.relative_to(ROOT)}")
    with APOLLO_STATUTORY_NAMED_ASSET_MAP.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "issuer_map_id", "proof_packet_id", "safe_summary_rank", "cusip",
            "issuer_or_description_sample", "athene_cash_like_consideration_usd",
            "athene_year_end_book_value_usd", "instrument_or_wrapper", "destination_lane",
            "mapped_platform_or_sponsor", "borrower_or_collateral_read", "source_backing_type",
            "source_url", "source_evidence_summary", "mapping_status", "cash_movement_read",
            "remaining_named_cash_documents", "safe_claim", "boundary", "next_action",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Apollo statutory named-asset map header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["issuer_map_id"] for row in rows] != [f"CFAASCIBM-{index:03d}" for index in range(1, 11)]:
        fail("Apollo statutory named-asset map rows changed unexpectedly")
    allowed_mapping_statuses = {
        "issuer-named-platform-marker-borrower-use-hold",
        "platform-related-issuer-visible-borrower-use-hold",
        "issuer-named-mixed-row-hold",
        "platform-wrapper-visible-underlying-collateral-hold",
        "borrower-wrapper-and-use-proxy-visible-cash-receipt-hold",
        "securitization-vehicle-visible-loan-collateral-hold",
        "sovereign-reserve-asset-mapped-operating-use-not-applicable",
    }
    for map_row in rows:
        if map_row["mapping_status"] not in allowed_mapping_statuses:
            fail(f"Apollo statutory named-asset map status over-promoted: {map_row['issuer_map_id']}")
        if not all(map_row[field].strip() for field in ("source_url", "source_evidence_summary", "safe_claim", "boundary", "next_action")):
            fail(f"Apollo statutory named-asset map row incomplete: {map_row['issuer_map_id']}")
        if "borrower" not in map_row["boundary"].lower() or "return" not in map_row["boundary"].lower():
            fail(f"Apollo statutory named-asset map boundary weakened: {map_row['issuer_map_id']}")
    by_id = {row["issuer_map_id"]: row for row in rows}
    row = by_id.get("CFAASCIBM-006")
    if row is None or row["cusip"] != "592918-AA-4":
        fail("MF1 2025-B2 statutory named-asset row changed unexpectedly")
    if row["mapping_status"] != "securitization-vehicle-visible-loan-collateral-hold":
        fail("MF1 statutory named-asset row was promoted beyond its mapping boundary")
    if "cash-like proceeds" not in row["cash_movement_read"] or "borrower" not in row["cash_movement_read"]:
        fail("MF1 statutory named-asset cash boundary is incomplete")
    if "borrower receipt" not in row["boundary"] or "final asset return" not in row["boundary"]:
        fail("MF1 statutory named-asset boundary no longer protects settled-return claims")
    if "2026-FL21" not in row["source_evidence_summary"] or "cross-series" not in row["source_evidence_summary"]:
        fail("MF1 statutory named-asset series-identity boundary is missing")
    if not row["next_action"].strip():
        fail("MF1 statutory named-asset next action is missing")


def verify_apollo_ari_seller_cash() -> None:
    if not APOLLO_ARI_SELLER_CASH.exists():
        fail(f"missing ARI seller-cash upgrade: {APOLLO_ARI_SELLER_CASH.relative_to(ROOT)}")
    with APOLLO_ARI_SELLER_CASH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != APOLLO_RELATED_PARTY_HEADER:
            fail(f"ARI seller-cash header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 5:
        fail(f"ARI seller-cash upgrade must contain 5 rows, found {len(rows)}")
    expected = {
        "ARI-Q2-01": ("9497.267", "inflow", "seller-cash-aggregate-confirmed"),
        "ARI-Q2-02": ("67.578", "inflow", "seller-cash-aggregate-confirmed"),
        "ARI-Q2-03": ("746.250", "outflow", "debt-use-confirmed"),
        "ARI-Q2-04": ("500.000", "outflow", "debt-use-confirmed"),
        "ARI-Q2-05": ("1239.480", "ending balance", "seller-liquidity-boundary-confirmed"),
    }
    by_id = {row["line_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"ARI seller-cash lines changed: {sorted(by_id)}")
    for line_id, (amount_musd, direction, status) in expected.items():
        row = by_id[line_id]
        if row["amount_musd"] != amount_musd or row["flow_direction"] != direction or row["return_or_access_status"] != status:
            fail(f"ARI seller-cash line changed unexpectedly: {line_id}")
        source = resolve_source(APOLLO_ARI_SELLER_CASH, row["source_artifact"])
        if not source.exists():
            fail(f"ARI seller-cash source missing: {row['source_artifact']}")
        if not row["interpretation"].strip() or not row["next_upgrade"].strip():
            fail(f"ARI seller-cash line incomplete: {line_id}")


def verify_apollo_ari_cash_reconciliation() -> None:
    if not APOLLO_ARI_CASH_RECONCILIATION.exists():
        fail(f"missing ARI cash reconciliation: {APOLLO_ARI_CASH_RECONCILIATION.relative_to(ROOT)}")
    with APOLLO_ARI_CASH_RECONCILIATION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "line_id", "entity", "metric", "amount_musd", "period",
            "flow_direction", "status", "source_artifact", "interpretation", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"ARI cash-reconciliation header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 6:
        fail(f"ARI cash reconciliation must contain 6 rows, found {len(rows)}")
    expected = {
        "ARI-CF-01": 139.825,
        "ARI-CF-02": 46.483,
        "ARI-CF-03": 8899.484,
        "ARI-CF-04": -7848.008,
        "ARI-CF-05": 1.696,
        "ARI-CF-06": 1239.480,
    }
    by_id = {row["line_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"ARI cash-reconciliation lines changed: {sorted(by_id)}")
    for line_id, expected_amount in expected.items():
        row = by_id[line_id]
        if not math.isclose(float(row["amount_musd"]), expected_amount, rel_tol=0, abs_tol=0.001):
            fail(f"ARI cash-reconciliation amount changed: {line_id}")
        if not resolve_source(APOLLO_ARI_CASH_RECONCILIATION, row["source_artifact"]).exists():
            fail(f"ARI cash-reconciliation source missing: {row['source_artifact']}")
        if not row["interpretation"].strip() or not row["next_upgrade"].strip():
            fail(f"ARI cash-reconciliation line incomplete: {line_id}")
    calculated = expected["ARI-CF-01"] + expected["ARI-CF-02"] + expected["ARI-CF-03"] + expected["ARI-CF-04"] + expected["ARI-CF-05"]
    if not math.isclose(calculated, expected["ARI-CF-06"], rel_tol=0, abs_tol=0.001):
        fail("ARI cash-flow reconciliation arithmetic failed")


def verify_apollo_ari_transaction_terms() -> None:
    if not APOLLO_ARI_TRANSACTION_TERMS.exists():
        fail(f"missing ARI transaction-terms boundary: {APOLLO_ARI_TRANSACTION_TERMS.relative_to(ROOT)}")
    with APOLLO_ARI_TRANSACTION_TERMS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "term_id", "transaction", "term", "value", "period", "status",
            "primary_source_url", "source_artifact", "what_is_proven", "missing_upgrade",
            "local_source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"ARI transaction-terms header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "ARI-TERM-001": ("purchase price percentage", "99.7% of total loan commitments"),
        "ARI-TERM-002": ("CECL treatment", "net of asset-specific CECL reserves"),
        "ARI-TERM-003": ("excluded loans", "146M combined principal expected to repay before closing"),
        "ARI-TERM-004": ("financing contingency", "none"),
    }
    by_id = {row["term_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"ARI transaction terms changed: {sorted(by_id)}")
    for term_id, (term, value) in expected.items():
        row = by_id[term_id]
        if row["term"] != term or row["value"] != value or row["status"] != "source-confirmed":
            fail(f"ARI transaction term changed unexpectedly: {term_id}")
        if row["primary_source_url"] != "https://www.sec.gov/Archives/edgar/data/1467760/000119312526027340/d58100dex991.htm":
            fail(f"ARI transaction-term primary source changed: {term_id}")
        if not resolve_source(APOLLO_ARI_TRANSACTION_TERMS, row["source_artifact"]).exists():
            fail(f"ARI transaction-term source missing: {row['source_artifact']}")
        if not (ROOT / row["local_source_artifact"]).exists():
            fail(f"ARI transaction-term local source missing: {term_id}")
        if not row["what_is_proven"].strip() or not row["missing_upgrade"].strip():
            fail(f"ARI transaction term incomplete: {term_id}")


def verify_apollo_ari_payment_mechanics() -> None:
    if not APOLLO_ARI_PAYMENT_MECHANICS.exists():
        fail(f"missing ARI payment-mechanics boundary: {APOLLO_ARI_PAYMENT_MECHANICS.relative_to(ROOT)}")
    with APOLLO_ARI_PAYMENT_MECHANICS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "mechanic_id", "mechanic", "requirement", "period", "status",
            "primary_source_url", "source_artifact", "what_is_proven", "missing_upgrade",
            "local_source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"ARI payment-mechanics header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {"ARI-MECH-001", "ARI-MECH-002", "ARI-MECH-003", "ARI-MECH-004", "ARI-MECH-005"}
    by_id = {row["mechanic_id"]: row for row in rows}
    if set(by_id) != expected_ids:
        fail(f"ARI payment mechanics changed: {sorted(by_id)}")
    source_url = "https://www.sec.gov/Archives/edgar/data/1467760/000119312526027340/d58100dex21.htm"
    for mechanic_id, row in by_id.items():
        if row["status"] != "source-confirmed" or row["primary_source_url"] != source_url:
            fail(f"ARI payment mechanic changed unexpectedly: {mechanic_id}")
        if not resolve_source(APOLLO_ARI_PAYMENT_MECHANICS, row["source_artifact"]).exists():
            fail(f"ARI payment-mechanics source missing: {row['source_artifact']}")
        if not (ROOT / row["local_source_artifact"]).exists():
            fail(f"ARI payment-mechanics local source missing: {row['mechanic_id']}")
        for field in ("mechanic", "requirement", "what_is_proven", "missing_upgrade"):
            if not row[field].strip():
                fail(f"ARI payment mechanic incomplete: {mechanic_id}")


def verify_apollo_ari_post_close_search() -> None:
    if not APOLLO_ARI_POST_CLOSE_SEARCH.exists():
        fail(f"missing ARI post-close search boundary: {APOLLO_ARI_POST_CLOSE_SEARCH.relative_to(ROOT)}")
    with APOLLO_ARI_POST_CLOSE_SEARCH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "search_id", "proof_object", "search_perimeter", "result_class",
            "primary_source_urls", "source_artifact", "observed_boundary", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"ARI post-close search header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {"ARI-SEARCH-001", "ARI-SEARCH-002", "ARI-SEARCH-003", "ARI-SEARCH-004"}
    by_id = {row["search_id"]: row for row in rows}
    if set(by_id) != expected_ids:
        fail(f"ARI post-close search rows changed: {sorted(by_id)}")
    for search_id, row in by_id.items():
        if row["result_class"] != "searched-negative":
            fail(f"ARI post-close search classification changed: {search_id}")
        if not row["primary_source_urls"].strip() or not row["search_perimeter"].strip():
            fail(f"ARI post-close search perimeter incomplete: {search_id}")
        if not resolve_source(APOLLO_ARI_POST_CLOSE_SEARCH, row["source_artifact"]).exists():
            fail(f"ARI post-close search source missing: {row['source_artifact']}")
        if not row["observed_boundary"].strip() or not row["next_upgrade"].strip():
            fail(f"ARI post-close search row incomplete: {search_id}")


def verify_apollo_private_credit_public_search() -> None:
    path = PILOT_DIR / "data" / "capital-flow-apollo-athene-private-credit-public-search-boundary-2026-09-16.csv"
    if not path.exists():
        fail(f"missing Apollo private-credit public-search boundary: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "search_id", "route", "cusip_fragments", "search_terms", "result_class",
            "public_context", "missing_proof", "next_action",
        ]
        if reader.fieldnames != expected_header:
            fail(f"private-credit public-search header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "PCPS-001": ("Eliant", "28655*-AA-7;28655*-AB-5"),
        "PCPS-002": ("AP Aristotle", "00264#-AB-3"),
    }
    by_id = {row["search_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"private-credit public-search rows changed: {sorted(by_id)}")
    for search_id, (route, cusips) in expected.items():
        row = by_id[search_id]
        if row["route"] != route or row["cusip_fragments"] != cusips or row["result_class"] != "searched-negative":
            fail(f"private-credit public-search result changed: {search_id}")
        for field in ("search_terms", "public_context", "missing_proof", "next_action"):
            if not row[field].strip():
                fail(f"private-credit public-search line incomplete: {search_id}")


def verify_apollo_mf1_remittance_access() -> None:
    path = PILOT_DIR / "data" / "capital-flow-apollo-athene-mf1-remittance-access-boundary-2026-09-16.csv"
    if not path.exists():
        fail(f"missing MF1 remittance-access boundary: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["search_id", "route", "result_class", "observed_boundary", "source_url", "local_source_artifact", "next_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"MF1 remittance-access header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "MF1-RAB-001": ("located-access-controlled", "CTSLink MF1CAP / 2025B2 series page"),
        "MF1-RAB-002": ("public-source-confirmed", "SEC MF1 data-procedures exhibit"),
        "MF1-RAB-003": ("public-source-confirmed", "SEC MF1 servicing agreement"),
    }
    by_id = {row["search_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"MF1 remittance-access rows changed: {sorted(by_id)}")
    for search_id, (result_class, route) in expected.items():
        row = by_id[search_id]
        if row["result_class"] != result_class or row["route"] != route:
            fail(f"MF1 remittance-access result changed: {search_id}")
        if not (ROOT / row["local_source_artifact"]).exists():
            fail(f"MF1 remittance-access local source missing: {search_id}")
        for field in ("observed_boundary", "source_url", "local_source_artifact", "next_upgrade"):
            if not row[field].strip():
                fail(f"MF1 remittance-access line incomplete: {search_id}")


def verify_apollo_mf1_servicing_waterfall_boundary() -> None:
    path = LEDGER_DIR / "capital-flow-apollo-athene-mf1-servicing-waterfall-mechanics-boundary-2026-09-17.csv"
    if not path.exists():
        fail(f"missing MF1 servicing-waterfall boundary: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "id", "gate", "source", "period", "observation", "result_class",
            "safe_use", "boundary", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"MF1 servicing-waterfall header mismatch: {reader.fieldnames}")
        rows = list(reader)
    by_id = {row["id"]: row for row in rows}
    if "MF1SW-009" not in by_id:
        fail("MF1 servicing-waterfall series-identity row is missing")
    row = by_id["MF1SW-009"]
    if row["gate"] != "series_identity" or row["period"] != "2026-09-17":
        fail("MF1 servicing-waterfall series-identity metadata changed")
    if "MF1 2026-FL21" not in row["observation"] or "MF1 2025-B2" not in row["boundary"]:
        fail("MF1 servicing-waterfall series distinction was lost")
    if row["result_class"] != "series-identity-boundary-visible":
        fail("MF1 servicing-waterfall series boundary was over-promoted")
    for field in ("safe_use", "boundary", "next_upgrade"):
        if not row[field].strip():
            fail(f"MF1 servicing-waterfall series line incomplete: {field}")


def verify_apollo_ari_cash_delta() -> None:
    if not APOLLO_ARI_CASH_DELTA.exists():
        fail(f"missing ARI cash-perimeter delta: {APOLLO_ARI_CASH_DELTA.relative_to(ROOT)}")
    with APOLLO_ARI_CASH_DELTA.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "delta_id", "metric", "amount_musd", "source_artifact", "status",
            "what_is_proven", "what_is_not_proven",
        ]
        if reader.fieldnames != expected_header:
            fail(f"ARI cash-delta header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {"ARI-DELTA-001": 8600.0, "ARI-DELTA-002": 9497.267, "ARI-DELTA-003": 897.267, "ARI-DELTA-004": 67.578}
    by_id = {row["delta_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"ARI cash-delta rows changed: {sorted(by_id)}")
    for delta_id, amount in expected.items():
        row = by_id[delta_id]
        if not math.isclose(float(row["amount_musd"]), amount, rel_tol=0, abs_tol=0.001):
            fail(f"ARI cash-delta amount changed: {delta_id}")
        if not resolve_source(APOLLO_ARI_CASH_DELTA, row["source_artifact"]).exists():
            fail(f"ARI cash-delta source missing: {row['source_artifact']}")
        if not row["what_is_proven"].strip() or not row["what_is_not_proven"].strip():
            fail(f"ARI cash-delta row incomplete: {delta_id}")
    if not math.isclose(expected["ARI-DELTA-002"] - expected["ARI-DELTA-001"], expected["ARI-DELTA-003"], rel_tol=0, abs_tol=0.001):
        fail("ARI cash-perimeter delta arithmetic failed")


def verify_apollo_ari_aum_outflow() -> None:
    if not APOLLO_ARI_AUM_OUTFLOW.exists():
        fail(f"missing ARI AUM outflow boundary: {APOLLO_ARI_AUM_OUTFLOW.relative_to(ROOT)}")
    with APOLLO_ARI_AUM_OUTFLOW.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "observation_id", "metric", "amount_musd", "period", "status",
            "primary_source_url", "source_artifact", "what_is_proven", "what_is_not_proven",
        ]
        if reader.fieldnames != expected_header:
            fail(f"ARI AUM outflow header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {"ARI-AUM-001": 7800.0, "ARI-AUM-002": 5000.0}
    by_id = {row["observation_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"ARI AUM outflow rows changed: {sorted(by_id)}")
    source_url = "https://ir.athene.com/sec-filings/all-sec-filings/content/0001527469-26-000047/agmearningsrelease2q2026.htm"
    for observation_id, amount in expected.items():
        row = by_id[observation_id]
        if row["status"] != "source-confirmed" or row["primary_source_url"] != source_url:
            fail(f"ARI AUM outflow classification changed: {observation_id}")
        if not math.isclose(float(row["amount_musd"]), amount, rel_tol=0, abs_tol=0.1):
            fail(f"ARI AUM outflow amount changed: {observation_id}")
        if not resolve_source(APOLLO_ARI_AUM_OUTFLOW, row["source_artifact"]).exists():
            fail(f"ARI AUM outflow source missing: {row['source_artifact']}")
        for field in ("metric", "period", "what_is_proven", "what_is_not_proven"):
            if not row[field].strip():
                fail(f"ARI AUM outflow row incomplete: {observation_id} / {field}")


def verify_apollo_ari_perimeter_reconciliation() -> None:
    if not APOLLO_ARI_PERIMETER_RECONCILIATION.exists():
        fail(f"missing ARI perimeter reconciliation: {APOLLO_ARI_PERIMETER_RECONCILIATION.relative_to(ROOT)}")
    with APOLLO_ARI_PERIMETER_RECONCILIATION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "source", "description", "amount_busd", "comparison_to_athene_buyer_pct",
            "interpretation", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"ARI perimeter reconciliation header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 4:
        fail(f"ARI perimeter reconciliation row count changed: {len(rows)}")
    expected = {
        "ARI proxy": (9.0, "3.45"),
        "ARI Q2 2026 10-Q": (8.6, "-1.15"),
        "Athene Q2 2026 10-Q": (8.7, "0.0"),
        "Athene Q2 2026 earnings release": (7.8, "not-comparable"),
    }
    by_source = {row["source"]: row for row in rows}
    if set(by_source) != set(expected):
        fail(f"ARI perimeter reconciliation sources changed: {sorted(by_source)}")
    for source, (amount, comparison) in expected.items():
        row = by_source[source]
        if not math.isclose(float(row["amount_busd"]), amount, rel_tol=0, abs_tol=0.001):
            fail(f"ARI perimeter reconciliation amount changed: {source}")
        if row["comparison_to_athene_buyer_pct"] != comparison:
            fail(f"ARI perimeter reconciliation comparison changed: {source}")
        if not resolve_source(APOLLO_ARI_PERIMETER_RECONCILIATION, row["source_artifact"]).exists():
            fail(f"ARI perimeter reconciliation source missing: {row['source_artifact']}")
        for field in ("description", "interpretation"):
            if not row[field].strip():
                fail(f"ARI perimeter reconciliation row incomplete: {source} / {field}")


def verify_apollo_ari_liquidation_distribution() -> None:
    if not APOLLO_ARI_LIQUIDATION_DISTRIBUTION.exists():
        fail(f"missing ARI liquidation-distribution boundary: {APOLLO_ARI_LIQUIDATION_DISTRIBUTION.relative_to(ROOT)}")
    with APOLLO_ARI_LIQUIDATION_DISTRIBUTION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "observation_id", "period", "metric", "lower_per_share_usd",
            "upper_per_share_usd", "fully_diluted_shares", "lower_aggregate_musd",
            "upper_aggregate_musd", "status", "what_is_proven",
            "what_is_not_proven", "source_artifact", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"ARI liquidation-distribution header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "ARI-LIQ-001": (7.75, 8.50, 1013.423, 1111.496),
        "ARI-LIQ-002": (11.50, 12.25, 1503.789, 1601.863),
    }
    if [row["observation_id"] for row in rows] != list(expected):
        fail("ARI liquidation-distribution observations changed unexpectedly")
    for row in rows:
        lower, upper, lower_aggregate, upper_aggregate = expected[row["observation_id"]]
        if row["status"] != "seller-common-residual-estimate-confirmed":
            fail(f"ARI liquidation-distribution estimate is over-promoted: {row['observation_id']}")
        if not math.isclose(float(row["lower_per_share_usd"]), lower, abs_tol=0.000001) or not math.isclose(float(row["upper_per_share_usd"]), upper, abs_tol=0.000001):
            fail(f"ARI liquidation-distribution per-share range changed: {row['observation_id']}")
        shares = float(row["fully_diluted_shares"])
        if not math.isclose(shares, 130764290, abs_tol=0.5):
            fail(f"ARI liquidation-distribution share count changed: {row['observation_id']}")
        if not math.isclose(float(row["lower_aggregate_musd"]), shares * lower / 1_000_000, abs_tol=0.001):
            fail(f"ARI liquidation-distribution lower aggregate does not reconcile: {row['observation_id']}")
        if not math.isclose(float(row["upper_aggregate_musd"]), shares * upper / 1_000_000, abs_tol=0.001):
            fail(f"ARI liquidation-distribution upper aggregate does not reconcile: {row['observation_id']}")
        if not math.isclose(float(row["lower_aggregate_musd"]), lower_aggregate, abs_tol=0.001) or not math.isclose(float(row["upper_aggregate_musd"]), upper_aggregate, abs_tol=0.001):
            fail(f"ARI liquidation-distribution aggregate range changed: {row['observation_id']}")
        if not resolve_source(APOLLO_ARI_LIQUIDATION_DISTRIBUTION, row["source_artifact"]).exists():
            fail(f"ARI liquidation-distribution source missing: {row['source_artifact']}")
        for field in ("period", "metric", "what_is_proven", "what_is_not_proven", "next_upgrade"):
            if not row[field].strip():
                fail(f"ARI liquidation-distribution row incomplete: {row['observation_id']} / {field}")


def verify_apollo_named_asset_ledger_gates() -> None:
    ledger = PILOT_LEDGERS[2]
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    by_id = {row["gate_id"]: row for row in rows}
    required = {"APO-032", "APO-033", "APO-034", "APO-071", "APO-072", "APO-073", "APO-074", "APO-075", "APO-076", "APO-079", "APO-080", "APO-081", "APO-082", "APO-083", "APO-084", "APO-085", "APO-086", "APO-087", "APO-088", "APO-089", "APO-090", "APO-091", "APO-092", "APO-093", "APO-095", "APO-096", "APO-097", "APO-108", "APO-109", "APO-110", "APO-111", "APO-112"}
    if not required.issubset(by_id):
        fail(f"Apollo named-asset ledger gates are missing: {sorted(required - set(by_id))}")
    expected = {
        "APO-032": ("borrower-wrapper-use-proxy-visible", "analysis/company-first-principles/capital-flow-apollo-athene-concord-named-cash-source-acquisition-pass-1.md"),
        "APO-033": ("platform-wrapper-athene-alignment-visible", "analysis/company-first-principles/capital-flow-apollo-athene-amaps-named-cash-source-acquisition-pass-1.md"),
        "APO-034": ("mixed-row-cash-like-candidate", "analysis/company-first-principles/capital-flow-apollo-athene-aristotle-mixed-row-resolution-pass-1.md"),
        "APO-071": ("same-cusip-statutory-bridge-visible", "analysis/company-first-principles/capital-flow-apollo-athene-statutory-same-cusip-bridge-upgrade-2026-09-15.md"),
        "APO-072": ("same-cusip-statutory-bridge-visible", "analysis/company-first-principles/capital-flow-apollo-athene-statutory-same-cusip-bridge-upgrade-2026-09-15.md"),
        "APO-073": ("statutory-parent-affiliate-boundary-visible", "analysis/company-first-principles/capital-flow-apollo-athene-statutory-parent-affiliate-boundary-upgrade-2026-09-15.md"),
        "APO-074": ("dilution-denominator-confirmed", "analysis/company-first-principles/capital-flow-apollo-q2-share-claim-dilution-boundary-upgrade-2026-09-15.md"),
        "APO-075": ("parent-only-dividend-receipt-visible", "analysis/company-first-principles/capital-flow-apollo-fy2025-parent-dividend-receipt-upgrade-2026-09-15.md"),
        "APO-076": ("athene-adip-related-party-flow-visible", "analysis/company-first-principles/capital-flow-apollo-fy2025-athene-adip-related-party-flow-upgrade-2026-09-15.md"),
        "APO-079": ("full-range-population-boundary-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-d-full-range-reconciliation-boundary-2026-09-15.md"),
        "APO-080": ("blank-column-parser-boundary-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-d-blank-column-boundary-2026-09-15.md"),
        "APO-081": ("section-total-reconciliation-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-upgrade-2026-09-15.md"),
        "APO-082": ("corrected-same-cusip-row-bridge-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-same-cusip-corrected-row-confirmation-2026-09-15.md"),
        "APO-083": ("same-cusip-lot-continuity-boundary-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-same-cusip-lot-chronology-boundary-2026-09-15.md"),
        "APO-084": ("mechanical-liability-cost-sensitivity-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-named-route-liability-cost-sensitivity-2026-09-15.md"),
        "APO-085": ("dated-legal-dividend-path-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-q2-dividend-schedule-upgrade-2026-09-15.md"),
        "APO-086": ("sensitivity-frontier-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-parent-receipt-attribution-frontier-2026-09-15.md"),
        "APO-087": ("source-search-boundary-confirmed", "analysis/company-first-principles/capital-flow-apollo-q2-financial-supplement-parent-receipt-search-boundary-2026-09-15.md"),
        "APO-088": ("athene-to-parent-flow-observed", "analysis/company-first-principles/capital-flow-apollo-athene-q2-parent-flow-upgrade-2026-09-15.md"),
        "APO-089": ("holdco-route-and-intercompany-boundary-confirmed", "analysis/company-first-principles/capital-flow-apollo-q2-holdco-liquidity-intercompany-boundary-2026-09-15.md"),
        "APO-090": ("q2-xbrl-parent-receipt-boundary-confirmed", "analysis/company-first-principles/capital-flow-apollo-q2-xbrl-parent-receipt-boundary-2026-09-15.md"),
        "APO-091": ("athene-to-agm-financing-route-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-intercompany-note-route-upgrade-2026-09-15.md"),
        "APO-092": ("period-matched-segment-spread-screen-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-fy2025-period-matched-spread-boundary-2026-09-15.md"),
        "APO-093": ("buyer-perimeter-expansion-boundary-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-ari-buyer-portfolio-expansion-boundary-2026-09-15.md"),
        "APO-095": ("attribution-frontier-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-q2-parent-receipt-attribution-frontier-2026-09-15.md"),
        "APO-096": ("seller-cash-and-debt-waterfall-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-ari-q2-seller-cash-debt-waterfall-upgrade-2026-09-15.md"),
        "APO-097": ("seller-cash-flow-reconciled", "analysis/company-first-principles/capital-flow-apollo-athene-ari-q2-cash-flow-reconciliation-2026-09-15.md"),
        "APO-108": ("buyer-acquisition-perimeter-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-ari-buyer-side-acquisition-boundary-2026-09-16.md"),
        "APO-109": ("buyer-credit-boundary-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-ari-buyer-side-acquisition-boundary-2026-09-16.md"),
        "APO-110": ("current-wrapper-exposure-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-q2-amaps-current-exposure-boundary-2026-09-16.md"),
        "APO-111": ("deal-level-servicing-payment-proxy-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-concord-named-cash-source-acquisition-pass-1.md"),
        "APO-112": ("independent-instrument-observability-confirmed", "analysis/company-first-principles/capital-flow-apollo-athene-concord-sec-nport-holder-observation-2026-09-16.md"),
    }
    for gate_id, (status, source_artifact) in expected.items():
        row = by_id[gate_id]
        if row["current_status"] != status:
            fail(f"Apollo named-asset gate {gate_id} grade changed unexpectedly")
        if row["source_artifact"] != source_artifact:
            fail(f"Apollo named-asset gate {gate_id} source changed unexpectedly")
        if not row["evidence_value"].strip() or not row["what_is_proven"].strip() or not row["missing_upgrade"].strip():
            fail(f"Apollo named-asset gate {gate_id} is incomplete")
        if not resolve_source(ledger, row["source_artifact"]).exists():
            fail(f"Apollo named-asset gate source missing: {row['source_artifact']}")


def verify_apollo_ba_lot_bridge() -> None:
    """Keep the corrected BA Part 2/3 lot-continuity controls reproducible."""
    for path in (
        APOLLO_BA_PART2,
        APOLLO_BA_PART2_RECON,
        APOLLO_BA_PART3,
        APOLLO_BA_PART3_MATCH,
        APOLLO_BA_CONTINUITY,
        APOLLO_BA_CONTINUITY_SUMMARY,
        APOLLO_BA_LOT_QUEUE,
        APOLLO_BA_SALE_CROSSWALK,
    ):
        if not path.exists():
            fail(f"Apollo BA lot-bridge artifact missing: {path.relative_to(ROOT)}")

    with APOLLO_BA_PART2.open(newline="", encoding="utf-8") as handle:
        part2 = list(csv.DictReader(handle))
    if len(part2) != 184:
        fail(f"Apollo BA Part 2 row count changed: {len(part2)}")

    with APOLLO_BA_PART2_RECON.open(newline="", encoding="utf-8") as handle:
        recon = {row["metric"]: row for row in csv.DictReader(handle)}
    expected_recon = {
        "actual_cost_at_time_of_acquisition": ("6030604899", "6030604898", "1"),
        "additional_investment_made_after_acquisition": ("3822866876", "3822866876", "0"),
    }
    for metric, expected_values in expected_recon.items():
        row = recon.get(metric)
        if row is None or tuple(row[field] for field in ("parser_value", "control_value", "difference")) != expected_values:
            fail(f"Apollo BA Part 2 reconciliation changed: {metric}")

    with APOLLO_BA_PART3.open(newline="", encoding="utf-8") as handle:
        part3 = list(csv.DictReader(handle))
    if len(part3) != 168:
        fail(f"Apollo BA Part 3 row count changed: {len(part3)}")
    consideration = sum(int(row["disposal_consideration"].replace(",", "").replace("(", "-").replace(")", "") or 0) for row in part3)
    if consideration != 4417190618:
        fail(f"Apollo BA Part 3 consideration control changed: {consideration}")

    with APOLLO_BA_PART3_MATCH.open(newline="", encoding="utf-8") as handle:
        matches = list(csv.DictReader(handle))
    if len(matches) != 168 or sum(row["match_status"] == "same-cusip-part1-and-part3-visible" for row in matches) != 65:
        fail("Apollo BA Part 3/Part 1 match controls changed")

    with APOLLO_BA_CONTINUITY.open(newline="", encoding="utf-8") as handle:
        continuity = list(csv.DictReader(handle))
    statuses = {}
    for row in continuity:
        statuses[row["continuity_status"]] = statuses.get(row["continuity_status"], 0) + 1
    expected_statuses = {
        "blank-cusip-event-no-continuity-key": 84,
        "part3-cusip-no-part1-or-part2-match": 2,
        "same-cusip-part1-and-part2-and-part3-visible": 61,
        "same-cusip-part1-and-part3-visible": 4,
        "same-cusip-part2-and-part3-visible": 17,
    }
    if len(continuity) != 168 or statuses != expected_statuses:
        fail(f"Apollo BA continuity status controls changed: {statuses}")

    with APOLLO_BA_LOT_QUEUE.open(newline="", encoding="utf-8") as handle:
        lot_queue = list(csv.DictReader(handle))
    tiers = {}
    for row in lot_queue:
        tiers[row["screen_tier"]] = tiers.get(row["screen_tier"], 0) + 1
    if len(lot_queue) != 10 or tiers != {"exact-within-$1": 4, "near-within-$1M": 6}:
        fail(f"Apollo BA lot-review queue changed: {tiers}")

    expected_lot_ids = {
        "309601-AE-2": "exact-within-$1",
        "05565A-DW-0": "exact-within-$1",
        "539439-BF-5": "exact-within-$1",
        "639057-AT-5": "exact-within-$1",
        "401378-AB-0": "near-within-$1M",
        "89116C-4H-7": "near-within-$1M",
        "401378-AA-2": "near-within-$1M",
        "018820-AE-0": "near-within-$1M",
        "05254H-AA-2": "near-within-$1M",
        "37187A-AL-8": "near-within-$1M",
    }
    queue_by_id = {row["cusip_or_identifier"]: row for row in lot_queue}
    if set(queue_by_id) != set(expected_lot_ids):
        fail("Apollo BA lot-review identifier set changed")
    for identifier, expected_tier in expected_lot_ids.items():
        if queue_by_id[identifier]["screen_tier"] != expected_tier:
            fail(f"Apollo BA lot-review tier changed: {identifier}")

    with APOLLO_BA_PART1.open(newline="", encoding="utf-8") as handle:
        part1_ids = {row["cusip_or_identifier"] for row in csv.DictReader(handle)}
    with APOLLO_BA_PART2.open(newline="", encoding="utf-8") as handle:
        part2_ids = {row["cusip_or_identifier"] for row in csv.DictReader(handle)}
    with APOLLO_BA_PART3.open(newline="", encoding="utf-8") as handle:
        part3_ids = {row["cusip_or_identifier"] for row in csv.DictReader(handle)}
    for identifier in expected_lot_ids:
        if not {identifier}.issubset(part1_ids & part2_ids & part3_ids):
            fail(f"Apollo BA lot-review source-row continuity changed: {identifier}")

    with APOLLO_BA_SALE_CROSSWALK.open(newline="", encoding="utf-8") as handle:
        sale_crosswalk = list(csv.DictReader(handle))
    if len(sale_crosswalk) != 3 or len({row["ba_cusip"] for row in sale_crosswalk}) != 3:
        fail("Apollo BA sale crosswalk control changed")

    if not APOLLO_BA_EXACT_LOT_REVIEW.exists():
        fail(f"Apollo BA exact-lot page review missing: {APOLLO_BA_EXACT_LOT_REVIEW.relative_to(ROOT)}")
    with APOLLO_BA_EXACT_LOT_REVIEW.open(newline="", encoding="utf-8") as handle:
        exact_review = list(csv.DictReader(handle))
    expected_exact_review = {
        "309601-AE-2": "source-column-sale-with-exact-book-continuity",
        "05565A-DW-0": "blank-disposal-nature-with-two-times-part2-cost",
        "539439-BF-5": "source-column-sale-with-exact-book-continuity",
        "639057-AT-5": "blank-disposal-nature-with-two-times-part2-cost",
    }
    review_by_id = {row["identifier"]: row for row in exact_review}
    if set(review_by_id) != set(expected_exact_review):
        fail("Apollo BA exact-lot page-review identifier set changed")
    for identifier, expected_classification in expected_exact_review.items():
        row = review_by_id[identifier]
        if row["classification"] != expected_classification or row["current_status"] != "reviewed-statutory-continuity-only":
            fail(f"Apollo BA exact-lot page-review classification changed: {identifier}")


def verify_apollo_ba_income_queue() -> None:
    """Keep the named statutory income prioritization screen bounded."""
    if not APOLLO_BA_INCOME_QUEUE.exists():
        fail(f"Apollo BA income queue missing: {APOLLO_BA_INCOME_QUEUE.relative_to(ROOT)}")
    for path in (APOLLO_AP_GRANGE_BRIDGE, APOLLO_AP_GRANGE_SEARCH_BOUNDARY):
        if not path.exists():
            fail(f"Apollo AP Grange boundary missing: {path.relative_to(ROOT)}")
    for path in (APOLLO_AP_GRANGE_BRIDGE, APOLLO_AP_GRANGE_SEARCH_BOUNDARY):
        text = path.read_text(encoding="utf-8")
        if "https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm" not in text:
            fail(f"Apollo AP Grange source route is not canonical SEC: {path.name}")
    if not APOLLO_AP_GRANGE_CALL_STATUTORY.exists():
        fail(f"Apollo AP Grange call/statutory ledger missing: {APOLLO_AP_GRANGE_CALL_STATUTORY.relative_to(ROOT)}")
    with APOLLO_AP_GRANGE_CALL_STATUTORY.open(newline="", encoding="utf-8") as handle:
        grange_rows = list(csv.DictReader(handle))
    if [row["bridge_id"] for row in grange_rows] != ["APG-001", "APG-002", "APG-003", "APG-004", "APG-005", "APG-006", "APG-007", "APG-008"]:
        fail("Apollo AP Grange call/statutory bridge identifiers changed")
    grange_by_id = {row["bridge_id"]: row for row in grange_rows}
    expected_grange = {
        "APG-001": ("5662 USD millions", "issuer-concentration-visible"),
        "APG-002": ("5080 USD millions", "issuer-concentration-visible"),
        "APG-003": ("673 USD millions", "issuer-call-gain-visible"),
        "APG-004": ("411.998739 USD millions book; 31.661927 USD millions investment income", "statutory-holding-visible"),
        "APG-005": ("396.661750 USD millions acquisition cost; 33.407636 USD millions additional investment", "statutory-addition-visible"),
        "APG-006": ("313313 USD consideration; nature blank", "statutory-event-unclassified"),
        "APG-007": ("04/10/2026 disposal; Various purchaser; $4,052,553,175 consideration; $3,687,230,219 par value; $3,690,374,758 actual cost; $3,691,539,180 book at disposal; $(4,308,961) total disposal loss; $414,342,613 bond interest received during year", "statutory-settlement-candidate"),
        "APG-008": ("no G2964#-AB-5 or second AP Grange row found in checked Part 3/4 pages 2457-2598", "statutory-negative-control"),
    }
    for bridge_id, (value, status) in expected_grange.items():
        row = grange_by_id[bridge_id]
        if row["observed_value"] != value or row["status"] != status:
            fail(f"Apollo AP Grange call/statutory bridge changed: {bridge_id}")
        if not row["what_is_proven"].strip() or not row["missing_join"].strip():
            fail(f"Apollo AP Grange call/statutory bridge incomplete: {bridge_id}")
        if not resolve_source(APOLLO_AP_GRANGE_CALL_STATUTORY, row["source_artifact"]).exists():
            fail(f"Apollo AP Grange call/statutory source missing: {row['source_artifact']}")
    if not APOLLO_BA_INCOME_RECONCILIATION.exists():
        fail(f"Apollo BA income reconciliation missing: {APOLLO_BA_INCOME_RECONCILIATION.relative_to(ROOT)}")
    with APOLLO_BA_INCOME_RECONCILIATION.open(newline="", encoding="utf-8") as handle:
        income_reconciliation = list(csv.DictReader(handle))
    if len(income_reconciliation) != 5:
        fail(f"Apollo BA income reconciliation row count changed: {len(income_reconciliation)}")
    expected_income_results = {
        "BAINC-001": ("237086006", "237086005", "1"),
        "BAINC-002": ("237086006", "-185080219", "422166225"),
        "BAINC-003": ("237086006", "-132204517", "369290523"),
        "BAINC-004": ("156037953", "", "156037953"),
        "BAINC-005": ("182801164", "237086006", "77.10%"),
    }
    by_reconciliation_id = {row["reconciliation_id"]: row for row in income_reconciliation}
    if set(by_reconciliation_id) != set(expected_income_results):
        fail("Apollo BA income reconciliation identifiers changed")
    for reconciliation_id, expected_values in expected_income_results.items():
        row = by_reconciliation_id[reconciliation_id]
        actual = (row["numerator_or_observed_value"], row["denominator_or_comparison_value"], row["arithmetic_result"])
        if actual != expected_values:
            fail(f"Apollo BA income reconciliation changed: {reconciliation_id}")
    if not APOLLO_PAGE18_NII.exists():
        fail(f"Apollo page-18 income table missing: {APOLLO_PAGE18_NII.relative_to(ROOT)}")
    with APOLLO_PAGE18_NII.open(newline="", encoding="utf-8") as handle:
        page18_rows = list(csv.DictReader(handle))
    if len(page18_rows) != 16:
        fail(f"Apollo page-18 income table row count changed: {len(page18_rows)}")
    category_rows = [row for row in page18_rows if row["source_line"] != "10"]
    total_rows = [row for row in page18_rows if row["source_line"] == "10"]
    if len(category_rows) != 15 or len(total_rows) != 1:
        fail("Apollo page-18 income table category/control partition changed")
    collected_sum = sum(int(row["collected_during_year"] or 0) for row in category_rows)
    earned_sum = sum(int(row["earned_during_year"] or 0) for row in category_rows)
    total = total_rows[0]
    if (collected_sum, earned_sum, int(total["collected_during_year"]), int(total["earned_during_year"])) != (13601183682, 14010808604, 13601183683, 14010808604):
        fail("Apollo page-18 income table totals changed")
    if not APOLLO_SCHEDULE_D_INTEREST_REPAIR.exists():
        fail(f"Apollo Schedule D interest repair missing: {APOLLO_SCHEDULE_D_INTEREST_REPAIR.relative_to(ROOT)}")
    with APOLLO_SCHEDULE_D_INTEREST_REPAIR.open(newline="", encoding="utf-8") as handle:
        interest_repair = list(csv.DictReader(handle))
    if len(interest_repair) != 3:
        fail(f"Apollo Schedule D interest repair row count changed: {len(interest_repair)}")
    repair_by_id = {row["repair_id"]: row for row in interest_repair}
    if repair_by_id.get("SDINT-001", {}).get("new_parser_observation") != "Interest income blank and interest received blank":
        fail("Apollo Treasury interest-column repair changed")
    if repair_by_id.get("SDINT-002", {}).get("new_parser_observation") != "Interest income due/accrued `$7.219623M`; interest received `$230.263772M`":
        fail("Apollo AP Grange interest-column repair changed")
    if repair_by_id.get("SDINT-003", {}).get("new_parser_observation") != "Corrected received-interest sum `$6.230478121B`":
        fail("Apollo Schedule D aggregate interest-column repair changed")
    with APOLLO_BA_PART1.open(newline="", encoding="utf-8") as handle:
        _ = list(csv.DictReader(handle))
    schedule_d_path = LEDGER_DIR / "capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
    if not schedule_d_path.exists():
        fail(f"Apollo corrected Schedule D output missing: {schedule_d_path.relative_to(ROOT)}")
    with schedule_d_path.open(newline="", encoding="utf-8") as handle:
        schedule_d_rows = list(csv.DictReader(handle))
    by_cusip = {row["cusip"]: row for row in schedule_d_rows}
    treasury = by_cusip.get("912803-DM-2")
    ap_grange = by_cusip.get("G2964#-AA-7")
    if treasury is None or treasury["interest_income"] or treasury["interest_received_during_year"]:
        fail("Apollo Treasury corrected interest fields changed")
    if ap_grange is None or (ap_grange["interest_income"], ap_grange["interest_received_during_year"]) != ("7,219,623", "230,263,772"):
        fail("Apollo AP Grange corrected interest fields changed")
    def parse_amount(value: str) -> int:
        return int((value or "0").replace(",", "").replace("(", "-").replace(")", ""))
    received_total = sum(parse_amount(row["interest_received_during_year"]) for row in schedule_d_rows)
    if received_total != 6230478121:
        fail(f"Apollo Schedule D corrected received-interest total changed: {received_total}")
    if not APOLLO_PAGE18_SCHEDULE_D_PERIMETER.exists():
        fail(f"Apollo page-18/Schedule D perimeter bridge missing: {APOLLO_PAGE18_SCHEDULE_D_PERIMETER.relative_to(ROOT)}")
    with APOLLO_PAGE18_SCHEDULE_D_PERIMETER.open(newline="", encoding="utf-8") as handle:
        perimeter_rows = list(csv.DictReader(handle))
    if len(perimeter_rows) != 9:
        fail(f"Apollo page-18/Schedule D perimeter bridge row count changed: {len(perimeter_rows)}")
    perimeter_by_id = {row["bridge_id"]: row for row in perimeter_rows}
    expected_perimeter = {
        "P18SDP-001": ("0", "source-controlled"),
        "P18SDP-002": ("0", "source-controlled"),
        "P18SDP-003": ("0", "source-controlled"),
        "P18SDP-004": ("0", "source-controlled"),
        "P18SDP-005": ("1897374415", "join-open"),
        "P18SDP-006": ("392923968", "definition-open"),
        "P18SDP-007": ("0", "source-visible"),
        "P18SDP-008": ("0", "source-visible"),
        "P18SDP-009": ("0", "source-visible"),
    }
    if set(perimeter_by_id) != set(expected_perimeter):
        fail("Apollo page-18/Schedule D perimeter bridge identifiers changed")
    for bridge_id, (expected_difference, expected_status) in expected_perimeter.items():
        row = perimeter_by_id[bridge_id]
        if row["difference_usd"] != expected_difference or row["current_status"] != expected_status:
            fail(f"Apollo page-18/Schedule D perimeter bridge changed: {bridge_id}")
    if not APOLLO_SCHEDULE_D_INTEREST_SUBTOTAL.exists():
        fail(f"Apollo Schedule D interest subtotal control missing: {APOLLO_SCHEDULE_D_INTEREST_SUBTOTAL.relative_to(ROOT)}")
    with APOLLO_SCHEDULE_D_INTEREST_SUBTOTAL.open(newline="", encoding="utf-8") as handle:
        subtotal_rows = list(csv.DictReader(handle))
    if len(subtotal_rows) != 3:
        fail(f"Apollo Schedule D interest subtotal control row count changed: {len(subtotal_rows)}")
    subtotal_by_id = {row["control_id"]: row for row in subtotal_rows}
    expected_subtotals = {
        "SDCTRL-001": ("888305222", "888305222", "3006747015", "3006747015", "subtotal-tied"),
        "SDCTRL-002": ("616145225", "616145225", "3223731106", "3223731106", "subtotal-tied"),
        "SDCTRL-003": ("1504450447", "1504450447", "6230478121", "6230478121", "combined-subtotal-tied"),
    }
    if set(subtotal_by_id) != set(expected_subtotals):
        fail("Apollo Schedule D interest subtotal control identifiers changed")
    for control_id, expected_values in expected_subtotals.items():
        row = subtotal_by_id[control_id]
        actual = (
            row["parser_interest_income_usd"],
            row["source_interest_income_usd"],
            row["parser_interest_received_usd"],
            row["source_interest_received_usd"],
            row["current_status"],
        )
        if actual != expected_values or row["interest_income_difference_usd"] != "0" or row["interest_received_difference_usd"] != "0":
            fail(f"Apollo Schedule D interest subtotal control changed: {control_id}")
    if not APOLLO_INCOME_POPULATION_BOUNDARY.exists():
        fail(f"Apollo income population boundary missing: {APOLLO_INCOME_POPULATION_BOUNDARY.relative_to(ROOT)}")
    with APOLLO_INCOME_POPULATION_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        population_rows = list(csv.DictReader(handle))
    if len(population_rows) != 6:
        fail(f"Apollo income population boundary row count changed: {len(population_rows)}")
    population_by_id = {row["boundary_id"]: row for row in population_rows}
    expected_population = {
        "INPOP-001": ("18", "source-controlled"),
        "INPOP-002": ("5836-5911", "source-controlled"),
        "INPOP-003": ("5912-6027", "source-controlled"),
        "INPOP-004": ("6074-6283", "source-controlled"),
        "INPOP-005": ("6284-6336", "source-controlled"),
        "INPOP-006": ("18+5836-6336", "population-join-open"),
    }
    if set(population_by_id) != set(expected_population):
        fail("Apollo income population boundary identifiers changed")
    for boundary_id, (expected_pages, expected_status) in expected_population.items():
        row = population_by_id[boundary_id]
        if row["source_page_or_range"] != expected_pages or row["current_status"] != expected_status:
            fail(f"Apollo income population boundary changed: {boundary_id}")
    if not APOLLO_PAGE18_SCHEDULE_D_RECONCILIATION.exists():
        fail(f"Apollo page-18/Schedule D income reconciliation missing: {APOLLO_PAGE18_SCHEDULE_D_RECONCILIATION.relative_to(ROOT)}")
    with APOLLO_PAGE18_SCHEDULE_D_RECONCILIATION.open(newline="", encoding="utf-8") as handle:
        reconciliation_rows = list(csv.DictReader(handle))
    if len(reconciliation_rows) != 6:
        fail(f"Apollo page-18/Schedule D income reconciliation row count changed: {len(reconciliation_rows)}")
    reconciliation_by_id = {row["reconciliation_id"]: row for row in reconciliation_rows}
    expected_reconciliation = {
        "P18SDR-001": ("8127852536", "source-controlled"),
        "P18SDR-002": ("6230478121", "subtotal-tied"),
        "P18SDR-003": ("2207402908", "subtotal-visible"),
        "P18SDR-004": ("-310028491", "source-controlled"),
        "P18SDR-005": ("8127852538", "near-reconciled-within-2"),
        "P18SDR-006": ("-2", "near-reconciled-within-2"),
    }
    if set(reconciliation_by_id) != set(expected_reconciliation):
        fail("Apollo page-18/Schedule D income reconciliation identifiers changed")
    for reconciliation_id, (expected_value, expected_status) in expected_reconciliation.items():
        row = reconciliation_by_id[reconciliation_id]
        if row["value_usd"] != expected_value or row["current_status"] != expected_status:
            fail(f"Apollo page-18/Schedule D income reconciliation changed: {reconciliation_id}")
    if not APOLLO_LEGAL_ENTITY_BRIDGE.exists():
        fail(f"Apollo legal-entity income bridge missing: {APOLLO_LEGAL_ENTITY_BRIDGE.relative_to(ROOT)}")
    with APOLLO_LEGAL_ENTITY_BRIDGE.open(newline="", encoding="utf-8") as handle:
        legal_bridge_rows = list(csv.DictReader(handle))
    if len(legal_bridge_rows) != 18:
        fail(f"Apollo legal-entity income bridge row count changed: {len(legal_bridge_rows)}")
    legal_bridge_by_id = {row["bridge_id"]: row for row in legal_bridge_rows}
    bridge_row = legal_bridge_by_id.get("CFAALEICB-006")
    if bridge_row is None or bridge_row["metric"] != "page18_collected_bond_income_to_schedule_d_reconstructed_bond_base":
        fail("Apollo legal-entity bridge collected-bond reconciliation row missing")
    if bridge_row["numerator_value"] != "8.127852536" or bridge_row["current_status"] != "near-reconciled-statutory-collected-bond-control":
        fail("Apollo legal-entity bridge collected-bond reconciliation changed")
    liability_bridge_row = legal_bridge_by_id.get("CFAALEICB-007")
    if liability_bridge_row is None or liability_bridge_row["metric"] != "net_investment_income_less_contract_or_deposit_interest_adjustments":
        fail("Apollo legal-entity bridge liability-burden row missing")
    if liability_bridge_row["numerator_value"] != "6.842002522" or liability_bridge_row["denominator_value"] != "12.732699320" or liability_bridge_row["current_status"] != "bounded-liability-burden-screen":
        fail("Apollo legal-entity bridge liability-burden row changed")
    individual_lob_row = legal_bridge_by_id.get("CFAALEICB-008")
    if individual_lob_row is None or individual_lob_row["metric"] != "individual_annuity_liability_interest_burden_to_summary_liability_interest":
        fail("Apollo legal-entity bridge individual-annuity allocation row missing")
    if individual_lob_row["numerator_value"] != "5.882288174" or individual_lob_row["denominator_value"] != "5.890696798" or individual_lob_row["current_status"] != "line-of-business-allocation-visible":
        fail("Apollo legal-entity bridge individual-annuity allocation changed")
    group_lob_row = legal_bridge_by_id.get("CFAALEICB-009")
    if group_lob_row is None or group_lob_row["metric"] != "group_annuity_liability_interest_burden_to_summary_liability_interest":
        fail("Apollo legal-entity bridge group-annuity allocation row missing")
    if group_lob_row["numerator_value"] != "0.008408625" or group_lob_row["denominator_value"] != "5.890696798" or group_lob_row["current_status"] != "line-of-business-allocation-visible":
        fail("Apollo legal-entity bridge group-annuity allocation changed")
    derivative_row = legal_bridge_by_id.get("CFAALEICB-010")
    if derivative_row is None or derivative_row["metric"] != "gross_derivative_assets_to_core_invested_asset_base":
        fail("Apollo legal-entity bridge derivative-scale row missing")
    if derivative_row["numerator_value"] != "2.482135218" or derivative_row["denominator_value"] != "270.261704399" or derivative_row["current_status"] != "hedge-scale-visible":
        fail("Apollo legal-entity bridge derivative-scale row changed")
    derivative_turnover_row = legal_bridge_by_id.get("CFAALEICB-011")
    if derivative_turnover_row is None or derivative_turnover_row["metric"] != "schedule_db_termination_considerations_to_part_a_ending_book_value":
        fail("Apollo legal-entity bridge derivative-turnover row missing")
    if derivative_turnover_row["numerator_value"] != "2.009384164" or derivative_turnover_row["denominator_value"] != "3.513012150" or derivative_turnover_row["current_status"] != "derivative-cash-control-visible":
        fail("Apollo legal-entity bridge derivative-turnover row changed")
    if not APOLLO_LIABILITY_BURDEN.exists():
        fail(f"Apollo liability-interest burden bridge missing: {APOLLO_LIABILITY_BURDEN.relative_to(ROOT)}")
    with APOLLO_LIABILITY_BURDEN.open(newline="", encoding="utf-8") as handle:
        liability_rows = list(csv.DictReader(handle))
    if len(liability_rows) != 6:
        fail(f"Apollo liability-interest burden bridge row count changed: {len(liability_rows)}")
    liability_by_id = {row["bridge_id"]: row for row in liability_rows}
    if liability_by_id.get("LIBUR-002", {}).get("value_usd") != "5890696798" or liability_by_id.get("LIBUR-002", {}).get("current_status") != "source-controlled":
        fail("Apollo liability-interest burden source line changed")
    if liability_by_id.get("LIBUR-003", {}).get("derived_difference_usd") != "6842002522" or liability_by_id.get("LIBUR-003", {}).get("current_status") != "bounded-liability-burden-screen":
        fail("Apollo liability-interest burden residual changed")
    if not APOLLO_LIABILITY_LOB.exists():
        fail(f"Apollo liability line-of-business allocation missing: {APOLLO_LIABILITY_LOB.relative_to(ROOT)}")
    with APOLLO_LIABILITY_LOB.open(newline="", encoding="utf-8") as handle:
        lob_rows = list(csv.DictReader(handle))
    if len(lob_rows) != 7:
        fail(f"Apollo liability line-of-business allocation row count changed: {len(lob_rows)}")
    lob_by_id = {row["bridge_id"]: row for row in lob_rows}
    if lob_by_id.get("LIBLOB-002", {}).get("value_usd") != "5882288174" or lob_by_id.get("LIBLOB-003", {}).get("value_usd") != "8408625":
        fail("Apollo liability line-of-business values changed")
    if lob_by_id.get("LIBLOB-004", {}).get("derived_difference_usd") != "1" or lob_by_id.get("LIBLOB-004", {}).get("current_status") != "near-reconciled-within-1":
        fail("Apollo liability line-of-business one-dollar control changed")
    if not APOLLO_DERIVATIVE_HEDGE.exists():
        fail(f"Apollo derivative hedge boundary missing: {APOLLO_DERIVATIVE_HEDGE.relative_to(ROOT)}")
    with APOLLO_DERIVATIVE_HEDGE.open(newline="", encoding="utf-8") as handle:
        derivative_rows = list(csv.DictReader(handle))
    if len(derivative_rows) != 18:
        fail(f"Apollo derivative hedge boundary row count changed: {len(derivative_rows)}")
    derivative_by_id = {row["boundary_id"]: row for row in derivative_rows}
    if derivative_by_id.get("DERIV-001", {}).get("value_usd") != "2482135218" or derivative_by_id.get("DERIV-005", {}).get("value_usd") != "112792182":
        fail("Apollo derivative hedge boundary values changed")
    if derivative_by_id.get("DERIV-008", {}).get("value_usd") != "2009384164" or derivative_by_id.get("DERIV-014", {}).get("value_usd") != "108756075":
        fail("Apollo Schedule DB derivative cash controls changed")
    if derivative_by_id.get("DERIV-016", {}).get("value_usd") != "1" or derivative_by_id.get("DERIV-017", {}).get("value_usd") != "1" or derivative_by_id.get("DERIV-018", {}).get("value_usd") != "0":
        fail("Apollo Schedule DB verification controls changed")
    if not APOLLO_SCHEDULE_DB_PART_C.exists():
        fail(f"Apollo Schedule DB Part C ledger missing: {APOLLO_SCHEDULE_DB_PART_C.relative_to(ROOT)}")
    with APOLLO_SCHEDULE_DB_PART_C.open(newline="", encoding="utf-8") as handle:
        part_c_rows = list(csv.DictReader(handle))
    if len(part_c_rows) != 735:
        fail(f"Apollo Schedule DB Part C ledger row count changed: {len(part_c_rows)}")
    mf1_rows = [row for row in part_c_rows if row["cash_instrument_cusip"] == "592918-AE-6" and row["cash_instrument_description"] == "MF1 2025-B2 B"]
    if len(mf1_rows) != 1 or mf1_rows[0]["derivative_identifier"] != "04687#AB4" or mf1_rows[0]["row_mapping_status"] != "source-row-visible-component-columns-resolved":
        fail("Apollo Schedule DB Part C MF1 2025-B2 B identity bridge changed")
    if any("settlement" not in row["boundary"] or "owner cash" not in row["boundary"] for row in part_c_rows):
        fail("Apollo Schedule DB Part C ledger boundary overclaims cash")
    if not APOLLO_SCHEDULE_DB_PART_C_SCHEDULE_D.exists():
        fail(f"Apollo Schedule DB Part C/Schedule D crosswalk missing: {APOLLO_SCHEDULE_DB_PART_C_SCHEDULE_D.relative_to(ROOT)}")
    with APOLLO_SCHEDULE_DB_PART_C_SCHEDULE_D.open(newline="", encoding="utf-8") as handle:
        crosswalk_rows = list(csv.DictReader(handle))
    if len(crosswalk_rows) != 743:
        fail(f"Apollo Schedule DB Part C/Schedule D crosswalk row count changed: {len(crosswalk_rows)}")
    if len({row["part_c_ledger_id"] for row in crosswalk_rows}) != 728 or len({row["cash_instrument_cusip"] for row in crosswalk_rows}) != 586:
        fail("Apollo Schedule DB Part C/Schedule D crosswalk match counts changed")
    mf1_crosswalk = [row for row in crosswalk_rows if row["cash_instrument_cusip"] == "592918-AE-6"]
    if len(mf1_crosswalk) != 1 or mf1_crosswalk[0]["schedule_d_book_adjusted_carrying_value"] != "57,647,000" or mf1_crosswalk[0]["schedule_d_interest_received_during_year"] != "2,526,028":
        fail("Apollo Schedule DB Part C/Schedule D MF1 crosswalk changed")
    if not APOLLO_SCHEDULE_DB_PART_C_NAMED_LOT.exists():
        fail(f"Apollo Schedule DB named-lot control missing: {APOLLO_SCHEDULE_DB_PART_C_NAMED_LOT.relative_to(ROOT)}")
    with APOLLO_SCHEDULE_DB_PART_C_NAMED_LOT.open(newline="", encoding="utf-8") as handle:
        named_lot_rows = list(csv.DictReader(handle))
    if len(named_lot_rows) != 52:
        fail(f"Apollo Schedule DB named-lot control row count changed: {len(named_lot_rows)}")
    if {row["named_family"] for row in named_lot_rows} != {"MF1", "AMAPS", "ATLAS", "VARDE", "ARES"}:
        fail("Apollo Schedule DB named-lot family set changed")
    if sum(row["numeric_control_status"] == "matched-identity-component-exposure-control" for row in named_lot_rows) != 51:
        fail("Apollo Schedule DB named-lot unambiguous control count changed")
    mf1_named = [row for row in named_lot_rows if row["cash_instrument_cusip"] == "592918-AE-6"]
    if len(mf1_named) != 1 or mf1_named[0]["part_c_book_candidate_sum_used"] != "2,882,000" or mf1_named[0]["schedule_d_book_value_sum"] != "57,647,000":
        fail("Apollo Schedule DB named-lot MF1 component control changed")
    if any("settlement" not in row["boundary"] or "owner cash" not in row["boundary"] for row in named_lot_rows):
        fail("Apollo Schedule DB named-lot boundary overclaims cash")
    if not APOLLO_SCHEDULE_DB_PART_C_NAMED_LOT_QUEUE.exists():
        fail(f"Apollo Schedule DB named-lot acquisition queue missing: {APOLLO_SCHEDULE_DB_PART_C_NAMED_LOT_QUEUE.relative_to(ROOT)}")
    with APOLLO_SCHEDULE_DB_PART_C_NAMED_LOT_QUEUE.open(newline="", encoding="utf-8") as handle:
        queue_rows = list(csv.DictReader(handle))
    if len(queue_rows) != 52 or {row["priority_tier"] for row in queue_rows} != {"A", "B", "C"}:
        fail("Apollo Schedule DB named-lot acquisition queue population changed")
    tier_counts = {tier: sum(row["priority_tier"] == tier for row in queue_rows) for tier in ("A", "B", "C")}
    if tier_counts != {"A": 8, "B": 30, "C": 14}:
        fail(f"Apollo Schedule DB named-lot acquisition queue tier counts changed: {tier_counts}")
    if queue_rows[0]["cash_instrument_cusip"] != "02300A-AA-8" or queue_rows[0]["priority_tier"] != "A":
        fail("Apollo Schedule DB named-lot acquisition queue top route changed")
    if any("cash" not in row["current_boundary"] or "settlement" not in row["current_boundary"] for row in queue_rows):
        fail("Apollo Schedule DB named-lot acquisition queue boundary overclaims cash")
    with APOLLO_BA_INCOME_QUEUE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 30 or rows[0]["rank"] != "1" or rows[0]["cusip_or_identifier"] != "G2964#-AB-5":
        fail("Apollo BA income queue population or top route changed")
    if rows[0]["investment_income"] != "$31,661,927" or rows[0]["part3_event_count"] != "1":
        fail("Apollo BA income queue AP Grange anchor changed")
    if rows[9]["cusip_or_identifier"] != "7620ET-AA-7" or rows[9]["part3_consideration_sum"] != "$20,000,000":
        fail("Apollo BA income queue RGA anchor changed")
    if any("not collected cash" not in row["boundary"] or "owner cash" not in row["boundary"] for row in rows):
        fail("Apollo BA income queue boundary overclaims cash")


def verify_apollo_q2_amaps_source() -> None:
    if not APOLLO_Q2_AMAPS_SOURCE.exists():
        fail(f"missing preserved Athene Q2 AMAPS source: {APOLLO_Q2_AMAPS_SOURCE.relative_to(ROOT)}")
    text = APOLLO_Q2_AMAPS_SOURCE.read_text(encoding="utf-8", errors="ignore")
    required_markers = (
        "Investment-grade ABS debt issued by AMAPS 1, LLC",
        ">2,544<",
        ">2,550<",
    )
    for marker in required_markers:
        if marker not in text:
            fail(f"Athene Q2 AMAPS source marker missing: {marker}")
    with APOLLO_Q2_AMAPS_EXPOSURE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["period", "wrapper", "exposure_musd", "source_artifact", "status", "boundary"]
        if reader.fieldnames != expected_header:
            fail(f"Athene Q2 AMAPS exposure header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [(row["period"], row["exposure_musd"]) for row in rows] != [("2025-12-31", "2550"), ("2026-06-30", "2544")]:
        fail("Athene Q2 AMAPS exposure rows changed")
    if int(rows[1]["exposure_musd"]) - int(rows[0]["exposure_musd"]) != -6:
        fail("Athene Q2 AMAPS exposure movement arithmetic failed")
    for row in rows:
        if row["wrapper"] != "AMAPS 1 LLC" or row["status"] != "reported-wrapper-exposure":
            fail(f"Athene Q2 AMAPS exposure row boundary changed: {row}")
        if not row["source_artifact"].strip() or not row["boundary"].strip():
            fail(f"Athene Q2 AMAPS exposure row incomplete: {row}")


def verify_concord_source_acquisition_boundary() -> None:
    if not CONCORD_SOURCE_ACQUISITION.exists():
        fail(f"missing Concord public acquisition boundary: {CONCORD_SOURCE_ACQUISITION.relative_to(ROOT)}")
    memo = CONCORD_SOURCE_ACQUISITION.read_text(encoding="utf-8")
    required_markers = (
        "Series 2025-3 new-issue report is located but premium-gated",
        "accessible July 2026 surveillance page",
        "No row upgraded to Athene receipt proof",
        "No row upgraded to return-model proof",
    )
    for marker in required_markers:
        if marker not in memo:
            fail(f"Concord acquisition boundary marker missing: {marker}")
    with CONCORD_SOURCE_ACQUISITION_DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    report = next((row for row in rows if row["request_id"] == "CFAACNCDR-008"), None)
    if report is None:
        fail("Concord KBRA report acquisition row missing")
    if report["route_status"] != "located-premium-access-controlled":
        fail("Concord KBRA report route overclaims access")
    for marker in ("ZTyQYFzg", "xpNPQytP"):
        if marker not in report["route_url"]:
            fail(f"Concord KBRA route marker missing: {marker}")
    if "timely interest" not in report["found_document_or_signal"]:
        fail("Concord accessible surveillance signal missing")


def verify_concord_sec_nport_observation() -> None:
    ledger = PILOT_LEDGERS[2]
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = {row["gate_id"]: row for row in csv.DictReader(handle)}
    row = rows.get("APO-112")
    if row is None:
        fail("Concord SEC N-PORT observation gate missing")
    source = resolve_source(ledger, row["source_artifact"])
    if not source.exists():
        fail(f"Concord SEC N-PORT source missing: {row['source_artifact']}")
    memo = source.read_text(encoding="utf-8")
    for marker in (
        "20633KAE8",
        "200,000",
        "$197,037.56",
        "does not establish",
        "Athene ownership",
        "2024-1A and 2025-3A CUSIPs",
    ):
        if marker not in memo:
            fail(f"Concord SEC N-PORT boundary marker missing: {marker}")
    if row["current_status"] != "independent-instrument-observability-confirmed":
        fail("Concord SEC N-PORT observation overclaims evidence")
    if "sec.gov/Archives/edgar/data/1478482/000114554925042590" not in memo:
        fail("Concord SEC N-PORT source URL missing")


def verify_apollo_related_party_ledger_gates() -> None:
    ledger = PILOT_LEDGERS[2]
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    by_id = {row["gate_id"]: row for row in rows}
    expected = {
        "APO-035": ("fee-payable-boundary-visible", "785M USD H1 management fees incurred; 140M USD payable at June 30 2026 versus 134M USD at prior year end"),
        "APO-036": ("named-asset-transfer-visible", "8.7B USD including accrued interest purchased from ARI on April 24 2026"),
        "APO-037": ("contingent-fee-boundary-visible", "392M USD at June 30 2026 versus 365M USD at December 31 2025"),
        "APO-038": ("related-party-credit-exposure-visible", "33207M USD amortized cost; 33078M USD fair value; 1M USD allowance at June 30 2026"),
        "APO-039": ("portfolio-credit-risk-visible", "1027M USD unpaid principal and 695M USD fair value at June 30 2026"),
        "APO-040": ("portfolio-loss-boundary-visible", "44M USD mortgage instrument-specific credit-risk loss and 61M USD intent-to-sell impairments in H1 2026"),
        "APO-041": ("primary-source-confirmed", "654M USD common-stock dividends paid in H1 2026"),
        "APO-042": ("primary-source-confirmed", "729M USD repurchases paid in H1 2026"),
        "APO-043": ("primary-source-confirmed", "49M USD preferred dividends paid in H1 2026"),
        "APO-044": ("source-search-boundary-confirmed", "No separately tagged upstream receipt fact surfaced in the accession-specific dividend distribution intercompany affiliate search"),
        "APO-046": ("entity-dividend-boundary-confirmed", "Athene 375M USD common dividends 71M USD preferred dividends 301M USD NCI distributions and 42M USD parent contribution; Apollo 654M USD common dividends 729M USD repurchases and 49M USD preferred dividends; no Apollo-specific upstream receipt joined"),
        "APO-047": ("legal-entity-income-cash-bridge-visible", "12.732699320B USD net investment income; 12.281980822B USD cash-flow net investment income; 13.601183683B USD collected gross investment income; 8.127852536B USD page-18 collected bond income reconstructed from Schedule D Parts 1/4/5 within $2; 6.230478121B USD corrected Schedule D interest received; 54.035221430B USD bond sale maturity or repayment proceeds; 158.619095705B USD parsed Schedule D bond base; 5.890696798B USD contract/deposit liability burden; 6.842002522B USD bounded residual after that burden; 2.482135218B USD gross derivative assets; 52 named Part C CUSIP controls"),
        "APO-048": ("completed-related-party-sale-and-seller-cash-use-visible", "Completed April 24 2026 cash sale to Athene based on 99.7 percent of loan commitments subject to adjustments; approximately 2.2B USD post-sale total assets primarily cash after debt and expenses; approximately 1.4B USD expected net cash and 1.7B USD common equity in proxy"),
        "APO-049": ("collateral-control-boundary-visible", "Proxy representations cover no unapproved collateral release; no cross-default or cross-collateralization; seller ownership free of liens other than permitted liens; and schedules for principal balances unfunded advances and reserve deposits"),
        "APO-050": ("parent-liquidity-source-route-visible", "Apollo is a holding company; distributions and other intercompany transfers from operating subsidiaries including Apollo Asset Management and Athene are identified as primary expected sources for parent dividends and other cash requirements; no dated Athene-to-parent receipt is joined"),
        "APO-051": ("legal-entity-gross-yield-screen-visible", "Collected bond income 7.859004314B USD divided by 158.852395201B USD statutory bond base equals 4.9474%; collected mortgage-loan income 4.557162846B USD divided by 84.664838463B USD first-lien mortgage base equals 5.3826%; net investment income divided by core invested asset base equals 4.7112%"),
        "APO-052": ("spread-dollar-screen-visible", "7.8B USD net investment earnings less 5.7B USD cost of funds equals 2.1B USD pre-tax spread contribution screen; reported net investment spread 1.41% versus 1.62% prior year, a 21 basis-point or approximately 13.0% relative compression"),
        "APO-113": ("bounded-liability-burden-screen", "$12.732699320B net investment income less $5.890696798B interest and adjustments on contract or deposit-type contract funds equals $6.842002522B; 53.7357% of net investment income"),
    }
    for gate_id, (status, evidence_value) in expected.items():
        if gate_id not in by_id:
            fail(f"Apollo related-party ledger gate missing: {gate_id}")
        row = by_id[gate_id]
        if row["current_status"] != status or row["evidence_value"] != evidence_value:
            fail(f"Apollo related-party ledger gate changed unexpectedly: {gate_id}")
        if not row["what_is_proven"].strip() or not row["missing_upgrade"].strip():
            fail(f"Apollo related-party ledger gate incomplete: {gate_id}")
        if not resolve_source(ledger, row["source_artifact"]).exists():
            fail(f"Apollo related-party ledger source missing: {row['source_artifact']}")


def verify_apollo_receipt_frontier() -> None:
    if not APOLLO_RECEIPT_FRONTIER.exists():
        fail(f"missing {APOLLO_RECEIPT_FRONTIER.relative_to(ROOT)}")
    with APOLLO_RECEIPT_FRONTIER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["case", "parent_receipt_musd", "athene_attribution_rate_pct", "mechanical_athene_attribution_musd", "common_owner_residual_musd", "status", "source_artifact", "interpretation"]
        if reader.fieldnames != expected_header:
            fail(f"Apollo receipt-frontier header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 5:
        fail(f"Apollo receipt frontier must contain 5 rows, found {len(rows)}")
    expected_rates = {"zero-attribution": 0, "quarter-attribution": 25, "half-attribution": 50, "three-quarter-attribution": 75, "full-attribution": 100}
    for row in rows:
        rate = expected_rates.get(row["case"])
        if rate is None or row["parent_receipt_musd"] != "750" or float(row["athene_attribution_rate_pct"]) != rate:
            fail(f"Apollo receipt-frontier input changed: {row}")
        expected_amount = 750 * rate / 100
        if not math.isclose(float(row["mechanical_athene_attribution_musd"]), expected_amount, rel_tol=0, abs_tol=0.001):
            fail(f"Apollo receipt-frontier arithmetic failed: {row}")
        if row["common_owner_residual_musd"] != "NA" or row["status"] != "sensitivity-only":
            fail(f"Apollo receipt-frontier boundary changed: {row}")
        if not resolve_source(APOLLO_RECEIPT_FRONTIER, row["source_artifact"]).exists():
            fail(f"Apollo receipt-frontier source missing: {row['source_artifact']}")


def verify_apollo_q2_receipt_frontier() -> None:
    if not APOLLO_Q2_RECEIPT_FRONTIER.exists():
        fail(f"missing Apollo Q2 receipt frontier: {APOLLO_Q2_RECEIPT_FRONTIER.relative_to(ROOT)}")
    with APOLLO_Q2_RECEIPT_FRONTIER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "attribution_case", "athene_h1_distributions_to_parent_musd",
            "assumed_agm_receipt_attribution_pct", "mechanical_attributed_amount_musd",
            "unrestricted_parent_cash_musd", "common_owner_residual_musd", "status",
            "source_artifact", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Apollo Q2 receipt-frontier header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 5:
        fail(f"Apollo Q2 receipt frontier must contain 5 rows, found {len(rows)}")
    expected_rates = {"0%": 0, "25%": 25, "50%": 50, "75%": 75, "100%": 100}
    for row in rows:
        rate = expected_rates.get(row["attribution_case"])
        if rate is None or row["athene_h1_distributions_to_parent_musd"] != "110":
            fail(f"Apollo Q2 receipt-frontier input changed: {row}")
        if float(row["assumed_agm_receipt_attribution_pct"]) != rate:
            fail(f"Apollo Q2 receipt-frontier rate changed: {row}")
        expected_amount = 110 * rate / 100
        if not math.isclose(float(row["mechanical_attributed_amount_musd"]), expected_amount, rel_tol=0, abs_tol=0.001):
            fail(f"Apollo Q2 receipt-frontier arithmetic failed: {row}")
        if row["unrestricted_parent_cash_musd"] != "NA" or row["common_owner_residual_musd"] != "NA":
            fail(f"Apollo Q2 receipt-frontier boundary changed: {row}")
        if row["status"] != "illustrative-attribution-frontier":
            fail(f"Apollo Q2 receipt-frontier status changed: {row}")
        if not resolve_source(APOLLO_Q2_RECEIPT_FRONTIER, row["source_artifact"]).exists():
            fail(f"Apollo Q2 receipt-frontier source missing: {row['source_artifact']}")


def verify_apollo_2026_credit_agreement_purpose() -> None:
    if not APOLLO_2026_CREDIT_AGREEMENT_PURPOSE.exists():
        fail(f"missing Apollo 2026 credit-agreement perimeter: {APOLLO_2026_CREDIT_AGREEMENT_PURPOSE.relative_to(ROOT)}")
    with APOLLO_2026_CREDIT_AGREEMENT_PURPOSE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "row_id", "source", "period", "field", "reported_value", "status_bucket",
            "proves", "does_not_prove", "next_required_source",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Apollo credit-agreement header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["row_id"] for row in rows] != [f"Q07CA-{index:03d}" for index in range(1, 8)]:
        fail("Apollo credit-agreement purpose rows changed unexpectedly")
    by_id = {row["row_id"]: row for row in rows}
    if by_id["Q07CA-001"]["status_bucket"] != "borrower-perimeter-visible":
        fail("Apollo credit-agreement borrower perimeter was promoted or downgraded")
    if by_id["Q07CA-002"]["reported_value"] != "1.750B USD" or by_id["Q07CA-002"]["status_bucket"] != "facility-capacity-visible":
        fail("Apollo credit-agreement commitment boundary changed")
    if by_id["Q07CA-006"]["status_bucket"] != "external-draw-closed-at-period-end":
        fail("Apollo external-facility quarter-end draw boundary changed")
    if "280M at 2026-03-31" not in by_id["Q07CA-007"]["reported_value"] or "279M at 2026-06-30" not in by_id["Q07CA-007"]["reported_value"]:
        fail("Apollo intercompany-note date control changed")
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"Apollo credit-agreement row incomplete: {row['row_id']}")
    for marker in ("cash", "receipt", "drawn balance", "actual use of proceeds"):
        if marker not in " ".join(row["does_not_prove"].lower() for row in rows):
            fail(f"Apollo credit-agreement perimeter lost boundary marker: {marker}")


def verify_apollo_intercompany_note_longitudinal() -> None:
    if not APOLLO_INTERCOMPANY_NOTE_LONGITUDINAL.exists():
        fail(f"missing Apollo intercompany-note longitudinal refresh: {APOLLO_INTERCOMPANY_NOTE_LONGITUDINAL.relative_to(ROOT)}")
    with APOLLO_INTERCOMPANY_NOTE_LONGITUDINAL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "search_id", "route", "as_of_date", "reported_balance_usd", "public_source",
            "source_url", "result_class", "proof_effect", "remaining_gap", "next_action",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Apollo intercompany-note header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["search_id"] for row in rows] != [f"ICNL-{index:03d}" for index in range(1, 9)]:
        fail("Apollo intercompany-note longitudinal rows changed unexpectedly")
    expected = {
        "ICNL-001": ("2022-12-31", "78000000"),
        "ICNL-002": ("2023-12-31", "109000000"),
        "ICNL-003": ("2024-12-31", "142000000"),
        "ICNL-004": ("2025-09-30", "226000000"),
        "ICNL-005": ("2025-12-31", "227000000"),
        "ICNL-006": ("2026-03-31", "280000000"),
        "ICNL-007": ("2026-06-30", "279000000"),
        "ICNL-008": ("2025-12-31", "227000000"),
    }
    for row in rows:
        if (row["as_of_date"], row["reported_balance_usd"]) != expected[row["search_id"]]:
            fail(f"Apollo intercompany-note observation changed: {row['search_id']}")
        if row["result_class"] not in {"partial-upgrade", "parent-side-cross-entity-corroboration"}:
            fail(f"Apollo intercompany-note row over-promoted: {row['search_id']}")
        if not row["source_url"].startswith("https://www.sec.gov/"):
            fail(f"Apollo intercompany-note source is not SEC-hosted: {row['search_id']}")
        if not row["remaining_gap"].strip() or not row["next_action"].strip():
            fail(f"Apollo intercompany-note upgrade path incomplete: {row['search_id']}")
    if "cash receipt" not in " ".join(row["remaining_gap"] for row in rows).lower():
        fail("Apollo intercompany-note longitudinal boundary lost cash-receipt language")


def verify_apollo_mf1_gross_proceeds_screen() -> None:
    if not APOLLO_MF1_GROSS_PROCEEDS_SCREEN.exists():
        fail(f"missing MF1 gross-proceeds screen: {APOLLO_MF1_GROSS_PROCEEDS_SCREEN.relative_to(ROOT)}")
    with APOLLO_MF1_GROSS_PROCEEDS_SCREEN.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "id", "metric", "value", "unit", "formula_or_source", "result_class",
            "boundary", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"MF1 gross-proceeds header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["id"] for row in rows] != [f"MF1RET-{index:03d}" for index in range(1, 9)]:
        fail("MF1 gross-proceeds rows changed unexpectedly")
    by_id = {row["id"]: row for row in rows}
    expected_values = {
        "MF1RET-001": "218271953",
        "MF1RET-002": "209559375",
        "MF1RET-003": "1302655",
        "MF1RET-004": "210862030",
        "MF1RET-007": "-7409923",
    }
    for row_id, value in expected_values.items():
        if by_id[row_id]["value"] != value:
            fail(f"MF1 gross-proceeds input changed: {row_id}")
    if not math.isclose(float(by_id["MF1RET-005"]["value"]), 209559375 / 218271953 * 100, abs_tol=0.0001):
        fail("MF1 consideration-to-holding ratio does not reconcile")
    if not math.isclose(float(by_id["MF1RET-006"]["value"]), 210862030 / 218271953 * 100, abs_tol=0.0001):
        fail("MF1 consideration-plus-income ratio does not reconcile")
    if by_id["MF1RET-008"]["result_class"] != "return-unproven" or by_id["MF1RET-008"]["unit"]:
        fail("MF1 gross-proceeds overall status was promoted")
    for row in rows:
        if not row["boundary"].strip() or not row["next_upgrade"].strip():
            fail(f"MF1 gross-proceeds promotion boundary incomplete: {row['id']}")
    for marker in ("Not proven cost basis", "Not bank settlement", "Not realized return", "Not gain loss"):
        if marker.lower() not in " ".join(row["boundary"].lower() for row in rows):
            fail(f"MF1 gross-proceeds boundary lost marker: {marker}")


def verify_apollo_mf1_same_cusip_join() -> None:
    if not APOLLO_MF1_SAME_CUSIP_JOIN.exists():
        fail(f"missing MF1 same-CUSIP servicing join: {APOLLO_MF1_SAME_CUSIP_JOIN.relative_to(ROOT)}")
    with APOLLO_MF1_SAME_CUSIP_JOIN.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "id", "gate", "source", "period", "observation", "result_class", "safe_use", "boundary", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"MF1 same-CUSIP join header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["id"] for row in rows] != [f"MF1JOIN-{index:03d}" for index in range(1, 6)]:
        fail("MF1 same-CUSIP join rows changed unexpectedly")
    by_id = {row["id"]: row for row in rows}
    if "592918-AA-4" not in by_id["MF1JOIN-001"]["observation"]:
        fail("MF1 same-CUSIP identity marker changed")
    if "209559375" not in by_id["MF1JOIN-003"]["observation"]:
        fail("MF1 same-CUSIP disposal consideration marker changed")
    if by_id["MF1JOIN-004"]["result_class"] != "servicing-route-visible":
        fail("MF1 servicing-route grade changed")
    if by_id["MF1JOIN-005"]["result_class"] != "partial-upgrade":
        fail("MF1 same-CUSIP promotion boundary changed")
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"MF1 same-CUSIP join row incomplete: {row['id']}")
    boundary_text = " ".join(row["boundary"].lower() for row in rows)
    for marker in ("athene legal ownership", "not bank settlement", "contractual mechanics", "apollo cash"):
        if marker not in boundary_text:
            fail(f"MF1 same-CUSIP join boundary lost marker: {marker}")


def verify_apollo_mf1_remittance_access() -> None:
    if not APOLLO_MF1_REMITTANCE_ACCESS.exists():
        fail(f"missing MF1 remittance-access boundary: {APOLLO_MF1_REMITTANCE_ACCESS.relative_to(ROOT)}")
    with APOLLO_MF1_REMITTANCE_ACCESS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "search_id", "route", "result_class", "observed_boundary", "source_url",
            "local_source_artifact", "next_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"MF1 remittance-access header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["search_id"] for row in rows] != ["MF1-RAB-001", "MF1-RAB-002", "MF1-RAB-003"]:
        fail("MF1 remittance-access rows changed unexpectedly")
    by_id = {row["search_id"]: row for row in rows}
    if by_id["MF1-RAB-001"]["result_class"] != "located-access-controlled":
        fail("MF1 CTSLink access state was promoted or downgraded")
    for row_id in ("MF1-RAB-002", "MF1-RAB-003"):
        if by_id[row_id]["result_class"] != "public-source-confirmed":
            fail(f"MF1 public mechanics source grade changed: {row_id}")
    if "sign-in" not in by_id["MF1-RAB-001"]["observed_boundary"].lower():
        fail("MF1 CTSLink sign-in boundary missing")
    if "23" not in by_id["MF1-RAB-002"]["observed_boundary"] or "74" not in by_id["MF1-RAB-002"]["observed_boundary"]:
        fail("MF1 collateral population boundary changed")
    if "collection accounts" not in by_id["MF1-RAB-003"]["observed_boundary"].lower():
        fail("MF1 servicing mechanics boundary changed")
    for row in rows:
        if not row["source_url"].startswith(("https://www.ctslink.com/", "https://www.sec.gov/")):
            fail(f"MF1 remittance source route changed: {row['search_id']}")
        if not row["next_upgrade"].strip() or not row["local_source_artifact"].strip():
            fail(f"MF1 remittance upgrade path incomplete: {row['search_id']}")


def verify_apollo_supplement_boundary() -> None:
    if not APOLLO_SUPPLEMENT_BOUNDARY.exists():
        fail(f"missing {APOLLO_SUPPLEMENT_BOUNDARY.relative_to(ROOT)}")
    with APOLLO_SUPPLEMENT_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["gate_id", "source", "period", "search_terms", "observed_fields", "current_status", "what_is_proven", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"Apollo supplement-boundary header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 1 or rows[0]["gate_id"] != "APO-SUP-001":
        fail("Apollo supplement-boundary rows changed")
    row = rows[0]
    if row["current_status"] != "source-search-boundary-confirmed" or "Athene-to-AGM" not in row["what_is_proven"]:
        fail("Apollo supplement-boundary status or claim changed")
    for field in ("source", "period", "search_terms", "observed_fields", "what_is_proven", "missing_upgrade"):
        if not row[field].strip():
            fail(f"Apollo supplement-boundary row incomplete: {field}")


def verify_apollo_liquidity_boundary() -> None:
    if not APOLLO_LIQUIDITY_BOUNDARY.exists():
        fail(f"missing {APOLLO_LIQUIDITY_BOUNDARY.relative_to(ROOT)}")
    with APOLLO_LIQUIDITY_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["gate_id", "source", "period", "metric", "value", "status", "what_is_proven", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"Apollo liquidity-boundary header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["gate_id"] for row in rows] != ["APO-LIQ-001", "APO-LIQ-002", "APO-LIQ-003", "APO-LIQ-004"]:
        fail("Apollo liquidity-boundary rows changed")
    expected_values = {"APO-LIQ-001": "36%", "APO-LIQ-002": "54%", "APO-LIQ-003": "$3.2B payable / $3.4B collateral", "APO-LIQ-004": "$6.0B payable / $6.2B collateral"}
    for row in rows:
        if row["value"] != expected_values[row["gate_id"]] or not row["what_is_proven"].strip() or not row["missing_upgrade"].strip():
            fail(f"Apollo liquidity-boundary row changed: {row}")


def verify_apollo_holdco_summary_context() -> None:
    if not APOLLO_HOLDCO_BOUNDARY.exists():
        fail(f"missing Apollo HoldCo boundary: {APOLLO_HOLDCO_BOUNDARY.relative_to(ROOT)}")
    memo = APOLLO_HOLDCO_BOUNDARY.read_text(encoding="utf-8")
    required_markers = (
        "## Parent-level liquidity context",
        "Cash and cash equivalents | `$3.412B`",
        "Investments, net | `$3.467B`",
        "Accrued performance fees receivable | `$1.511B`",
        "Net clawback payable | `$(95M)`",
        "Debt | `$(5.762B)`",
        "Net balance sheet value | `$2.533B`",
        "Shares outstanding | `624M`",
        "therefore must not be used as common-owner",
    )
    for marker in required_markers:
        if marker not in memo:
            fail(f"Apollo HoldCo summary marker missing: {marker}")
    ledger = PILOT_LEDGERS[2]
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = {row["gate_id"]: row for row in csv.DictReader(handle)}
    row = rows.get("APO-089")
    if row is None or "$3.412B" not in row["evidence_value"] or "$2.533B" not in row["evidence_value"]:
        fail("Apollo APO-089 ledger lacks the parent-summary balance-sheet context")
    if "parent-summary balance-sheet context" not in row["what_is_proven"]:
        fail("Apollo APO-089 proof boundary does not describe the parent-summary context")


def verify_apollo_company_distribution_route() -> None:
    ledger = PILOT_LEDGERS[2]
    with ledger.open(newline="", encoding="utf-8") as handle:
        rows = {row["gate_id"]: row for row in csv.DictReader(handle)}
    row = rows.get("APO-104")
    if row is None:
        fail("Apollo company-distribution route gate APO-104 is missing")
    expected_source = "analysis/company-first-principles/capital-flow-apollo-q2-fund-distributions-to-company-boundary-2026-09-15.md"
    if row["source_artifact"] != expected_source:
        fail("Apollo company-distribution route source changed unexpectedly")
    if row["current_status"] != "company-level-distribution-route-confirmed":
        fail("Apollo company-distribution route grade changed unexpectedly")
    if "$799M" not in row["evidence_value"] or "$2.040B" not in row["evidence_value"]:
        fail("Apollo company-distribution route values are incomplete")
    if not row["what_is_proven"].strip() or not row["missing_upgrade"].strip():
        fail("Apollo company-distribution route boundary is incomplete")
    if not resolve_source(ledger, row["source_artifact"]).exists():
        fail("Apollo company-distribution route source missing")


def verify_apollo_credit_quality_boundary() -> None:
    if not APOLLO_CREDIT_QUALITY.exists():
        fail(f"missing {APOLLO_CREDIT_QUALITY.relative_to(ROOT)}")
    with APOLLO_CREDIT_QUALITY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["line_id", "metric", "amount_musd", "period", "scope", "status", "source_artifact", "what_is_proven", "missing_upgrade"]
        if reader.fieldnames != expected_header:
            fail(f"Apollo credit-quality header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {"APO-CQ01": "33207", "APO-CQ02": "33078", "APO-CQ03": "1", "APO-CQ04": "1027", "APO-CQ05": "44", "APO-CQ06": "61"}
    by_id = {row["line_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"Apollo credit-quality lines changed: {sorted(by_id)}")
    for line_id, amount in expected.items():
        row = by_id[line_id]
        if row["amount_musd"] != amount:
            fail(f"Apollo credit-quality amount changed: {line_id}")
        for field in ("metric", "scope", "status", "what_is_proven", "missing_upgrade"):
            if not row[field].strip():
                fail(f"Apollo credit-quality row incomplete: {line_id}")
        if not resolve_source(APOLLO_CREDIT_QUALITY, row["source_artifact"]).exists():
            fail(f"Apollo credit-quality source missing: {row['source_artifact']}")


def verify_thesis_breaker_register() -> None:
    if not THESIS_BREAKERS.exists():
        fail(f"missing {THESIS_BREAKERS.relative_to(ROOT)}")
    with THESIS_BREAKERS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["breaker_id", "pilot", "thesis_or_claim", "observable_breaker", "measurement_or_trigger", "next_document", "source_artifact", "current_status"]
        if reader.fieldnames != expected_header:
            fail(f"thesis-breaker header mismatch: {reader.fieldnames}")
        rows = list(reader)
    required = {"TB-WPM-01", "TB-WPM-02", "TB-WPM-03", "TB-RET-01", "TB-RET-02", "TB-RET-03", "TB-APO-01", "TB-APO-02", "TB-APO-03"}
    by_id = {row["breaker_id"]: row for row in rows}
    if set(by_id) != required:
        fail(f"thesis-breaker rows changed: {sorted(by_id)}")
    for breaker_id, row in by_id.items():
        if row["current_status"] != "active-qualified":
            fail(f"thesis-breaker status overclaims: {breaker_id}")
        for field in ("pilot", "thesis_or_claim", "observable_breaker", "measurement_or_trigger", "next_document"):
            if not row[field].strip():
                fail(f"thesis-breaker row incomplete: {breaker_id}")
        if not resolve_source(THESIS_BREAKERS, row["source_artifact"]).exists():
            fail(f"thesis-breaker source missing: {row['source_artifact']}")


def verify_return_input_schemas() -> None:
    expected_header = [
        "schema_id", "input_family", "model_field", "current_status",
        "current_observation", "unit_or_denominator", "model_use",
        "exact_upgrade_document", "source_artifact", "proof_grade",
    ]
    cases = (
        (WHEATON_Q03_RETURN_INPUT_SCHEMA, "Q03-INPUT-", 13),
        (APOLLO_Q07_COMMON_OWNER_INPUT_SCHEMA, "Q07-INPUT-", 12),
        (RETAIL_OWNER_CASH_INPUT_SCHEMA, "RET-INPUT-", 16),
    )
    for path, prefix, expected_count in cases:
        if not path.exists():
            fail(f"missing return-input schema: {path.relative_to(ROOT)}")
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != expected_header:
                fail(f"return-input schema header mismatch: {path.name}")
            rows = list(reader)
        if len(rows) != expected_count or any(not row["schema_id"].startswith(prefix) for row in rows):
            fail(f"return-input schema row count or prefix changed: {path.name}")
        for row in rows:
            for field in expected_header:
                if not row[field].strip():
                    fail(f"return-input schema row incomplete: {path.name} {row['schema_id']} {field}")
            if not resolve_source(path, row["source_artifact"]).exists():
                fail(f"return-input schema source missing: {row['schema_id']}")
        if path == WHEATON_Q03_RETURN_INPUT_SCHEMA:
            q03 = {row["schema_id"]: row for row in rows}
            required_missing = {
                "Q03-INPUT-003",  # BHP-only recovered ounces
                "Q03-INPUT-005",  # quotation-period realized price
                "Q03-INPUT-006",  # invoice/settlement/cash entry
            }
            if any(q03[schema_id]["current_status"] != "missing" for schema_id in required_missing):
                fail("Q-03 decisive delivery, price, and receipt fields were over-promoted")
            required_partial = {
                "Q03-INPUT-008",  # funding allocation
                "Q03-INPUT-009",  # facility-specific financing
                "Q03-INPUT-011",  # Antamina tax allocation
                "Q03-INPUT-012",  # reserve-backed curve
                "Q03-INPUT-013",  # source-linked return
            }
            if any(q03[schema_id]["current_status"] != "partial" for schema_id in required_partial):
                fail("Q-03 partial financing, tax, reserve, or return fields changed status")
        if path == APOLLO_Q07_COMMON_OWNER_INPUT_SCHEMA:
            q07 = {row["schema_id"]: row for row in rows}
            if q07["Q07-INPUT-004"]["current_status"] != "searched-negative":
                fail("Q-07 AGM receipt boundary was over-promoted or reclassified")
            for schema_id in ("Q07-INPUT-005", "Q07-INPUT-012"):
                if q07[schema_id]["current_status"] != "missing" and q07[schema_id]["current_status"] != "not-assembled":
                    fail(f"Q-07 decisive waterfall field changed status: {schema_id}")
            for schema_id in ("Q07-INPUT-002", "Q07-INPUT-003", "Q07-INPUT-006", "Q07-INPUT-007", "Q07-INPUT-008", "Q07-INPUT-009", "Q07-INPUT-010"):
                if q07[schema_id]["current_status"] != "partial":
                    fail(f"Q-07 entity, access, claim, fee, or use field changed status: {schema_id}")
        if path == RETAIL_OWNER_CASH_INPUT_SCHEMA:
            retail = {row["schema_id"]: row for row in rows}
            required_missing = {
                "RET-INPUT-009",  # matched operating-lease cash
                "RET-INPUT-010",  # matched cash taxes
                "RET-INPUT-011",  # maintenance capex
                "RET-INPUT-013",  # allocated attached-service cost/cash
                "RET-INPUT-016",  # final normalized residual
            }
            if any(retail[schema_id]["current_status"] != "missing" for schema_id in required_missing):
                fail("CA-06 decisive lease, tax, maintenance, service, or residual fields were over-promoted")
            required_partial = {
                "RET-INPUT-006",  # supplier-finance settlement
                "RET-INPUT-007",  # temporary support recurrence
                "RET-INPUT-012",  # growth-capex allocation
                "RET-INPUT-014",  # debt and other senior claims
            }
            if any(retail[schema_id]["current_status"] != "partial" for schema_id in required_partial):
                fail("CA-06 partial supplier-finance, support, growth-capex, or senior-claim fields changed status")
        if not any(row["current_status"] == "missing" for row in rows):
            fail(f"return-input schema must preserve missing fields: {path.name}")
        if not any(row["current_status"] == "partial" for row in rows):
            fail(f"return-input schema must preserve partial fields: {path.name}")


def verify_reader_decision_layer() -> None:
    synthesis = PILOT_DIR / "combined-investment-research-current-synthesis.md"
    text = synthesis.read_text(encoding="utf-8")
    required_markers = (
        "## Decision layer: what the evidence supports today",
        "## Falsifier-first handoff",
        "`strongest named-asset proxy; return unproven`",
        "`cohort signal; no normalized ranking`",
        "`platform and wrapper map; common cash unproven`",
        "measurable filing tests",
    )
    for marker in required_markers:
        if marker not in text:
            fail(f"reader decision layer marker missing: {marker}")


def verify_completion_audit() -> None:
    if not COMPLETION_AUDIT.exists():
        fail(f"missing {COMPLETION_AUDIT.relative_to(ROOT)}")
    with COMPLETION_AUDIT.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["audit_id", "goal_requirement", "status", "authoritative_evidence", "source_artifact", "remaining_gap", "verification_method"]
        if reader.fieldnames != expected_header:
            fail(f"completion-audit header mismatch: {reader.fieldnames}")
        rows = list(reader)
    required = {f"CA-{index:02d}" for index in range(1, 14)}
    by_id = {row["audit_id"]: row for row in rows}
    if set(by_id) != required:
        fail(f"completion-audit rows changed: {sorted(by_id)}")
    expected_status = {
        "CA-01": "proven",
        "CA-02": "proven",
        "CA-03": "proven",
        "CA-04": "proven",
        "CA-05": "proven",
        "CA-06": "partial",
        "CA-07": "proven",
        "CA-08": "proven",
        "CA-09": "proven",
        "CA-10": "proven",
        "CA-11": "proven",
        "CA-12": "proven",
        "CA-13": "proven",
    }
    for audit_id, row in by_id.items():
        if row["status"] not in {"proven", "qualified", "partial", "unresolved"}:
            fail(f"completion-audit status invalid: {audit_id}")
        if row["status"] != expected_status[audit_id]:
            fail(f"completion-audit status changed unexpectedly: {audit_id}")
        for field in ("goal_requirement", "authoritative_evidence", "remaining_gap", "verification_method"):
            if not row[field].strip():
                fail(f"completion-audit row incomplete: {audit_id}")
        if not resolve_source(COMPLETION_AUDIT, row["source_artifact"]).exists():
            fail(f"completion-audit source missing: {row['source_artifact']}")
    if sum(row["status"] == "proven" for row in rows) != 12 or by_id["CA-06"]["status"] != "partial":
        fail("completion-audit promotion count changed: CA-06 must remain the single partial requirement")
    if "226 evidence gates" not in by_id["CA-10"]["authoritative_evidence"]:
        fail("completion-audit CA-10 lost the current evidence-gate total")
    if "Concord deal-level timely-interest servicing boundary" not in by_id["CA-10"]["authoritative_evidence"]:
        fail("completion-audit CA-10 lost the Concord servicing boundary")
    audit_memo = (PILOT_DIR / "combined-investment-research-completion-audit.md").read_text(encoding="utf-8")
    required_memo_markers = (
        "CA-06 owner-cash promotion matrix",
        "allocation-sensitivity-only",
        "minimum promotion bundle",
        "QoE and financial-shenanigans gate",
        "valuation and expectation promotion matrix",
        "12 of the 13",
    )
    for marker in required_memo_markers:
        if marker not in audit_memo:
            fail(f"completion-audit reader surface missing current control: {marker}")


def verify_cash_denominator_reconciliation() -> None:
    if not CAP_CASH_RECONCILIATION.exists():
        fail(f"missing cash-denominator reconciliation: {CAP_CASH_RECONCILIATION.relative_to(ROOT)}")
    with CAP_CASH_RECONCILIATION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "denominator_id", "audit_id", "pilot", "current_source_denominator",
            "scope_correctly_measured", "remaining_outside", "promotion_blocker",
            "status", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"cash-denominator reconciliation header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_pilots = {"Wheaton-Antamina", "TJX", "Target", "Walmart", "Apollo-Athene"}
    if len(rows) != 5 or {row["pilot"] for row in rows} != expected_pilots:
        fail("cash-denominator reconciliation rows changed unexpectedly")
    for row in rows:
        if row["audit_id"] != "CA-06" or row["status"] != "scope-reconciled-not-promoted":
            fail(f"cash-denominator reconciliation status changed: {row}")
        for field in ("current_source_denominator", "scope_correctly_measured", "remaining_outside", "promotion_blocker"):
            if not row[field].strip():
                fail(f"cash-denominator reconciliation row incomplete: {row['pilot']} {field}")
        if not resolve_source(CAP_CASH_RECONCILIATION, row["source_artifact"]).exists():
            fail(f"cash-denominator reconciliation source missing: {row['source_artifact']}")


def verify_owner_cash_promotion_matrix() -> None:
    if not OWNER_CASH_PROMOTION.exists():
        fail(f"missing owner-cash promotion matrix: {OWNER_CASH_PROMOTION.relative_to(ROOT)}")
    with OWNER_CASH_PROMOTION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "matrix_id", "pilot", "denominator", "period_alignment",
            "operating_cash_working_capital", "reinvestment_financing",
            "owner_claims_legal_entity", "service_contract_attribution",
            "promotion_decision", "next_promotion_test", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"owner-cash promotion header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 5 or {row["matrix_id"] for row in rows} != {f"OCP-{index:03d}" for index in range(1, 6)}:
        fail("owner-cash promotion rows changed unexpectedly")
    expected_decisions = {
        "OCP-001": "hold-stream-level-proxy",
        "OCP-002": "hold-reported-illustrative-screen",
        "OCP-003": "hold-reported-illustrative-screen",
        "OCP-004": "hold-reported-illustrative-screen",
        "OCP-005": "hold-segment-statutory-proxy",
    }
    for row in rows:
        if row["promotion_decision"] != expected_decisions[row["matrix_id"]]:
            fail(f"owner-cash promotion decision changed: {row['matrix_id']}")
        if "promote" in row["promotion_decision"]:
            fail(f"owner-cash matrix overpromotes a denominator: {row['matrix_id']}")
        for field in ("pilot", "denominator", "period_alignment", "operating_cash_working_capital", "reinvestment_financing", "owner_claims_legal_entity", "service_contract_attribution", "next_promotion_test"):
            if not row[field].strip():
                fail(f"owner-cash promotion row incomplete: {row['matrix_id']} {field}")
        if not resolve_source(OWNER_CASH_PROMOTION, row["source_artifact"]).exists():
            fail(f"owner-cash promotion source missing: {row['source_artifact']}")


def verify_method_registry() -> None:
    if not METHOD_REGISTRY.exists():
        fail(f"missing {METHOD_REGISTRY.relative_to(ROOT)}")
    with METHOD_REGISTRY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["layer", "contribution", "source_artifact", "current_status", "boundary", "first_party_method_references"]
        if reader.fieldnames != expected_header:
            fail(f"method registry header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_layers = {"Social research", "Inc. 5000", "IBIS Industries", "Annual reports and SEC/IR", "Damodaran valuation", "Lyn Alden macro/liquidity", "Investments article and hard-gate bridge", "Capital-flow and legal-entity proof", "Quality of earnings and financial shenanigans", "Reader and confidence layer", "Completion audit"}
    if {row["layer"] for row in rows} != expected_layers:
        fail("method registry layers changed unexpectedly")
    expected_status = {
        "Social research": "usable-directional-context",
        "Inc. 5000": "discovery-layer",
        "IBIS Industries": "industry-map-context",
        "Annual reports and SEC/IR": "primary-source-routed",
        "Damodaran valuation": "qualified-illustrative",
        "Lyn Alden macro/liquidity": "qualified-mechanism-layer",
        "Investments article and hard-gate bridge": "connected-hypothesis-and-triage-layer",
        "Capital-flow and legal-entity proof": "qualified-named-cash-pilots",
        "Quality of earnings and financial shenanigans": "connected-diagnostic-overlay",
        "Reader and confidence layer": "route-verified",
        "Completion audit": "checked-control",
    }
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"method registry row incomplete: {row.get('layer', '<unknown>')}")
        if row["current_status"] != expected_status[row["layer"]]:
            fail(f"method registry status changed unexpectedly: {row['layer']}")
        if not resolve_source(METHOD_REGISTRY, row["source_artifact"]).exists():
            fail(f"method registry source missing: {row['source_artifact']}")
    references = {row["layer"]: row["first_party_method_references"] for row in rows}
    if "pages.stern.nyu.edu/adamodar" not in references["Damodaran valuation"]:
        fail("Damodaran method registry references are missing")
    if "lynalden.com" not in references["Lyn Alden macro/liquidity"]:
        fail("Lyn Alden method registry references are missing")


def verify_investments_repository_bridge() -> None:
    if not INVESTMENTS_BRIDGE.exists():
        fail(f"missing Investments repository bridge: {INVESTMENTS_BRIDGE.relative_to(ROOT)}")
    bridge = INVESTMENTS_BRIDGE.read_text(encoding="utf-8")
    required_markers = (
        "article or macro stance",
        "hard gate: exact metric, period, denominator, and source",
        "owner-cash and liability normalization",
        "measurable filing-based thesis breaker",
        "Pilot 01 article bridge",
        "473` pattern-screen rows",
        "blocked_by_hard_gate`",
        "701` resolved metric rows",
        "do not mean all 75 article-derived",
    )
    for marker in required_markers:
        if marker not in bridge:
            fail(f"Investments bridge marker missing: {marker}")
    sibling = ROOT.parent / "investments"
    required_sources = (
        sibling / "analysis" / "combined-analysis-workflow.md",
        sibling / "analysis" / "hard_gate_data_acquisition_batch.csv",
        sibling / "analysis" / "hard_gate_process_verification.md",
        sibling / "first_principles_alignment.html",
    )
    for source in required_sources:
        if not source.exists():
            fail(f"Investments bridge source missing: {source}")
    analysis = sibling / "analysis"
    def read_rows(name: str) -> list[dict[str, str]]:
        path = analysis / name
        if not path.exists():
            fail(f"Investments hard-gate artifact missing: {path}")
        with path.open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    pattern_rows = read_rows("pattern_screen_results.csv")
    execution_rows = read_rows("pattern_hard_gate_execution.csv")
    filled_rows = read_rows("pattern_hard_gate_filled_execution.csv")
    resolved_rows = read_rows("hard_gate_resolved_metrics.csv")
    gap_rows = read_rows("hard_gate_remaining_metric_gaps.csv")
    acquisition_rows = read_rows("hard_gate_data_acquisition_batch.csv")
    if len(pattern_rows) != 473 or len(execution_rows) != 75 or len(filled_rows) != 75:
        fail("Investments hard-gate row counts changed unexpectedly")
    if len(resolved_rows) != 701 or gap_rows or acquisition_rows:
        fail("Investments hard-gate resolved/gap counts changed unexpectedly")
    decisions = {row.get("gate_decision") for row in execution_rows}
    if not decisions.issubset({"needs_data_before_gate", "blocked_by_hard_gate", "passes_hard_gate"}):
        fail(f"Investments hard-gate decisions changed: {decisions}")
    filled_decisions = {row.get("filled_gate_decision") for row in filled_rows}
    if filled_decisions != {"blocked_by_hard_gate", "passes_hard_gate"}:
        fail(f"Investments filled hard-gate decisions changed: {filled_decisions}")
    if sum(row["filled_gate_decision"] == "blocked_by_hard_gate" for row in filled_rows) != 40:
        fail("Investments blocked hard-gate count changed")
    if sum(row["filled_gate_decision"] == "passes_hard_gate" for row in filled_rows) != 35:
        fail("Investments passed hard-gate count changed")
    if any(row.get("filled_gate_decision") not in {"blocked_by_hard_gate", "passes_hard_gate"} for row in filled_rows):
        fail("Investments filled hard-gate output contains a non-decisive result")


def verify_investments_article_handoff() -> None:
    if not INVESTMENTS_ARTICLE_HANDOFF.exists():
        fail(f"missing Investments article handoff: {INVESTMENTS_ARTICLE_HANDOFF.relative_to(ROOT)}")
    handoff = INVESTMENTS_ARTICLE_HANDOFF.read_text(encoding="utf-8")
    for marker in (
        "2021-03-28",
        "Franco Nevada, FNV and Sandstorm Gold, SAND Deep Dive Analysis",
        "commodity_supply_squeeze",
        "liquidity_sensitive_growth",
        "fed_policy",
        "BHP Antamina contract",
        "article-to-filing-handoff-confirmed",
    ):
        if marker not in handoff:
            fail(f"Investments article handoff marker missing: {marker}")
    sibling = ROOT.parent / "investments" / "analysis"
    index_path = sibling / "article_index.csv"
    thesis_path = sibling / "article_thesis_records.csv"
    queue_path = sibling / "article_insight_investigation_queue.csv"
    for path in (index_path, thesis_path, queue_path):
        if not path.exists():
            fail(f"Investments article source missing: {path}")
    with index_path.open(newline="", encoding="utf-8") as handle:
        index_rows = list(csv.DictReader(handle))
    article = next((row for row in index_rows if row.get("date") == "2021-03-28" and "Franco Nevada" in row.get("title", "")), None)
    if article is None or "WPM" not in article.get("tickers", "").split(";"):
        fail("Investments article index does not preserve the WPM source row")
    with thesis_path.open(newline="", encoding="utf-8") as handle:
        thesis_rows = list(csv.DictReader(handle))
    matching_theses = [row for row in thesis_rows if row.get("date") == "2021-03-28" and "Franco Nevada" in row.get("title", "") and "WPM" in row.get("tickers", "").split(";")]
    if not {row.get("thesis") for row in matching_theses}.issuperset({"commodity_supply_squeeze", "liquidity_sensitive_growth"}):
        fail("Investments thesis records do not preserve both WPM handoff hypotheses")
    with queue_path.open(newline="", encoding="utf-8") as handle:
        queue_rows = list(csv.DictReader(handle))
    queued = next((row for row in queue_rows if row.get("date") == "2021-03-28" and "Franco Nevada" in row.get("title", "") and "WPM" in row.get("tickers", "").split(";")), None)
    if queued is None or "fed_policy" not in queued.get("failure_regimes", "") or "rates" not in queued.get("failure_regimes", ""):
        fail("Investments article queue does not preserve WPM failure regimes")


def verify_social_research_bridge() -> None:
    if not SOCIAL_THEME_MATRIX.exists():
        fail(f"missing social-research theme matrix: {SOCIAL_THEME_MATRIX}")
    matrix = SOCIAL_THEME_MATRIX.read_text(encoding="utf-8")
    required_markers = (
        "**social_themes:** 11",
        "**social_subthemes:** 36",
        "**annual_report_source_company_rows:** 75",
        "Affordability, Substitution, And Constrained Choice | 33 | 1553 | 1777 | $87.3B | 15 | directional",
        "This matrix triangulates business formation and operating evidence",
        "does not turn company counts, revenue, or annual-report examples into consumer adoption",
    )
    for marker in required_markers:
        if marker not in matrix:
            fail(f"social-research matrix marker missing: {marker}")
    atlas = PILOT_DIR / "combined-investment-research-force-to-company-atlas-2026-09-15.md"
    if not atlas.exists() or "33 social affordability/substitution signals" not in atlas.read_text(encoding="utf-8"):
        fail("force-to-company atlas is not connected to the affordability social signal count")
    atlas_text = atlas.read_text(encoding="utf-8")
    for marker in (
        "Regulated power-grid customer cash (next-cycle route)",
        "Insurance statutory named-asset wrapper (next-cycle route)",
        "Asset-backed rental collateral (next-cycle route)",
        "upstream prevalence and causal attribution remain unasserted",
        "do not call wrapper evidence an Athene receipt",
        "do not call facility capacity or fleet resale recovery a lifecycle return",
    ):
        if marker not in atlas_text:
            fail(f"force-to-company atlas expansion marker missing: {marker}")


def verify_ibis_industry_handoff() -> None:
    if not IBIS_CROSSWALK.exists() or not IBIS_HANDOFF.exists():
        fail("IBIS crosswalk or retail handoff is missing")
    crosswalk = IBIS_CROSSWALK.read_text(encoding="utf-8")
    for marker in (
        "# `ibis-industries` Crosswalk",
        "consumer-goods-value-portfolio",
        "the-hollow-middle",
        "the-margin-vise",
        "the-channel-shift",
        "Do not use `ibis-industries` to answer",
    ):
        if marker not in crosswalk:
            fail(f"IBIS crosswalk marker missing: {marker}")
    with IBIS_HANDOFF.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 3 or {row["ibis_force"] for row in rows} != {"the-hollow-middle", "the-margin-vise", "the-channel-shift"}:
        fail("IBIS retail handoff force coverage changed")
    for row in rows:
        if row["current_grade"] != "industry-handoff-confirmed" or not row["boundary"].strip():
            fail(f"IBIS retail handoff boundary changed: {row}")
        if not resolve_source(IBIS_HANDOFF, row["primary_filing_route"]).exists():
            fail(f"IBIS handoff filing route missing: {row['primary_filing_route']}")


def verify_inc5000_discovery_bridge() -> None:
    raw_dir = INC5000_ROOT / "2026Data"
    source_files = sorted(raw_dir.glob("inc (*.csv"))
    if len(source_files) != 5:
        fail(f"Inc. 5000 2026 source-file count changed: {len(source_files)}")
    all_rows: list[list[str]] = []
    for path in source_files:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.reader(handle)
            header = next(reader, [])
            rows = list(reader)
        if not rows:
            fail(f"Inc. 5000 source file is empty: {path}")
        all_rows.extend(rows)
    # The five downloaded files are not a clean one-row-per-company export:
    # they contain overlapping rank ranges and repeated company names.  Keep
    # both the capture size and the deduplicated identifiers explicit so a
    # later refresh cannot silently confuse source rows with companies.
    unique_ranks = {row[0].strip() for row in all_rows if row and row[0].strip()}
    unique_names = {row[1].strip() for row in all_rows if len(row) > 1 and row[1].strip()}
    if len(all_rows) != 5152 or len(unique_ranks) != 5000 or len(unique_names) != 4999:
        fail(
            "Inc. 5000 2026 raw-capture reconciliation changed: "
            f"rows={len(all_rows)}, unique_ranks={len(unique_ranks)}, "
            f"unique_names={len(unique_names)}"
        )
    grocery = next((row for row in all_rows if len(row) > 1 and row[1] == "Grocery TV"), None)
    if grocery is None:
        fail("Inc. 5000 source does not preserve the Grocery TV bridge row")
    expected = {0: "2,103", 3: "162%", 4: "$25M - $50M", 5: "20%", 6: "2016"}
    for index, value in expected.items():
        if len(grocery) <= index or grocery[index] != value:
            observed = grocery[index] if len(grocery) > index else None
            fail(f"Inc. 5000 Grocery TV field changed at column {index}: {observed!r}")
    bridge = PILOT_DIR / "combined-investment-research-inc5000-retail-attached-services-bridge-2026-09-15.md"
    if not bridge.exists() or "Inc. 5000 discovery-to-public-filing route confirmed" not in bridge.read_text(encoding="utf-8"):
        fail("Inc. 5000 retail attached-services bridge is missing its bounded conclusion")
    bridge_text = bridge.read_text(encoding="utf-8")
    for marker in ("5,152 raw rows", "5,000 distinct", "4,999 distinct company names"):
        if marker not in bridge_text:
            fail(f"Inc. 5000 raw-capture reconciliation marker missing: {marker}")


def verify_macro_liquidity_matrix() -> None:
    if not MACRO_LIQUIDITY_MATRIX.exists():
        fail(f"missing {MACRO_LIQUIDITY_MATRIX.relative_to(ROOT)}")
    text = MACRO_LIQUIDITY_MATRIX.read_text(encoding="utf-8")
    for marker in ("Retail cohort", "Wheaton–Antamina", "Apollo–Athene", "Next measurable test", "Interpretation boundary"):
        if marker not in text:
            fail(f"macro-liquidity matrix missing marker: {marker}")


def verify_next_evidence_queue() -> None:
    if not NEXT_EVIDENCE_QUEUE.exists():
        fail(f"missing {NEXT_EVIDENCE_QUEUE.relative_to(ROOT)}")
    with NEXT_EVIDENCE_QUEUE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = ["queue_id", "pilot", "missing_evidence", "next_document_or_source", "upgrade_test", "current_status", "result_class", "source_artifact"]
        if reader.fieldnames != expected_header:
            fail(f"next-evidence queue header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if {row["queue_id"] for row in rows} != {f"Q-{index:02d}" for index in range(1, 14)}:
        fail("next-evidence queue IDs changed unexpectedly")
    expected_result_classes = {
        "Q-01": "searched-negative",
        "Q-11": "searched-negative",
        **{f"Q-{index:02d}": "evidence-insufficient" for index in range(2, 11)},
        "Q-12": "evidence-insufficient",
        "Q-13": "evidence-insufficient",
    }
    for row in rows:
        if row["current_status"] not in {"open", "open-source-boundary", "partial-upgrade"}:
            fail(f"next-evidence queue status invalid: {row['queue_id']}")
        if row["result_class"] != expected_result_classes[row["queue_id"]]:
            fail(f"next-evidence queue result class changed: {row['queue_id']}")
        for field in expected_header:
            if not row[field].strip():
                fail(f"next-evidence queue row incomplete: {row['queue_id']}")
        if not resolve_source(NEXT_EVIDENCE_QUEUE, row["source_artifact"]).exists():
            fail(f"next-evidence queue source missing: {row['source_artifact']}")
    q01 = next(row for row in rows if row["queue_id"] == "Q-01")
    if "portfolio page" not in q01["next_document_or_source"]:
        fail("Q-01 queue perimeter lost the current Wheaton portfolio-page cross-check")
    if "metal-credit" not in q01["upgrade_test"]:
        fail("Q-01 upgrade test no longer names the metal-credit reconciliation")
    q08 = next(row for row in rows if row["queue_id"] == "Q-08")
    for marker in ("premium-gated Concord Series 2025-3 report", "timely-interest proxy", "trustee remittance"):
        if marker not in q08["next_document_or_source"] + q08["upgrade_test"]:
            fail(f"Q-08 queue lost Concord servicing boundary marker: {marker}")
    with FPL_HISTORICAL_RECOVERY_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        fpl_reader = csv.DictReader(handle)
        fpl_rows = list(fpl_reader)
    if len(fpl_rows) != 6 or {row["boundary_id"] for row in fpl_rows} != {f"FPL-HR-{index:03d}" for index in range(1, 7)}:
        fail("FPL historical recovery-boundary rows changed unexpectedly")
    for row in fpl_rows:
        if row["current_status"] == "" or not row["source_url"].startswith("https://www.floridapsc.com/"):
            fail(f"FPL historical recovery-boundary row incomplete: {row['boundary_id']}")
    fpl_memo = (PILOT_DIR / "capital-flow-fpl-sppcrc-historical-recovery-boundary-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("$998.817M", "$984.084M", "category-cash-unproven", "Inspection invoice or collection ledger", "$1.244B"):
        if marker not in fpl_memo:
            fail(f"FPL historical recovery-boundary marker missing: {marker}")
    with FPL_RATE_CLASS_FACTORS.open(newline="", encoding="utf-8") as handle:
        factor_reader = csv.DictReader(handle)
        factor_rows = list(factor_reader)
    if len(factor_rows) != 13 or {row["factor_id"] for row in factor_rows} != {f"FPL-F-{index:03d}" for index in range(1, 14)}:
        fail("FPL rate-class factor rows changed unexpectedly")
    for row in factor_rows:
        if row["current_status"] != "conditional-factor-visible" or not row["source_url"].startswith("https://www.floridapsc.com/"):
            fail(f"FPL rate-class factor row incomplete: {row['factor_id']}")
    factor_memo = (PILOT_DIR / "capital-flow-fpl-2026-sppcrc-rate-class-factor-boundary-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("rate-class-factor-visible", "$0.00995/kWh", "$1.80/kW", "not a billing determinant"):
        if marker not in factor_memo:
            fail(f"FPL rate-class factor marker missing: {marker}")
    with FPL_RATE_CLASS_DETERMINANTS.open(newline="", encoding="utf-8") as handle:
        determinant_reader = csv.DictReader(handle)
        determinant_rows = list(determinant_reader)
    if len(determinant_rows) != 14 or {row["determinant_id"] for row in determinant_rows} != {f"FPL-D-{index:03d}" for index in range(1, 15)}:
        fail("FPL rate-class determinant rows changed unexpectedly")
    for row in determinant_rows:
        if row["current_status"] != "public-projection-denominator-visible" or not row["source_url"].startswith("https://www.floridapsc.com/"):
            fail(f"FPL rate-class determinant row incomplete: {row['determinant_id']}")
        if not row["projected_sales_at_meter_kwh"].strip() or not row["total_sppcrc_cost_usd"].strip():
            fail(f"FPL rate-class determinant numeric boundary missing: {row['determinant_id']}")
    determinant_memo = (PILOT_DIR / "capital-flow-fpl-sppcrc-rate-class-determinant-boundary-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("public-projection-denominator-visible", "128,430,086,092 kWh", "not a collection ledger", "not-actual-collection"):
        if marker not in determinant_memo:
            fail(f"FPL rate-class determinant marker missing: {marker}")


def verify_duke_anderson_cost_sensitivity() -> None:
    if not DUKE_ANDERSON_COST_SENSITIVITY.exists():
        fail(f"missing Duke Anderson cost sensitivity: {DUKE_ANDERSON_COST_SENSITIVITY.relative_to(ROOT)}")
    with DUKE_ANDERSON_COST_SENSITIVITY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "row_id", "participant", "nominal_mw", "total_nominal_mw", "capacity_share_pct",
            "proposed_project_cost_usd", "mechanical_cost_share_usd", "status", "do_not_infer", "source_url",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Duke Anderson sensitivity header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["row_id"] for row in rows] != ["DCAS-001", "DCAS-002", "DCAS-003", "DCAS-004"]:
        fail("Duke Anderson sensitivity rows changed unexpectedly")
    expected_mw = {"DCAS-001": 1170, "DCAS-002": 100, "DCAS-003": 95, "DCAS-004": 1365}
    total_cost = 3_218_000_000
    for row in rows:
        if int(row["nominal_mw"]) != expected_mw[row["row_id"]] or int(row["total_nominal_mw"]) != 1365:
            fail(f"Duke Anderson capacity denominator changed: {row['row_id']}")
        expected_share = int(row["nominal_mw"]) / 1365 * 100
        expected_cost = total_cost * int(row["nominal_mw"]) / 1365
        if not math.isclose(float(row["capacity_share_pct"]), expected_share, abs_tol=0.011):
            fail(f"Duke Anderson capacity-share arithmetic failed: {row['row_id']}")
        if not math.isclose(float(row["mechanical_cost_share_usd"]), expected_cost, abs_tol=1.0):
            fail(f"Duke Anderson cost-allocation arithmetic failed: {row['row_id']}")
        if row["source_url"] != "https://dms.psc.sc.gov/Attachments/Matter/e5ddc5b1-26d3-429d-b4ea-4a9a3fe5ab35":
            fail(f"Duke Anderson source route changed: {row['row_id']}")
        if row["row_id"] != "DCAS-004" and row["status"] != "mechanical-allocation-sensitivity":
            fail(f"Duke Anderson participant row was over-promoted: {row['row_id']}")
        if not row["do_not_infer"].strip():
            fail(f"Duke Anderson sensitivity boundary missing: {row['row_id']}")
    if rows[-1]["status"] != "mechanical-reconciliation" or float(rows[-1]["mechanical_cost_share_usd"]) != total_cost:
        fail("Duke Anderson total reconciliation changed")


def verify_fpl_billing_receipt_chase() -> None:
    if not FPL_BILLING_RECEIPT_CHASE.exists():
        fail(f"missing FPL billing/receipt chase: {FPL_BILLING_RECEIPT_CHASE.relative_to(ROOT)}")
    with FPL_BILLING_RECEIPT_CHASE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "chase_id", "proof_gate", "source_document", "source_route", "period",
            "current_evidence", "value_or_metric", "current_status", "what_it_proves",
            "what_it_does_not_prove", "next_required_source", "upgrade_test",
        ]
        if reader.fieldnames != expected_header:
            fail(f"FPL billing/receipt chase header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["chase_id"] for row in rows] != [f"CFFPLBDCR-{index:03d}" for index in range(1, 10)]:
        fail("FPL billing/receipt chase rows changed unexpectedly")
    by_id = {row["chase_id"]: row for row in rows}
    expected_status = {
        "CFFPLBDCR-001": "aggregate-cash-proxy-visible",
        "CFFPLBDCR-002": "monthly-aggregate-visible",
        "CFFPLBDCR-003": "factor-authority-visible",
        "CFFPLBDCR-004": "allocation-mechanics-visible",
        "CFFPLBDCR-005": "category-recovery-visible",
        "CFFPLBDCR-006": "forward-factor-use-visible",
        "CFFPLBDCR-007": "billing-determinant-hold",
        "CFFPLBDCR-008": "category-receipt-hold",
        "CFFPLBDCR-009": "recovery-mechanics-visible",
    }
    for chase_id, status in expected_status.items():
        if by_id[chase_id]["current_status"] != status:
            fail(f"FPL billing/receipt chase status changed: {chase_id}")
    if by_id["CFFPLBDCR-001"]["value_or_metric"] != "804.620369M USD":
        fail("FPL aggregate clause-revenue denominator changed")
    if "15.942971M USD" not in by_id["CFFPLBDCR-005"]["value_or_metric"] or "38.320627M USD" not in by_id["CFFPLBDCR-005"]["value_or_metric"]:
        fail("FPL Distribution Inspection category-recovery values changed")
    if by_id["CFFPLBDCR-009"]["value_or_metric"] != "859.244393M USD total jurisdictional 2026 revenue requirements":
        fail("FPL recovery-return denominator changed")
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"FPL billing/receipt chase row incomplete: {row['chase_id']}")
    for chase_id in ("CFFPLBDCR-007", "CFFPLBDCR-008"):
        row = by_id[chase_id]
        if "not found" not in row["value_or_metric"].lower() or "hold" not in row["current_status"]:
            fail(f"FPL searched-negative receipt boundary changed: {chase_id}")
        if "pass only if" not in row["upgrade_test"].lower():
            fail(f"FPL receipt upgrade test missing: {chase_id}")


def verify_fpl_distribution_inspection_refresh() -> None:
    if not FPL_DISTRIBUTION_INSPECTION_REFRESH.exists():
        fail(f"missing FPL Distribution Inspection refresh: {FPL_DISTRIBUTION_INSPECTION_REFRESH.relative_to(ROOT)}")
    memo = FPL_DISTRIBUTION_INSPECTION_REFRESH.read_text(encoding="utf-8")
    for marker in (
        "02711-2025.pdf",
        "13931-2025/13931-2025.pdf",
        "02559-2026/02559-2026.pdf",
        "180,000",
        "$92.1M",
        "$94.1M",
        "$917.1M",
        "category-specific cash",
        "source-of-funds",
        "evidence-insufficient",
        "final 2026 SPPCRC true-up",
        "2025 final-true-up petition",
        "project-detail exhibits",
        "searched-negative for those specific public packet",
    ):
        if marker not in memo:
            fail(f"FPL Distribution Inspection refresh marker missing: {marker}")
    lower = memo.lower()
    for boundary in ("not customer cash", "not customer cash or shareholder return", "does not justify"):
        if boundary not in lower:
            fail(f"FPL Distribution Inspection QoE boundary missing: {boundary}")


def verify_duke_anderson_approval_boundary() -> None:
    if not DUKE_ANDERSON_APPROVAL_BOUNDARY.exists():
        fail(f"missing Duke Anderson approval boundary: {DUKE_ANDERSON_APPROVAL_BOUNDARY.relative_to(ROOT)}")
    with DUKE_ANDERSON_APPROVAL_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "row_id", "company", "period", "source_type", "metric", "reported_value",
            "status_bucket", "qoe_control", "proves", "does_not_prove", "source_url",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Duke Anderson approval header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 18 or [row["row_id"] for row in rows] != [f"DAG-{index:03d}" for index in range(1, 19)]:
        fail("Duke Anderson approval-boundary rows changed unexpectedly")
    by_id = {row["row_id"]: row for row in rows}
    expected_markers = {
        "DAG-002": ("1365 MW", "project-scale"),
        "DAG-003": ("95 MW", "shared-ownership"),
        "DAG-004": ("100 MW", "shared-ownership"),
        "DAG-009": ("1365 MW total; DEC 1170 MW; NCEMC 100 MW; Central 95 MW", "shared-ownership"),
        "DAG-015": ("3.218B USD", "project-cost-estimate"),
        "DAG-018": ("approved subject to required federal, state, and local permits, consultations, and certifications", "regulator-approved-conditioned"),
    }
    for row_id, (reported_value, status) in expected_markers.items():
        if by_id[row_id]["reported_value"] != reported_value or by_id[row_id]["status_bucket"] != status:
            fail(f"Duke Anderson approval-boundary observation changed: {row_id}")
    for row in rows:
        if not row["source_url"].startswith(("https://dms.psc.sc.gov/", "https://news.duke-energy.com/")):
            fail(f"Duke Anderson approval source route changed: {row['row_id']}")
        if not row["qoe_control"].strip() or not row["does_not_prove"].strip():
            fail(f"Duke Anderson approval QoE boundary missing: {row['row_id']}")
    combined_boundaries = " ".join((row["qoe_control"] + " " + row["does_not_prove"]).lower() for row in rows)
    for marker in ("cash", "rate base", "return", "capex"):
        if marker not in combined_boundaries:
            fail(f"Duke Anderson approval boundary lost marker: {marker}")


def verify_uri_borrowing_base_chase() -> None:
    if not URI_BORROWING_BASE_CHASE.exists():
        fail(f"missing URI borrowing-base chase: {URI_BORROWING_BASE_CHASE.relative_to(ROOT)}")
    with URI_BORROWING_BASE_CHASE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "chase_id", "proof_gate", "source_document", "source_route", "period",
            "current_evidence", "value_or_metric", "current_status", "what_it_proves",
            "what_it_does_not_prove", "next_required_source", "upgrade_test",
        ]
        if reader.fieldnames != expected_header:
            fail(f"URI borrowing-base chase header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["chase_id"] for row in rows] != [f"CFURIBBCA-{index:03d}" for index in range(1, 14)]:
        fail("URI borrowing-base chase rows changed unexpectedly")
    by_id = {row["chase_id"]: row for row in rows}
    expected_status = {
        "CFURIBBCA-001": "availability-disclosure-visible",
        "CFURIBBCA-002": "certificate-existence-visible",
        "CFURIBBCA-003": "threshold-visible",
        "CFURIBBCA-004": "field-map-visible",
        "CFURIBBCA-005": "public-proxy-visible",
        "CFURIBBCA-006": "draw-intensity-visible",
        "CFURIBBCA-007": "receivables-collateral-visible",
        "CFURIBBCA-008": "equipment-base-proxy-visible",
        "CFURIBBCA-009": "covenant-threshold-visible",
        "CFURIBBCA-010": "certificate-hold",
        "CFURIBBCA-011": "facility-availability-visible",
        "CFURIBBCA-012": "facility-availability-visible",
        "CFURIBBCA-013": "availability-reconciliation-visible",
    }
    for chase_id, status in expected_status.items():
        if by_id[chase_id]["current_status"] != status:
            fail(f"URI borrowing-base status changed: {chase_id}")
    expected_metrics = {
        "CFURIBBCA-001": "2.428B USD disclosed availability",
        "CFURIBBCA-003": "1.000B USD minimum",
        "CFURIBBCA-005": "2.887B USD implied combined facility availability",
        "CFURIBBCA-007": "125.8 percent collateral-pool coverage",
        "CFURIBBCA-011": "2.802B USD ABL capacity",
        "CFURIBBCA-012": "85M USD AR capacity",
        "CFURIBBCA-013": "2.887B USD reconciled availability",
    }
    for chase_id, metric in expected_metrics.items():
        if by_id[chase_id]["value_or_metric"] != metric:
            fail(f"URI borrowing-base metric changed: {chase_id}")
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"URI borrowing-base row incomplete: {row['chase_id']}")
    if "not" not in by_id["CFURIBBCA-010"]["value_or_metric"].lower() and "not found" not in by_id["CFURIBBCA-010"]["current_evidence"].lower():
        fail("URI populated-certificate hold was lost")
    boundary_text = " ".join(row["what_it_does_not_prove"].lower() for row in rows)
    for marker in ("certificate", "nolv", "reserves", "source-of-funds"):
        if marker not in boundary_text:
            fail(f"URI borrowing-base boundary lost marker: {marker}")


    with URI_REPORTING_REGIME_BOUNDARY.open(newline="", encoding="utf-8") as handle:
        uri_reader = csv.DictReader(handle)
        uri_rows = list(uri_reader)
    if len(uri_rows) != 8 or {row["boundary_id"] for row in uri_rows} != {f"URI-RR-{index:03d}" for index in range(1, 9)}:
        fail("URI reporting-regime boundary rows changed unexpectedly")
    for row in uri_rows:
        if not row["source_url"].startswith("https://www.sec.gov/") or not row["current_status"].strip():
            fail(f"URI reporting-regime row incomplete: {row['boundary_id']}")
    uri_memo = (PILOT_DIR / "capital-flow-uri-abl-borrowing-base-reporting-regime-boundary-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("reporting-regime-and-thresholds-visible", "quarterly Borrowing Base Certificates", "$1.000B", "populated certificate"):
        if marker not in uri_memo:
            fail(f"URI reporting-regime marker missing: {marker}")


def verify_uri_abl_proxy_bridge() -> None:
    if not URI_ABL_PROXY_BRIDGE.exists():
        fail(f"missing URI ABL proxy bridge: {URI_ABL_PROXY_BRIDGE.relative_to(ROOT)}")
    with URI_ABL_PROXY_BRIDGE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "row_id", "period", "company", "ticker", "theme", "subtheme", "metric",
            "value", "unit", "source_file", "source_detail", "calculation_or_source",
            "evidence_status", "what_it_says", "what_it_does_not_say", "next_source",
        ]
        if reader.fieldnames != expected_header:
            fail(f"URI ABL proxy header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["row_id"] for row in rows] != [f"URIABLProxy-{index:03d}" for index in range(1, 26)]:
        fail("URI ABL proxy rows changed unexpectedly")
    by_id = {row["row_id"]: row for row in rows}
    numeric = {row_id: float(by_id[row_id]["value"]) for row_id in by_id if by_id[row_id]["unit"] != "status"}
    checks = {
        "URIABLProxy-003": numeric["URIABLProxy-002"] - numeric["URIABLProxy-001"],
        "URIABLProxy-006": numeric["URIABLProxy-004"] - numeric["URIABLProxy-005"],
        "URIABLProxy-010": numeric["URIABLProxy-008"] - numeric["URIABLProxy-009"],
        "URIABLProxy-013": numeric["URIABLProxy-011"] - numeric["URIABLProxy-009"],
        "URIABLProxy-014": numeric["URIABLProxy-006"] + numeric["URIABLProxy-010"],
        "URIABLProxy-015": numeric["URIABLProxy-014"] - numeric["URIABLProxy-003"],
    }
    for row_id, expected in checks.items():
        if abs(numeric[row_id] - expected) > 0.2:
            fail(f"URI ABL proxy arithmetic changed: {row_id}")
    ratio_checks = {
        "URIABLProxy-007": numeric["URIABLProxy-005"] / numeric["URIABLProxy-004"] * 100,
        "URIABLProxy-012": numeric["URIABLProxy-011"] / numeric["URIABLProxy-009"] * 100,
        "URIABLProxy-016": numeric["URIABLProxy-003"] / numeric["URIABLProxy-002"] * 100,
        "URIABLProxy-017": numeric["URIABLProxy-001"] / numeric["URIABLProxy-002"] * 100,
        "URIABLProxy-021": numeric["URIABLProxy-020"] / numeric["URIABLProxy-004"] * 100,
        "URIABLProxy-022": 23800 / numeric["URIABLProxy-004"] * 100,
        "URIABLProxy-023": 2931 / numeric["URIABLProxy-003"] * 100,
        "URIABLProxy-024": 3305 / 2931 * 100,
    }
    for row_id, expected in ratio_checks.items():
        if abs(numeric[row_id] - expected) > 0.2:
            fail(f"URI ABL proxy ratio changed: {row_id}")
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"URI ABL proxy row incomplete: {row['row_id']}")
    boundary_text = " ".join(row["what_it_does_not_say"].lower() for row in rows)
    for marker in ("borrowing-base certificate", "eligible", "nolv", "source of funds"):
        if marker not in boundary_text:
            fail(f"URI ABL proxy boundary lost marker: {marker}")


def verify_wheaton_financing_cash_flow() -> None:
    if not WHEATON_FINANCING_CASH_FLOW.exists():
        fail(f"missing Wheaton financing cash-flow ledger: {WHEATON_FINANCING_CASH_FLOW.relative_to(ROOT)}")
    with WHEATON_FINANCING_CASH_FLOW.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "bridge_id", "queue_id", "evidence_gate", "evidence_source", "current_status",
            "period", "evidence_now", "value_or_metric", "proof_result", "money_movement_answer",
            "missing_proof", "next_required_source", "safe_claim",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Wheaton financing header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["bridge_id"] for row in rows] != [f"WPMFCFU-{index:03d}" for index in range(1, 10)]:
        fail("Wheaton financing rows changed unexpectedly")
    by_id = {row["bridge_id"]: row for row in rows}
    if by_id["WPMFCFU-001"]["value_or_metric"] != "2700000 USD thousands":
        fail("Wheaton debt draw changed")
    if by_id["WPMFCFU-002"]["value_or_metric"] != "728000 USD thousands":
        fail("Wheaton debt repayment changed")
    if by_id["WPMFCFU-003"]["value_or_metric"] != "2700000 - 728000 = 1972000 USD thousands":
        fail("Wheaton net debt reconciliation changed")
    if by_id["WPMFCFU-004"]["value_or_metric"] != "29886 USD thousands":
        fail("Wheaton interest-paid observation changed")
    if by_id["WPMFCFU-008"]["proof_result"] != "passes-contractual-use-link" or "partially finance" not in by_id["WPMFCFU-008"]["evidence_now"]:
        fail("Wheaton contractual use-of-proceeds link changed")
    if by_id["WPMFCFU-009"]["proof_result"] != "passes-announced-envelope-reconciliation" or by_id["WPMFCFU-009"]["value_or_metric"] != "1.500B + approximately 0.900B = approximately 2.400B USD planned debt funding":
        fail("Wheaton announced debt-funding envelope changed")
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"Wheaton financing row incomplete: {row['bridge_id']}")
    combined = " ".join((row["missing_proof"] + " " + row["safe_claim"]).lower() for row in rows)
    for marker in ("allocation", "waterfall", "antamina", "pmpa"):
        if marker not in combined:
            fail(f"Wheaton financing boundary lost marker: {marker}")


def verify_expansion_lane_qoe_overlay() -> None:
    if not EXPANSION_LANE_QOE_OVERLAY.exists():
        fail(f"missing expansion-lane QoE overlay: {EXPANSION_LANE_QOE_OVERLAY.relative_to(ROOT)}")
    with EXPANSION_LANE_QOE_OVERLAY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "qoe_id", "lane", "diagnostic_family", "question", "current_signal",
            "evidence_status", "risk_flag", "next_required_source", "do_not_infer",
        ]
        if reader.fieldnames != expected_header:
            fail(f"expansion-lane QoE header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if [row["qoe_id"] for row in rows] != [f"ELQOE-{index:03d}" for index in range(1, 13)]:
        fail("expansion-lane QoE rows changed unexpectedly")
    expected_status = {
        "ELQOE-003": "missing", "ELQOE-010": "missing",
        **{f"ELQOE-{index:03d}": "partial" for index in (1, 2, 4, 5, 6, 7, 8, 9, 11, 12)},
    }
    for row in rows:
        if row["evidence_status"] != expected_status[row["qoe_id"]]:
            fail(f"expansion-lane QoE status changed: {row['qoe_id']}")
        if not all(row[field].strip() for field in ("diagnostic_family", "question", "current_signal", "risk_flag", "next_required_source", "do_not_infer")):
            fail(f"expansion-lane QoE row incomplete: {row['qoe_id']}")
        if "do not " not in row["do_not_infer"].lower():
            fail(f"expansion-lane QoE promotion boundary missing: {row['qoe_id']}")
    lanes = {row["lane"] for row in rows}
    if lanes != {"power_grid_customer_cash", "insurance_statutory_named_asset", "asset_backed_collateral_and_borrowing_base"}:
        fail(f"expansion-lane QoE lane coverage changed: {sorted(lanes)}")
    signals = " ".join(row["do_not_infer"].lower() for row in rows)
    for marker in ("cash", "collateral", "liquidity", "return"):
        if marker not in signals:
            fail(f"expansion-lane QoE boundary lost marker: {marker}")
    fpl_signals = " ".join(row["current_signal"] for row in rows if row["lane"] == "power_grid_customer_cash")
    for marker in ("180,000", "$92.1M", "$94.1M", "$917.1M"):
        if marker not in fpl_signals:
            fail(f"expansion-lane FPL refresh signal missing: {marker}")


def verify_apollo_q2_parent_receipt_script() -> None:
    script = ROOT / "scripts" / "check-apollo-q2-parent-receipt-boundary.py"
    if not script.exists():
        fail(f"missing Apollo Q2 parent-receipt checker: {script.relative_to(ROOT)}")
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail(f"Apollo Q2 parent-receipt checker failed: {result.stderr.strip() or result.stdout.strip()}")
    expected = "29 dividend-related facts, 0 upstream-receipt/intercompany/affiliate facts"
    if expected not in result.stdout:
        fail(f"Apollo Q2 parent-receipt checker output changed: {result.stdout.strip()}")


def verify_macro_liquidity_stress_screen() -> None:
    path = PILOT_DIR / "data" / "combined-investment-research-macro-liquidity-stress-screen.csv"
    expected_header = [
        "pilot", "stress_case", "source_anchored_start", "shock_or_transmission",
        "output_metric", "current_status", "next_evidence",
    ]
    if not path.exists():
        fail(f"missing macro/liquidity stress screen: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"macro/liquidity stress screen header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 8:
        fail(f"macro/liquidity stress screen must contain 8 rows, found {len(rows)}")
    if {row["pilot"] for row in rows} != {"Retail cohort", "Wheaton-Antamina", "Apollo-Athene"}:
        fail("macro/liquidity stress screen pilot coverage changed unexpectedly")
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"macro/liquidity stress screen row incomplete: {row}")
    statuses = {row["current_status"] for row in rows}
    if statuses != {"quantified-boundary", "illustrative-screen", "denominator-held", "source-boundary"}:
        fail(f"macro/liquidity stress screen statuses changed unexpectedly: {statuses}")
        if not resolve_source(NEXT_EVIDENCE_QUEUE, row["source_artifact"]).exists():
            fail(f"next-evidence queue source missing: {row['source_artifact']}")


def verify_apollo_q2_parent_flow_artifact() -> None:
    artifact = LEDGER_DIR / "capital-flow-apollo-athene-q2-parent-flow-upgrade-2026-09-15.csv"
    if not artifact.exists():
        fail(f"missing {artifact.relative_to(ROOT)}")
    with artifact.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "gate_id", "entity", "period", "source_line",
            "contributions_from_parent_q2_usd_m", "distributions_to_parent_q2_usd_m",
            "contributions_from_parent_h1_usd_m", "distributions_to_parent_h1_usd_m",
            "common_dividends_q2_usd_m", "common_dividends_h1_usd_m",
            "current_status", "what_is_proven", "missing_upgrade",
        ]
        if reader.fieldnames != expected_header:
            fail(f"Apollo Q2 parent-flow artifact header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 1:
        fail("Apollo Q2 parent-flow artifact must contain one row")
    row = rows[0]
    expected = {
        "gate_id": "APO-088",
        "contributions_from_parent_q2_usd_m": "58",
        "distributions_to_parent_q2_usd_m": "32",
        "contributions_from_parent_h1_usd_m": "241",
        "distributions_to_parent_h1_usd_m": "110",
        "common_dividends_q2_usd_m": "187",
        "common_dividends_h1_usd_m": "375",
    }
    for field, value in expected.items():
        if row[field] != value:
            fail(f"Apollo Q2 parent-flow artifact changed unexpectedly: {field}")
    if row["current_status"] != "athene-to-parent-flow-observed":
        fail("Apollo Q2 parent-flow artifact overclaims its status")
    if int(row["contributions_from_parent_q2_usd_m"]) - int(row["distributions_to_parent_q2_usd_m"]) != 26:
        fail("Apollo Q2 parent-flow net direction arithmetic failed")
    if int(row["contributions_from_parent_h1_usd_m"]) - int(row["distributions_to_parent_h1_usd_m"]) != 131:
        fail("Apollo H1 parent-flow net direction arithmetic failed")
    if row["common_dividends_q2_usd_m"] == row["distributions_to_parent_q2_usd_m"] or row["common_dividends_h1_usd_m"] == row["distributions_to_parent_h1_usd_m"]:
        fail("Apollo parent-flow and common-dividend categories were conflated")
    for field in ("what_is_proven", "missing_upgrade"):
        if not row[field].strip():
            fail(f"Apollo Q2 parent-flow artifact has empty {field}")


def verify_theme_status_map() -> None:
    artifact = LEDGER_DIR / "combined-investment-research-theme-status-map-2026-09-16.csv"
    if not artifact.exists():
        fail(f"missing {artifact.relative_to(ROOT)}")
    with artifact.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "theme", "representative_writeup", "connected_route",
            "current_grade", "decisive_open_question", "mechanism",
            "current_supported", "promotion_gate",
        ]
        if reader.fieldnames != expected_header:
            fail(f"theme-status map header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "Affordability and substitution": (
            "analysis/company-first-principles/annual-report-theme-value-retail-pass-1.md",
            "analysis/company-first-principles/combined-investment-research-pilot-02-affordability-value.md",
            "qualified",
        ),
        "Scarce physical assets and contractual control": (
            "analysis/company-first-principles/annual-report-theme-basic-materials-input-scarcity-pass-1.md",
            "analysis/company-first-principles/combined-investment-research-pilot-01-wheaton-antamina.md",
            "qualified",
        ),
        "Institutional capital and financial intermediation": (
            "analysis/company-first-principles/annual-report-theme-capital-platforms-pass-1.md",
            "analysis/company-first-principles/combined-investment-research-pilot-03-apollo-athene.md",
            "qualified",
        ),
        "Valuation and reinvestment": (
            "analysis/company-first-principles/combined-investment-research-method-registry.md",
            "analysis/company-first-principles/combined-investment-research-price-implied-expectation-2026-09-15.md",
            "illustrative-qualified",
        ),
        "Macro and liquidity transmission": (
            "analysis/company-first-principles/combined-investment-research-macro-liquidity-transmission-matrix.md",
            "analysis/company-first-principles/combined-investment-research-macro-historical-regime-validation-2026-09-15.md",
            "qualified",
        ),
    }
    if len(rows) != len(expected) or {row["theme"] for row in rows} != set(expected):
        fail("theme-status map rows changed unexpectedly")
    for row in rows:
        representative, route, grade = expected[row["theme"]]
        if (row["representative_writeup"], row["connected_route"], row["current_grade"]) != (representative, route, grade):
            fail(f"theme-status map routing or grade changed: {row['theme']}")
        for field in (
            "representative_writeup", "connected_route", "current_grade",
            "decisive_open_question", "mechanism", "current_supported",
            "promotion_gate",
        ):
            if not row[field].strip():
                fail(f"theme-status map row incomplete: {row['theme']} / {field}")
        for field in ("representative_writeup", "connected_route"):
            if not (ROOT / row[field]).exists():
                fail(f"theme-status map source missing: {row[field]}")


def verify_causal_test_protocol() -> None:
    if not CAUSAL_TEST_PROTOCOL.exists():
        fail(f"missing causal-test protocol: {CAUSAL_TEST_PROTOCOL.relative_to(ROOT)}")
    with CAUSAL_TEST_PROTOCOL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "test_id", "pilot", "mechanism", "dependent_observables",
            "principal_confound_controls", "promotion_requirement",
            "filing_based_breaker", "current_status", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"causal-test protocol header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {"CAUSAL-01", "CAUSAL-02", "CAUSAL-03"}
    by_id = {row["test_id"]: row for row in rows}
    if set(by_id) != expected_ids:
        fail(f"causal-test protocol rows changed: {sorted(by_id)}")
    for test_id, row in by_id.items():
        if row["current_status"] != "protocol-defined-evidence-insufficient":
            fail(f"causal-test protocol status changed: {test_id}")
        for field in ("pilot", "mechanism", "dependent_observables", "principal_confound_controls", "promotion_requirement", "filing_based_breaker", "source_artifact"):
            if not row[field].strip():
                fail(f"causal-test protocol row incomplete: {test_id}")
        if not resolve_source(CAUSAL_TEST_PROTOCOL, row["source_artifact"]).exists():
            fail(f"causal-test protocol source missing: {row['source_artifact']}")


def verify_retail_panel_diagnostic() -> None:
    if not RETAIL_PANEL_DIAGNOSTIC.exists():
        fail(f"missing retail panel diagnostic: {RETAIL_PANEL_DIAGNOSTIC.relative_to(ROOT)}")
    with RETAIL_PANEL_DIAGNOSTIC.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "diagnostic_id", "split", "observations", "mean_cash_after_property_musd",
            "median_cash_after_property_musd", "comparison_musd", "result_class",
            "source_artifact", "what_is_proven", "what_is_not_proven",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail panel diagnostic header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "Q10-RETAIL-DIAG-001": (11, 7813.7, 4917.0, 631.3),
        "Q10-RETAIL-DIAG-002": (7, 7182.4, 3994.0, 0.0),
        "Q10-RETAIL-DIAG-003": (12, 7401.6, 4405.5, -499.9),
        "Q10-RETAIL-DIAG-004": (6, 7901.5, 6396.5, 0.0),
    }
    by_id = {row["diagnostic_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"retail panel diagnostic rows changed: {sorted(by_id)}")
    for diagnostic_id, (observations, mean_value, median_value, comparison) in expected.items():
        row = by_id[diagnostic_id]
        if row["result_class"] != "descriptive-mechanism-screen":
            fail(f"retail panel diagnostic class changed: {diagnostic_id}")
        if int(row["observations"]) != observations:
            fail(f"retail panel diagnostic observations changed: {diagnostic_id}")
        for field, value in (("mean_cash_after_property_musd", mean_value), ("median_cash_after_property_musd", median_value), ("comparison_musd", comparison)):
            if not math.isclose(float(row[field]), value, rel_tol=0, abs_tol=0.1):
                fail(f"retail panel diagnostic value changed: {diagnostic_id} / {field}")
        if not resolve_source(RETAIL_PANEL_DIAGNOSTIC, row["source_artifact"]).exists():
            fail(f"retail panel diagnostic source missing: {row['source_artifact']}")
        for field in ("split", "what_is_proven", "what_is_not_proven"):
            if not row[field].strip():
                fail(f"retail panel diagnostic row incomplete: {diagnostic_id} / {field}")


def verify_retail_within_company_diagnostic() -> None:
    if not RETAIL_WITHIN_DIAGNOSTIC.exists():
        fail(f"missing within-company retail diagnostic: {RETAIL_WITHIN_DIAGNOSTIC.relative_to(ROOT)}")
    with RETAIL_WITHIN_DIAGNOSTIC.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "transition_id", "company", "prior_period", "current_period",
            "real_wage_delta_pct", "cash_after_property_delta_musd", "direction",
            "result_class", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"within-company retail diagnostic header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 15:
        fail(f"within-company retail diagnostic row count changed: {len(rows)}")
    expected_counts = {"same": 6, "opposite": 6, "no-change": 3}
    counts = {direction: sum(row["direction"] == direction for row in rows) for direction in expected_counts}
    if counts != expected_counts:
        fail(f"within-company retail diagnostic direction counts changed: {counts}")
    for row in rows:
        if row["result_class"] != "descriptive-mechanism-screen":
            fail(f"within-company retail diagnostic class changed: {row['transition_id']}")
        if not resolve_source(RETAIL_WITHIN_DIAGNOSTIC, row["source_artifact"]).exists():
            fail(f"within-company retail diagnostic source missing: {row['source_artifact']}")
        for field in ("company", "prior_period", "current_period", "direction"):
            if not row[field].strip():
                fail(f"within-company retail diagnostic row incomplete: {row['transition_id']} / {field}")


def verify_retail_lagged_diagnostic() -> None:
    if not RETAIL_LAGGED_DIAGNOSTIC.exists():
        fail(f"missing lagged retail diagnostic: {RETAIL_LAGGED_DIAGNOSTIC.relative_to(ROOT)}")
    with RETAIL_LAGGED_DIAGNOSTIC.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "diagnostic_id", "prior_real_wage_condition", "usable_transitions",
            "same_direction", "opposite_direction", "result_class", "source_artifact",
            "what_is_proven", "what_is_not_proven",
        ]
        if reader.fieldnames != expected_header:
            fail(f"lagged retail diagnostic header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "Q10-RETAIL-LAG-001": ("positive", 8, 4, 4),
        "Q10-RETAIL-LAG-002": ("negative", 7, 3, 4),
        "Q10-RETAIL-LAG-003": ("total", 15, 7, 8),
    }
    by_id = {row["diagnostic_id"]: row for row in rows}
    if set(by_id) != set(expected):
        fail(f"lagged retail diagnostic rows changed: {sorted(by_id)}")
    for diagnostic_id, (condition, usable, same, opposite) in expected.items():
        row = by_id[diagnostic_id]
        if row["prior_real_wage_condition"] != condition or row["result_class"] != "descriptive-mechanism-screen":
            fail(f"lagged retail diagnostic classification changed: {diagnostic_id}")
        if (int(row["usable_transitions"]), int(row["same_direction"]), int(row["opposite_direction"])) != (usable, same, opposite):
            fail(f"lagged retail diagnostic values changed: {diagnostic_id}")
        if not resolve_source(RETAIL_LAGGED_DIAGNOSTIC, row["source_artifact"]).exists():
            fail(f"lagged retail diagnostic source missing: {row['source_artifact']}")
        for field in ("what_is_proven", "what_is_not_proven"):
            if not row[field].strip():
                fail(f"lagged retail diagnostic row incomplete: {diagnostic_id} / {field}")


def verify_source_family_routes() -> None:
    if not SOURCE_FAMILY_ROUTES.exists():
        fail(f"missing source-family route ledger: {SOURCE_FAMILY_ROUTES.relative_to(ROOT)}")
    with SOURCE_FAMILY_ROUTES.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "source_family", "primary_route", "local_or_cross_repo_artifact",
            "current_status", "boundary",
        ]
        if reader.fieldnames != expected_header:
            fail(f"source-family route header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "Social research": ("https://www.federalreserve.gov/consumerscommunities/shed.htm", "usable-directional-context", "/home/mehtama1/git-repo/social-research/analysis/social/cross-repository-theme-evidence-matrix.md"),
        "Official macro / affordability data": ("https://www.bls.gov/opub/reports/consumer-expenditures/2024/home.htm", "official-macro-anchor", "analysis/company-first-principles/combined-investment-research-pilot-02-independent-affordability-validation-2026-09-15.md"),
        "Inc. 5000": ("https://www.inc.com/inc5000", "discovery-layer", "/home/mehtama1/git-repo/inc5000-analysis/README.md"),
        "IBIS Industries": ("https://www.ibisworld.com/", "industry-map-context", "../../notes/ibis-industries-crosswalk.md"),
        "Investments article and hard-gate bridge": ("https://www.sec.gov/Archives/edgar/data/1323404/000127956926000263/ex991.htm", "connected-hypothesis-and-triage-layer", "analysis/company-first-principles/combined-investment-research-investments-repo-bridge.md"),
        "Damodaran valuation": ("https://pages.stern.nyu.edu/adamodar/New_Home_Page/lectures/approach.html", "qualified-illustrative", "analysis/company-first-principles/combined-investment-research-method-registry.md"),
        "Lyn Alden macro/liquidity": ("https://www.lynalden.com/fiscal-and-monetary-policy/", "qualified-mechanism-layer", "analysis/company-first-principles/combined-investment-research-method-registry.md"),
    }
    by_family = {row["source_family"]: row for row in rows}
    if set(by_family) != set(expected):
        fail(f"source-family route rows changed: {sorted(by_family)}")
    for family, (route, status, artifact) in expected.items():
        row = by_family[family]
        if row["primary_route"] != route or row["current_status"] != status or row["local_or_cross_repo_artifact"] != artifact:
            fail(f"source-family route changed unexpectedly: {family}")
        if not row["boundary"].strip():
            fail(f"source-family route incomplete: {family}")
        if not resolve_source(SOURCE_FAMILY_ROUTES, row["local_or_cross_repo_artifact"]).exists():
            fail(f"source-family artifact missing: {row['local_or_cross_repo_artifact']}")


def verify_reader_handoff_guides() -> None:
    for path, markers in {
        REVIEWERS_GUIDE: (
            "13 goal requirements",
            "connected but not done",
            "226 evidence gates",
            "quality-of-earnings and\nfinancial-shenanigans overlay",
            "diagnostic register—not a fraud score",
            "3.75%–4.00%",
            "Power-grid customer cash",
            "institutional capital and financial intermediation",
            "normalized common-owner cash is not promoted",
            "annual lease-and-tax cash control",
            "cannot be carried into the current H1 denominator",
            "source-recovery and move-on rule",
            "never reconstructed from memory",
            "highest-value joinable\nobject",
        ),
        NEXT_CYCLE_EXPANSION: (
            "public-evidence-only handoff",
            "FPL Distribution Inspection category recovery",
            "legal entity -> named asset/CUSIP",
            "facility balance -> eligible collateral",
            "QoE and financial-shenanigans\noverlay",
            "does not calculate a cross-lane",
        ),
    }.items():
        if not path.exists():
            fail(f"missing reader handoff guide: {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8").lower()
        for marker in markers:
            if marker.lower() not in text:
                fail(f"reader handoff marker missing from {path.relative_to(ROOT)}: {marker}")


def verify_expansion_lane_verifiers() -> None:
    for script_name in (
        "verify-power-grid-expansion-lane.py",
        "verify-insurance-statutory-expansion-lane.py",
        "verify-asset-backed-expansion-lane.py",
    ):
        script = ROOT / "scripts" / script_name
        if not script.exists():
            fail(f"missing expansion-lane verifier: {script.relative_to(ROOT)}")
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            detail = result.stderr.strip() or result.stdout.strip()
            fail(f"{script_name} failed inside combined verification: {detail}")


def verify_expansion_promotion_action_register() -> None:
    if not EXPANSION_PROMOTION_ACTIONS.exists():
        fail(f"missing expansion promotion action register: {EXPANSION_PROMOTION_ACTIONS.relative_to(ROOT)}")
    expected_header = [
        "queue_id", "lane", "current_status", "current_evidence_artifact", "required_source",
        "time_gate", "join_fields", "promotion_test", "blocked_by", "source_artifact",
    ]
    with EXPANSION_PROMOTION_ACTIONS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"expansion promotion action header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_status = {
        "Q-11": "searched-negative; hold-with-strong-route-visible",
        "Q-12": "evidence-insufficient",
        "Q-13": "evidence-insufficient",
    }
    if len(rows) != 3 or {row["queue_id"] for row in rows} != set(expected_status):
        fail("expansion promotion action register rows changed unexpectedly")
    for row in rows:
        if row["current_status"] != expected_status[row["queue_id"]]:
            fail(f"expansion promotion action status changed: {row['queue_id']}")
        for field in expected_header[1:9]:
            if not row[field].strip():
                fail(f"expansion promotion action field missing: {row['queue_id']} {field}")
        for field in ("current_evidence_artifact", "source_artifact"):
            if not resolve_source(EXPANSION_PROMOTION_ACTIONS, row[field]).exists():
                fail(f"expansion promotion action source missing: {row[field]}")
    memo = PILOT_DIR / "combined-investment-research-next-cycle-candidate-expansion-2026-09-16.md"
    text = memo.read_text(encoding="utf-8")
    for marker in (
        "Current execution checkpoint — 2026-09-17",
        "searched-negative; hold-with-strong-route-visible",
        "evidence-insufficient",
        "structured expansion promotion action register",
    ):
        if marker not in text:
            fail(f"expansion promotion action memo marker missing: {marker}")


def verify_macro_historical_regime_panel() -> None:
    artifact = LEDGER_DIR / "combined-investment-research-macro-historical-regime-validation-2026-09-15.csv"
    if not artifact.exists():
        fail(f"missing {artifact.relative_to(ROOT)}")
    with artifact.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "period", "observation_basis", "cpi_u_annual_average_index",
            "approx_annual_cpi_change_pct", "federal_funds_target_range",
            "real_average_hourly_earnings_yoy_pct", "regime_reading",
            "validation_status", "source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"macro historical regime header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 7 or [row["period"] for row in rows] != ["2020", "2021", "2022", "2023", "2024", "2025", "2026-current"]:
        fail("macro historical regime periods changed unexpectedly")
    for row in rows:
        for field in ("period", "observation_basis", "federal_funds_target_range", "regime_reading", "validation_status", "source_artifact"):
            if not row[field].strip():
                fail(f"macro historical regime field missing: {field}")
        if not resolve_source(artifact, row["source_artifact"]).exists():
            fail(f"macro historical regime source missing: {row['source_artifact']}")
    for row in rows[:6]:
        if "annual CPI average" not in row["observation_basis"] or not row["cpi_u_annual_average_index"].strip():
            fail(f"completed annual regime row lacks annual basis: {row['period']}")
    expected_early_regimes = {
        "2020": ("111.098", "1.2", "0%-0.25%", "3.7"),
        "2021": ("116.318", "4.7", "0%-0.25%", "-2.4"),
    }
    for period, expected_values in expected_early_regimes.items():
        row = next(row for row in rows if row["period"] == period)
        observed_values = (
            row["cpi_u_annual_average_index"],
            row["approx_annual_cpi_change_pct"],
            row["federal_funds_target_range"],
            row["real_average_hourly_earnings_yoy_pct"],
        )
        if observed_values != expected_values:
            fail(f"macro early-regime anchors changed unexpectedly: {period}")
    for previous, current in zip(rows[:5], rows[1:6]):
        previous_index = float(previous["cpi_u_annual_average_index"])
        current_index = float(current["cpi_u_annual_average_index"])
        calculated_change = (current_index / previous_index - 1.0) * 100.0
        reported_change = float(current["approx_annual_cpi_change_pct"])
        if not math.isclose(calculated_change, reported_change, abs_tol=0.15):
            fail(
                f"macro historical CPI arithmetic failed for {current['period']}: "
                f"calculated {calculated_change:.3f} versus reported {reported_change:.3f}"
            )
    current = rows[-1]
    if current["observation_basis"] != "August CPI and real earnings; July target range":
        fail("2026 current regime observation basis changed unexpectedly")
    if current["cpi_u_annual_average_index"].strip():
        fail("2026 current regime must not carry a completed annual CPI average")
    row_2023 = next(row for row in rows if row["period"] == "2023")
    if row_2023["real_average_hourly_earnings_yoy_pct"] != "0.8":
        fail("2023 macro panel must retain the revised BLS real-earnings observation")
    memo = PILOT_DIR / "combined-investment-research-macro-historical-regime-validation-2026-09-15.md"
    memo_text = memo.read_text(encoding="utf-8")
    for marker in (
        "realer_01112024.htm",
        "real-average-hourly-earnings-increased-0-8-percent-from-december-2022-to-december-2023.htm",
        "initial January 2024 release",
        "revised/summary observation",
    ):
        if marker not in memo_text:
            fail(f"macro historical source-reconciliation marker missing: {marker}")


def verify_macro_current_regime_memo() -> None:
    if not MACRO_CURRENT_REGIME_MEMO.exists():
        fail(f"missing current-regime macro memo: {MACRO_CURRENT_REGIME_MEMO.relative_to(ROOT)}")
    memo = MACRO_CURRENT_REGIME_MEMO.read_text(encoding="utf-8")
    lower = memo.lower()
    for marker in (
        "current-regime-validation-partial",
        "3.75%–4.00%",
        "`3.4%` year-over-year headline inflation",
        "`2.4%` core inflation",
        "`16.3%`\nenergy inflation",
        "`3.0%` saving",
        "does not promote the company tests to causal proof",
        "through-cycle validation and causal attribution remain",
    ):
        if marker.lower() not in lower:
            fail(f"current-regime macro boundary marker missing: {marker}")
    for route in (
        "monetary20260916a.htm",
        "cpi_09112026.htm",
        "https://www.bea.gov/news/glance",
    ):
        if route not in memo:
            fail(f"current-regime macro source route missing: {route}")


def verify_macro_longitudinal_retail_bridge() -> None:
    if not MACRO_LONGITUDINAL_RETAIL.exists():
        fail(f"missing {MACRO_LONGITUDINAL_RETAIL.relative_to(ROOT)}")
    with MACRO_LONGITUDINAL_RETAIL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "company", "fiscal_period", "fiscal_timing", "dominant_macro_regime",
            "approx_cpi_change_pct", "federal_funds_target_range",
            "real_hourly_earnings_yoy_pct", "operating_cash_flow_musd",
            "property_or_capex_musd", "cash_after_property_musd", "denominator_status",
            "macro_reading", "boundary", "macro_source_artifact", "company_source_artifact",
        ]
        if reader.fieldnames != expected_header:
            fail(f"macro longitudinal retail header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 18:
        fail(f"macro longitudinal retail row count changed unexpectedly: {len(rows)}")
    companies = {row["company"] for row in rows}
    if companies != {"Target", "Walmart", "TJX"}:
        fail(f"macro longitudinal retail company coverage changed: {companies}")
    expected_historical = {
        ("Target", "FY2020"): (10525, 2649, 7876),
        ("Target", "FY2021"): (8625, 3544, 5081),
        ("Target", "FY2022"): (4018, 5528, -1510),
        ("Walmart", "FY2021"): (36074, 10264, 25810),
        ("Walmart", "FY2022"): (24181, 13106, 11075),
        ("Walmart", "FY2023"): (28841, 16857, 11984),
        ("TJX", "FY2021"): (4562, 568, 3994),
        ("TJX", "FY2022"): (3057, 1045, 2012),
        ("TJX", "FY2023"): (4084, 1457, 2627),
    }
    observed_historical = {
        (row["company"], row["fiscal_period"]): (
            int(row["operating_cash_flow_musd"]),
            int(row["property_or_capex_musd"]),
            int(row["cash_after_property_musd"]),
        )
        for row in rows
        if (row["company"], row["fiscal_period"]) in expected_historical
    }
    if observed_historical != expected_historical:
        fail(f"macro longitudinal historical observations changed: {observed_historical}")
    source_note = PILOT_DIR / "combined-investment-research-macro-longitudinal-retail-source-note-2026-09-16.md"
    if not source_note.exists():
        fail(f"missing longitudinal retail source note: {source_note.relative_to(ROOT)}")
    source_note_text = source_note.read_text(encoding="utf-8")
    for marker in ("FY2020", "FY2021", "FY2022", "CIK 0000027419", "CIK 0000104169", "CIK 0000109198", "-1,510"):
        if marker not in source_note_text:
            fail(f"longitudinal retail source-note marker missing: {marker}")
    for row in rows:
        for field in (
            "company", "fiscal_period", "fiscal_timing", "dominant_macro_regime",
            "federal_funds_target_range", "denominator_status", "macro_reading",
            "boundary", "macro_source_artifact", "company_source_artifact",
        ):
            if not row[field].strip():
                fail(f"macro longitudinal retail field missing: {field}")
        ocf = int(row["operating_cash_flow_musd"])
        capex = int(row["property_or_capex_musd"])
        cash = int(row["cash_after_property_musd"])
        if cash != ocf - capex:
            fail(f"macro longitudinal retail cash arithmetic failed: {row}")
        if row["denominator_status"] not in {"reported-cash-screen", "qualified-cash-screen"}:
            fail(f"macro longitudinal retail status overclaims denominator: {row}")
        for source_field in ("macro_source_artifact", "company_source_artifact"):
            if not resolve_source(MACRO_LONGITUDINAL_RETAIL, row[source_field]).exists():
                fail(f"macro longitudinal retail source missing: {row[source_field]}")


def verify_ca06_quantified_allocation_surface() -> None:
    data_path = LEDGER_DIR / "combined-investment-research-ca06-quantified-allocation-surface-2026-09-16.csv"
    memo_path = PILOT_DIR / "combined-investment-research-ca06-quantified-allocation-surface-2026-09-16.md"
    if not data_path.exists() or not memo_path.exists():
        fail("missing CA-06 quantified allocation surface")
    with data_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    expected = {
        "CA06-001": (-42.310, 444.446),
        "CA06-002": (1631.0, 2186.0),
        "CA06-003": (597.0, 2115.0),
        "CA06-004": (981.0, 5529.0),
        "CA06-005": (0.0, 110.0),
    }
    if len(rows) != len(expected) or {row["surface_id"] for row in rows} != set(expected):
        fail("CA-06 quantified allocation rows changed unexpectedly")
    for row in rows:
        lower, upper = expected[row["surface_id"]]
        if float(row["lower_screened_cash_musd"]) != lower or float(row["upper_screened_cash_musd"]) != upper:
            fail(f"CA-06 allocation surface values changed: {row['surface_id']}")
        if row["status"] != "allocation-sensitivity-only":
            fail(f"CA-06 allocation surface overclaims status: {row['surface_id']}")
        if not row["remaining_upgrade"].strip() or not row["range_basis"].strip():
            fail(f"CA-06 allocation surface row incomplete: {row['surface_id']}")
        if not resolve_source(data_path, row["source_artifact"]).exists():
            fail(f"CA-06 allocation surface source missing: {row['source_artifact']}")
    memo = memo_path.read_text(encoding="utf-8")
    for marker in ("allocation surface", "not a", "new owner-cash estimate", "The ranges are not additive", "Promotion rule"):
        if marker not in memo:
            fail(f"CA-06 allocation memo marker missing: {marker}")


def verify_retail_cohort_working_capital() -> None:
    if not RETAIL_COHORT_WORKING_CAPITAL.exists():
        fail(f"missing {RETAIL_COHORT_WORKING_CAPITAL.relative_to(ROOT)}")
    with RETAIL_COHORT_WORKING_CAPITAL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "screen_id", "queue_id", "company", "period", "inventory_begin_musd",
            "inventory_end_musd", "inventory_change_musd", "accounts_payable_begin_musd",
            "accounts_payable_end_musd", "accounts_payable_change_musd",
            "mechanical_net_signal_musd", "cash_flow_inventory_effect_musd",
            "cash_flow_accounts_payable_effect_musd", "cash_flow_mechanical_signal_musd",
            "status", "source_artifact", "remaining_claims",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail cohort working-capital header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("H1 FY2027", 7297, 7862, 4575, 5024, -603, 470),
        "Target": ("H1 2026", 12304, 13249, 12622, 13306, -945, 612),
        "Walmart": ("H1 FY2027", 58851, 61600, 63061, 64318, -2660, 1648),
    }
    if len(rows) != len(expected) or {row["company"] for row in rows} != set(expected):
        fail("retail cohort working-capital rows changed unexpectedly")
    for row in rows:
        period, inv_begin, inv_end, ap_begin, ap_end, cf_inv, cf_ap = expected[row["company"]]
        if row["period"] != period:
            fail(f"retail cohort working-capital period changed: {row['company']}")
        if int(row["inventory_change_musd"]) != inv_end - inv_begin:
            fail(f"retail cohort inventory arithmetic failed: {row}")
        if int(row["accounts_payable_change_musd"]) != ap_end - ap_begin:
            fail(f"retail cohort payable arithmetic failed: {row}")
        if int(row["mechanical_net_signal_musd"]) != (ap_end - ap_begin) - (inv_end - inv_begin):
            fail(f"retail cohort balance signal arithmetic failed: {row}")
        if int(row["cash_flow_inventory_effect_musd"]) != cf_inv or int(row["cash_flow_accounts_payable_effect_musd"]) != cf_ap:
            fail(f"retail cohort cash-flow inputs changed: {row}")
        if int(row["cash_flow_mechanical_signal_musd"]) != cf_inv + cf_ap:
            fail(f"retail cohort cash-flow signal arithmetic failed: {row}")
        if row["status"] != "balance-and-cash-flow-screen":
            fail(f"retail cohort working-capital status changed: {row}")
        if not resolve_source(RETAIL_COHORT_WORKING_CAPITAL, row["source_artifact"]).exists():
            fail(f"retail cohort working-capital source missing: {row['source_artifact']}")
    memo = (PILOT_DIR / "combined-investment-research-pilot-02-retail-cohort-inventory-payable-balance-screen-2026-09-15.md").read_text(encoding="utf-8")
    for marker in ("Supplier-finance overlay", "$3.2B", "$6.4B", "must not be subtracted from operating cash a second time", "TJX has no comparable"):
        if marker not in memo:
            fail(f"retail cohort working-capital boundary marker missing: {marker}")


def verify_retail_margin_support_transition() -> None:
    if not RETAIL_MARGIN_SUPPORT_TRANSITION.exists():
        fail(f"missing {RETAIL_MARGIN_SUPPORT_TRANSITION.relative_to(ROOT)}")
    with RETAIL_MARGIN_SUPPORT_TRANSITION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_header = [
            "transition_id", "company", "period", "current_net_sales_musd",
            "current_gross_profit_musd", "reported_gross_margin_pct",
            "prior_gross_margin_pct", "reported_change_bp",
            "identifiable_support_musd", "support_removal_gross_profit_musd",
            "support_removal_gross_margin_pct", "support_removal_change_bp",
            "status", "source_artifact", "remaining_claims",
        ]
        if reader.fieldnames != expected_header:
            fail(f"retail margin-support transition header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "RMS-000": ("TJX", "H1 FY2027", 29503, 9552, 32.376369, 30.132306, 224, 331, 9221, 31.254449, 112),
        "RMS-001": ("Target", "H1 2026", 51982, 16318, 31.4, 28.6, 280, 994, 15324, 29.479435, 88),
        "RMS-002": ("Walmart", "H1 FY2027", 361784, 89922, 24.9, 24.3, 53, 2900, 87022, 24.053579, -25),
    }
    if len(rows) != len(expected) or {row["transition_id"] for row in rows} != set(expected):
        fail("retail margin-support transition rows changed unexpectedly")
    for row in rows:
        values = expected[row["transition_id"]]
        company, period, sales, gross_profit, reported_margin, prior_margin, reported_change, support, adjusted_profit, adjusted_margin, adjusted_change = values
        if (row["company"], row["period"]) != (company, period):
            fail(f"retail margin-support transition identity changed: {row['transition_id']}")
        if int(row["current_net_sales_musd"]) != sales or int(row["current_gross_profit_musd"]) != gross_profit:
            fail(f"retail margin-support transition base changed: {row['transition_id']}")
        if float(row["reported_gross_margin_pct"]) != reported_margin or float(row["prior_gross_margin_pct"]) != prior_margin or int(row["reported_change_bp"]) != reported_change:
            fail(f"retail margin-support transition reported margin changed: {row['transition_id']}")
        if int(row["identifiable_support_musd"]) != support or int(row["support_removal_gross_profit_musd"]) != gross_profit - support:
            fail(f"retail margin-support transition support arithmetic failed: {row['transition_id']}")
        if not math.isclose(float(row["support_removal_gross_margin_pct"]), adjusted_margin, abs_tol=0.000001) or int(row["support_removal_change_bp"]) != adjusted_change:
            fail(f"retail margin-support transition adjusted arithmetic failed: {row['transition_id']}")
        if row["status"] != "cohort-support-removal-screen-with-TJX-allocation-boundary" or not row["remaining_claims"].strip():
            fail(f"retail margin-support transition boundary changed: {row['transition_id']}")
        if not resolve_source(RETAIL_MARGIN_SUPPORT_TRANSITION, row["source_artifact"]).exists():
            fail(f"retail margin-support transition source missing: {row['transition_id']}")
    memo = (PILOT_DIR / "combined-investment-research-pilot-02-retail-margin-support-transition-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("margin-support transition screen", "$331M", "$994M", "approximately `$2.9B`", "not a normalized margin", "weaker `candidate` label"):
        if marker not in memo:
            fail(f"retail margin-support transition marker missing: {marker}")


def verify_quality_of_earnings_overlay() -> None:
    if not QOE_OVERLAY.exists():
        fail(f"missing QoE overlay: {QOE_OVERLAY.relative_to(ROOT)}")
    expected_header = [
        "overlay_id", "pilot", "risk_family", "diagnostic", "current_evidence",
        "current_status", "proof_grade", "upgrade_test", "source_artifact",
    ]
    with QOE_OVERLAY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"QoE overlay header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_ids = {f"QOE-{index:03d}" for index in range(1, 13)}
    if {row["overlay_id"] for row in rows} != expected_ids:
        fail("QoE overlay rows changed unexpectedly")
    for row in rows:
        if not all(row[field].strip() for field in expected_header):
            fail(f"QoE overlay row incomplete: {row['overlay_id']}")
        if row["current_status"] not in {"observed", "partial", "searched-negative", "not-assembled"}:
            fail(f"QoE overlay status changed: {row['overlay_id']}")
        if row["proof_grade"] not in {"qualified", "unresolved"}:
            fail(f"QoE overlay proof grade changed: {row['overlay_id']}")
        if not resolve_source(QOE_OVERLAY, row["source_artifact"]).exists():
            fail(f"QoE overlay source missing: {row['overlay_id']}")
    by_id = {row["overlay_id"]: row for row in rows}
    if by_id["QOE-010"]["current_status"] != "searched-negative":
        fail("QoE settlement boundary lost searched-negative status")
    if by_id["QOE-012"]["current_status"] != "not-assembled" or by_id["QOE-012"]["proof_grade"] != "unresolved":
        fail("QoE composite accrual boundary changed")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-financial-shenanigans-overlay-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("not a mechanical", "Beneish-style", "not a fraud finding", "not-assembled"):
        if marker not in memo:
            fail(f"QoE overlay boundary marker missing: {marker}")
    methods_memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-forensic-methods-map-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("Sloan accrual-versus-cash persistence", "Beneish M-score family", "Schilit-style financial-shenanigans review", "same entity + same period"):
        if marker not in methods_memo:
            fail(f"QoE forensic methods marker missing: {marker}")
    if not QOE_COMPOSITE_SCHEMA.exists():
        fail(f"missing QoE composite schema: {QOE_COMPOSITE_SCHEMA.relative_to(ROOT)}")
    with QOE_COMPOSITE_SCHEMA.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        expected_schema_header = [
            "input_id", "input_family", "model_field", "current_status",
            "current_observation", "required_for", "upgrade_test",
            "source_artifact", "proof_grade",
        ]
        if reader.fieldnames != expected_schema_header:
            fail(f"QoE composite schema header mismatch: {reader.fieldnames}")
        schema_rows = list(reader)
    if len(schema_rows) != 14 or {row["input_id"] for row in schema_rows} != {f"QOE-INPUT-{index:03d}" for index in range(1, 15)}:
        fail("QoE composite schema rows changed unexpectedly")
    for row in schema_rows:
        if not all(row[field].strip() for field in expected_schema_header):
            fail(f"QoE composite schema row incomplete: {row['input_id']}")
        if row["current_status"] not in {"observed", "partial", "missing", "diagnostic-panel-assembled-not-promotable"}:
            fail(f"QoE composite schema status changed: {row['input_id']}")
        if not resolve_source(QOE_COMPOSITE_SCHEMA, row["source_artifact"]).exists():
            fail(f"QoE composite schema source missing: {row['input_id']}")
    schema_memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-composite-input-schema-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("minimum comparable inputs", "not-assembled", "not proof of fraud"):
        if marker not in schema_memo:
            fail(f"QoE composite schema boundary marker missing: {marker}")
    if not QOE_RETAIL_COMPONENT_SCREEN.exists():
        fail(f"missing retail QoE component screen: {QOE_RETAIL_COMPONENT_SCREEN.relative_to(ROOT)}")
    with QOE_RETAIL_COMPONENT_SCREEN.open(newline="", encoding="utf-8") as handle:
        component_reader = csv.DictReader(handle)
        expected_component_header = [
            "screen_id", "company", "from_period", "to_period",
            "receivables_index", "sg_index", "depreciation_index",
            "sga_or_osga_index", "claims_index", "accrual_proxy_current_assets",
            "available_components", "unavailable_components", "diagnostic_reading",
            "status", "source_artifact",
        ]
        if component_reader.fieldnames != expected_component_header:
            fail(f"retail QoE component-screen header mismatch: {component_reader.fieldnames}")
        component_rows = list(component_reader)
    if len(component_rows) != 6 or {row["company"] for row in component_rows} != {"TJX", "Target", "Walmart"}:
        fail("retail QoE component-screen rows changed unexpectedly")
    required_component_fields = [
        field for field in expected_component_header
        if field not in {"receivables_index"}
    ]
    for row in component_rows:
        if not all(row[field].strip() for field in required_component_fields):
            fail(f"retail QoE component-screen row incomplete: {row['screen_id']}")
        if row["status"] != "diagnostic-only" or not resolve_source(QOE_RETAIL_COMPONENT_SCREEN, row["source_artifact"]).exists():
            fail(f"retail QoE component-screen boundary changed: {row['screen_id']}")
    component_memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-component-screen-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("six same-company annual transitions", "standard Beneish total-accruals variable", "composite-score-not-promotable", "does not establish a financial-shenanigans finding"):
        if marker not in component_memo:
            fail(f"retail QoE component-screen marker missing: {marker}")
    forensic_gate_memos = {
        "combined-investment-research-quality-of-earnings-tjx-historical-vector-2026-09-16.md": (
            "Forensic promotion gate", "Sloan-style cash/accrual review", "Beneish-style screen", "Not calculated",
        ),
        "combined-investment-research-quality-of-earnings-target-historical-vector-2026-09-16.md": (
            "Forensic promotion gate", "receivables field remains", "Beneish-style screen", "Not calculated",
        ),
        "combined-investment-research-quality-of-earnings-walmart-historical-vector-2026-09-16.md": (
            "Forensic promotion gate", "Walmart's OSG&A presentation", "Beneish-style screen", "Not calculated",
        ),
        "combined-investment-research-quality-of-earnings-retail-comparability-bridge-2026-09-16.md": (
            "Method-level promotion gate", "Sloan-style cash/accrual review", "Beneish-style composite", "Not calculated",
        ),
    }
    for memo_name, markers in forensic_gate_memos.items():
        memo_text = (PILOT_DIR / memo_name).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in memo_text:
                fail(f"QoE forensic promotion marker missing from {memo_name}: {marker}")


def verify_retail_qoe_cash_conversion() -> None:
    if not QOE_RETAIL_CASH_CONVERSION.exists():
        fail(f"missing retail QoE cash screen: {QOE_RETAIL_CASH_CONVERSION.relative_to(ROOT)}")
    expected_header = [
        "screen_id", "company", "fiscal_period", "dominant_macro_regime",
        "operating_cash_flow_musd", "property_or_capex_musd", "cash_after_property_musd",
        "capex_intensity", "cash_after_property_conversion", "negative_cash_after_property",
        "diagnostic_status", "source_artifact",
    ]
    with QOE_RETAIL_CASH_CONVERSION.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail QoE cash screen header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 18:
        fail(f"retail QoE cash screen row count changed: {len(rows)}")
    negative = []
    for row in rows:
        ocf = float(row["operating_cash_flow_musd"])
        capex = float(row["property_or_capex_musd"])
        after = float(row["cash_after_property_musd"])
        if not math.isclose(after, ocf - capex, abs_tol=0.01):
            fail(f"retail QoE cash arithmetic failed: {row['screen_id']}")
        if not math.isclose(float(row["capex_intensity"]), capex / ocf, abs_tol=0.000001):
            fail(f"retail QoE capex intensity failed: {row['screen_id']}")
        if not math.isclose(float(row["cash_after_property_conversion"]), after / ocf, abs_tol=0.000001):
            fail(f"retail QoE conversion failed: {row['screen_id']}")
        if not resolve_source(QOE_RETAIL_CASH_CONVERSION, row["source_artifact"]).exists():
            fail(f"retail QoE cash source missing: {row['screen_id']}")
        if row["negative_cash_after_property"] == "true":
            negative.append(row["screen_id"])
            if row["diagnostic_status"] != "stress-flag-not-fraud":
                fail("retail QoE negative screen was over-promoted")
    if negative != ["QOE-CASH-003"]:
        fail(f"retail QoE negative-screen set changed: {negative}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-cash-conversion-screen-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("18 company-period observations", "not a Beneish score", "not proof of"):
        if marker not in memo:
            fail(f"retail QoE cash screen marker missing: {marker}")


def verify_current_retail_earnings_cash_screen() -> None:
    if not QOE_CURRENT_RETAIL_EARNINGS_CASH.exists():
        fail(f"missing current retail QoE screen: {QOE_CURRENT_RETAIL_EARNINGS_CASH.relative_to(ROOT)}")
    expected_header = [
        "screen_id", "company", "period", "net_income_musd", "net_income_basis",
        "operating_cash_flow_musd", "property_spending_musd", "ocf_to_net_income",
        "cash_after_property_musd", "cash_after_property_to_net_income", "status",
        "source_artifact",
    ]
    with QOE_CURRENT_RETAIL_EARNINGS_CASH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"current retail QoE header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "QOE-CURRENT-001": ("TJX", "H1 FY2027", 2852, 3345, 1159, 2186),
        "QOE-CURRENT-002": ("Target", "H1 2026", 2658, 4519, 2404, 2115),
        "QOE-CURRENT-003": ("Walmart", "H1 FY2027", 11696, 19710, 14181, 5529),
    }
    if {row["screen_id"] for row in rows} != set(expected):
        fail("current retail QoE rows changed unexpectedly")
    for row in rows:
        screen_id = row["screen_id"]
        company, period, net_income, ocf, capex, after = expected[screen_id]
        if (row["company"], row["period"]) != (company, period):
            fail(f"current retail QoE identity changed: {screen_id}")
        if (int(row["net_income_musd"]), int(row["operating_cash_flow_musd"]), int(row["property_spending_musd"]), int(row["cash_after_property_musd"])) != (net_income, ocf, capex, after):
            fail(f"current retail QoE values changed: {screen_id}")
        if not math.isclose(float(row["ocf_to_net_income"]), ocf / net_income, abs_tol=0.000001):
            fail(f"current retail QoE OCF conversion failed: {screen_id}")
        if not math.isclose(float(row["cash_after_property_to_net_income"]), after / net_income, abs_tol=0.000001):
            fail(f"current retail QoE cash conversion failed: {screen_id}")
        if row["status"] != "reported-period-screen" or not row["net_income_basis"].strip():
            fail(f"current retail QoE boundary changed: {screen_id}")
        if not resolve_source(QOE_CURRENT_RETAIL_EARNINGS_CASH, row["source_artifact"]).exists():
            fail(f"current retail QoE source missing: {screen_id}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-current-retail-earnings-cash-screen-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("matched current-period earnings comparison", "not normalized owner cash", "attributable to Walmart"):
        if marker not in memo:
            fail(f"current retail QoE marker missing: {marker}")


def verify_current_retail_composite_input_panel() -> None:
    if not QOE_CURRENT_RETAIL_COMPOSITE_PANEL.exists():
        fail(f"missing current retail composite panel: {QOE_CURRENT_RETAIL_COMPOSITE_PANEL.relative_to(ROOT)}")
    expected_header = [
        "company", "period", "revenue_musd", "net_income_musd", "net_income_basis",
        "receivables_musd", "inventory_musd", "accounts_payable_musd", "current_assets_musd",
        "net_ppe_musd", "da_musd", "sga_musd", "debt_and_lease_claims_musd", "sbc_musd",
        "diluted_shares_m", "diluted_shares_basis", "operating_cash_flow_musd",
        "property_spending_musd", "input_status", "qoe_observation", "source_artifact",
    ]
    with QOE_CURRENT_RETAIL_COMPOSITE_PANEL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"current retail composite panel header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("H1 FY2027", 29503, 2852, 665, 7862, 5024, 15329, 8567, 676, 3345, 1159),
        "Target": ("H1 2026", 51982, 2658, None, 13249, 13306, 20928, 34767, 1597, 4519, 2404),
        "Walmart": ("H1 FY2027", 361784, 11696, 11075, 61600, 64318, 88703, 142482, 7746, 19710, 14181),
    }
    if {row["company"] for row in rows} != set(expected) or len(rows) != 3:
        fail("current retail composite panel company set changed unexpectedly")
    for row in rows:
        period, revenue, net_income, receivables, inventory, payable, current_assets, ppe, da, ocf, capex = expected[row["company"]]
        if row["period"] != period or row["input_status"] != "partial":
            fail(f"current retail composite panel identity/status changed: {row['company']}")
        numeric = {
            "revenue_musd": revenue, "net_income_musd": net_income,
            "inventory_musd": inventory, "accounts_payable_musd": payable,
            "current_assets_musd": current_assets, "net_ppe_musd": ppe,
            "da_musd": da, "operating_cash_flow_musd": ocf,
            "property_spending_musd": capex,
        }
        if receivables is not None:
            numeric["receivables_musd"] = receivables
        for field, value in numeric.items():
            if int(row[field]) != value:
                fail(f"current retail composite panel value changed: {row['company']} {field}")
        if receivables is None and row["receivables_musd"].strip():
            fail("Target receivables should remain missing")
        if not row["source_artifact"].startswith("https://www.sec.gov/"):
            fail(f"current retail composite panel source route changed: {row['company']}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-current-retail-composite-input-panel-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("not a Beneish score", "Target's current earnings", "composite score"):
        if marker not in memo:
            fail(f"current retail composite panel marker missing: {marker}")


def verify_current_retail_diagnostic_ratio_panel() -> None:
    panel = LEDGER_DIR / "combined-investment-research-quality-of-earnings-current-retail-diagnostic-ratio-panel-2026-09-16.csv"
    if not panel.exists():
        fail(f"missing current retail diagnostic ratio panel: {panel.relative_to(ROOT)}")
    expected_header = [
        "company", "period", "operating_cash_flow_musd", "net_income_musd",
        "cash_after_property_musd", "inventory_change_musd", "accounts_payable_change_musd",
        "revenue_musd", "da_musd", "net_ppe_musd", "sbc_musd", "debt_and_lease_claims_musd",
        "ocf_to_net_income", "cash_after_property_to_net_income", "capex_to_ocf",
        "net_inventory_less_ap_change_to_revenue", "inventory_change_to_revenue",
        "accounts_payable_change_to_revenue", "da_to_net_ppe", "sbc_to_net_income",
        "debt_and_lease_claims_to_ocf", "diagnostic_status", "source_artifact",
    ]
    with panel.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"current retail diagnostic ratio header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": (3345, 2852, 2186, 565, 449, 29503, 676, 8567, 85, 14317),
        "Target": (4519, 2658, 2115, 945, 684, 51982, 1597, 34767, 154, None),
        "Walmart": (19710, 11696, 5529, 2749, 1257, 361784, 7746, 142482, None, 73755),
    }
    if {row["company"] for row in rows} != set(expected) or len(rows) != 3:
        fail("current retail diagnostic ratio company set changed unexpectedly")
    for row in rows:
        company = row["company"]
        ocf, ni, after, inv_delta, ap_delta, revenue, da, ppe, sbc, claims = expected[company]
        if row["diagnostic_status"] != "current-period-diagnostic-partial":
            fail(f"current retail diagnostic ratio status changed: {company}")
        if (int(row["operating_cash_flow_musd"]), int(row["net_income_musd"]), int(row["cash_after_property_musd"])) != (ocf, ni, after):
            fail(f"current retail diagnostic ratio base values changed: {company}")
        expected_capex = ocf - after
        expected_ratios = {
            "ocf_to_net_income": ocf / ni,
            "cash_after_property_to_net_income": after / ni,
            "capex_to_ocf": expected_capex / ocf,
            "net_inventory_less_ap_change_to_revenue": (inv_delta - ap_delta) / revenue,
            "inventory_change_to_revenue": inv_delta / revenue,
            "accounts_payable_change_to_revenue": ap_delta / revenue,
            "da_to_net_ppe": da / ppe,
        }
        if sbc is not None:
            expected_ratios["sbc_to_net_income"] = sbc / ni
        if claims is not None:
            expected_ratios["debt_and_lease_claims_to_ocf"] = claims / ocf
        for field, value in expected_ratios.items():
            if not math.isclose(float(row[field]), value, abs_tol=0.000001):
                fail(f"current retail diagnostic ratio arithmetic failed: {company} {field}")
        if sbc is None and row["sbc_to_net_income"].strip():
            fail(f"current retail diagnostic SBC should remain missing: {company}")
        if claims is None and row["debt_and_lease_claims_to_ocf"].strip():
            fail(f"current retail diagnostic claims should remain missing: {company}")
        if not resolve_source(panel, row["source_artifact"]).exists():
            fail(f"current retail diagnostic source missing: {company}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-current-retail-diagnostic-ratio-panel-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("not a Beneish score", "not evidence of financial shenanigans", "current-period-diagnostic-partial"):
        if marker not in memo:
            fail(f"current retail diagnostic ratio marker missing: {marker}")


def verify_tjx_historical_qoe_vector() -> None:
    vector = LEDGER_DIR / "combined-investment-research-quality-of-earnings-tjx-historical-vector-2026-09-16.csv"
    if not vector.exists():
        fail(f"missing TJX historical QoE vector: {vector.relative_to(ROOT)}")
    expected_header = [
        "company", "fiscal_year", "revenue_musd", "net_income_musd", "receivables_musd",
        "inventory_musd", "accounts_payable_musd", "current_assets_musd", "net_ppe_musd",
        "da_musd", "sga_musd", "debt_and_lease_claims_musd", "sbc_musd", "diluted_shares_m",
        "operating_cash_flow_musd", "property_additions_musd", "equity_investment_purchases_musd",
        "inventory_cash_use_musd", "accounts_payable_cash_source_musd", "ocf_to_net_income",
        "cash_after_property_to_net_income", "capex_to_ocf", "da_to_net_ppe", "sbc_to_net_income",
        "debt_and_lease_claims_to_ocf", "status", "source_artifact",
    ]
    with vector.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"TJX historical QoE vector header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "FY2024": (54217, 4474, 6057, 1722, 145, 64, 964, 6571, 160, 12542),
        "FY2025": (56360, 4864, 6116, 1918, 539, 448, 1104, 7346, 183, 12778),
        "FY2026": (60372, 5494, 6874, 1957, 724, 239, 1247, 8220, 214, 13489),
    }
    if {row["fiscal_year"] for row in rows} != set(expected) or len(rows) != 3:
        fail("TJX historical QoE vector periods changed unexpectedly")
    for row in rows:
        year = row["fiscal_year"]
        revenue, ni, ocf, capex, inv_use, ap_source, da, ppe, sbc, claims = expected[year]
        if row["company"] != "TJX" or row["status"] != "TJX-company-history-partial":
            fail(f"TJX historical QoE vector identity/status changed: {year}")
        values = {"revenue_musd": revenue, "net_income_musd": ni, "operating_cash_flow_musd": ocf, "property_additions_musd": capex, "inventory_cash_use_musd": inv_use, "accounts_payable_cash_source_musd": ap_source, "da_musd": da, "net_ppe_musd": ppe, "sbc_musd": sbc, "debt_and_lease_claims_musd": claims}
        for field, value in values.items():
            if int(row[field]) != value:
                fail(f"TJX historical QoE vector value changed: {year} {field}")
        expected_ratios = {
            "ocf_to_net_income": ocf / ni,
            "cash_after_property_to_net_income": (ocf - capex) / ni,
            "capex_to_ocf": capex / ocf,
            "da_to_net_ppe": da / ppe,
            "sbc_to_net_income": sbc / ni,
            "debt_and_lease_claims_to_ocf": claims / ocf,
        }
        for field, value in expected_ratios.items():
            if not math.isclose(float(row[field]), value, abs_tol=0.000001):
                fail(f"TJX historical QoE vector arithmetic failed: {year} {field}")
        if not row["source_artifact"].startswith("https://www.sec.gov/"):
            fail(f"TJX historical QoE source route changed: {year}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-tjx-historical-vector-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("same-company QoE vector", "cross-company Beneish score", "maintenance-versus-growth capital"):
        if marker not in memo:
            fail(f"TJX historical QoE marker missing: {marker}")


def verify_target_historical_qoe_vector() -> None:
    vector = LEDGER_DIR / "combined-investment-research-quality-of-earnings-target-historical-vector-2026-09-16.csv"
    if not vector.exists():
        fail(f"missing Target historical QoE vector: {vector.relative_to(ROOT)}")
    expected_header = [
        "company", "fiscal_year", "revenue_musd", "net_income_musd", "receivables_musd",
        "inventory_musd", "accounts_payable_musd", "current_assets_musd", "net_ppe_musd",
        "da_musd", "sga_musd", "debt_and_disclosed_lease_claims_musd", "sbc_musd",
        "diluted_shares_m", "operating_cash_flow_musd", "property_additions_musd",
        "inventory_cash_effect_musd", "accounts_payable_cash_effect_musd", "ocf_to_net_income",
        "cash_after_property_to_net_income", "capex_to_ocf", "da_to_net_ppe", "sbc_to_net_income",
        "debt_and_disclosed_lease_claims_to_ocf", "status", "source_artifact",
    ]
    with vector.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Target historical QoE vector header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "FY2023": (107412, 4138, 8621, 4806, 1613, -1216, 2801, 33096, 251, 19317),
        "FY2024": (106566, 4091, 7367, 2891, -854, 1008, 2981, 33022, 304, 19522),
        "FY2025": (104780, 3705, 6562, 3727, 436, -501, 3134, 33749, 281, 19918),
    }
    if {row["fiscal_year"] for row in rows} != set(expected) or len(rows) != 3:
        fail("Target historical QoE vector periods changed unexpectedly")
    for row in rows:
        year = row["fiscal_year"]
        revenue, ni, ocf, capex, inv_effect, ap_effect, da, ppe, sbc, claims = expected[year]
        if row["company"] != "Target" or row["status"] != "Target-company-history-partial":
            fail(f"Target historical QoE vector identity/status changed: {year}")
        values = {"revenue_musd": revenue, "net_income_musd": ni, "operating_cash_flow_musd": ocf, "property_additions_musd": capex, "inventory_cash_effect_musd": inv_effect, "accounts_payable_cash_effect_musd": ap_effect, "da_musd": da, "net_ppe_musd": ppe, "sbc_musd": sbc, "debt_and_disclosed_lease_claims_musd": claims}
        for field, value in values.items():
            if int(row[field]) != value:
                fail(f"Target historical QoE vector value changed: {year} {field}")
        expected_ratios = {
            "ocf_to_net_income": ocf / ni,
            "cash_after_property_to_net_income": (ocf - capex) / ni,
            "capex_to_ocf": capex / ocf,
            "da_to_net_ppe": da / ppe,
            "sbc_to_net_income": sbc / ni,
            "debt_and_disclosed_lease_claims_to_ocf": claims / ocf,
        }
        for field, value in expected_ratios.items():
            if not math.isclose(float(row[field]), value, abs_tol=0.000001):
                fail(f"Target historical QoE vector arithmetic failed: {year} {field}")
        if row["receivables_musd"].strip():
            fail(f"Target receivables should remain missing: {year}")
        if not row["source_artifact"].startswith("https://www.sec.gov/"):
            fail(f"Target historical QoE source route changed: {year}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-target-historical-vector-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("second same-company annual QoE vector", "receivables field", "cross-company Beneish score"):
        if marker not in memo:
            fail(f"Target historical QoE marker missing: {marker}")


def verify_walmart_historical_qoe_vector() -> None:
    vector = LEDGER_DIR / "combined-investment-research-quality-of-earnings-walmart-historical-vector-2026-09-16.csv"
    if not vector.exists():
        fail(f"missing Walmart historical QoE vector: {vector.relative_to(ROOT)}")
    expected_header = [
        "company", "fiscal_year", "total_revenue_musd", "consolidated_net_income_musd",
        "attributable_net_income_musd", "noncontrolling_interest_musd", "receivables_musd",
        "inventory_musd", "accounts_payable_musd", "current_assets_musd", "net_ppe_musd",
        "da_musd", "osga_musd", "debt_and_lease_claims_musd", "sbc_musd", "diluted_shares_m",
        "operating_cash_flow_musd", "property_additions_musd", "acquisitions_musd",
        "strategic_investment_disposals_musd", "receivables_cash_effect_musd", "inventory_cash_effect_musd",
        "accounts_payable_cash_effect_musd", "supplier_finance_obligations_musd",
        "ocf_to_attributable_net_income", "cash_after_property_to_attributable_net_income",
        "capex_to_ocf", "da_to_net_ppe", "sbc_to_attributable_net_income",
        "debt_and_lease_claims_to_ocf", "status", "source_artifact",
    ]
    with vector.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"Walmart historical QoE vector header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "FY2024": (648125, 16270, 15511, 759, 35726, 20606, 9, 0, -797, 2017, 2515, 11853, 110810, 2093, 51321, 8108),
        "FY2025": (680985, 20157, 19436, 721, 36443, 23783, 1896, 4080, -1106, -2755, 3228, 12973, 119993, 2769, 60114, 8081),
        "FY2026": (713163, 22270, 21893, 377, 41565, 26642, 53, 927, -1136, -1443, 1611, 14203, 136083, 3603, 67095, 8022),
    }
    if {row["fiscal_year"] for row in rows} != set(expected) or len(rows) != 3:
        fail("Walmart historical QoE vector periods changed unexpectedly")
    for row in rows:
        year = row["fiscal_year"]
        revenue, consolidated_ni, attributable_ni, nci, ocf, capex, acquisitions, disposals, receivable_effect, inv_effect, ap_effect, da, ppe, sbc, claims, shares = expected[year]
        if row["company"] != "Walmart" or row["status"] != "Walmart-company-history-partial":
            fail(f"Walmart historical QoE vector identity/status changed: {year}")
        values = {
            "total_revenue_musd": revenue, "consolidated_net_income_musd": consolidated_ni,
            "attributable_net_income_musd": attributable_ni, "noncontrolling_interest_musd": nci,
            "operating_cash_flow_musd": ocf, "property_additions_musd": capex,
            "acquisitions_musd": acquisitions, "strategic_investment_disposals_musd": disposals,
            "receivables_cash_effect_musd": receivable_effect, "inventory_cash_effect_musd": inv_effect,
            "accounts_payable_cash_effect_musd": ap_effect, "da_musd": da, "net_ppe_musd": ppe,
            "sbc_musd": sbc, "debt_and_lease_claims_musd": claims, "diluted_shares_m": shares,
        }
        for field, value in values.items():
            if float(row[field]) != value:
                fail(f"Walmart historical QoE vector value changed: {year} {field}")
        expected_ratios = {
            "ocf_to_attributable_net_income": ocf / attributable_ni,
            "cash_after_property_to_attributable_net_income": (ocf - capex) / attributable_ni,
            "capex_to_ocf": capex / ocf,
            "da_to_net_ppe": da / ppe,
            "sbc_to_attributable_net_income": sbc / attributable_ni,
            "debt_and_lease_claims_to_ocf": claims / ocf,
        }
        for field, value in expected_ratios.items():
            if not math.isclose(float(row[field]), value, abs_tol=0.000001):
                fail(f"Walmart historical QoE vector arithmetic failed: {year} {field}")
        if not row["source_artifact"].startswith("https://www.sec.gov/"):
            fail(f"Walmart historical QoE source route changed: {year}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-walmart-historical-vector-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("third same-company annual QoE vector", "attributable to Walmart", "Supplier-finance obligations"):
        if marker not in memo:
            fail(f"Walmart historical QoE marker missing: {marker}")


def verify_retail_qoe_comparability_bridge() -> None:
    if not QOE_RETAIL_COMPARABILITY.exists():
        fail(f"missing retail QoE comparability bridge: {QOE_RETAIL_COMPARABILITY.relative_to(ROOT)}")
    expected_header = [
        "company", "fiscal_year", "fiscal_period_end", "revenue_basis", "earnings_basis",
        "cash_basis", "receivables_status", "inventory_status", "accounts_payable_status",
        "current_assets_status", "ppe_da_status", "expense_taxonomy_status", "claims_status",
        "sbc_dilution_status", "transaction_status", "comparable_cash_screen_status",
        "composite_accrual_status", "primary_source",
    ]
    with QOE_RETAIL_COMPARABILITY.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail QoE comparability header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 9 or {row["company"] for row in rows} != {"TJX", "Target", "Walmart"}:
        fail("retail QoE comparability row set changed unexpectedly")
    expected_periods = {
        "TJX": {"FY2024", "FY2025", "FY2026"},
        "Target": {"FY2023", "FY2024", "FY2025"},
        "Walmart": {"FY2024", "FY2025", "FY2026"},
    }
    for company, periods in expected_periods.items():
        company_rows = [row for row in rows if row["company"] == company]
        if len(company_rows) != 3 or {row["fiscal_year"] for row in company_rows} != periods:
            fail(f"retail QoE comparability periods changed: {company}")
    for row in rows:
        if row["comparable_cash_screen_status"] != "comparable-diagnostic" or row["composite_accrual_status"] != "not-promotable":
            fail(f"retail QoE comparability promotion status changed: {row['company']} {row['fiscal_year']}")
        if row["company"] == "Target" and row["receivables_status"] != "missing":
            fail("Target receivables comparability boundary changed")
        if row["company"] == "Walmart" and not row["expense_taxonomy_status"].startswith("partial:"):
            fail("Walmart OSG&A comparability boundary changed")
        if not row["primary_source"].startswith("https://www.sec.gov/"):
            fail(f"retail QoE comparability source route changed: {row['company']} {row['fiscal_year']}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-comparability-bridge-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("does not calculate a Beneish score", "Target does not separately disclose", "OSG&A", "not-promotable"):
        if marker not in memo:
            fail(f"retail QoE comparability marker missing: {marker}")


def verify_retail_qoe_trend_diagnostics() -> None:
    if not QOE_RETAIL_TREND_DIAGNOSTICS.exists():
        fail(f"missing retail QoE trend diagnostics: {QOE_RETAIL_TREND_DIAGNOSTICS.relative_to(ROOT)}")
    expected_header = [
        "company", "start_fiscal_year", "end_fiscal_year", "ocf_to_earnings_start",
        "ocf_to_earnings_end", "cash_after_property_to_earnings_start",
        "cash_after_property_to_earnings_end", "claims_to_ocf_start", "claims_to_ocf_end",
        "sbc_to_earnings_start", "sbc_to_earnings_end", "cash_conversion_flag",
        "reinvestment_flag", "claims_flag", "dilution_flag", "follow_up_priority",
        "interpretation", "source_artifact",
    ]
    with QOE_RETAIL_TREND_DIAGNOSTICS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail QoE trend diagnostics header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": ("FY2024", "FY2026", 1.353822, 1.251183, 0.968932, 0.894976, "medium"),
        "Target": ("FY2023", "FY2025", 2.083374, 1.771120, 0.921943, 0.765182, "high"),
        "Walmart": ("FY2024", "FY2026", 2.303269, 1.898552, 0.974792, 0.681633, "high"),
    }
    if len(rows) != 3 or {row["company"] for row in rows} != set(expected):
        fail("retail QoE trend diagnostic company set changed unexpectedly")
    for row in rows:
        company = row["company"]
        start_year, end_year, ocf_start, ocf_end, after_start, after_end, priority = expected[company]
        if (row["start_fiscal_year"], row["end_fiscal_year"], row["follow_up_priority"]) != (start_year, end_year, priority):
            fail(f"retail QoE trend diagnostic identity changed: {company}")
        for field, value in {
            "ocf_to_earnings_start": ocf_start, "ocf_to_earnings_end": ocf_end,
            "cash_after_property_to_earnings_start": after_start,
            "cash_after_property_to_earnings_end": after_end,
        }.items():
            if not math.isclose(float(row[field]), value, abs_tol=0.000001):
                fail(f"retail QoE trend diagnostic value changed: {company} {field}")
        if not row["source_artifact"].endswith(".csv"):
            fail(f"retail QoE trend diagnostic source route changed: {company}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-trend-diagnostics-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("not a financial-shenanigans score", "TJX", "Target", "Walmart", "does not establish"):
        if marker not in memo:
            fail(f"retail QoE trend diagnostic marker missing: {marker}")


def verify_ca06_promotion_matrix() -> None:
    if not CA06_PROMOTION_MATRIX.exists():
        fail(f"missing CA-06 promotion matrix: {CA06_PROMOTION_MATRIX.relative_to(ROOT)}")
    expected_header = [
        "pilot", "base_period", "reported_cash_denominator", "working_capital_status",
        "temporary_support_status", "reinvestment_status", "lease_status", "tax_status",
        "service_or_asset_allocation_status", "senior_claim_status", "dilution_or_nci_status",
        "legal_entity_receipt_status", "final_owner_cash_status", "promotion_status",
        "next_required_source",
    ]
    with CA06_PROMOTION_MATRIX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"CA-06 promotion matrix header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_pilots = {"Wheaton-Antamina", "Retail cohort", "Apollo-Athene"}
    if len(rows) != 3 or {row["pilot"] for row in rows} != expected_pilots:
        fail("CA-06 promotion matrix pilot set changed unexpectedly")
    for row in rows:
        if row["promotion_status"] != "allocation-sensitivity-only":
            fail(f"CA-06 promotion status changed: {row['pilot']}")
        if row["final_owner_cash_status"] != "missing":
            fail(f"CA-06 final owner-cash status changed: {row['pilot']}")
        if not row["next_required_source"].strip():
            fail(f"CA-06 next source missing: {row['pilot']}")
    memo = (PILOT_DIR / "combined-investment-research-ca06-promotion-matrix-2026-09-16.md").read_text(encoding="utf-8")
    for marker in (
        "sixth definition-of-done",
        "Wheaton–Antamina",
        "Retail cohort",
        "Apollo–Athene",
        "promotion-ready",
        "Minimum promotion bundle",
        "legal entity, period",
        "allocation-sensitivity-only",
        "QoE and financial-shenanigans gate",
        "These are reconciliation prompts, not a",
        "No row may be promoted because a diagnostic score looks favorable",
    ):
        if marker not in memo:
            fail(f"CA-06 promotion matrix marker missing: {marker}")


def verify_valuation_promotion_matrix() -> None:
    if not VALUATION_PROMOTION_MATRIX.exists():
        fail(f"missing valuation promotion matrix: {VALUATION_PROMOTION_MATRIX.relative_to(ROOT)}")
    expected_header = [
        "case", "market_or_transaction_basis", "valuation_object",
        "implied_expectation_or_burden", "base_input_status", "owner_cash_or_return_status",
        "proof_grade", "required_join", "thesis_breaker",
    ]
    with VALUATION_PROMOTION_MATRIX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"valuation promotion matrix header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_cases = {"Wheaton-Antamina", "TJX", "Target", "Walmart", "Apollo-Athene"}
    if len(rows) != 5 or {row["case"] for row in rows} != expected_cases:
        fail("valuation promotion matrix case set changed unexpectedly")
    for row in rows:
        if row["proof_grade"] != "qualified-expectation-screen":
            fail(f"valuation promotion grade changed: {row['case']}")
        if row["owner_cash_or_return_status"] != "not promotable to normalized owner cash" and row["owner_cash_or_return_status"] != "not promotable to asset-level return" and row["owner_cash_or_return_status"] != "not promotable to common-owner residual":
            fail(f"valuation promotion boundary changed: {row['case']}")
        if not row["required_join"].strip() or not row["thesis_breaker"].strip():
            fail(f"valuation promotion join or breaker missing: {row['case']}")
    memo = (PILOT_DIR / "combined-investment-research-valuation-promotion-matrix-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("Damodaran-style", "Wheaton–Antamina", "Retail", "Apollo–Athene", "qualified-expectation-screen"):
        if marker not in memo:
            fail(f"valuation promotion marker missing: {marker}")


def verify_retail_fixed_effect_diagnostic() -> None:
    if not RETAIL_FIXED_EFFECT_DIAGNOSTIC.exists():
        fail(f"missing retail fixed-effect diagnostic: {RETAIL_FIXED_EFFECT_DIAGNOSTIC.relative_to(ROOT)}")
    expected_header = ["unit", "usable_transitions", "within_company_demeaned_correlation", "interpretation", "status", "source_artifact"]
    with RETAIL_FIXED_EFFECT_DIAGNOSTIC.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail fixed-effect diagnostic header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "TJX": (4, 0.210861), "Target": (4, 0.198533),
        "Walmart": (4, 0.152991), "Pooled-company-demeaned": (12, 0.113120),
    }
    if len(rows) != 4 or {row["unit"] for row in rows} != set(expected):
        fail("retail fixed-effect diagnostic unit set changed unexpectedly")
    for row in rows:
        transitions, correlation = expected[row["unit"]]
        if int(row["usable_transitions"]) != transitions or not math.isclose(float(row["within_company_demeaned_correlation"]), correlation, abs_tol=0.000001):
            fail(f"retail fixed-effect diagnostic arithmetic changed: {row['unit']}")
        if row["status"] != "descriptive-only" or not resolve_source(RETAIL_FIXED_EFFECT_DIAGNOSTIC, row["source_artifact"]).exists():
            fail(f"retail fixed-effect diagnostic status/source changed: {row['unit']}")
    memo = (PILOT_DIR / "combined-investment-research-through-cycle-retail-fixed-effect-diagnostic-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("company-demeaned", "0.113120", "not a causal regression", "fixed-effect-descriptive-only"):
        if marker not in memo:
            fail(f"retail fixed-effect diagnostic marker missing: {marker}")


def verify_retail_transition_panel() -> None:
    if not QOE_RETAIL_TRANSITION_PANEL.exists():
        fail(f"missing retail QoE transition panel: {QOE_RETAIL_TRANSITION_PANEL.relative_to(ROOT)}")
    expected_header = [
        "company", "from_fiscal_year", "to_fiscal_year", "receivables_status",
        "inventory_to_revenue_start", "inventory_to_revenue_end", "inventory_to_revenue_change",
        "accounts_payable_to_revenue_start", "accounts_payable_to_revenue_end", "accounts_payable_to_revenue_change",
        "ocf_to_earnings_start", "ocf_to_earnings_end", "ocf_to_earnings_change",
        "cash_after_property_to_earnings_start", "cash_after_property_to_earnings_end", "cash_after_property_to_earnings_change",
        "capex_to_ocf_start", "capex_to_ocf_end", "capex_to_ocf_change",
        "claims_to_ocf_start", "claims_to_ocf_end", "claims_to_ocf_change",
        "sbc_to_earnings_start", "sbc_to_earnings_end", "sbc_to_earnings_change",
        "diagnostic_flags", "follow_up_priority", "status", "source_artifact",
    ]
    with QOE_RETAIL_TRANSITION_PANEL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"retail QoE transition panel header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_keys = {
        ("TJX", "FY2024", "FY2025"), ("TJX", "FY2025", "FY2026"),
        ("Target", "FY2023", "FY2024"), ("Target", "FY2024", "FY2025"),
        ("Walmart", "FY2024", "FY2025"), ("Walmart", "FY2025", "FY2026"),
    }
    if len(rows) != 6 or {(r["company"], r["from_fiscal_year"], r["to_fiscal_year"]) for r in rows} != expected_keys:
        fail("retail QoE transition panel period set changed unexpectedly")
    for row in rows:
        if row["status"] != "diagnostic-only" or row["follow_up_priority"] not in {"medium", "high"}:
            fail(f"retail QoE transition panel status changed: {row['company']} {row['from_fiscal_year']}")
        if not row["diagnostic_flags"].strip() or not resolve_source(QOE_RETAIL_TRANSITION_PANEL, row["source_artifact"]).exists():
            fail(f"retail QoE transition panel flag/source missing: {row['company']} {row['from_fiscal_year']}")
        for field in ("ocf_to_earnings_change", "cash_after_property_to_earnings_change", "capex_to_ocf_change", "claims_to_ocf_change", "sbc_to_earnings_change"):
            if not math.isclose(float(row[field]), float(row[field.replace("_change", "_end")]) - float(row[field.replace("_change", "_start")]), abs_tol=0.000001):
                fail(f"retail QoE transition panel arithmetic changed: {row['company']} {field}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-transition-panel-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("six same-company", "diagnostic-panel-assembled", "composite-score-not-promotable", "not a manipulation finding"):
        if marker not in memo:
            fail(f"retail QoE transition panel marker missing: {marker}")


def verify_capital_flow_qoe_ratio_panel() -> None:
    if not QOE_CAPITAL_FLOW_RATIO_PANEL.exists():
        fail(f"missing capital-flow QoE ratio panel: {QOE_CAPITAL_FLOW_RATIO_PANEL.relative_to(ROOT)}")
    expected_header = [
        "panel_id", "pilot", "period", "metric", "numerator_musd", "denominator_musd",
        "ratio", "denominator_basis", "evidence_status", "diagnostic_flags", "next_join", "source_artifact",
    ]
    with QOE_CAPITAL_FLOW_RATIO_PANEL.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"capital-flow QoE ratio panel header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected = {
        "CFQOE-001": (222.223, 277.563, 0.8009),
        "CFQOE-002": (32.502, 222.223, 0.1463),
        "CFQOE-003": (41.0, 4300.0, 0.0095),
        "CFQOE-004": (12281.981, 12732.699, 0.9646),
        "CFQOE-005": (13601.184, 14010.809, 0.9708),
        "CFQOE-006": (12732.699, 270261.704, 0.0471),
        "CFQOE-007": (779.0, 785.0, 0.9924),
        "CFQOE-008": (54.035, 158.852, 0.3402),
    }
    if len(rows) != len(expected) or {row["panel_id"] for row in rows} != set(expected):
        fail("capital-flow QoE ratio panel row set changed unexpectedly")
    for row in rows:
        numerator, denominator, ratio = expected[row["panel_id"]]
        if not math.isclose(float(row["numerator_musd"]), numerator, abs_tol=0.000001) or not math.isclose(float(row["denominator_musd"]), denominator, abs_tol=0.000001) or not math.isclose(float(row["ratio"]), ratio, abs_tol=0.0001):
            fail(f"capital-flow QoE ratio arithmetic changed: {row['panel_id']}")
        if row["evidence_status"] not in {"qualified", "partial", "allocation-sensitive"} or not row["diagnostic_flags"].strip() or not row["next_join"].strip():
            fail(f"capital-flow QoE ratio boundary changed: {row['panel_id']}")
        if not resolve_source(QOE_CAPITAL_FLOW_RATIO_PANEL, row["source_artifact"]).exists():
            fail(f"capital-flow QoE ratio source missing: {row['panel_id']}")
    memo = (PILOT_DIR / "combined-investment-research-quality-of-earnings-capital-flow-ratio-panel-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("80.09%", "96.46%", "97.08%", "99.24%", "no cross-pilot score", "not owner cash"):
        if marker not in memo:
            fail(f"capital-flow QoE ratio marker missing: {marker}")


def verify_evidence_chain_handoff_matrix() -> None:
    if not EVIDENCE_CHAIN_HANDOFF_MATRIX.exists():
        fail(f"missing evidence-chain handoff matrix: {EVIDENCE_CHAIN_HANDOFF_MATRIX.relative_to(ROOT)}")
    expected_header = [
        "chain_id", "pilot", "force_status", "industry_control_status", "company_selection_status",
        "filing_status", "operating_model_status", "qoe_status", "owner_cash_status", "valuation_status",
        "macro_status", "capital_flow_status", "thesis_breaker_status", "current_bottleneck", "safe_claim", "source_artifact",
    ]
    with EVIDENCE_CHAIN_HANDOFF_MATRIX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            fail(f"evidence-chain handoff header mismatch: {reader.fieldnames}")
        rows = list(reader)
    expected_pilots = {"Retail TJX Target Walmart", "Wheaton Antamina", "Apollo Athene ARI"}
    if len(rows) != 3 or {row["pilot"] for row in rows} != expected_pilots:
        fail("evidence-chain handoff pilot set changed unexpectedly")
    allowed = {"proven", "qualified", "partial", "diagnostic-panel"}
    for row in rows:
        for field in expected_header[2:13]:
            if row[field] not in allowed:
                fail(f"evidence-chain handoff status changed: {row['chain_id']} {field}")
        if not row["current_bottleneck"].strip() or not row["safe_claim"].strip() or not resolve_source(EVIDENCE_CHAIN_HANDOFF_MATRIX, row["source_artifact"]).exists():
            fail(f"evidence-chain handoff row incomplete: {row['chain_id']}")
        if row["owner_cash_status"] != "partial":
            fail(f"evidence-chain owner-cash boundary changed: {row['chain_id']}")
    memo = (PILOT_DIR / "combined-investment-research-evidence-chain-handoff-matrix-2026-09-16.md").read_text(encoding="utf-8")
    for marker in ("force -> industry control point", "diagnostic-panel", "investment-conclusion-not-promoted", "cannot upgrade an upstream gap"):
        if marker not in memo:
            fail(f"evidence-chain handoff marker missing: {marker}")


def verify_industrial_uptime_lane() -> None:
    """Verify the controlled industrial move-on cohort and its proof boundaries."""
    required_memos = [
        PILOT_DIR / "combined-investment-research-industrial-uptime-source-family-handoff-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-industrial-uptime-sterling-project-cash-bridge-pass-1-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-industrial-uptime-sterling-organic-acquisition-backlog-refresh-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-industrial-uptime-wesco-fastenal-owner-cash-burden-bundle-pass-1-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-industrial-uptime-wesco-fastenal-quarterly-persistence-screen-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-industrial-uptime-uri-fleet-lifecycle-bridge-pass-1-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-industrial-uptime-thesis-breaker-register-2026-09-17.md",
    ]
    for path in required_memos:
        if not path.exists():
            fail(f"missing industrial uptime memo: {path.relative_to(ROOT)}")

    with INDUSTRIAL_EVIDENCE.open(newline="", encoding="utf-8") as handle:
        evidence_reader = csv.DictReader(handle)
        expected_evidence_header = [
            "evidence_id", "candidate", "evidence_type", "period", "value",
            "unit", "source_artifact", "interpretation", "status", "next_join",
        ]
        if evidence_reader.fieldnames != expected_evidence_header:
            fail(f"industrial evidence header mismatch: {evidence_reader.fieldnames}")
        evidence_rows = list(evidence_reader)
    evidence_ids = {row["evidence_id"] for row in evidence_rows}
    if len(evidence_rows) < 46 or not {"IUP-001", "IUP-030", "IUP-039", "IUP-043", "IUP-046"}.issubset(evidence_ids):
        fail("industrial evidence register lost its baseline or upstream handoff rows")

    with INDUSTRIAL_PROMOTION_ACTIONS.open(newline="", encoding="utf-8") as handle:
        promotion_reader = csv.DictReader(handle)
        expected_promotion_header = [
            "queue_id", "candidate", "current_status", "current_evidence_artifact",
            "required_source", "time_gate", "join_fields", "promotion_test",
            "blocked_by", "source_artifact",
        ]
        if promotion_reader.fieldnames != expected_promotion_header:
            fail(f"industrial promotion header mismatch: {promotion_reader.fieldnames}")
        promotion_rows = list(promotion_reader)
    if {row["queue_id"] for row in promotion_rows} != {"IUP-WF", "IUP-STRL", "IUP-URI"}:
        fail("industrial promotion register candidate set changed")
    for row in promotion_rows:
        if not row["current_evidence_artifact"].strip() or not row["blocked_by"].strip():
            fail(f"industrial promotion row incomplete: {row['queue_id']}")
        if not any(token in row["promotion_test"].lower() for token in ("cash", "return")):
            fail(f"industrial promotion row lost cash/return test: {row['queue_id']}")

    with INDUSTRIAL_VALUATION.open(newline="", encoding="utf-8") as handle:
        valuation_reader = csv.DictReader(handle)
        valuation_rows = list(valuation_reader)
    if len(valuation_rows) != 12 or {row["candidate"] for row in valuation_rows} != {"WESCO", "Fastenal", "Sterling", "United Rentals"}:
        fail("industrial valuation workbench candidate or scenario set changed")
    if any(row["status"] != "qualified-expectation-screen" for row in valuation_rows):
        fail("industrial valuation workbench promoted a candidate beyond expectation screen")

    with INDUSTRIAL_BREAKERS.open(newline="", encoding="utf-8") as handle:
        breaker_reader = csv.DictReader(handle)
        breaker_rows = list(breaker_reader)
    if len(breaker_rows) != 7 or not all(row["breaker_id"].startswith("TB-IUP-") for row in breaker_rows):
        fail("industrial thesis-breaker register must contain seven TB-IUP rows")
    if any(row["current_status"] != "active-qualified" for row in breaker_rows):
        fail("industrial thesis-breaker row was activated without a joined filing test")

    if not URI_H1_CASH_CLAIM_BRIDGE.exists():
        fail(f"missing URI H1 cash-claim bridge: {URI_H1_CASH_CLAIM_BRIDGE.relative_to(ROOT)}")
    with URI_H1_CASH_CLAIM_BRIDGE.open(newline="", encoding="utf-8") as handle:
        uri_cash_rows = list(csv.DictReader(handle))
    if len(uri_cash_rows) != 9 or uri_cash_rows[0]["amount_usd_millions"] != "3305" or uri_cash_rows[-1]["cumulative_after_item_usd_millions"] != "-356":
        fail("URI H1 cash-claim bridge arithmetic or population changed")
    if any("not allocated" not in row["what_is_not_proven"] for row in uri_cash_rows):
        fail("URI H1 cash-claim bridge boundary changed")
    uri_cash_memo = (PILOT_DIR / "capital-flow-uri-h1-2026-cash-claim-bridge-pass-1.md").read_text(encoding="utf-8")
    for marker in ("Mechanical residual", "(356)", "not normalized owner cash", "URNA"):
        if marker not in uri_cash_memo:
            fail(f"URI H1 cash-claim bridge marker missing: {marker}")

    handoff = (PILOT_DIR / "combined-investment-research-industrial-uptime-source-family-handoff-2026-09-17.md").read_text(encoding="utf-8")
    for marker in ("Social research", "Inc. 5000 discovery", "IBIS / industry map", "Damodaran valuation", "Lyn Alden-style macro/liquidity", "source-family-handoff-complete"):
        if marker not in handoff:
            fail(f"industrial source-family handoff marker missing: {marker}")


def main() -> int:
    verify_research_csv_shapes()
    verify_preserved_primary_artifact_signatures()
    verify_antamina_associate_economics()
    verify_antamina_mine_plan_burden()
    verify_antamina_silver_production_cross_check()
    verify_antamina_bhp_share_conversion()
    verify_wheaton_production_receipt_bridge()
    verify_wheaton_post_q2_search_refresh()
    verify_no_withdrawn_antamina_q4_claims()
    verify_active_packet_coverage()
    verify_market_snapshot_2026_09_16()
    verify_market_snapshot_2026_09_17()
    verify_walmart_call_upgrade()
    verify_target_call_upgrade()
    rows = verify_ledgers()
    verify_apollo_q2_parent_flow_artifact()
    verify_theme_status_map()
    verify_source_family_routes()
    verify_reader_handoff_guides()
    verify_expansion_lane_verifiers()
    verify_expansion_promotion_action_register()
    verify_industrial_uptime_lane()
    verify_macro_historical_regime_panel()
    verify_macro_current_regime_memo()
    verify_macro_longitudinal_retail_bridge()
    verify_ca06_quantified_allocation_surface()
    verify_reader_gate_count(rows)
    verify_workbench()
    verify_antamina_workbench()
    verify_apollo_workbench()
    verify_apollo_primary_source_upgrade()
    verify_wheaton_settlement_boundary_upgrade()
    verify_wheaton_forward_profile_source_control()
    verify_wheaton_teck_reserve_cross_check()
    verify_wheaton_credit_agreement_boundary()
    verify_wheaton_maturity_cliff()
    verify_wheaton_maturity_bullet()
    verify_wheaton_bhp_source_manifest()
    verify_wheaton_bhp_payable_silver()
    verify_wheaton_antamina_source_manifest()
    verify_apollo_q2_parent_receipt_refresh()
    verify_athene_corporate_structure_boundary()
    verify_cross_sector_comparison()
    verify_wheaton_packet_boundary()
    verify_wheaton_first_delivery_boundary()
    verify_wheaton_after_tax_frontier()
    verify_wheaton_reserve_ceiling()
    verify_wheaton_reserve_recovery_frontier()
    verify_wheaton_after_tax_frontier()
    verify_apollo_common_owner_bridge()
    verify_retail_owner_cash_bridge()
    verify_retail_burden_normalization()
    verify_retail_cash_screen()
    verify_retail_support_dependency()
    verify_tjx_temporary_support()
    verify_retail_temporary_support()
    verify_retail_supplier_finance()
    verify_retail_supplier_finance_rollforward()
    verify_retail_supplier_finance_settlement_frontier()
    verify_tjx_q2_cash_capex_boundary()
    verify_uri_q13_next_source_package()
    verify_apollo_ap_grange_next_source_package()
    verify_wheaton_q03_next_source_package()
    verify_apollo_q07_next_source_package()
    verify_insurance_q12_next_source_package()
    verify_apollo_ap_grange_tranche_a_cash_accrual()
    verify_retail_attached_services()
    verify_retail_attached_frontier()
    verify_retail_attached_denominator_reconciliation()
    verify_retail_cohort_matrix()
    verify_retail_common_period_cash()
    verify_retail_cohort_working_capital()
    verify_retail_margin_working_capital()
    verify_retail_margin_support_transition()
    verify_retail_capex_classification()
    verify_retail_promotion_action_register()
    verify_tjx_maintenance_expense_boundary()
    verify_retail_capex_boundary_overlay()
    verify_retail_post_financing_residual()
    verify_walmart_cash_denominator()
    verify_target_cash_denominator()
    verify_target_gift_card_boundary()
    verify_retail_cohort_cash_denominator()
    verify_retail_per_share_cash()
    verify_retail_stacked_residual_per_share()
    verify_retail_annual_lease_tax_cash()
    verify_retail_annual_cohort_denominator()
    verify_retail_annual_attached_frontier()
    verify_retail_annual_expectation_screen()
    verify_retail_interim_lease_tax_search()
    verify_retail_interim_inline_xbrl_search()
    verify_quality_of_earnings_overlay()
    verify_retail_qoe_cash_conversion()
    verify_current_retail_earnings_cash_screen()
    verify_current_retail_composite_input_panel()
    verify_current_retail_diagnostic_ratio_panel()
    verify_tjx_historical_qoe_vector()
    verify_target_historical_qoe_vector()
    verify_walmart_historical_qoe_vector()
    verify_retail_qoe_comparability_bridge()
    verify_retail_qoe_trend_diagnostics()
    verify_ca06_promotion_matrix()
    verify_valuation_promotion_matrix()
    verify_retail_fixed_effect_diagnostic()
    verify_retail_transition_panel()
    verify_capital_flow_qoe_ratio_panel()
    verify_evidence_chain_handoff_matrix()
    verify_apollo_debt_solutions_coupon_carry()
    verify_apollo_debt_solutions_issuer_bridge()
    verify_apollo_debt_solutions_payment_boundary()
    verify_apollo_related_party_bridge()
    verify_apollo_fee_rollforward()
    verify_apollo_named_asset_routes()
    verify_apollo_statutory_named_asset_return_boundary()
    verify_apollo_ari_seller_cash()
    verify_apollo_ari_cash_reconciliation()
    verify_apollo_ari_transaction_terms()
    verify_apollo_ari_payment_mechanics()
    verify_apollo_ari_post_close_search()
    verify_apollo_private_credit_public_search()
    verify_apollo_mf1_remittance_access()
    verify_apollo_mf1_servicing_waterfall_boundary()
    verify_causal_test_protocol()
    verify_retail_panel_diagnostic()
    verify_retail_within_company_diagnostic()
    verify_retail_lagged_diagnostic()
    verify_apollo_ari_cash_delta()
    verify_apollo_ari_aum_outflow()
    verify_apollo_ari_perimeter_reconciliation()
    verify_apollo_ari_liquidation_distribution()
    verify_apollo_named_asset_ledger_gates()
    verify_apollo_ba_lot_bridge()
    verify_apollo_ba_income_queue()
    verify_apollo_q2_amaps_source()
    verify_apollo_2026_credit_agreement_purpose()
    verify_apollo_intercompany_note_longitudinal()
    verify_apollo_mf1_gross_proceeds_screen()
    verify_apollo_mf1_same_cusip_join()
    verify_apollo_mf1_remittance_access()
    verify_concord_source_acquisition_boundary()
    verify_concord_sec_nport_observation()
    verify_apollo_related_party_ledger_gates()
    verify_apollo_receipt_frontier()
    verify_apollo_q2_receipt_frontier()
    verify_apollo_q2_parent_receipt_script()
    verify_apollo_supplement_boundary()
    verify_apollo_liquidity_boundary()
    verify_apollo_holdco_summary_context()
    verify_apollo_company_distribution_route()
    verify_apollo_credit_quality_boundary()
    verify_thesis_breaker_register()
    verify_return_input_schemas()
    verify_reader_decision_layer()
    verify_completion_audit()
    verify_cash_denominator_reconciliation()
    verify_owner_cash_promotion_matrix()
    verify_method_registry()
    verify_investments_repository_bridge()
    verify_investments_article_handoff()
    verify_social_research_bridge()
    verify_ibis_industry_handoff()
    verify_inc5000_discovery_bridge()
    verify_macro_liquidity_matrix()
    verify_macro_liquidity_stress_screen()
    verify_retail_capex_sensitivity()
    verify_retail_capex_public_refresh()
    verify_retail_attached_services_public_refresh()
    verify_next_evidence_queue()
    verify_fpl_billing_receipt_chase()
    verify_fpl_distribution_inspection_refresh()
    verify_duke_anderson_cost_sensitivity()
    verify_duke_anderson_approval_boundary()
    verify_uri_borrowing_base_chase()
    verify_uri_abl_proxy_bridge()
    verify_wheaton_financing_cash_flow()
    verify_expansion_lane_qoe_overlay()
    for required in (
        PILOT_DIR / "combined-investment-research-meaty-end-to-end-goal.md",
        PILOT_DIR / "combined-investment-research-pilot-01-wheaton-antamina.md",
        PILOT_DIR / "combined-investment-research-pilot-02-affordability-value.md",
        PILOT_DIR / "combined-investment-research-pilot-03-apollo-athene.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.md",
        PILOT_DIR / "capital-flow-apollo-athene-q07-common-owner-input-schema-2026-09-16.md",
        PILOT_DIR / "capital-flow-retail-owner-cash-input-schema-2026-09-16.md",
        PILOT_DIR / "capital-flow-apollo-athene-corporate-structure-presentation-boundary-2026-09-16.md",
        PILOT_DIR / "data/capital-flow-apollo-athene-corporate-structure-presentation-boundary-2026-09-16.csv",
        PILOT_DIR / "data/capital-flow-apollo-athene-corporate-structure-presentation-summary-2026-09-16.html",
        PILOT_DIR / "capital-flow-apollo-athene-fee-rollforward-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-mf1-servicing-waterfall-mechanics-boundary-2026-09-17.md",
        LEDGER_DIR / "capital-flow-apollo-athene-mf1-servicing-waterfall-mechanics-boundary-2026-09-17.csv",
        PILOT_DIR / "combined-investment-research-current-synthesis.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-financial-shenanigans-overlay-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-forensic-methods-map-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-cash-conversion-screen-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-composite-input-schema-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-current-retail-earnings-cash-screen-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-current-retail-composite-input-panel-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-current-retail-diagnostic-ratio-panel-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-tjx-historical-vector-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-target-historical-vector-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-walmart-historical-vector-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-comparability-bridge-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-trend-diagnostics-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-ca06-promotion-matrix-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-valuation-promotion-matrix-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-through-cycle-retail-fixed-effect-diagnostic-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-retail-transition-panel-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-quality-of-earnings-capital-flow-ratio-panel-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-evidence-chain-handoff-matrix-2026-09-16.md",
        QOE_OVERLAY,
        QOE_RETAIL_CASH_CONVERSION,
        QOE_COMPOSITE_SCHEMA,
        QOE_CURRENT_RETAIL_EARNINGS_CASH,
        QOE_CURRENT_RETAIL_COMPOSITE_PANEL,
        LEDGER_DIR / "combined-investment-research-quality-of-earnings-current-retail-diagnostic-ratio-panel-2026-09-16.csv",
        LEDGER_DIR / "combined-investment-research-quality-of-earnings-tjx-historical-vector-2026-09-16.csv",
        LEDGER_DIR / "combined-investment-research-quality-of-earnings-target-historical-vector-2026-09-16.csv",
        LEDGER_DIR / "combined-investment-research-quality-of-earnings-walmart-historical-vector-2026-09-16.csv",
        QOE_RETAIL_COMPARABILITY,
        QOE_RETAIL_TREND_DIAGNOSTICS,
        CA06_PROMOTION_MATRIX,
        VALUATION_PROMOTION_MATRIX,
        RETAIL_FIXED_EFFECT_DIAGNOSTIC,
        QOE_RETAIL_TRANSITION_PANEL,
        QOE_CAPITAL_FLOW_RATIO_PANEL,
        QOE_RETAIL_COMPONENT_SCREEN,
        EVIDENCE_CHAIN_HANDOFF_MATRIX,
        PILOT_DIR / "combined-investment-research-cross-sector-comparison-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-macro-historical-regime-validation-2026-09-15.md",
        MACRO_CURRENT_REGIME_MEMO,
        REVIEWERS_GUIDE,
        NEXT_CYCLE_EXPANSION,
        ROOT / "scripts" / "verify-power-grid-expansion-lane.py",
        ROOT / "scripts" / "verify-insurance-statutory-expansion-lane.py",
        ROOT / "scripts" / "verify-asset-backed-expansion-lane.py",
        PILOT_DIR / "combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.md",
        PILOT_DIR / "combined-investment-research-market-snapshot-2026-09-15.md",
        PILOT_DIR / "combined-investment-research-market-snapshot-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-market-snapshot-2026-09-17.md",
        MARKET_SNAPSHOT_2026_09_16,
        MARKET_SNAPSHOT_2026_09_17,
        PILOT_DIR / "combined-investment-research-pilot-02-retail-owner-cash-bridge.md",
        PILOT_DIR / "combined-investment-research-pilot-02-target-q2-management-call-control-point-upgrade-2026-09-15.md",
        PILOT_DIR / "combined-investment-research-pilot-02-target-gift-card-liability-boundary-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-burden-normalization.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-normalized-cash-screen.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-per-share-cash.md",
        PILOT_DIR / "combined-investment-research-pilot-02-tjx-h1-temporary-support.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-temporary-support.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-supplier-finance-boundary.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-attached-services-boundary.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-attached-services-cash-frontier-2026-09-15.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-cohort-operating-matrix.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-common-period-cash-matrix.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-margin-working-capital-normalization.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-capex-classification.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-capex-allocation-sensitivity.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-capex-public-source-refresh-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-attached-services-public-source-refresh-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-cohort-denominator-control-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-attached-services-cash-frontier-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-annual-reported-cash-expectation-screen-2026-09-17.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-cash-quality-support-dependency-2026-09-15.md",
        PILOT_DIR / "combined-investment-research-pilot-02-retail-cohort-inventory-payable-balance-screen-2026-09-15.md",
        PILOT_DIR / "combined-investment-research-pilot-02-tjx-forward-capex-category-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-bhp-fy2026-settlement-boundary-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-bhp-fy2026-payable-silver-quantity-boundary-2026-09-16.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-local-packet-settlement-search-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-term-maturity-bullet-coverage-screen-2026-09-16.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-q2-2026-delivery-boundary-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-bhp-contract-denominator-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-production-profile-boundary-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-q2-incremental-production-proxy-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-q2-first-delivery-receipt-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-company-burden-boundary-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-after-tax-financed-allocation-frontier-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-reserve-constrained-delivery-ceiling-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-reserve-capped-upfront-recovery-frontier-2026-09-15.md",
        WHEATON_RESERVE_RECOVERY_FRONTIER,
        PILOT_DIR / "capital-flow-wheaton-antamina-teck-reserve-cross-check-2026-09-16.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-after-tax-financed-allocation-frontier-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-financing-terms-boundary-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-wheaton-antamina-financing-cash-flow-upgrade-2026-09-15.md",
        WHEATON_FINANCING_CASH_FLOW,
        PILOT_DIR / "combined-investment-research-pilot-03-apollo-related-party-return-bridge.md",
        PILOT_DIR / "capital-flow-apollo-parent-cash-use-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-upstream-receipt-source-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-upstream-dividend-boundary-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.md",
        PILOT_DIR / "capital-flow-apollo-athene-ari-portfolio-sale-cash-use-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-ari-q2-seller-cash-debt-waterfall-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-ari-q2-cash-flow-reconciliation-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-statutory-safe-cashlike-column-review-pass-1.md",
        APOLLO_STATUTORY_NAMED_ASSET_MAP,
        PILOT_DIR / "capital-flow-apollo-athene-related-party-fee-transfer-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-credit-quality-return-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-parent-liquidity-source-route-upgrade-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-parent-receipt-attribution-frontier-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-q2-parent-receipt-attribution-frontier-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-q2-parent-receipt-refresh-2026-09-16.md",
        PILOT_DIR / "capital-flow-apollo-athene-2026-credit-agreement-purpose-perimeter-2026-09-17.md",
        APOLLO_2026_CREDIT_AGREEMENT_PURPOSE,
        PILOT_DIR / "capital-flow-apollo-athene-intercompany-note-longitudinal-refresh-2026-09-16.md",
        APOLLO_INTERCOMPANY_NOTE_LONGITUDINAL,
        PILOT_DIR / "capital-flow-apollo-athene-mf1-gross-proceeds-income-denominator-screen-2026-09-17.md",
        APOLLO_MF1_GROSS_PROCEEDS_SCREEN,
        PILOT_DIR / "capital-flow-apollo-athene-mf1-same-cusip-servicing-join-boundary-2026-09-17.md",
        APOLLO_MF1_SAME_CUSIP_JOIN,
        PILOT_DIR / "capital-flow-apollo-athene-mf1-remittance-access-boundary-2026-09-16.md",
        APOLLO_MF1_REMITTANCE_ACCESS,
        PILOT_DIR / "capital-flow-apollo-athene-q2-policyholder-liquidity-repo-burden-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-athene-apollo-debt-solutions-payment-observability-boundary-2026-09-16.md",
        PILOT_DIR / "capital-flow-fpl-sppcrc-historical-recovery-boundary-2026-09-16.md",
        FPL_HISTORICAL_RECOVERY_BOUNDARY,
        PILOT_DIR / "capital-flow-fpl-2026-sppcrc-rate-class-factor-boundary-2026-09-16.md",
        FPL_RATE_CLASS_FACTORS,
        PILOT_DIR / "capital-flow-fpl-sppcrc-rate-class-determinant-boundary-2026-09-16.md",
        FPL_RATE_CLASS_DETERMINANTS,
        PILOT_DIR / "capital-flow-fpl-billing-determinant-category-receipt-proof-chase-pass-1.md",
        FPL_BILLING_RECEIPT_CHASE,
        FPL_DISTRIBUTION_INSPECTION_REFRESH,
        PILOT_DIR / "capital-flow-uri-abl-borrowing-base-reporting-regime-boundary-2026-09-16.md",
        URI_REPORTING_REGIME_BOUNDARY,
        PILOT_DIR / "combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.md",
        EXPANSION_LANE_QOE_OVERLAY,
        PILOT_DIR / "capital-flow-duke-anderson-project-cost-attribution-sensitivity-2026-09-17.md",
        DUKE_ANDERSON_COST_SENSITIVITY,
        PILOT_DIR / "capital-flow-duke-anderson-county-generation-approval-recovery-boundary-2026-09-16.md",
        DUKE_ANDERSON_APPROVAL_BOUNDARY,
        PILOT_DIR / "capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md",
        URI_BORROWING_BASE_CHASE,
        PILOT_DIR / "capital-flow-uri-abl-public-disclosure-proxy-bridge-pass-1.md",
        URI_ABL_PROXY_BRIDGE,
        PILOT_DIR / "capital-flow-apollo-q2-fund-distributions-to-company-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-q2-financial-supplement-parent-receipt-search-boundary-2026-09-15.md",
        PILOT_DIR / "capital-flow-apollo-q2-xbrl-parent-receipt-boundary-2026-09-15.md",
        ROOT / "raw/primary-sources/capital-flow/apollo/q2-2026/apollo-broadcom-ai-xpv-platform-release.html",
        ROOT / "raw/primary-sources/capital-flow/apollo/q2-2026/apollo-2026-q2-10q.pdf",
        ROOT / "scripts" / "check-apollo-q2-parent-receipt-boundary.py",
        ROOT / "scripts" / "check-apollo-q2-financial-supplement-boundary.py",
        PILOT_DIR / "capital-flow-apollo-athene-investment-spread-screen-upgrade-2026-09-15.md",
        PILOT_DIR / "combined-investment-research-thesis-breaker-register.md",
        PILOT_DIR / "combined-investment-research-completion-audit.md",
        PILOT_DIR / "combined-investment-research-method-registry.md",
        MACRO_LIQUIDITY_MATRIX,
        PILOT_DIR / "combined-investment-research-macro-liquidity-stress-screen.md",
        PILOT_DIR / "combined-investment-research-macro-liquidity-current-anchor-2026-09-15.md",
        PILOT_DIR / "data/combined-investment-research-macro-liquidity-current-anchor-2026-09-15.csv",
        PILOT_DIR / "combined-investment-research-next-evidence-queue.md",
        PILOT_DIR / "combined-investment-research-pilot-03-apollo-named-asset-return-routes.md",
        ROOT / "raw/primary-sources/capital-flow/bhp/fy2026/bhp-fy2026-20f.htm",
        ROOT / "raw/primary-sources/capital-flow/wheaton/2026-09-16/wheaton-investor-day-corporate-presentation-september-2026.pdf",
    ):
        if not required.exists():
            fail(f"missing required goal artifact: {required.relative_to(ROOT)}")
    print(
        f"Combined investment pilot verification passed: {len(PILOT_LEDGERS)} ledgers, "
        f"{rows} evidence gates, valuation workbenches checked, "
        "three expansion-lane verifiers and industrial uptime lane checked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
