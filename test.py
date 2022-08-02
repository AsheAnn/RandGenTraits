import os
import json
import random as rd
import pandas as pd


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


def relatvie_trait_shuffle():
    with open("../RandGenTraits/json/traits3.json") as f:
        data = json.load(f)
        traits = data["traits"]
        new_array = []
        relative_array = []
    for j in range(0, len(traits)):
        count = traits[j]["count"]
        seed = traits[j]["seed"]
        name = traits[j]["name"]
        new_list = []
        relatvie_list = []
        for i in range(0, count):
            index = traits[j]["type"][i]["index"]
            percent = traits[j]["type"][i]["percent"]
            traits_name = traits[j]["type"][i]["name"]
            color = traits[j]["type"][i]["color"]
            for k in range(0, len(color)):
                c_index = color[k]["index"]
                c_name = color[k]["name"]
                c_percent = color[k]["percent"]
                relatvie_list.extend([{
                    "t_index": index,
                    "c_index": c_index,
                }] * int(seed * percent / 100 * (c_percent / 100)))
            rd.shuffle(relatvie_list)
            rand_reresult = {f"{name}": relatvie_list}
            relative_array.append(rand_reresult)
            new_list.extend(([{
                "index": index,
                "name": traits_name,
                "score": calculate_score(count, percent),
            }] * count_value(seed, percent)))
            rd.shuffle(new_list)
        rand_result = {f"{name}": new_list}
        new_array.append(rand_result)
    return array2dic(relative_array)
    # return array2dic(new_array)


def generate_traits_list(result):
    al = []
    for k in result:
        idz = []
        tname = []
        for v in range(0, len(result[k])):
            idz.append(result[k][v]["t_index"])
            tname.append(result[k][v]["c_index"])
        la = {f"{k}": idz}
        laa = {"body_color": tname}
        newa = la | laa
        al.append(newa)
    w = []
    for i in range(0, len(al)):
        w.append(pd.DataFrame(al[i]))
    df = pd.concat(w, axis=1)
    os.makedirs("./csv", exist_ok=True)
    df.to_csv("./csv/out_4.csv")


if __name__ == "__main__":
    generate_traits_list(relatvie_trait_shuffle())
