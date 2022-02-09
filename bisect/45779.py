# BUG: Accessing a one-level MultiIndex with .loc raises with an unclear error (in 1.4) #45779

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    data=[[0], [1]],
    index=pd.MultiIndex.from_tuples(
        [("a",), ("b",)],
        names=[
            "first",
        ],
    ),
)

result = df.loc["a"]
print(result)
