# HealthCar

**Electric Vehicle Health Monitoring and Predictive Maintenance System**

HealthCar is a research-oriented, read-only decision-support prototype for passenger battery-electric vehicles. It processes available vehicle telemetry, explores anomalous operating patterns, and studies fault diagnosis with appropriately labeled component data. Predictive maintenance is a **conditional research workstream**, evaluated only when verified historical failure data support it.

**Project phase:** Planning baseline approved; dataset characterization in progress.  
**Latest verified progress:** Local SCUT and PMSM downloads plus preliminary audit completed; full source coverage and data-quality findings pending.

## Start here

- [Project charter](docs/project_charter.md) — final problem definition, scope, goals and success criteria.
- [Project plan](docs/project_plan.md) — stages, deliverables, acceptance gates and dependencies.
- [Progress tracker](docs/progress_tracker.md) — dated evidence log and task checkboxes.
- [System requirements](docs/system_requirements.md) — functional and nonfunctional requirements.
- [Architecture](docs/architecture.md) — modules, data flow and boundaries.
- [Data requirements](docs/data_requirements.md) and [dataset feasibility](docs/dataset_feasibility.md).
- [Evaluation protocol](docs/evaluation_plan.md), [research sources](docs/references.md) and [repository conventions](docs/repository_conventions.md).

## Research tracks

| Track | Primary dataset | Objective | Evidence boundary |
|---|---|---|---|
| Vehicle telemetry | SCUT passenger EV #1; optional #7 | Data characterization, monitoring and exploratory anomaly detection | No published verified future-failure labels |
| Inverter diagnostics | Zenodo PMSM inverter fault dataset | Experimental supervised classification | Laboratory system; requires leakage-safe validation |
| Battery early warning | Zhang et al. (2023) processed EV charging data | Conditional future-risk research | Separate label, licensing and prediction-horizon review |

## Repository structure

```text
docs/                 Approved plan, requirements, architecture and evaluation
notebooks/            Dataset exploration (01 SCUT, 02 PMSM)
scripts/              Local dataset acquisition and audit
src/healthcar/        Reusable Python utilities
tests/                Unit tests on synthetic fixtures
data/raw/             Local source archives (Git-ignored)
data/processed/       Local intermediate datasets (Git-ignored)
data/reports/         Generated audit reports (Git-ignored)
.github/workflows/    Automated tests
```

## Quick start (Windows, Python 3.10+)

Download this repository, extract it, open Command Prompt in the project directory, then run:

```bat
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe scripts\download_data.py
.venv\Scripts\python.exe scripts\run_audit.py --dataset both
.venv\Scripts\python.exe -m jupyter notebook
```

Windows helpers: `scripts/setup_windows.bat` and `scripts/start_notebooks_windows.bat`. For subsequent sessions, only the final Jupyter command is needed. In Jupyter, open `notebooks/01_scut_data_audit.ipynb`.

**Data distribution:** Third-party datasets and generated reports are not tracked by Git. Download them from original publishers using `scripts/download_data.py` and review the [source registry](docs/dataset_feasibility.md). Record dataset provenance and redistribution conditions before sharing raw data.

**Research integrity:** An anomaly score is not a diagnosed fault. Model performance is not claimed without an independent test set. This project does not control vehicle hardware or replace professional inspection.

## License and citations

Dataset ownership and terms remain with the original publishers. See [References](docs/references.md) for source links and DOI records. No software license has been selected yet; until a license is added, source reuse is not automatically authorized.
