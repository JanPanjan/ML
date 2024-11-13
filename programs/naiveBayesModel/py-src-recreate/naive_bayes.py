from frequency_table import FrequencyTable
from display import Display
from numpy import array


class NaiveBayes:
    def __init__(self) -> None:
        self.display = Display(self)

    def train(self, X, Y, col_names) -> None:
        f_mat = array(X).T
        c_vec = Y
        self.feature_col_names = col_names[:-1]
        self.ft = FrequencyTable(f_mat, self.feature_col_names, c_vec)

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
    def predict(self, case):
        # spremenljivki za verjetnost
        self.p_yes = 1.0
        self.p_no  = 1.0

        # dobi likelihoods za yes in no
        for val in range(len(case)):
            cur_atr = self.feature_col_names[val]
            cur_val = case[val]

            self.p_yes *= self.ft.fr_table[cur_atr][cur_val]["Yes"]
            self.p_no  *= self.ft.fr_table[cur_atr][cur_val]["No"]

        # množi še s frekcencami za yes in no
        self.p_yes *= self.ft.cls_table["Yes"]
        self.p_no  *= self.ft.cls_table["No"]

        # izračuna verjetnost
        p_sum = self.p_yes + self.p_no
        self.p_yes = self.p_yes / p_sum
        self.p_no  = self.p_no  / p_sum

        self.probabilities = {"Yes": self.p_yes, "No": self.p_no}
        return self.probabilities
