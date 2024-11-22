import numpy as np
import pandas as pd
import util
from naive_bayes import NaiveBayes
from decision_tree import *


def main():
    # prebere podatke iz csv (predpostavi, da je prvi line header)
    data_csv = pd.read_csv("weather.csv", header=None).values.tolist()
    col_names = data_csv[0]
    # odstrani col names iz podatkov
    data = util.rem_row(data_csv, 0)
    # definira feature matrix in class vector
    X = util.rem_col(data, 4)  # vsi brez zadnjega so features
    Y = util.ext_col(data, 4)  # zadnji atribut je class

    # predelamo podatke z modelom
    nb = NaiveBayes()
    nb.train(X, Y, col_names)
    nb.display.table()
    nb.display.fr_table()

    # predicta class value glede na neko X vrstico
    case = ["Sunny", "Hot", "Normal", "False"]
    prediction_nb = nb.predict(case)
    nb.display.probabilities(prediction_nb)
    nb.display.prediction(prediction_nb)

    # ---- decision treeeee ----
    dt = DecisionTree()
    dt.train(X, Y, col_names)
    prediction_dt = dt.predict(case)
    print("\n", prediction_dt)

if __name__ == "__main__":
    main()