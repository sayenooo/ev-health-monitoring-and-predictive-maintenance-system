# HealthCar — BDAPP Project Plan
**Document ID:** HC-PL-001 · **Version:** 1.1 · **Approved:** 2026-10-16

## Research question
Can ML models trained on *past EV charging records* identify battery problems confirmed **after** the observed history, better than simple baselines, without leaking information from the same vehicle into train and test?

## Prediction specification — feasibility gated
- **Unit:** vehicle, derived from chronologically ordered historical charging snippets.
- **Inputs:** historical current, voltage, temperature, charge and derived time-series descriptors, as available from primary data.
- **Primary label candidate:** verified vehicle-level fault outcome (binary normal vs confirmed fault).
- **Prediction horizon:** only set a specific time-to-fault cutoff if file-level event timestamps support it. Otherwise call this *early fault-risk classification*, **not** 'fails within seven days'.
- **Output:** per-vehicle risk score/class and supporting feature evidence.
- **Split:** whole vehicles separated across train/validation/test, with time-order safeguards and preprocessing fitted only on training vehicles.
- **Metrics:** PR-AUC, class recall, precision, F1, confusion matrix, false-positive trade-offs, calibration; event lead time only if labels support it.

## Work breakdown structure
| ID | Workstream | Outputs | Completion gate |
|---|---|---|---|
| M1 | Ideation & ML Research Planning | Approved RQs, target candidate, dataset strategy, metrics, risks, milestone plan | **COMPLETE** |
| M2 | Target & Dataset Feasibility | Primary processed dataset inventory, label granularity and timestamp review, go/no-go on horizon | Dataset demonstrably supports a predictive target |
| M3 | EDA & Data Preparation | Temporal data quality, outliers, imbalance, split manifest and features | Leakage controls and data dictionary documented |
| M4 | Prediction Baselines | Dummy, logistic regression, random forest or other justified baselines | Reproducible independent initial metrics |
| M5 | Advanced Model Comparison | Gradient boosting and optional sequence approach; tuning on validation only | Fair comparison against baseline |
| M6 | Evaluation & Interpretation | PR curves, threshold trade-offs, calibration, ablations/explanations, robustness | Scientifically defensible findings and limitations |
| M7 | BDAPP Final Deliverables | Clean notebooks, figures, report, proposal/presentation updates, GitHub reproducibility | Complete ML-focused course submission |

## Experimental strategy
1. Audit publisher source files and metadata before stating any temporal prediction horizon.
2. Construct non-overlapping vehicle-level groups.
3. Describe class prevalence and time/coverage differences by outcome.
4. Fit baseline feature extraction and preprocessing only on training partitions.
5. Train simple models first. Use a sequence network only if split/sample size and project time warrant it.
6. Tune class weights and thresholds on validation, **never** the held-out test.
7. Document uncertainty, false alarms, failure misses and applicability limits.

## Dataset priority
1. **Primary:** processed Zhang et al. EV charging/fault dataset: https://doi.org/10.6084/m9.figshare.23659323
2. **Auxiliary:** SCUT telemetry — for independent EDA/monitoring feature investigation, not primary labels.
3. **Optional:** PMSM labeled laboratory fault classification — separate supplementary experiment, not vehicle future-failure prediction.

## Research risks & mitigations
| Risk | Mitigation |
|---|---|
| Vehicle-level labels without reliable failure timestamps | Use earlier-history vehicle-level risk classification; do not invent an N-day horizon |
| Same-vehicle / neighboring-snippet leakage | Vehicle-disjoint partitions and group-aware evaluation |
| Extreme class imbalance and uncertain negative class | PR-AUC, per-class recall, baseline and probability calibration |
| Large primary dataset / limited RAM | Metadata inventory, streamed reads, bounded subset prototyping |
| Lab vs on-road source mismatch | Keep PMSM as a separate optional result |
| Unsupported full-EV multi-component claim | Define the model's supported battery target explicitly |
| Complicated software engineering scope | Notebook-first pipeline; interface not required |

## Phase closure policy
M1 is signed off based on clear research design. M2–M7 are checked in [progress_tracker.md](progress_tracker.md) only after data and model evidence exist. The PDF companion is a fixed version snapshot, not live GitHub synchronization.
