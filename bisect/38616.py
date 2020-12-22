import pandas as pd

pd.__version__

left = pd.DataFrame({"x": [1, 1], "z": ["foo", "foo"]})
right = pd.DataFrame({"x": [1, 1], "z": ["foo", "foo"]})

result = pd.merge(left, right, how="right", left_index=True, right_on="x")

print(result)
