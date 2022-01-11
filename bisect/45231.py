# BUG: 1.4.0rc1 Error vectorizing grouping aggregation on empty dataframe with object column #45231

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"group": pd.Series(dtype="object"), "str": pd.Series(dtype="object")}
)

result = df.groupby("group").any()
print(result)

expected = pd.DataFrame(
    {"str": pd.Series([], dtype=bool)}, index=pd.Index([], dtype="object", name="group")
)
pd.testing.assert_frame_equal(result, expected)
