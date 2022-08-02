import os
import json
import random as rd
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


def relatvie_trait_shuffle():
    with open("./json/traits3.json") as f:
        data = json.load(f)
        traits = data["traits"]
        relative_array = []
    for j in range(0, len(traits)):
        count = traits[j]["count"]
        seed = traits[j]["seed"]
        name = traits[j]["name"]
        relatvie_list = []
        for i in range(0, count):
            index = traits[j]["type"][i]["index"]
            percent = traits[j]["type"][i]["percent"]
            color = traits[j]["type"][i]["color"]
            for k in range(0, len(color)):
                c_index = color[k]["index"]
                c_name = color[k]["name"]
                c_percent = color[k]["percent"]
                relatvie_list.extend([{
                    "t_index":
                    int(index),
                    "c_index":
                    int(c_index),
                    "traits_name":
                    c_name,
                    "score":
                    (calculate_score(count, percent,
                                     (seed * percent / 100), c_percent)),
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
        trait_name = []
        score = []
        for v in range(0, len(result[k])):
            trait_id.append(result[k][v]["t_index"])
            color_id.append(result[k][v]["c_index"])
            trait_name.append(result[k][v]["traits_name"])
            score.append(result[k][v]["score"])
        col_1 = {f"{k}": trait_id}
        col_2 = {
            f"{k}"
            "_color": color_id
        }
        col_3 = {"name": trait_name}
        col_4 = {"score": score}
        newa = col_1 | col_2 | col_3 | col_4
        all_traits.append(newa)
    w = []
    for i in range(0, len(all_traits)):
        w.append(pd.DataFrame(all_traits[i]))
    df = pd.concat(w, axis=1)
    os.makedirs("./csv", exist_ok=True)
    df.to_csv("./csv/out_4.csv")


if __name__ == "__main__":
    generate_traits_list(relatvie_trait_shuffle())
