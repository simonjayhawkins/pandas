import pandas as pd

print(pd.__version__)

result = pd.Series([0]).isin(["0"])
print(result)

result2 = pd.Series([1]).isin(["1"])
print(result2)

result3 = pd.Series([1.1]).isin(["1.1"])
print(result3)

assert result.all()
assert result2.all()
assert result3.all()
