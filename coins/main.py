from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np


def area(LB, label=1):
    return (LB == label).sum()


def areas(LB,label):
    coins = []
    for i in range(1,label+1):
        coins.append(area(LB,i))
    coins = sorted(coins)
    return coins


def unq(lst):
    unq_nmb = []
    for i in lst:
        if i not in unq_nmb and i != 0:
            unq_nmb.append(i)
        else:pass
    return sorted(unq_nmb)


im = np.load("coins.npy.txt")

lb = label(im)

coins = areas(lb,lb.max()+1)
nom = unq(coins)

ones = coins.count(nom[0])
twos = coins.count(nom[1]) * 2
fives = coins.count(nom[2]) * 5
tens = coins.count(nom[3]) * 10

print(ones+twos+fives+tens)