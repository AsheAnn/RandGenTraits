import os
import json
import random as rd
from numpy import number
import pandas as pd


def lerp(a, b, f):
    return a + (b - a) * (f / 100)


def calculate_score(trait_amount, trait_percent, color_amount, color_percent):
    trait_score = round(
        (lerp(100, 0, trait_amount) * lerp(1234, 0, trait_percent) +
         lerp(100, 0, color_amount) * lerp(1234, 0, color_percent)),
        3,
    )
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


def repalce_values():
    pass


def shuffle_relative_traits(file):
    with open(file) as f:
        data = json.load(f)
        traits = data["traits"]
        seed = data["seed"]
        relative_array = []
    for j in range(0, len(traits)):
        count = traits[j]["count"]
        name = traits[j]["name"]
        relative_list = []
        for i in range(0, count):
            index = traits[j]["type"][i]["index"]
            percent = traits[j]["type"][i]["percent"]
            color = traits[j]["type"][i]["color"]
            for k in range(0, len(color)):
                c_index = color[k]["index"]
                c_percent = color[k]["percent"]
                relative_list.extend([{
                    "t_index": index,
                    "c_index": c_index,
                }] * int(seed * (percent / 100) * (c_percent / 100)))
            rd.shuffle(relative_list)
            rand_reresult = {f"{name}": relative_list}
            relative_array.append(rand_reresult)
        null_list = []
        for item in relative_list:
            null_list.append(item["t_index"])
    return array2dic(relative_array)


def shuffle_mono_traits(file):
    with open(file) as f:
        data = json.load(f)
        traits = data["traits"]
        seed = data["seed"]
        new_list = []
    for j in range(0, len(traits)):
        count = traits[j]["count"]
        name = traits[j]["name"]
        mono_list = []
        for i in range(0, count):
            t_index = traits[j]["trait"][i]["index"]
            percent = traits[j]["trait"][i]["percent"]
            mono_list.extend([t_index] * int(seed * percent / 100))
        rd.shuffle(mono_list)
        rand_result = {f"{name}": mono_list}
        new_list.append(rand_result)
    # final_list = []
    # for k in range(len(body)):
    #     if body[k] == 0:
    #         new_list[0]["Hand"][k] = 0
    #         new_list[1]["Neck"][k] = 0
    #     print(new_list)
    return new_list


def relatvie_trait_shuffle():
    with open("./json/traits3.json") as f:
        data = json.load(f)
        traits = data["traits"]
        seed = data["seed"]
        relative_array = []
    for j in range(0, len(traits)):
        count = traits[j]["count"]
        name = traits[j]["name"]
        relatvie_list = []
        for i in range(0, count):
            index = traits[j]["type"][i]["index"]
            percent = traits[j]["type"][i]["percent"]
            color = traits[j]["type"][i]["color"]
            for k in range(0, len(color)):
                c_index = color[k]["index"]
                c_percent = color[k]["percent"]
                relatvie_list.extend([{
                    "t_index": index,
                    "c_index": c_index,
                }] * int(seed * percent / 100 * (c_percent / 100)))
            rd.shuffle(relatvie_list)
            rand_reresult = {f"{name}": relatvie_list}
            relative_array.append(rand_reresult)
    return array2dic(relative_array)


def generate_traits_list(result):
    all_traits = []
    for k in result:
        trait_id = []
        color_id = []
        for v in range(0, len(result[k])):
            trait_id.append(result[k][v]["t_index"])
            color_id.append(result[k][v]["c_index"])
        col_1 = {f"{k}": trait_id}
        col_2 = {
            f"{k}"
            "_color": color_id
        }
        newa = col_1 | col_2
        all_traits.append(newa)
    w = []
    for i in range(0, len(all_traits)):
        w.append(pd.DataFrame(all_traits[i]).astype("string"))
    df = pd.concat(w, axis=1)
    os.makedirs("./csv", exist_ok=True)
    df.to_csv("./csv/out_6.csv", index=False)


def generate_extract_list(result):
    # all_traits = []
    # for k in result:
    #     trait_id = []
    #     color_id = []
    #     for v in range(0, len(result[k])):
    #         trait_id.append(result[k][v]["t_index"])
    #     col_1 = {f"{k}": trait_id}
    #     col_2 = {
    #         f"{k}"
    #         "_color": color_id
    #     }
    #     newa = col_1 | col_2
    #     all_traits.append(newa)
    w = []
    for i in range(0, len(result)):
        w.append(pd.DataFrame(result[i]).astype("string"))
    df = pd.concat(w, axis=1)
    os.makedirs("./csv", exist_ok=True)
    df.to_csv("./csv/extra.csv", index=False)


if __name__ == "__main__":
    # generate_traits_list(relatvie_trait_shuffle())
    generate_extract_list(shuffle_mono_traits("./json/neck_and_hand.json"))
    generate_traits_list(shuffle_relative_traits("./json/body3.json"))
