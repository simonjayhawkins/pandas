import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"key": ["a", "a", "b", "b"], "val": ["a", "b", "c", "d"]}, dtype="string"
)

res = df.groupby("key").agg({"val": "first"})
print(res)
