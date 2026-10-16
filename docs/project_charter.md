# HealthCar — Project Charter
**Document ID:** HC-CH-001 · **Version:** 1.1 · **Status:** Final BDAPP planning baseline · **Date:** 2026-10-16

## Project identity
**Title:** Machine Learning-Based Electric Vehicle Fault Prediction and Predictive Maintenance  
**Discipline:** Big Data Analysis and Prediction Project (BDAPP)  
**Domain:** EV time-series analysis, imbalanced classification, early-warning prediction  
**Deliverable type:** ML research pipeline, reproducible experiments and evaluation report.

## Problem statement
Potential battery problems may be preceded by subtle historical changes in voltage, current and temperature. Detecting such predictive signals from real-world charging histories is difficult due to irregular sampling, heterogeneous operating conditions, rare events and possible validation leakage. A comparative, reproducible study is needed to determine whether ML can identify at-risk EVs from historical telemetry.

## Main research objective
**Train and evaluate predictive ML models on pre-fault EV charging history to identify vehicles at elevated risk of subsequently confirmed battery faults.** A fixed N-day failure-horizon target will be used only if actual label timestamps support it; otherwise the primary target is vehicle-level early fault-risk classification, not time-to-failure.

## Research questions
- RQ1: Which historical charging and thermal/electrical features are informative for future battery-fault risk?
- RQ2: Which classification approaches generalize best to independently held-out vehicles?
- RQ3: What are the effects of imbalance, aggregation window, and decision threshold on missed faults and false alarms?
- RQ4: How interpretable and calibrated are model outputs?
- RQ5: Is a time-specific lead-time forecast feasible from the available metadata?

## Primary hypothesis
History-aware models provide better early risk discrimination than an appropriate prior-probability or simple-feature baseline, under vehicle-disjoint evaluation. This is a **hypothesis to test**, not a claimed result.

## Primary dataset
Zhang et al. (2023), *Realistic fault detection of li-ion battery via dynamical deep learning*, publicly released processed data: https://doi.org/10.6084/m9.figshare.23659323. Publisher reports three collections, >690,000 charging snippets from 347 EVs and vehicle-level fault annotations. **Actual file schema, vehicle IDs and label timing must be checked before defining final outcome and horizon.**

## Supporting data
SCUT: exploratory EV telemetry and features, no future fault ground truth. PMSM: optional independent, labeled **laboratory current-fault classification** study. Neither replaces the primary prediction experiment.

## In scope
Dataset/label audit; EDA; time-series feature engineering; data leakage prevention; class imbalance mitigation; classification baselines and advanced models where justified; group-aware cross-validation; evaluation; interpretability; scientific report and presentation.

## Out of scope
Production EV health application, dashboards as deliverables, FastAPI/backend, OBD-II hardware, live monitoring, vehicle control, universal multi-component future-failure claims.

## Completion criteria
- A clearly validated target and dataset provenance.
- A documented vehicle-disjoint split and leakage prevention.
- At least one naive baseline and two substantive candidate prediction approaches.
- Reproducible metrics with precision/recall/F1/PR-AUC, confusion matrix and threshold analysis.
- Scientifically defensible conclusions, model limitations, notebooks and BDAPP presentation.
- If predictive ground truth is insufficient, explicit feasibility revision instead of false claims.

**Ideation and Project Planning is COMPLETE. Model building and empirical feasibility are subsequent stages.**
