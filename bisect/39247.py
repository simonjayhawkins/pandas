import codecs

import pandas as pd

print(pd.__version__)


x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = ["a", "b", "c", "d", "e"]
data = {"X": x, "Y": y, "Z": z}
df = pd.DataFrame(data, columns=["X", "Y", "Z"])

fp = codecs.open("out-testPD12.csv", "w", "utf-8")
df.to_csv(fp, index=False, header=True)
fp.close()

result = pd.read_csv("out-testPD12.csv")
print(result)
