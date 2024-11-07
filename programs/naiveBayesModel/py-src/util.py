@staticmethod
def remove_column(data, col_to_remove):
    new_data = []

    for row in data:
        # naredi list iz elementov row[col], kjer je col 0,...,len(row)
        # preskoči iteracijo, ko je col enak col_to_remove
        new_row = [row[col] for col in range(len(row)) if col != col_to_remove]
        new_data.append(new_row)

    return new_data


@staticmethod
def extract_column(data, col_to_extract):
    # za vsak row iz data vrne element na indeksu col_to_extract
    return [row[col_to_extract] for row in data]


@staticmethod
def unique(cols):
    unique_vals = []

    # za vsak item v stolpcu doda v unique_vals samo tiste, ki še niso notri
    for item in cols:
        if item not in unique_vals:
            unique_vals.append(item)

    return unique_vals
