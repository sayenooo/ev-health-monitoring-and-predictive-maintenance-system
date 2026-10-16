# Dataset availability status

**Source data is NOT included in this repository, and this commit does not claim local downloads or completed real-data audits.**

The scripts fetch SCUT passenger vehicle #1 and the PMSM laboratory inverter dataset directly from their original publishers. SCUT vehicle #7 is optional and larger.

Run on your computer:
```bash
python scripts/download_data.py
python scripts/run_audit.py --dataset both
```
Generated raw files and audit reports live under ignored `data/` directories. For a failed download, use the official manual URLs in [dataset feasibility](docs/dataset_feasibility.md), verify the ZIP, and place it into `data/raw/downloads/` using the expected name printed by the script.

**Scientific status:** These notebooks initially contain no execution output. Results will only be valid after actual source files are downloaded and audited.
