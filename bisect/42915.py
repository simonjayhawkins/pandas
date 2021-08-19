# BUG: df.groupy().rolling().cov() does not group properly and the cartesian product of all groups is returned instead #42915

import pandas as pd

print(pd.__version__)

df_a = pd.DataFrame(
    {"value": range(10), "idx1": [1] * 5 + [2] * 5, "idx2": [1, 2, 3, 4, 5] * 2}
).set_index(["idx1", "idx2"])

df_b = pd.DataFrame({"value": range(5), "idx2": [1, 2, 3, 4, 5]}).set_index("idx2")

result = df_a.groupby(level=0).rolling(2).cov(df_b)
print(result)

assert len(result) == 10
