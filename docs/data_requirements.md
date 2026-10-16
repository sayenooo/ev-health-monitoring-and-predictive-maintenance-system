# Data Requirements & Sensor Dictionary

## SCUT passenger EV telemetry
Published schema (to be confirmed against downloaded archives):

| Field | Meaning | Intended use |
|---|---|---|
| `Time` | timestamp | temporal ordering, sampling gaps |
| `vhc_speed` | vehicle speed (km/h) | driving context |
| `charging_signal` | source codes 1=charging, 3=driving | mode-specific analysis; other codes require verification |
| `vhc_totalMile` | accumulated mileage (km) | exposure/usage context |
| `hv_voltage` | pack voltage | electric-state monitoring |
| `hv_current` | pack current | current and tentative power trends |
| `bcell_soc` | battery SOC | charge-level context; verify units |
| `bcell_maxVoltage` | maximum cell voltage | spread proxy |
| `bcell_minVoltage` | minimum cell voltage | spread proxy |
| `bcell_maxTemp` | maximum cell temperature | thermal monitoring |
| `bcell_minTemp` | minimum cell temperature | thermal monitoring |

### Derived fields (after unit checks)
- `cell_voltage_spread_V = bcell_maxVoltage - bcell_minVoltage`
- `cell_temperature_spread_C = bcell_maxTemp - bcell_minTemp`
- `battery_power_W_unverified_sign = hv_voltage * hv_current`
- Later: operating-mode-aware rolling trends and rates, after handling irregular timestamps.

**Not supported by SCUT alone:** validated battery SOH, RUL, motor condition, brake/tire wear, coolant-pump faults, actual future failure dates.

## PMSM inverter laboratory dataset
Expected original sensor columns (case may vary): `Ia`, `Ib`, `VDC`, `IDC`, `T1`, `T2`, `T3`, `VD`; fault target `FDD` with F0 normal and F1–F8 experimental faults. Verify the actual columns, target mapping, units and repeated sessions before model building. Derived features require label-leakage inspection.

## Data quality gates
- Timestamp parse and ordering; gaps and duplicate times.
- Null percentages, infinities, plausible physical values and units.
- Correct vehicle selection: exclude SCUT buses from the passenger-EV MVP.
- Operating codes and current sign conventions.
- Different sampling rates and battery chemistries per SCUT vehicle.
- PMSM class counts, experiments/session boundaries, possible correlated rows.
- Provenance, source references and redistribution/license constraints.
