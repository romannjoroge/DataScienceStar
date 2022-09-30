"""
    Uses the same bag of words concept to find the closest pair of sentences
    Distance is calculated using the manhattan algorithm
    Words are represented as TF_IDF vectors
    TF_IDF vectors values are calculated as tf * log10(1 / df)
"""
import math
from typing import List, Dict
from collections import Counter
import numpy as np
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

Vector = List[int]
Matrix = List[List[int]]

def main(text:str) -> Vector:
    """
    Returns the most similar pair of words in a text using tf-idf vectors
    text: A string containing the documents
    """

    # 1. split the text into words, and get a list of unique words that appear in it
    # Capitalize the text(so as to treat words with different capitalizations as the same)
    text = text.upper()
    # Split text into sentences usin .split('\n')
    sentences = text.split('\n')
    # Add a list of words in each sentence to another list
    words = [sentence.split(' ') for sentence in sentences]
    no_doc = len(words)
    # flatten it to get all words as a 1D array
    words_flattend = [x for sublist in words for x in sublist]
    # Get unique words from flattened array
    unique_words = np.unique(words_flattend)

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    # To calculate number of times a term occurs in each sentence I will create a Counter 
    # object from each sentence in words list
    term_counts = [Counter(sentence) for sentence in words]
    # From term_counts calculate term frequencies by dividing each count by sum of counts and store in dict
    term_frequencies:List[Dict[str, int]] = [{key:val / sum(count.values()) for key, val in count.items()} for count in term_counts]
    # Store document frequency as a dict where each unique word is a key and the value is the 
    # frequency of the word in the documents
    # List that has the number of times a word has been in all documents
    # For each unique word check if in each document and sum result
    word_counts = [sum([w in sent for sent in words]) for w in unique_words]
    # Use word_count to make document counts by zipping unique_words and word_counts and making
    # a dict from that
    doc_freq = {key:val/no_doc for key, val in zip(unique_words, word_counts)}

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    # Create a list of vectors, the value of the vectors will be the tf of word * log(1/df)
    tf_idf_representation:Matrix = [[sent[w] * math.log10(1 / doc_freq[w]) if w in sent else 0 for w in unique_words] for sent in term_frequencies]

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    def manhattan_dist(v1:Vector, v2:Vector) -> float:
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
        
        # Calculate the distances between each vector and all the other vectors and store in distances
        distances = np.array([[np.Inf if i==j else manhattan_dist(data[i], data[j]) for j in range(lenData)] for i in range(lenData)])

        # Find the index of the min arguement in distances, this is the indexes of the closest
        # vectors
        print(np.unravel_index(np.argmin(distances), distances.shape))
    find_nearest_pair(tf_idf_representation)

main(text)
