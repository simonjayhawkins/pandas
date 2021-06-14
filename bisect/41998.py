# BUG?: 1.3 behavior change with groupby and asindex=False #41998

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(columns=["date", "crew_member_id"])

grp = df.groupby(["date", "crew_member_id"], as_index=False)
result = grp.sum()

print(result)
