# BUG: set_index screws up the dtypes on empty DataFrames #38419

import sys

import pandas as pd
import pandas.testing as tm

print(pd.__version__)

d1 = pd.DataFrame(
    {
        "a": pd.Series(dtype="datetime64[ns]"),
        "b": pd.Series(dtype="int64"),
        "c": [],
    }
)
# d1

# d1.dtypes

d2 = d1.set_index(["a", "b"])
# d2

# d2.dtypes

result = d2.index.to_frame().dtypes
print(result)

expected = d1.loc[:, ["a", "b"]].dtypes
print(expected)

# assert (d1.loc[:, ["a", "b"]].dtypes == d2.index.to_frame().dtypes).all()

try:
    tm.assert_series_equal(result, expected)
except:
    pass
else:
    sys.exit(1)
