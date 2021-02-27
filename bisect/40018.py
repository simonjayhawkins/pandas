import pandas as pd
import pandas.testing as tm

print(pd.__version__)

df = pd.DataFrame({"a": [1, 2], "b": [1, 4], "c": [1, 4]})

res = df.transform({"b": ["sqrt", "abs"], "c": "sqrt"})
print(res)

expected = pd.MultiIndex.from_tuples(
    [("b", "sqrt"), ("b", "abs"), ("c", "sqrt")],
)

tm.assert_index_equal(res.columns, expected)
