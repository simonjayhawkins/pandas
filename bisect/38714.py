import pandas as pd
import pandas.testing as tm

print(pd.__version__)

df = pd.DataFrame({"a": [1] * 2188})

p = "test.csv.zip"  # replace with available path
df.to_csv(p)
result = pd.read_csv(p)
print(result)

tm.assert_frame_equal(result[["a"]], df)
