import numpy as np

import pandas as pd

print(pd.__version__)

idx = pd.MultiIndex.from_arrays(
    [[str(i) for i in range(100)], np.random.choice(["A", "B"], size=(100,))],
    names=["a", "b"],
)

data_dict = {str(i): np.random.rand(100) for i in range(10)}
data_dict["string"] = [str(i) for i in range(100)]
data_dict["bool"] = np.random.choice([True, False], (100,))
data = pd.DataFrame(data_dict, index=idx)

result = data.sem(level=1)
print(result)
