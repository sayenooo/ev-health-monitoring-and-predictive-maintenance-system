# ML Experiment Architecture — HealthCar
**Document ID:** HC-ARC-001 · **Version:** 1.1 · **Baseline:** 2026-10-16

## Prediction-first flow

```text
Published processed EV charging/fault records (Zhang et al.)
        |
        v
[Source inventory + vehicle-level labels + chronology]
        |
        v
[Quality audit + target/horizon feasibility]
        |
        v
[Vehicle-disjoint train / validation / test split]
        |
        v
[Historical feature extraction and train-only preprocessing]
        |
        +----------------------+----------------------+
        |                      |                      |
        v                      v                      v
[Dummy / linear]        [Tree / boosting]      [Optional sequence]
        |                      |                      |
        +----------------------+----------------------+
                               |
                               v
                    [Independent test comparison]
                               |
                               v
                [PR-AUC / recall / precision / F1]
                               |
                               v
             [Interpretation + technical report + slides]

Auxiliary: SCUT --> real-vehicle signal characterization.
Optional: PMSM --> separate laboratory fault classification experiment.
```

## Main deliverables
- Dataset, target and split specification.
- EDA and preprocessing notebooks.
- Baseline/model comparison notebooks.
- Reproducible metrics and error analysis.
- BDAPP research report / presentation.

## Design rules
Use vehicle-level grouping for validation, prevent overlapping temporal information, fit transformations exclusively within training partitions and document missing sensors. A numeric 'fault within N days' endpoint must not be introduced before verifying event timestamps. SCUT and PMSM are separate evidence tracks, not replacements for labeled future-fault outcomes.

## No application layer required
API services, live OBD-II, continuous vehicle monitoring and production dashboards are not part of the BDAPP core.
