import pandas as pd
import pandas.testing as tm

print(pd.__version__)

df = pd.DataFrame([], columns=["id", "field"])

result = df["id"].transform(lambda x: x + 10)
print(result)

expected = pd.Series([], index=pd.Index([], dtype="object"), name="id", dtype="object")

tm.assert_series_equal(result, expected)
