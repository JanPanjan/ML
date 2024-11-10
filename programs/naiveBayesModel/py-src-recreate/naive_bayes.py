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
        self.p_yes = 1.0
        self.p_no  = 1.0

        self.msg_vals = {"Yes": [], "No": []}
        self.msg_nums = {"Yes": [], "No": []}

        # calculate likelihoods
        for x in range(len(input_vec)):
            cur_atr = self.feature_col_names[x]
            cur_val = input_vec[x]

            self.msg_vals["Yes"].append(cur_val)
            self.msg_vals["No"].append(cur_val)

            self.msg_nums["Yes"].append(self.ft.fr_table[cur_atr][cur_val]["Yes"])
            self.msg_nums["No"].append(self.ft.fr_table[cur_atr][cur_val]["No"])

            self.p_yes *= self.ft.fr_table[cur_atr][cur_val]["Yes"]
            self.p_no  *= self.ft.fr_table[cur_atr][cur_val]["No"]


        self.msg_vals["Yes"].append("class")
        self.msg_vals["No"].append("class")
        self.msg_nums["Yes"].append(self.ft.cls_table["Yes"])
        self.msg_nums["No"].append(self.ft.cls_table["No"])

        # multiply z yes in no frekvenco
        self.p_yes *= self.ft.cls_table["Yes"]
        self.p_no  *= self.ft.cls_table["No"]

        # normalize to get probability
        p_sum = self.p_yes + self.p_no
        self.p_yes = self.p_yes / p_sum
        self.p_no  = self.p_no  / p_sum

        self.probabilities = {"Yes": self.p_yes, "No": self.p_no}
        return self.probabilities

    
    def display_result(self, probabilities):
        print("\n=== likelihood for yes:", self.p_yes)
        for x in range(len(self.msg_vals["Yes"])):
            spc = " " * (6 - len(self.msg_vals["Yes"][x]))
            print("  ", self.msg_vals["Yes"][x], spc, self.msg_nums["Yes"][x])

        print("\n=== likelihood for no:", self.p_no)
        for x in range(len(self.msg_vals["No"])):
            spc = " " * (6 - len(self.msg_vals["No"][x]))
            print("  ", self.msg_vals["No"][x], spc, self.msg_nums["No"][x])

        print("\nPredictions:")
        print("==============================")
        for x in probabilities.items():
            spc = " " * (3 - len(x[0]))
            print(x[0], spc, f": {x[1] * 100} %")
