import os
import json
import random as rd
import pandas as pd
import hashlib as hs


def lerp(a, b, f):
    return a + (b - a) * (f / 100)


def calculate_score(trait_amount, trait_percent):
    trait_score = round(
        (lerp(100, 0, trait_amount) * lerp(1234, 0, trait_percent)), 3)
    return trait_score


def count_value(seed, percent):
    ps = percent / 100
    trait_quantity = int(seed * ps)
    return trait_quantity


def array2dic(array):
    result = {}
    for dic in array:
        result.update(dic)
    return result


def shuffle_traits():
    with open("../trait/json/traits2.json") as f:
        data = json.load(f)
        traits = data["traits"]
    new_array = []
    for j in range(0, len(traits)):
        count = traits[j]["count"]
        seed = traits[j]["seed"]
        name = traits[j]["name"]
        new_list = []
        for i in range(0, count):
            index = traits[j]["trait"][i]["index"]
            percent = traits[j]["trait"][i]["percent"]
            traits_name = traits[j]["trait"][i]["name"]
            new_list.extend(([{
                "index": index,
                "name": traits_name,
                "score": calculate_score(count, percent),
            }] * count_value(seed, percent)))
            rd.shuffle(new_list)
        rand_result = {f"{name}": new_list}
        new_array.append(rand_result)
    return array2dic(new_array)


def generate_traits_list(result):
    al = []
    for k in result:
        idz = []
        scores = []
        tname = []
        for v in range(0, len(result[k])):
            idz.append(result[k][v]["index"])
            tname.append(result[k][v]["name"])
            scores.append(result[k][v]["score"])
        la = {f"{k}": idz}
        laa = {"name": tname}
        laaa = {"score": scores}
        newa = la | laa | laaa
        al.append(newa)
    w = []
    for i in range(0, len(al)):
        w.append(pd.DataFrame(al[i]))
    df = pd.concat(w, axis=1)
    dfd = df.drop_duplicates(keep=False)
    os.makedirs("../trait/csv", exist_ok=True)
    df.to_csv("../trait/csv/out_1.csv")


# def convertToCsv(alist):
#     df = pd.DataFrame(data=alist).drop_duplicates(keep=False)
#     os.makedirs("../trait/csv", exist_ok=True)
#     df.to_csv("../trait/csv/out_1.csv", index=None)

if __name__ == "__main__":
    # convertToCsv(generate_traits_list())
    # print(generate_traits_list())
    # print(convertToCsv(generate_traits_list(shuffle_traits())))
    generate_traits_list(shuffle_traits())
