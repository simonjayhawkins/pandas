import pandas as pd

print(pd.__version__)


print("Test 1")
a = pd.Series([1, 2, 3, 4], index=[1, 1, 2, 2], name=("a", "a"))
a.index.name = ("b", "b")
print(a)
print(a.index)
print(a.groupby(level=0).last())

print("Test 2")
a = pd.Series([1, 2, 3, 4], index=[2, 3, 4, 5], name=("a", "a"))
b = pd.Series([1, 1, 2, 2], index=[2, 3, 4, 5], name=("b", "b"))
a.index = b.reindex(a.index)
print(a)
print(a.index)
print(a.groupby(level=0).last())
