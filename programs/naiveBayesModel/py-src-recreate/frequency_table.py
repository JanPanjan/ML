import numpy as np


class FrequencyTable:
    """
    vsak atribut ima svoj stolpec. to bo dictionary, nekako tako:
    Frequency_table = {
                          outlook: {
                              sunny: [2,3],
                              rainy: [3,2],
                              overcast: [4,0]
                          },
                          temperature: {
                              ...
                              ...
                          }
                      }
    """

    # ko ustvarimo instanco Table, se bo naredila celotna tabela
    # iz feature matrix in class vector

    def __init__(self, f_mat, col_names, c_vec) -> None:
        # ustvarimo dictionary z imeni atributov brez zadnjega, ker je class
        self.table = {atr: {} for atr in col_names}

        # v atr ustvarimo še dicts za vsako vrednost iz col_names
        # self.table['outlook']['sunny'] = {}
        # self.table['outlook']['rainy'] = {}
        # ...
        # moram dobit unikatne vrednosti vsakega atributa
        # to dobimo s set funkcijo
        self.uq_val_table = {f"{col_names[atr]}": list(set(f_mat[atr])) for atr in range(len(f_mat))}

        for x in range(len(col_names)):
            cur_col = col_names[x]
            cur_atr = self.uq_val_table[cur_col]

            for uq_val in cur_atr:
                self.table[cur_col][uq_val] = {}

        # prav tako moram dobit tabelo indeksov teh unikatnih vrednosti
        # np.where(f_mat[0] == "sunny")[0]
        # np.where(f_mat[0] == "rainy")[0]
        # np.where(f_mat[0] == "overcast")[0]
        # np.where(f_mat[1] == "high")[0]
        # ...
        self.val_id_table = {}

        # vals je list unikatnih elementov
        for id, vals in enumerate(self.uq_val_table.values()):
            for uq_val in vals:
                ids = np.where(f_mat[id] == uq_val)[0]
                self.val_id_table[uq_val] = list(ids)

        # zdaj ma vsak atribut dict za vsako vrednost
        # vsaka stolpec je nek atribut, right
        # torej moramo najprej dobiti celotni stolpec in nato gledati frekvence
        # najlažje bi bilo, če bi samo transponirali naš feature matrix
        # ker zdaj je tak:
        #       sunny, cold, high, false
        #       rainy, cold, mild, true
        #       ...
        # hočemo pa, da je tak:
        #       sunny, rainy ...
        #       cold, cold ...
        #       high, mild ...
        #       false, true ...
        # potem lahko preprosto loopamo in štejemo count yes in no,
        # ker bodo stolpci enake velikosti kot class vector
        # naj bo passana že transponirana matrika, da ne kličem
        # import še enkrat

        # gremo čez vsako vrstico po vrsti, da so colnames v
        # pravem redu dostopani
        # - vzami atribut outlook = atry
        # - pojdi čez vsako vrednost v atry
        # - shrani vrednost (sunny, rainy...) = occy
        # - shrani index vrednosti = indy
        # - shrani vrednost (yes,no) iz class vectorja na indexu indy
        # - v Frequency_table na mestu [atry][occy] shrani c_vec[indy]

        # hočemo zračunat kolikokrat se pojavi yes ali no za nek unique
        # value v atributu od f_mat
        # gremo v atribut skozi val_id_table

        for val_id, val in enumerate(self.val_id_table):
            print(val_id, val)
            # val_id je indeks trenutne unikatne vrednosti
            # val je string trenutne unikatne vrednosti
            # 0=sunny, 1=overcast, 2=rainy, 3=nov atribut,...

            # za vsak val ustvarimo frekvenčno tabelo, gremo
            # čez indekse val v f_mat preko id tabele in
            # preštejemo frekvence yes in no za val
            cls_freq_t = {"Yes": 0, "No": 0}

            for x in self.val_id_table[val]:
                # vzamemo indeks od idk sunny = x -> 0
                # dobimo class vrednost v c_vec = c_vec[x] -> "yes" or "no"
                # posodobimo cls_freq_t na mestu c_vec[x]
                cls_freq_t[c_vec[x]] += 1

            # freq table dodamo na pravo mesto v Table
            # to pomeni, da pospravimo na pravi atribut, na pravi
            # unique value
            # self.table[atribut][uq_val]
            # kako dobim atribut....

        for atr in self.table.keys():
            for id, uq_val in enumerate(self.table[atr].keys()):
                cls_freq_t = {"Yes": 0, "No": 0}

                # za vsak uq value preštejemo frekvence
                for val in self.val_id_table[uq_val]:
                    cls_freq_t[c_vec[val]] += 1

                # frekvence zapakiramo na pravo mesto
                # atribut: uq value = frekvence
                self.table[atr][uq_val] = cls_freq_t

