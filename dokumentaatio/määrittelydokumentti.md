Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti

Aihe
Projektin aiheena on kirjoitusvirheiden korjaaja. Ohjelma tulee ottamaan merkkijonoja syötteenä ja tarkastaa ne mahdollisten kirjoitusvirheiden varalta. Kirjoitusvirheet tarkistetaan vertaamalla niitä trie-tietorakenteeseen tallennettuihin sanoihin Damerau-Levenchstein -etäisyyttä hyödyntäen. Ohjelma on tarkoitettu toimivaksi vain suomen kielellä.

Ydin
Harjoitustyön ydin on kirjoitusvirheitä korjaavan algoritmin toteuttaminen. Korjausehdotukset haetaan Damerau-Levenchstein -etäisyyttä hyödyntäen.

Ohjelmointikieli
Toteutan projektin Pythonilla ja olen valmis vertausarvioimaan vain muita Python projekteja.

Aikavaativuus
Trie-tietorakenteesta haku, poisto ja lisäys onnistuvat O(m) ajassa toimivalla algoritmilla, jossa m on parametriksi annetun merkkijonon avaimen koko. Korjausehdotuksia antava Damerau-Levenchstein -etäisyys toimii O(M * N * max(M, N)) ajassa.

Lähteet
Trie-tietorakenne:
https://en.wikipedia.org/wiki/Trie

Damerau-Levenchstein -etäisyys:
https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
https://www.geeksforgeeks.org/dsa/damerau-levenshtein-distance/
