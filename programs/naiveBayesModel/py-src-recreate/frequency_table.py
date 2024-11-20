import numpy as np


class FrequencyTable:
    """ ko ustvarimo instanco Table, se bodo naredile vse tabele
    iz feature matrix, class vector in col_names """

    def __init__(self, f_mat, col_names, c_vec) -> None:
        # tabela frekvenc vrednosti glede na class atribut
        self.table = {atr: {} for atr in col_names}
        # tabela deležev?verjetij?frekvenc vrednosti glede na class atribut
        self.fr_table = {atr: {} for atr in col_names}
        # tabela unikatnih vredosti vsakega feture atributa
        self.uq_val_table = {f"{col_names[atr]}": list(set(f_mat[atr])) for atr in range(len(f_mat))}
        # tabela indeksov vrednosti znotraj atributov
        self.val_id_table = {}

        # za vsako vrednost v vsakem atributu  ustvari placeholder 
        # dictionary za frekvence
        for x in range(len(col_names)):
            atr = col_names[x]
            atr_vals = self.uq_val_table[atr]

            for uq_val in atr_vals:
                self.table[atr][uq_val] = {}
                self.fr_table[atr][uq_val] = {}

        # najde indekse vseh unikatnih vrednosti v feature matriki
        for id, vals in enumerate(self.uq_val_table.values()):
            for uq_val in vals:
                ids = np.where(f_mat[id] == uq_val)[0]
                self.val_id_table[uq_val] = list(ids)


        """Funckija aplicira Laplace (additive) smoothing, kar je ključno
        za naš model. Vse frekvence spremeni za faktor alpha (smoothing
        parameter) enakomerno, da izniči ničelne vrednosti. 
        Ker se frekvence smoothajo malo drugače glede na features in class
        vrednosti, odloča cls parameter, ali naj uporabi kalkulacijo za 
        fatures ali class vrednosti. """
        def __adjust_features(alpha, c_val, c_val_count) -> float:
            return ((alpha + f_val) / (count + alpha))

        def __adjust_class(alpha, c_val, c_vec_len) -> float:
            return ((alpha + c_val) / (c_vec_len + 2*alpha))

        def __adjust_frequencies(self, table, smoothing_type, alpha=1) -> dict:
            match smoothing_type:
                case "feature":
                    count_yes = c_vec.count("Yes")
                    count_no = c_vec.count("No")

                    return {
                        "Yes": __adjust_features(alpha, "Yes", count_yes),
                        "No": __adjust_features(alpha, "No", count_no),
                    }

                case "class":
                    c_len = len(self.c_vec)
                    return {
                        "Yes": __adjust_class(alpha, "Yes", c_len),
                        "No": __adjust_class(alpha, "No", c_len)
                    }

        # poračuna frekvence in verjetnosti vseh unikatnih vrednosti v 
        # vseh atributih glede na class value
        for atr in self.table.keys():
            for id, uq_val in enumerate(self.table[atr].keys()):
                freq_t = {"Yes": 0, "No": 0}

                # ----- table -----
                for val in self.val_id_table[uq_val]:
                    freq_t[c_vec[val]] += 1

                self.table[atr][uq_val] = freq_t

                # ----- fr_table -----
                self.fr_table[atr][uq_val] = __adjust_frequencies(freq_t)


        # tabeli za frekvence in verjetnosti class vrednosti
        self.cls_table_adjusted = {"Yes": 0.0, "No": 0.0}
        self.cls_table = {"Yes": 0, "No": 0}

        for cls_val in c_vec:
            self.cls_table[cls_val] += 1

        self.cls_table_adjusted["Yes"] = self.cls_table["Yes"] / len(c_vec)
        self.cls_table_adjusted["No"]  = self.cls_table["No"] / len(c_vec)

