# BUG: DafaFrame.insert doesn't raise an exception when inserting another DataFrame #42403

import pandas

print(pandas.__version__)

df = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})
df.insert(1, "newcol", df)
print(df)
