import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

try:
    result = df.sum(min_count=10)
except AttributeError:
    pass
else:
    print(result)
