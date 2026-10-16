"""Audit SCUT or PMSM locally and write JSON/CSV reports into data/reports/."""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from healthcar.audit import write_report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", choices=["scut1", "scut7", "pmsm", "both", "all"],
                        default="both")
    parser.add_argument("--max-rows", type=int, default=250000)
    parser.add_argument("--full", action="store_true", help="Use all rows; can require a lot of RAM")
    args = parser.parse_args()
    kinds = {"both": ["scut1", "pmsm"], "all": ["scut1", "pmsm", "scut7"]}.get(
        args.dataset, [args.dataset]
    )
    failed = False
    for kind in kinds:
        try:
            report, _ = write_report(kind, None if args.full else args.max_rows)
            print(f"{kind}: {report['rows_loaded']:,} rows, {report['duplicate_rows']} duplicates")
            for warning in report["warnings"]:
                print(f"  - {warning}")
        except Exception as exc:
            failed = True
            print(f"ERROR {kind}: {exc}", file=sys.stderr)
    print("Reports: data/reports/")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
