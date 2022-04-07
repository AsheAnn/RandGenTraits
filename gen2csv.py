import random as rd
import pandas as pd
import os
import json


def randomTrait(name, count, seed):
    index = []
    for i in range(0, seed):
        traitIndex = rd.randint(0, count - 1)
        index.append(traitIndex)
    rd.shuffle(index)
    randResult = {f"{name}": index}
    return randResult


def generateTraitsList():
    with open("../trait/json/trait.json") as f:
        data = json.load(f)
        traits = data["traits"]
    nullList = []
    for j in range(0, len(traits)):
        name = traits[j]["name"]
        count = traits[j]["count"]
        seed = traits[j]["seed"]
        allTraits = randomTrait(name, count, seed)
        nullList.append(allTraits)
    result = {}
    for dic in nullList:
        result.update(dic)
    return result


def convertToCsv(allList):
    df = pd.DataFrame(data=allList).drop_duplicates(keep=False)
    os.makedirs("../trait/csv", exist_ok=True)
    df.to_csv("../trait/csv/out.csv")


if __name__ == "__main__":
    convertToCsv(generateTraitsList())
