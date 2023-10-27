import numpy as np
"""
array = np.arange(10)

print(array[5])
print(array[5:8])
array[5:8] = 12
print(array) 
 """

""" 
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array2d[2])
print(array2d[0][2])
print(array2d[0,2])

print(array2d[2][2])
print(array2d[2,2])
 """
""" 
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array3d)
print(array3d[0])

oldValues = array3d[0].copy()
array3d[0] = 42
print(array3d)

print(array3d[1,0])
print(array3d[1,0,1])
 """

# indexing with slices
"""
print(array[1:6])
print(array2d)
print(array2d[:2])
print(array2d[:2,1:])
print(array2d[1,:2])
print(array2d[2,:1])
print(array2d[:2,:1])
"""
# boolean indexing
""" 
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7,4)

print(names)

print(data)

 """
"""

Suppose each name corresponds to a row in the data array. If we wanted to select all
the rows with corresponding name 'Bob'. Like arithmetic operations, comparisons
(such as ==) with arrays are also vectorized. Thus, comparing names with the string
'Bob' yields a boolean array:
In [87]: names == 'Bob'
Out[87]: array([ True, False, False, True, False, False, False], dtype=bool)

"""
""" 
print(names == "Bob")


print(data[names == "Bob"])

print(data[names == "Bob", 2:])
print(data[names == "Bob", 3])
"""
""" 
print(names != "Bob")

mask = ((names == "Bob") | (names == "Will"))

print(data[mask])

data[data < 0] = 0
print(data)
data[names != 'Joe'] = 7

print(data)

"""

""" 
array4 = np.empty((8,4))

for i in range(8):
    array4[i] = i

print(array4)

print(array4[[4,3,0,6]])

print(array4[[-3,-5,-7]])

"""


# transposing array and swapping axes

array = np.arange(15).reshape((3,5))

print(array)
print(array.T)

array2 = np.random.randn(6,3)
print(np.dot(array2.T, array2))

array3 = np.arange(16).reshape((2,2,4))

print("For higher dimensional arrays, transpose will accept a tuple of axis numbers to permute the axes (for extra mind bending): \n", array3.transpose((1,0,2)))


