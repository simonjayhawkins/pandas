# BUG: to_csv requires escapechar unnecessarily when data contains
# null byte \x00 (PowerShell only) #47871

import csv
import pandas as pd

print(pd.__version__)

df = pd.DataFrame({"A": ["\x00"]})
try:
    df.to_csv("null_byte.csv", index=False)
except csv.Error as e:
    print(e)
else:
    exit(1) 
