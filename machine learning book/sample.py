import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import mglearn

x, y = mglearn.datasets.make_forge()
plt.scatter(x[:,0], x[:,1], c=y, s=60, cmap=mglearn.cm2)

print("x.shape %s" %(x.shape,))

plt.show()


x, y = mglearn.datasets.make_wave(n_samples=40)

plt.plot(x, y, 'o')
plt.plot(x, -3 * np.ones(len(x)), 'o')
plt.ylim(-3.1, 3.1)

plt.show()