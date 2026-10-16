# Project Charter — HealthCar
**Document ID:** HC-CH-001  
**Version:** 2.0  
**Status:** FINAL — IDEATION COMPLETE  
**Approved baseline:** 2026-10-16  
**Course:** Big Data Analysis and Prediction Project (BDAPP)

## 1. Official project title
**HealthCar: Electric Vehicle Health Monitoring and Predictive Maintenance System**

## 2. Main objective (fixed)
**To develop a machine learning-based system that continuously monitors electric vehicle health using sensor data, detects abnormal operating conditions, predicts potential future failures, and provides early warnings to support preventive maintenance.**

## 3. Problem statement
Electric vehicles generate time-dependent measurements of electrical, thermal and operating conditions. Deviations may indicate an emerging issue, yet individual readings can be normal for one condition and suspicious for another. Historical changes may also contain signals preceding future faults. HealthCar studies whether machine learning can analyze **incoming telemetry plus its recent history** to identify unusual conditions and predict documented future maintenance risks with appropriate uncertainty.

## 4. Intended operation
1. Receive time-ordered sensor measurements.
2. Validate and accumulate a rolling history window.
3. Estimate current health indicators and detect abnormal behavior.
4. Predict future fault risk where temporally appropriate verified labels exist.
5. Generate explainable alerts for the vehicle owner.
6. Repeat these steps as new measurements arrive.

**Continuous** means repeated inference over new observations. It does not require the model to update its weights online. An offline replay of chronological telemetry is the initial BDAPP demonstration; live vehicle hardware integration may follow in later research.

## 5. Research questions
- RQ1: Which telemetry features and operating context indicate abnormal EV behavior?
- RQ2: Which methods detect anomalies effectively without treating all outliers as confirmed faults?
- RQ3: Can historical time-series windows predict a *subsequently documented* component fault or elevated future risk?
- RQ4: How do different models trade detection lead time, false warnings and missed failures?
- RQ5: How can uncertainty and evidence be conveyed in a clear early-warning output?

## 6. Scope
**Core Track A — Continuous EV health monitoring**
Time-series ingestion/replay, quality checks, contextual indicators, anomaly model/baseline, repeated scoring and anomaly alerts.

**Core Track B — Predictive maintenance**
Define a historically verifiable target; construct features from pre-event windows; train and compare supervised temporal/fault-risk models; quantify early warning accuracy and lead time *if event time is available*.

**Core Track C — Early warning**
Combine monitoring and predictive signals into interpretable evidence-based notifications and preventive-maintenance suggestions. A modest notebook/visual demo is sufficient.

## 7. Component coverage
The **product vision** concerns the health of an EV's battery, drive motor, inverter, charging and thermal components. The **evaluated MVP** will cover those components for which actual measured inputs and valid model ground truth are available. Dataset constraints determine testable submodules, not the overall project identity.

## 8. BDAPP deliverables
Data assessment; preprocessing; EDA; time-series feature engineering; monitoring/anomaly model; future-risk prediction model; baseline and advanced model comparison; independent evaluation; sequential replay proof of concept; scientific report and presentation.

## 9. Explicit exclusions
Full commercial application, authentication/backend business functions, route planning, remote vehicle control, autonomous repairs, claims of universal EV compatibility or unvalidated exact failure dates.

## 10. Acceptance criteria
- The monitoring model produces repeated, traceable outputs as telemetry windows advance.
- The predictive model is evaluated only where the source supports documented subsequent faults/risk targets.
- The pipeline has time/vehicle-group leakage safeguards, documented data quality, class imbalance treatment and independent evaluation.
- Reports distinguish anomalous signals, statistical forecasts, confirmed failures and unavailable data.
- False alarms and detection performance are quantified where suitable labels exist.
- Results can be reproduced from cited datasets and code.

## 11. Scientific feasibility rule
**The project goal will not be redefined to match whichever dataset is easiest.** If an available source lacks future fault labels, it can support monitoring but not validated future-failure prediction. Find/validate a suitable labeled source for the predictive track or clearly report the blocked requirement. Never invent a target or lead-time statistic.

**Ideation & Project Planning: CLOSED.** Changes after this baseline require an explicit new scope decision, not informal rewriting.
