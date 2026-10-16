# Progress Tracker — HealthCar
**Document ID:** HC-TR-001 · **Version:** 2.0 · **Updated:** 2026-10-16

| ID | Milestone | Status | Evidence / next action |
|---|---|---|---|
| M1 | Ideation & Project Planning | **COMPLETE** | Final project charter v2.0 and project plan v2.0 |
| M2 | Data Source & Target Feasibility | **IN PROGRESS** | SCUT/PMSM locally downloaded; future-fault source must be audited |
| M3 | EDA & Time-Series Preprocessing | NOT STARTED | — |
| M4 | Continuous Monitoring Model | NOT STARTED | — |
| M5 | Predictive Maintenance Model | NOT STARTED | — |
| M6 | Joint Evaluation & Early-Warning Demo | NOT STARTED | — |
| M7 | BDAPP Final Report & Presentation | NOT STARTED | — |

## M1 — COMPLETE (2026-10-16)
- [x] One permanent project title and ML research objective.
- [x] Continuous EV monitoring specified as required.
- [x] Current anomaly/fault detection specified as required.
- [x] Future fault-risk prediction specified as required, contingent on ground-truth evidence.
- [x] Early warning and explanation included.
- [x] BDAPP model-centric deliverables, requirements and evaluation defined.
- [x] Offline telemetry replay selected as initial demonstration.
- [x] Clear separation of scope, verified results and data limitations.

## M2 — CURRENT
- [x] Official SCUT and PMSM sources selected for monitoring / supporting diagnostics.
- [x] SCUT and PMSM source archives downloaded on user's Windows computer.
- [x] Preliminary selected-table audits run: 81,898 SCUT rows, 10,892 PMSM rows; these are not verified dataset-wide totals.
- [ ] Inventory source files and correct the SCUT selected-table total discrepancy.
- [ ] Record sensor columns, units, timestamps, missing/non-finite values and operating codes.
- [ ] Download/inspect real-EV fault histories, vehicle IDs and labels.
- [ ] Verify that labels represent subsequent outcomes relative to the observation windows.
- [ ] Freeze per-track prediction target, data split and feasible lead-time measures.

## M3 — PENDING
- [ ] EDA and time-series window design for both required tracks.
- [ ] Train/validation/test splits with time/group leakage protection.
- [ ] Documented preprocessing and feature dictionary.

## M4 — PENDING
- [ ] Context-aware monitoring baseline.
- [ ] Monitoring anomaly model.
- [ ] Repeated chronological inference, alert stability and false alert assessment.

## M5 — PENDING
- [ ] Prospective fault target and naive risk baseline.
- [ ] At least two valid predictive model approaches.
- [ ] Independent predictive evaluation and feature interpretation.

## M6 — PENDING
- [ ] Demonstrate sequential replay with updated health and future-risk outputs.
- [ ] Explain alerts, uncertainty, missed events and false alarms.
- [ ] Integrate validated results in a reproducible notebook or modest demo.

## M7 — PENDING
- [ ] Final figures, tables, BDAPP report and presentation.
- [ ] Clean reproducibility instructions and code.
- [ ] Report demonstrated scope separately from longer-term EV component vision.

## Evidence log
| Date | Observation |
|---|---|
| 2026-10-16 | Project concept confirmed: continuous EV health monitoring + anomaly detection + future fault-risk prediction + early warnings |
| 2026-10-16 | Existing source acquisition logs confirm SCUT and PMSM downloads and preliminary source-table audits; predictive future-fault source not yet inspected |
