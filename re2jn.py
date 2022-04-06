import pandas as pd

df = pd.read_json(
    "https://raw.githubusercontent.com/domoritz/maps/master/data/iris.json")
df.head()
