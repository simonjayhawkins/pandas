# BUG: Difference in CSV roundtrip between 1.3.5 and 1.4.1 #46317

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    index=pd.MultiIndex.from_tuples([], names=["a", "b", "c"]), columns=["x"]
)
df.loc[(1, 2, 3)] = "bar"
print(df)

expected = pd.DataFrame(
    ["bar"],
    index=pd.MultiIndex.from_tuples([(1, 2, 3)], names=["a", "b", "c"]),
    columns=["x"],
)
pd.testing.assert_frame_equal(df, expected)
