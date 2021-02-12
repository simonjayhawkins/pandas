import pandas as pd

print(pd.__version__)

dft = pd.DataFrame({"A": [0, 1], "B": [10, 11]})
dft.to_excel("test.xlsx", columns=["A", "B", "A"], engine="openpyxl")

result = pd.read_excel("test.xlsx", engine="openpyxl")
print(result)
