# BUG: list-like objects are broadcast to each row (1.3 regression) #42549

import pandas as pd

print(pd.__version__)


class MySequence:
    def __getitem__(self, key):
        return range(3)[key]

    def __len__(self):
        return 3


my_sequence = MySequence()

result = pd.DataFrame(index=range(3), data={"a": my_sequence})
print(result)

expected = pd.DataFrame(index=range(3), data={"a": range(3)})
pd.testing.assert_frame_equal(result, expected)
