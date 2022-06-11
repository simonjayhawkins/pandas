# BUG: groupby transform doesn't respect Series index anymore #45648

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "bar", "foo", "foo"],
        "C": [2.1, 1.9, 3.6, 4.0, 1.9, 7.8, 2.8],
    }
)
grp = df.groupby("A")["C"]

# sort C within groups defined by A
result = grp.transform(pd.Series.sort_values)
print(result)

expected = grp.transform(lambda x: x.sort_values().values)
pd.testing.assert_series_equal(result, expected)
