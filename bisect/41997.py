# 1.3: (intended?) Behavior change with empty apply #41997

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(columns=["a", "b"])

df["a"] = df.apply(lambda x: x["a"], axis=1)

print(df)
