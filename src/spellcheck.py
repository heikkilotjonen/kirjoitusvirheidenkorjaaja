from trie import Trie


class SpellChecker:
    def __init__(self):
        self.trie = Trie()

    # Lataa sanalista trie-rakenteeseen
    def load_dictionary(self, word_list):
        for word in word_list:
            self.trie.insert(word)

    # Lataa sanalista tiedostosta trie-rakenteeseen
    def load_dictionary_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                self.trie.insert(word)

    # Tarkistaa onko sana oikein kirjoitettu
    def is_correct(self, word):
        return self.trie.search(word)

    # Ehdottaa korjauksia väärin kirjoitetulle sanalle
    def suggest(self, word, max_suggestions=5):
        # Haetaan kaikki sanat Triesta, joiden edit distance on enintään 2
        suggestions = self.trie.find_similar_words(word, max_distance=2)
        
        # Järjestetään ehdotukset etäisyyden mukaan
        suggestions.sort(key=lambda x: x[1])
        # Palautetaan vain parhaat ehdotukset
        return [suggestion[0] for suggestion in suggestions[:max_suggestions]]
