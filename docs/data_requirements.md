# Prediction Data Requirements — HealthCar
**Document ID:** HC-DAT-001 · **Version:** 1.1 · **Baseline:** 2026-10-16

## Primary dataset (Zhang et al. 2023)
**Source:** https://doi.org/10.6084/m9.figshare.23659323

Required metadata:
- `vehicle_id` (or equivalent consistent per-vehicle grouping), identifying independent evaluation units.
- A validated vehicle-level fault label; fault types/notes where actually available.
- Chronological sequence/index for earlier charging snippets.
- Recorded available electrical/thermal signals (paper describes current, voltage and temperature histories).
- Event/verification timestamp *if present*; otherwise a fixed-day horizon is not measurable.
- Per-record/session source information and author data transformation notes.

The original column names and label encoding are **not yet verified**; generic names above describe modeling requirements rather than claiming they are dataset columns.

## Derived ML features (after source inspection)
- Statistical summaries of voltage, current, temperature.
- Trends, range/spread, rates and rolling features over valid historical windows.
- Charging-session frequency, coverage and duration, if recorded.
- Time-aware aggregates at vehicle level.
- Missingness and measurement-coverage indicators where informative and non-leaky.

## Ground-truth and leakage requirements
- A target `y` must be grounded in the publisher's verified labels, never manufactured from rule thresholds.
- Same-vehicle snippets must not appear in train and test.
- No use of diagnostic observations taken at or after a target event.
- Do not fit preprocessing on held-out vehicles or all timestamps together.
- Label grouping and temporal windows should be frozen before final model comparison.

## Supporting datasets
- **SCUT:** source variables include `Time`, `vhc_speed`, `charging_signal`, `vhc_totalMile`, `hv_voltage`, `hv_current`, `bcell_soc`, `bcell_maxVoltage`, `bcell_minVoltage`, `bcell_maxTemp`, `bcell_minTemp`. Useful for supporting analysis only.
- **PMSM:** inverter rig inputs `Ia`, `Ib`, `VDC`, `IDC`, `T1`, `T2`, `T3`, `VD`, `FDD` where confirmed; optional separate fault diagnosis.

## Data governance
Record publisher/source DOI, usage terms, versions/hashes, train/validation/test group IDs and measured sample counts. Large primary archives remain Git-ignored.
