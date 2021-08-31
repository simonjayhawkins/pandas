# BUG: resampling DataFrame with DateTimeIndex with holes and uint64 columns leads to error on pandas==1.3.2 (not in 1.1.0) #43329

import numpy as np
import pandas as pd

print(pd.__version__)

# Data generation: DataFrame with DateTimeIndex, one row per hour, values are 0 or 1.
df = pd.DataFrame(
    index=pd.date_range(start="2000-01-01", end="2000-01-03 23", freq="H"),
    columns=["x"],
    data=[0, 1, 0] * 24,
)

# Removing some rows in order to have a hole in the dataset
df = df.loc[(df.index < "2000-01-02") | (df.index > "2000-01-03"), :]

# Create dummy indicator
one_hot = pd.get_dummies(
    df["x"]
)  # This line leads to having "RuntimeError: empty group with uint64_t"
# one_hot = pd.get_dummies(df["x"], dtype=int)  # This line leads to having expected dataframe
# Keeping, for each day, the maximum day value.
df_output = one_hot.resample("D").max()
print(df_output)

# Expected_dataframe:
df_expected = pd.DataFrame(
    index=pd.date_range(start="2000-01-01", end="2000-01-03", freq="D"),
    data={col: [1, np.nan, 1] for col in [0, 1]},
)

pd.testing.assert_frame_equal(df_expected, df_output)
