from typing import TextIO
import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Change strings to be file like
    train_file:TextIO = StringIO(train_string)
    test_file:TextIO = StringIO(test_string)

    # read in the training data and separate it to x_train and y_train
    # Converting the files to numpy arrays
    X = np.genfromtxt(train_file)
    Y = np.genfromtxt(test_file)

    # Extract features from numpy arrays
    X_label = X[:, -1]  # Training labels
    Y_label = Y[:, -1]  # Test labels
    X_data = np.delete(X, -1, axis=1) # Training data
    Y_data = np.delete(Y, -1, axis=1) # Test data

    # fit a linear regression model to the data and get the coefficients
    # using the np.linalg.lstsqr() function using training data
    coeff = np.linalg.lstsq(X_data, X_label)[0]

    # # print out the linear regression coefficients
    print(coeff)

    # # this will print out the predicted prics for the two new cabins in the test data set
    print(Y_data @ coeff)


main()
