import pandas as pd

print(pd.__version__)

df1 = pd.DataFrame({"a": ["A", "A", "B"], "b": ["ca", "cb", "cb"], "v": [10] * 3})

df1 = df1.set_index(["a", "b"])

# int column
df1["is_"] = 1

df1 = df1.unstack("b")

# Will not work, keeping NaN in the value
df1[("is_", "ca")] = df1[("is_", "ca")].fillna(0)

# Will raise ValueError: Cannot convert non-finite values (NA or inf) to integer
df1[("is_", "ca")] = df1[("is_", "ca")].astype("uint8")
print(df1)
