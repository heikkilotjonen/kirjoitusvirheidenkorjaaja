from trie import Trie
from distance import dl_distance

class SpellChecker:
    def __init__(self):
        self.trie = Trie()
        self.dl_distance = dl_distance
    
    def load_dictionary(self, word_list):
        for word in word_list:
            self.trie.insert(word)
    
    def is_correct(self, word):
        return self.trie.search(word)
    
    