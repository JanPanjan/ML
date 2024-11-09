import numpy as np
import util
from frequency_table import FrequencyTable

""" moji podatki. zadnji stolpec je class attribute """ 
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

""" ----- cilj 1 -----
hočem posebej feature matrix (tabelo atributov brez class) in
class vector (vektor ali 1D array class vrednosti)
ustvarim funkciji, ki bosta naredili subsets mojih tabel """
f_mat = util.rem_col(data, 4)
c_vec = util.ext_col(data, 4)

col_names = ["outlook", "temperature", "humidity", "windy", "play"]
fm_col_names = col_names[:len(col_names)-1]

""" ----- cilj 2 -----
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
ker bodo stolpci enake velikosti kot class vector """

fm_trans = np.array(f_mat).T  # T transponira matriko
ft = FrequencyTable(fm_trans, fm_col_names, c_vec)

util.pretty_print_dict(ft.table, "Class value frequencies")
util.pretty_print_dict(ft.fr_table, "Class value frequencies (float)")

""" frekvenčno tabelo imamo, potrebujemo še (mogoče) tabelo, kjer bodo deleži
frekvenc. kaj to pomeni:

	obstaja 9 "yes" in 5 "no". "sunny" ima 2x "yes" in 3x "no". "sunny" 
    pripomore h deležu od "yes" 2/9 in h "no" 2/5. prav tako imamo deleže
    za class atribut. "yes" je 9/14 in "no" 5/14.

v FrequencyTable razredu ustvarim še eno tabelo z deleži frekvenc vrednosti (tudi 
class), preko katere bom potem predictal class vrednosti v NaiveBayes razredu.  """








""" ----- cilj 3 -----
Zdaj mam frekvence, moram ustvariti model, ki bo predictal vrednosti.
Ustvarim NaiveBayes class, kjer bo naš model.
Najprej je treba model natrenirati s podatki """
