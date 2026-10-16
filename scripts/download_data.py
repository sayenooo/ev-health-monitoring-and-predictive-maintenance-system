"""Fetch research ZIP files from their publishers and extract into ignored data/raw/."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import zipfile

import requests

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
SOURCES = {
    "scut1": {
        "url": "https://raw.githubusercontent.com/Translab-SCUT/Electric-vehicle-operation-data/main/vehicle%231.zip",
        "filename": "vehicle_1_scut.zip", "folder": "scut_vehicle1",
        "manual": "https://github.com/Translab-SCUT/Electric-vehicle-operation-data/blob/main/vehicle%231.zip",
    },
    "pmsm": {
        "url": "https://zenodo.org/records/14482932/files/PMSM-inverter-fault-diagnosis-3.0.zip?download=1",
        "filename": "PMSM-inverter-fault-diagnosis-3.0.zip", "folder": "pmsm",
        "manual": "https://zenodo.org/records/14482932",
    },
    "scut7": {
        "url": "https://raw.githubusercontent.com/Translab-SCUT/Electric-vehicle-operation-data/main/vehicle%237.zip",
        "filename": "vehicle_7_scut.zip", "folder": "scut_vehicle7",
        "manual": "https://github.com/Translab-SCUT/Electric-vehicle-operation-data/blob/main/vehicle%237.zip",
    },
}


def download(url: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_suffix(path.suffix + ".part")
    for attempt in range(1, 4):
        try:
            with requests.get(url, timeout=(20, 90), stream=True) as response:
                response.raise_for_status()
                expected = int(response.headers.get("content-length") or 0)
                size = 0
                with partial.open("wb") as out:
                    for block in response.iter_content(chunk_size=1024 * 1024):
                        if block:
                            out.write(block)
                            size += len(block)
                if size < 200 or (expected and size != expected):
                    raise OSError(f"Incomplete or suspicious download: {size} bytes")
            os.replace(partial, path)
            return
        except (requests.RequestException, OSError) as exc:
            partial.unlink(missing_ok=True)
            print(f"Attempt {attempt}/3 failed: {exc}", file=sys.stderr)
            if attempt == 3:
                raise
            time.sleep(attempt * 2)


def inspect_zip(path: Path) -> dict:
    if not zipfile.is_zipfile(path):
        raise ValueError(f"Not a ZIP archive: {path}")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    with zipfile.ZipFile(path) as archive:
        corrupted = archive.testzip()
        if corrupted:
            raise ValueError(f"ZIP entry failed integrity test: {corrupted}")
        entries = [z for z in archive.infolist() if not z.is_dir()]
        if not entries:
            raise ValueError("Empty ZIP")
    return {"sha256": digest.hexdigest(), "bytes": path.stat().st_size,
            "files": len(entries)}


def safe_extract(path: Path, folder: Path) -> None:
    root = folder.resolve()
    with zipfile.ZipFile(path) as archive:
        for entry in archive.infolist():
            destination = (root / entry.filename).resolve()
            if not destination.is_relative_to(root):
                raise ValueError(f"Unsafe ZIP member: {entry.filename}")
            if (entry.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("ZIP contains a symbolic link")
        folder.mkdir(parents=True, exist_ok=True)
        archive.extractall(folder)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=["scut1", "pmsm", "scut7", "all"])
    parser.add_argument("--redownload", action="store_true")
    args = parser.parse_args()
    kinds = list(SOURCES) if args.only == "all" else (
        [args.only] if args.only else ["scut1", "pmsm"]
    )
    failures = []
    for name in kinds:
        source = SOURCES[name]
        archive = RAW / "downloads" / source["filename"]
        print(f"[{name}] {source['url']}")
        try:
            if args.redownload or not archive.exists():
                download(source["url"], archive)
            metadata = inspect_zip(archive)
            folder = RAW / source["folder"]
            safe_extract(archive, folder)
            (folder / ".healthcar_download.json").write_text(
                json.dumps({"name": name, "url": source["url"], **metadata}, indent=2),
                encoding="utf-8"
            )
            print(f"  OK: {metadata['files']} files; {metadata['bytes']/1e6:.2f} MB")
        except Exception as exc:
            failures.append(name)
            print(f"  FAILED: {exc}\n  Manual download: {source['manual']}\n"
                  f"  Save ZIP as: {archive}", file=sys.stderr)
    if failures:
        raise SystemExit(f"Download failures: {', '.join(failures)}")
    print("Next: python scripts/run_audit.py --dataset both")


if __name__ == "__main__":
    main()
