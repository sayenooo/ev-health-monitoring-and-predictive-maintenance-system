# Research Sources — HealthCar
**Document ID:** HC-REF-001 · **Version:** 1.1 · **Reviewed:** 2026-10-16

## Primary scientific and prediction dataset
**Zhang, J., Wang, Y., Jiang, B., et al. (2023).** Realistic fault detection of li-ion battery via dynamical deep learning. *Nature Communications*, 14, 5940.  
Article DOI: https://doi.org/10.1038/s41467-023-41226-5  
Processed source data DOI: https://doi.org/10.6084/m9.figshare.23659323  
Authors' model code: https://github.com/962086838/Battery_fault_detection_NC_github

The publisher reports three collections comprising over 690,000 charging snippets from 347 EVs. Vehicle-level battery-fault labels were reported by drivers and confirmed by engineers; near-failure data were excluded in the article's early-detection setup. Figshare lists approximately 1.38 GB of processed data, CC BY 4.0. **Research feasibility gate:** actual file-level labels and event chronology must be audited; this summary does not establish an exact N-day forecast target or a proven model outcome for HealthCar.

## Supporting real EV telemetry (not prediction labels)
**Translab-SCUT.** Electric vehicle operation data.  
https://github.com/Translab-SCUT/Electric-vehicle-operation-data

Published real-world battery/vehicle telemetry is useful for feature analysis and exploratory sensor studies. The selected SCUT data do **not** establish verified future failure labels. Publisher-level total-record estimates are not necessarily equal to the local reader's selected-table row count.

## Optional experimental fault-classification research
**PMSM inverter fault-diagnosis dataset (Zenodo record 14482932).**  
https://zenodo.org/records/14482932  
DOI: https://doi.org/10.5281/zenodo.14482932

Contains lab inverter-driven permanent-magnet synchronous motor operating/fault conditions. Can support a separate supervised classification example; **not** direct validation of future road-vehicle faults.

## Use and reporting rules
- Cite primary paper and original data record with their DOIs.
- Record downloaded archive checksums and data versions in M2.
- Follow dataset licenses; keep third-party archives outside Git.
- Keep published results distinct from outcomes personally reproduced by the HealthCar experiment.
