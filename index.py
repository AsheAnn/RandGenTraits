import pandas as pd 
import os


index = []
for i in range(0, 10000):
    s = f"{i}"
    idx = s.zfill(5)
    index.append(idx)
t = {"Int":index}
df = pd.DataFrame(t)
os.makedirs("../trait/csv", exist_ok=True)
df.to_csv("../trait/csv/out_index.csv", index=None)

