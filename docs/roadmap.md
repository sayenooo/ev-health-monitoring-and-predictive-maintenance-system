# Development Roadmap

| Phase | Scope | Exit criteria |
|---|---|---|
| 1. Ideation and datasets | vision, feasibility, data requirements | source links and measurable MVP defined |
| 2. Statistical audit | obtain SCUT #1/PMSM, inspect schema, gaps and classes | reproducible JSON/CSV reports |
| 3. Preprocessing / EDA | data cleaning, operating modes, feature plots | no unexplained missingness or leakage |
| 4. Monitoring baseline | rules and optional anomaly model | chronologically valid diagnostics + stable alert volume |
| 5. Lab fault classifier | PMSM supervised baselines | leakage-aware macro-F1 / class recall |
| 6. Integration | backend, read-only replay, driver-facing dashboard | end-to-end demo with traceable evidence |
| 7. Research extension | labeled real-EV battery faults | validated forward-looking metrics if feasible |

Current focus: **Phases 1–2**, not premature model-accuracy claims.
