# Behavior change of 1.4.rc0 when group by apply returns a copy of the passed data frame #45315

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([[1, 2, 3, 4]], columns=["A", "B", "C", "D"])
grouped = df.groupby(["A", "B"], as_index=True)[["C", "D"]]

combined = grouped.apply(lambda x: x.copy())
print(combined)

result = combined.reset_index().columns
print(result)

expected = pd.Index(["A", "B", "level_2", "C", "D"], dtype="object")
pd.testing.assert_index_equal(result, expected)
