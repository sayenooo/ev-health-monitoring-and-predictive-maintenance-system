"""Transparent dataset discovery, basic quality reports, and conservative EV features."""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np
import pandas as pd

SCUT_FIELDS = [
    "Time", "vhc_speed", "charging_signal", "vhc_totalMile",
    "hv_voltage", "hv_current", "bcell_soc",
    "bcell_maxVoltage", "bcell_minVoltage",
    "bcell_maxTemp", "bcell_minTemp",
]
PMSM_SENSORS = ["ia", "ib", "vdc", "idc", "t1", "t2", "t3", "vd"]
EXTENSIONS = {".csv", ".txt", ".tsv", ".xlsx", ".xls"}


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read_table(path: Path, nrows: int | None = None) -> pd.DataFrame:
    """Read ordinary tabular formats with a conservative encoding fallback."""
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path, nrows=nrows)
    for enc in ("utf-8-sig", "gb18030", "latin-1"):
        try:
            frame = pd.read_csv(path, nrows=nrows, encoding=enc,
                                sep=None, engine="python")
            if frame.shape[1] > 1:
                return frame
        except (UnicodeError, pd.errors.ParserError, ValueError):
            pass
    return pd.read_csv(path, nrows=nrows, sep=r"\s+",
                       engine="python", encoding="latin-1")


def discover_dataset(kind: str, raw_root: Path | None = None) -> tuple[Path, list[dict]]:
    folders = {"scut1": "scut_vehicle1", "scut7": "scut_vehicle7", "pmsm": "pmsm"}
    if kind not in folders:
        raise ValueError(f"Unsupported dataset: {kind}")
    root = raw_root if raw_root is not None else project_root() / "data" / "raw"
    folder = root / folders[kind]
    if not folder.exists():
        raise FileNotFoundError(f"Not found: {folder}. Run python scripts/download_data.py --only {kind}")
    candidates = []
    for path in folder.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS or path.stat().st_size <= 32:
            continue
        try:
            head = _read_table(path, nrows=6)
            cols = {str(c).strip().lower() for c in head.columns}
            matched = len(cols.intersection(
                {c.lower() for c in SCUT_FIELDS} if kind.startswith("scut") else set(PMSM_SENSORS)
            ))
            labeled = bool(cols.intersection({"fdd", "label", "fault_label"}))
            score = matched * 10 + (30 if kind == "pmsm" and labeled else 0)
            candidates.append({"path": str(path), "matched_features": matched,
                               "has_label": labeled, "score": score,
                               "columns": list(map(str, head.columns))})
        except Exception as exc:
            candidates.append({"path": str(path), "matched_features": 0,
                               "score": -1, "error": str(exc)[:250]})
    candidates.sort(key=lambda x: x["score"], reverse=True)
    if not candidates or candidates[0]["matched_features"] < (3 if kind.startswith("scut") else 2):
        raise RuntimeError(f"No recognizable {kind} dataset in {folder}; inspect raw ZIP structure.")
    return Path(candidates[0]["path"]), candidates


def read_dataset(kind: str, max_rows: int | None = 250_000,
                 raw_root: Path | None = None) -> tuple[pd.DataFrame, Path, list[dict]]:
    source, options = discover_dataset(kind, raw_root)
    frame = _read_table(source, nrows=max_rows)
    frame.columns = [str(c).strip() for c in frame.columns]
    return frame, source, options


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Simple signals for analysis, not confirmed fault or safety thresholds."""
    out = df.copy()
    for hi, lo, target in [
        ("bcell_maxVoltage", "bcell_minVoltage", "cell_voltage_spread_V"),
        ("bcell_maxTemp", "bcell_minTemp", "cell_temperature_spread_C"),
    ]:
        if hi in out and lo in out:
            out[target] = (pd.to_numeric(out[hi], errors="coerce")
                           - pd.to_numeric(out[lo], errors="coerce"))
    if {"hv_voltage", "hv_current"}.issubset(out.columns):
        out["battery_power_W_unverified_sign"] = (
            pd.to_numeric(out["hv_voltage"], errors="coerce")
            * pd.to_numeric(out["hv_current"], errors="coerce")
        )
    return out


def audit(kind: str, df: pd.DataFrame, path: Path,
          max_rows: int | None = None) -> dict:
    number = df.select_dtypes(include="number")
    report = {
        "dataset": kind, "selected_file": str(path),
        "rows_loaded": len(df), "columns": list(df.columns),
        "sampled_first_rows": max_rows is not None,
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_percent": df.isna().mean().mul(100).round(3).to_dict(),
        "dtype": df.dtypes.astype(str).to_dict(),
        "infinite_counts": {c: int(np.isinf(number[c]).sum()) for c in number.columns},
        "warnings": [],
    }
    if kind.startswith("scut"):
        report["missing_expected_fields"] = [c for c in SCUT_FIELDS if c not in df.columns]
        if "Time" in df:
            t = pd.to_datetime(df["Time"], errors="coerce")
            delta = t.diff().dt.total_seconds()
            positives = delta[delta > 0]
            report["time_quality"] = {
                "invalid_timestamps": int(t.isna().sum()),
                "duplicate_timestamps": int(t.duplicated().sum()),
                "negative_time_jumps": int((delta < 0).sum()),
                "median_positive_interval_s": float(positives.median()) if len(positives) else None,
                "max_positive_gap_s": float(positives.max()) if len(positives) else None,
            }
        if "charging_signal" in df:
            report["operating_codes"] = {
                str(k): int(v) for k, v in df["charging_signal"].value_counts(dropna=False).items()
            }
        for hi, lo, name in [
            ("bcell_maxVoltage", "bcell_minVoltage", "negative_voltage_spreads"),
            ("bcell_maxTemp", "bcell_minTemp", "negative_temperature_spreads"),
        ]:
            if {hi, lo}.issubset(df.columns):
                diff = pd.to_numeric(df[hi], errors="coerce") - pd.to_numeric(df[lo], errors="coerce")
                report[name] = int((diff < 0).sum())
        report["warnings"].append(
            "SCUT has no verified future-failure ground truth; anomaly flags are not diagnosed faults."
        )
    elif kind == "pmsm":
        report["label_candidates"] = [
            c for c in df if c.lower() in {"fdd", "label", "fault_label", "class", "target"}
        ]
        report["sensor_candidates"] = [
            c for c in df if c.lower() in PMSM_SENSORS
        ]
        report["class_counts"] = {
            c: {str(k): int(v) for k, v in df[c].value_counts(dropna=False).items()}
            for c in report["label_candidates"]
        }
        report["warnings"].append(
            "PMSM labels were obtained on a lab rig, not validated on passenger EVs."
        )
    if max_rows is not None:
        report["warnings"].append("This report covers only the first rows, not the entire source file.")
    return report


def write_report(kind: str, max_rows: int | None = 250_000,
                 raw_root: Path | None = None, reports_dir: Path | None = None):
    frame, path, candidates = read_dataset(kind, max_rows, raw_root)
    report = audit(kind, frame, path, max_rows)
    report["candidate_tables"] = candidates[:10]
    folder = reports_dir if reports_dir is not None else project_root() / "data" / "reports"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{kind}_audit.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
    )
    frame.isna().mean().mul(100).rename("missing_pct").to_csv(
        folder / f"{kind}_missing.csv", header=True
    )
    frame.describe(include="all").transpose().to_csv(folder / f"{kind}_summary.csv")
    return report, frame
