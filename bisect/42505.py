# BUG: Regression - AmbiguousTimeError creating DataFrame #42505

import pandas as pd

print(pd.__version__)

dt = pd.to_datetime("2019-11-03 01:00:00-0700").tz_convert("America/Los_Angeles")

result = pd.DataFrame({"dt": dt, "value": [1]})
print(result)
print(result.dtypes)
