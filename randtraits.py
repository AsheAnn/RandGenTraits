import random as rd
import pandas as pd
import os
import json


def trait(name, count, seed):
    index = []
    for i in range(0, seed):
        traitIndex = rd.randint(0, count - 1)
        index.append(traitIndex)
    rd.shuffle(index)
    dp = {f"{name}": index}
    return dp


def loadjson(file):
    with open(file) as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    t0 = trait("Body", 13, 3333)
    t1 = trait("Hand", 6, 3333)
    t2 = trait("Skin", 5, 3333)
    t3 = trait("Hair", 6, 3333)
    t4 = trait("Face", 8, 3333)
    t5 = trait("Ears", 8, 3333)
    t6 = trait("Nose", 3, 3333)
    t7 = trait("Eyes", 24, 3333)
    t8 = trait("Eyesbrow", 10, 3333)
    t9 = trait("Neck", 4, 3333)
    t10 = trait("Mouth", 15, 3333)
    t11 = trait("BodyGear", 4, 3333)
    t12 = trait("HeadGear", 4, 3333)
    t13 = trait("FaceGearFront", 3, 3333)
    t14 = trait("FaceGearBack", 5, 3333)
    t15 = trait("Background", 8, 3333)
    print(t0 | t1)
    # ts1 = t0 | t1 | t2 | t3 | t4 | t5 | t6 | t7
    # ts2 = t8 | t9 | t10 | t11 | t12 | t13 | t14 | t15
    # tsall = ts1 | ts2
    #
    # df = pd.DataFrame(data=tsall).drop_duplicates(keep=False)
    # os.makedirs("../trait/csv2", exist_ok=True)
    # df.to_csv("../trait/csv2/out2.csv")
