import numpy as np
import util
from frequency_table import FrequencyTable
from naive_bayes import NaiveBayes


# moji podatki. zadnji stolpec je class attribute
data = np.array([
    ["Sunny", "Hot", "High", "False", "No"],
    ["Sunny", "Hot", "High", "True", "No"],
    ["Overcast", "Hot", "High", "False", "Yes"],
    ["Rainy", "Mild", "High", "False", "Yes"],
    ["Rainy", "Cool", "Normal", "False", "Yes"],
    ["Rainy", "Cool", "Normal", "True", "No"],
    ["Overcast", "Cool", "Normal", "True", "Yes"],
    ["Sunny", "Mild", "High", "False", "No"],
    ["Sunny", "Cool", "Normal", "False", "Yes"],
    ["Rainy", "Mild", "Normal", "False", "Yes"],
    ["Sunny", "Mild", "Normal", "True", "Yes"],
    ["Overcast", "Mild", "High", "True", "Yes"],
    ["Overcast", "Hot", "Normal", "False", "Yes"],
    ["Rainy", "Mild", "High", "True", "No"]
])

def main():

    col_names = ["outlook", "temperature", "humidity", "windy", "play"]

    X = util.rem_col(data, 4)
    Y = util.ext_col(data, 4)

    nb = NaiveBayes()
    nb.train(X, Y, col_names)
    nb.display.table()

    case_1 = ["Sunny", "Hot", "Normal", "False"]
    prediction_1 = nb.predict(case_1)
    nb.display.probabilities(prediction_1)
    nb.display.prediction(prediction_1)

if __name__ == "__main__":
    main()
