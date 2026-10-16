# HealthCar 🚗⚡
### AI-Powered Electric Vehicle Health Monitoring & Predictive Maintenance System

**Status:** Phase 1 — ideation, dataset acquisition and data feasibility audit. **No trained or validated fault-prediction model is claimed yet.**

HealthCar is an explainable, **non-autonomous** research prototype for passenger battery-electric vehicles. The long-term goal is to **Monitor → Detect → Predict (when labels permit) → Recommend**, while retaining all decisions with the driver.

## What is in this repository?
| Module | Evidence | Current stage |
|---|---|---|
| EV battery / driving telemetry | [SCUT passenger EV operation data](https://github.com/Translab-SCUT/Electric-vehicle-operation-data) | First real-world monitoring source; data-quality audit |
| Inverter / motor fault classification | [PMSM inverter fault diagnosis — Zenodo](https://zenodo.org/records/14482932) | Separate laboratory dataset; labels and session leakage must be checked |
| EV battery early warning | [Zhang et al., 2023](https://www.nature.com/articles/s41467-023-41226-5) | Future research extension; not downloaded by default |
| Driver-facing dashboard | Monitoring → contextual alerts → evidence and recommendations | Planned after data audit |

**Important:** SCUT has battery telemetry but no verified future-failure labels. PMSM comes from a lab motor/inverter rig rather than production EVs. We will not pool their rows or treat anomaly scores as confirmed failures.

## Quick start — Windows (Python 3.10+)
Clone this repository (GitHub → **Code** → **Download ZIP**, or `git clone`), open the project folder, then double-click `START_HERE_WINDOWS.bat`.

Or run in PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts\download_data.py
.\.venv\Scripts\python.exe scripts\run_audit.py --dataset both
.\.venv\Scripts\python.exe -m jupyter notebook
```

Manual / selective downloads:
```bash
python scripts/download_data.py --only scut1
python scripts/download_data.py --only pmsm
python scripts/download_data.py --only scut7  # optional larger LFP EV
```
Dataset archives are stored in `data/raw/` and **not** committed. The download script checks the archive and gives official fallback links on failure. Network access is required on your machine.

## Project layout
```text
docs/            vision, sensor requirements, dataset feasibility, evaluation plan
notebooks/       01_scut_data_audit.ipynb, 02_pmsm_data_audit.ipynb
scripts/         download_data.py, run_audit.py
src/healthcar/   reusable Python audit + feature utilities
tests/           smoke tests on synthetic sample frames (not real EV results)
data/            raw/, processed/, reports/ (local; ignored by Git)
```

## Data and scientific integrity
- Respect dataset licenses and do not commit third-party archives.
- Validate units, timestamps, operating modes and charge-current sign conventions before modeling.
- SCUT is for monitoring/unsupervised exploration; no ground-truth recall/accuracy may be reported for real vehicle faults.
- PMSM metrics describe a lab rig; avoid random row splits that leak experimental sessions.
- Future event prediction requires real future-failure labels and vehicle/time-disjoint validation.
- No automated vehicle actuation, DIY high-voltage repair, or safety-critical autonomous advice.

## Documentation
Read [Project Vision](docs/project_vision.md) → [Data Requirements](docs/data_requirements.md) → [Dataset Feasibility](docs/dataset_feasibility.md) → [Evaluation Plan](docs/evaluation_plan.md).

## Research sources
- [SCUT EV operation data](https://github.com/Translab-SCUT/Electric-vehicle-operation-data)
- [PMSM inverter fault diagnosis dataset](https://doi.org/10.5281/zenodo.14482932)
- [Realistic fault detection of Li-ion battery (2023)](https://doi.org/10.1038/s41467-023-41226-5)
