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



Metodi get\_all\_words testataan erikseen ilman etuliitettä, sekä väärällä ja oikealla etuliitteellä. Trie:hen syötetään sanoja ja niitä etsitään etuliitteen kanssa ja ilman.

###### **Invarianttitestaus**
Invarianttitestauksella testataan testissä test_suggest_random_words, että saadut ehdotukset ovat oikeasti sanakirjan sanoja. Testi luo random generoituja sanoja ja sanat syötetään suggest metodiin. Saadut ehdotukset verrataan sanakirjan sanoihin.



###### **Testikattavuusreportti**

Name                           Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------------
src\distance.py                   14      0     12      0   100%
src\spellcheck.py                 24      0      8      0   100%
src\tests\__init__.py              0      0      0      0   100%
src\tests\spellcheck_test.py      37      1      2      1    95%   46
src\tests\trie_test.py            34      0      0      0   100%
src\trie.py                       35      0     16      0   100%
--------------------------------------------------------------------------
TOTAL                            144      1     38      1    99%