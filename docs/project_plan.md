# HealthCar — Practical Project Plan
**Project:** AI-Powered Electric Vehicle Health Monitoring & Predictive Maintenance System  
**Status updated:** 2026-10-16  
**Current checkpoint:** Stage 2 — understand the downloaded datasets (before model training).

> **North star:** Monitor available EV signals → detect abnormal behavior → predict future faults **only when verified failure histories exist** → explain findings and recommend non-autonomous actions.

## 0. The problem in plain English
Imagine a car continuously reporting voltage, temperature, charge and movement. HealthCar takes that raw telemetry, checks whether readings are trustworthy, visualizes how values change over time, flags potentially unusual behavior, and eventually helps the owner interpret the evidence. The code does **not** repair or control the car.

**Dataset A: SCUT passenger EV** — authentic driving/battery signals; used for health monitoring and anomaly exploration. No validated future-failure labels.

**Dataset B: PMSM inverter** — experimental laboratory motor/inverter sensor data with fault labels; used for a separate supervised classifier. It cannot be represented as proven real-vehicle diagnosis.

## 1. Official milestones (do not jump ahead)

### Stage 1 — Ideation & Planning (initial draft DONE)
- [x] Define problem, goal, target users and non-autonomous scope.
- [x] Document initial MVP and data requirements.
- [x] Select SCUT and PMSM as candidate datasets; record limitations.
- [ ] Revisit feasibility after actual data inspection.
**Evidence:** `docs/project_vision.md`, `docs/data_requirements.md`, `docs/dataset_feasibility.md`.

### Stage 2 — Dataset Acquisition & Understanding (CURRENT)
- [x] Create local Python environment and install dependencies.
- [x] Download and extract SCUT #1 and PMSM on Windows (confirmed by user's console log).
- [x] Generate preliminary audit reports on the selected source tables.
- [ ] Open `notebooks/01_scut_data_audit.ipynb` and execute the first **two code cells**.
- [ ] Confirm the exact SCUT file, row/column counts, source columns and operating modes.
- [ ] Run the remaining SCUT EDA cells and inspect missingness, gaps and distributions.
- [ ] Open `notebooks/02_pmsm_data_audit.ipynb`; verify target `FDD`, classes, infinities and whether recordings can be split independently.
- [ ] Compare what the archives contain versus what our discovery script selected; don't assume one CSV equals all published source data.
- [ ] Write a short, evidence-based dataset suitability decision.

**Exit criteria:** We can describe every chosen feature in plain language, understand missing/non-finite data, and know what kind of ML target each dataset actually supports.

### Stage 3 — Preprocessing & EDA (NOT STARTED)
- [ ] Choose a leakage-safe split (time/vehicle or experiment groups).
- [ ] Define handling of missing, infinite, physically implausible and duplicate readings.
- [ ] Validate sensor units, power-current sign and sample gaps.
- [ ] Engineer meaningful derived variables (voltage and temperature spreads).
- [ ] Produce reproducible, labeled plots and a data quality report.

**Exit criteria:** Clean, documented training and evaluation tables, without silently inventing readings.

### Stage 4 — Battery/EV Monitoring Baseline (NOT STARTED)
- [ ] Start with simple contextual statistical rules.
- [ ] If justified, try Isolation Forest as a comparison.
- [ ] Measure alert frequency and stability under charging/driving modes.
- [ ] Show evidence for alerts without calling anomalies confirmed failures.

**Exit criteria:** Defensible monitoring baseline and honest limitations.

### Stage 5 — PMSM Fault Classification (NOT STARTED)
- [ ] Check laboratory labels F0–F8 and recording/session groups.
- [ ] Compare majority baseline, logistic regression and Random Forest.
- [ ] Prevent train/test leakage across adjacent samples or sessions.
- [ ] Report macro-F1, per-class recall and confusion matrix.

**Exit criteria:** Reproducible laboratory fault classifier (not falsely advertised as on-road validated).

### Stage 6 — HealthCar User Interface & Integration (NOT STARTED)
- [ ] Implement read-only telemetry replay and model endpoints.
- [ ] Build simple dashboard: sensor overview, trends and contextual alerts.
- [ ] Explain model output, data availability, uncertainty and safe next steps.
- [ ] Add tests, run instructions and a demo.

**Exit criteria:** A running end-to-end portfolio prototype with clearly identified research limitations.

### Stage 7 — True Predictive Maintenance (CONDITIONAL RESEARCH)
- [ ] Audit a real-EV dataset with verified historical failure dates.
- [ ] Choose a defensible prediction horizon and independent validation.
- [ ] Evaluate false alarms, recall and early warning lead time.
- [ ] Include in HealthCar only if the results substantiate the claim.

**Not a prerequisite for the first monitoring MVP.**

## 2. EXACT NEXT ACTION — one small task
The local setup succeeded; **do not reinstall packages or download again.**

1. If Jupyter is already open, keep it. Otherwise open Windows CMD and enter:
   ```bat
   cd /d C:\pp\ev-health-monitoring-and-predictive-maintenance-system-main
   .\.venv\Scripts\python.exe -m jupyter notebook
   ```
2. In the browser open `notebooks/01_scut_data_audit.ipynb`.
3. Run only the **first code cell** (imports) with **Shift+Enter**. Expected: it prints the project root path and has no red traceback.
4. Run only the **second code cell** (starts with `KIND = "scut1"`). Expected: selected file path, table shape, first five records and candidate table list.
5. Save the notebook. Share **those two output areas** or the exact text of any error. We will interpret what each field means before running more cells.

## 3. Important concepts
- **Data acquisition:** downloading data.
- **Data audit:** checking what is present, missing, invalid or inconsistent.
- **EDA:** exploring what measured values look like, before making ML decisions.
- **Preprocessing:** turning raw data into reliable model inputs.
- **Training:** learning statistical patterns from training data.
- **Evaluation:** testing on separate held-out data.
- **Dashboard:** a human-readable view of observed signals and model evidence.

## 4. What has actually happened on the user's Windows machine
Console output confirms Python dependencies installed, ZIP archives extracted, basic reports written and Jupyter launched. The preliminary selected-table reports showed **81,898 SCUT rows** and **10,892 PMSM rows** with zero exact duplicates in those selected tables. These counts are *not* proof that the original publications contain only this many rows: other source files and audit report details have not been independently inspected here. A RuntimeWarning in PMSM statistics suggests non-finite values requiring inspection. Updated audit code in GitHub handles these more clearly; local copies require syncing before re-running.

**No neural networks, monitoring baseline, fault predictor or dashboard have been trained or completed yet.**
