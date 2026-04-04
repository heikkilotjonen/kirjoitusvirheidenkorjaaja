### **Testausdokumentti**

#### 

###### **Mitä**

Projektissa on suoritettu yksikkötestit luokille Spellchecker ja Trie pytestin avulla.



###### Spellchecker testit

Spellchecker testeissä on testattu metodit load\_dictionary, is\_correct ja suggest.



Metodi load\_dictionary testataan syöttämällä lista sanoja, ja varmistamalla, että kaikki sanat ovat triessä.



Metodi is\_correct testataan syöttämällä sana trie:hen ja etsimällä tämä sana, sekä muu sana joka ei ole trie:ssä.



Metodi suggest testataan syöttämällä kaksi Sanaa trie:hen, kirjoittamalla toinen sanoista hieman väärin, ja testaamalla, että oikea sanoista annetaan korjausehdotukseksi.



###### **Trie testit**

Metodi insert testataan syöttämällä sana trie:hen ja etsimällä se.



Metodi search testataan syöttämällä sana trie:hen ja etsimällä se ja toinen sana jota ei ole syötetty.



Metodi get\_all\_words testataan erikseen ilman etuliitettä, sekä väärällä ja oikealla etuliitteellä. Trie:hen syötetään sanoja ja niitä etsitään etuliitteen kanssa ja ilman.



###### **Testikattavuusreportti**

Name                           Stmts   Miss Branch BrPart  Cover   Missing

\--------------------------------------------------------------------------

src\\distance.py                   12      0     10      0   100%

src\\spellcheck.py                 19      0      6      0   100%

src\\tests\\\_\_init\_\_.py              0      0      0      0   100%

src\\tests\\spellcheck\_test.py      20      0      0      0   100%

src\\tests\\trie\_test.py            34      0      0      0   100%

src\\trie.py                       35      0     16      0   100%

\--------------------------------------------------------------------------

TOTAL                            120      0     32      0   100%

