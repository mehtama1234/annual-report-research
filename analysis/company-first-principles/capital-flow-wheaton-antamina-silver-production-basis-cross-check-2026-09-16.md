# Antamina silver-production basis cross-check

Research date: `2026-09-16`

Two official-source routes now provide useful but non-identical silver
observations:

| Observation | Basis | Value | Safe use |
| --- | --- | ---: | --- |
| Antamina Sustainability Report 2023 | Operator metallic silver production, dry metric tonnes | `360 t` actual versus `352 t` budget | Historical operator production point; the report does not identify BHP/Wheaton entitlement or settlement |
| Antamina Sustainability Report 2024 | Operator metallic silver production, dry metric tonnes | `0.35 Kt` actual versus `0.31 Kt` budget | Historical operator production point; the report does not identify BHP/Wheaton entitlement or settlement |
| BHP SEC Form 6-K, February 17, 2026 | Antamina silver produced in calendar 2025 on a BHP-share basis | `5.4 Moz` | BHP-share historical production proxy; not a metal-credit invoice, payable-ounce schedule, or receipt |

The observations are not forced into one series. The 2023 Antamina table reports
metric tonnes, the 2024 table reports dry kilotonnes, and BHP's 2025 statement
uses million troy ounces and explicitly describes a BHP-share basis. The
operator report also displays a `0.4` Kt difference in the table; because that
does not reconcile cleanly to the displayed actual and budget values or the
13% variance, the table's difference cell is preserved as reported and not
used in a calculated curve.

This cross-check improves the historical production denominator and confirms
that a BHP-share observation exists. It still does not provide annual BHP-only
payable silver through the `100M`-ounce threshold, smelter weights/assays,
Wheaton metal-credit quantity, invoice, settlement date, or cash receipt.

Sources: [Antamina Sustainability Report 2023](https://www.antamina.com/wp-content/uploads/2024/10/sustainability-report-antamina-2023.pdf), [Antamina Sustainability Report 2024](https://www.antamina.com/wp-content/uploads/2025/11/sustainability-report-antamina-2024.pdf), and [BHP SEC Form 6-K](https://www.sec.gov/Archives/edgar/data/811809/000119312526052837/d29257d6k.htm).

Structured control: [Antamina silver-production basis CSV](data/capital-flow-wheaton-antamina-silver-production-basis-cross-check-2026-09-16.csv) and [Wheaton–Antamina source manifest](data/capital-flow-wheaton-antamina-source-manifest-2026-09-16.csv).
