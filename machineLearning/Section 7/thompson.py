import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
data = pd.read_csv("advertisements.csv")

import random

N = 10000
d = 10
toplam = 0
oduller = [0] * d
secilenler = []
birler = [0] * d
sifirlar = [0] * d
for n in range(0,N):
    ad = 0
    maxUCB = 0
    for i in range(0,d):
        rasbeta = random.betavariate(birler[i] + 1, sifirlar[i] + 1)
        if rasbeta > maxUCB:
            maxUCB = rasbeta
            ad = i
    secilenler.append(ad)
    odul = data.values[n,ad]
    if odul == 1:
        birler[ad] = birler[ad] + 1
    else:
        sifirlar[ad] = sifirlar[ad] + 1
    oduller[ad] = oduller[ad] + odul
    toplam = toplam + odul
plt.hist(secilenler)
print("toplam ödül")
print(toplam)
















