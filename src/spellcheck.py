from trie import Trie
from distance import dl_distance

class SpellChecker:
    def __init__(self):
        self.trie = Trie()
        self.dl_distance = dl_distance              
    
    def load_dictionary(self, word_list):                       # Lataa sanalista trie-rakenteeseen
        for word in word_list:
            self.trie.insert(word)
    
    def is_correct(self, word):                                 # Tarkistaa onko sana oikein kirjoitettu
        return self.trie.search(word)
    
    def suggest(self, word, max_suggestions=5):                 # Ehdottaa korjauksia väärin kirjoitetulle sanalle
        suggestions = []
        for candidate in self.trie.get_all_words():             # Käy läpi kaikki sanalistassa olevat sanat
            distance = self.dl_distance(word, candidate)        # Laskee editointietäisyyden
            if distance <= 2:                                   # Jos etäisyys on 2 tai vähemmän, lisätään ehdotuksiin
                suggestions.append((candidate, distance))
        
        suggestions.sort(key=lambda x: x[1])                    # Järjestetään ehdotukset etäisyyden mukaan
        return [suggestion[0] for suggestion in suggestions[:max_suggestions]]    # Palautetaan vain parhaat ehdotukset
    
    
    
    