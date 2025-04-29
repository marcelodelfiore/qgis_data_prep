# Soil Analysis XLSX to CSV Extractor

This project processes a soil analysis `.xlsx` file and exports each soil data column into separate **tab-separated CSV files**, preserving the two coordinate columns in each output.

---

## Requirements

- Python 3.7+
- pip

Install dependencies:

```bash
make install
# or manually:
pip install -r requirements.txt
```

## Usage

### From the project root, use:

```bash
make run
```

This will create the output folder `CSV` and write the CSV files there.

Alternatively:

```bash
./run.sh Dados_Cafe
```

### Clean Generated CSVs

To remove all .csv files in the output folder:

```bash
make clean
```
