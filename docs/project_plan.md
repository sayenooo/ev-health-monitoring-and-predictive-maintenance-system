# Project Plan — HealthCar
**Document ID:** HC-PL-001  
**Version:** 1.0 · **Baseline date:** 2026-10-16  
**Planning status:** COMPLETE · **Execution status:** Data acquisition and characterization

## 1. Execution strategy
Develop an offline, reproducible research prototype before adding live integration. Maintain three independent evidence tracks: SCUT passenger-EV telemetry, labeled laboratory PMSM diagnostics, and optional verified real-EV failure histories. Do not combine heterogeneous sources as if they represent the same observation space.

## 2. Work breakdown structure & exit gates
| ID | Phase | Main work | Deliverables | Exit gate |
|---|---|---|---|---|
| P1 | Ideation & Project Planning | Charter, RQs, scope, requirements, source assessment, architecture, risk register | Approved planning package | **COMPLETE — 2026-10-16** |
| P2 | Dataset Acquisition & Characterization | Download, file inventory, schema, class labels, timestamps, missing/infinite values | Source inventory, audit reports, data dictionary | Every selected file and critical quality issue understood |
| P3 | Data Preparation & EDA | Clean/validate signals, handle irregular timing, derive features and visualize | Reproducible preprocessing, EDA findings, split manifest | Processing decisions justified; no obvious leakage |
| P4 | EV Monitoring Baseline | Context-aware rules; optional anomaly model and alert analysis | Monitoring baseline, qualitative anomaly assessment | Stable, traceable alert outputs; no false diagnosis claims |
| P5 | PMSM Fault Classification | Labels/session audit, supervised baselines, independent evaluation | Experimental fault report, metrics and confusion matrix | Test protocol and per-class results documented |
| P6 | Application & Integration | Read-only replay, dashboard, evidence/uncertainty display, tests | Executable demo, screenshots, runbook | End-to-end demo reproducible |
| P7 | Predictive Maintenance Research | Review real-EV labeled failure records; prediction horizon; model if feasible | Feasibility decision and optional early-warning experiment | Validated independent prospective-style evidence |

P4 and P5 may proceed as distinct tracks after P3. P7 is not a prerequisite for a monitoring MVP.

## 3. Recommended implementation sequence
- **Milestone M1 — planning package:** final approved charter, requirements, architecture, risks, acceptance criteria.
- **M2 — data quality gate:** source file selection reconciled with publishers, anomaly/missingness summary, correct unit interpretation.
- **M3 — preprocessing baseline:** deterministic cleaning and context-specific feature pipeline.
- **M4 — monitoring prototype:** measured signals + contextual alerts + evaluation report.
- **M5 — experimental fault model:** held-out PMSM classification assessment.
- **M6 — user-facing MVP:** dashboard, model interfaces, integration tests and reproducible demo.
- **M7 — conditional research outcome:** explicit go/no-go for future-failure prediction.

## 4. Dependencies and decision gates
- P2 → P3: file inventory, schema and critical defects understood.
- P3 → P4: agreed features, time-aware evaluation boundary, safe transformations.
- P3 → P5: verified PMSM target mapping and independent split group.
- P4/P5 → P6: stable model interfaces with honest uncertainty semantics.
- P7 **GO** only if verified real-world failure labels, sufficient lead-time histories and independent vehicle/time-based validation can be established; otherwise document **NO-GO** and ship the monitoring MVP without a future-failure prediction claim.

## 5. Quality and evaluation principles
- **Data:** missingness, finite-value checks, schema consistency, sampling gaps, timestamp order and source versions.
- **SCUT:** evaluate alert volume/robustness; without ground-truth faults, do not state real fault precision or recall.
- **PMSM:** majority-class baseline followed by justified models; evaluate macro-F1, per-class recall, supports and confusion matrix using group-aware split where possible.
- **Dashboard:** distinguish absent data, unusual observation, model-generated hypothesis and verified fault; safe read-only actions.
- **Engineering:** repeatable commands, unit tests, source references, no secrets or original dataset dumps in Git.

## 6. Risk register
| ID | Risk | Impact | Mitigation / response |
|---|---|---|---|
| R1 | No verified failure labels in telemetry source | Predictive claims cannot be tested | Limit to anomaly analysis; separate optional labeled research |
| R2 | Experimental PMSM data differ from operational EV conditions | Poor on-road generalization | Clearly label lab-only results; no vehicle-level performance claim |
| R3 | Incomplete/incorrect source file selection | Biased EDA and mistaken row counts | Inventory all files, compare published totals and select explicitly |
| R4 | Non-finite, implausible or irregular measurements | Unstable statistics/models | Audit first; document cleaning choices and timing gaps |
| R5 | Leakage between similar time windows / lab sessions | Inflated reported metrics | Time/group-based train/test partitions, split manifest |
| R6 | Driver recommendations overstate certainty | Misleading action guidance | Evidence, uncertainty, unavailable-data status, no autonomous actuation |
| R7 | Large additional data / limited hardware | Runtime and storage burden | Start with a single SCUT passenger car and sampled inspection |
| R8 | Third-party license or redistribution uncertainty | Publication issue | Link original records; verify terms; do not upload raw archives |

## 7. Roles and change control
Primary developer/researcher owns data provenance, preprocessing, experiments, evaluation, documentation and integration. Record architecture or requirement changes with a short rationale in Git commits/PRs. Change the plan version if the scope, target, datasets or acceptance criteria materially change.

## 8. Progress and evidence
The living task ledger is [progress_tracker.md](progress_tracker.md). Check tasks there only when their evidence can be linked to a commit, notebook, audit artifact or demo. The companion PDF is a signed-off **planning snapshot** and printable/markable milestone tracker, not a live mirror of GitHub state.

## 9. References
See [references.md](references.md). Claims about model effectiveness will be introduced only with completed project experiments and citations.
