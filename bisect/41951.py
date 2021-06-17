# DataFrame.melt fails if there are duplicate value_vars #41951

import pandas as pd

print(pd.__version__)

df = pd.DataFrame([["id", 2, 3]]).set_axis(["id_var", "value_var", "value_var"], axis=1)

result = df.melt(id_vars=["id_var"], value_vars=["value_var"])
print(result)

expected = pd.DataFrame(
    {"id_var": ["id", "id"], "variable": ["value_var", "value_var"], "value": [2, 3]}
)
expected

pd.testing.assert_frame_equal(result, expected)
