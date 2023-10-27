import matplotlib.pyplot as plt
import numpy as np
# generate a sequence of integers

x = np.arange(20)

# create a second array using sinus

y = np.sin(x)

# the plot function makes a line chart of one array against another

plt.plot(x, y, marker="x")
plt.show()