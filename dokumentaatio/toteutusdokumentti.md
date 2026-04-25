# Toteutusdokumentti

## Yleisrakenne
Työ on Pythonilla tehty kirjotusvirheidenkorjaaja. Ohjelma käyttää Trie tietorakennetta säilömään sanakirjan. Käyttäjä syöttää sanoja, ja ohjelma tarkistaa ovatko sanat sanakirjassa. Jos sana ei ole, ohjelma etsii onko sanakirjassa sanoja jotka ovat lähellä väärinkirjoitettua sanaa. Damerau-Levenshtein etäisyyttä käytetään laskemaan väärinkirjoitetun sanan etäisyys oikeaan sanaan.

## Laajojen kielimallien käyttö
Käytin Claude Sonnettia ennen työn aloitusta hahmottamaan ohjelman mahdollisen yleisrakenteen. Koodaamisessa käytin apuna vscoden agenttia.

Käytin myös Claude Sonnettia apuna luomaan koodia, joka generoi lib-voikon avulla valmiin sanakirjan sanoista taivutusmuodot.

## Lähteet
https://www.geeksforgeeks.org/dsa/damerau-levenshtein-distance/
https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
https://en.wikipedia.org/wiki/Trie