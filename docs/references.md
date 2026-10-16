# Data and Research Sources — HealthCar
**Document ID:** HC-REF-001 · **Version:** 1.0 · **Reviewed:** 2026-10-16

## 1. Real-world EV operation data (SCUT)
**Publisher:** Translab-SCUT. *Electric-vehicle-operation-data* (public research repository).  
**Primary page:** https://github.com/Translab-SCUT/Electric-vehicle-operation-data  
**Scope:** 11 published telemetry fields (timestamp; speed; charging mode; mileage; pack voltage/current; SOC; min/max cell voltage/temperature). Vehicle #1 is a passenger EV, NCM chemistry; publisher lists 954,754 data points and nominal 0.1 Hz sampling. Vehicle #7 is a passenger EV, LFP chemistry; publisher lists 5,304,111 data points at nominal 0.5 Hz. The repository presents data for 7 passenger cars and 3 buses.

**Interpretation rule:** Row totals provided by the publisher are publication-level metadata. The current local selection script identified a table with 81,898 rows from downloaded vehicle #1; this must not be silently treated as the entire published vehicle time series.

## 2. PMSM inverter fault dataset
**Creator:** Abdelkabir Bacha. *Comprehensive Dataset for Fault Detection and Diagnosis in Inverter-Driven PMSM Systems*. Zenodo record 14482932 (version described as 3.0 archive).  
**DOI:** https://doi.org/10.5281/zenodo.14482932  
**Primary page:** https://zenodo.org/records/14482932  
**Scope:** 10,892 samples, nine operating conditions, eight original sensor measurements and 15 derived features; 10 Hz experimental data. Source archive includes `raw_data`, `processed_data`, `metadata` and `code`. Fault classes pertain to a laboratory inverter-driven PMSM system.

## 3. Optional real-EV battery-fault research
**Citation:** Zhang, J., Wang, Y., Jiang, B. et al. (2023). "Realistic fault detection of li-ion battery via dynamical deep learning." *Nature Communications*, 14, 5940.  
**DOI:** https://doi.org/10.1038/s41467-023-41226-5  
**Processed data:** https://doi.org/10.6084/m9.figshare.23659323  
**Scope:** Research reports >690,000 charging snippets from 347 EVs and vehicle-level fault confirmation. Different label granularity and preprocessing require separate feasibility validation. This dataset is not part of the initial downloads.

## Source usage policy
Link to authoritative original publisher pages and record versions and hashes on local download. Do not redistribute archives or claim that the paper's reported metrics transfer directly to HealthCar. Verify data usage/licensing terms before any publication of derived assets.
