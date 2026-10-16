# HealthCar — ML Evaluation Plan (draft)

## Gate 0: before modeling
- [ ] Download official source archives; validate integrity and provenance
- [ ] Identify exact raw tables and field names, types, labels and units
- [ ] Calculate duplicate / missing / infinity / timestamp-gap rates by vehicle
- [ ] Confirm charging modes, sign of pack current and presence of experiment IDs

## Track A — SCUT EV monitoring
1. Train simple context-aware statistical rules on a defined earlier observation period.
2. Compare a robust-baseline score with Isolation Forest only if warranted by the signal distribution.
3. Evaluate warning volume per observation/time period, temporal stability and behavior across charging/driving modes.
4. Preserve chronological boundaries; no shuffled random adjacent windows.
5. **Never report fault-detection accuracy/recall** on SCUT without true verified fault labels. Artificially inserted perturbations may be labeled synthetic stress tests, not 'real EV faults'.

## Track B — PMSM supervised lab classification
1. Confirm F0–F8 target, class counts, original vs derived predictors.
2. Compare majority baseline, logistic regression and Random Forest.
3. Split by experimental recording/session or nonoverlapping time blocks when possible.
4. Report macro-F1, per-class recall, class support, confusion matrix and uncertainty.
5. Be explicit about any inability to validate on unseen rigs/vehicles.

## Track C — optional predictive maintenance
Require verified failure times and pre-fault histories before predicting future failure. Group test by vehicle and time; define horizon from the available labels. Report precision/recall, PR-AUC, false alarms per vehicle-time, and advance warning lead time.

## Product validation
- Distinguish sensor missingness, anomalous observation, potential fault and confirmed diagnosis.
- Prefer evidence-based, non-invasive recommendations with uncertainty.
- No actuator control, dangerous maintenance instructions or automatic repairs.
