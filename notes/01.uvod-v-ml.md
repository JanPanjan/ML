# Podatkovno rudarjenje in strojno učenje

Zaradi neskončne količine podatkov, je pomembno podatkovno rudarjenje.
Ponavadi vseh podatkov ne uporabimo za analize, zato je pomembno, da
se podatki sproti evaluirajo.

Razlika med strojnim učenjem in ne-strojnim učenjem je v tem, kdo dela delo.
Če ti odločaš in ugotavljaš glede na podatke od računalnika, to je machine learning.
Če dela namesto tebe nekdo odločitve, je to AI.

Najbolj pogoste tehnike ML:

- Klasifikacija/napovedovanje razreda primerov
- Regresija/ocenjevanje vrednosti
- Razvrščanje v skupine (clustering)/iskanje skupin v podatkih
- Asociacije
- Vizualizacija/lažje odkrivanje zakonitosti
- Povzemanje/opisovanje skupin podatkov
- Odkrivanje odstopanj/iskanje znakov sprememb
- Analiza povezav/relacij med podatki

## Supervised learning

Imamo rešitev, ki jo nameravamo doseč s podatki. Ko delamo model, ga učimo
kako prit do te rešitve. Za treniranje modela uporabljamo **del** vseh podatkov.
AI se raje pifla kot *razume* podatke, zato lahko tako preverjaš, če tvoj
model sploh dela.

### Klasifikacija

Modeli z omejenimi možnimi odgovori. Model napove razred primera.

>Npr. prepoznavanje psov in mačk.
>Tak model lahko vrne 2 vrednosti - mačka ali pes.

### Regresija

Vsak model, ki fukne ven **številko**.
Lahko fukne ven neskončno številk.

>Npr. koliko bo stala hiša in this current economy.

## Unsupervised learning

Nimamo rešitve, računalniku rečemo, naj reši problem. Npr. rečemo mu,
da naj zmaga igro šaha.

## Reinforcment learning

Npr. game AI, robot navigation...
Zakomplicirano in ne bomo delal.
