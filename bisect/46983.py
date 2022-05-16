# BUG: Setting values on a multiindex df, via loc, does nothing on 1.4.x #46983

import pandas as pd

print(pd.__version__)

index = pd.MultiIndex.from_tuples(
    [("A", "a"), ("A", "b"), ("A", "c"), ("A", "d"), ("B", "a"), ("B", "b")]
)
df = pd.DataFrame(
    [[10, 100], [20, 200], [30, 300], [40, 400], [50, 500], [60, 600]],
    columns=["val1", "val2"],
    index=index,
)
df.loc["A"]["val1"] = 1
print(df)

expected = pd.DataFrame(
    {"val1": [1, 1, 1, 1, 50, 60], "val2": [100, 200, 300, 400, 500, 600]}, index=index
)
pd.testing.assert_frame_equal(df, expected)
