# BUG: DataFrame index name is missing after call ".loc[]" in some cases. #42188

import pandas as pd

print(pd.__version__)

df1 = pd.DataFrame(
    {"col1": [1, 2, 3], "col2": [2, 3, 4], "col_index": ["a", "b", "b"]}
).set_index("col_index")
df2 = pd.DataFrame(
    {"col1": [1, 2, 3], "col2": [2, 3, 4], "col_index": ["a", "b", "c"]}
).set_index("col_index")

selected_index = df1.index.intersection(["a"])

result = df2.loc[selected_index]
print(result)

assert not result.index.name == "col_index", repr(result.index.name)
