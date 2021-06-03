import pandas as pd

print(pd.__version__)

d = {
    "num_legs": [4, 4, 2, 2, 8],
    "num_wings": [0, 0, 2, 2, 0],
    "class": ["mammal", "mammal", "mammal", "bird", "insect"],
    "animal": ["cat", "dog", "bat", "penguin", "spider"],
    "locomotion": ["walks", "walks", "flies", "walks", "walks"],
}
df = pd.DataFrame(data=d)
df = df.set_index(["class", "animal", "locomotion"])
df = df.transpose()
print(df)

result = df.xs(["mammal", "bird"], drop_level=False, axis=1)
print(result)
