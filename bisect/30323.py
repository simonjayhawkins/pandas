# json_normalize skips an entry in a pymongo cursor #30323

import pandas as pd

print(pd.__version__)

test_data = [{"_id": 1, "name": "Miriam"}, {"_id": 2, "name": "Peter"}]
data_gen = (record for record in test_data)
result = pd.json_normalize(data_gen)
print(result)

# bisecting for a fix
not_expected = pd.json_normalize(test_data[1:])
pd.testing.assert_frame_equal(result, not_expected)
