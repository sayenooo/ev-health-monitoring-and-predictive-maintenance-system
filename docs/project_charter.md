# Project Charter — HealthCar
**Document ID:** HC-CH-001  
**Version:** 1.0  
**Status:** Approved planning baseline  
**Date:** 2026-10-16

## 1. Project identity
- **Name:** HealthCar
- **Formal title:** Electric Vehicle Health Monitoring and Predictive Maintenance System
- **Domain:** Applied machine learning, automotive telemetry, fault diagnosis
- **Primary user:** Owners of passenger battery-electric vehicles (BEVs)
- **Product type:** Non-autonomous, read-only research decision-support prototype

## 2. Problem
Battery-electric vehicles produce operating telemetry that can reveal charge state, electrical load, thermal behavior, and potential anomalies. Useful interpretations are not always accessible or consistent across vehicles. A system is needed to organize the *available* measurements, detect unusual behavior in context, and communicate the evidence and uncertainty to the owner.

## 3. Goal
Design and implement a reproducible ML-assisted prototype that (a) monitors available EV telemetry, (b) detects contextual anomalies, (c) investigates classifiable component faults with suitable labels, and (d) explains findings and recommendations. Future-failure risk estimation is undertaken only when data provide verified historical events and a defensible test protocol.

## 4. Research questions
- RQ1: What operating and battery-condition indicators can be computed from publicly available passenger-EV signals?
- RQ2: How robustly can atypical sensor behavior be identified without verified fault labels?
- RQ3: How accurately can laboratory inverter conditions be classified under a leakage-aware evaluation protocol?
- RQ4: Can model evidence be communicated in an honest, non-autonomous driver-facing interface?
- RQ5 (conditional): Can labeled real-EV battery records support early-warning estimates at a predefined horizon?

## 5. Objectives and deliverables
| Objective | Deliverable |
|---|---|
| O1: Define reproducible data provenance and quality standards | Source registry, statistical audits, data dictionary |
| O2: Establish EV monitoring baseline | Feature pipeline and context-aware anomaly analysis |
| O3: Evaluate component fault classification | PMSM laboratory baseline and confusion matrix |
| O4: Create explainable prototype | Read-only telemetry replay dashboard and evidence-based alerts |
| O5: Evaluate future-risk feasibility | Go/no-go memo; only train if labels and lead times are verifiable |
| O6: Demonstrate engineering quality | Versioned Git repository, tests, runbook and reproducible demo |

## 6. MVP scope
**Included:** CSV ingestion, data-quality validation, battery/operating monitoring from available signals, exploratory anomaly detection, independently evaluated laboratory PMSM fault classification, readable explanations, read-only replay UI.

**Deferred:** Live vehicle integration, other component-specific diagnosis without relevant datasets, battery SOH/RUL where ground truth is absent, validated future-failure estimates until the external labels have been reviewed.

**Excluded:** Automatic control or repair, replacement for OEM safety systems, guaranteed vehicle-brand coverage, clinical/safety certifications or advice to work on high-voltage components.

## 7. Constraints and operating assumptions
- SCUT provides real passenger-EV telemetry; available fields are restricted to publisher-documented signals. Verified failure dates are not supplied in the selected SCUT data.
- PMSM is a labeled lab-system dataset and cannot directly demonstrate performance on road-going EVs.
- Sensor availability, units and diagnostic access vary by vehicle.
- Open third-party data may be analyzed under applicable source terms; archives are not committed to the repository.
- Implementation starts with offline CSV/replay and never claims continuous live monitoring before integration.

## 8. Acceptance criteria for MVP
1. A third party can set up the environment and reproduce all published results from documented data sources.
2. Raw-data provenance, schema, units, missingness, non-finite values, timestamp issues and known data gaps are recorded.
3. Monitoring outputs reflect measured signals and operating context, with alert limitations clearly shown.
4. PMSM metrics, if included, use documented independent evaluation and include class-wise results.
5. The dashboard distinguishes **observed measurement**, **statistical anomaly**, **model hypothesis** and **confirmed fault**.
6. No automatic actuation or autonomous repair is implemented.
7. Tests pass on the main branch, and repository documentation reflects actual project status.

## 9. Completion decision
**Phase 1 — Ideation & Project Planning: COMPLETE (2026-10-16).** The vision, use cases, MVP boundaries, architecture, data strategy, evaluation requirements, milestones and principal risks are defined. Dataset empirical quality and model results remain delivery tasks under later phases, not unfinished planning.
