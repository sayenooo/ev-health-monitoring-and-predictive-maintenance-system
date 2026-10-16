# Dataset Feasibility — Prediction-First Research
**Document ID:** HC-DAT-002 · **Version:** 1.1 · **Baseline:** 2026-10-16

## Priority 1: processed real-EV charging histories and confirmed battery faults
**Source:** Zhang et al. (2023) "Realistic fault detection of li-ion battery via dynamical deep learning," Nature Communications.  
**Dataset:** https://doi.org/10.6084/m9.figshare.23659323  
**Publisher scope:** 3 datasets, >690,000 charging snippets from 347 EVs, 1.38 GB downloadable. Vehicle-level labels were based on driver reports and engineer confirmation; near-fault samples were deliberately excluded by the study. <The paper does not guarantee an event timestamp suitable for a new N-day failure target.>

**Proposed ML unit:** a vehicle, with a history of snippets grouped without future leakage.  
**Proposed y:** confirmed faulty/non-faulty EV as provided by actual published labels.  
**Mandatory M2 audit:** inspect file types, label encoding, missingness, vehicle IDs, time ordering, event timing, restrictions and previously defined splits. If time-to-event information is unavailable, classify risk from earlier data rather than claim failure date forecasts.

## Priority 2: SCUT real passenger-EV telemetry
**Source:** https://github.com/Translab-SCUT/Electric-vehicle-operation-data  
**Purpose:** supporting EV signal profiling, temporal feature experimentation and methodology demonstration. **No confirmed future battery-fault labels in selected SCUT source.**
**Local status:** SCUT #1 archive already downloaded. The existing audit selected a table with 81,898 rows, which has not yet been reconciled with all archive contents / source publication counts.

## Priority 3: laboratory PMSM inverter-fault classification (optional)
**Source:** https://zenodo.org/records/14482932  
**Purpose:** supervised **present-state** lab-condition classification only, not future vehicle breakdown prediction.  
**Local status:** archive downloaded and one selected table audited with 10,892 records; non-finite values flagged for review.

## Dataset-governance decision
The research claim must follow the supported ground truth, **not** the project title. A multi-component universal failure predictor is outside scope without independent future-failure labels. This is a dataset feasibility boundary, not an intent to build a vehicle monitoring platform.

## Next actions
- [ ] Inspect Figshare data structure, available labels, vehicle grouping and timestamps.
- [ ] Decide early-risk target and exact input observation window.
- [ ] Define split by vehicle and evaluation approach.
- [ ] Update experimental target declaration and proceed to EDA.

Original data are stored locally and not committed to Git.
