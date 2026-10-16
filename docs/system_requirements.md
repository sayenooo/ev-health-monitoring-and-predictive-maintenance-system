# ML System Requirements — HealthCar
**Document ID:** HC-SRS-001 · **Version:** 2.0 · **Baseline:** 2026-10-16

## Functional requirements
| ID | Requirement | Priority | Verification |
|---|---|---|---|
| ML-01 | Consume time-ordered EV telemetry and retain a rolling history window | Must | Sequential replay shows updated input state |
| ML-02 | Validate missing, non-finite, stale and implausible measurements | Must | Data-quality report and checks |
| ML-03 | Calculate interpretable context-aware vehicle-health descriptors | Must | Tested feature-extraction pipeline |
| ML-04 | Detect unusual current behavior using statistical/ML anomaly methods | Must | Contextual monitoring outputs and alert analysis |
| ML-05 | Generate new monitoring inference as each observation/window arrives | Must | Sequential replay test |
| ML-06 | Train predictive models using strictly earlier inputs and verified subsequent fault outcomes | Must | Target/split audit and predictive experiment |
| ML-07 | Compare predictive baselines and candidate stronger models | Must | Independent model comparison |
| ML-08 | Report future-risk score and clearly state supported time horizon (if any) | Must | Risk output and defensible definition |
| ML-09 | Produce evidence-backed early warnings and suggestions, without vehicle control | Must | Demonstration with explanation and uncertainty |
| ML-10 | Evaluate PR-AUC, recall, precision/F1, class distribution, false alarms and, where available, lead time | Must | Evaluation report |
| ML-11 | Maintain reproducible data provenance, code, seeds and experiment settings | Must | Reproducibility audit |
| ML-12 | Support other EV components only when compatible sensors and labels exist | Scope guard | Evidence mapping by component |

## Quality requirements
- **Temporal validity:** no look-ahead in feature engineering or labels; no overlapping leakage across partitions.
- **Group validity:** recordings from the same vehicle or experiment do not cross incompatible holdout groups.
- **Signal integrity:** explicit units, time gaps, data quality flags and source definitions.
- **Operational definition:** repeated inference in chronological replay; continuous weight updates are *not* assumed.
- **Transparency:** distinguish observed deviations, model-estimated risk, confirmed fault and unavailable sensors.
- **Reproducibility:** notebooks/code, versioned configurations and measured results.
- **Safety:** informational recommendations only; no actuation, automatic repair or safety certification claims.

## BDAPP deliverable boundary
The deliverable is a tested **ML research prototype** for both monitoring and prediction, not a full website or business software platform.
