# Dataset Registry & Feasibility Audit

## Initial downloads

### A. SCUT EV Operation Data — passenger vehicle #1
- Publisher: [Translab-SCUT](https://github.com/Translab-SCUT/Electric-vehicle-operation-data)
- Direct ZIP: https://raw.githubusercontent.com/Translab-SCUT/Electric-vehicle-operation-data/main/vehicle%231.zip
- GitHub manual fallback: https://github.com/Translab-SCUT/Electric-vehicle-operation-data/blob/main/vehicle%231.zip
- Reported NCM car, 0.1 Hz nominal logging, approx. 954,754 measurements.
- Objective: real-world battery and operating-condition monitoring. **No verified future fault event labels.**
- Do not redistribute source archives in this repository; check authors' current usage terms.

### B. PMSM inverter fault diagnosis
- Record/DOI: https://zenodo.org/records/14482932
- Direct ZIP: https://zenodo.org/records/14482932/files/PMSM-inverter-fault-diagnosis-3.0.zip?download=1
- Approx. 10,892 labeled records from an experimental inverter/PMSM rig; 9 conditions including normal.
- Objective: fault classification **only in the laboratory dataset**; verify raw schema and experiment/session independence.

## Optional download

### C. SCUT passenger vehicle #7
- Direct ZIP: https://raw.githubusercontent.com/Translab-SCUT/Electric-vehicle-operation-data/main/vehicle%237.zip
- Reported LFP car, nominal 0.5 Hz, ~5.3M records. Significantly larger; opt in via `--only scut7`.
- Objective: compare operating contexts / chemistry, **not** guaranteed cross-vehicle generalization.

### D. Real battery-fault early-warning research dataset
- Paper: https://www.nature.com/articles/s41467-023-41226-5
- Data: https://figshare.com/articles/dataset/23659323
- Approx. 1.38GB processed data; **not downloaded by default**.
- Requires audit of real fault labels, prediction horizon, vehicle/time separation and data access terms.

## Feasibility matrix
| Target | Source | Status |
|---|---|---|
| Pack and cell summary monitoring | SCUT | Candidate; schema/values audit required |
| Charging/driving context | SCUT | Candidate; validate codes and sampling |
| Anomaly flags | SCUT | Exploratory unsupervised work, no failure ground truth |
| Motor/inverter fault classification | PMSM | Labeled *laboratory* work only |
| Early battery fault warning | Figshare | Conditional extension |
| SOH/RUL, motor on-road failures, brakes/tires/cooling | None in MVP | **Not supported** |

The published file descriptions are **not substitutes for inspecting downloaded archives**.
