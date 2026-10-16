# Project Plan — HealthCar
**Document ID:** HC-PL-001 · **Version:** 2.0 · **Baseline:** 2026-10-16  
**Scope:** ML-based EV Health Monitoring **AND** Predictive Maintenance for BDAPP

## Fixed research objective
Build an ML system that repeatedly evaluates available EV telemetry, detects current anomalies and predicts prospective maintenance risks from **earlier measurements** when validated subsequent-fault outcomes are available. Give interpretable early warnings; do not build a commercial vehicle-control platform.

## Milestone plan
| ID | Milestone | Main work | Exit gate |
|---|---|---|---|
| M1 | Ideation & Project Planning | Fix objective, core ML tracks, scope, metrics, risks and source strategy | **COMPLETE — 2026-10-16** |
| M2 | Data Source & Target Feasibility | Inventory actual SCUT, PMSM and real-EV fault sources; verify inputs, labels and time order | Valid monitoring source and valid prospective prediction target identified |
| M3 | EDA & Time-Series Preprocessing | Audit sensor units, gaps and missingness; create temporal windows; define splits | Reproducible datasets and no leakage |
| M4 | Continuous Monitoring Model | Build operating-context baseline and anomaly model; evaluate alert behavior | Sequential scoring and evidence-backed current-health alerts |
| M5 | Predictive Maintenance Model | Train future-risk baseline(s) and improved model(s); set horizon only if labels permit | Independent predictive evaluation |
| M6 | Joint Evaluation & Early-Warning Demo | Replay telemetry, surface monitoring/prediction results, evaluate alert errors and timing | Working ML research proof of concept and clear measured limitations |
| M7 | BDAPP Research Deliverables | Final model comparison, report, graphs, notebooks, presentation | Reproducible and defensible final submission |

M4 and M5 are **both mandatory modeling goals**, subject to the scientifically necessary future-event label gate. A data limitation does not erase the goal.

## Dataset allocation
- **Monitoring:** SCUT real-world EV telemetry (available locally; selected table quality not yet fully audited).
- **Future prediction:** Zhang et al. real EV historical charging/fault records (candidate; dataset structure and event chronology need inspection). Another source may be selected only after documented feasibility assessment.
- **Optional additional fault classification:** PMSM experimental inverter data, clearly labeled laboratory evidence.

## Technical evaluation design
### Monitoring track
Interpret raw context → rolling windows → health features → statistical/ML anomaly scores → repeated alert decisions. Evaluate false alert burden, temporal stability and known/verified anomalies only where ground truth exists.

### Prediction track
Define observed history interval and subsequent fault outcome; ensure future information is excluded from features. Partition by vehicle and, when applicable, time. Compare naive baseline, logistic/tree methods and justified temporal models. Report PR-AUC, recall, precision, F1, calibration and false-alarm tradeoffs; report lead time only if event times permit.

### Integration
Use an offline historical telemetry replay to demonstrate repeated model inference and alert generation. No requirement for deployed OBD hardware, full frontend or automated repairs.

## Research risks and controls
| Risk | Control |
|---|---|
| Inadequate prospective failure labels | Audit labeled source and actual event times; do not invent prediction horizon |
| Different sensors or component coverage | Independent experimental tracks and explicit scope-of-validity |
| Leakage via overlapping windows / vehicle identity | Group-aware, chronology-aware partitions and train-only transforms |
| Highly imbalanced faults | PR-AUC, class-specific recall, threshold and false-alarm analysis |
| Spurious anomaly alerts | Contextual baselines and persistence/robustness checks |
| Hardware/data size limits | Stream/chunk data and demonstrate inference via offline replay |
| False sense of automotive reliability | Research-only alerts with evidence and uncertainties |

## Progress governance
The latest completion record lives in `docs/progress_tracker.md`. The companion PDF is a versioned baseline with a markable checklist, not an automatically synchronized project-management system.

**Next task:** M2 — inspect all downloaded data files, validate the real-EV future-fault source and freeze valid inputs and targets for both core tracks.
