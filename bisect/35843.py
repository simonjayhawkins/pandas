import pandas as pd

print(pd.__version__)

values = [
    pd.Timestamp("2012-05-01T01:00:00.000000"),
    pd.Timestamp("2016-05-01T01:00:00.000000"),
]
arr = pd.arrays.SparseArray(values)
print(arr)

ser = pd.Series(arr)
print(ser)
