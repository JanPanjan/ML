# ustvari novi array iz vseh razen col_to_rem
@staticmethod
def rem_col(data, *col_to_rem) -> list:
    new_ar = []

    for row in data:
        new_row = [row[col] for col in range(len(row)) if col not in col_to_rem]
        new_ar.append(new_row)

    return new_ar

# ustvari novi array brez podane vrstice
@staticmethod
def rem_row(data, row_to_rem):
    return [data[row] for row in range(len(data)) if row != row_to_rem]

# zgradi list iz col_to_ext stolpcev iz vseh row
@staticmethod
def ext_col(data, col_to_ext) -> list:
    return [row[col_to_ext] for row in data]