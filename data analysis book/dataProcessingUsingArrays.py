import numpy as np
import matplotlib.pyplot as plt


"""As a simple example, suppose we wished to evaluate the function sqrt(x^2 + y^2)
across a regular grid of values. The np.meshgrid function takes two 1D arrays and 
produces two 2D matrices corresponding to all pairs of (x, y) in the two arrays:
"""

points = np.arange(-5,5,0.01)
points1 = np.arange(-5,5,0.01)
xs, ys = np.meshgrid(points1,points)
print("xs : \n", xs)
print("ys : \n", ys)

z = np.sqrt(xs ** 2 + ys ** 2)
# plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.show()


# expressing conditional logic as array operations



""" The numpy.where function is a vectorized version of the ternary expression x if condi
tion else y. Suppose we had a boolean array and two arrays of values:
"""
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = np.where(condition=cond, x=xarr, y=yarr)



"""

The second and third arguments to np.where don’t need to be arrays; one or both of
them can be scalars. A typical use of where in data analysis is to produce a new array of
values based on another array. Suppose you had a matrix of randomly generated data
and you wanted to replace all positive values with 2 and all negative values with -2.
This is very easy to do with np.where:

"""




array = np.random.randn(4,4)

print(np.where(array > 0, 2, -2))



