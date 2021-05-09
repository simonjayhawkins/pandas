import pandas as pd

print(pd.__version__)
d1 = pd.DataFrame([("a",)], columns=["id"], dtype="string")
d2 = pd.DataFrame([("b",)], columns=["id"], dtype="string")
result = d1.merge(d2, on="id", how="right")
dtype = result.dtypes["id"]
print(dtype)
assert isinstance(dtype, pd.StringDtype)
