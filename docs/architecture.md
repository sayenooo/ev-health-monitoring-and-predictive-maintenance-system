# System Architecture — HealthCar
**Document ID:** HC-ARC-001 · **Version:** 1.0 · **Baseline:** 2026-10-16

## Architectural principles
1. Read-only, offline-first and reproducible.
2. Separate raw telemetry, feature pipelines, modeling and human-facing explanations.
3. Keep the source/evaluation boundary between SCUT real EV telemetry and PMSM laboratory fault data.
4. Prefer interpretable baselines; use more complex models only when clearly justified.
5. Fail visibly for missing/invalid signals; do not invent unavailable measurements.

## Logical flow

```text
Publisher CSV/ZIP sources
       |
       v
[Acquisition & provenance] --> data/raw/ (local only)
       |
       v
[Schema / timestamp / quality validation] --> data/reports/
       |
       v
[Context-aware preprocessing + features] --> data/processed/
       |
       +---------- SCUT track ---------+
       |                               |
       v                               v
[EV monitoring baseline]        [Exploratory anomaly model]
       |                               |
       +---------------+---------------+
                       |
                       v
             [Alert evidence interface]
                       |
                       v
           [Read-only HealthCar dashboard]

Separately:
PMSM lab files --> lab-data validation --> lab classifier --> lab-only model report

Optional later:
Labeled real EV histories --> label/horizon audit --> future-risk experiment
```

## Responsibility boundaries
| Component | Responsibility | Initial implementation |
|---|---|---|
| Dataset downloader | Publisher retrieval, archive verification, extraction | `scripts/download_data.py` |
| Data audit | Table discovery, quality reports, conservative derived signals | `src/healthcar/audit.py` |
| Dataset notebooks | Inspection and interpretation; no production logic | `notebooks/01_scut_data_audit.ipynb` and `02_pmsm_data_audit.ipynb` |
| Preprocessing package | Future: validated transformations and split manifests | P3 |
| Monitoring models | Future: contextual baselines, model artifacts and evaluation | P4 |
| PMSM classifier | Future: labeled laboratory classification | P5 |
| Application layer | Future: telemetry replay and read-only dashboard | P6 |
| Future-risk research | Conditional separate validation and integration | P7 |

## Proposed interface contracts (for later implementation)
**Telemetry observation:** `source_id`, `vehicle_id` (if provided), `timestamp`, `signal_name`, `value`, `unit`, `data_quality`, `operating_mode`.

**Model alert:** `alert_id`, `timestamp`, `component`, `alert_type`, `evidence`, `score`, `confidence_status`, `data_source`, `model_version`, `recommendation`.

These are **design contracts**, not claims of implemented endpoints.

## Storage and access
- `data/raw/`: official archives and extracted source data; Git-ignored.
- `data/processed/`: derived datasets; Git-ignored.
- `data/reports/`: local audit/EDA outputs; Git-ignored.
- Commit Python code, Markdown docs, notebooks without private source data and tests.

## Future integration
Live OBD-II or an OEM-compatible API may be added only after vehicle-specific signal availability and protocol permissions are verified. The MVP uses offline telemetry replay.
