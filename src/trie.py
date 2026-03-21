class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word):                         # Lisää sana trie:hen
        node = self.root
        for char in word.lower():                   # Käy läpi sanan merkit
            if char not in node.children:           # Jos merkki ei ole lapsissa, luodaan uusi solmu
                node.children[char] = TrieNode()
            node = node.children[char]              # Siirrytään seuraavaan solmuun
        node.is_word = True

    def search(self, word):                         # Tarkistaa, onko trie:ssä sana
        node = self.root
        for char in word.lower():                   # Käy läpi sanan merkit
            if char not in node.children:           # Jos merkki ei ole lapsissa, palautetaan False
                return False
            node = node.children[char]              # Siirrytään seuraavaan solmuun
        return node.is_word
