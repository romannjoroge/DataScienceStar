"""
    One of the methods of working with text is the bag of words method.
    In this method a sentence is represented as a List where the values are the counts of the
    words found in the text e.g for the text 'Hello there. I go to school there' the text would
    be represented as a list of 2 lists i.e
    [[1, 1, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1]]
    In this representation the order of the words in the sentence are lost, so only the counts of the 
    words are used.
    To see if 2 sentences are similar you use mahattan distance(sum of absolute difference of all dimensions)
"""

from typing import List
import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

Vector = List[int]  # Creating a type alias for List
Matrix = List[Vector]  # Creating a type alias for List[List[int]]

def manhattan_dist(v1:Vector, v2:Vector) -> int:
    """
    Returns the Manhattan difference between 2 vectors v1 and v2. 
    The function assumes that the vectors are not empty and that they have the same dimensions
    The distance is calculated as the sum of the absolute difference of every vector
    value(coordinate)
    """
    # Assertions
    assert v1, "v1 should not be empty"
    assert v2, "v2 should not be empty"
    assert len(v1) == len(v2), "v1 and v2 should have the same number of dimensions"

    # Create a list that contains the absolute differences between elements in vectors
    differences = [abs(x - y) for x,y in zip(v1, v2)]

    # Returns the sum of the differences
    return sum(differences)

def find_nearest_pair(data:Matrix) -> Vector:
    """
    Returns the most similar pair of vectors as a Vector where the values represent the index
    of the vector in a certain dimension.
    The function assumes that data is a non empty matrix and that all vectors in the matrix are
    of the same length

    data: Matrix
    """
    # Assertions
    assert data, "data should not be empty"
    lenData = len(data)

    # Create an empty matrix that has the same shape as data to store distances between vectors
    # Matrix will be of shape lenData x lenData
    distances = np.empty(shape=(lenData, lenData))
    
    # Calculate the distances between each vector and all the other vectors and store in distances
    for i in range(lenData):
        # Selects a vector to compare to all other vectors
        # Compare selected vector to all other vectors and store in distances
        for j in range(lenData):
            if i == j:
                distances[i][j] = np.Inf
            else:
                distances[i][j] = manhattan_dist(data[i], data[j])

    # Find the index of the min arguement in distances, this is the indexes of the closest
    # vectors
    print(np.unravel_index(np.argmin(distances), distances.shape))

find_nearest_pair(data)
