#
#
import tensorflow as tf
print(tf.__version__)
#
#
from tensorflow.keras.layers import Input, SimpleRNN, Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD, Adam

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
#
# Things you should automatically know and have memorized
# N = number of samples
# T = sequence length
# D = number of input features
# M = number of hidden units
# K = number of output units
# Make some data
N = 1
T = 10
D = 3
K = 2
X = np.random.randn(N, T, D)
# Make an RNN
M = 5 # number of hidden units
i = Input(shape=(T, D))
x = SimpleRNN(M)(i)
x = Dense(K)(x)

model = Model(i, x)
#
#
# Get the output
Yhat = model.predict(X)
print(Yhat)
#
#
# See if we can replicate this output
# Get the weights first
model.summary()
#
#
# See what's returned
model.layers[1].get_weights()
#
#
# Check their shapes
# Should make sense
# First output is input > hidden
# Second output is hidden > hidden
# Third output is bias term (vector of length M)
a, b, c = model.layers[1].get_weights()
print(a.shape, b.shape, c.shape)
#
#
Wx, Wh, bh = model.layers[1].get_weights()
Wo, bo = model.layers[2].get_weights()
#
#
h_last = np.zeros(M) # initial hidden state
x = X[0] # the one and only sample
Yhats = [] # where we store the outputs

for t in range(T):
  h = np.tanh(x[t].dot(Wx) + h_last.dot(Wh) + bh)
  y = h.dot(Wo) + bo # we only care about this value on the last iteration
  Yhats.append(y)
  
  # important: assign h to h_last
  h_last = h

# print the final output
print(Yhats[-1])
#
#
# Bonus exercise: calculate the output for multiple samples at once (N > 1)