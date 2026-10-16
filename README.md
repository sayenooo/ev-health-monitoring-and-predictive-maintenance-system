# HealthCar

**Electric Vehicle Health Monitoring and Predictive Maintenance System**

**Course:** Big Data Analysis and Prediction Project (BDAPP)  
**Project type:** Applied machine learning and time-series prediction  
**Planning baseline:** v2.0 (2026-10-16) — **IDEATION COMPLETE**  
**Current execution phase:** M2 — Data and prediction-target feasibility

## Project objective

Develop a machine learning-based system that **continuously monitors electric vehicle health using sensor data, detects abnormal operating conditions, predicts potential future failures, and provides early warnings to support preventive maintenance**.

**Monitoring and predictive maintenance are both core requirements.** HealthCar targets EV health as a system-level concept; only components with appropriate observed signals and validated targets can be evaluated empirically.

## Operating concept

```text
EV telemetry (time-ordered observations)
                  |
           Quality validation
                  |
         Rolling history windows
                  |
        +---------+----------+
        |                    |
        v                    v
Current-health /        Future-risk model
anomaly model          (labeled event data)
        |                    |
        +---------+----------+
                  |
         Evidence-based alerts
                  |
     Results, metrics, interpretation
```

For BDAPP, continuous operation is demonstrated by **replaying historical telemetry sequentially** and scoring each new observation/window. This is *continuous inference*, not a claim of a working live OBD-II link or continuous online training.

## Core ML questions
1. Can time-series EV sensor signals reveal deviations from normal operating behavior?
2. Can historical measurements identify elevated risk of a future fault **before** its documented occurrence?
3. How reliable are anomaly scores and future-risk predictions on independent data?
4. How can evidence, uncertainty and early-warning lead time be communicated clearly?

## Data strategy

| Data source | Role | Evaluation boundary |
|---|---|---|
| [SCUT EV operation data](https://github.com/Translab-SCUT/Electric-vehicle-operation-data) | **Monitoring track**: real-world EV telemetry and anomaly analysis | No verified future-failure labels in this source |
| [Zhang et al. 2023 processed EV battery-fault histories](https://doi.org/10.6084/m9.figshare.23659323) | **Predictive track candidate**: historical charging signals and confirmed fault outcomes | Need to verify timestamps, vehicle IDs, available horizon and label definition |
| [PMSM inverter-fault dataset](https://zenodo.org/records/14482932) | Optional component-level fault-classification study | Laboratory present-state fault labels, not verified on-road future failures |

Different datasets support different experiments; they are not merged into one table without valid shared measurements and targets.

## BDAPP deliverables
- Source and prediction-label feasibility analysis
- EDA, data quality assessment and time-aware preprocessing
- Rolling-window feature engineering and dataset partition design
- **Model A: health monitoring / anomaly detection**
- **Model B: future fault-risk prediction**, validated against historical events
- Baseline comparisons, precision/recall, PR-AUC, false alarm analysis and lead-time analysis where measurable
- Sequential telemetry replay showing updated status and alerts
- Reproducible notebooks, evaluation report and final presentation

**Not the project focus:** accounts, bookings, a full web app, backend business workflows, vehicle control or automatic repairs.

## Repository contents
- [Project charter](docs/project_charter.md) — fixed goal, research questions and MVP
- [Project plan](docs/project_plan.md) — work breakdown and gates
- [Progress tracker](docs/progress_tracker.md) — milestone status and evidence
- [System requirements](docs/system_requirements.md)
- [ML architecture](docs/architecture.md)
- [Data requirements](docs/data_requirements.md)
- [Dataset feasibility](docs/dataset_feasibility.md)
- [Evaluation protocol](docs/evaluation_plan.md)
- [Research references](docs/references.md)
- [Naming conventions](docs/repository_conventions.md)

## Getting started

This repository currently includes scripts for downloading **supporting** SCUT/PMSM datasets and performing their first audits. The real-EV prospective-fault data have **not yet been downloaded or audited**.

```bat
cd /d C:\pp\ev-health-monitoring-and-predictive-maintenance-system-main
.venv\Scripts\python.exe scripts\download_data.py
.venv\Scripts\python.exe scripts\run_audit.py --dataset both
.venv\Scripts\python.exe -m jupyter notebook
```

For a fresh setup, run `scripts/setup_windows.bat` first. Data files and locally produced reports remain under Git-ignored `data/` folders. Do not present observed anomalies as confirmed failures, or estimate a time-to-failure horizon without matching timestamps.
