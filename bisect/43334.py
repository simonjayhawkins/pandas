# BUG: pd.Categorical turns all values into NaN #43334

import numpy as np
import pandas as pd

print(pd.__version__)

data = pd.DataFrame({"Survived": [1, 0, 1], "Sex": [0, 1, 1]})
data["Survived"] = data["Survived"].astype("category")
data["Sex"] = data["Sex"].astype("category")
data.Survived.cat.categories = ["No", "Yes"]
data.Sex.cat.categories = ["female", "male"]
result = pd.Categorical(data.Survived, categories=["No", "Yes"], ordered=False)
print(result)

expected = np.array([1, 0, 1], dtype=np.int8)
pd._testing.assert_numpy_array_equal(result.codes, expected)
