from typing import List, Tuple, Callable
import math

Vector = List[float]  # Creates a type alias
Matrix = List[Vector]

# A function to add vectors
def add(v:Vector, w:Vector) -> Vector:
    assert len(v) == len(w), "vectors must be of the same length"
    # Add the vectors and return it
    return [x + y for x, y in zip(v, w)]

# A function to subtract vectors
def subtract(v:Vector, w:Vector) -> Vector:
    assert len(v) == len(w), "vectors must have the same length"
    # Subtract the vectors and return it
    return [x - y for x,y in zip(v, w)]

# Compentwise sum more than 2 vectors
def vector_sum(vectors:List[Vector]) -> Vector:
    # Assert that the list of vectors is not empty
    assert vectors, "vectors should not be empty"
    
    # Assert that the length of all vectors are equal
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "vectors must be of the same size"

    # Return the i-th result of the sum of every vector
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

# Multiply a vector by a scalar
def scalar_multiply(c:float, v:Vector) -> Vector:
    """Multiplies every element in v by c"""
    return [c * x for x in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    """Does componentwise mean on the vector"""
    sum_vectors = vector_sum(vectors)
    no_elem = len(vectors)
    return scalar_multiply(1/no_elem, sum_vectors)

def dot(v:Vector, w:Vector) -> float:
    """Retruns the dot product of 2 vectors"""
    assert len(v) == len(w), "vectors should have the same length"
    return sum(x* y for x,y in zip(v, w))

def sum_of_squares(v:Vector) -> float:
    """Returns the dot product of the vector and its self"""
    return dot(v, v)

def magnitude(v:Vector) -> float:
    """Returns the magnitude of a vector"""
    return math.sqrt(sum_of_squares(v))

def squared_distance(v:Vector, w:Vector) -> float:
    """Retruns the squared distance between 2 vectors"""
    return sum_of_squares(subtract(v, w))

def distance(v:Vector, w:Vector) -> float:
    """Returns the distance between 2 vectors"""
    return math.sqrt(squared_distance(v, w))

assert add([1,2], [1,2]) == [2,4]
assert subtract([2,3], [1,1]) == [1,2]
assert vector_sum([[1,2], [1,2], [1,2], [1,2]]) == [4,8]
assert scalar_multiply(2, [1,2]) == [2,4]
assert vector_mean([[1,2], [1,2], [1,2]]) == [1,2]
assert dot([1, 2], [1,2]) == 5
assert sum_of_squares([1, 2, 3]) == 14
assert magnitude([3, 4]) == 5


def shape(A:Matrix) -> Tuple:
    """Returns the number of rows and columns in the matrix"""
    num_rows = len(A)
    num_col = len(A[0]) if A else 0  # Returns 0 if the matrix is empty
    return num_rows, num_col

def get_row(A:Matrix, i:int) -> Vector:
    """Returns the ith row of A"""
    return A[i]

def get_column(A:Matrix, i:int) -> Vector:
    """Returns the ith column of A"""
    return [x[i] for x in A]

def make_matrix(num_rows:int, 
                num_col:int, 
                func:Callable[[int, int], float]) -> Matrix:
    """Return a num_rows x num_col matrix whose (i,j)th entry
       is func(i, j)"""
    return [[func(i, j) for j in range(num_col)]
            for i in range(num_rows)]

def identity_matrix(n:int) -> Matrix:
    """Create a n x n identity matrix"""
    return make_matrix(n, n, lambda i,j: 1 if i == j else 0)

assert shape([[1,2], [1,2], [1, 2]]) == (3, 2)