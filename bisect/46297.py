# BUG: Error writing DataFrame with categorical type column and interval data to a CSV file #46297

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(index=[0], columns=["a"])
df.at[0, "a"] = pd.Interval(pd.Timestamp("2020-01-01"), pd.Timestamp("2020-01-02"))
df["a"] = df["a"].astype("category")  # astype("object") does not raise an error

result = df.to_csv()
print(result)

expected = ',a\n0,"(2020-01-01, 2020-01-02]"\n'
assert result == expected
