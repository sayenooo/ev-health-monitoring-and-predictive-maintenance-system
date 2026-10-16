# Evaluation Protocol — HealthCar
**Document ID:** HC-EVL-001 · **Version:** 1.0 · **Baseline:** 2026-10-16

This document defines the **methodology**, not measured model performance.

## Gate 1: dataset eligibility
1. List every file in each official archive and record extraction path/version.
2. Verify actual schema, columns, source units, row counts and any embedded metadata.
3. Record missingness, +inf/-inf, duplicate timestamps, gaps, impossible values and mode codes.
4. Reconcile selected SCUT source-table row counts with the publisher's stated vehicle total.
5. Identify true PMSM recording/session IDs or document inability to construct a defensible group split.

**Required result:** accepted data source inventory and documented exceptions before models.

## Track A — SCUT monitoring / anomaly research
- Fit a context-aware transparent baseline (e.g., robust conditional signal range) on an earlier time period.
- Where justified, compare a representative unsupervised model such as Isolation Forest.
- Keep training/testing chronological; prevent overlap across split boundaries.
- Present alert rate per observation and per available operating time, persistence, and sensitivity to conditions/thresholds.
- Assess plausibility through expert/feature review and separately labeled synthetic stress tests when needed.
- **Prohibited claim:** real-world fault-classification F1/recall from unlabeled SCUT records.

## Track B — PMSM laboratory supervised fault classification
- Identify `FDD` label definitions, class distributions, raw versus engineered predictors and possible label proxies.
- Inspect session/time/operating-condition metadata and block leakage from correlated adjacent samples.
- Majority-class dummy baseline; compare logistic regression and tree-based model where reasonable.
- Independent holdout with group/recording separation where available; record limitations if only time-blocking feasible.
- Report macro-F1, per-class precision/recall, class supports, normalized and raw confusion matrix.
- Label all figures and metrics as **laboratory PMSM experimental results**, not production-vehicle performance.

## Track C — conditional real-EV early warning
**Eligibility:** documented vehicle-level fault labels, pre-event history, defined lead-time window, and vehicle/time-disjoint holdout.

If eligible, pre-register evaluation horizon; report PR-AUC, false alarms per vehicle-time, class-wise recall and advance warning lead time, including model limitations. If ineligible, record **NO-GO** and retain monitoring-only scope.

## Reproducibility policy
- Fixed seeds where stochastic procedures are used; software versions recorded.
- Versioned split specifications; transformations fitted only on training observations.
- Persist model/configuration metadata and link reports to code commits.
- Separate exploratory/validation/test data to avoid threshold selection on the final test set.
- Never present a plot, warning or statistical pattern as a confirmed maintenance diagnosis without its supporting ground truth.

## Application verification
- Data unavailable vs invalid reading vs anomaly vs diagnosed fault clearly separated.
- All alerts point to source signals and preserve model uncertainty.
- Output is advisory only. No automotive actuation or high-voltage repair instructions.
