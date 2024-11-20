import numpy as np


class FrequencyTable:
    """ ko ustvarimo instanco Table, se bodo naredile vse tabele
    iz feature matrix, class vector in col_names """

    def __init__(self, f_mat, col_names, c_vec) -> None:
        self.table = {atr: {} for atr in col_names}
        self.fr_table = {atr: {} for atr in col_names}

        self.uq_val_table = {f"{col_names[atr]}": list(set(f_mat[atr])) for atr in range(len(f_mat))}

        for x in range(len(col_names)):
            cur_col = col_names[x]
            cur_atr = self.uq_val_table[cur_col]

            for uq_val in cur_atr:
                self.table[cur_col][uq_val] = {}
                self.fr_table[cur_col][uq_val] = {}


        self.val_id_table = {}

        for id, vals in enumerate(self.uq_val_table.values()):
            for uq_val in vals:
                ids = np.where(f_mat[id] == uq_val)[0]
                self.val_id_table[uq_val] = list(ids)


        def adjust_frequencies(freq_table: dict) -> dict:
            count_yes = c_vec.count("Yes")
            count_no = c_vec.count("No")

            return {
                "Yes": (0.1 + freq_table["Yes"]) / (count_yes + 0.1),
                "No": (0.1 + freq_table["No"]) / (count_no + 0.1)
            }


        for atr in self.table.keys():
            for id, uq_val in enumerate(self.table[atr].keys()):
                freq_t = {"Yes": 0, "No": 0}

                # ----- table -----
                for val in self.val_id_table[uq_val]:
                    freq_t[c_vec[val]] += 1

                self.table[atr][uq_val] = freq_t

                # ----- fr_table -----
                self.fr_table[atr][uq_val] = adjust_frequencies(freq_t)


        self.cls_table_adjusted = {"Yes": 0.0, "No": 0.0}
        self.cls_table = {"Yes": 0, "No": 0}

        for cls_val in c_vec:
            self.cls_table[cls_val] += 1


        self.cls_table_adjusted["Yes"] = self.cls_table["Yes"] / len(c_vec)
        self.cls_table_adjusted["No"]  = self.cls_table["No"] / len(c_vec)

