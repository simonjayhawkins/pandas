# PERF: concat along axis 1 unnecessarily materializes RangeIndex->Int64Index #47501

import pandas as pd

print(pd.__version__)

result = pd.concat(
    [pd.DataFrame({"a": range(10)}), pd.DataFrame({"b": range(10)})], sort=True, axis=1
)
print(result.index)

assert isinstance(result.index, pd.RangeIndex)
