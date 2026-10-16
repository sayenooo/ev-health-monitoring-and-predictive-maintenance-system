# System Requirements Specification — HealthCar
**Document ID:** HC-SRS-001 · **Version:** 1.0 · **Baseline:** 2026-10-16

## Actors and environment
**Primary actor:** BEV owner. **Research/maintenance actor:** project developer maintaining datasets, ML models and evaluation artifacts.

**Runtime:** Local offline historical CSV / sensor replay; web-based read-only dashboard. A future supported live interface is explicitly outside the initial release.

## Functional requirements
| ID | Requirement | Priority | Acceptance evidence |
|---|---|---|---|
| FR-01 | Import officially documented source datasets from configurable local paths | Must | Successfully import selected source table and report provenance |
| FR-02 | Validate schema, types, timestamps, missing and non-finite values | Must | Machine-readable audit report |
| FR-03 | Compute descriptive operating and battery indicators from documented inputs | Must | Reproducible feature functions with unit tests |
| FR-04 | Separate charging/driving context where `charging_signal` is valid | Must | Traceable context labels or unknown-code status |
| FR-05 | Visualize recorded signals and variation over time | Must | Dashboard plot from real data/replay |
| FR-06 | Generate context-aware anomaly indicators with supporting evidence | Must | Repeatable baseline and documented limitations |
| FR-07 | Display clear alert states: available, unavailable, anomalous and unconfirmed | Must | UI examples and tests |
| FR-08 | Classify PMSM lab fault labels using supervised model where justified | Should | Independent test evaluation and class explanations |
| FR-09 | Explain which measured features contributed to a model warning | Should | Explanation tied to model outputs and input fields |
| FR-10 | Provide safe, non-autonomous next-step recommendations | Should | Text guidance with uncertainty and no actuation |
| FR-11 | Record reproducible outputs and experiment configurations | Must | Reports and run instructions |
| FR-12 | Estimate future failure risk only after labeled-horizon feasibility gate | Could | Separate approved data/evaluation protocol |

`Must` requirements define MVP; `Should` define target completeness; `Could` is conditional.

## Nonfunctional requirements
| ID | Requirement | Verification |
|---|---|---|
| NFR-01 | Reproducibility | Fresh checkout + published requirements reproduce audit / model runs |
| NFR-02 | Data provenance | Every source has URL, citation, selected files, version and restrictions |
| NFR-03 | Evaluation validity | No inadvertent sharing of time windows or lab sessions across splits |
| NFR-04 | Operational safety | No writing to vehicle hardware, ECU, BMS or control buses |
| NFR-05 | Transparency | Distinguish direct sensor readings from estimates and model hypotheses |
| NFR-06 | Data minimization | Avoid uploading raw third-party telemetry or secrets to GitHub |
| NFR-07 | Maintainability | Cohesive modules, snake_case Python paths and automated smoke tests |
| NFR-08 | Resource practicality | First data-audit workflow works with a defined row limit on a Windows laptop |
| NFR-09 | Robustness | Corrupt or missing source files produce actionable error messages |
| NFR-10 | Portability | Supported Python environment and install instructions documented |

## Requirement traceability
FR-01–04, FR-11 → M2/M3; FR-05–07, FR-09–10 → M4/M6; FR-08 → M5; FR-12 → M7.

## Safety boundary
The system is informational and research-oriented, does not interpret every unusual observation as a fault and does not replace professional vehicle diagnostics.
