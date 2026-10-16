# Dataset Feasibility and Source Registry
**Document ID:** HC-DAT-002 · **Version:** 1.0 · **Baseline:** 2026-10-16

## Dataset selection decision
Three independent research purposes are supported by different kinds of evidence; they must not be merged as if drawn from one instrumentation platform.

| Source | Primary intended use | Feasibility | Next validation |
|---|---|---|---|
| SCUT passenger EV #1 | Pack/cell summary monitoring and operating context | Selected for M2/M3 | Reconcile archive files, timestamps, columns and units |
| PMSM inverter lab dataset | Labeled experimental fault classification | Selected for M2/M5 | Verify `FDD` and group/session splits, check infinity |
| SCUT passenger EV #7 | Cross-vehicle/chemistry exploratory comparison | Optional | Size/resources and cross-vehicle signal consistency |
| Zhang et al. 2023 Figshare | Real-EV battery early warning | Conditional M7 | Verify actual labels and prediction horizon |

## Source A: SCUT EV operational data
Original: https://github.com/Translab-SCUT/Electric-vehicle-operation-data  
Vehicle #1: https://github.com/Translab-SCUT/Electric-vehicle-operation-data/blob/main/vehicle%231.zip  
Vehicle #7: https://github.com/Translab-SCUT/Electric-vehicle-operation-data/blob/main/vehicle%237.zip

Publisher-reported vehicle #1 total: **954,754 data points**. On 2026-10-16, the local discovery/audit tool reported **81,898 rows in its selected source table**. This discrepancy is **unresolved** until all extracted files are inventoried and source-table selection is verified. Neither number should be represented as the independently verified complete number of loaded rows across the archive.

Monitoring features require actual column-unit verification and timestamps. Source does not expose verified future failure dates for supervised predictive maintenance.

## Source B: PMSM inverter fault records
Original: https://zenodo.org/records/14482932  
Archive: `PMSM-inverter-fault-diagnosis-3.0.zip`; publisher describes 10,892 samples across nine operational conditions. The local audit reported 10,892 selected-table rows with zero exact duplicates but emitted warnings consistent with non-finite numeric values. Confirm their precise counts with the corrected audit and inspect metadata for session boundaries before modeling.

This is **experimental PMSM hardware**, not an on-road passenger-EV fault history.

## Source C: future battery early-warning
Article: https://doi.org/10.1038/s41467-023-41226-5  
Processed records: https://doi.org/10.6084/m9.figshare.23659323

The article discusses confirmed vehicle-level faults in historical charging records. A successful reproduction requires exact label/split/horizon review. **Do not include predictive accuracy claims in MVP without this review.**

## M2 exit checks
- [ ] Enumerate all raw extracted source files and archive metadata.
- [ ] Verify selected tabular files, shapes and unique vehicle identifiers.
- [ ] Confirm units, encoding, type conversions, time ordering and sampling gaps.
- [ ] Quantify missing values, infinity and out-of-range sensor values.
- [ ] Confirm PMSM target mapping and independent recording groups.
- [ ] Produce a short decision memo declaring the specific usable fields and model targets.

## Source governance
Raw archives stay in ignored local `data/raw/` directories. Link publications and dataset pages; verify licensing/redistribution terms before any third-party data sharing.
