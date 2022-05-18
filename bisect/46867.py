# BUG: groupby.transform with execution engine numba does not work in multiindex case since 1.3 #46867

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([{"A": 1, "B": 2, "C": 3}]).set_index(["A", "B"])


def numba_func(values, index):
    return 1


result = df.groupby("A").transform(numba_func, engine="numba")
print(result)

expected = pd.DataFrame([{"A": 1, "B": 2, "C": 1.0}]).set_index(["A", "B"])
pd.testing.assert_frame_equal(result, expected)
