# BUG: Error writing DataFrame with categorical type column and "Int" data to a CSV file ("int" works of course) #46812

import numpy as np
import pandas as pd

print(pd.__version__)

d = {
    "name": ["bob", "todd", "sarah", "john"],
    "gp": [1, 2, np.NaN, 2],
    "score": [90, 40, 80, 98],
}
df = pd.DataFrame(d)
df.name = df.name.astype("category")
df.gp = df.gp.astype("Int16")
df.gp = df.gp.astype("category")

result = df.to_csv()
print(result)

expected = ",name,gp,score\n0,bob,1,90\n1,todd,2,40\n2,sarah,,80\n3,john,2,98\n"
assert result == expected
