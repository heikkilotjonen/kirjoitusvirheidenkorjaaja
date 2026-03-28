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

    def get_all_words(self, prefix=""):             # Hakee kaikki trie:ssä olevat sanat
        node = self.root
        for char in prefix.lower():                 # Käy läpi etuliitteen merkit
            if char not in node.children:
                return []
            node = node.children[char]              # Siirrytään seuraavaan solmuun
        results = []
        self._dfs(node, prefix.lower(), results)    # Syvyyssuuntainen haku trie:ssä
        return results

    def _dfs(self, node, prefix, results):          # Apumetodi syvyyssuuntaiseen hakuun
        if node.is_word:                            # Jos solmu on sanan loppu, lisätään se tuloksiin
            results.append(prefix)
        for char, child in node.children.items():   # Käydään läpi lapsisolmut rekursiivisesti
            self._dfs(child, prefix + char, results)
