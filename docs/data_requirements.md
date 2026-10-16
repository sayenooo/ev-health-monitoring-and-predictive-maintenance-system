# Data Requirements — HealthCar
**Document ID:** HC-DAT-001 · **Version:** 2.0 · **Baseline:** 2026-10-16

## Monitoring track (current sensor state)
Required records: `timestamp`, source/vehicle identifier where available, sensor values, units, operating mode, quality flags. Each new observation is incorporated into a rolling time-series window.

SCUT publisher-documented fields: `Time`, `vhc_speed`, `charging_signal`, `vhc_totalMile`, `hv_voltage`, `hv_current`, `bcell_soc`, `bcell_maxVoltage`, `bcell_minVoltage`, `bcell_maxTemp`, `bcell_minTemp`. Verify actual encodings/units/time gaps before modeling. Derive `cell_voltage_spread_V`, `cell_temperature_spread_C`, and a signed electrical-power proxy only after checking current conventions.

## Predictive maintenance track (future target)
Required:
- Identifiers grouping all observations for each source vehicle.
- Chronological historical sensor readings and observation cutoffs.
- Verified later fault event or a defensible at-risk label tied to prior history.
- Label semantics, component type and date of verification when available.
- Enough fault-positive and reference vehicles for independent validation.

Candidate data: Zhang et al. historical real-EV charging/fault corpus. Actual raw field names and event chronology are **not yet audited**. A fixed horizon such as `fault_within_7_days` may not be defined unless event timestamps support it.

## Feature families
Rolling means/medians, maxima/minima, spreads, slopes, rates of change, variability, charging context and coverage, to the extent supported by each instrument. Features must use only current/past data, never future measurements.

## Quality and split requirements
- Source file inventory, provenance and checksums.
- Nulls, non-finite values, implausible readings, duplicates and sample gaps.
- Operating-mode semantics, sensor unit verification and missing-channel handling.
- Vehicle-disjoint and time-aware train/validation/test.
- Imbalance analysis and baseline comparison.

## Component scope
The system concept covers vehicle-wide EV health. A module is only claimed to be empirically validated if its relevant sensor inputs and fault events are available. Uninstrumented components are reported as unavailable rather than inferred without evidence.
