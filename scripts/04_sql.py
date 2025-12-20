"""SQL join examples."""

import pandas as pd
import sqlite3


# =================================================================================================
def parse_pairs_matrix(s: str) -> pd.DataFrame:
    cols = {}
    for segment in s.split(";"):
        if not segment.strip(): 
            continue
        head, key = segment.rsplit(":", 1)
        key = key.strip()
        pairs = re.findall(r"([+-]?\d+(?:\.\d+)?)\s*,\s*([+-]?\d+(?:\.\d+)?)", head)
        for x, y in pairs:
            cols.setdefault(key, {})[float(x)] = float(y)
    return pd.DataFrame(cols).sort_index()

s = "5.0, 100, 5.5, 101, 6.0, 102:L10;5.0, 99, 5.5, 100, 6.0, 101:L20"
df = parse_pairs_matrix(s)
print(df)

# =================================================================================================

emp = pd.read_csv("./inputs/employees.csv")
dept = pd.read_csv("./inputs/departments.csv")

con = sqlite3.connect(":memory:")
emp.to_sql("employees", con, index=False)
dept.to_sql("departments", con, index=False)

left_join = """
SELECT e.EmpID, e.Name, d.DeptName
FROM employees e
LEFT JOIN departments d
  ON e.DeptID = d.DeptID
WHERE e.EmpID >= 2 
ORDER BY e.EmpID;
"""

inner_join = """
SELECT e.EmpID, e.Name, d.DeptName
FROM employees e
INNER JOIN departments d
  ON e.DeptID = d.DeptID
WHERE e.EmpID >= 2
ORDER BY e.EmpID;
"""

print("Left join:")
print(pd.read_sql_query(left_join, con))  # skips Alice due to EmpID > 2
print("Inner join:")
print(pd.read_sql_query(inner_join, con))  # skips David too since his DeptID is missing in dep


# -----------------------------------
# Right join: Not in sqlite because redundant s.t. one can swap the tables.
# Full outer join: Not in sqlite because it's costly due to merging L/R joins + deduplication
# Workaround:
# SELECT * FROM A LEFT JOIN B ON A.id = B.id   # left join
# UNION
# SELECT * FROM B LEFT JOIN A ON A.id = B.id;  # reversed left join = right join

# -----------------------------------
# Using duckdb: Alternative shortcut
# print("INNER:")
# print(duckdb.query("SELECT * FROM emp INNER JOIN dept USING(DeptID)").to_df(), "\n")

# print("LEFT:")
# print(duckdb.query("SELECT * FROM emp LEFT JOIN dept USING(DeptID)").to_df(), "\n")
