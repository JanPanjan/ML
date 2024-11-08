# ustvarimo novi array iz vseh razen col_to_rem
@staticmethod
def rem_col(data, *col_to_rem) -> list:
    new_ar = []

    for row in data:
        new_row = [row[col] for col in range(len(row)) if col not in col_to_rem]
        new_ar.append(new_row)

    return new_ar


# zgradi list iz col_to_ext stolpcev iz vseh row
@staticmethod
def ext_col(data, col_to_ext) -> list:
    return [row[col_to_ext] for row in data]


# ni pretty, ampak za zdaj je tko
@staticmethod
def pretty_print_dict(data, main):
    print("Table: ", main)
    eqs = "=" * (12 + len(main))
    print(f"{eqs}")
    for atr in data.items():
        spaces = "-" * (10 - len(atr[0]))
        print(atr[0], f"{spaces}-----------------------")
        for uq_val in data[atr[0]].items():
            print(f"  ", f"{uq_val[0]}:", " " * (8 - len(uq_val[0]))  , f"{uq_val[1]}")

