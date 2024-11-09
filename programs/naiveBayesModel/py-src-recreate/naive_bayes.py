from frequency_table import FrequencyTable
import numpy as np
import util


class NaiveBayes:
    def __init__(self, data, col_names) -> None:

        self.feature_col_names = col_names[:-1]
        self.f_mat = np.array(util.rem_col(data, 4)).T
        self.c_vec = util.ext_col(data, 4)

        self.ft = FrequencyTable(self.f_mat, self.feature_col_names, self.c_vec)

    """ Ko mislimo predictat nekaj, to pomeni, da mu 
    podamo podatke o outlook, temperature, humidity in windy,
    ter hočemo predictat kaka bo play vrednost (class). 

    prediction naredimo iz izračunanih frekvenc. e.g. dobimo
    vrstico "Sunny", "Hot", "High", "True". Dobimo frekvenco
    za vsako vrednost in jih množimo skupaj, da dobimo verjetje
    (likelihood). 

        yes = 2/9 × 3/9 × 3/9 × 3/9 × 9/14 = 0,0053
        no  = 3/5 × 1/5 × 4/5 × 3/5 × 5/14 = 0,0206

    V verjetnost pretvorimo tako, da delimo verjetje za class 
    z vsoto class verjetjih.

        P(yes) = P(podatki|yes) / (P(podatki|yes) + P(podatki|no)) 
        P(no)  = P(podatki|no)  / (P(podatki|yes) + P(podatki|no)) 
    """
    def predict(self, input_vec):
        p_yes = 1.0
        p_no  = 1.0

        # calculate likelihoods
        print("\n=== calculating likelihoods")
        for x in range(len(input_vec)):
            cur_atr = self.feature_col_names[x]
            cur_val = input_vec[x]

            print(f"cur atr: {cur_atr}\ncur val: {cur_val}")

            y = self.ft.fr_table[cur_atr][cur_val]["Yes"]
            n = self.ft.fr_table[cur_atr][cur_val]["No"]

            print(f"cur val freq (yes): {y}")
            print(f"cur val freq (no): {n}")

            p_yes *= self.ft.fr_table[cur_atr][cur_val]["Yes"]
            p_no  *= self.ft.fr_table[cur_atr][cur_val]["No"]

        print("\n---raw calc:")
        print(p_yes)
        print(p_no)
        print("------------")

        # multiply z yes in no frekvenco
        print(self.ft.cls_table["Yes"])
        print(self.ft.cls_table["No"])

        p_yes *= self.ft.cls_table["Yes"]
        p_no  *= self.ft.cls_table["No"]

        print(p_yes)
        print(p_no)

        # normalize to get probability
        p_sum = p_yes + p_no
        p_yes = p_yes / p_sum
        p_no  = p_no  / p_sum

        print("after normalized")
        print(p_yes)
        print(p_no)
        print("sum :", p_yes + p_no)

        self.probabilities = {"Yes": p_yes, "No": p_no}
        return self.probabilities

    
    def display_result(self, probabilities):
        print("\nVerjetnosti za class vrednosti")
        print("==============================")
        for x in probabilities.items():
            spc = " " * (3 - len(x[0]))
            print(x[0], spc, f": {x[1] * 100} %")
