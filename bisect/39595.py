import pandas as pd

print(pd.__version__)

df1 = pd.DataFrame([1, 2, 3, 4], columns=["w"])
df2 = pd.DataFrame([1, 2, 3, 4], columns=["w"])
c1 = df1["w"].where(df1["w"] < 4, 4)
c2 = df2["w"].where(df2["w"] < 5)
c1 *= 2
c2 *= 2
print(df1["w"])
print(df2["w"])
assert (c1 == c2).all()
assert (df1["w"] == df2["w"]).all()  # df2 got changed, so assertion fails
