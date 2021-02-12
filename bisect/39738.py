import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

result = df.sum(min_count=10)
print(result)
