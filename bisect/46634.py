# BUG: Replace changes the dtype of other columns #46634

import pandas as pd

print(pd.__version__)

cat_series = pd.Series(["b", "b", "b", "d"], dtype="category")
df = pd.DataFrame(
    {
        "id": pd.Series([5, 4, 3, 2], dtype="float64"),
        "col": cat_series,
    }
)
result = df.replace({3: None})

print(result)

print(result.dtypes)

expected = pd.DataFrame(
    {
        "id": pd.Series([5.0, 4.0, None, 2.0], dtype="object"),
        "col": cat_series,
    }
)

pd.testing.assert_frame_equal(result, expected)
