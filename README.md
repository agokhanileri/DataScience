# Data Science

## Description

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-BSD--3--Clause-lightgrey.svg)
![Lint](https://img.shields.io/badge/lint-Ruff-black.svg)

Data science learning path with data manipulation, visualization, access, and database.<br>

## Content

| #  | Script                                       | Level |Status |Linting| Topics                                                                |
|----|----------------------------------------------|:-----:|:-----:|:-----:|-----------------------------------------------------------------------|
| 01 | [Numpy](./numpy.py)                          | Soft  | ✅    | ❌    | Scalars, Arrays, Matrices, ...                                        |
| 02 | [Pandas](./pandas.py)                        | Med   | ⚠️    | ❌    | Series, DataFrame,                                                    |
| 03 | [Scipy](./scipy.py)                          | Soft  | ⚠️    | ❌    |                                                                       |
| 04 | [Matplotlib](./matplotlib.py)                | Soft  | ✅    | ❌    |                                                                       |
| 05 | [Seaborn](./seaborn.py)                      | Soft  | ❌    | ❌    |                                                                       |
| 06 | [FileHandling](./file_handling.py)           | Firm  | ❌    | ❌    | Read/Write, CSV, JSON, Parquet, URL, excel, multimodal, ...           |
| 07 | [SQL](./sql.py)                              | Firm  | ⚠️    | ❌    | properties, joins, merges, pyconnector, postgresql, ...               |

## Manual

### Style

Philosopy: Pythonic | Zen<br>
\- Relevant lines are grouped together as much as possible.<br>

Linter: ruff<br>
Formatter: black<br>

Execution: line-by-line<br>
\- Although some scripts may run directly.<br>
### Run the currency app (local)

A small FastAPI app that provides a single-page USD currency converter is included at `currency/currency.py` with its template in `currency/templates/index.html`. To run it locally:

1. Create and activate a virtual environment (macOS / zsh):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the required packages (minimal set):

```bash
pip install fastapi uvicorn httpx jinja2 python-multipart
# or install dev extras if you added them to pyproject: pip install -e .[dev]
```

3. Start the app (one of the two ways):

- Via uvicorn directly:

```bash
uvicorn currency.currency:app --reload --port 8000
```

- Or using the convenience runner included in `scripts`:

```bash
python scripts/run_currency.py
```

4. Open the UI at: http://127.0.0.1:8000

- Click **Load currencies** to populate the select input, enter a USD amount and choose a target currency, then click **Convert**. The conversion is saved to a local SQLite database file (`conversions.db`) and a history is shown beneath the form.
### Dependencies

Python: v3.12

Packages: numpy, pandas, scipy, matplotlib, seaborn, scikit-learn, pytorch, tensorflow, keras, sqlite3

CI/CD: ruff, black, mypy, pytest, pre-commit

## License

This project is licensed under the BSD 3-Clause License.