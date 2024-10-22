# Podatkovno rudarjenje po CRISP-DM standardu

*CRISP-DM* je **cross industry standard process for data mining**. Industrijski
standard, ki natančno določa potek analize podatkov s pomočjo podatkovnega
rudarjenja.

Je prosto dostopen procesni model, neodvisen od aplikacije/problema ter neodvisen od orodja/
programa. Osredotočen na poslovne probleme.

## Zakaj je treba proces standardizirati?

Podatkovno rudarjenje je **proces** , ki mora biti zanesljiv in ponovljiv.
To omogoča lažje planiranje in vodenje projektor. Novi uporabniki se lažje
uvedejo, če je proces standardiziran, torej odvisnost od *super-strokonjakov* 
ni tako velika (pomisli na Rust).

## Nastanek CRISP (standardizacije)

Med leti 1997-1999, pobuda s strani podjetij izkušenih v podatkovnem rudarjenju.
Leta 1999 izide CRISP-DM 1.0

## Faze CRISP-DM

### 1. Razumevanje problema

Kaj moramo naredit, kakšne cilje imam, kako bomo dobili podatke... definicija
problema

- določiti cilj projekta
- oceniti trenutno situacijo
- določiti cilje podatkovnega rudarjenja
- narediti projektni plan

### 2. Razumevanje podatkov

Izbiranje in spoznavanje podatkov, vsi niso kvalitetni.

- zbiranje začetnih podatkov
- opisovanje podatkov
- raziskovanje podatkov
- preverjanje kakovosti podatkov

### 3. Priprava podatkov

Izbor tabel, atributov, primerov. Podatke očistimo in uredimo v pravi format.

- izbiranje kvalitetnih podatkov
- čiščenje podatkov
- sestavljanja in integriranje podatkov
- *formatiranje* podatkov

### 4. Modeliranje

Izbor ustreznih tehnik modeliranja in njihova aplikacija

- izbiranje tehnike modeliranja
- načrtovanje potek testiranja
- izgrajevanje modela
- ocena kakovosti modela

### 5. Evalvacija oz. ocena modelov

Ali smo s modeli zadovoljili potrebe problema? Kateri modeli ja, kateri ne...

- ocena rezultatov
- ocena celotnega procesa
- ??

### Predaja končnemu uporabniku

Dokumentacija modela, da je proces lahko ponovljiv ter predaja/implementacija
modela (production).

- planiranje predaje/implementacije
- spremljanje in vzdrževanje
- končno poročilo
- ocena uspeha projekta
