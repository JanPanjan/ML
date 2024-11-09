==========================
----- TABELA DELEŽEV -----
==========================

frekvenčno tabelo imamo, potrebujemo še (mogoče) tabelo, kjer bodo deleži
frekvenc. kaj to pomeni:

	obstaja 9 "yes" in 5 "no". "sunny" ima 2x "yes" in 3x "no". "sunny" pripomore h
	deležu od "yes" 2/9 in h "no" 2/5. prav tako imamo deleže za class atribut.
	"yes" je 9/14 in "no" 5/14.

=========================
----- NAPOVEDOVANJE -----
=========================

temelji na teh deležih. primer:

	outlook, temp, humidity, windy, play
	sunny, 	 cool, high,     true,  (?)

	vrednost "yes" in "no" napovemo preko deležev. deleže za vsako vrednost
	množimo med sabo, da dobimo *verjetje* (likelyhood) razreda:

		  sunny cool  high  true  yes
	yes = 2/9 × 3/9 × 3/9 × 3/9 × 9/14 = 0,0053
	no  = 3/5 × 1/5 × 4/5 × 3/5 × 5/14 = 0,0206

	v verjetnost pretvorimo tako, da normaliziramo vrednosti z enačbo:

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
	P["yes"|E] = P[outlook = "sunny" |"yes"] ×
 		     P[temperature = "cool" |"yes"] ×
		     P[humidity = "high" |"yes"] ×
		     P[windy = "true" |"yes"] ×
		     P["yes"] / P[E]

	           = 2/9 × 3/9 × 3/9 × 3/9 × 9/14
		     ----------------------------
		                 P[E]
