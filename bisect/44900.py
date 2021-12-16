# BUG: Using pd.concat(axis="columns") on differently sized MultiIndexed
# DataFrames with a datetime index level containing exclusively NaT values
# causes the level in the returned DataFrame to be a float instead of a datetime
# #44900

import numpy as np

import pandas as pd

print(pd.__version__)
df_a = pd.DataFrame({"a": range(5), "idx1": range(5), "idx2": [pd.NaT] * 5}).set_index(
    ["idx1", "idx2"]
)
df_b = pd.DataFrame({"b": range(6), "idx1": range(6), "idx2": [pd.NaT] * 6}).set_index(
    ["idx1", "idx2"]
)
result = pd.concat([df_a, df_b], axis="columns")
print(result)

expected = pd.DataFrame(
    {
        "a": list(range(5)) + [np.nan],
        "b": range(6),
        "idx1": range(6),
        "idx2": [pd.NaT] * 6,
    }
).set_index(["idx1", "idx2"])
expected

pd.testing.assert_frame_equal(result, expected)
