# BUG: using NamedTuples with .loc works only sometimes #48124


import pandas as pd
from collections import namedtuple

print(pd.__version__)

# A df with two level MutltiIndex
df = pd.DataFrame(
    index=pd.MultiIndex.from_product(
        [["A", "B"], ["a", "b", "c"]], names=["first", "second"]
    )
)

# complicated subset
expected = df.loc[("A", ["a", "b"]), :]  # <- Works

indexer_tuple = namedtuple("Indexer", df.index.names)

# complicated subset with named tuple
result = df.loc[indexer_tuple(first="A", second=["a", "b"]), :]  # <- DOES NOT WORK!
# Raises:
# InvalidIndexError: Indexer(first='A', second=['a', 'b'])
print(result)

pd.testing.assert_frame_equal(result, expected)
