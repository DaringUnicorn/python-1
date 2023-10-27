import numpy as np

data = np.array([[ 0.9526, -0.246 , -0.8856], [ 0.5639, 0.2379, 0.9104]])

print(data)
print(data + data)
print(data * 10)
print(data.shape)
print(data.dtype)

data1 = [6, 7.5, 8, 0, 1]

array1 = np.array(data1)

print(array1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]


array2 = np.array(data2)

print(array2)
print(array2.shape)

# creating zeros arrays

print(np.zeros(10))
print(np.zeros((3,6)))

print(np.empty((2,3,2)))

"""
short list of standard numpy array functions

array Convert input data (list, tuple, array, or other sequence type) to an ndarray either by
inferring a dtype or explicitly specifying a dtype. Copies the input data by default.


asarray Convert input to ndarray, but do not copy if the input is already an ndarray
arange Like the built-in range but returns an ndarray instead of a list.


ones, ones_like Produce an array of all 1’s with the given shape and dtype. ones_like takes another
array and produces a ones array of the same shape and dtype.


zeros, zeros_like Like ones and ones_like but producing arrays of 0’s instead


empty, empty_like Create new arrays by allocating new memory, but do not populate with any values like
ones and zeros


eye, identity Create a square N x N identity matrix (1’s on the diagonal and 0’s elsewhere)

"""


array3 = np.array([[1., 2., 3.], [4., 5., 6.]])

print(array3)
print(array3 * array3)
print(array3 - array3)
print(1/array3)
print(array3 ** 0.5)


