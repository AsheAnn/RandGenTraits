import random as rd
import csv
import pandas as pd
from itertools import zip_longest


def initIndex(name, seed):
    index = []
    for i in range(0, seed):
        index.append(i)
    n = f"{name}"
    # dp = n + index
    # data = [dp]
    # export_data = zip_longest(*data, fillvalue="")
    # with open("../trait/csv2/trait_1.csv", "w", newline="") as f:
    #     wr = csv.writer(f)
    #     wr.writerows(export_data)
    dp = {n: index}
    return dp


def trait(name, count, seed):
    index = []
    for i in range(0, seed):
        traitIndex = rd.randint(0, count - 1)
        index.append(traitIndex)
    rd.shuffle(index)
    n = f"{name}"
    # dp = n + index
    # data = [dp]
    # export_data = zip_longest(*data, fillvalue="")
    # with open("../trait/csv2/trait_1.csv", "w", newline="") as f:
    #     wr = csv.writer(f)
    #     wr.writerows(export_data)
    dp = {n: index}
    return dp


if __name__ == "__main__":
    t0 = trait("Body", 13, 3333)
    t1 = trait("Hand", 6, 3333)
    t2 = trait("Skin", 5, 3333)
    t3 = trait("Hair", 6, 3333)
    t4 = trait("Face", 21, 3333)
    t5 = trait("Ears", 8, 3333)
    t6 = trait("Nose", 3, 3333)
    t7 = trait("Eyes", 24, 3333)
    t8 = trait("Eyesbrow", 10, 3333)
    t9 = trait("Neck", 4, 3333)
    t10 = trait("Mouth", 15, 3333)
    t11 = trait("BodyGear", 4, 3333)
    t12 = trait("HeadGear", 4, 3333)
    t13 = trait("FaceGearFront", 4, 3333)
    t14 = trait("FaceGearBack", 5, 3333)
    t15 = trait("Background", 8, 3333)







    d3 = d1 | d2
    df = pd.DataFrame(data=d3)
    dfwodu = df.drop_duplicates()
    print(dfwodu)


