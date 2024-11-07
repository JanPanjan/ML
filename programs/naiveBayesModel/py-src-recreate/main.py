import numpy as np
import util


# moji podatki
# zadnji stolpec je class attribute
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

# ----- cilj 1 -----
# hočem posebej feature matrix (tabelo atributov brez class) in
# class vector (vektor ali 1D array class vrednosti)
# ustvarim funkciji, ki bosta naredili subsets mojih tabel
f_mat = util.rem_col(data, 4)
c_vec = util.rem_col(data, 0, 1, 2, 3)

print("================", "feature matrix:", "================")
util.pretty_print(f_mat)
print("================", "class vector:", "================")
util.pretty_print(c_vec)

"""
----- cilj 2 -----
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
                          sunny: [2,3],
                          rainy: [3,2],
                          overcast: [4,0]
                      },
                      temperature: {
                          ...
                          ...
                      }
                  }

vrednosti sunny: [2,3] pomeni, da imata dva sunny yes in trije sunny no
kaj moramo naredit torej:
  - vzami atribut outlook = atry
  - pojdi čez vsako vrednost v atry
  - shrani vrednost (sunny, rainy...) = occy
  - shrani index vrednosti = indy
  - shrani vrednost (yes,no) iz class vectorja na indexu indy
  - v Frequency_table na mestu [atry][occy] shrani c_vec[indy]

tako bom dobil frekvence za yes in no za vrednost sunny atributa outlook.
to moram ponoviti za vsako vrednost v vsakem atributu, da izgradim svoj 
Frequency_table.
"""
