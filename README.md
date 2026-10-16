# HealthCar
## Machine Learning-Based Electric Vehicle Fault Prediction and Predictive Maintenance

**Course:** Big Data Analysis and Prediction Project (BDAPP)  
**Project type:** Applied machine learning research — prediction first, not a software platform.  
**Planning baseline:** v1.1 · 2026-10-16 · COMPLETE  
**Current milestone:** M2 — prediction-label and dataset feasibility audit.

### Research goal

Develop, compare and independently evaluate machine learning models that use **historical electric vehicle sensor recordings** to identify vehicles at risk of **subsequently confirmed battery faults**. The primary outcome is a reproducible predictive experiment with defensible validation, rather than a production dashboard.

### Dataset roles

| Source | Role | Supported claim |
|---|---|---|
| [Zhang et al. 2023 processed EV charging data](https://figshare.com/articles/dataset/23659323) | **Primary prediction dataset candidate** (347 EVs; vehicle-level confirmed battery problem labels) | Historical charging records used to identify at-risk vehicles; exact forecast horizon requires label/timestamp audit |
| [SCUT EV operation data](https://github.com/Translab-SCUT/Electric-vehicle-operation-data) | Supporting exploration of EV telemetry and feature engineering | Historical monitoring signals; **no verified future-fault target** |
| [PMSM inverter-fault data](https://zenodo.org/records/14482932) | Optional, separate lab fault-classification comparison | Supervised diagnosis of lab conditions; **not future vehicle-failure prediction** |

**Core prediction question:** Can historical charging telemetry distinguish EVs that later experience a confirmed battery fault from those without an observed fault, on independently held-out vehicles?

### Main ML deliverables

1. Dataset provenance, label analysis and target definition.
2. EDA, imbalance assessment and leakage-safe splits.
3. Reproducible feature engineering and temporal aggregation.
4. Baseline models (e.g., DummyClassifier / logistic regression / random forest).
5. Advanced comparison where justified (e.g., gradient boosting and a sequence model).
6. Honest out-of-sample comparison: PR-AUC, recall, precision, F1, confusion matrix, calibration and, if event timing is verified, lead time.
7. Interpretation, limitations, scientific report, presentation and clean notebooks.

**No production frontend, API, OBD hardware, automated recommendations or live-vehicle integration is required for BDAPP.** A small static visualization may help present results but is not an objective.

### Repository map

```text
docs/          charter, BDAPP plan, requirements, source feasibility, evaluation, progress
notebooks/     early supporting dataset audits (SCUT and PMSM)
scripts/       existing source download and statistical audit utilities
src/healthcar/ reusable data-audit functions
tests/         reproducibility / data-audit tests
data/          original/derived local data; Git-ignored
```

**Next step:** Audit the primary [processed fault dataset on Figshare](https://figshare.com/articles/dataset/23659323) and verify that its vehicle identifiers and labels permit the stated task. It is approximately 1.38 GB and is **not** downloaded by the existing SCUT/PMSM script. Do not train before checking the label/time semantics.

### Documents

[Project charter](docs/project_charter.md) · [Project plan](docs/project_plan.md) · [Progress tracker](docs/progress_tracker.md) · [Data requirements](docs/data_requirements.md) · [Dataset feasibility](docs/dataset_feasibility.md) · [Evaluation plan](docs/evaluation_plan.md) · [References](docs/references.md) · [Naming conventions](docs/repository_conventions.md)

### Supporting audits already executable

The existing Windows setup used `requirements.txt`, `scripts/download_data.py` and `scripts/run_audit.py` successfully for SCUT and PMSM. Those supporting datasets are locally downloaded on the user's computer; **the primary fault dataset has not yet been audited**.

Third-party datasets stay outside Git. Model quality, future-risk horizons and automotive deployment claims must never be fabricated.
