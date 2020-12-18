import pandas as pd

print(pd.__version__)

arrays = [
    ["Falcon", "Falcon", "Parrot", "Parrot"],
    ["Captive", "Wild", "Captive", "Wild"],
]
index = pd.MultiIndex.from_arrays(arrays, names=("Animal", "Type"))
df = pd.DataFrame({"Max Speed": [390.0, 350.0, 30.0, 20.0]}, index=index)

result = df.groupby(level=0)["Max Speed"].rolling(2).sum()
print(result)

expected = pd.MultiIndex.from_tuples(
    [
        ("Falcon", "Falcon", "Captive"),
        ("Falcon", "Falcon", "Wild"),
        ("Parrot", "Parrot", "Captive"),
        ("Parrot", "Parrot", "Wild"),
    ],
    names=["Animal", "Animal", "Type"],
)

import pandas.testing as tm

tm.assert_index_equal(result.index, expected)
