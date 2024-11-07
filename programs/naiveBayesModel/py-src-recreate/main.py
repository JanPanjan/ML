import numpy as np


# naši podatki
# zadnji stolpec je class attribute
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

# ----- cilj 1 -----
# hočemo posebej feature matrix (tabelo atributov brez class) in
# class vector (vektor ali 1D array class vrednosti)

f_mat = rem_col(data=data, col_to_rem=4)


class Util:
    # class bo nosil rem_col (remove column) in ext_col (extract column)
    # funkciji, saj sta taki generični and we are all about reusability

    # funkcija bo naredila nov 2D array brez vrednosti na col indexu
    @staticmethod
    def rem_col(data: list, col_to_rem: int) -> list:
        new_ar = []

        for row in data:
            # ustvarimo novi array iz vseh razen col_to_rem
            new_row = [row[col] for col in range(len(row)) if row[col] != col_to_rem]

            # dodamo v novi array
            new_ar.append(new_row)

        return new_ar
