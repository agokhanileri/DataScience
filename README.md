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

### Dependencies

Python: v3.12

Packages: numpy, pandas, scipy, matplotlib, seaborn, scikit-learn, pytorch, tensorflow, keras, sqlite3

CI/CD: ruff, black, mypy, pytest, pre-commit

## License

This project is licensed under the BSD 3-Clause License.