# BUG: DataFrame.select_dtypes(include='number') includes BooleanDtype columns #46870

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "a": [1, 2, 3],
        "b": pd.Series([True, False, True], dtype=pd.BooleanDtype()),
        "c": pd.Series([True, False, True], dtype=bool),
    }
)

result = df.select_dtypes(include="number")
print(result)

expected = df[["a"]]
pd.testing.assert_frame_equal(result, expected)
