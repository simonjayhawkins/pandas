# BUG: Styler renders booleans True/False as digits since 1.4.0 #46384

import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"A": [True, False]})

result = df.style.to_html()
print(result)

assert "True" in result
assert "False" in result
