import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {
        "name": ["Raphael", "Donatello", "Miguel Angel", "Leonardo"],
        "mask": ["red", "purple", "orange", "blue"],
        "weapon": ["sai", "bo staff", "nunchunk", "katana"],
    }
)

df.to_csv("tmnt.csv", index=False, encoding="utf-16")

result = pd.read_csv(
    filepath_or_buffer="tmnt.csv",
    encoding="utf-16",
    sep=",",
    header=0,
    decimal=".",
    memory_map=True,
)
print(result)
