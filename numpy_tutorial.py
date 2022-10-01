# Numpy can be used to represent and work with multi-dimensional arrays in a fast and easy way
# Numpy arrays have a fixed type, stores types using less space and uses contiguous memory

import numpy as np
# Initializing an array
a = np.array([1, 2, 3])
b = np.array([[1, 2 ,3],
              [4, 5, 6]]) # Multidimensional array

# General info - number of dimensions, shape, number of elements, size of elements and data type of elements
# Get number of dimension of array
print(f"a has {a.ndim} dimensions!")
print(f"b has {b.ndim} dimensions!")

# Getting shape
print(f"a's shape is{a.shape}")
print(f"b's shape is{b.shape}")  # Is a tuple containing number of rows and columns

c = np.array([[1, 2, 3]])
print(f"Even tho a and c both have 1 array c has {c.ndim} dimensions and has a shape of {c.shape}")

# Get data type of elements in array and size of each element
print(f"a has {a.dtype} in it and each are {a.itemsize}")

# Get number of elements in array
print(f"a has {a.size} elements")

# Accessing / Changing specific elements, rows, columns etc
# Index the arrays using numbers, lists, start:stop:step
# Specify both row and column
d = np.array([[1, 2, 3, 4, 5, 6, 7],
              [8, 9, 10, 11, 12, 13, 14]])

# Getting an element in a specific row and column e.g to get 13 we go to second row 6th column
print(d[1, 5]) # Index using [row, column] or [row][column]

# Get an entire row / column [r, :] or [:, c]
print(d[0:, ])

# You can also index using [start:stop:step]
print(d[0, 1::2])

# You can index using a list of values
print(d[1, [0, 1, 3, 4, 5]])

# To change an element in the array you get its index and change e.g to change element at 1st row third column
d[0, 2] = 20

# To initialize a matrix full of zeros use np.zeros(shape), full of ones use np.ones(shape), full of any value np.full(shape, value)
e = np.zeros((4, 4))
print(e)
f = np.full((7), 100) # Create a vector full of 100s
print(f"The marks for this sem will be {f}")
# Initialize a matrix full of random numbers
g = np.random.rand(2, 2) # 2 by 2 matrix filled with random values between 1 and 0
print(g)
h = np.random.randint(1, 3, size=(2,2))  # Create a 2 by 2 matrix with random ints between 1 and 3
print(h)
# Get 3 x 3 identity matrix
print(np.identity(3))
i = np.ones((5, 5))
i[1:4, 1:4] = np.zeros((3,3))
i[2, 2] = 9
print(i)

j = i.copy() # Assign a copy of i to j

# Element wise operations
print(j + 2)
# Perform a function on all array elements
print(np.sin(j))