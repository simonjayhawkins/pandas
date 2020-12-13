import pandas as pd

print(pd.__version__)

ci = pd.CategoricalIndex(["a", "b"])
df = pd.DataFrame([[1, 2], [3, 4]], index=ci, columns=ci)

result = df.shift(axis=1)
print(result)

# expected = pd.DataFrame([[np.nan, 1.0], [np.nan, 3.0]], index=ci, columns=ci)

# import pandas.testing as tm

# tm.assert_frame_equal(result, expected)
