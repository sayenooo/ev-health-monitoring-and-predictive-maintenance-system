# Evaluation Plan — HealthCar
**Document ID:** HC-EVL-001 · **Version:** 2.0 · **Baseline:** 2026-10-16

## Question being evaluated
Does HealthCar (A) identify anomalous *current* EV behavior from continuously consumed telemetry and (B) forecast elevated risk of a **subsequently documented** fault from earlier measurements, with acceptable false-alarm and missed-event trade-offs?

## Track A: continuous monitoring
- Time-ordered loading, data-validation and rolling-window construction.
- Operating-context statistical baseline and ML anomaly method where justified.
- Repeated inference and alert-persistence experiments on historical replay.
- Measure signal coverage, alerts per time/records, distribution shifts, sensitivity to operating modes and stability.
- Only compute real-fault precision/recall where independently confirmed event labels exist; simulated perturbations must be labeled synthetic.

## Track B: future risk prediction
- Freeze event-label definition, observation end time and prediction horizon (only if verified in actual records).
- Train/validation/test with vehicle separation and chronological safeguards.
- Compute all transforms with training-only fit; no future sensor readings as features.
- Compare naive baseline and at least two justified predictive ML methods.
- Primary outcomes where available: fault-positive PR-AUC, recall/precision and false-alarm burden.
- Secondary: macro-F1, confusion matrix, ROC-AUC as appropriate, calibration, threshold curves, confidence intervals.
- For documented event timestamps only: advanced warning lead time and time-to-event metrics.

## Combined demonstration
Run both inference interfaces sequentially over replayed telemetry **where relevant model inputs exist**. For differing datasets, demonstrate two explicit tracks rather than fabricate a shared vehicle record. Show status, risk estimate, source, uncertainty and evidence; distinguish prediction from diagnosis.

## Reporting requirements
- Cite source records and data processing decisions.
- Show class prevalence, warning thresholds and error types.
- Include leakage checks and independently held-out results.
- No invented quantitative accuracy, no universal multi-component reliability claims and no automated vehicle intervention.
