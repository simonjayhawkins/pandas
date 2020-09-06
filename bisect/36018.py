import pandas as pd
import pandas.testing as tm

print(pd.__version__)

pser = pd.Series(
    [1, 2, 3, 2],
    index=pd.MultiIndex.from_tuples([("a", "x"), ("a", "y"), ("b", "z"), ("c", "z")]),
    name="a",
)

result = pser.groupby(pser).rolling(2).max()
print(result)

result.index

expected = pd.MultiIndex.from_tuples(
    [(1, "a", "x"), (2, "a", "y"), (2, "c", "z"), (3, "b", "z")],
    names=["a", None, None],
)

tm.assert_index_equal(result.index, expected)
