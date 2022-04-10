import os
import json
import random as rd
import pandas as pd


def lerp(a, b, f):
    return a + (b - a) * (f / 100)


def calculate_score(trait_amount, trait_percent):
    trait_score = lerp(100, 0, trait_amount) * lerp(1234, 0, trait_percent)
    return trait_score


def count_value(seed, percent):
    ps = percent / 100
    trait_quantity = int(seed * ps)
    return trait_quantity


def generate_traits_list():
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
            new_list.extend(([index] * count_value(seed, percent)))
            rd.shuffle(new_list)
        rand_result = {f"{name}": new_list}
        new_array.append(rand_result)
    result = {}
    for dic in new_array:
        result.update(dic)
    return result


def convertToCsv(alist):
    df = pd.DataFrame(data=alist).drop_duplicates(keep=False)
    os.makedirs("../trait/csv", exist_ok=True)
    df.to_csv("../trait/csv/out_0.csv")


if __name__ == "__main__":
    convertToCsv(generate_traits_list())
    # print(generate_traits_list()["Body"][2])

