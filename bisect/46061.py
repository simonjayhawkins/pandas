# BUG: groupby().rolling("freq") validation raises even if dates are sorted within each group #46061

import pandas as pd

print(pd.__version__)
test_df = pd.DataFrame(
    {
        "Name": ["L", "L", "L", "M", "M", "M", "M", "M", "M"],
        "ID": ["L1", "L2", "L3", "M1", "M2", "M3", "M4", "M5", "M6"],
        "Date": [
            "2005-01-01",
            "2006-01-01",
            "2013-01-01",
            "2005-01-01",
            "2006-01-01",
            "2006-01-01",
            "2017-01-01",
            "2006-02-01",
            "2006-03-01",
        ],
        "indicator": [0, 1, 0, 0, 1, 0, 0, 1, 0],
        "rolling_sum": [0, 0, 1, 0, 0, 0, 0, 1, 2],
    }
)
test_df["Date"] = pd.to_datetime(test_df["Date"], errors="coerce")

grp = test_df.groupby("Name").rolling("731D", on="Date")

print(grp)
# grp["indicator"].sum().reset_index()
