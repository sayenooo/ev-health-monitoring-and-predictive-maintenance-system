# HealthCar — Project Vision (v0.1)

## Problem statement
Passenger battery-electric vehicles generate rich telemetry, but access to useful measurements varies by make, model and hardware. The owner may lack transparent historical trends, explanations of unusual conditions, and clear recommended next steps. A student prototype must not assume universal vehicle or OEM diagnostic access.

## Target audience
Owners of **passenger BEVs**. Not limited to Tesla, and not a heavy-truck/Scania product.

## Goal
Develop an AI-powered **non-autonomous**, evidence-driven software prototype to monitor available EV telemetry, detect unusual operating patterns, demonstrate component-specific fault classification where labels exist, and present understandable driver recommendations. True future-failure prediction is a research extension dependent on labeled longitudinal data.

## Core flow
1. **Monitor:** ingest and inspect vehicle signals with their operating context.
2. **Detect:** surface sensor anomalies while distinguishing them from verified diagnoses.
3. **Predict:** estimate validated future risk only after verifying event dates and a leakage-safe evaluation design.
4. **Recommend:** give explainable, read-only decision support; driver retains authority.

## MVP scope
- Time series ingestion and quality reports for passenger SCUT EV battery/driving telemetry.
- Cell-voltage and temperature spreads, pack measurements, operating-mode context.
- Contextual anomaly rules/ML baselines **after** preprocessing.
- Separate 9-class laboratory PMSM/inverter fault model **after** labeled-data audit.
- Later: telemetry replay dashboard with alerts containing uncertainty and evidence.

## Not in MVP
- Automatic repair or vehicle actuation, guaranteed make/model compatibility, validated SOH/RUL or future failure dates without ground truth, charging-network routing, tires/brakes/cooling diagnosis without matching data.

## Success criteria
- Downloadable, reproducible data processing with no third-party archives in Git.
- Every diagnostic metric is traceable to real measured fields and documented units.
- Timestamp gaps, missingness and sensor anomalies are reported.
- Evaluations avoid adjacent-window / same-session leakage.
- UI distinguishes 'data unavailable', 'anomaly', 'possible problem' and 'confirmed diagnosis'.
