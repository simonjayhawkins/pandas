import numpy as np

import pandas as pd

print(pd.__version__)

input_df = pd.DataFrame(
    **{
        "index": [0, 1],
        "columns": [
            "loss",
            "category_64973.fc_size",
            "category_64973.num_fc_layers",
            "training.learning_rate",
        ],
        "data": [
            [1.0549572706222534, 240, 2, 0.0014908184659929895],
            [1.225046157836914, 160, 2, 0.0013734204727201226],
        ],
    }
)

input_df["training.learning_rate"] = pd.qcut(
    input_df["training.learning_rate"],
    q=10,
    precision=3,
    duplicates="drop",
)

data = input_df.pivot_table(
    index="category_64973.fc_size",
    columns="training.learning_rate",
    values="loss",
    aggfunc="mean",
)

# Seaborn code starts here
mask = np.zeros(data.shape, bool)
mask = pd.DataFrame(mask, index=data.index, columns=data.columns, dtype=bool)

print(mask)

print(pd.isnull(data))

res = mask | pd.isnull(data)
print(res)
