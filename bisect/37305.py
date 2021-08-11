import numpy as np

import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"col": range(10)}, index=pd.date_range("2012-01-01", periods=10, freq="20min")
)
df

df.index

# res = df.resample("H").apply(lambda group: len(group["col"].unique()))
# res

# res.index

res = df.resample("H")
res

res.axis

res.binner

res.grouper

res._set_binner()
res

res.binner

res.grouper

func = lambda group: len(group["col"].unique())
func

# from pandas.core.aggregation import aggregate

# result, how = aggregate(res, func)
# result, how # (None, True)

# res.binner
# # DatetimeIndex(['2012-01-01 00:00:00', '2012-01-01 01:00:00',
# #                '2012-01-01 02:00:00', '2012-01-01 03:00:00',
# #                '2012-01-01 04:00:00'],
# #               dtype='datetime64[ns]', freq='H')

# res.grouper
# # <pandas.core.groupby.ops.BinGrouper at 0x2768ebbc550>

obj = res._selected_obj
obj

obj is df

obj.index

grouper = res.grouper
grouper

axis = res.axis
axis

from pandas.core.groupby.groupby import get_groupby

grouped = get_groupby(obj, by=None, grouper=grouper, axis=axis)
grouped

# result = grouped._aggregate_item_by_item(func)

result = grouped.apply(func)
print(result)

assert result.index.freq is None
