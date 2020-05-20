__ Project moneymaker __

Cilj projekta je provjeriti uspješnost neuronske mreže u predviđanju rezultata nogometnih utakmica.
Kao dataset su korištene utakmice engleskog Premier League-a od 2013 do 2019 godine što je ukupno oko 2400 utakmica. 
Ulaz u neuronsku mrežu sastojao se od koeficienata sa betstarsa i analize mišnjenja o utakmici s twittera. 
Za svaku utakmicu je prikupljeno 2000 tweetova u razdoblju tjedan dana prije utakmice na kojima je obavljena analiza sentimenta te je svaki tweet kalsificiran na skali subjektivnosti i polarnosti.
Sveukupno je analizirano preko pola milijuna tweetova. 
Neuronska mreža se može kladiti na 1, 2, x ,1x, 2x ili se može odlućiti ne kladiti na tu utakmicu.
Pošto cilj neuronske mreže nije bila najveća toćnost predviđanja rezultata nego najveći profit, za treniranje je korištena poseban loss funkcija foja mjeri profit.
Prosjećni profit na svim utakmicama je 4.5%. Ovaj rezultat je za ovako jednostavnu mrežu zadovoljavajuć i podudara se s očekivanjima.

Struktura mreže:
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         (None, 19)                0
_________________________________________________________________
dense_1 (Dense)              (None, 15)                300
_________________________________________________________________
dropout_1 (Dropout)          (None, 15)                0
_________________________________________________________________
dense_2 (Dense)              (None, 10)                160
_________________________________________________________________
dropout_2 (Dropout)          (None, 10)                0 
_________________________________________________________________
dense_3 (Dense)              (None, 6)                 66
=================================================================
Total params: 526
Trainable params: 526
Non-trainable params: 0
_________________________________________________________________


Najveći trenutni problem je što neuronska mreža često zapne u lokalnom minimumu zbog malog broja parametara (526 trenirajućih) koje nije moguće povećati zbog overfittinga.

