==========================
----- TABELA DELEŽEV -----
==========================

ima frekvenčno tabelo in tabelo, kjer so deleži frekvenc. kaj to pomeni:

	obstaja 9 "yes" in 5 "no". "sunny" ima 2x "yes" in 3x "no". "sunny" pripomore h
	deležu od "yes" 2/9 in h "no" 2/5. prav tako imamo deleže za class atribut.
	"yes" je 9/14 in "no" 5/14.

=========================
----- NAPOVEDOVANJE -----
=========================

temelji na deležih vrednosti. primer:

	outlook, temp, humidity, windy, play
	sunny, 	 cool, high,     true,  (?)

	vrednost "yes" in "no" napove preko deležev. deleže za vsako vrednost
	množi med sabo, da dobi *verjetje* (likelyhood) razreda:

		  sunny cool  high  true  yes
	yes = 2/9 × 3/9 × 3/9 × 3/9 × 9/14 = 0,0053
	no  = 3/5 × 1/5 × 4/5 × 3/5 × 5/14 = 0,0206

	v verjetnost pretvori tako, da normalizira vrednosti z enačbo:

		verjetnost(yes) = verjetje_yes / (verjetje_yes + verjetje_no)
		P(yes) =          0,0053       / (0,0053       + 0,0206) = 0,205
		P(no) =           0,0206       / (0,0053       + 0,0206) = 0,795

============================
----- BAYESOVO PRAVILO -----
============================

Verjetnost dogodka H pri poznanih dejstvih E: P[H] je verjetnost hipoteze
preden poznamo dejstva (a priori), P[H|E] je verjetnost hipoteze, ko poznamo
dejstva (a posteriori).

	P[H|E] = P[E|H] × P[H]
	         -------------
	              P[E]

Hočemo izvedeti *kakšna je verjetnost razreda (class) pri poznanih verjetnostih
vrednosti ostalih atributov primera (sunny, cool,...)*.

	- E: dejstva, vrednosti atributov
	- H: hipoteza, vrednost razreda pri podanih vrednostih

Naivni Bayes, ker model predpostavlja, da so verjetnosti atributov neodvisne
med seboj; zaradi te predpostavke, razdelimo dejstva E na dele:

	P[H|E] = P[E1|H] × P[E2|H] × P[E3|H] × ... × P[En|H] × P[H]
		     --------------------------------------------------
			                 P[E]

	outlook, temp, humidity, windy, play
	sunny, 	 cool, high,     true,  (?)  <=== dejstva E

	verjetnost razreda yes
	    |
	    |
	    v
	P["yes"|E] = P[outlook = "sunny" | "yes"] ×
				 P[temperature = "cool" | "yes"] ×
				 P[humidity = "high" | "yes"] ×
				 P[windy = "true" | "yes"] ×
				 P["yes"] / P[E]

				= 2/9 × 3/9 × 3/9 × 3/9 × 9/14
				  ----------------------------
						      P[E]

----- NIČELNE FREKVENCE -----

Verjetnost bo enaka 0, če ima neka določena vrednost frekvenco 0 za nek
class value (npr. P[humidity = high | yes] = 0). Zaradi tega vsem
frekvencam v tabeli frekvenc doda 1 - verjetnosti ne bodo nikoli 0.

Včasih je boljše dodati kako drugo vrednost kot 1, saj se natančnost manjša
glede na velikost verjetnosti AL NEKAJ TAKEGA (do not quote me on this). 
Ni nujno da so uteži enako, le njihova vsota mora biti vedno enaka 1 (saj 
delamo z verjetnostjo).

----- MANJKAJOČE VREDNOSTI -----

Teh ne upošteva pri izračunu frekvenc v tabeli frekvenc in pri klasifikaciji
ne upešteva za izračun verjetij.
