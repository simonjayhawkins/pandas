# BUG: misleading error message when aggregating duplicate column names in groupby #44924

import pandas as pd

print(pd.__version__)

grp = pd.DataFrame.from_dict(
    {
        "A": [1, 2],
        "B": [3, 3],
        "C": ["G", "G"],
    }
).groupby("C")

print([i for i in grp])

grp2 = grp[["A", "B", "A"]]
print(grp2.mean())
