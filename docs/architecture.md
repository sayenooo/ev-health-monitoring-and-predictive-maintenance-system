# Machine Learning Architecture — HealthCar
**Document ID:** HC-ARC-001 · **Version:** 2.0 · **Baseline:** 2026-10-16

## Conceptual inference pipeline

```text
            Time-ordered EV sensor observations
                           |
                           v
             Signal integrity and timestamp checks
                           |
                           v
             Rolling time-series history window
                           |
               +-----------+-----------+
               |                       |
               v                       v
     TRACK A: CURRENT HEALTH    TRACK B: FUTURE RISK
     operating context         temporal features
     statistical baseline      labeled event outcomes
     anomaly model             prospective risk model
               |                       |
               v                       v
      Current anomaly score     Future fault-risk score
               |                       |
               +-----------+-----------+
                           |
                           v
          Early warning, evidence and uncertainty
                           |
                           v
          Sequential replay + evaluated ML outputs
```

Each new record/window triggers **new model inference** in the replay. Model training is conducted as separate offline experiments. This is continuous observation/inference, not continuous retraining.

## Modules
1. **Source adapters:** historical CSV/archive loaders and provenance.
2. **Validation:** schema, units, timestamps, missing, non-finite/stale records.
3. **Temporal features:** rolling-window aggregates, trends, operational context.
4. **Monitoring ML:** contextual baselines/anomaly detection and persistence checks.
5. **Predictive ML:** supervised classification/risk from verified pre-event history.
6. **Alert layer:** evidence, model limitations and suggested owner action.
7. **Evaluation/replay:** measured alert behavior, prediction metrics, short time-series demo.

## Research datasets
SCUT supports track A sensor monitoring and feature exploration; Zhang et al. processed real-EV fault histories are a track B candidate pending label/time audit; PMSM supports optional, independent laboratory diagnostics.

**Data from incompatible instruments must not be merged as if measured on the same vehicle or event timeline.**

## Scope boundaries
The long-term concept concerns EV battery, propulsion, inverter, thermal and charging subsystems. Empirical implementation is limited to validated available signals and failures. User accounts, full application platform, live OBD hardware, automatic diagnosis without evidence and vehicle commands are not required for BDAPP.
