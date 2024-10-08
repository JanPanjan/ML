# Klasifikacija

## ZeroR - zero rules

Algoritem, ki predvide katera izmed dveh možnosti je bolj verjetna,
da se zgodi. Glej *weather data set*.

Noben atribut ne vzame kot vir za svoj odgovor. V splošnem ni uporaben.

## OneR - one rule

Za razliko od ZeroR se odloči glede na neke atribute. Odloči se glede
ne en stolpec. Prešteje class za vsako vrednost in vzame tisto, ki se
večkrat pojavi.

Vseeno ni pravilnega stolpca za izbrat v tem modelu. Moraš it čez vse
stolpce in pogledat napake, ki jih bodo imeli. Ponavadi tisti, ki imajo
več različnih vrednosti, imajo manjšo napako.

Uporaben (morda) v okolju, kjer imaš zelo omejen computing power, npr.
na neki mali napravci. Ampak je preveč enostaven za kompleksne real-life
rešitve.

### Kako model predvidi odgovor

Prešteje yes in no v vrstici od stolpcev in spet vzame tisto, ki se
večkrat pojavi.
