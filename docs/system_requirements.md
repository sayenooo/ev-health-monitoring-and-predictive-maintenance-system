# Research and ML Requirements — HealthCar
**Document ID:** HC-SRS-001 · **Version:** 1.1 · **Baseline:** 2026-10-16

This specification governs an **applied ML prediction experiment** for BDAPP, not an application/backend.

## Research functional requirements
| ID | Requirement | Verification |
|---|---|---|
| ML-01 | Inventory processed EV fault source, provenance and labels | File/metadata audit |
| ML-02 | Define candidate target and temporal cutoff with no future information in features | Target specification / leakage review |
| ML-03 | Quantify class imbalance, source missingness and operating-condition coverage | EDA tables and plots |
| ML-04 | Create train/validation/test separated by vehicle | Split manifest and no overlapping vehicle IDs |
| ML-05 | Extract historical statistical and time-series features | Documented code and feature dictionary |
| ML-06 | Train naive and meaningful comparison baselines | Experiment logs |
| ML-07 | Compare a justified stronger model family | Controlled metrics on same split |
| ML-08 | Evaluate PR-AUC, precision, recall, F1, confusion matrix and false alarms | Independent test report |
| ML-09 | Document feature influence, calibration and limitations | Interpretation report |
| ML-10 | Produce reproducible notebooks, technical report and presentation | BDAPP deliverables |

## Nonfunctional research requirements
- Provenance, licensing and data-version traceability.
- No train/test leakage by vehicle, time or preprocessing fit.
- Fixed random seeds and dependency listing.
- Memory-aware processing of >1 GB research dataset.
- Clear distinction among binary vehicle-level risk, time-bounded fault prediction and present-time diagnosis.
- Never claim a numeric failure horizon without labels that support it.
- Standard names: snake_case code, numbered notebooks, versioned documentation.

## Not required for this course
User registration, backend API, dashboard/frontend, live CAN/OBD-II integration, vehicle commands, maintenance scheduling platform or automated repairs.
