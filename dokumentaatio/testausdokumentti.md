### **Testausdokumentti**

#### 

###### **Mitä**

Projektissa on suoritettu yksikkötestit luokille Spellchecker ja Trie pytestin avulla.



###### Spellchecker testit

Spellchecker testeissä on testattu metodit load\_dictionary, is\_correct ja suggest.



Metodi load\_dictionary testataan syöttämällä lista sanoja, ja varmistamalla, että kaikki sanat ovat triessä.

Metodi load\_dicitonary\_from file testataan kirjoittamalla tiedostoon sanoja, lataamalla tiedosto spellcheckeriin ja varmistamalla, että spellchecker löytää sanat tiedostosta.

Metodi is\_correct testataan syöttämällä sana trie:hen ja etsimällä tämä sana, sekä muu sana joka ei ole trie:ssä.



Metodi suggest testataan syöttämällä kaksi Sanaa trie:hen, kirjoittamalla toinen sanoista hieman väärin, ja testaamalla, että oikea sanoista annetaan korjausehdotukseksi.



###### **Trie testit**

Metodi insert testataan syöttämällä sana trie:hen ja etsimällä se.



Metodi search testataan syöttämällä sana trie:hen ja etsimällä se ja toinen sana jota ei ole syötetty.




###### **Damerau-Levenchstein testit**
Damerau-Levenschtein etäisyyttä on testattu kaikilla operaatioilla tilanteissa, joissa operaatioita on täyty käyttää kahden siirron verran. Testauksia on tehty vain kahteen siirtoon asti, koska sovellus ottaa huomioon ehdotuksissa vain tapauksia, joissa etäisyys on 2 tai vähemmän.

###### **Invarianttitestaus**
Invarianttitestauksella testataan testissä test_suggest_random_words, että saadut ehdotukset ovat oikeasti sanakirjan sanoja. Testi luo random generoituja sanoja ja sanat syötetään suggest metodiin. Saadut ehdotukset verrataan sanakirjan sanoihin.

###### **Suorituskyky testit**
Suorituskykyä testataan testaamalla kuinka nopeasti korjaaja antaa sanaehdotuksia.
Saatiin 1 ehdotusta sanalle 'kammioves' 2.2289 sekunnissa.
Saatiin 5 ehdotusta sanalle 'koir' 1.8511 sekunnissa.
Saatiin 5 ehdotusta sanalle 'oikes' 1.6832 sekunnissa.


###### **Testikattavuusreportti**

Name                        Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------
distance.py                    14      0     12      0   100%
spellcheck.py                  18      0      4      0   100%
tests\__init__.py               0      0      0      0   100%
tests\distance_test.py         43      0      0      0   100%
tests\performance_test.py      13      9      2      1    33%   6-11, 16-18
tests\spellcheck_test.py       40      1      2      1    95%   50
tests\trie_test.py             19      0      0      0   100%
trie.py                        46      0     20      1    98%   50->54
-----------------------------------------------------------------------
TOTAL                         193     10     40      3    94%