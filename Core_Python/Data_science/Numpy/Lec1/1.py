# NUMPY
#
# Numpy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.
#
# Arrays
#
# > A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers.
#
# > The number of dimensions is the rank of the array
#
# > The shape of an array is a tuple of integers giving the size of the array along each dimension.

import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print(type(a))  # Prints "<class 'numpy.ndarray'>"
print(a)
print(a.shape)  # Prints "(3,)"
print(a[0], a[1], a[2])  # Prints "1 2 3"
a[0] = 5  # Change an element of the array
print(a)  # Prints "[5, 2, 3]"

b = np.array([[1, 2, 3], [4, 5, 6]])  # Prints "1 2 4" # Create a rank 2 array
print(b.shape)  # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])
