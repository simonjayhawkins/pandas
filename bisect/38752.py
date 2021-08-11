import math
import sys

import numpy as np

try:
    import pandas as pd
except NameError:
    sys.exit(125)
import pandas._testing as tm

print(pd.__version__)


id1 = (
    pd.date_range("2019-10-01", "2020-01-08", freq="2H")
    .to_frame(name="stamp")
    .reset_index(drop=True)
)
id2 = (
    pd.date_range("2019-10-01", "2020-01-08")
    .to_frame(name="stamp")
    .reset_index(drop=True)
)
id1["id"] = 1
a = 2.5
id1["value"] = (math.e + a) ** (((id1.index + 10) % 40) - 20)
id2["id"] = 2
id2["value"] = np.nan
id2.loc[id2.stamp == "2019-11-15", "value"] = 10.0 ** -13

df = pd.concat([id1, id2], ignore_index=True)
df.sort_values("stamp", inplace=True)

roll_sum = df.groupby("id").rolling("93D", on="stamp")["value"].sum().reset_index()

result1 = roll_sum[roll_sum.id == 2].iloc[-1].value
print(result1)

roll_sum_2 = (
    df[df.id == 2].groupby("id").rolling("93D", on="stamp")["value"].sum().reset_index()
)

result2 = roll_sum_2[roll_sum_2.id == 2].iloc[-1].value
print(result2)

tm.assert_almost_equal(result1, result2)
