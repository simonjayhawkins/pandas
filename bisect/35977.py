import pandas as pd

print(pd.__version__)
df = pd.DataFrame({"a": ["a", "b", "c"], "b": ["d", "", ""]}, dtype="string")

df.replace(r"^\s*$", pd.NA, regex=True, inplace=True)
print(df)
