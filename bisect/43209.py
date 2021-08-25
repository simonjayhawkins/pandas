# BUG: groupby aggregation methods produce empty DataFrame with mixed DataTypes #43209

import pandas as pd

print(pd.__version__)


df = pd.DataFrame([[1, 2, 3, 4, 5, 6]] * 3)
df.columns = pd.MultiIndex.from_product([["a", "b"], ["i", "j", "k"]])

for col in df.columns:
    if col[-1] == "j":
        df[col] = df[col].astype("Int64")

result = df.groupby(level=1, axis=1).sum()
print(result)

assert len(result)
