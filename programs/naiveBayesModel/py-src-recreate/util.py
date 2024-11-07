from numpy import size
from pandas import DataFrame
from tabulate import tabulate


@staticmethod
def rem_col(data, *col_to_rem) -> list:
    new_ar = []

    for row in data:
        # ustvarimo novi array iz vseh razen col_to_rem
        new_row = [row[col] for col in range(len(row)) if col not in col_to_rem]

        # dodamo v novi array
        new_ar.append(new_row)

    return new_ar


@staticmethod
def ext_col(data, col_to_ext) -> list:
    # zgradi list iz col_to_ext stolpcev iz vseh row
    return [row[col_to_ext] for row in data]


@staticmethod
def pretty_print(data):
    # ni pretty, ampak za zdaj je tko
    [print(row) for row in data]
