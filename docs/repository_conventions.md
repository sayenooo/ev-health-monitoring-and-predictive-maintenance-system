# Repository Conventions — HealthCar
**Document ID:** HC-ENG-001 · **Version:** 1.0

## Names and paths
- **Repository slug:** `ev-health-monitoring-and-predictive-maintenance-system` (GitHub kebab-case).
- **Product:** `HealthCar` (proper noun); **package:** `healthcar` (lowercase).
- **Python modules, functions, scripts and Markdown filenames:** `snake_case`.
- **Notebooks:** `NN_topic_description.ipynb` with zero-padded step number, such as `01_scut_data_audit.ipynb`.
- **Tests:** `test_<module>.py`; test functions `test_<behavior>`.
- **Data:** use `raw/`, `processed/`, `reports/` under `data/`, never commit originals.
- **Documentation:** stable document ID `HC-...-001`, version, revision date; no parallel competing roadmaps.
- **Git commit subjects:** conventional, concise imperative, e.g. `docs: finalize requirements`, `fix: validate non-finite values`.
- **Language:** professional, concise English for repository documents, comments and artifact captions; user-facing instructions may be translated separately.

## Source-data handling
No large source archives or proprietary raw measurements in Git. Put links to publisher pages in `docs/references.md`. Export reproducible derived artifacts only with clear licensing, data/label provenance and ethical limitations.

## Milestone governance
`docs/progress_tracker.md` is the single editable progress ledger. Before checking a task, add the specific evidence and date. The PDF v1.0 is a fixed baseline snapshot, not an automatically synchronized online tracker.

## Evidence and result nomenclature
Use **observed signal**, **statistical anomaly**, **model prediction**, **diagnosed fault** only when the corresponding evidence supports the term. Avoid production-readiness or generalized safety claims from laboratory/synthetic data.
