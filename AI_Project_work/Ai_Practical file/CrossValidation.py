# import modules

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# read data file from github
# dataframe: houseDf
gitFileURL = 'https://raw.githubusercontent.com/andrewgurung/data-repository/master/housing.csv'
cols = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
houseDf = pd.read_csv(gitFileURL, delim_whitespace=True, names = cols)

# convert into numpy array for scikit-learn
houseArr = houseDf.values

# Let's split columns into the usual feature columns(X) and target column(Y)
# Y represents the target 'MEDV' column
X = houseArr[:, 0:13]
Y = houseArr[:, 13]

# set k-fold count
folds = 10

# set seed to reproduce the same random data each time
seed = 7

# split data using KFold
kfold = KFold(n_splits=folds, random_state=seed, shuffle=True)

# instantiate a regression model
model = LinearRegression()

# set scoring parameter to 'neg_mean_absolute_error'
scoring = 'neg_mean_absolute_error'

# call cross_val_score() to run cross validation
resultArr = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)

# calculate mean of scores for all folds
mae = resultArr.mean()

# display Mean Absolute Error
# descending score(smallest score is best) is denoted by negative even though the value is positive
print("Mean Absolute Error: %.3f" % (mae))

