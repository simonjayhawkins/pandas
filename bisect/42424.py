# BUG: creating DF from series with non exact categorical indices created from pd.cut #42424


import pandas as pd

print(pd.__version__)

ser = pd.Series(range(0, 100))
ser1 = pd.cut(ser, 10).value_counts().head(5)
ser2 = pd.cut(ser, 10).value_counts().tail(5)

result = pd.DataFrame({"1": ser1, "2": ser2})
print(result)
