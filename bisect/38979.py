import pandas as pd
import pandas.testing as tm

print(pd.__version__)

df = pd.DataFrame(zip("abc", "def"))

expected = df.apply(lambda f: "/".join(f), axis=1).str.upper()

result = df.apply(lambda f: "/".join(f.str.upper()), axis=1)

print(result)

tm.assert_series_equal(result, expected)
