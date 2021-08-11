import pandas as pd

print(pd.__version__)
df = pd.DataFrame({"a": [1, 1, 1, 2, 2], "b": [1, 2, 3, 4, 5]})
df["b"] = df["b"].astype(pd.Int32Dtype())
try:
    res = df.groupby("a").agg("std")
except TypeError:
    # 1.0.0rc raised TypeError: cannot safely cast non-equivalent float64 to int32)
    pass
else:
    print(res)
