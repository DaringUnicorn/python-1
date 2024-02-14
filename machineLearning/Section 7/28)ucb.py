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
tiklamalar = [0] * d
secilenler = []
for n in range(0,N):
    ad = 0
    maxUCB = 0
    for i in range(0,d):
        if (tiklamalar[i] > 0):
           ortalama = oduller[i] / tiklamalar[i]
           delta = math.sqrt(3/2*math.log(n) / tiklamalar[i])
           ucb = ortalama + delta
        else:
            ucb = N * 10
        if maxUCB < ucb:
            maxUCB = ucb
            ad = i
    secilenler.append(ad)
    tiklamalar[ad] = tiklamalar[ad] + 1
    odul = data.values[n,ad]
    oduller[ad] = oduller[ad] + odul
    toplam = toplam + odul
plt.hist(secilenler)
print("toplam ödül")
print(toplam)















