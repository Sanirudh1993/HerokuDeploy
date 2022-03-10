import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def marks_prediction(marks):


    X = pd.read_csv("Train_sample.csv")
    y = pd.read_csv("Train_sample_y.csv")

    X = X.values
    y = y.values

    model = LinearRegression()
    model.fit(X, y)

    X_test = np.array(marks).reshape((1, -1))


    return model.predict(X_test)[0]







