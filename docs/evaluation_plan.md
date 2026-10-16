# ML Evaluation Protocol — HealthCar
**Document ID:** HC-EVL-001 · **Version:** 1.1 · **Baseline:** 2026-10-16

## Scientific objective
Evaluate whether historical EV charging sensor records predict vehicle-level confirmed battery-fault status for unseen vehicles, and assess whether an explicit future prediction horizon is supported by labels and timestamps.

## Validation design
1. Audit original label creation, time ordering, vehicle IDs, dataset classes and any publisher-established train/test splits.
2. Define observation windows *before* labels / confirmed failures where such timing is verifiable.
3. Split at the **vehicle level** into train, validation and held-out test. Never let snippets from the same vehicle cross partitions.
4. Fit scalers, imputers, encoders and feature selection solely on the training data within each fold.
5. Use stratification/group-aware techniques without leaking labels through vehicle identifiers or future information.

## Models
- **Reference:** majority/prior-probability or constant-risk dummy.
- **Baselines:** logistic regression and random forest (or comparable, resource-feasible predictors).
- **Stronger comparison:** gradient boosting; evaluate a sequence model only if fair train/validation support exists.

## Measures
**Primary:** PR-AUC and class-specific recall/precision for the confirmed-fault class in imbalanced data.

**Secondary:** macro-F1, confusion matrix, ROC-AUC where defined, threshold-vs-false-alert trade-off, probability calibration and bootstrap uncertainty where feasible.

**Lead-time / horizon:** calculate only when per-vehicle fault times and data windows support it. Do not reinterpret vehicle-level status as an N-day failure label.

## Error analysis
Analyze false positives and missed fault cases, class prevalence, time-coverage effects and the influence of sensor histories. Document dataset domain and possible distribution shift to other EV brands or conditions.

## Supporting data limits
SCUT has no verified future-fault events, so it cannot prove predictive fault accuracy. PMSM faults are laboratory present-state classes; report separately if used.

## Reporting policy
Release split definitions, configuration, model seeds, data schema decisions, charts and balanced limitations. No 'accuracy' or 'failure prediction' numbers until actual independent test experiments have run.
