## Klasifikacija

Klasifikator je nek model, ki ga zgradimo z uporabo že klasificiranih primerov, ki ga
uporabimo za klasifikacijo novih primerov. Spada v nadzorovano učenje (vrednosti primerov,
na katerih se uči, so poznane).

Klasifikator je lahko množica pravil, odločitveno drevo, nevronska mreža...

## Klasificijski algoritmi

Izbira algoritma je odvisna od podatkov - ne obstaja *generični* najboljši algoritem.

### 0R

Ne upošteva atributov, pogleda samo class stolpec. Predpostavlja se, da je spremenljivka, ki jo
napovedujemo, nominalnega tipa. Lahko si predstavljaš kot osnova za ostale klasifikatorje.

Pogleda koliko primerov ima + in koliko - => napove tisto class vrednost, katere je več :3.

> $80 \ %$ yes in $20 \ %$ no $\implies$ yes (!!)

### 1R

Gleda atribut po atribut in se odloči nekaj. Manjkajoče vrednosti upošteva kot ločene vrednosti
atributa.

#### Nominalni atributi

Primer z weather podatki. Predpostavlja, da so vsi atributi nominalni. Imamo *outlook, temp,
humidity, windy* in class razred *play*. Algoritem gleda vsak atribut posebej in ga razbije
na tri podmnožice - sunny, rainy, overcast. Gleda vsako vrednost in prešteje yes in no iz play.

> weather dataset: sunny;yes = 3, sunny;no = 2 - rainy;yes = 3, rainy;no = 2, overc;yes = 4, 
> overc;no = 0

Za sunny je več yes kot no, zato bo izbral yes - naredi napako $2/5$, ker 2 od vseh sta no... Za
overcast je yes 4x in no 0x, zato izbere yes - ne naredi napake. Za rainy enako kot sunny, samo da 
izbere no.

Napake seštejemo in dobimo **skupno napako** $4/15$ atributa. Izberemo tisti atribut, ki ima **naj-
manjšo napako** (ta primer outlook ali humidity).

Zdaj se za outlook odloči tako: sunny = yes, rainy = no, overcast = yes. **To je naš model.**

#### Numerični atributi

Za numerične atribute naredi 1R razredno diskretizacijo - binning in jih enako primerja kot prej,
samo da so vrednosti zdaj bins.

### Bayes-ovo statistično modeliranje in Naivni Bayes

Nasprotno od 1R, upoštevajo se vsi atributi. Predpostavlja, da so atributi enako pomembni in
statistično neodvisni (predpostavka neodvnisnosti skoraj nikoli ne drži), zato nam da soliden
klasifikator in je včasih kar točen.

Algoritem deluje boljše za neko podmnožico atributov, saj veliko enakih atributov(..) manjša
točnost izračunov. Izbrati moramo samo *najboljše vrednosti*. (not sure about this)

#### Nominalni atributi

Primer z weather podatki: prešteje frekvence in ustvari tabelo iz podatkov, ki je kombinacija vseh
vrednosti atributa in vseh class vrednosti. Enako kot prej sunny 2 in 3, rainy 3 in 2, overcast 4
in 0. To naredi za vsak atribut. Za vsak atribut prešteje frekvence tudi za play.

Nato naredi tabelo verjetnosti, ki izračuna delež sunny yes od vseh yes v play - $2/9$; za class
atribut pa $9/14$ (play ima 14 vrstic).

Napoved se zgodi tako, da poračuna verjetnosti za vsak razred. Gleda eno vrstico in vrednost za
vsak atribut - sunny, cool, high, true, ? (play). Za yes in no vrednosti poračuna verjetnosti
koliko je za vsako vrednost atributa verjetno da ima yes ali no (damn).

Npr. za yes $= 2/9 \times 3/9 \times ...$ in vrne večjo vrednost med yes in no.

##### Popravljanje atributov

**Problem ničte verjetnosti** - primer no:outlook:overcast = 0, kar pomeni, da bi končni izračun bil
enak 0 samo zaradi tega. Tega se izognemo tako, da vsem verjetnosti prištejemo ena. Tako ohranimo
razmerje med verjetnostmi in se izognimo 0 (ali missing data... :o not really).

##### Manjkajoče vrednosti

Pri učenju ne upoštevamo manjkajočih vrednosti v tabeli frekvenc. Pri klasifikaciji atributa ne
upoštevamo pri izračunu verjetnosti.

> Npr. outlook ima null, zato njegove verjetnosti ne dodamo v končni produkt.

#### Numerični atributi

Običajna predpostavka: atributi imajo normalno (Gaussovo) verjetnostno porazdelitev glede na razred.
Glej funkcijo za gostoto verjetnosti za normalno porazdelitev. Z njo dobimo verjetnost za neko
numerično vrednost.

Glej prosojnice (rumena tabela).

## Odločitvena drevesa (TDIDT)

Tako kot prejšnji omogočajo analizo vseh možnih podatkov. Drevo se gradi od zgoraj navzdol. 
Prednost: v vsakem koraku znamo izbrazi najbolši atribut za delitev podatkov. Z delitvami
delamo disjunktne množice.

Notranje vozlišče predstavja test po atributu. Veja je rezultat primerjave npr. "color=red".

Glej prosojnice za graf.

Odločitvena drevesa želimo graditi tako, da so množice čimbolj *čiste*.

### Izbor atributa za delitev drevesa

V vsakem vozlišču uporabimo funkcijo primernosti, ki oceni razpoložjive atribute glede na nijigovo soposonost delitve primerov na *čiste*  podmnoožice.

- ID3
- C4.5
- CART

#### ID3 - Informacijski prispevek

Kako izberemo atribut, ki bo v root: narišemo drevo za vsak atribut. Izberemo tistega, ki privodi
do najmanjšega drevesa. Informacijska čistost je ta vrednost, ki jo iščemo. Hočemo čim manjšo
entropijo. Lahko si prestavljaš, da ima vsak atribut nek dogodek, ki se bo zgodil, če bo npr. sunny yes ali pa sunny no. Entropijo izračunamo iz verjetnosti teh dogodkov.

> `-` je v enačbi, da se obrne negativna vrednost, ki pride kot rezultat enačbe 
> (nariši graf za log).

Čim so vrednosti enega atributa enako, rečemo, da je entropija enaka 0... i think. S pomočjo 
entropije izračunamo **informacijski prispevek**.

Primer za outlook: fuknemo not verjetnosti in dobimo neko število bitov. Ko dobimo vse uteži, jih
množimo z verjetnostjo, da je sunny yes ali no itn. Na koncu zračunamo razliko in dobimo
informacijski prispevek.

Dobimo 4 vrednosti (vsak atribut ena vrednost) in jih primerjamo med sabo. Tisti, ki ima največjo,
je najboljši za root, nato pa ponovimo za vsako poddrevo vse korake.

#### C4.5

Algoritem zna primerjati tudi numerične vrednosti, kar ID3 ne more.

#### CART - Gini indeks

Dobimo gini indekse za vsako množico in izberemo atribut z **najmanjšim gini indeksom**, ki je
najboljši.
