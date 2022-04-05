# BUG: Unexpected change of behavior on DataFrame type float32 between pandas versions. #46552

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([[0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype="float32")
df.iloc[0][0] = "10"
print(df)

expected = pd.DataFrame(
    [[10.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype="float32"
)
pd.testing.assert_frame_equal(df, expected)
