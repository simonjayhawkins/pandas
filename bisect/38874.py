import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"A": [1e-8, -1.1e-8, 1.2e-8, -1.1e-8] * 5})

result = df["A"].rolling(10).std(ddof=0)
print(result)

expected = df["A"][-10:].std(ddof=0)

assert result[19] == expected
