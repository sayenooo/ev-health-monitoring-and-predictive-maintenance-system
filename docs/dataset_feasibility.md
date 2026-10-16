# Data Source & Target Feasibility — HealthCar
**Document ID:** HC-DAT-002 · **Version:** 2.0 · **Baseline:** 2026-10-16

## Two mandatory evidence tracks
| Research track | Candidate source | Supports | Known limitation |
|---|---|---|---|
| A — Continuous Health Monitoring | [SCUT EV operation data](https://github.com/Translab-SCUT/Electric-vehicle-operation-data) | Real EV telemetry, current-state descriptors and anomaly analysis | Selected source lacks confirmed future faults |
| B — Predictive Maintenance | [Zhang et al. processed real EV fault dataset](https://doi.org/10.6084/m9.figshare.23659323) | Historical charging data and confirmed fault outcome labels | Verify file-level IDs, event timestamps, observation windows, future-risk semantics |
| Supplementary — Component Fault Diagnosis | [PMSM inverter fault data](https://zenodo.org/records/14482932) | Labeled laboratory operating/fault classes | Present-state laboratory classification, not future road-EV failures |

## Track A — SCUT
Source provides measured operating and battery signals (speed, mileage, charging mode, pack voltage/current, SOC, min/max cell voltages and temperatures). Local acquisition succeeded, but the reader selected a table of **81,898 records**, which must be reconciled with publisher-wide vehicle counts. The source can test repeated contextual monitoring; without verified failure labels it cannot alone validate future-fault forecasting.

## Track B — Prospective real-EV faults
Zhang et al. (2023) report a real-EV charging-data corpus with engineer-confirmed battery faults (347 EVs and >690,000 charging snippets in the published study). Data availability and precise label timing are to be audited. Determine:
1. Unit of observation (charging snippet/window/vehicle).
2. Reliable vehicle identifiers and recording chronology.
3. Whether the label represents a future confirmed event relative to the input window.
4. If a numeric early-warning horizon can be defined from fault timestamps.
5. Group- and time-disjoint split feasibility.
6. Data rights and reproducibility.

**If fixed failure dates are absent, use a properly justified future-risk/at-risk-vehicle classification outcome only if chronology and label semantics support it. Never claim a precise time-to-failure without observed event times.**

## Optional PMSM experiment
The lab inverter-fault dataset was downloaded locally; one source table had 10,892 records in the initial audit. May be used to demonstrate component fault classification, but does not replace mandatory predictive maintenance evaluation.

## Decision criterion for M2
M2 closes only after a valid real-EV monitoring source and a scientifically defensible historical-fault prediction target are documented. Where the prospective source is unsuitable, review an alternate source **without changing the project objective**.

## Data governance
Keep publisher archives in Git-ignored local data directories; cite sources, verify licenses and never treat unlabeled statistical anomalies as confirmed real failures.
