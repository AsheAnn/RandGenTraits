import random as rd 
import csv
from itertools import zip_longest


def traitBody(Avalue, Bvalue, Cvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    l1 = [0] * a 
    l2 = [1] * b
    l3 = [2] * c
    la = l1 + l2 + l3
    rd.shuffle(la)
    Body = la
    index = range(0,MaxSeed)
    I = list(index)
    data = [I, Body]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_0.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerow(("index","Body"))
        wr.writerows(export_data)
        

def traitHead(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["Head"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_1.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)



def traitEyes(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["Eyes"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_2.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)

def traitMouth(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["Mouth"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_3.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)


def traitEars(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["Ears"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_4.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)

def traitHair(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["Hair"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_5.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)


def traitNose(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["Nose"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_6.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)

def traitEyebrow(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["Eyebrow"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_7.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)

def traitBodyGear(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["BodyGear"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_8.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)


def traitExtraGear(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["ExtraGear"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_9.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)


def traitHeadGear(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["HeadGear"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_10.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)


def traitBG(Avalue, Bvalue, Cvalue, Dvalue, MaxSeed):
    a = int(Avalue * MaxSeed)
    b = int(Bvalue * MaxSeed)
    c = int(Cvalue * MaxSeed)
    d = int(Dvalue * MaxSeed)
    Fl1 = [0] * a 
    Fl2 = [1] * b
    Fl3 = [2] * c
    Fl4 = [3] * d
    Fla = Fl1 + Fl2 + Fl3 + Fl4
    rd.shuffle(Fla)
    name = ["BG"]
    F = name + Fla
    data = [F]
    export_data = zip_longest(*data, fillvalue= '')
    with open('../trait/TD/trait_11.csv', 'w', newline= '') as f:
        wr = csv.writer(f)
        wr.writerows(export_data)



if __name__ == '__main__':
    seed = 1000
    traitBody(0.1, 0.45, 0.45, seed)
    traitHead(0.1, 0.3, 0.4, 0.2, seed)
    traitHair(0.2, 0.21, 0.39, 0.2, seed)
    traitMouth(0.2, 0.2, 0.5, 0.1, seed)
    traitNose(0.15, 0.22, 0.33, 0.3, seed)
    traitEars(0.2, 0.1, 0.3, 0.4, seed)
    traitEyes(0.4, 0.2, 0.2, 0.2, seed)
    traitEyebrow(0.01, 0.39, 0.25, 0.35, seed)
    traitBodyGear(0.3, 0.1, 0.4, 0.2, seed)
    traitHeadGear(0.5, 0.1, 0.2, 0.2, seed)
    traitExtraGear(0.1, 0.2, 0.3, 0.4, seed)
    traitBG(0.2, 0.2, 0.4, 0.2, seed)

