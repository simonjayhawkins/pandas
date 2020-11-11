import pandas as pd

print(pd.__version__)

import pandas as pd

d = pd.DataFrame({"a": [1, 1, 2, 1], "b": [(1, 1, 0)] * 4})
d.loc[d["a"] == 1, "b"] = [[(0, 0, 1)]]
print(d)
