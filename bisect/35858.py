import pandas
import pandas.testing as tm

print(pandas.__version__)

date = pandas.Timestamp("2000")
x = pandas.DataFrame([["a", date, 1],], columns=["a", "b", "c"]).set_index(
    ["a", "b"]
)["c"]
print(x)

res = x.loc[:, [date]]
print(res)

tm.assert_series_equal(res, x)
