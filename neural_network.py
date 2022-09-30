"""
    You can think of a nueral network like a bunch of logistic regression nodes connected to each other.
    The outputs from one layer becomes the inputs to the nodes in the next layer.
    You can have a bias which is added as a constant to the value calculated by the function in the node before
    activation
"""
import numpy as np

# Weights for the first hidden layer, where the values at the first column are the weights
# for the first node and the last column the second node
w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
                   [-2.75768443e-01,  3.43724167e-01],
                   [ 2.29138536e+01,  3.91783025e-01],
                   [-1.22397711e-02, -1.03029800e+00]])

# Weights for the second hidden layer, first column for first node and second column for
# second node
w1 = np.array([[11.5631751 , 11.87043684],
                   [-0.85735419,  0.27114237]])

# Weights for the output layer
w2 = np.array([[11.04122165],
                   [10.44637262]])

# Biases from first hidden
b0 = np.array([-4.21310294, -0.52664488])

# Bias for second hidden
b1 = np.array([-4.84067881, -4.53335139])

# Bias for output
b2 = np.array([-7.52942418])

# Training data
x = np.array([[111, 13, 12, 1, 161],
                 [125, 13, 66, 1, 468],
                 [46, 6, 127, 2, 961],
                 [80, 9, 80, 2, 816],
                 [33, 10, 18, 2, 297],
                 [85, 9, 111, 3, 601],
                 [24, 10, 105, 2, 1072],
                 [31, 4, 66, 1, 417],
                 [56, 3, 60, 1, 36],
                 [49, 3, 147, 2, 179]])

# Training labels
y = np.array([335800., 379100., 118950., 247200., 107950., 266550.,  75850.,
                93300., 170650., 149000.])


def hidden_activation(z:float) -> float:
    """Returns either 0 or z whatever is highest"""
    assert z, "z should not be empty"
    return max(0, z)

def output_activation(z):
    """Returns the input"""
    return z

x_test = [[82, 2, 65, 3, 516]]  # Input layer

# Pass through all the layers
# First hidden layer output should be a list of the outputs from the nodes in the hidden layer,
# items in input layer dot product weights added to bias
hidden1_outputs = [hidden_activation((x_test[0] @ w0[:, c]) + b0[c]) for c in range(w0.shape[1])]

# Make outputs of hidden layer 1 to be inputs of hidden layer 2
hidden2_outputs = [hidden_activation((hidden1_outputs @ w1[:, c])) + b1[c] for c in range(len(hidden1_outputs))]

# Make outputs of second hidden layer inputs of output layer
print((w2[0][0] * hidden2_outputs[0] + w2[1][0] * hidden2_outputs[1]) + b2[0])