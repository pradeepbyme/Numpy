import numpy as np

# initializing arrays:

# Array Method
array1 = np.array([1, 2, 3, 4])
print(array1)
# Specifying DataType
array2 = np.array([1, 2, 3, 4])
print(array2)

# Zeros Method (Default datatype is float)
array3 = np.zeros((2,3), dtype=int)
print(array3)

# Ones Method (Default datatype is float)
array4 = np.ones((2,3), dtype=int)
print(array4)

# Empty Method
array5 = np.empty((2, 3), dtype=int, order='F')
print(array5)

# Reshaping array
array6 = np.arange(0, 10, 2).reshape(5, 1)
print(array6)

# Knowing the shape of an array
print(array6.shape)

# Knowing the size of an array (returns the number of elements)
print(array6.size)

# initializing an array using arange method
# arange(start,stop, step, dtype)
array7 = np.arange(0, 100, 20, dtype = float)
print(array7)

# linspace : similar to arange
array8 = np.linspace(10, 100, 10, endpoint = False, dtype = int)
print(array8)

# astype : changes the datatype
print(array8.astype('f')) # represents float

# dimension of an array
print(array8.ndim)
print(array7.reshape(5,1).ndim)
