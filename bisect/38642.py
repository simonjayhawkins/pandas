import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"key": pd.Categorical(["b"] * 5, categories=["a", "b", "c", "d"]), "col": range(5)}
)

gb = df.groupby("key")

result = list(gb.indices)
print(result)
# Out[12]: ['a', 'b', 'c', 'd']

assert result == ["a", "b", "c", "d"]
