import numpy as np


class FrequencyTable:
    """ vsak atribut ima svoj stolpec. to bo dictionary, nekako tako:
        table = {
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

    istočasno se bo naredila še frekvenčna tabela deležev vrednosti:
        fr_table = {
            outlook: {
                sunny: { yes: 1+(2/9), no: 1+(3/5) },
                rainy: { yes: 1+(3/9), no: 1+(2/5) },
                overcast: { yes: 1+(4/9), no: 1+(0/5) }
            },
            temperature: {
                ...
                ...
            }
        }

    9 je število "yes" in 5 število "no" iz c_vec. prav tako moram vsem
    dodati 1, ker se npr. pri [outlook = overcast | no] pojavi 0 in bo
    motilo izračun verjetij.

        ***---------------------------------------------------------***
    ***-za zdaj bom pustil dve tabeli, drugače potrebujem samo to drugo-***
        ***---------------------------------------------------------***

    ko ustvarimo instanco Table, se bodo naredile vse tabele
    iz feature matrix, class vector in col_names
    """

    def __init__(self, f_mat, col_names, c_vec) -> None:
        self.table = {atr: {} for atr in col_names}
        self.fr_table = {atr: {} for atr in col_names}

        """ v atr ustvarimo še dicts za vsako vrednost iz col_names
            self.table['outlook']['sunny'] = {}
            self.table['outlook']['rainy'] = {}
            ...
        moram dobit unikatne vrednosti vsakega atributa
        to dobimo s set funkcijo """

        self.uq_val_table = {f"{col_names[atr]}": list(set(f_mat[atr])) for atr in range(len(f_mat))}

        for x in range(len(col_names)):
            cur_col = col_names[x]
            cur_atr = self.uq_val_table[cur_col]

            for uq_val in cur_atr:
                self.table[cur_col][uq_val] = {}
                self.fr_table[cur_col][uq_val] = {}

        """ prav tako moram dobit tabelo indeksov teh unikatnih vrednosti
            np.where(f_mat[0] == "sunny")[0]
            np.where(f_mat[0] == "rainy")[0]
            np.where(f_mat[0] == "overcast")[0]
            np.where(f_mat[1] == "high")[0]
            ...
        where vrne touple x in y vrednosti, kjer se pojavi vrednost v pogoju
        e.g. za sunny vrne [0,1,7,8,10] in [0,0,0,0,0], ker se vse vrednosti
        sunny v f_mat pojavijo v prvem stolpcu

        ker hočemo indekse atributu, vzamemo prvi array """

        self.val_id_table = {}

        for id, vals in enumerate(self.uq_val_table.values()):
            for uq_val in vals:
                ids = np.where(f_mat[id] == uq_val)[0]
                self.val_id_table[uq_val] = list(ids)

        """ gremo čez vsako vrstico po vrsti, da so colnames v
        pravem redu dostopani

        val je string trenutne unikatne vrednosti
            0=sunny, 1=overcast, 2=rainy, 3=nov atribut,...

        za vsak val ustvarimo frekvenčno tabelo za class vrednosti

        gremo čez vsak indeks unikatne vrednosti v class vektorju
        in prištejemo 1 yes ali no, glede na to kaj se nahaja na
        tistem indeksu

        e.g. sunny se pojavi na mestih 0,1,7,8,10 - na mestih
        0,1,7 ima no ter na 8,10 ima yes

        cls_freq_table dodamo na pravo mesto v Table - to pomeni, da 
        pospravimo na pravi atribut, na pravi unique value
            atribut: uq value = frekvence
            self.table[atribut][uq_val] 

        fr_table vsebuje uravnovešene vrednosti frekvenc
        """


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

        """ potrebujem še frekvence za class values, ki jih bom hranil posebej,
        da ne bo kake zmede. 

        grem čez c_vec in enako preštejem vrednosti za yes in no in nato še
        dobim deleže """

        self.cls_table = {"Yes": 0.0, "No": 0.0}

        for cls_val in c_vec:
            self.cls_table[cls_val] += 1

        self.cls_table["Yes"] = self.cls_table["Yes"] / len(c_vec)
        self.cls_table["No"]  = self.cls_table["No"] / len(c_vec)

