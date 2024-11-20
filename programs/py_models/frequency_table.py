import numpy as np


class FrequencyTable:
    """ ko ustvarimo instanco Table, se bodo naredile vse tabele
    iz feature matrix, class vector in col_names """

    def __init__(self, f_mat: list, col_names: list, c_vec: list) -> None:
        self.c_vec = c_vec
        self.f_mat = f_mat

        # table ----------- tabela frekvenc vrednosti glede na class atribut
        # fr_table -------- tabela deležev?verjetij?frekvenc vrednosti glede na class atribut
        # uq_val_table ---- tabela unikatnih vredosti vsakega feture atributa
        # val_id_table ---- tabela indeksov vrednosti znotraj atributov
        self.table = {atr: {} for atr in col_names}
        self.fr_table = {atr: {} for atr in col_names}
        self.uq_val_table = {f"{col_names[atr]}": list(set(f_mat[atr])) for atr in range(len(f_mat))}
        self.val_id_table = {}

        # za vsako vrednost v vsakem atributu  ustvari 
        # placeholder dictionary za frekvence
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


        # poračuna frekvence in verjetnosti vseh unikatnih vrednosti v 
        # vseh atributih glede na class value
        for atr in self.table.keys():
            for id, uq_val in enumerate(self.table[atr].keys()):
                freq_t = {"Yes": 0, "No": 0}

                # ----- table -----
                for val in self.val_id_table[uq_val]:
                    freq_t[c_vec[val]] += 1

                self.table[atr][uq_val] = freq_t
                self.fr_table[atr][uq_val] = freq_t

                # ----- fr_table -----
                # adjusted
                self.fr_table[atr][uq_val] = self.__adjust_feature(freq_t, 0.1)


        # tabeli za frekvence in verjetnosti class vrednosti
        self.cls_table_adjusted = {"Yes": 0.0, "No": 0.0}
        self.cls_table = {"Yes": 0, "No": 0}

        for cls_val in c_vec:
            self.cls_table[cls_val] += 1

        self.cls_table_adjusted = self.__adjust_class(self.cls_table, 0.1)

        return


    """Funckiji aplicirata Laplace (additive) smoothing, kar je ključno
    za naš model. Vse frekvence spremeni za faktor alpha (smoothing
    parameter) enakomerno, da izniči ničelne vrednosti. Ker se verjetnosti
    smoothajo različno glede na atribute, je funckionalnost razdeljena na
    __adjust_feature, ki smootha vrednosti feature atributov ter 
    __adjust_class, ki smootha vrednosti class atributa """
    def __adjust_feature(self, table: dict, alpha=1) -> dict:
        """ 
        Smooth feature values probabilities.

        @param table: dict of size 2 with yes and no probabilities for a
        given feature attribute value.
        @param alpha: smoothing scalar. default 1.
        @returns: dict with adjusted values. 
        """
        count_yes = self.c_vec.count("Yes")
        count_no = self.c_vec.count("No")
        return {
            "Yes": ((alpha + table["Yes"]) / (count_yes + alpha)),
            "No": ((alpha + table["Yes"]) / (count_no + alpha))
        }

    def __adjust_class(self, table: dict, alpha=1) -> dict:
        """ 
        Smooth class values probabilities.

        @param table: dict of size 2 with yes and no probabilities for a
        given class attribute value.
        @param alpha: smoothing scalar. default 1.
        @returns: dict with adjusted values. 
        """
        c_len = len(self.c_vec)
        return {
            "Yes": ((alpha + table["Yes"]) / (c_len + 2*alpha)),
            "No": ((alpha + table["No"]) / (c_len + 2*alpha))
        }