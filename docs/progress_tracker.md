# HealthCar — Progress Tracker
**Tracker ID:** HC-TR-001  
**As of:** 2026-10-16  
**Source of truth:** this file on `main`. Update evidence and date before checking a box.

## Milestone status
| ID | Milestone | Status | Evidence |
|---|---|---|---|
| M1 | Project ideation and planning | **COMPLETE** | `project_charter.md`, `project_plan.md`, requirements, architecture |
| M2 | Dataset inventory and quality gate | IN PROGRESS | Local downloads + preliminary audit; detailed inspection pending |
| M3 | Preprocessing and EDA | NOT STARTED | — |
| M4 | EV monitoring baseline | NOT STARTED | — |
| M5 | PMSM lab fault classification | NOT STARTED | — |
| M6 | End-to-end application | NOT STARTED | — |
| M7 | Labeled real-EV predictive research | CONDITIONAL | Go/no-go decision pending |

## M1 — Complete · 2026-10-16
- [x] Problem statement, audience and overall goal approved.
- [x] Research questions, objectives and MVP boundaries finalized.
- [x] Functional and nonfunctional requirements established.
- [x] System architecture and data strategy established.
- [x] Evaluation principles and success criteria established.
- [x] Milestones, dependencies and principal risks documented.

## M2 — Current work
- [x] Python environment and dependencies installed locally (Windows console log, 2026-10-16).
- [x] SCUT #1 and PMSM archives downloaded locally (Windows console log, 2026-10-16).
- [x] Preliminary audit script executed for the two selected tables (81,898 and 10,892 rows respectively, **not certified source-wide totals**).
- [ ] Record full inventory of archive tables/files and reconcile SCUT with published source totals.
- [ ] Confirm units, types, timestamp quality, expected columns and signal semantics.
- [ ] Quantify nulls, infinities, duplicates, operating modes and PMSM class distribution.
- [ ] Decide explicitly which source tables and labels are suitable for model development.
- [ ] Document M2 conclusion and evidence links.

## M3 — Data preparation and EDA
- [ ] Preprocessing rules and data-validation checks.
- [ ] Time-aware or group-aware partition specification.
- [ ] Reproducible exploratory plots and data-quality report.
- [ ] Features and their units validated.

## M4 — EV monitoring
- [ ] Contextual baseline and alert-generation logic.
- [ ] Exploratory anomaly method comparison, if justified.
- [ ] Documented alert rate and error/uncertainty limitations.

## M5 — PMSM classification
- [ ] Confirm label mapping and independent recording/session splits.
- [ ] Train baseline classifier and compare alternatives.
- [ ] Report macro-F1, per-class recall and confusion matrix.

## M6 — Application
- [ ] Read-only telemetry replay and dashboard.
- [ ] Explainable alerts with uncertainty and recommendations.
- [ ] Integration tests, demo, runbook and documentation.

## M7 — Conditional research
- [ ] Verify labels, horizon and usage terms of real-EV battery-fault dataset.
- [ ] Record explicit GO/NO-GO decision.
- [ ] If GO, evaluate model on independently held-out vehicles/time.

## Evidence log
| Date | Milestone | Evidence / decision |
|---|---|---|
| 2026-10-16 | M1 | Approved planning baseline, all P1 documentation |
| 2026-10-16 | M2 | User's local installation/download/audit logs: SCUT selected table 81,898 rows; PMSM selected table 10,892 rows; no exact duplicates in selected tables; warnings require review |

**Progress rule:** A completed planning milestone does not imply that ML experiments or a functional vehicle-monitoring product have already been built.
