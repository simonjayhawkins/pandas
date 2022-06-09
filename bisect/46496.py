# BUG: lambda with positional references in apply after groupby on empty dataframe errors #46496

import pandas as pd

print(pd.__version__)


result = (
    pd.DataFrame([], columns=["a", "b", "c"])
    .groupby("a")
    .b.apply(lambda x: x[0] - x[1])
)
print(repr(result))

expected = pd.Series(
    [],
    name="b",
    dtype=object,
    index=pd.Index([], dtype="object", name="a"),
)
pd.testing.assert_series_equal(result, expected)
