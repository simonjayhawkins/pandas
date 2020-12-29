import pandas as pd
import pandas.testing as tm

print(pd.__version__)

dti = pd.date_range("2016-01-01", periods=3)
dti2 = dti.tz_localize("UTC")

df = pd.DataFrame(dti)
df2 = pd.DataFrame(dti2)

result = df.all()
print(result)
result2 = df2.all()
print(result2)


tm.assert_series_equal(result, result2)
