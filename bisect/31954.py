import sys

import numpy as np

import pandas

a = np.array([[1, 2], [3, 4]])

# DO NOT WORKS
b = np.array([[0.5, 6], [7, 8]])
# b = np.array([[.5,6],[7,8]])  # The same problem

# This one works fine:
# b = np.array([[5,6],[7,8]])

dfA = pandas.DataFrame(a)
# This works fine EVEN using .5, because the columns name is different
# dfA = pandas.DataFrame(a, columns=['a','b'])
dfB = pandas.DataFrame(b)

df_new = pandas.concat([dfA, dfB], axis=1)

try:
    res = df_new[df_new > 5]
    print(res)
except:
    sys.exit(0)
else:
    sys.exit(1)
