from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from healthcar.audit import build_features, audit, discover_dataset


def test_derived_signals():
    df = pd.DataFrame({
        "bcell_maxVoltage": [3.9, 3.8], "bcell_minVoltage": [3.7, 3.7],
        "bcell_maxTemp": [35, 32], "bcell_minTemp": [31, 30],
        "hv_voltage": [350, 352], "hv_current": [10, -2],
    })
    features = build_features(df)
    assert round(features.loc[0, "cell_voltage_spread_V"], 5) == 0.2
    assert features.loc[0, "cell_temperature_spread_C"] == 4
    assert features.loc[1, "battery_power_W_unverified_sign"] == -704


def test_time_quality(tmp_path):
    df = pd.DataFrame({
        "Time": ["2026-01-01 10:00:00", "2026-01-01 10:00:10"],
        "charging_signal": [1, 3],
        "bcell_maxVoltage": [3.8, 3.9], "bcell_minVoltage": [3.7, 3.7],
    })
    report = audit("scut1", df, tmp_path / "example.csv", None)
    assert report["time_quality"]["median_positive_interval_s"] == 10
    assert report["negative_voltage_spreads"] == 0


def test_dataset_file_discovery(tmp_path):
    root = tmp_path / "data"
    folder = root / "scut_vehicle1"
    folder.mkdir(parents=True)
    pd.DataFrame({
        "Time": ["2026-01-01"], "hv_voltage": [350],
        "bcell_soc": [50], "bcell_maxTemp": [32],
        "bcell_minTemp": [28]
    }).to_csv(folder / "vehicle.csv", index=False)
    source, candidates = discover_dataset("scut1", root)
    assert source.name == "vehicle.csv"
    assert candidates[0]["matched_features"] >= 3

def test_partial_read_warning_only_at_limit(tmp_path):
    df = pd.DataFrame({
        "Ia": [1.0, 2.0, 3.0],
        "Ib": [2.0, 3.0, 4.0],
        "FDD": [0, 0, 1],
    })
    full = audit("pmsm", df, tmp_path / "lab.csv", max_rows=250000)
    assert full["sampled_first_rows"] is False
    assert not any("first rows" in w for w in full["warnings"])

    limited = audit("pmsm", df, tmp_path / "lab.csv", max_rows=3)
    assert limited["sampled_first_rows"] is True
    assert any("first rows" in w for w in limited["warnings"])


def test_infinities_are_detected_without_imputation(tmp_path):
    import numpy as np
    from healthcar.audit import write_report

    raw = tmp_path / "data" / "pmsm"
    raw.mkdir(parents=True)
    pd.DataFrame({
        "Ia": [1.0, np.inf, -np.inf],
        "Ib": [2.0, 3.0, 4.0],
        "VDC": [350.0, 355.0, 360.0],
        "FDD": [0, 1, 2],
    }).to_csv(raw / "sensor.csv", index=False)
    report, original = write_report(
        "pmsm", max_rows=100,
        raw_root=tmp_path / "data",
        reports_dir=tmp_path / "reports",
    )
    assert report["infinite_counts"]["Ia"] == 2
    assert original["Ia"].isin([np.inf, -np.inf]).sum() == 2
    assert report["sampled_first_rows"] is False
    assert (tmp_path / "reports" / "pmsm_summary.csv").exists()
