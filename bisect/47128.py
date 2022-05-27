# BUG: RangeIndex problem #47128

import pandas as pd

print(pd.__version__)

A = pd.DataFrame({"a": [False, True]})  # index=[0,1] vs index=range(2)
A["i"] = A.index
A.loc[A["a"], "i"] = -2
result = A.loc[A["a"], :]
print(result)

expected = pd.DataFrame({"a": True, "i": -2}, index=[1])
pd.testing.assert_frame_equal(result, expected)
