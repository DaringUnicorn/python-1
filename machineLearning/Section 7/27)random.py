import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("advertisements.csv")

import random

N = 10000
d = 10
toplam = 0
chosens = []
for n in range(0,N):
    ad = random.randrange(d)
    odul = data.values[n, ad]
    chosens.append(ad)
    toplam = toplam + odul

plt.hist(chosens)















