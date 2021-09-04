# BUG: RollingGroupby.corr() producing incorrect results #43386

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"a": ["g1"] * 4 + ["g2"] * 4, "b": range(8), "c": [0, 4, 6, 1, 2, 7, 3, 5]}
).sort_values("c")
grp = df.groupby("a")[["b", "c"]].rolling(3)

result = grp.corr()
print(result)

expected = df.sort_values(["a", "c"]).groupby("a")[["b", "c"]].rolling(3).corr()
pd.testing.assert_frame_equal(result, expected)
