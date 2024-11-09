import numpy as np


class FrequencyTable:
    """
    vsak atribut ima svoj stolpec. to bo dictionary, nekako tako:
        Frequency_table = {
            outlook: {
                sunny: { yes: 2, no: 3 },
                rainy: { yes: 3, no: 2 },
                overcast: { yes: 4, no: 0 }
            },
            temperature: {
                ...
                ...
            }
        }
    ko ustvarimo instanco Table, se bo naredila celotna tabela
    iz feature matrix in class vector
    """
    def __init__(self, f_mat, col_names, c_vec) -> None:
        self.table = {atr: {} for atr in col_names}

        """
        v atr ustvarimo še dicts za vsako vrednost iz col_names
            self.table['outlook']['sunny'] = {}
            self.table['outlook']['rainy'] = {}
            ...
        moram dobit unikatne vrednosti vsakega atributa
        to dobimo s set funkcijo
        """
        self.uq_val_table = {f"{col_names[atr]}": list(set(f_mat[atr])) for atr in range(len(f_mat))}

        for x in range(len(col_names)):
            cur_col = col_names[x]
            cur_atr = self.uq_val_table[cur_col]

            for uq_val in cur_atr:
                self.table[cur_col][uq_val] = {}

        """
        prav tako moram dobit tabelo indeksov teh unikatnih vrednosti
            np.where(f_mat[0] == "sunny")[0]
            np.where(f_mat[0] == "rainy")[0]
            np.where(f_mat[0] == "overcast")[0]
            np.where(f_mat[1] == "high")[0]
            ...
        where vrne touple x in y vrednosti, kjer se pojavi vrednost v pogoju
        e.g. za sunny vrne [0,1,7,8,10] in [0,0,0,0,0], ker se vse vrednosti
        sunny v f_mat pojavijo v prvem stolpcu

        ker hočemo indekse atributu, vzamemo prvi array
        """
        self.val_id_table = {}

        for id, vals in enumerate(self.uq_val_table.values()):
            for uq_val in vals:
                ids = np.where(f_mat[id] == uq_val)[0]
                self.val_id_table[uq_val] = list(ids)

        """
        gremo čez vsako vrstico po vrsti, da so colnames v
        pravem redu dostopani

        val je string trenutne unikatne vrednosti
            0=sunny, 1=overcast, 2=rainy, 3=nov atribut,...

        za vsak val ustvarimo frekvenčno tabelo za class vrednosti

        gremo čez vsak indeks unikatne vrednosti v class vektorju
        in prištejemo 1 yes ali no, glede na to kaj se nahaja na
        tistem indeksu

        e.g. sunny se pojavi na mestih 0,1,7,8,10 - na mestih
        0,1,7 ima no ter na 8,10 ima yes

        freq table dodamo na pravo mesto v Table - to pomeni, da 
        pospravimo na pravi atribut, na pravi unique value
            atribut: uq value = frekvence
            self.table[atribut][uq_val]
        """
        for atr in self.table.keys():
            for id, uq_val in enumerate(self.table[atr].keys()):
                cls_freq_t = {"Yes": 0, "No": 0}

                # za vsak unique value preštejemo frekvence
                for val in self.val_id_table[uq_val]:
                    cls_freq_t[c_vec[val]] += 1

                self.table[atr][uq_val] = cls_freq_t
