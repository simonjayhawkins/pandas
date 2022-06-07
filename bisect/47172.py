# BUG: Memory leak when setting Series value via __setitem__ #47172

import gc
import os

import psutil

import pandas as pd

print(pd.__version__)


# create example data
items = [f"item_{i}" for i in range(10_000)]

data = {}
for i, col in enumerate(items[:1000]):
    data[col] = [1] * len(items)
df = pd.DataFrame(index=items, data=data)

gc.collect()
process = psutil.Process(os.getpid())
rss = process.memory_info().rss / 1024 / 1024

for item in df.columns[:10]:
    df[item][item] = -10
    gc.collect()
    new_rss = process.memory_info().rss / 1024 / 1024
    result = "{:.2f} MiB".format(new_rss - rss)
    print(result)

assert result == "0.00 MiB", result
