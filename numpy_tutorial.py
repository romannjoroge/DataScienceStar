# Numpy can be used to represent and work with multi-dimensional arrays in a fast and easy way
# Numpy arrays have a fixed type, stores types using less space and uses contiguous memory

import numpy as np
# Initializing an array
a = np.array([1, 2, 3])
b = np.array([[1, 2 ,3],
              [4, 5, 6]]) # Multidimensional array
v = np.arange(10)  # To create a numpy array that has values from 0 to 9
w = v[v % 2 == 1]

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

# To multiply 2 matrices use function np.matmul()
k = np.full((2, 2), 4)
l = np.identity(2)
m = np.matmul(k, l)
print(m)
print(f"m's determinant is {np.linalg.det(m)}")

# Statistics
n = np.random.rand(4, 3)
print(n)
print(np.min(n))  # Smallest element in entire array
print(np.max(n))  # Biggest element in entire array
print(np.min(n, axis=0))  # Smallest element of every column, returns an array
print(np.max(n, axis=1))  # Biggest element of every row, returns an array
print(np.sum(n))  # Sum of all elements in array
print(np.sum(n, axis=0))  # Returns an array containing sums of all columns

# Reorgainizing
before = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
print(f"Array before reshaping is {before}")
after = before.reshape((2, 2, 2))  # Give the function the shape of the new array you want, the size of the new array must be the same as old one
print(f"Array after reshaping is {after}")
# To stack multiple arrays ontop of each other(vertical stacking), arrays should have same number of columns
o = np.array([[j for j in range(1, 5)] for i in range(1, 5)])
p = np.array([i for i in range(5, 9)])
print(o, p)
print(f"o and p vertically stacked is {np.vstack([o, p])}")
# To stack arrays horizontally use np.hstack, arrays should have the same number of rows
q = np.ones((3, 5))
r = np.zeros((3, 7))
print(f"q and r horizontally stacked makes{np.hstack([q, r])}")

# Miscellaneous
print(r.astype('int32'))  # Changes data types of elements in array and returns copy of changed array

# Boolean Masking and Advanced Masking
s = np.random.randint(1, 51, size=(100))
# To get a boolean array where the value in array is whether that element met a condition or not
t = s == 50
print(t)
# To get values that meet a condition, index array with booleans
print(s[s > 45])
# To see whether the columns / rows have any values that meet a condition
u = np.random.randint(5, 16, size=(4, 3))
print(u)
print(np.any(u > 10, axis=0)) # Return booleans of which columns have any values greater than 10
print(np.all(u > 10, axis=0)) # Return booleans for which columns have all values greater than 10
# ~ - not, & - and | - or
test = np.array([i for i in range(1, 31)])
test = test.reshape((6, 5))
print(test)
print(test[2:4, :2])
print(test[[0, 1, 2, 3], [1, 2, 3, 4]])
print(test[[0, 4, 5], -2:])
