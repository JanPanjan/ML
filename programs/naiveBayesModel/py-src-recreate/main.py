import numpy as np
import util
from frequency_table import FrequencyTable
from naive_bayes import NaiveBayes

# moji podatki. zadnji stolpec je class attribute
data = np.array([
    ["Sunny", "Hot", "High", "False", "No"],
    ["Sunny", "Hot", "High", "True", "No"],
    ["Overcast", "Hot", "High", "False", "Yes"],
    ["Rainy", "Mild", "High", "False", "Yes"],
    ["Rainy", "Cool", "Normal", "False", "Yes"],
    ["Rainy", "Cool", "Normal", "True", "No"],
    ["Overcast", "Cool", "Normal", "True", "Yes"],
    ["Sunny", "Mild", "High", "False", "No"],
    ["Sunny", "Cool", "Normal", "False", "Yes"],
    ["Rainy", "Mild", "Normal", "False", "Yes"],
    ["Sunny", "Mild", "Normal", "True", "Yes"],
    ["Overcast", "Mild", "High", "True", "Yes"],
    ["Overcast", "Hot", "Normal", "False", "Yes"],
    ["Rainy", "Mild", "High", "True", "No"]
])

def main():
    """ Model bo vzel vrstico (en occurence), iz frekvenčne tabele dobil frekvenčne deleže
    vseh vrednosti, izračunal verjetnosti in vrnil verjetnost za "yes" in "no". 

    delaj se, da je zgornji data tvoj training dataset. 

    1. najprej model natreniramo (dobimo frekvence in verjetnosti),
    2. nato predictamo nekaj iz novih podatkov (glej case_1). 

    e.g. java:
        String[][] X = Util.removeColumn(data, 4);
        String[] Y = Util.extractColumn(data, 4);

        NaiveBayes nb = new NaiveBayes();
        nb.train(X, Y);
        nb.display();

        String[] toPredict = { "Sunny", "Hot", "High", "False" };
        String prediction = nb.predict(toPredict); """

    col_names = ["outlook", "temperature", "humidity", "windy", "play"]

    X = util.rem_col(data, 4)
    Y = util.ext_col(data, 4)

    nb = NaiveBayes()
    nb.train(X, Y, col_names)
    nb.display.table()

    case_1 = ["Sunny", "Hot", "Normal", "False"]
    prediction_1 = nb.predict(case_1)
    nb.display.probabilities(prediction_1)
    nb.display.prediction(prediction_1)

if __name__ == "__main__":
    main()


""" CILJ 1 -----
hočem posebej feature matrix (tabelo atributov brez class) in
class vector (vektor ali 1D array class vrednosti)
ustvarim funkciji, ki bosta naredili subsets mojih tabel.

CILJ 2 -----
moram naredit frequency table s frekvencami yes no za vsak atribut
s tem namenom bom ustvaril nov razred Frequency_table, ki bo izgledal
tako:
    outlook
      sunny: [2, 3]
      rainy: [3, 2]
      overcast: [4, 0]

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

najprej moramo dobiti celotni stolpec in nato gledati frekvence
najlažje bi bilo, da samo transponiramo naš feature matrix
ker zdaj je tak:
      sunny, cold, high, false
      rainy, cold, mild, true
      ...
hočemo pa, da je tak:
      sunny, rainy ...
      cold, cold ...
      high, mild ...
      false, true ...
potem lahko preprosto loopamo in štejemo count yes in no,
ker bodo stolpci enake velikosti kot class vector.

frekvenčno tabelo imamo, potrebujemo še (mogoče) tabelo, kjer bodo deleži
frekvenc. kaj to pomeni:

        obstaja 9 "yes" in 5 "no". "sunny" ima 2x "yes" in 3x "no". "sunny" 
    pripomore h deležu od "yes" 2/9 in h "no" 2/5. prav tako imamo deleže
    za class atribut. "yes" je 9/14 in "no" 5/14.

v FrequencyTable razredu ustvarim še eno tabelo z deleži frekvenc vrednosti (tudi 
class), preko katere bom potem predictal class vrednosti v NaiveBayes razredu.

CILJ 3 -----
Zdaj mam frekvence, moram ustvariti model, ki bo predictal vrednosti.
To bo class NaiveBayes. Mislim, da vse kar moramo naredit right now je to,
da ustvarim frequency table v njem in iz frekvenc izračunam verjetnost
za class values glede na Bayes-ovo formulo.

    --- --- --- disclaimer --- --- --- --- --- --- --- --- --- --- --- --- ---
    - Basically, NaiveBayes bo naredil vse, zdaj je v main, samo zato, da    -
    - vidim kaj se dogaja, drugače mislim naredit tako, da se to vse zgodi v -
    - NaiveBayes.                                                            -
    --- --- --- disclaimer --- --- --- --- --- --- --- --- --- --- --- --- ---

Model bo vzel vrstico (en occurence), iz frekvenčne tabele dobil frekvenčne deleže
vseh vrednosti, izračunal verjetnosti in vrnil verjetnost za "yes" in "no". """
