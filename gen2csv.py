import random as rd
import pandas as pd
import os
import json


def random_trait(name, count, seed):
    index = []
    for i in range(0, seed):
        trait_index = rd.randint(0, count - 1)
        index.append(trait_index)
    rd.shuffle(index)
    rand_result = {f"{name}": index}
    return rand_result


def generate_traits_list():
    with open("../trait/json/trait.json") as f:
        data = json.load(f)
        traits = data["traits"]
    new_list = []
    for j in range(0, len(traits)):
        name = traits[j]["name"]
        count = traits[j]["count"]
        seed = traits[j]["seed"]
        all_traits = random_trait(name, count, seed)
        new_list.append(all_traits)
    result = {}
    for dic in new_list:
        result.update(dic)
    return result


def convertToCsv(alist):
    df = pd.DataFrame(data=alist).drop_duplicates(keep=False)
    return df
    # os.makedirs("../trait/csv", exist_ok=True)
    # df.to_csv("../trait/csv/out.csv")


if __name__ == "__main__":
    print(generate_traits_list())
