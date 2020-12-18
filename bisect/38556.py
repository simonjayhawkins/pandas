import pandas as pd

print(pd.__version__)

res = pd.CategoricalIndex(["A", "B", "C", "A", "B"]).get_indexer(
    pd.CategoricalIndex(["B", "C", "D", "E"])
)
print(res)
