# BUG: pd.date_range not factoring in nanoseconds in freq #46877

import pandas as pd

print(pd.__version__)

end = pd.Timestamp("1970-01-01 00:00:00")
offset = pd.DateOffset(**{"hours": 10, "nanoseconds": 3})
result = end + offset
print(result)

expected = pd.Timestamp("1970-01-01 10:00:00.000000003")

assert not result == expected, result
