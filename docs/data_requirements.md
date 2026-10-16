# Data Requirements and Sensor Dictionary
**Document ID:** HC-DAT-001 · **Version:** 1.0 · **Baseline:** 2026-10-16

## SCUT passenger EV source schema
The following field definitions are from the [SCUT publisher's documentation](https://github.com/Translab-SCUT/Electric-vehicle-operation-data); the empirical archive-level validation belongs to M2.

| Source field | Intended meaning | Unit / interpretation | Monitoring use |
|---|---|---|---|
| `Time` | Acquisition timestamp | Verify parsed timezone and interval | Trend/order/gaps |
| `vhc_speed` | Vehicle speed | km/h | Operating condition |
| `charging_signal` | Source mode indicator | 1 = charging; 3 = driving | Context segmentation |
| `vhc_totalMile` | Cumulative distance | km | Usage exposure |
| `hv_voltage` | Battery pack voltage | V | Electrical signal |
| `hv_current` | Battery pack current | A; sign to verify | Electrical signal |
| `bcell_soc` | Battery state of charge | Scale/range to verify | Charge context |
| `bcell_maxVoltage` | Highest cell voltage | V | Voltage variation |
| `bcell_minVoltage` | Lowest cell voltage | V | Voltage variation |
| `bcell_maxTemp` | Highest cell temperature | °C | Thermal variation |
| `bcell_minTemp` | Lowest cell temperature | °C | Thermal variation |

## Conservative derived indicators
- `cell_voltage_spread_V = bcell_maxVoltage - bcell_minVoltage`
- `cell_temperature_spread_C = bcell_maxTemp - bcell_minTemp`
- `battery_power_W_unverified_sign = hv_voltage * hv_current`
- Mode-conditioned, time-aware rolling medians and slopes **after** irregular timestamps are resolved.

These are monitoring descriptors, not validated battery damage thresholds or SOH estimators.

## PMSM experimental source schema
Zenodo's 3.0 archive is expected to provide eight core measured inputs such as phase currents (`Ia`, `Ib`), DC-bus voltage/current (`VDC`, `IDC`), half-bridge temperatures (`T1`–`T3`) and gate-driver voltage (`VD`); class label `FDD` may be present in processed data. **Exact file-level spellings, meanings, labels and units must be verified from downloaded metadata.** Derived features need target leakage checks.

## Data acceptance requirements
1. Preserve originals, metadata and extraction source; compute/check archive checksums where possible.
2. Document missing and infinite values before transforming them.
3. Parse and sort time correctly; flag repeated timestamps and long gaps.
4. Preserve operating-mode codes and mark unrecognized values as unknown.
5. Document source-specific labels and their unit of prediction (sample, experiment or vehicle).
6. Avoid mixing data from different battery chemistries without explicit context.
7. Keep unrelated component fields as `unavailable` rather than imputing them.

## Boundaries
These inputs alone do not establish verified battery SOH, RUL, future failure times, motor condition on public roads, tire/brake wear or coolant system faults.
