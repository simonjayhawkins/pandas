import pandas as pd

print(pd.__version__)


df = pd.DataFrame(
    {"a": list("abcde"), "b": list("abcde")}, index=list("aabbc"), dtype="category"
)

result = df.agg("-".join, axis=1)
print(result)

expected = pd.Series(["a-a", "b-b", "c-c", "d-d", "e-e"], index=list("aabbc"))
pd.testing.assert_series_equal(result, expected)
