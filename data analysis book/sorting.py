import numpy as np

""" 
array = np.random.randn(8)

print(array)
print(array.sort())
"""
"""
Multidimensional arrays can have each 1D section of values sorted 
in-place along anaxis by passing the axis number to sort:
"""

array= np.random.randn(5,3)

print(array)

array.sort(1)
print(array)

