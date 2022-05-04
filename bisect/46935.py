# BUG: pd.read_json throwing error on bytes input #BUG: pd.read_json throwing error on bytes input #46935

import pandas as pd

print(pd.__version__)

buffer = b'[{"amount":100,"name":"Alice"},{"amount":200,"name":"Bob"},{"amount":300,"name":"Charlie"},{"amount":400,"name":"Dennis"}]'

result = pd.read_json(buffer)
print(result)

expected = pd.DataFrame(
    {"amount": [100, 200, 300, 400], "name": ["Alice", "Bob", "Charlie", "Dennis"]}
)
pd.testing.assert_frame_equal(result, expected)
