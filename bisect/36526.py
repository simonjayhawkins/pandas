import pandas as pd

s = pd.Series(list(range(0, 24)) * 500) - 5
s

result = s % 24
print(result)

result = result >= 0
assert result.all()
