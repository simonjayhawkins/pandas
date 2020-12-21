import pandas as pd

print(pd.__version__)

idx = pd.Index(["あ", b"a"], dtype="object")

res = idx.astype(str)
print(res)

assert res[1] == "a"
