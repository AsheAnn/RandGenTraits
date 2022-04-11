import pandas as pd 
import csv
import os


index = []
for i in range(0, 10000):
    if i < 10:
        index.append("int0000"f"{i}")
    elif i < 100:
        index.append("int000"f"{i}")
    elif i < 1000:
        index.append("int00"f"{i}")
    else:
        index.append("int0"f"{i}")

t = {"Int":index}
df = pd.DataFrame(t)
os.makedirs("../trait/csv", exist_ok=True)
df.to_csv("../trait/csv/out_index.csv", index=None)
