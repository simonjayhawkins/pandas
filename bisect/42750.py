# BUG: highlight_min and highlight_max do not work with pd.NA #42750

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(dict(a=[pd.NA, -1, 1], b=[pd.NA, -1, 1]))

result = df.style.highlight_min().render()
print(result)
