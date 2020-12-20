import pandas as pd

print(pd.__version__)

x = pd.DataFrame([["foo", "bar"], [1, None]])
y = x[1].copy()

result = x.isin(y)
print(result)

assert result[1].all()
