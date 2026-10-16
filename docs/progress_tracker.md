# HealthCar — BDAPP Progress Tracker
**Document ID:** HC-TR-001 · **Version:** 1.1 · **Updated:** 2026-10-16

## Milestone ledger
| ID | Milestone | Status | Evidence |
|---|---|---|---|
| M1 | Ideation & prediction research planning | **COMPLETE** | Final research question, charter, model requirements and BDAPP plan |
| M2 | Primary data / target feasibility | **IN PROGRESS** | Source published; files and labels not yet fully audited |
| M3 | EDA and leakage-safe preprocessing | NOT STARTED | — |
| M4 | Prediction baselines | NOT STARTED | — |
| M5 | Advanced model comparison | NOT STARTED | — |
| M6 | Evaluation and interpretation | NOT STARTED | — |
| M7 | BDAPP report, slides and reproducibility | NOT STARTED | — |

## M1 — COMPLETE (2026-10-16)
- [x] Define the prediction-first BDAPP problem and primary candidate target.
- [x] Prioritize a real-EV labeled dataset for early fault-risk classification.
- [x] Specify data leakage controls, comparison metrics and candidate modeling approaches.
- [x] Establish research scope, expected deliverables and risk/decision gates.

## M2 — CURRENT: target feasibility
- [x] Identify primary processed Figshare dataset and peer-reviewed methodology.
- [x] Download supporting SCUT and PMSM datasets locally; basic audit executed (2026-10-16).
- [ ] Inventory all Figshare archive files, labels and vehicle identifiers.
- [ ] Verify presence or absence of fault/event time stamps and available prediction lead time.
- [ ] Establish valid `y`, unit of prediction and allowable temporal inputs.
- [ ] Record target availability, class distribution, licensing and split decision.
- [ ] Update target specification and close M2 with evidence.

## M3 — EDA & PREPROCESSING
- [ ] Explore pre-fault historical signals and imbalance.
- [ ] Clean/standardize training-only features and document gaps.
- [ ] Engineer temporal aggregates / trend descriptors.
- [ ] Produce vehicle-disjoint train/validation/test manifest.

## M4 — BASELINES
- [ ] Define dummy baseline.
- [ ] Train and validate at least two candidate prediction methods.
- [ ] Record PR-AUC, precision, recall, F1 and confusion matrix.

## M5 — ADVANCED
- [ ] Tune gradient boosting or justified alternative.
- [ ] Evaluate sequence modeling only if feasible and useful.
- [ ] Compare controlled experimental variants fairly.

## M6 — EVALUATION
- [ ] Analyze false alarms, misses, threshold behavior and calibration.
- [ ] Interpret important historical features and subgroup performance.
- [ ] Document conclusions and generalization limits.

## M7 — DELIVERY
- [ ] Produce final BDAPP technical report and slides.
- [ ] Clean reproducible notebooks/code and update README.
- [ ] Provide final dataset/model/metric references and course demo.

## Evidence log
| Date | Change | Notes |
|---|---|---|
| 2026-10-16 | M1 planning complete (v1.1) | Research re-centered on predictive ML for BDAPP |
| 2026-10-16 | Supporting data acquired | Local SCUT selected table: 81,898 rows; PMSM selected table: 10,892 rows; not the primary predictive labels |
